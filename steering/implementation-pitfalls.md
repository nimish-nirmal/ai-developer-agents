# Implementation Pitfalls

This document captures recurring implementation mistakes identified through code review. Apply these rules to every implementation regardless of domain or feature.

---

## 1. Never Mutate Objects After Storing References

Pushing an object into an array and then modifying it mutates the stored reference, creating inconsistent state between what was stored and what was intended.

**Bad:**
```typescript
items.push(item);
item.status = 'inverted'; // mutates the stored reference
```

**Good:**
```typescript
const updated = { ...item, status: 'inverted' };
items[items.length - 1] = updated; // replace, don't mutate
```

**Rule**: After pushing an object to an array or assigning it to a variable, treat it as immutable. Create a new object for any modifications.

---

## 2. Complete All Field Mappings When Bridging Two Schemas

When mapping from one schema to another, explicitly map every field that downstream consumers need. Missing a field causes silent failures.

**Checklist before finishing a schema mapping:**
- List all fields the destination type requires
- Verify each is present in the mapping function
- Check all callers of the mapped object to find what fields they access
- Add a test that accesses every field on the mapped result

---

## 3. Time-Windowed Rate Limits Must Include the Window in the Key

Using `if_not_exists` for TTL on a rate limit counter means the TTL is only set on the first write and never updated. The counter persists beyond its intended window.

**Bad:**
```typescript
Key: { id: `RATELIMIT#${resourceId}` }
UpdateExpression: 'SET #count = if_not_exists(#count, :zero) + :one, #ttl = if_not_exists(#ttl, :ttl)'
```

**Good:**
```typescript
const windowStart = Math.floor(now / 1000 / windowSeconds) * windowSeconds;
Key: { id: `RATELIMIT#${resourceId}#${windowStart}` }
UpdateExpression: 'SET #count = if_not_exists(#count, :zero) + :one, #ttl = :ttl'
```

**Rule**: For any time-windowed counter, include the window boundary in the key.

---

## 4. DynamoDB Composite Keys Require All Key Attributes in Conditions

When a table has a composite primary key (PK + SK), a ConditionExpression checking only one key attribute does not prevent overwrites from items with the same SK but a different PK.

**Bad:**
```typescript
ConditionExpression: 'attribute_not_exists(sortKey)' // only checks SK
```

**Good:**
```typescript
ConditionExpression: 'attribute_not_exists(partitionKey) AND attribute_not_exists(sortKey)'
```

**Rule**: Always include all key attributes in uniqueness conditions for composite-key tables.

---

## 5. Timezone Conversion — Use Intl.DateTimeFormat

`new Date(someDate.toLocaleString('en-US', { timeZone: tz }))` is unreliable.

**Bad:**
```typescript
const localTime = new Date(date.toLocaleString('en-US', { timeZone: timezone }));
const hour = localTime.getHours();
```

**Good:**
```typescript
const parts = new Intl.DateTimeFormat('en-US', {
  timeZone: timezone,
  hour: 'numeric', minute: 'numeric', hour12: false,
}).formatToParts(date);
const hour = parseInt(parts.find(p => p.type === 'hour')?.value ?? '0', 10);
```

**Rule**: Always use `Intl.DateTimeFormat.formatToParts()` for timezone-aware time extraction.

---

## 6. Empty Strings Are Not Zero — Guard Numeric Coercion

`Number("")` returns `0`, making empty strings appear numeric.

**Bad:**
```typescript
const bothNumeric = !isNaN(Number(actual)) && !isNaN(Number(expected));
```

**Good:**
```typescript
const actualStr = String(actual ?? '');
const expectedStr = String(expected ?? '');
const bothNumeric =
  actualStr.trim() !== '' && expectedStr.trim() !== '' &&
  !isNaN(Number(actualStr)) && isFinite(Number(actualStr)) &&
  !isNaN(Number(expectedStr)) && isFinite(Number(expectedStr));
```

**Rule**: Before treating a value as numeric, verify it is non-empty and finite.

---

## 7. Ownership Verification Before Data Access

Any handler that fetches data by ID must verify the authenticated user owns that resource.

**Checklist for every GET/LIST handler:**
- Extract user identifier from authorizer claims
- Either query with user identifier as part of the key, OR
- Fetch the resource and check resource owner matches requester

---

## 8. Wrap JSON.parse in try/catch — Always

`JSON.parse` throws on invalid input. Any code path that calls it with user-provided data must catch the error and return a meaningful response rather than crashing.

**Rule**: Every `JSON.parse` call must be wrapped in `try/catch`.

---

## 9. Don't Cache Time-Sensitive Computations

In-memory caches keyed by input parameters will return stale results for any computation whose output depends on the current time.

**Rule**: Any computation whose result changes over time must either be excluded from caching or include the current timestamp in the cache key.

---

## 10. Module-Level Shared Clients for Connection Reuse

Creating a new SDK client inside a service constructor that is called on every invocation prevents connection pooling and adds cold-start overhead.

**Bad:**
```typescript
export const handler = async (event) => {
  const service = new MyService(logger); // creates new client each invocation
};
```

**Good:**
```typescript
// Module-level — reused across warm invocations
const sharedClient = createSharedClient();

export const handler = async (event) => {
  const service = new MyService(logger, sharedClient); // injected
};
```

**Rule**: All services must accept optional injected clients. Handlers must create module-level shared clients and pass them in.

---

## 11. Validate Template Parameter Values Before Substitution

User-provided parameter values containing template syntax can chain into another substitution, injecting unintended content.

**Rule**: Before substituting any parameter value, validate it does not contain template placeholder syntax.

---

## 12. Never Substitute Empty String Defaults Into Configs

Optional parameters with an empty string default will substitute an empty string into the config, producing invalid IDs or broken values downstream.

**Rule**: Skip substitution for any parameter whose resolved value is empty string, null, or undefined.

---

## 13. GSI Composite Sort Keys Must Use Original Timestamps

When a GSI sort key is a composite of `{status}#{timestamp}`, using the current time at update time corrupts sort order.

**Rule**: Use the original timestamp, not the update time, in GSI composite sort keys.

# Version Control Standards

## Commit Standards - Conventional Commits

### Format Structure
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Required Types
- **feat**: New feature (correlates with MINOR in SemVer)
- **fix**: Bug fix (correlates with PATCH in SemVer)
- **BREAKING CHANGE**: Breaking API change (correlates with MAJOR in SemVer)

### Additional Types
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes bug nor adds feature
- **perf**: Performance improvement
- **test**: Adding/correcting tests
- **chore**: Build process or auxiliary tool changes
- **ci**: Continuous integration changes
- **build**: Build system changes

### Scope Guidelines
- Use parentheses: `feat(auth): add login validation`
- Derive from file path or affected component
- Keep scopes consistent within the project

### Description Rules
- Use imperative mood: "add feature" not "added feature"
- Keep first line under 50 characters when possible
- Don't capitalize first letter
- No period at the end

### Examples
```
feat(auth): add user authentication function
fix(utils): resolve incorrect date parsing
docs: update API documentation
refactor(components): simplify button component logic
perf(database): optimize query performance
test(auth): add integration tests for login flow
```

### Breaking Changes
- Use `!` after type/scope: `feat(api)!: change authentication method`
- Or use footer: `BREAKING CHANGE: authentication now requires API key`

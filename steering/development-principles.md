# Development Principles

## Core Philosophy
- **YAGNI (You Aren't Gonna Need It)**: The best code is no code. Don't add features we don't need right now
- **Simple over Clever**: We STRONGLY prefer simple, clean, maintainable solutions over clever or complex ones. Readability and maintainability are PRIMARY CONCERNS
- **Minimal Changes**: Make the SMALLEST reasonable changes to achieve the desired outcome
- **No Over-Engineering**: Don't over-engineer a solution when a simple one is possible

## Change Management
- **Concentrated Changes**: Make focused, related changes in single commits
- **No Unrelated Changes**: NEVER make code changes unrelated to your current task. If you notice something that should be fixed but is unrelated, document it rather than fixing it immediately
- **Ask Before Rewriting**: Ask permission before reimplementing features or systems from scratch instead of updating the existing implementation
- **Reduce Duplication**: Work hard to reduce code duplication, even if the refactoring takes extra effort

## Code Quality Standards
- **Match Existing Style**: Match the style and formatting of surrounding code, even if it differs from standard style guides. Consistency within a file trumps external standards
- **Preserve Comments**: NEVER remove code comments unless you can PROVE they are actively false. Comments are important documentation
- **Evergreen Comments**: Comments should describe the code as it is NOW, not what it used to do
- **No Temporal References**: NEVER refer to temporal context in comments or code
- **Value-Adding Comments**: Only include comments that explain WHY code exists or works a certain way, not WHAT it does

## Naming Conventions
- **Domain-Focused Names**: Names MUST tell what code does, not how it's implemented
- **No Historical Context**: NEVER use temporal/historical context in names
- **Avoid "New/Improved" Names**: If you name something "new" or "enhanced" or "improved", you've probably made a mistake

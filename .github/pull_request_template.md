## Development Mode

Which approach did you use for this change?

- [ ] **Vibe** — Code-first, tests after (cooking by feel)
- [ ] **TDD** — Tests-first, then implementation (cooking by scale)
- [ ] **Spec-Driven** — Spec first, tests from spec, then code (cooking by recipe)

## Description

<!-- Brief description of what this PR does -->

## Changes

<!-- List the key changes in this PR -->

- 
- 
- 

## Checklist: Save Yourself Later

### Before You Code
- [ ] **Write the bug before the fix** — This PR references an issue or has a clear problem statement
- [ ] **Know your mode** — I've chosen the right development approach for this task

### Before You Submit
- [ ] **Protect the risky lines** — New/changed code has test coverage
- [ ] **Edge cases considered** — Invalid input, boundary conditions, error paths
- [ ] **Behaviour over implementation** — Tests verify what the code does, not how

### Review Readiness
- [ ] **Label your mode** — Mode checkbox is marked above
- [ ] **Tests pass locally** — `make test` succeeds
- [ ] **Code is readable** — Functions are small, names are clear, docs exist

## Testing

<!-- How did you test this change? -->

```bash
# Commands you ran
make test-vibe
make test-tdd
make test-spec
```

## Notes for Reviewers

<!-- Anything specific you want reviewers to focus on? -->

---

**Remember**: Each mode has strengths. Vibe is fast, TDD catches regressions, Spec aligns teams. Pick the right tool for the job! 🎯


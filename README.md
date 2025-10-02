# Spec vs TDD vs Vibe: Three Parallel Implementations

This repository demonstrates three different development approaches for implementing the same tiny API feature: a POST `/price` endpoint that calculates prices with VAT and discount codes.

Based on the blog post: **"Coding by Vibe, by Tests, or by Spec — Which Hat Are You Wearing?"**

## The Feature

All three implementations provide:
- **Endpoint**: `POST /price`
- **Input**: `{"amount": float, "vat_pct": float, "code": string?}`
- **Business Logic**:
  - Apply VAT percentage first
  - Then apply 10% discount for code `"WELCOME10"` (case-insensitive)
  - Round to 2 decimal places
- **Output**: `{"final": float}`

**Example**: `{"amount": 100, "vat_pct": 20, "code": "WELCOME10"}` → `{"final": 108.0}`

## Three Modes, Three Philosophies

### 🎸 Vibe Mode (`vibe/`)
**Cooking by feel** - Fast, intuitive, relies on experience.

- Code first, tests after
- Trust your instincts and domain knowledge
- Great for prototyping and well-understood problems
- Risk: Missing edge cases until production

**Run**: `make run-vibe` → http://localhost:8000  
**Test**: `make test-vibe`

### 🔬 TDD Mode (`tdd/`)
**Cooking by scale** - Precise, repeatable, catches mistakes early.

- Tests first, then minimal implementation
- Red → Green → Refactor cycle
- Small, focused functions with clear behaviour
- Great for complex logic and regression prevention

**Run**: `make run-tdd` → http://localhost:8001  
**Test**: `make test-tdd`

### 📋 Spec-Driven Mode (`spec_driven/`)
**Cooking by recipe card** - Shared understanding, no surprises at review.

- Specification first (Gherkin feature file)
- Tests verify compliance with spec
- Implementation satisfies the contract
- Great for team alignment and stakeholder communication

**Run**: `make run-spec` → http://localhost:8002  
**Test**: `make test-spec`

## Quick Start

### Installation

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make install
# or: pip install -e .
```

### Running Tests

```bash
# All tests
make test

# Individual modes
make test-vibe
make test-tdd
make test-spec

# With coverage
make coverage
```

### Running the Apps

Each mode runs on a different port so you can try them all:

```bash
# Vibe mode (port 8000)
make run-vibe

# TDD mode (port 8001)
make run-tdd

# Spec-driven mode (port 8002)
make run-spec
```

### Try It Out

```bash
# Test any running app
curl -X POST http://127.0.0.1:8000/price \
  -H "Content-Type: application/json" \
  -d '{"amount":100,"vat_pct":20,"code":"WELCOME10"}'

# Expected response
{"final":108.0}

# Without discount code
curl -X POST http://127.0.0.1:8000/price \
  -H "Content-Type: application/json" \
  -d '{"amount":100,"vat_pct":20}'

# Expected response
{"final":120.0}
```

## Project Structure

```
├── src/
│   └── dev_modes/           # Source package
│       ├── vibe/            # Vibe mode implementation
│       │   ├── calculator.py
│       │   └── app.py
│       ├── tdd/             # TDD mode implementation
│       │   ├── calculator.py
│       │   └── app.py
│       └── spec_driven/     # Spec-driven implementation
│           ├── calculator.py
│           └── app.py
├── vibe/tests/              # Vibe mode tests (written after)
├── tdd/tests/               # TDD tests (written first)
├── spec_driven/
│   ├── specs/
│   │   └── price.feature    # Gherkin specification
│   └── tests/               # Spec compliance tests
├── .github/
│   ├── workflows/
│   │   └── ci.yml           # CI pipeline
│   └── pull_request_template.md
├── pyproject.toml           # Dependencies and config
├── Makefile                 # Task runner
└── README.md
```

## Which Mode Should You Use?

### Use Vibe Mode When:
- ✅ Prototyping or spike work
- ✅ The problem domain is well-understood
- ✅ You're working solo on a tight deadline
- ⚠️  But watch out for missing edge cases

### Use TDD Mode When:
- ✅ Building complex business logic
- ✅ Regression prevention is critical
- ✅ You want confidence in refactoring
- ⚠️  But don't let perfect be the enemy of good

### Use Spec-Driven Mode When:
- ✅ Multiple stakeholders need alignment
- ✅ The feature has unclear requirements
- ✅ You want a living contract for the code
- ⚠️  But avoid over-specifying implementation details

## Common Edge Cases to Consider Later

All three implementations handle the happy path, but production code should consider:

- **Invalid input**: Negative amounts, crazy VAT percentages (>100%)
- **Malformed JSON**: Missing required fields, wrong types
- **Code length limits**: What if someone sends a 10,000 character code?
- **Locale**: Should rounding use banker's rounding? Locale-specific formatting?
- **Concurrency**: Multiple discount codes? Stackable discounts?
- **Audit**: Should we log price calculations for compliance?

## CI/CD

GitHub Actions workflow runs on push and PR:
- Pytest with coverage
- Checks all three modes
- See `.github/workflows/ci.yml`

## Development Guidelines

When submitting PRs, use the template to indicate which mode you're working in:
- [ ] Vibe
- [ ] TDD  
- [ ] Spec-Driven

And remember the guardrails:
- **Write the bug before the fix**: Reference an issue
- **Protect the risky lines**: Aim for high diff coverage
- **Label your mode**: Help reviewers understand your approach

## License

MIT

## Credits

Inspired by the blog post "Coding by Vibe, by Tests, or by Spec, Which Hat Are You Wearing?"


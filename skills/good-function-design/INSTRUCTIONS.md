# Good Function Design

This skill guides you through writing Python functions that are small, readable, and easy to test. Apply these principles whenever you write a new function, refactor an existing one, or review code for function quality.

---

## Core principles

### 1. One function, one responsibility

A function should do exactly one thing. If you can describe a function with the word "and" — "it validates the input **and** saves it to the database **and** sends an email" — it is doing too much. Extract each responsibility into its own named function.

### 2. Keep functions small

Aim for functions under 20 lines of code. Shorter functions are easier to understand, easier to name accurately, and easier to test. If a function grows beyond 20 lines, ask yourself: can I extract a meaningful sub-step into its own function?

### 3. Use descriptive, verb-phrase names

Function names should describe what the function does, using a verb phrase:
- `calculate_total_price()` — not `total()` or `calc()`
- `validate_email_address()` — not `check()` or `email()`
- `fetch_user_by_id()` — not `get()` or `user()`

The name should be precise enough that a reader does not need to read the body to understand what the function does.

### 4. Explicit parameters, no hidden state

All inputs to a function should appear as parameters. A function should not silently read from global state, module-level variables, or instance attributes unless that is the intended design.

**Bad:**
```python
def calculate_discount():
    return PRICE * DISCOUNT_RATE  # reading globals silently
```

**Good:**
```python
def calculate_discount(price: float, discount_rate: float) -> float:
    return price * discount_rate
```

Explicit parameters make the function's dependencies visible. They make it easy to test the function with different inputs.

### 5. Explicit return values

Always return a value explicitly with a `return` statement. Avoid relying on implicit `None` returns. Use type hints to document what the function returns.

```python
def find_user(user_id: int) -> Optional[User]:
    ...
    return user  # or return None
```

### 6. Write docstrings

Every public function should have a docstring that explains:
- What the function does (one sentence)
- Parameters and their types (if not obvious from type hints)
- Return value
- Any exceptions raised

```python
def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate the discounted price.

    Args:
        price: The original price in dollars.
        discount_rate: The discount as a decimal (e.g., 0.1 for 10%).

    Returns:
        The price after applying the discount.
    """
    return price * (1 - discount_rate)
```

### 7. Aim for pure functions

A pure function always produces the same output for the same input, and has no side effects. Pure functions are the easiest to test — you just call them and check the return value.

Prefer pure functions. When a function must have side effects (writing to a file, sending an email, updating a database), make the side effects explicit and intentional.

### 8. Avoid mutable default arguments

Never use mutable objects (lists, dicts) as default parameter values in Python. They are shared across all calls.

**Bad:**
```python
def append_item(item, collection=[]):
    collection.append(item)
    return collection
```

**Good:**
```python
def append_item(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection
```

---

## Step-by-step refactoring process

When you have a function that needs improvement:

1. **Identify responsibilities.** List every distinct thing the function does. Each item on the list is a candidate for extraction.
2. **Name each responsibility.** Give each extracted function a clear verb-phrase name.
3. **Extract one at a time.** Extract one responsibility, test it, then move to the next.
4. **Add type hints.** Add parameter and return type annotations.
5. **Write or update docstrings.** Ensure each function is self-documenting.
6. **Write a unit test.** Verify that the extracted function works correctly in isolation.

---

## Common mistakes to avoid

- **God functions**: Functions that span hundreds of lines and do everything. Break them up.
- **Ambiguous names**: `process()`, `handle()`, `do_stuff()`. These convey nothing. Use specific names.
- **Boolean parameters that flip behavior**: `def save(data, overwrite=True)` — consider two separate functions instead.
- **Returning inconsistent types**: A function that sometimes returns a string and sometimes returns `None` without clear intent. Use `Optional[str]` and document it.
- **Side effects buried in the middle of logic**: If a function validates, then makes an API call, then logs, make the API call and logging explicit or separate.

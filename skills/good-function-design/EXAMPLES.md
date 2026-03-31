# Examples: Good Function Design

---

## Example 1: Splitting a multi-responsibility function

### Before (without this skill)

```python
def process_order(order_id, db, emailer):
    # Fetch order
    order = db.query(f"SELECT * FROM orders WHERE id = {order_id}")
    if not order:
        return None

    # Calculate total
    total = 0
    for item in order["items"]:
        price = item["price"]
        qty = item["quantity"]
        if item.get("discount"):
            price = price * (1 - item["discount"])
        total += price * qty

    # Apply tax
    tax = total * 0.08
    total_with_tax = total + tax

    # Save to DB
    db.execute(f"UPDATE orders SET total = {total_with_tax} WHERE id = {order_id}")

    # Send confirmation email
    emailer.send(order["customer_email"], f"Your order total is ${total_with_tax:.2f}")

    return total_with_tax
```

### After (with this skill applied)

```python
def fetch_order(order_id: int, db) -> Optional[dict]:
    """Retrieve an order from the database by ID."""
    return db.query("SELECT * FROM orders WHERE id = ?", [order_id])


def calculate_item_price(item: dict) -> float:
    """Calculate the final price for one order item, applying any discount."""
    price = item["price"]
    if item.get("discount"):
        price = price * (1 - item["discount"])
    return price * item["quantity"]


def calculate_order_subtotal(items: list) -> float:
    """Sum the prices of all items in an order."""
    return sum(calculate_item_price(item) for item in items)


def apply_tax(subtotal: float, tax_rate: float = 0.08) -> float:
    """Apply a tax rate to a subtotal and return the total."""
    return subtotal * (1 + tax_rate)


def save_order_total(order_id: int, total: float, db) -> None:
    """Persist the final order total to the database."""
    db.execute("UPDATE orders SET total = ? WHERE id = ?", [total, order_id])


def send_order_confirmation(customer_email: str, total: float, emailer) -> None:
    """Send a confirmation email with the final order total."""
    emailer.send(customer_email, f"Your order total is ${total:.2f}")


def process_order(order_id: int, db, emailer) -> Optional[float]:
    """Orchestrate the full order processing pipeline.

    Returns the final order total, or None if the order was not found.
    """
    order = fetch_order(order_id, db)
    if not order:
        return None

    subtotal = calculate_order_subtotal(order["items"])
    total = apply_tax(subtotal)
    save_order_total(order_id, total, db)
    send_order_confirmation(order["customer_email"], total, emailer)
    return total
```

### Why it's better

Each function has one responsibility. You can test `calculate_item_price`, `calculate_order_subtotal`, and `apply_tax` without a database or email service — they are pure functions. The orchestrating `process_order` function is now a clean pipeline that reads like a summary of the steps.

---

## Example 2: Removing hidden state and adding explicit parameters

### Before (without this skill)

```python
# Module level
CONFIG = {"tax_rate": 0.08, "currency": "USD"}
last_calculation = None

def calculate_total(items):
    global last_calculation
    tax = CONFIG["tax_rate"]  # hidden dependency on module global
    total = sum(item["price"] * item["qty"] for item in items)
    total_with_tax = total * (1 + tax)
    last_calculation = total_with_tax  # side effect: modifies global state
    return total_with_tax
```

### After (with this skill applied)

```python
def calculate_total(items: list, tax_rate: float = 0.08) -> float:
    """Calculate the total price including tax for a list of items.

    Args:
        items: List of dicts with 'price' and 'qty' keys.
        tax_rate: Tax rate as a decimal (default 0.08 = 8%).

    Returns:
        Total price including tax.
    """
    subtotal = sum(item["price"] * item["qty"] for item in items)
    return subtotal * (1 + tax_rate)
```

### Why it's better

The improved version takes `tax_rate` as an explicit parameter. There is no hidden dependency on `CONFIG`. There is no side effect modifying `last_calculation`. The function is pure — given the same inputs, it always returns the same output. It can be tested with a single `assert calculate_total(items, 0.1) == expected_value`.

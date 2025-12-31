# Basket Orders (Multi Order) — Python Examples

Basket Orders (also called **Multi Orders**) allow you to place **multiple independent orders in a single API call**.

Each order in the basket:
- Is validated independently
- Is placed atomically in one request
- Behaves exactly like a normal single order

This is useful when you want to:
- Submit multiple legs together
- Reduce network latency
- Coordinate execution across strategies
- Build complex execution flows programmatically

---

## How Multi Order Works

- You pass an **array of order payloads**
- Each payload follows the standard `create_order` schema
- All orders are submitted together
- The response contains one result per order

> There is **no implicit dependency** between legs unless your strategy enforces it.

---

## Example: Stoploss + Iceberg Basket

This example demonstrates a **two-leg basket**:
1. A **STOPLOSS LIMIT** order (intraday)
2. An **ICEBERG LIMIT** order (delivery)

Both orders:
- Use the same instrument
- Are submitted in a single API request
- Can have different quantities, order types, and algo parameters

---

## File

- `place_multi_order.py` – Stoploss + Iceberg basket example

---

## Notes

- Multi Order supports **mixed order types** (REGULAR, STOPLOSS, ICEBERG)
- Each leg can have its own:
  - Order type
  - Quantity
  - Price type
  - Validity
  - Algo parameters
- Basket execution reduces request overhead and improves coordination

> Use `NubraEnv.PROD` for live trading after testing in UAT.


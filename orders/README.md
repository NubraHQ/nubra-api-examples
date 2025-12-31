# Order Placement Examples (Python)

This folder contains **standalone, execution-ready examples** demonstrating
how to place different types of orders using **Nubra Trading API (V2)**.

Each file focuses on **one order type**, mapped to the 4 core pillars:
- Order Side
- Order Type
- Price Type
- Validity

## Files

- `place_limit_order.py` – LIMIT order with trigger
- `place_market_order.py` – MARKET order (IOC)
- `place_regular_order.py` – Regular LIMIT order
- `place_stoploss_order.py` – STOPLOSS LIMIT order
- `place_iceberg_order.py` – ICEBERG order

> All examples use **UAT** by default.
Switch to `NubraEnv.PROD` for live trading.

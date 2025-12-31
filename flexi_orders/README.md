# Flexi Basket Orders

Flexi Basket Orders are a Nubra-native order type designed specifically for **options strategies involving multiple legs**, such as straddles, strangles, spreads, and complex hedged positions.

Traditional order types treat each leg independently. While this works for simple trades, it quickly breaks down for strategy-based trading where **execution coordination, sizing accuracy, and hedge awareness** are critical.

Flexi Baskets were built to solve exactly this problem.

---

## Why Flexi Baskets?

While working closely with algorithmic traders, discretionary options traders, and trading desks, we observed recurring challenges:

- Managing **multiple option legs independently** leads to execution risk
- Position sizing becomes inaccurate when hedge benefits are ignored
- Modifying strategies mid-flight (price, size, timing) is cumbersome
- Margin visibility for multi-leg strategies is often incomplete
- Strategy intent is lost when orders are treated as isolated legs

These gaps become more pronounced as strategies scale in:
- Number of legs
- Capital deployed
- Frequency of execution

Flexi Baskets were designed as a **strategy-first order construct**, rather than a leg-first one.

---

## What is a Flexi Basket?

A Flexi Basket allows you to define an **entire options strategy as a single logical order**, while still executing individual legs under the hood.

With a Flexi Basket, you can:

- Group **any number of option legs** into one strategy
- Define **strategy-level parameters** such as:
  - Entry price
  - Stoploss
  - Execution window (entry & exit time)
  - Multiplier (position scaling)
- Modify these parameters dynamically after order creation
- Execute strategies in a **time-bound and coordinated manner**

The strategy remains intact even as individual legs are managed internally.

---

## Accurate Position Sizing & Hedge Benefits

One of the key advantages of Flexi Baskets is **strategy-aware position sizing**.

Because all legs are submitted as part of a single basket:
- Margin calculations account for **hedge benefits**
- Position size reflects the **true risk of the combined strategy**
- Capital utilization becomes significantly more efficient

This is especially important for:
- Delta-neutral strategies
- Premium selling with hedges
- Multi-leg spreads and adjustments

---

## Strategy Direction & Execution Semantics

Flexi Baskets follow a **clear separation of concerns**:

- **Basket-level parameters**
  - Define how the strategy is executed (price, timing, sizing, stoploss)
  - `basket_params.order_side` is always set to `ORDER_SIDE_BUY` for Flexi baskets

- **Leg-level parameters**
  - Define the actual trading intent (BUY / SELL) per instrument
  - Each leg specifies its own `order_side` based on the strategy

This design ensures:
- Consistent execution semantics
- Clear intent representation
- Safe modification and lifecycle management

---

## Typical Use Cases

Flexi Baskets are well suited for:

- Long / Short Straddles
- Long / Short Strangles
- Vertical & Calendar spreads
- Hedged option selling strategies
- Intraday and time-window-based executions
- Strategies requiring frequent modification

---

## Examples in This Folder

This directory contains runnable examples demonstrating:

- Creating Flexi baskets for common option strategies
- Using LIMIT-based strategy entry
- Applying stoploss at the strategy level
- Modifying Flexi baskets dynamically:
  - Entry price
  - Multiplier
  - Stoploss
  - Entry and exit times

Each example focuses on **strategy intent**, not just order placement.

---

## Final Notes

Flexi Baskets are built for traders and developers who think in terms of **strategies**, not isolated trades.

If your trading logic involves:
- Multiple legs
- Risk-aware sizing
- Coordinated execution
- Dynamic adjustments

Flexi Baskets are the recommended order type.

For full API details, refer to the Nubra Trading API documentation.

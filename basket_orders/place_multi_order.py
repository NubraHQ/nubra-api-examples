"""
Example: Multi Order (Basket)
Leg 1: STOPLOSS LIMIT
Leg 2: ICEBERG LIMIT
"""

from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.marketdata.market_data import MarketData
from nubra_python_sdk.trading.trading_data import NubraTrader

# 1. Initialize Nubra SDK
nubra = InitNubraSdk(NubraEnv.UAT)

# 2. Fetch Market Quote (shared across legs)
md = MarketData(nubra)

REF_ID = 1842210
quote = md.quote(ref_id=REF_ID, levels=5)
ltp = quote.orderBook.last_traded_price
print(f"LTP: {ltp}")

# 3. Create Multi Order (Basket)
trade = NubraTrader(nubra, version="V2")

TOTAL_QTY = 1000
LEG_SIZE = 100
STOPLOSS_QTY = 50

result = trade.multi_order([
    {
        "ref_id": REF_ID,
        "order_type": "ORDER_TYPE_STOPLOSS",
        "order_qty": STOPLOSS_QTY,
        "order_side": "ORDER_SIDE_BUY",
        "order_delivery_type": "ORDER_DELIVERY_TYPE_IDAY",
        "validity_type": "DAY",
        "price_type": "LIMIT",
        "order_price": ltp + 50,
        "exchange": "NSE",
        "tag": "stoploss_leg",
        "algo_params": {
            "trigger_price": ltp + 30
        }
    },
    {
        "ref_id": REF_ID,
        "order_type": "ORDER_TYPE_ICEBERG",
        "order_qty": TOTAL_QTY,
        "order_side": "ORDER_SIDE_BUY",
        "order_delivery_type": "ORDER_DELIVERY_TYPE_CNC",
        "validity_type": "DAY",
        "price_type": "LIMIT",
        "order_price": ltp + 10,
        "exchange": "NSE",
        "tag": "iceberg_leg",
        "algo_params": {
            "leg_size": LEG_SIZE
        }
    }
])

print("Multi Order Response:")
print(result)

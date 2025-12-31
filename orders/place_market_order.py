from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.trading.trading_data import NubraTrader

# Initialize SDK
nubra = InitNubraSdk(NubraEnv.UAT)
trade = NubraTrader(nubra, version="V2")

# Place MARKET order (IOC only)
result = trade.create_order({
    "ref_id": 1842210,
    "order_side": "ORDER_SIDE_BUY",
    "order_type": "ORDER_TYPE_REGULAR",
    "price_type": "MARKET",
    "order_qty": 1,
    "validity_type": "IOC",
    "order_delivery_type": "ORDER_DELIVERY_TYPE_CNC",
    "exchange": "NSE",
    "tag": "market_example"
})

print(result)

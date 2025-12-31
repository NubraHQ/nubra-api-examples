from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.marketdata.market_data import MarketData
from nubra_python_sdk.trading.trading_data import NubraTrader

nubra = InitNubraSdk(NubraEnv.UAT)
md = MarketData(nubra)

REF_ID = 1842210
quote = md.quote(ref_id=REF_ID, levels=5)
ltp = quote.orderBook.last_traded_price

trade = NubraTrader(nubra, version="V2")

result = trade.create_order({
    "ref_id": REF_ID,
    "order_type": "ORDER_TYPE_STOPLOSS",
    "order_qty": 1,
    "order_side": "ORDER_SIDE_BUY",
    "order_delivery_type": "ORDER_DELIVERY_TYPE_IDAY",
    "validity_type": "DAY",
    "price_type": "LIMIT",
    "order_price": ltp + 50,
    "exchange": "NSE",
    "tag": "stoploss_example",
    "algo_params": {
        "trigger_price": ltp + 30
    }
})

print(result)

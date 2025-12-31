"""
Flexi Basket Order Example: Buy Straddle (Limit)

This example demonstrates how to place a FLEXI basket order to BUY
a straddle (CE + PE) using a LIMIT entry price.

Key characteristics:
- Entry price is derived from live order book prices
- Entry and exit times are specified (IST converted to UTC)
- Uses Trading API V2
- Intended for intraday, time-bound execution
"""

from time import sleep
from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.trading.trading_data import NubraTrader
from nubra_python_sdk.trading.trading_enum import (
    DeliveryTypeEnum,
    OrderSideEnum,
    PriceTypeEnumV2,
    ExchangeEnum
)
from nubra_python_sdk.marketdata.market_data import MarketData

# =========================================================
# INITIALIZATION
# =========================================================

# Initialize SDK using environment credentials (.env)
nubra = InitNubraSdk(NubraEnv.PROD, env_creds=True)

# Trading & Market Data clients
trade = NubraTrader(nubra, version="V2")
md = MarketData(nubra)

# Option reference IDs (example: NIFTY ATM CE & PE)
REF_CE = 956870
REF_PE = 956857
QTY = 75  # 1 lot

# =========================================================
# Helper: Derive LIMIT price from live order book
# =========================================================

def get_limit_price(ref_id, side):
    """
    Fetches the best available price from the order book
    to be used as a LIMIT price fallback.
    """
    quote = md.quote(ref_id=ref_id, levels=5)
    ob = quote.orderBook

    if side == OrderSideEnum.ORDER_SIDE_BUY:
        return ob.ask[0].price if ob.ask else ob.last_traded_price
    else:
        return ob.bid[0].price if ob.bid else ob.last_traded_price


# =========================================================
# FETCH INDIVIDUAL LEG PRICES
# =========================================================

ce_price = get_limit_price(REF_CE, OrderSideEnum.ORDER_SIDE_BUY)
pe_price = get_limit_price(REF_PE, OrderSideEnum.ORDER_SIDE_BUY)

print(f"CE Best Ask Price : {ce_price}")
print(f"PE Best Ask Price : {pe_price}")

# Combined straddle entry price (with small buffer)
entry_price = ce_price + pe_price - 10
print(f"Final Straddle LIMIT Entry Price: {entry_price}")

# =========================================================
# PLACE FLEXI BASKET ORDER (STRADDLE)
# =========================================================

"""
Entry & Exit Times:
- Provided in UTC
- Converted from IST manually
"""

basket_response = trade.flexi_order({
    "exchange": ExchangeEnum.NSE,
    "basket_name": "BuyStraddleLimit",
    "tag": "buy_straddle_limit_entry",

    "orders": [
        {
            "ref_id": REF_CE,
            "order_qty": QTY,
            "order_side": OrderSideEnum.ORDER_SIDE_BUY
        },
        {
            "ref_id": REF_PE,
            "order_qty": QTY,
            "order_side": OrderSideEnum.ORDER_SIDE_BUY
        }
    ],

    "basket_params": {
        "order_side": OrderSideEnum.ORDER_SIDE_BUY,
        "order_delivery_type": DeliveryTypeEnum.ORDER_DELIVERY_TYPE_CNC,
        "price_type": PriceTypeEnumV2.LIMIT,
        "entry_price": entry_price,
        "multiplier": 1,

        # Time-bound execution (UTC)
        "entry_time": "2025-12-29T09:10:00.000Z",
        "exit_time": "2025-12-29T09:40:00.000Z"  
    }
})

basket_id = basket_response.basket_id
print(f"\nFlexi Basket Created | Basket ID: {basket_id}")

# Allow backend to register the basket
sleep(2)

# =========================================================
# FETCH & VERIFY BASKET STATE
# =========================================================

basket = trade.get_flexi_order()
print("Current Flexi Basket State:")
print(basket)

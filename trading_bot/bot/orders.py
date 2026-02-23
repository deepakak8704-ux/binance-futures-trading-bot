from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def execute_order(symbol, side, order_type, quantity, price=None):
    client = BinanceFuturesClient()

    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    response = client.place_order(**params)

    return response
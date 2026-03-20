import logging
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def create_order(client, symbol, side, order_type, quantity, price=None):
    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(float(quantity))
        price = validate_price(price, order_type)

        order_params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order_params.update({
                "price": price,
                "timeInForce": "GTC"
            })

        logging.info(f"Order Request: {order_params}")

        response = client.place_order(**order_params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise

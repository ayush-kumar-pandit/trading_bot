import click
from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.logging_config import setup_logging

setup_logging()

@click.command()
@click.option("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--order_type", required=True, help="MARKET or LIMIT")
@click.option("--quantity", required=True, type=float)
@click.option("--price", required=False, type=float)

def main(symbol, side, order_type, quantity, price):
    client = BinanceFuturesClient()

    click.echo("\n===== ORDER SUMMARY =====")
    click.echo(f"Symbol: {symbol}")
    click.echo(f"Side: {side}")
    click.echo(f"Type: {order_type}")
    click.echo(f"Quantity: {quantity}")
    if order_type.upper() == "LIMIT":
        click.echo(f"Price: {price}")

    try:
        response = create_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        click.echo("\n===== ORDER RESPONSE =====")
        click.echo(f"Order ID: {response.get('orderId')}")
        click.echo(f"Status: {response.get('status')}")
        click.echo(f"Executed Qty: {response.get('executedQty')}")
        click.echo(f"Avg Price: {response.get('avgPrice')}")

        click.echo("\n✅ Order placed successfully")

    except Exception as e:
        click.echo(f"\n❌ Failed: {str(e)}")

if __name__ == "__main__":
    main()

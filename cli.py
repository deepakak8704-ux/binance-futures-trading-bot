import argparse
from bot.orders import execute_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        print("\n=== ORDER REQUEST SUMMARY ===")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")

        response = execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        logger.error(str(e))
        print(f"\n❌ Order failed: {str(e)}")


if __name__ == "__main__":
    main()
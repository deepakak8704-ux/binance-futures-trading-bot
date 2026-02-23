import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()


class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API credentials not found in .env file")

        self.client = Client(self.api_key, self.api_secret)

        # Set Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet Client initialized")

    def place_order(self, **params):
        try:
            logger.info(f"Order request: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API error: {str(e)}")
            raise
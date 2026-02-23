# Binance Futures Testnet Trading Bot

A simplified Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

This project was built as part of a Python Developer Internship assignment.

---

## 📌 Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- CLI-based input using argparse
- Structured project architecture
- Logging of API requests, responses, and errors
- Exception handling and input validation
- Works with Binance Futures Testnet (USDT-M)

---

## 🏗 Project Structure
USDT-M/
│── logs/                # Log files for bot activity and errors
│── trading_bot/         # Core trading bot package
|   |--bot/
│      │─- __init__.py
│      │── client.py        # Binance API client setup
│      │── order.py         # Order execution logic
│      │── utils.py         # Helper functions
│
│── .env                 # Environment variables (API keys, secrets)
│── cli.py               # Command-line interface entry point
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone <your-repo-link>
cd USDT-M


---

### 2️⃣ Install Dependencies
pip install -r requirements.txt

---

### 3️⃣ Create Binance Futures Testnet Account

Go to:

https://testnet.binancefuture.com

- Login
- Go to API Management
- Create **System Generated** API key
- Enable **Futures Trading**
- Copy API Key and Secret

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in project root:
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key


⚠️ No quotes. No spaces.

---

## 🚀 How to Run

### ▶ MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


---

### ▶ LIMIT Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000

---

## 📝 Output

The program prints:

- Order request summary
- Order response (orderId, status, executedQty, avgPrice)
- Success or failure message

---

## 📂 Logs

All API requests, responses, and errors are logged in:
logs/trading_bot.log


Log file includes:
- Order parameters
- Binance API response
- Error messages (if any)

---

## ⚠️ Important Notes

- Binance Futures Testnet requires a minimum notional value of 100 USDT.
- Ensure your order quantity satisfies this requirement.
- This bot is for testnet usage only.

---

## 📧 Submission

This project satisfies the requirements for:

Application Task – Python Developer  
(Simplified Trading Bot on Binance Futures Testnet)

Includes:
- Structured code
- Logging
- Exception handling
- CLI input validation
- Market and Limit order support
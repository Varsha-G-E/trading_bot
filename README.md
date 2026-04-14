# Binance Futures Testnet Trading Bot

## 📌 Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input
- Logging and error handling

## ⚙️ Setup
pip install -r requirements.txt

## 🔑 Add API Keys
Create .env file:

API_KEY=your_api_key  
API_SECRET=your_secret_key  

## ▶️ Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 30000
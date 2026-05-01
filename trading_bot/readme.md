"""
# Binance Futures Testnet Trading Bot

## Setup
1. Clone repo
2. Create .env file:
   API_KEY=your_key
   API_SECRET=your_secret

3. Install dependencies:
   pip install -r requirements.txt

## Run Examples

### MARKET ORDER
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

### LIMIT ORDER
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 60000

## Notes
- Uses Binance Futures Testnet
- Logs stored in trading_bot.log
"""
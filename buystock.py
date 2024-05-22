from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest 
from alpaca.trading.enums import OrderSide, TimeInForce
import config

# FILE FOR TESTING OF BUYING STOCKS WITHOUT ANALYSIS

trading_client = TradingClient(config.ALPACA_API_KEY, config.ALPACA_API_SECRET_KEY, paper=True)
stocks_of_interest = ['AAPL','MSFT','AMZN','NVDA','GOOGL','META','GOOG','TSLA','BRK.B','AVGO']

for item in stocks_of_interest:
    market_order_data = MarketOrderRequest(
                    symbol=item,
                    qty=50,
                    side=OrderSide.BUY, # change to sell to sell stock
                    time_in_force=TimeInForce.DAY
                    )
    market_order = trading_client.submit_order(order_data=market_order_data)

    print(market_order_data.side + " of " + market_order_data.symbol)
    print(market_order_data.qty)









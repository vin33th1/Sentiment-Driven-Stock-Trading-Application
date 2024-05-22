from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest 
from alpaca.trading.enums import OrderSide, TimeInForce
from openai import OpenAI
import finnhub
from datetime import datetime
import ast
import config
import time

# Fill all API keys in config.py aswell as stocks your interested in looking at

#Alpaca
trading_client = TradingClient(config.ALPACA_API_KEY, config.ALPACA_API_SECRET_KEY, paper=True)
#OpenAI
client = OpenAI(api_key=config.OPEN_AI_API_KEY,)
#FinnHub
finnhub_account = finnhub.Client(api_key=config.FINNHUB_API_KEY)

stock_picks = config.stocks_of_interest
    

def buy_stock(ticker: str, quantity: int):
    market_order_data = MarketOrderRequest(
                    symbol=ticker,
                    qty=quantity,
                    side=OrderSide.BUY, 
                    time_in_force=TimeInForce.DAY
                    )
    market_order = trading_client.submit_order(order_data=market_order_data)
    print(market_order_data.side + " of " + market_order_data.symbol)
    print(market_order_data.qty)
    return
def sell_stock(ticker: str, quantity: int):
    market_order_data = MarketOrderRequest(
                    symbol=ticker,
                    qty=quantity,
                    side=OrderSide.SELL, 
                    time_in_force=TimeInForce.DAY
                    )
    market_order = trading_client.submit_order(order_data=market_order_data)
    print(market_order_data.side + " of " + market_order_data.symbol)
    print(market_order_data.qty)
    return
def get_summaries(ticker: str):
    current_datetime = datetime.now()
    data = [finnhub_account.company_news(ticker, _from=current_datetime.date(), to=current_datetime.date())]

    all_summaries = []
    specfic_key = 'summary'
    for dictionary in data[0]:
        if specfic_key in dictionary:
            all_summaries.append(dictionary[specfic_key])
    return all_summaries
def valid_response(reply):
    allowed_chars = set('10-,[] ')
    is_valid_list = all(char in allowed_chars for char in reply)

    return is_valid_list
    
def get_sentiments(list: list):
    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an AI language model trained to analyze and detect the sentiment of news summaries."},
        {"role": "user","content": f"Use sentiment analysis and determine if these pieces of content in this python list are postive negative or neutral {list} answer with an integer value ranging from [-1,1] -1 being negative and 1 being postivie only output the numerical values as a python list",}
    ],
    model="gpt-3.5-turbo",
    )
    reply_content = chat_completion.choices[0].message.content 

    while(not valid_response(reply_content)):
        time.sleep(20)
        chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI language model trained to analyze and detect the sentiment of news summaries and only outputs as python lists."},
            {"role": "user","content": f"Use sentiment analysis and determine if these pieces of content in this python list are postive negative or neutral {list} answer with an integer value ranging from [-1,1] -1 being negative and 1 being postivie only output the numerical values as a python list",}
        ],
        model="gpt-3.5-turbo",
        )
        reply_content = chat_completion.choices[0].message.content 


    reply_list = ast.literal_eval(reply_content)

    return reply_list

for item in stock_picks:
        stock_summaries = get_summaries(item)
        stock_sentiments = get_sentiments(stock_summaries)
        sentiment_average = sum(stock_sentiments) / len(stock_sentiments)
        print(item)
        print(sentiment_average)

        if sentiment_average > 0:
            if sentiment_average > 0.25:
                buy_stock(item, 5)
            elif sentiment_average > 0.50:
                buy_stock(item, 7)
            elif sentiment_average > 0.75:
                buy_stock(item, 10)
        elif sentiment_average < 0:
            if sentiment_average < -0.25:
                sell_stock(item, 5)
            elif sentiment_average < -0.50:
                sell_stock(item, 7)
            elif sentiment_average < -0.75:
                sell_stock(item, 10)
        time.sleep(20)

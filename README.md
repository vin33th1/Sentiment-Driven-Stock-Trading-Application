Sentiment-Driven Stock Trading Application
Overview

The Sentiment-Driven Stock Trading Application is a project that analyzes news headlines related to your choice of stock tickers. By running sentiment analysis on these headlines, the application aims to inform buying and selling decisions for stock holdings based on the sentiment of the news.

Features

    News Headline Aggregation: Collects and aggregates news headlines for popular stock tickers.
    Sentiment Analysis: Utilizes sentiment analysis techniques to evaluate the sentiment (positive, negative, neutral) of each headline.
    Trading Signals: Generates buy or sell signals based on the aggregated sentiment scores for each stock ticker.

Installation
Prerequisites

    Python 3.8 or higher
    Git
    Virtualenv (optional but recommended)
    OpenAI Account
    Finnhub Account
    Alpaca Trading Account

Clone the Repository


git clone https://github.com/yourusername/Sentiment-Driven-Stock-Trading.git
cd sentiment-driven-stock-trading


Install Dependencies

pip install -r requirements.txt

Usage
Configuration

Before running the application, ensure you configure the necessary API keys and settings. Update the config.py with apporiate keys.


ALPACA_API_KEY = 'INSERT KEY HERE'
ALPACA_API_SECRET_KEY = 'INSERT KEY HERE'
MAIN_WATCHLIST_ID = 'INSERT KEY HERE'
FINNHUB_API_KEY = "INSERT KEY HERE"
OPEN_AI_API_KEY = 'INSERT KEY HERE'

Running the Application

To start the application, run:

python main.py


Contact

For any questions or suggestions, please open an issue or contact vin33th1.

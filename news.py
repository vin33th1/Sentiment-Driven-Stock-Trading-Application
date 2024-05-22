import finnhub
import config
from datetime import datetime

current_datetime = datetime.now()

finnhub_account = finnhub.Client(api_key=config.FINNHUB_API_KEY)
data = [finnhub_account.company_news('AAPL', _from=current_datetime.date(), to=current_datetime.date())]

all_summaries = []
specfic_key = 'summary'
for dictionary in data[0]:
    if specfic_key in dictionary:
        all_summaries.append(dictionary[specfic_key])

print(f"all summaries {all_summaries}")

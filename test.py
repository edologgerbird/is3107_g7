import TickerExtractor
import pandas as pd
import time
start_time = time.time()

ticker_extractor_layer = TickerExtractor.TickerExtractor()
data_in = pd.read_csv("sbr_articles_stocks.csv")
data_in_df = data_in["Text"]
df = ticker_extractor_layer.populate_ticker_occurences(data_in_df)
df.to_csv("tickers_found.csv")

print("--- %s seconds ---" % (time.time() - start_time))

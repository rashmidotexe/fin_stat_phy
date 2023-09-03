url_sentiment = "https://api.financialdata.com/sentiment"
response_sentiment = requests.get(url_sentiment)
sentiment_data = response_sentiment.json()

sentiment_df = pd.DataFrame(sentiment_data)
sentiment_df.to_csv("data/sentiment_data.csv")

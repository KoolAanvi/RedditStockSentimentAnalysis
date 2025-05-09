# import praw
# import pandas as pd
# from datetime import datetime, timedelta
# from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
# import yfinance as yf
# import math

# # Reddit setup
# reddit = praw.Reddit(
#     client_id="",
#     client_secret="",
#     user_agent=""
# )

# # FinBERT model
# tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
# model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
# finbert = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# def get_finbert_score(text):
#     try:
#         result = finbert(text[:512])[0]
#         label = result["label"]
#         score = result["score"]
#         compound = score if label == "positive" else -score if label == "negative" else 0
#         return compound, label
#     except:
#         return 0, "error"

# def get_reddit_posts(ticker, subreddits, days=7):
#     posts = []
#     since = datetime.utcnow() - timedelta(days=days)
#     for subreddit in subreddits:
#         for post in reddit.subreddit(subreddit).search(ticker, sort="new", time_filter="all"):
#             created = datetime.utcfromtimestamp(post.created_utc)
#             if created < since:
#                 continue
#             compound, label = get_finbert_score(post.title + " " + post.selftext)
#             if compound == 0:
#                 continue
#             weight = math.log(1 + post.score) * math.log(1 + len(post.selftext))
#             weighted = compound * weight
#             posts.append({
#                 "text": post.title,
#                 "score": compound,
#                 "label": label,
#                 "weighted_score": weighted,
#                 "display_score": round((weighted + 10) / 20 * 9 + 1, 2),
#                 "upvotes": post.score,
#                 "link": f"https://reddit.com{post.permalink}",
#                 "date": created
#             })
#     df = pd.DataFrame(posts)
#     if not df.empty:
#         df["date"] = pd.to_datetime(df["date"])
#         df.set_index("date", inplace=True)
#     return df

# def generate_summary(df, ticker):
#     if df.empty:
#         return f"No recent discussions found for ${ticker.upper()}."
#     avg = df["display_score"].mean()
#     tone = (
#         "generally positive" if avg > 6.5 else
#         "generally negative" if avg < 4.5 else
#         "mixed or neutral"
#     )
#     most_discussed_day = pd.Series(df.index.date).value_counts().idxmax()
#     return (
#         f"📊 Sentiment Summary for ${ticker.upper()}\n\n"
#         f"Posts analyzed: {len(df)}\n"
#         f"Average sentiment: {round(avg, 2)}/10 ({tone})\n"
#         f"Most active day: {most_discussed_day}"
#     )

# def get_stock_data(ticker, days=7):
#     end = datetime.today()
#     start = end - timedelta(days=days)
#     print(f"📅 Fetching stock data for {ticker} from {start.date()} to {end.date()}")

#     try:
#         # Try without end date
#         data = yf.download(ticker, start=start)
#         print(f"📦 Returned data:\n{data.head()}")

#         if data.empty or "Adj Close" not in data.columns:
#             print("⚠️ No data returned or missing 'Adj Close'")
#             return pd.DataFrame(columns=["Price"])

#         cleaned = data[["Adj Close"]].rename(columns={"Adj Close": "Price"})
#         cleaned.index = pd.to_datetime(cleaned.index)
#         return cleaned

#     except Exception as e:
#         print(f"❌ Error fetching stock data for {ticker}: {e}")
#         return pd.DataFrame(columns=["Price"])





# # import praw
# # import pandas as pd
# # import yfinance as yf
# # from datetime import datetime, timedelta
# # from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
# # import tweepy
# # import math

# # # Reddit API setup
# # reddit = praw.Reddit(
# #     client_id="xSbaqBD_OvYC9bqLPeRAIg",
# #     client_secret="KbzFNldd7S8L8BFOnQV8ZaJJYxLtaQ",
# #     user_agent="Sentiment Analysis by u/getting-thru-it"
# # )

# # # Twitter Bearer Token (hardcoded for now)
# # TWITTER_BEARER = "AAAAAAAAAAAAAAAAAAAAANFG0wEAAAAAtgEbIt6sM0Sxhwz0kaa0JcDvR10%3DQwxpYZaKRqEHzVDqSdGdY1Yi5G2sUVEZa0YYvv2Ed34CTVjPKT"
# # client = tweepy.Client(bearer_token=TWITTER_BEARER)

# # # FinBERT model
# # tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
# # model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
# # finbert = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# # def get_finbert_score(text):
# #     try:
# #         result = finbert(text[:512])[0]
# #         label = result["label"]
# #         score = result["score"]
# #         return (score if label == "positive" else -score if label == "negative" else 0), label
# #     except:
# #         return 0, "error"

# # def get_reddit_posts(ticker, subreddits, days=7):
# #     posts = []
# #     since = datetime.utcnow() - timedelta(days=days)
# #     for subreddit in subreddits:
# #         for post in reddit.subreddit(subreddit).search(ticker, sort="new", time_filter="week"):
# #             created = datetime.utcfromtimestamp(post.created_utc)
# #             if created < since:
# #                 continue
# #             compound, label = get_finbert_score(post.title + " " + post.selftext)
# #             if compound == 0:
# #                 continue
# #             weight = math.log(1 + post.score) * math.log(1 + len(post.selftext))
# #             weighted = compound * weight
# #             posts.append({
# #                 "text": post.title,
# #                 "score": compound,
# #                 "label": label,
# #                 "weighted_score": weighted,
# #                 "display_score": round((weighted + 10) / 20 * 9 + 1, 2),
# #                 "upvotes": post.score,
# #                 "platform": "Reddit",
# #                 "link": f"https://reddit.com{post.permalink}",
# #                 "date": created
# #             })
# #     df = pd.DataFrame(posts)
# #     if not df.empty:
# #         df["date"] = pd.to_datetime(df["date"])
# #         df.set_index("date", inplace=True)
# #     return df

# # def get_tweets(ticker, days=7, max_results=100):
# #     import datetime
# #     tweet_data = []
# #     try:
# #         end_time = datetime.datetime.utcnow()
# #         start_time = end_time - datetime.timedelta(days=min(days, 7))
# #         query = f"({ticker} OR ${ticker}) lang:en -is:retweet"
# #         tweets = tweepy.Paginator(
# #             client.search_recent_tweets,
# #             query=query,
# #             start_time=start_time.isoformat("T") + "Z",
# #             end_time=end_time.isoformat("T") + "Z",
# #             tweet_fields=["created_at", "text", "public_metrics", "id"],
# #             max_results=100
# #         ).flatten(limit=max_results)

# #         for tweet in tweets:
# #             compound, label = get_finbert_score(tweet.text)
# #             if compound == 0:
# #                 continue
# #             metrics = tweet.public_metrics
# #             weight = math.log(1 + metrics["like_count"] + metrics["retweet_count"]) * math.log(1 + len(tweet.text))
# #             weighted = compound * weight
# #             tweet_data.append({
# #                 "text": tweet.text,
# #                 "score": compound,
# #                 "label": label,
# #                 "weighted_score": weighted,
# #                 "display_score": round((weighted + 10) / 20 * 9 + 1, 2),
# #                 "likes": metrics["like_count"],
# #                 "retweets": metrics["retweet_count"],
# #                 "platform": "Twitter",
# #                 "link": f"https://twitter.com/i/web/status/{tweet.id}",
# #                 "date": tweet.created_at
# #             })
# #     except Exception as e:
# #         raise RuntimeError(f"🐦 Twitter fetch failed: {str(e)}")

# #     df = pd.DataFrame(tweet_data)
# #     if not df.empty:
# #         df["date"] = pd.to_datetime(df["date"])
# #         df.set_index("date", inplace=True)
# #     return df

# # def get_stock_data(ticker, days=7):
# #     end = datetime.today()
# #     start = end - timedelta(days=days)
# #     data = yf.download(ticker, start=start, end=end)
# #     if "Adj Close" not in data.columns or data.empty:
# #         return pd.DataFrame(columns=["Price"])
# #     return data[["Adj Close"]].rename(columns={"Adj Close": "Price"})

# # def generate_summary(df, ticker):
# #     if df.empty:
# #         return f"No recent discussions found for ${ticker.upper()}."
# #     avg = df["display_score"].mean()
# #     tone = (
# #         "generally positive" if avg > 6.5 else
# #         "generally negative" if avg < 4.5 else
# #         "mixed or neutral"
# #     )
# #     most_discussed_day = pd.Series(df.index.date).value_counts().idxmax()
# #     return (
# #         f"📊 Sentiment Summary for ${ticker.upper()}\n\n"
# #         f"Posts/Tweets analyzed: {len(df)}\n"
# #         f"Average sentiment: {round(avg, 2)}/10 ({tone})\n"
# #         f"Most active day: {most_discussed_day}"
# #     )

import praw
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import math

# Reddit API
reddit = praw.Reddit(
    client_id="xSbaqBD_OvYC9bqLPeRAIg",
    client_secret="KbzFNldd7S8L8BFOnQV8ZaJJYxLtaQ",
    user_agent="Sentiment Analysis by u/getting-thru-it"
)

# FinBERT setup
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
finbert = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Soft-scale weighted sentiment to [1–10]
def scale_sentiment(score):
    score = max(min(score, 25), -25)
    return round((score + 25) / 50 * 9 + 1, 2)

def get_finbert_score(text):
    try:
        result = finbert(text[:512])[0]
        label = result["label"]
        score = result["score"]
        compound = score if label == "positive" else -score if label == "negative" else 0
        return compound, label
    except:
        return 0, "error"

def get_reddit_posts(ticker, subreddits, days=7):
    posts = []
    since = datetime.utcnow() - timedelta(days=days)
    for subreddit in subreddits:
        for post in reddit.subreddit(subreddit).search(ticker, sort="new", time_filter="all"):
            created = datetime.utcfromtimestamp(post.created_utc)
            if created < since:
                continue
            compound, label = get_finbert_score(post.title + " " + post.selftext)
            if compound == 0:
                continue
            weight = math.log(1 + post.score + 1) * math.log(1 + len(post.selftext) + 1)
            weighted = compound * weight
            posts.append({
                "text": post.title,
                "score": compound,
                "label": label,
                "weighted_score": weighted,
                "display_score": scale_sentiment(weighted),
                "upvotes": post.score,
                "link": f"https://reddit.com{post.permalink}",
                "date": created
            })
    df = pd.DataFrame(posts)
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)
    return df

def generate_summary(df, ticker):
    if df.empty:
        return f"No recent discussions found for ${ticker.upper()}."
    avg = df["display_score"].mean()
    tone = (
        "generally positive" if avg > 6.5 else
        "generally negative" if avg < 4.5 else
        "mixed or neutral"
    )
    top_day = pd.Series(df.index.date).value_counts().idxmax()
    return (
        f"📊 Sentiment Summary for ${ticker.upper()}\n\n"
        f"Posts analyzed: {len(df)}\n"
        f"Average sentiment: {round(avg, 2)}/10 ({tone})\n"
        f"Most active day: {top_day}"
    )

def get_stock_data(ticker, days=7):
    end = datetime.today()
    start = end - timedelta(days=days)
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            print("⚠️ No data returned.")
            return pd.DataFrame(columns=["Price"])
        if "Adj Close" not in data.columns:
            print("⚠️ 'Adj Close' column missing.")
            return pd.DataFrame(columns=["Price"])
        cleaned = data[["Adj Close"]].rename(columns={"Adj Close": "Price"})
        cleaned.dropna(inplace=True)
        if cleaned.empty:
            print("⚠️ All stock prices are NaN after cleaning.")
        return cleaned
    except Exception as e:
        print(f"❌ Error fetching stock data: {e}")
        return pd.DataFrame(columns=["Price"])


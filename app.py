# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from sentiment_utils import get_reddit_posts, generate_summary, get_stock_data

# st.set_page_config(page_title="Stock Sentiment App", layout="wide")
# st.title("📈 Reddit Sentiment Analyzer")

# # Date range selection
# range_label = st.selectbox("Select time range:", ["1 Week", "2 Weeks", "1 Month", "2 Months", "3 Months"])
# range_map = {
#     "1 Week": 7,
#     "2 Weeks": 14,
#     "1 Month": 30,
#     "2 Months": 60,
#     "3 Months": 90
# }
# days = range_map[range_label]

# ticker = st.text_input("Enter stock ticker (e.g., NVDA)", "NVDA").upper()

# if st.button("Analyze Sentiment"):
#     with st.spinner("Fetching Reddit posts..."):
#         reddit_df = get_reddit_posts(ticker, ["stocks", "investing", "wallstreetbets"], days=days)
#         stock_df = get_stock_data(ticker, days=days)

#         st.subheader("📄 Debugging Info")
#         st.write("📘 Reddit Data Preview", reddit_df.head())
#         st.write("📘 Stock Price Preview", stock_df.head())

#         if reddit_df.empty:
#             st.warning("No relevant Reddit posts found.")
#         else:
#             st.markdown(generate_summary(reddit_df, ticker))

#             st.subheader("📈 Stock Price and Sentiment Over Time")
#             fig, ax1 = plt.subplots(figsize=(10, 4))
#             daily_sent = reddit_df.resample("D")["display_score"].mean()
#             daily_sent.plot(ax=ax1, color="tab:blue", label="Sentiment Score (1–10)")
#             ax1.set_ylabel("Sentiment Score (1–10)", color="tab:blue")
#             ax1.axhline(5.5, linestyle="--", color="gray", alpha=0.4)
#             ax1.set_xlabel("Date")

#             if not stock_df.empty:
#                 ax2 = ax1.twinx()
#                 stock_df["Price"].plot(ax=ax2, color="gray", alpha=0.6, label="Stock Price")
#                 ax2.set_ylabel("Stock Price", color="gray")
#             else:
#                 st.warning("⚠️ No stock price data available.")

#             fig.legend(loc="upper left")
#             st.pyplot(fig)

#             st.subheader("👍 Top Positive Reddit Posts")
#             top_pos = reddit_df.sort_values(by="weighted_score", ascending=False).head(5)
#             for _, row in top_pos.iterrows():
#                 st.markdown(f"[{row['text']}]({row['link']}) — Score: {row['display_score']} ({row['label']})")

#             st.subheader("👎 Top Negative Reddit Posts")
#             top_neg = reddit_df.sort_values(by="weighted_score", ascending=True).head(5)
#             for _, row in top_neg.iterrows():
#                 st.markdown(f"[{row['text']}]({row['link']}) — Score: {row['display_score']} ({row['label']})")


# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # from sentiment_utils import get_reddit_posts, get_tweets, get_stock_data, generate_summary

# # st.set_page_config(page_title="Stock Sentiment App", layout="wide")
# # st.title("📈 Reddit & Twitter Sentiment Analyzer")
# # st.caption("🕒 Twitter data limited to the past 7 days due to API restrictions.")

# # ticker = st.text_input("Enter stock ticker (e.g., NVDA)", "NVDA").upper()
# # use_twitter = st.checkbox("Include Twitter data")

# # if st.button("Analyze Sentiment"):
# #     with st.spinner("📥 Fetching Reddit posts..."):
# #         reddit_df = get_reddit_posts(ticker, ["stocks", "investing", "wallstreetbets"], days=7)

# #     if use_twitter:
# #         with st.spinner("🐦 Fetching tweets..."):
# #             try:
# #                 twitter_df = get_tweets(ticker)
# #             except RuntimeError as e:
# #                 st.error(str(e))
# #                 twitter_df = pd.DataFrame()
# #     else:
# #         twitter_df = pd.DataFrame()

# #     price_df = get_stock_data(ticker, days=7)

# #     all_df = pd.concat([reddit_df, twitter_df])
# #     if all_df.empty:
# #         st.warning("No relevant posts or tweets found.")
# #     else:
# #         st.markdown(generate_summary(all_df, ticker))

# #         # Chart: sentiment + price
# #         st.subheader("📈 Stock Price and Sentiment Over Time")
# #         fig, ax1 = plt.subplots(figsize=(10, 4))

# #         sentiment_series = all_df.resample("D")["score"].mean()
# #         if not sentiment_series.empty:
# #             sentiment_scaled = sentiment_series.apply(lambda x: round((x + 1) * 4.5 + 1, 2))
# #             sentiment_scaled.plot(ax=ax1, label="Sentiment Score (1–10)", color="tab:blue")
# #             ax1.axhline(5.5, linestyle='--', color='gray', alpha=0.4)
# #             ax1.set_ylabel("Sentiment Score (1–10)", color="tab:blue")
# #             ax1.set_xlabel("Date")

# #             if not price_df.empty:
# #                 ax2 = ax1.twinx()
# #                 price_df["Price"].plot(ax=ax2, color="gray", alpha=0.6, label="Stock Price")
# #                 ax2.set_ylabel("Stock Price", color="gray")

# #             fig.legend(loc="upper left")
# #             st.pyplot(fig)
# #         else:
# #             st.info("Not enough sentiment data to generate chart.")

# #         # Top Posts Display
# #         def display_top_posts(df, title, ascending):
# #             st.subheader(title)
# #             top_df = df[df["weighted_score"] != 0].sort_values(by="weighted_score", ascending=ascending).drop_duplicates(subset="text").head(5)
# #             if top_df.empty:
# #                 st.markdown("_No strong posts to display._")
# #                 return
# #             for _, row in top_df.iterrows():
# #                 st.markdown(
# #                     f"[{row['text']}]({row['link']}) — **{row['platform']}**, "
# #                     f"Score: {round(row['display_score'], 2)} ({row['label']})"
# #                 )

# #         display_top_posts(all_df, "👍 Top Positive Posts/Tweets", ascending=False)
# #         display_top_posts(all_df, "👎 Top Negative Posts/Tweets", ascending=True)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment_utils import get_reddit_posts, generate_summary, get_stock_data

st.set_page_config(page_title="Stock Sentiment App", layout="wide")
st.title("📈 Reddit Sentiment Analyzer")

# Time range options
range_label = st.selectbox("Select time range:", ["1 Week", "2 Weeks", "1 Month", "2 Months", "3 Months"])
range_map = {
    "1 Week": 7,
    "2 Weeks": 14,
    "1 Month": 30,
    "2 Months": 60,
    "3 Months": 90
}
days = range_map[range_label]

ticker = st.text_input("Enter stock ticker (e.g., NVDA)", "NVDA").upper()

if st.button("Analyze Sentiment"):
    with st.spinner("Fetching Reddit posts..."):
        reddit_df = get_reddit_posts(ticker, ["stocks", "investing", "wallstreetbets"], days=days)
        price_df = get_stock_data(ticker, days=days)

        if reddit_df.empty:
            st.warning("No relevant Reddit posts found.")
        else:
            st.markdown(generate_summary(reddit_df, ticker))

            # Plot stock and sentiment in separate graphs
            st.subheader("📈 Stock Price and Sentiment Over Time")
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

            # Sentiment line chart
            sent_series = reddit_df.resample("D")["display_score"].mean()
            sent_series.plot(ax=ax1, label="Sentiment Score (1–10)", color="tab:blue")
            ax1.axhline(5.5, linestyle="--", color="gray", alpha=0.5)
            ax1.set_ylabel("Sentiment Score (1–10)")
            ax1.set_title("Sentiment Over Time")
            ax1.legend()

            # Stock price line chart
            if not price_df.empty and "Price" in price_df.columns and not price_df["Price"].isna().all():
                price_df["Price"].plot(ax=ax2, label="Stock Price", color="tab:green", alpha=0.8)
                ax2.set_ylabel("Stock Price ($)")
                ax2.set_title("Stock Price Over Time")
                ax2.legend()
            else:
                ax2.set_title("Stock Price Over Time (No data available)")
                st.warning("⚠️ Stock price data is empty or all NaNs.")


            ax2.set_xlabel("Date")
            plt.tight_layout()
            st.pyplot(fig)


            st.subheader("👍 Top Positive Reddit Posts")
            top_pos = reddit_df[reddit_df["weighted_score"] > 0].sort_values(by="weighted_score", ascending=False).head(5)
            for _, row in top_pos.iterrows():
                st.markdown(f"[{row['text']}]({row['link']}) — Score: {row['display_score']} ({row['label']})")

            st.subheader("👎 Top Negative Reddit Posts")
            top_neg = reddit_df[reddit_df["weighted_score"] < 0].sort_values(by="weighted_score", ascending=True).head(5)
            for _, row in top_neg.iterrows():
                st.markdown(f"[{row['text']}]({row['link']}) — Score: {row['display_score']} ({row['label']})")

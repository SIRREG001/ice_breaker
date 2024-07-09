import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()
twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
)


def scrape_user_tweets(username, num_tweets=5, mock: bool = False):
    """
    Scrapes a Twitter user's original tweets(i.e., not retweets or replies) and returns them as a list of dictionaries
    Each dictionary has three fields: "time pasted"(relative to new), "text", and "url"
    """
    tweet_list = []
    if mock:
        UDOCHUKWU_REGINALD_GIST = "https://gist.githubusercontent.com/SIRREG001/f62ef35e24ed775894ad85e9508db0d1/raw/2ebad3756b66ae124141354fd25d30b9db97f0ad/udochukwu-reginald-twitter.json"
        tweets = requests.get(UDOCHUKWU_REGINALD_GIST, timeout=5).json()


    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )
        tweets = tweets.data
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="SIRREG4", mock=True)
    print(tweets)

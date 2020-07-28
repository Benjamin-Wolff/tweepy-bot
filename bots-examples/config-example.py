# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


# used to create the API for the bot
def create_api():
    # Use following to import your own information from Twitter Developer Account, if desired
    """CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")"""

    # Otherwise, input the information here
    CONSUMER_KEY = "INSERT CONSUMER KEY HERE"
    CONSUMER_SECRET = "INSERT CONSUMER SECRET KEY HERE"

    ACCESS_TOKEN = "INSERT ACCESS TOKEN HERE"
    ACCESS_TOKEN_SECRET = "INSERT SECRET ACCESS TOKEN HERE"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created properly")

    return api

# tweepy-bots/bots/squidbot.py
import tweepy
import logging
from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# used to run the SquidBot
class SquidBotListener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info("Processing tweet id {}".format(tweet.id))
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.retweeted:
            try:
                tweet.retweet()
                logger.info("Replying to {}".format(tweet.user.name))
                self.api.update_status("INSERT REPLY TEXT HERE",
                                       in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True,)
            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


# main function to run the bot
def main(twitter_id):
    api = create_api()
    tweets_listener = SquidBotListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=twitter_id)


if __name__ == "__main__":
    main(["INSERT NUMBER OF DESIRED TWITTER USER'S USER ID HERE"])
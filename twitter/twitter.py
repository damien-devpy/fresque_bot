from os import environ

import tweepy


class Twitter:
    """Wrapper over tweepy in order to tweet messages."""

    def __init__(self, message):
        """Create a Twitter object.

        self.message (string): message to tweet
        self.api (Twitter API object): Manage Twitter API

        """
        self._consumer_key = environ.get("CONSUMER_KEY")
        self._consumer_secret = environ.get("CONSUMER_SECRET")
        self._access_token = environ.get("ACCESS_TOKEN")
        self._access_token_secret = environ.get("ACCESS_TOKEN_SECRET")

        self.message = message.message
        self.api = self._build_api()

    def tweet(self):
        self.api.update_status(self.message)

    def _build_api(self):
        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)

        return tweepy.API(auth)

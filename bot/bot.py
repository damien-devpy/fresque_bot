from os import environ

import requests
from counter.counter import Counter
from message.message import Message
from twitter.twitter import Twitter


class Bot:
    """Twitter bot.

    In ordre to promote the Climat Collage, the point is to display regularly the animation counter
    and links to workshops.
    """

    def __init__(self):
        """Create a bot.

        self.counter (Counter object): An object containing the animation counter
        self.message (Message object): Message object computing pre registered message from counter
        self.twitter (Twitter API)
        """

        self.counter = self._set_counter()
        self.message = self._set_message()
        self.twitter = self._set_twitter()

    def tweet(self):
        self._tweet()

    def _set_counter(self):
        response = requests.get(environ.get("URL"))
        counter = Counter(response.text)
        counter.extract_counter()
        return counter

    def _set_message(self):
        message = Message(self.counter)
        message.compute_message()
        return message

    def _set_twitter(self):
        twitter = Twitter(self.message)
        return twitter

    def _tweet(self):
        self.twitter.tweet()

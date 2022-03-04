class Counter:
    """Counter object used to extract the number of person reached."""

    def __init__(self, content):
        """Create a Counter object in order to extract the count.
        Args:

            self.content (dict)
            self.counter (string)
        """

        self.content = content
        self.counter = self.extract_counter()

    def extract_counter(self):
        return self.content['data']['rows'][0][0]

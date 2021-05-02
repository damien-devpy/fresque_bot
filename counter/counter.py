import re

from lxml.html import fromstring

from .missingcounterexception import MissingCounterException


class Counter:
    """Counter object used to extract the number of person reached from an HTML body."""

    REGEX = r"(?P<participants>participants[#,:\\\w]*rows[\\\w:]*(?P<number>[0-9]{6,}))"

    def __init__(self, content):
        """Create a Counter object in order to extract the count.
        Args:

            self.content (string): HTML body from where we need to extract the counter
            self.counter (string): Count extract from content. Default to None.
        """

        self.content = self._extract_javascript(content)
        self.counter = None

    def extract_counter(self):
        """Extract the counter from the obsfucated javascript."""

        match = re.search(self.REGEX, self.content)
        if match:
            self.counter = match["number"]
        # Extract with a regex is pretty fragile, so we need to be prepare that it could break
        else:
            raise MissingCounterException("Counter can't be found")

    def _extract_javascript(self, content):
        """Interesting data are located in obfuscated javascript.

        The point is to parse HTML, get the right script balise and return is content.
        """

        content_as_html = fromstring(content)
        js = content_as_html.xpath(
            "//div[@id='embed_chart']//following-sibling::script[2]"
        )[0]

        return js.text

class Solution:

    def __init__(self):
        self.urls = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1

        short_url = str(self.counter)
        self.urls[short_url] = longUrl

        return short_url

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]
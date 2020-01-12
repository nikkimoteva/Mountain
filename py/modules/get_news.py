from newsapi import NewsApiClient


class NewsClient:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key)

    def yield_articles(self, query, category, language, country):
        top_headlines = self.newsapi.get_top_headlines(
            query, category, language, country)
        for article in news_json["articles"]:
            yield article

from newsapi import NewsApiClient


class NewsClient:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key)

    def yield_headlines(self, query, category, country):
        top_headlines = self.newsapi.get_top_headlines(
            query, category, country)
        for headline in top_headlines["articles"]:
            yield headline

    def get_articles(self, query, language):
        articles = self.newsapi.get_everything(
            query, language, sort_by="relevancy", page_size=10)
        return articles["articles"]

from modules.get_news import NewsClient
from modules.azure_connect import yield_sentiments
from modules import helpers
import config
import db


def main():
    newsapi = NewsClient(config.GOOGLE_NEWS_API_KEY)
    countries_permutations = helpers.yield_permutations(db.countries)
    for permutation in countries_permutations:
        origin = permutation["country_origin"]
        targets = permutation["target_origins"]
        average_sentiments = []
        for target in targets:
            hash_id = helpers.commutative_md5(
                origin["country"], target["country"])
            query = origin["country"] + ", " + target["country"]
            articles = newsapi.get_articles(query, language="en")

            document = helpers.contruct_document(articles)

            sentiments = yield_sentiments(
                config.AZURE_SENTIMENT_URL, config.AZURE_API_KEY, document)
            avg_sentiment = helpers.get_mean_sentiments(sentiments)
            average_sentiments.append({
                "target": target["code"],
                "sentiment": avg_sentiment
            })
            # print(hash_id, avg_sentiment)
            # print(hash_id, document)
        print({"origin": origin, "sentiments": average_sentiments})


if __name__ == "__main__":
    main()

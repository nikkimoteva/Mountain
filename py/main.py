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
        for target in targets:
            hash_id = helpers.commutative_md5(
                origin["country"], target["country"])
            query = origin["country"] + ", " + target["country"]
            articles = newsapi.get_articles(query, language="en")
            document = helpers.contruct_document(articles)
            sentiments = yield_sentiments(
                config.AZURE_SENTIMENT_URL, config.AZURE_API_KEY, document)
            for sent in sentiments:
                print(sent)
    # news = get news generator
    # process news ->
    # for n in news:
    #   POST(n, firebase_data)
    #   POST(n, azure_ml)
    #   .then(sentiment => {
    #     POST(sentiment, firebase_sentiments)
    #   })
    #   .catch(err => print(err))


if __name__ == "__main__":
    main()

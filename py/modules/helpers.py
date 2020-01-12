from hashlib import md5


# def yield_permutations(config_countries):
#     for i in range(len(config_countries) - 1):
#         country_origin = config_countries[i]
#         country_targets = config_countries[i + 1:]
#         permutation = {
#             "country_origin": country_origin,
#             "target_origins": country_targets
#         }
#         yield permutation

def yield_permutations(config_countries):
    for i in range(len(config_countries)):
        country_origin = config_countries[i]
        country_targets = config_countries[:i] + config_countries[i + 1:]
        permutation = {
            "country_origin": country_origin,
            "target_origins": country_targets
        }
        yield permutation


def commutative_md5(str1, str2):
    sorted_str = "".join(sorted(str1 + str2)).encode("utf-8")
    m = md5()
    m.update(sorted_str)
    return m.hexdigest()


def contruct_document(articles):
    documents = []
    id_n = 0
    for article in articles:
        try:
            documents.append({
                "id": id_n,
                "text": article["title"] + ". " + article["description"]
            })
        except:
            documents.append({
                "id": id_n,
                "text": "Neutral"
            })
        id_n += 1
    return {"documents": documents}


def get_mean_sentiments(sentiments):
    avg = 0
    counter = 0
    for sent in sentiments:
        avg += sent["score"]
        counter += 1
    if counter == 0:
        return 0
    return avg / counter

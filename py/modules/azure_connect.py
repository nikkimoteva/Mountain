import requests


def yield_sentiments(resource_url, subscription_key, document):
    # assume no errors exist
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(resource_url, headers=headers, json=document)

    res = response.json()["documents"]
    for sentiment in res:
        yield sentiment


# def language(documents):
#     lang = [dict() for x in range(len(document["document"]))]
#     d = {}
#     for i in range(len(document["document"])):
#             #lang[i]["data"] = "en"
#             title = document["document"][i]["title"].rsplit(" -", 1)[0]
#             #lang[i]["countryHint"] = "US"
#             lang[i]["id"] = str(i)
#             if document["document"][i]["source"]['name'] == 'Youtube.com':
#                 lang[i]["text"] = title
#             else:
#                 lang[i]["text"] = title + " " + \
#                     document["document"][i]["description"]
#     lang = {"documents": lang}
#     print(lang)
#     AZURE_API_KEY = "7cadd7aa228c4920b0b92cadcd7bb557"
#     ENDPOINT = AZURE_API_ENDPOINT+"/text/analytics/v2.0/languages"
#     endpoint = ENDPOINT
#     headers = {
#         "Ocp-Apim-Subscription-Key": AZURE_API_KEY
#     }
#     req = requests.post(url=endpoint, json=lang, headers=headers)
#     language = req.json()["documents"]
#     print(language)
#     return language


# def sentiments(document):
#     languages = language(document)
#     text = ""
#     doc_mount = [dict() for x in range(len(document["document"]))]
#     for i in range(len(document["document"])):
#         #doc_mount[i]["id"] = document["document"][i]["url"]
#         doc_mount[i]["id"] = str(i)
#         #doc_mount[i]["language"] = "en" CALL TO LANGUE FUNC HERE
#         title = document["document"][i]["title"].rsplit(" -", 1)[0]
#         if document["document"][i]["source"]['name'] == 'Youtube.com':
#             doc_mount[i]["text"] = title
#         else:
#             doc_mount[i]["text"] = title + " " + \
#                 document["document"][i]["description"]
#         doc_mount[i]["language"] = languages[i]["detectedLanguages"][0]["iso6391Name"]
#     doc_mount = {"documents": doc_mount}
#     print(doc_mount)
#     subscription_key = AZURE_API_KEY
#     endpoint = AZURE_API_ENDPOINT
#     sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"
#     # making a request
#     headers = {"Ocp-Apim-Subscription-Key": subscription_key}
#     # documents is the dictionary
#     response = requests.post(sentiment_url, headers=headers, json=doc_mount)
#     sentiments = response.json()
#     pprint(sentiments["documents"])

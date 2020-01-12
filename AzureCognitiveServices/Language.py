# Date: Saturday, January 12, 2020
# Author: Nikki Moteva
# Purpose: Use Microsoft Azure Cognitive services to get the language that the news headlines and descriptions are in

import requests
import config
from pprint import pprint

def language(document):
    lang = [dict() for x in range(len(document["document"]))]
    d = {}
    for i in range(len(document["document"])):
            #lang[i]["data"] = "en"
            title = document["document"][i]["title"].rsplit(" -", 1)[0]
            #lang[i]["countryHint"] = "US"
            lang[i]["id"] = str(i)
            if document["document"][i]["source"]['name'] == 'Youtube.com':
                lang[i]["text"] = title
            else:
                lang[i]["text"] = title + " " + document["document"][i]["description"]
    lang = {"documents":lang}
    print(lang)
    subscription_key = config.AZURE_API_KEY
    ENDPOINT = config.AZURE_API_ENDPOINT + "/text/analytics/v2.0/languages"
    endpoint = ENDPOINT
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key
    }
    req = requests.post(url = endpoint, json = lang, headers = headers)
    language = req.json()["documents"]
    #pprint(language)
    return language

#language(documents)


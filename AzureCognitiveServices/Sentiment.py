# Date: Saturday, January 12, 2020
# Author: Nikki Moteva
# Purpose: Use Microsoft Azure Cognitive services to retrieve the sentiments of the news headlines and descriptions

import requests
import config
from pprint import pprint
import os
import data

# add the document receiving here


def sentiments(document):
    languages = data.language(document)
    text = ""
    doc_mount = [dict() for x in range(len(document["document"]))]
    for i in range(len(document["document"])):
        doc_mount[i]["id"] = str(i)
        title = document["document"][i]["title"].rsplit(" -", 1)[0]
        if document["document"][i]["source"]['name'] == 'Youtube.com':
            doc_mount[i]["text"] = title
        else:
            doc_mount[i]["text"] = title + " " + document["document"][i]["description"]
        doc_mount[i]["language"] = languages[i]["detectedLanguages"][0]["iso6391Name"]
    doc_mount = {"documents":doc_mount}
    print(doc_mount)
    subscription_key = config.AZURE_API_KEY
    endpoint = config.AZURE_API_ENDPOINT
    sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"
    # making a request
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    # documents is the dictionary
    response = requests.post(sentiment_url, headers=headers, json=doc_mount)
    sentiments = response.json()
    #pprint(sentiments["documents"])

sentiments(document)
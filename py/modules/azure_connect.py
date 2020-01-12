import requests


def yield_sentiments(resource_url, subscription_key, document):
    # assume no errors exist
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(resource_url, headers=headers, json=document)
    for sentiment in response.json()["documents"]:
        yield sentiment

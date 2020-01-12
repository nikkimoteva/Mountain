import requests


def yield_sentiments(document, resource_url, subscription_key):
    # assume no errors exist
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(resource_url, headers=headers, json=document)
    for sentiment in response.json()["documents"]:
        yield sentiment

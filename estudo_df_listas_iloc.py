import requests
import pandas as pd

url_bacen = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json'
url = url_bacen

def coleta_api(url):
    api_bacen= requests.get(url)
    json_bacen = api_bacen.json()
    pd.json_normalize(json_bacen)
    df = pd.read_json(url_bacen)
    return df

df = coleta_api(url)

print(df)



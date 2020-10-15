import requests
from .models import CurrencyRate


def get_rate(base, quote='usdt', reverse=False):
    url = f'https://api.huobi.pro/market/trade?symbol={base}{quote}'
    data = requests.get(url.format(base, quote)).json()
    if data['status'] == 'ok':
        rate = float(data['tick']['data'][0]['price'])
        return rate
    return 0.0
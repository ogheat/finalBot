import blockcypher
from blockcypher.constants import UNIT_CHOICES, UNIT_MAPPINGS

import requests

COINAPI_KEY = "4BBD01E1-75BD-4010-843C-FFBAE2C073AE"

url = 'https://rest.coinapi.io/v1/exchangerate/LTC/RUB'
headers = {'X-CoinAPI-Key': COINAPI_KEY}


def to_satoshis(input_quantity, input_type):
    assert input_type in UNIT_CHOICES, input_type
    if input_type in ('btc', 'mbtc', 'bit'):
        satoshis = float(input_quantity) * float(UNIT_MAPPINGS[input_type]['satoshis_per'])
    elif input_type == 'satoshi':
        satoshis = input_quantity
    else:
        raise Exception('Invalid Unit Choice: %s' % input_type)

    return int(satoshis)


def from_satoshis(input_satoshis, output_type):
    if output_type in ('btc', 'mbtc', 'bit'):
        return input_satoshis / float(UNIT_MAPPINGS[output_type]['satoshis_per'])
    elif output_type == 'satoshi':
        return int(input_satoshis)
    else:
        raise Exception('Invalid Unit Choice: %s' % output_type)


def rub_to_ltc(rub: int):
    response = int(requests.get(url, headers=headers).json()["rate"])
    return  format(float(rub / response), '.8f')

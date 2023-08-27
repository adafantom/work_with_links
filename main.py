import os
import requests
from urllib.parse import urlparse, urlunparse


API_KEY = os.environ['API_KEY']
headers = {
        "Authorization": "Bearer {}".format(API_KEY)
    } 


def shorten_link(API_KEY, long_link):
    payload = {
        'long_url': long_link
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(API_KEY, user_link):
    parsed = urlparse(user_link)
    bitlink = parsed.netloc + parsed.path
    payload = {
        'bitlink': bitlink,
        "units": -1
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(user_link):
    parsed = urlparse(user_link)
    bitlink = parsed.netloc + parsed.path
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(bitlink)
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    try:
        user_link = input('Введите ссылку: ')
        if is_bitlink(user_link):
            return 'Количество посещений: ' + str(count_clicks(API_KEY, user_link))
        else:
            return 'Сокращенная ссылка: ' + shorten_link(API_KEY, user_link)
    except requests.exceptions.HTTPError as error:
        return "Can't get data from server:\n{0}".format(error)


if __name__ == "__main__":
    print(main())
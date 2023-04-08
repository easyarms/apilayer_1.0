from datetime import datetime
import requests
import json

import os

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CURRENCY_RATES_FILE = 'currency_rates.json'


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод ')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:S')

        print(f'Курс {currency} к RUB: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберете действие (1 - продолжить, 2 - выйти): ')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Некорректный ввод ')


def get_currency_rate(base: str) -> float:
    """Получает курс валюты от API и возвращает float"""
    url = "https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в файл JSON"""
    with open(CURRENCY_RATES_FILE, 'a') as file:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], file)
        else:
            with open(CURRENCY_RATES_FILE) as file:
                data_list = json.load(file)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as file:
                json.dump(data_list, file)


if __name__ == '__main__':
    main()

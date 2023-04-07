from datetime import datetime


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод ')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

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


def get_currency_rate(base):
    pass

def save_to_json(base):
    pass


if __name__ == '__main__':
    main()

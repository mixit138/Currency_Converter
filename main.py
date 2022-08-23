import requests

my_currency = input()
my_currency = my_currency.upper()
r = requests.get(f'http://www.floatrates.com/daily/{my_currency.lower()}.json')
currency = r.json()
if my_currency == 'USD':
    currency_rate = {'EUR': currency['eur']['inverseRate']}
elif my_currency == 'EUR':
    currency_rate = {'USD': currency['usd']['inverseRate']}
else:
    currency_rate = {'USD': currency['usd']['inverseRate'], 'EUR': currency['eur']['inverseRate']}

while True:
    exchange_currency = input()
    exchange_currency = exchange_currency.upper()
    if len(exchange_currency) == 3:
        my_money = float(input())
        print('Checking the cache...')
        if exchange_currency in currency_rate:
            print('Oh! It is in the cache!')
            result = my_money / currency_rate[f'{exchange_currency}']
            print(f'You received {result} {exchange_currency}.')
        elif exchange_currency not in currency_rate:
            currency_rate[f'{exchange_currency}'] = currency[f'{exchange_currency.lower()}']['inverseRate']
            print('Sorry, but it is not in the cache!')
            result = my_money / currency_rate[f'{exchange_currency}']
            print(f'You received {result} {exchange_currency}.')
    else:
        break

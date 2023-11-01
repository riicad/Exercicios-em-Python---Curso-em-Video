import requests

cores = {'red': '\033[1;31m',
         'yellow': '\033[1;33m'}

try:
    on = requests.get('http://pudim.com.br/')
    on.raise_for_status()

except requests.exceptions.HTTPError:
    print()
    print(f'{cores["red"]}O site não está acessível.')

else:
    print()
    print(f'{cores["yellow"]}O site está acessível.')

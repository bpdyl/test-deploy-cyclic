import requests
import time

def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    else:
        return 'Failed to fetch a quote'

while True:
    print(fetch_random_quote())
    time.sleep(5)  # Add a delay to avoid flooding the console with quotes

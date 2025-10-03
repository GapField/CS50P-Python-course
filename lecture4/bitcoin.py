import requests
import sys

try:
    if not len(sys.argv) == 2:
        print("Mising command-line arugement")
    else:
        amount = int(sys.argv[1])
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=5c600cc9acc44873bcc32c4b083a67d6579de383aee13564d02f3ba4355969fc")
        data = r.json()
        assets = data["data"]
        market_cap = float(assets['marketCapUsd'])
        end_price = amount*market_cap
        print(f"Bitcoin cost: {end_price:,.2f}")
except requests.RequestException as e:
    print("error: ", e)
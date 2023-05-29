import os

from krakenpy import Kraken, exceptions, payloads

kraken = Kraken(
    api_key=os.environ["API_KEY_KRAKEN"],
    api_secret=os.environ["API_SEC_KRAKEN"],
)

try:
    results = kraken.get_ledgers(
        payload=payloads.LedgersPayload(
            type="deposit",
        )
    )
    print(results)
except exceptions.KrakenError as e:
    print(e)

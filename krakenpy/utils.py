import time

from .exceptions import KrakenError
from .response import Response


def gen_nonce():
    return int(1000 * time.time())


def verified(method: str, response: Response):
    if response["error"]:
        raise KrakenError(method=method, errors=response["error"])
    return response["result"]

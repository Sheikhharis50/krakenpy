import time

from .exceptions import KrakenError
from .response import Response


def gen_nonce():
    return int(1000 * time.time())


def remove_none(_dict, dict_only: bool = False):
    """Remove None values recursively from all of the dictionaries, tuples, lists, sets"""
    if isinstance(_dict, dict):
        for key, value in list(_dict.items()):
            if isinstance(value, (list, dict, tuple, set)):
                _dict[key] = remove_none(value)
            elif value is None or key is None:
                del _dict[key]

    elif not dict_only and isinstance(_dict, (list, set, tuple)):
        _dict = type(_dict)(remove_none(item) for item in _dict if item is not None)

    return _dict


def verified(method: str, response: Response):
    if response["error"]:
        raise KrakenError(method=method, errors=response["error"])
    return response["result"]

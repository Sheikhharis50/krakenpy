# krakenpy

krakenpy is a python integration for kraken API. This package is using `krakenex` underneath, because `krakenex` only provides two methods `query_private` and `query_public` and it's really hard to guess the request params. Therefore, I have introduced Python `Typing` and `dataclasses` to readability.

## Installation

```
pip install krakenpy
```

or

```
poetry add krakenpy
```

## Usage

```
from krakenpy import Kraken, KrakenError

if __name__ == "__main__":
    kraken = Kraken(
        api_key="KRAKEN_API_KEY",
        api_secret="KRAKEN_API_SECRET",
    )

    # Returns the Kraken server status.
    print(kraken.get_status())

```

## Authors

- [Sheikh Haris Zahid](https://github.com/sheikhharis50)

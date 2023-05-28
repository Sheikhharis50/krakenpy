import os

import pytest

from krakenpy.service import Kraken


@pytest.fixture
def service():
    return Kraken(
        api_key=os.environ["API_KEY_KRAKEN"],
        api_secret=os.environ["API_SEC_KRAKEN"],
    )


def test_client_creation(service: Kraken):
    import krakenex

    assert type(service.client) == krakenex.API

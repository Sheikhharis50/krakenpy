import krakenex

from .payloads import AccountBalance, Payload, TradesHistory
from .utils import verified


class Kraken:
    TIMEOUT = 60  # sec

    def __init__(
        self, api_key: str | None = None, api_secret: str | None = None
    ) -> None:
        self.client = self._get_client(api_key, api_secret)

    def _get_client(self, api_key: str | None = None, api_secret: str | None = None):
        """Create krakenex API client.

        :param api_key: Kraken API key
        :type api_key: str
        :param api_secret: Kraken API Secret
        :type api_secret: str
        :return: krakenex API client
        :rtype: krakenex.API
        """
        return krakenex.API(key=api_key or "", secret=api_secret or "")

    def _call(self, private: bool, method: str, payload: Payload | None = None):
        """Calls public and private krakenAPI using krakenex package

        :param private: Whether API is private or public
        :type private: bool
        :param method: API method provided by kraken
        :type method: str
        :param payload: Request payload requires by API, defaults to None
        :type payload: Payload | None, optional
        :return: Response dictionary from krakenAPI
        :rtype: Response
        """
        query = {
            False: self.client.query_public,
            True: self.client.query_private,
        }

        response = query[private](
            method,
            data=payload.to_dict() if payload else payload,
            timeout=self.TIMEOUT,
        )
        return verified(method, response=response)

    def get_status(self):
        """
        KrakenAPI:
            [Public][Method => SystemStatus]
        description:
            It provides the server status or availability.
        """
        return self._call(private=False, method="SystemStatus")

    def get_trades_history(self):
        """
        KrakenAPI:
            [Private][Method => TradesHistory]
        description:
            It the trades history of buy/sell.
        """
        return self._call(private=True, method="TradesHistory", payload=TradesHistory())

    def get_balance(self):
        """
        KrakenAPI:
            [Private][Method => Balance]
        description:
            It shows the account balance.
        """
        return self._call(private=True, method="Balance", payload=AccountBalance())

    def __del__(self):
        """Closes the krakenex.API session"""
        self.client.close()

import krakenex

from .payloads import (
    AccountBalancePayload,
    LedgersPayload,
    Payload,
    TradeBalancePayload,
    TradesHistoryPayload,
)
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

    def _call(
        self,
        private: bool,
        method: str,
        payload: Payload | None = None,
        timeout: int | None = None,
    ):
        """Calls public and private krakenAPI using krakenex package

        :param private: Whether API is private or public
        :type private: bool
        :param method: API method provided by kraken
        :type method: str
        :param payload: Request payload requires by API, defaults to None
        :type payload: Payload | None, optional
        :param timeout: Request timeout, defaults to None
        :type timeout: int | None, optional
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
            timeout=timeout or self.TIMEOUT,
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

    def get_trades_history(self, payload: TradesHistoryPayload | None = None):
        """
        KrakenAPI:
            [Private][Method => TradesHistory]
        description:
            It fetches the trades history of buy/sell.
        """
        return self._call(
            private=True,
            method="TradesHistory",
            payload=payload or TradesHistoryPayload(),
        )

    def get_ledgers(self, payload: LedgersPayload | None = None):
        """
        KrakenAPI:
            [Private][Method => Ledgers]
        description:
            It fetches the User's ledgers which includes the following types:
            `all`, `deposit`, `withdrawal`, `trade`, `margin`, `rollover`,
            `credit`, `transfer`, `settled`, `staking`, and `sale`
        """
        return self._call(
            private=True,
            method="Ledgers",
            payload=payload or LedgersPayload(),
        )

    def get_balance(self, payload: AccountBalancePayload | None = None):
        """
        KrakenAPI:
            [Private][Method => Balance]
        description:
            It fetches the account balance.
        """
        return self._call(
            private=True,
            method="Balance",
            payload=payload or AccountBalancePayload(),
        )

    def get_trade_balance(self, payload: TradeBalancePayload | None = None):
        """
        KrakenAPI:
            [Private][Method => TradeBalance]
        description:
            It fetches the account balance.
        """
        return self._call(
            private=True,
            method="TradeBalance",
            payload=payload or TradeBalancePayload(),
        )

    def __del__(self):
        """Closes the krakenex.API session"""
        self.client.close()

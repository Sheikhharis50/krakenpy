from dataclasses import asdict, dataclass, field
from typing import Literal

from .utils import gen_nonce, remove_none


@dataclass
class Payload:
    nonce: int = field(init=False, default_factory=gen_nonce)

    def to_dict(self):
        return remove_none(asdict(self), dict_only=True)


TRADE_HISTORY_TYPES = Literal[
    "all",
    "any position",
    "closed position",
    "closing position",
    "no position",
]


@dataclass
class TradesHistoryPayload(Payload):
    trades: bool = field(default=True)
    type: TRADE_HISTORY_TYPES = field(default="all")
    start: int | None = field(default=None)
    end: int | None = field(default=None)
    ofs: int | None = field(default=None)
    consolidate_taker: bool = field(default=True)


LEDGER_TYPES = Literal[
    "all",
    "deposit",
    "withdrawal",
    "trade",
    "margin",
    "rollover",
    "credit",
    "transfer",
    "settled",
    "staking",
    "sale",
]


@dataclass
class LedgersPayload(Payload):
    asset: str = field(default="all")
    aclass: str = field(default="currency")
    type: LEDGER_TYPES = field(default="all")
    start: int | None = field(default=None)
    end: int | None = field(default=None)
    ofs: int | None = field(default=None)
    without_count: bool | None = field(default=None)


@dataclass
class AccountBalancePayload(Payload):
    ...


@dataclass
class TradeBalancePayload(Payload):
    asset: str = field(default="ZUSD")

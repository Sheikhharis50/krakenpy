from dataclasses import asdict, dataclass, field
from typing import Literal

from .utils import gen_nonce


@dataclass
class Payload:
    nonce: int = field(init=False, default_factory=gen_nonce)

    def to_dict(self):
        return asdict(self)


TRADE_HISTORY_TYPES = Literal[
    "all",
    "any position",
    "closed position",
    "closing position",
    "no position",
]


@dataclass
class TradesHistory(Payload):
    trades: bool = field(default=True)
    type: TRADE_HISTORY_TYPES = field(default="all")
    start: int | None = field(default=None)
    end: int | None = field(default=None)
    ofs: int | None = field(default=None)
    consolidate_taker: bool = field(default=True)


@dataclass
class QueryLedgers(Payload):
    id: str | None = field(init=False, default=None)
    trades: bool = field(default=True)

    def add_ids(self, *ledger_ids):
        ids = self.id.split(",") if self.id else []
        self.id = ",".join(ids + list(ledger_ids))


@dataclass
class AccountBalance(Payload):
    ...

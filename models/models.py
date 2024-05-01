# models.py

from dataclasses import dataclass


class Order:
    pass


@dataclass
class Payment:
    id: str
    amount: float
    currency: str
    status: str


class Customer:
    pass


class Card:
    pass


class Webhook:
    pass

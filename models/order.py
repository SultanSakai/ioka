from dataclasses import dataclass
from models.payment import Payment


@dataclass
class Order:
    amount: float
    currency: str
    capture_method: str
    status: str
    id: str
    created_at: str
    updated_at: str
    payment: Payment


example_order = Order(amount=150, currency="KZT", capture_method="AUTO", status="CREATED", id=None, created_at=None,
                      updated_at=None, payment=None)

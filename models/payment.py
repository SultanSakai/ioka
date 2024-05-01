from dataclasses import dataclass


@dataclass
class Payment:
    pan: str
    exp: str
    holder: str
    cvc: str
    save: bool
    id: str
    created_at: str
    updated_at: str
    order_id: str


example_payment = Payment(pan="4242424242424242", exp="12/24", holder="John Doe", cvc="123", save=True, id=None,
                          created_at=None, updated_at=None, order_id=None)

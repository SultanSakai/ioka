from exceptions.exceptions import ioka_api_error
from models.order import example_order, Order
from models.payment import example_payment, Payment
from src.client import IokaAPI
from src.config import api_key, base_url

ioka = IokaAPI(base_url, api_key)

if __name__ == "__main__":
    try:
        # Creating an order
        order = example_order
        payment = example_payment
        make_order = ioka.create_order(order.amount, order.currency)
        print(f"Order created: {make_order}")
        all_orders = ioka.get_all_orders()
        print(f"All orders: {all_orders}")
        make_payment = ioka.create_card_payment(make_order["order"]["id"], payment.pan, payment.exp, payment.holder,
                                                payment.cvc)
        print(f"Payment created: {make_payment}")
    except ioka_api_error as e:
        print(e)

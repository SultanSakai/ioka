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
        make_order = ioka.create_order(order.amount, order.currency)
        print(f"Order created: {make_order}")

        # Getting all orders
        all_orders = ioka.get_all_orders()
        print(f"All orders: {all_orders}")

        # Getting an order by id
        order_by_id = ioka.get_order_by_id(make_order["order"]["id"])
        print(f"Order by id: {order_by_id}")

        # Creating a payment
        payment = example_payment
        make_payment = ioka.create_card_payment(make_order["order"]["id"], payment.pan, payment.exp, payment.holder,
                                                payment.cvc)
        print(f"Payment created: {make_payment}")

        # Getting a payment by id
        payment_by_id = ioka.get_payment(make_order["order"]["id"], make_payment["id"])
        print(f"Payment by id: {payment_by_id}")
    except ioka_api_error as e:
        print(e)

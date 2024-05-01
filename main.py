from src.client import IokaAPI
from exceptions.exceptions import ioka_api_error
from src.config import api_key, base_url

ioka = IokaAPI(base_url, api_key)

if __name__ == "__main__":
    try:
        # Creating an order
        make_order = ioka.create_order(150, "KZT")
        print(f"Order created: {make_order}")
        all_orders = ioka.get_all_orders()
        print(f"All orders: {all_orders}")
        payment = ioka.create_card_payment(make_order["order"]["id"], "4242424242424242", "12/24", "John Doe", "123")
        print(f"Payment created: {payment}")


    except ioka_api_error as e:
        print(f"Ioka API Error: {e}")


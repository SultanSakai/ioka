import requests
from exceptions.exceptions import ioka_api_error


class IokaAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    # func to make a request to the API
    def _make_request(self, method, endpoint, data=None) -> dict:
        headers = {'API-KEY': self.api_key}
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ioka_api_error(e)

    # func to create an order
    def create_order(self, amount, currency) -> dict:
        data = {"amount": amount, "currency": currency, "capture_method": "AUTO"}
        return self._make_request("POST", "/orders", data)

    # func to create a card payment
    def create_card_payment(self, order_id, pan, exp, holder, cvc, save=True) -> dict:
        data = {"pan": pan, "exp": exp, "holder": holder, "cvc": cvc, "save": save}
        endpoint = f"/orders/{order_id}/payments/card"
        return self._make_request("POST", endpoint, data)

    # func to get all orders
    def get_all_orders(self) -> dict:
        return self._make_request("GET", "/orders", None)

    # func to get an order by id
    def get_order_by_id(self, order_id) -> dict:
        return self._make_request("GET", f"/orders/{order_id}", None)

    # func to get a payment by id
    def get_payment(self, order_id, payment_id) -> dict:
        return self._make_request("GET", f"/orders/{order_id}/payments/{payment_id}", None)
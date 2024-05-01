import requests
from exceptions.exceptions import ioka_api_error


class ioka_api:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, method, endpoint, data):
        headers = {
            'API-KEY': self.api_key,
        }
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ioka_api_error(e)

    def create_order(self, amount, currency):
        data = {"amount": amount, "currency": currency, "capture_method": "AUTO"}
        return self._make_request("POST", "/orders", data)

    def create_card_payment(self, order_id, pan, exp, holder, cvc, save=True):
        data = {"pan": pan, "exp": exp, "holder": holder, "cvc": cvc, "save": save}
        endpoint = f"/orders/{order_id}/payments/card"
        return self._make_request("POST", endpoint, data)

    def get_all_orders(self):
        return self._make_request("GET", "/orders", None)
import unittest
from src.models.payment import example_payment
from src.client import IokaAPI
from src.config import api_key, base_url
from unittest.mock import patch

ioka = IokaAPI(base_url, api_key)


class MyTestCase(unittest.TestCase):
    @patch('src.client.IokaAPI._make_request')
    def test_create_payment(self, mock_make_request):
        mock_make_request.return_value = {"status_code": 201}
        response = ioka.create_card_payment(example_payment.order_id,
                                            example_payment.pan, example_payment.exp,
                                            example_payment.holder,
                                            example_payment.cvc)
        self.assertEqual(response, {"status_code": 201})

    @patch('src.client.IokaAPI._make_request')
    def test_get_order(self, mock_make_request):
        mock_make_request.return_value = {"status_code": 200}
        response = ioka.get_order_by_id(1)
        self.assertEqual(response, {"status_code": 200})


if __name__ == '__main__':
    unittest.main()

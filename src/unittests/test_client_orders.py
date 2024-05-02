import unittest
from src.models.order import example_order
from src.client import IokaAPI
from src.config import api_key, base_url
from unittest.mock import patch

ioka = IokaAPI(base_url, api_key)


class MyTestCase(unittest.TestCase):
    @patch('src.client.IokaAPI._make_request')
    def test_create_order_success(self, mock_make_request):
        mock_make_request.return_value = {"status_code": 201}
        response = ioka.create_order(example_order.amount, example_order.currency)
        self.assertEqual(response, {"status_code": 201})


    @patch('src.client.IokaAPI._make_request')
    def test_get_all_orders(self, mock_make_request):
        mock_make_request.return_value = {"status_code": 200}
        response = ioka.get_all_orders()
        self.assertEqual(response, {"status_code": 200})

    @patch('src.client.IokaAPI._make_request')
    def test_get_order(self, mock_make_request):
        mock_make_request.return_value = {"status_code": 200}
        response = ioka.get_order_by_id(1)
        self.assertEqual(response, {"status_code": 200})


if __name__ == '__main__':
    unittest.main()

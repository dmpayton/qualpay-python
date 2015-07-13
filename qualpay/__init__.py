
__version__ = '0.1.0'

merchant_id = None
secret_key = None
base_endpoint = 'https://api.qualpay.com'

from .card import Card
from .error import APIError, GatewayError, HttpError
from .gateway import (PaymentGateway, authorize, verify, capture, sale, void,
    refund, credit, force, tokenize)

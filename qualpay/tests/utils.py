import datetime
import json
import qualpay
import unittest

# Test credit cards
TEST_CARDS = {
    'visa': '4111 1111 1111 1111',
    'mastercard': '5555 5555 5555 4444',
    'discover': '6011 1111 1111 1117',
    'amex': '3714 4963 5392 376',
    'diners': '3855 5565 0100 05',
    'jcb': '3530 1420 1995 5809',
}

# Example responses for API endpoints
RESPONSE = {
    'authorize': json.dumps({
        'rcode': '000',
        'rmsg': 'Approved T63362',
        'pg_id': '8af556ae480811e484b20c4de99f0aaf'
    }),

    'verify': json.dumps({
        'auth_code': 'T42069',
        'auth_cvv2_result': 'M',
        'pg_id': 'e8418d1d706cd73548f9f16f1d55ad6e',
        'rcode': '085',
        'rmsg': 'No reason to decline TT42069'
    }),

    'capture': json.dumps({
        'rcode': '000',
        'rmsg': 'Capture request accepted',
        'pg_id': '52b992ca441611e480a8005056c00008'
    }),

    'sale': json.dumps({
        'rcode': '000',
        'rmsg': 'Approved T42926',
        'pg_id': 'daab5fff480811e484b20c4de99f0aaf'
    }),

    'void': json.dumps({
        'rcode': '000',
        'rmsg': 'Transaction voided',
        'pg_id': 'f0f85062441311e49863005056c00008'
    }),

    'refund': json.dumps({
        'rcode': '000',
        'rmsg': 'Refund request accepted',
        'pg_id': '1c5ff91b480711e4ac850c4de99f0aaf'
    }),

    'tokenize': json.dumps({
        'rcode': '000',
        'rmsg': 'Token request complete',
        'pg_id': '88a4099c480711e4ac850c4de99f0aaf',
        'card_id': '88b4363 d480711e4ac850c4de99f0aaf'
    }),

    'force': json.dumps({
        'rcode': '000',
        'rmsg': 'Force transaction accepted',
        'pg_id': '65824102480c11e484b20c4de99f0aaf'
    }),

    'error': json.dumps({
        'rcode': '999',
        'rmsg': 'Internal error',
        'pg_id': 'cb5e100e5a9a3e7f6d1fd97512215282'
    })
}


class QualpayTests(unittest.TestCase):
    def setUp(self):
        qualpay.merchant_id = 'test'
        qualpay.security_key = 'TEST1234567890'
        qualpay.base_endpoint = 'https://api-test.qualpay.com'

        today = datetime.date.today()
        self.month = today.month
        self.year = today.year

        super(QualpayTests, self).setUp()

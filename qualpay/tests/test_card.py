import datetime
import responses
import unittest
import qualpay

from .utils import RESPONSE, TEST_CARDS, QualpayTests


class CardTests(QualpayTests):
    def test_luhn_valid(self):
        for number in TEST_CARDS.values():
            card = qualpay.Card(number, self.month, self.year, '111')
            self.assertTrue(card.is_luhn_valid)

    def test_luhn_invalid(self):
        card = qualpay.Card('4111111111111112', self.month, self.year, '111')
        self.assertFalse(card.is_luhn_valid)

        card = qualpay.Card('asdf 123', self.month, self.year, '111')
        self.assertFalse(card.is_luhn_valid)
        self.assertEqual(card.mask, 'invalid')

    def test_missing_number(self):
        card = qualpay.Card('', self.month, self.year, '111')
        self.assertFalse(card.is_luhn_valid)
        self.assertEqual(card.mask, 'invalid')

    def test_mask(self):
        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        self.assertEqual(card.mask, 'XXXX-XXXX-XXXX-1111')

        card = qualpay.Card(TEST_CARDS['amex'], self.month, self.year, '111')
        self.assertEqual(card.mask, 'XXXX-XXXXXX-X2376')

    def test_brand(self):
        for brand in ('visa', 'mastercard', 'amex', 'discover'):
            card = qualpay.Card(TEST_CARDS[brand], self.month, self.year, '111')
            self.assertEqual(card.brand, brand)

        card = qualpay.Card(TEST_CARDS['diners'], self.month, self.year, '111')
        self.assertEqual(card.brand, 'unknown')

        card = qualpay.Card(TEST_CARDS['jcb'], self.month, self.year, '111')
        self.assertEqual(card.brand, 'unknown')

    def test_expired(self):
        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year - 1, '111')
        self.assertTrue(card.is_expired)

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year + 1, '111')
        self.assertFalse(card.is_expired)

    def test_expdate_format(self):
        card = qualpay.Card(TEST_CARDS['visa'], 1, 2020, '111')
        self.assertEqual(card.exp_date.mmyyyy, '01/2020')
        self.assertEqual(card.exp_date.mm, '01')
        self.assertEqual(card.exp_date.yyyy, '2020')

    @responses.activate
    def test_gateway_authorize(self):
        endpoint = 'https://api-test.qualpay.com/pg/auth'
        responses.add(responses.POST, endpoint, body=RESPONSE['authorize'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        response = card.authorize(1)

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_gateway_verify(self):
        endpoint = 'https://api-test.qualpay.com/pg/verify'
        responses.add(responses.POST, endpoint, body=RESPONSE['verify'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        response = card.verify()

        assert isinstance(response, dict)
        assert response.get('rcode') == '085'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_gateway_sale(self):
        endpoint = 'https://api-test.qualpay.com/pg/sale'
        responses.add(responses.POST, endpoint, body=RESPONSE['sale'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        response = card.sale(1)

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_tokenize(self):
        endpoint = 'https://api-test.qualpay.com/pg/tokenize'
        responses.add(responses.POST, endpoint, body=RESPONSE['tokenize'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        response = card.tokenize()

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

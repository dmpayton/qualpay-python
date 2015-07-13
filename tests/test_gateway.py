import datetime
import qualpay
import responses
import unittest

from .utils import RESPONSE, TEST_CARDS


class GatewayTests(unittest.TestCase):
    def setUp(self):
        qualpay.merchant_id = 'test'
        qualpay.security_key = 'TEST1234567890'
        qualpay.base_endpoint = 'https://api-test.qualpay.com'

        today = datetime.date.today()
        self.month = today.month
        self.year = today.year

        super(GatewayTests, self).setUp()

    @responses.activate
    def test_authorize(self):
        endpoint = 'https://api-test.qualpay.com/pg/auth'
        responses.add(responses.POST, endpoint, body=RESPONSE['authorize'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        gateway = qualpay.PaymentGateway()
        response = gateway.authorize(
            card_number=card.number,
            exp_date=card.exp_date.mmyy,
            cvv2=card.cvv2,
            amt_tran=1,
        )

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_capture(self):
        pg_id = 'd7ba9bbfda42b9657f14ee37ef76150b'
        endpoint = 'https://api-test.qualpay.com/pg/capture/{0}'.format(pg_id)

        responses.add(responses.POST, endpoint, body=RESPONSE['capture'],
            content_type='application/json')

        gateway = qualpay.PaymentGateway()
        response = gateway.capture(pg_id)

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_sale(self):
        endpoint = 'https://api-test.qualpay.com/pg/sale'
        responses.add(responses.POST, endpoint, body=RESPONSE['sale'],
            content_type='application/json')

        card = qualpay.Card(TEST_CARDS['visa'], self.month, self.year, '111')
        gateway = qualpay.PaymentGateway()
        response = gateway.sale(
            card_number=card.number,
            exp_date=card.exp_date.mmyy,
            cvv2=card.cvv2,
            amt_tran=1,
        )

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_void(self):
        pg_id = 'cab8111fd0b710a336c898e539090e34'
        endpoint = 'https://api-test.qualpay.com/pg/void/{0}'.format(pg_id)

        responses.add(responses.POST, endpoint, body=RESPONSE['void'],
            content_type='application/json')

        gateway = qualpay.PaymentGateway()
        response = gateway.void(pg_id)

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint

    @responses.activate
    def test_refund(self):
        pg_id = 'df6f85687a0d5820baa1a069a04eff2d'
        endpoint = 'https://api-test.qualpay.com/pg/refund/{0}'.format(pg_id)

        responses.add(responses.POST, endpoint, body=RESPONSE['refund'],
            content_type='application/json')

        gateway = qualpay.PaymentGateway()
        response = gateway.refund(pg_id)

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
        gateway = qualpay.PaymentGateway()
        response = gateway.tokenize(
            card_number=card.number,
            exp_date=card.exp_date.mmyy,
            cvv2=card.cvv2,
        )

        assert isinstance(response, dict)
        assert response.get('rcode') == '000'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == endpoint


if __name__ == '__main__':
    unittest.main()

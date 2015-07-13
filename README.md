# qualpay-python
Python bindings for Qualpay

Usage
=====

```
import qualpay

qualpay.merchant_id = 'test'
qualpay.security_key = 'test1234567890'

card = qualpay.Card(
    number='4111 1111 1111 1111',
    exp_month=1,
    exp_year=2020,
    cvv2='111'
)

card.is_valid
response = card.authorize(10)
```

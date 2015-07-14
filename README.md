qualpay-python
==============

[Python](https://www.python.org/) bindings for [Qualpay](https://www.qualpay.com/)

[![Build Status](https://secure.travis-ci.org/dmpayton/qualpay-python.svg?branch=master)](http://travis-ci.org/dmpayton/qualpay-python)
[![Code Climate GPA](https://codeclimate.com/github/dmpayton/qualpay-python/badges/gpa.svg)](https://codeclimate.com/github/dmpayton/qualpay-python)
[![codecov.io](http://codecov.io/github/dmpayton/qualpay-python/coverage.svg?branch=master)](http://codecov.io/github/dmpayton/qualpay-python?branch=master)

Documentation
-------------

[qualpay-python.readthedocs.org](https://qualpay-python.readthedocs.org/)

Basic Usage
-----------

```
>>> import qualpay

>>> qualpay.merchant_id = '<your merchant id>'
>>> qualpay.security_key = '<your security key>'

>>> card = qualpay.Card(
    number='4111 1111 1111 1111',
    exp_month=1,
    exp_year=2020,
    cvv2='111'
)

>>> card.is_valid
True

>>> card.authorize(10)
{
    'rcode': '000',
    'rmsg': 'Approved T63362',
    'pg_id': '8af556ae480811e484b20c4de99f0aaf'
}
```

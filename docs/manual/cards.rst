===============
The card object
===============

The ``qualpay.Card`` object allows you to validate and charge credit cards. It's
essentially a utility class that wraps the ``qualpay.PaymentGateway`` and
provides additional helpers for validating card information before sending
it off to the API.

::

    >>> card = qualpay.Card(
        number='4111 1111 1111 1111',
        exp_month=1,
        exp_year=2020,
        cvv2='111'
    )
    >>> card.is_expired
    False
    >>> card.is_valid
    True
    >>> card.authorize(1)
    {'rcode': '000', 'rmsg': 'Approved T63362', 'pg_id': '8af556ae480811e484b20c4de99f0aaf'}


Gateway helpers
===============

Authorization
-------------

Create an authorization of $10.00::

    >>> card.authorize(10)
    {
        'rcode': '000',
        'rmsg': 'Approved T63362',
        'pg_id': '8af556ae480811e484b20c4de99f0aaf'
    }


Sale
----

Immediately charge $10.00::

    >>> card.sale(10)
    {
        'rcode': '000',
        'rmsg': 'Approved T42926',
        'pg_id': 'daab5fff480811e484b20c4de99f0aaf'
    }

Verify
------

Verify the card information::

    >>> card.verify()
    {
        'rcode': '085',
        'rmsg': 'No reason to decline T19093',
        'pg_id': '299cf38f29b111e5b1460a12fcf6f1a3',
        'auth_cvv2_result': 'M',
        'auth_code': 'T19093'
    }

Tokenize
--------

Tokenize the card::

    >>> card.tokenize()
    {
        'rcode': '000',
        'rmsg': 'Token request complete',
        'pg_id': '88a4099c480711e4ac850c4de99f0aaf',
        'card_id': '88b4363 d480711e4ac850c4de99f0aaf'
    }

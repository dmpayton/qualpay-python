===================
The payment gateway
===================


Authorization
=============

::

    qualpay.authorize(
        card_number='4111111111111111'
        exp_date='0120',
        cvv2='111',
        tran_amt=10
    )

Capture
=======

::

    qualpay.capture(
        pg_id='8af556ae480811e484b20c4de99f0aaf'
    )

Sale
====

::

    qualpay.sale(
        card_number='4111111111111111'
        exp_date='0120',
        cvv2='111',
        tran_amt=10
    )

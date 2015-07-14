===============
Getting Started
===============

Installation
============

::

    $ pip install qualpay

Authentication
==============

::

    import qualpay

    qualpay.merchant_id = '<your merchant id>'
    qualpay.security_key = '<your security key>'


Using the test gateway
======================

To use the test payment gateway (such as during development), set
``qualpay.base_endpoint`` to the correct URL::

    qualpay.base_endpoint = 'https://api-test.qualpay.com'

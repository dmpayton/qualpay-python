=========
Reference
=========

Payment gateway functions
=========================

.. autofunction:: qualpay.authorize

.. autofunction:: qualpay.verify

.. autofunction:: qualpay.capture

.. autofunction:: qualpay.sale

.. autofunction:: qualpay.void

.. autofunction:: qualpay.refund

.. autofunction:: qualpay.credit

.. autofunction:: qualpay.tokenize

.. autofunction:: qualpay.force

qualpay.Card
============

.. autoclass:: qualpay.Card
    :members:

qualpay.PaymentGateway
======================

.. autoclass:: qualpay.PaymentGateway
    :members: authorize, verify, capture, sale, void, refund, credit, tokenize, force

Exceptions
==========

.. autoexception:: qualpay.APIError

.. autoexception:: qualpay.GatewayError

.. autoexception:: qualpay.HttpError

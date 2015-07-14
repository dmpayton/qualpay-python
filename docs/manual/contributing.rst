============
Contributing
============

Reporting bugs
==============

Perhaps the easiest way to contribute to qualpay-python is to report any bugs you
run into on the `github issue tracker <https://github.com/dmpayton/qualpay-python/issues>`_.

Useful bug reports are ones that get bugs fixed. A useful bug report normally
has two qualities:

1. **Reproducible.** If your bug is not reproducible it will never get fixed.
   You should clearly mention the steps to reproduce the bug. Do not assume or
   skip any reproducing step. Described the issue, step-by-step, so that it is
   easy to reproduce and fix.

2. **Specific.** Do not write a essay about the problem. Be Specific and to the
   point. Try to summarize the problem in minimum words yet in effective way.
   Do not combine multiple problems even they seem to be similar. Write
   different reports for each problem.

Writing code
============

Our workflow is based on Vincent Driessen's `successful git branching model
<http://nvie.com/posts/a-successful-git-branching-model/>`_:

* The ``master`` branch is our current release
* The ``develop`` branch is what all pull requests should be based against
* Feature branches are where new features, both major and minor, should be developed.

.. seqdiag:: /_static/git-flow.diag

`git-flow <https://github.com/nvie/gitflow>`_ is a git plugin that helps
facilitate this branching strategy. It's not required, but can help make
things a bit easier to manage. There is also a good write up on
`using git-flow <http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/>`_.

We also request that git commit messages follow the
`standard format <http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_.

Testing
=======

Continuous integration provided by `Travis CI`_.

Test requirements
-----------------

See *requirements.txt*:

.. literalinclude:: ../../requirements.txt

Running the tests
-----------------

Once your requirements are installed, the unit tests can be run with::

    $ py.test tests/ --cov qualpay --cov-report term-missing --pep8 qualpay

    ...

    ==================== 15 passed in 0.15 seconds ====================


For testing against different Python versions, we use `Tox`_.

::

    $ tox

    ...

    _______________ summary _______________
    py27: commands succeeded
    py34: commands succeeded
    congratulations :)


.. _Tox: http://tox.readthedocs.org/
.. _Travis CI: https://travis-ci.org/

Submit a pull request
=====================

You've done your hacking and are ready to submit your patch. Great! Now it's
time to submit a `pull request <https://help.github.com/articles/using-pull-requests>`_
to our `issue tracker <https://github.com/dmpayton/qualpay-python/issues>`_ on Github.

.. important::

    Pull requests are not considered complete until they include all of the
    following:

    * **Code** that conforms to PEP8.
    * **Unit tests** that pass locally and in our CI environment.
    * **Documentation** updates on an as needed basis.

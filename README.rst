.. contents:: **mbstrdecoder**
   :backlinks: top
   :local:


Summary
=======
`mbstrdecoder <https://github.com/thombashi/mbstrdecoder>`__ is a Python library for multi-byte character string decoder.


.. image:: https://badge.fury.io/py/mbstrdecoder.svg
    :target: https://badge.fury.io/py/mbstrdecoder
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/mbstrdecoder.svg
   :target: https://pypi.org/project/mbstrdecoder
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/thombashi/mbstrdecoder/master.svg?label=Linux/macOS%20CI
    :target: https://travis-ci.org/thombashi/mbstrdecoder
    :alt: Linux/macOS CI status

.. image:: https://img.shields.io/appveyor/ci/thombashi/mbstrdecoder/master.svg?label=Windows%20CI
    :target: https://ci.appveyor.com/project/thombashi/mbstrdecoder

.. image:: https://coveralls.io/repos/github/thombashi/mbstrdecoder/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/mbstrdecoder?branch=master
    :alt: Test coverage


Installation
============
::

    pip install mbstrdecoder

or install all of the optional dependencies:

::

    pip install mbstrdecoder[all]


Usage
=====

:Sample Code:
    .. code:: python

        from __future__ import print_function
        from mbstrdecoder import MultiByteStrDecoder

        encoded_multibyte_text = "マルチバイト文字".encode("utf-8")
        decoder = MultiByteStrDecoder(encoded_multibyte_text)

        print("encoded bytes: {}".format(encoded_multibyte_text))
        print("unicode: {}".format(decoder.unicode_str))
        print("codec: {}".format(decoder.codec))

:Output:
    ::

        encoded bytes: b'\xe3\x83\x9e\xe3\x83\xab\xe3\x83\x81\xe3\x83\x90\xe3\x82\xa4\xe3\x83\x88\xe6\x96\x87\xe5\xad\x97'
        unicode: マルチバイト文字
        codec: utf_8


Dependencies
============
Python 2.7+ or 3.4+

Optional dependencies
----------------------------------
- `chardet <https://github.com/chardet/chardet>`__

Test dependencies
----------------------------------
- `pytest <https://pypi.org/project/pytest>`__
- `pytest-runner <https://github.com/pytest-dev/pytest-runner>`__
- `six <https://pypi.org/project/six/>`__
- `tox <https://pypi.org/project/tox>`__

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

.. image:: https://img.shields.io/pypi/implementation/mbstrdecoder.svg
    :target: https://pypi.org/project/mbstrdecoder
    :alt: Supported Python implementations

.. image:: https://github.com/thombashi/mbstrdecoder/actions/workflows/lint_and_test.yml/badge.svg
    :target: https://github.com/thombashi/mbstrdecoder/actions/workflows/lint_and_test.yml
    :alt: CI status of Linux/macOS/Windows

.. image:: https://coveralls.io/repos/github/thombashi/mbstrdecoder/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/mbstrdecoder?branch=master
    :alt: Test coverage

.. image:: https://github.com/thombashi/mbstrdecoder/actions/workflows/codeql-analysis.yml/badge.svg
    :target: https://github.com/thombashi/mbstrdecoder/actions/workflows/codeql-analysis.yml
    :alt: CodeQL


Installation
============

Install from PyPI
------------------------------
::

    pip install mbstrdecoder

Install from PPA (for Ubuntu)
------------------------------
::

    sudo add-apt-repository ppa:thombashi/ppa
    sudo apt update
    sudo apt install python3-mbstrdecoder


Usage
=====

:Sample Code:
    .. code:: python

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
- Python 3.7+
- `Python package dependencies (automatically installed) <https://github.com/thombashi/mbstrdecoder/network/dependencies>`__

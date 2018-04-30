# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

from textwrap import dedent

import pytest
from mbstrdecoder._func import *


@pytest.mark.parametrize(["value", "expected"], [
    ["utf8", "utf8"],
    ["utf-8", "utf_8"],
    ["UTF8", "utf8"],
    ["UTF-8", "utf_8"],
    [None, None],
])
def test_to_codec_name(value, expected):
    assert to_codec_name(value) == expected

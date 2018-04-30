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


@pytest.mark.parametrize(["value", "expected"], [
    ["utf8", "utf_8"],
    ["utf16", "utf_16"],
])
def test_detect_file_encoding(tmpdir, value, expected):
    data = dedent("""\
        # ほげほげ -----
        print(con.get_attr_name_list(table_name))
        result = con.select(select="*", table_name=table_name)
        for record in result.fetchall():
        print(record)
        """)
    p_csv = tmpdir.join("test_detect_file_encoding")

    with open(str(p_csv), "wb") as f:
        f.write(data.encode(value))

    assert detect_file_encoding(str(p_csv)) == expected

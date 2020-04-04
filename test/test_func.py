"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import os
import platform
from textwrap import dedent

import pytest

from mbstrdecoder._func import detect_file_encoding, to_codec_name


@pytest.mark.parametrize(
    ["value", "expected"],
    [["utf8", "utf8"], ["utf-8", "utf_8"], ["UTF8", "utf8"], ["UTF-8", "utf_8"], [None, None]],
)
def test_to_codec_name(value, expected):
    assert to_codec_name(value) == expected


class Test_detect_file_encoding:
    @pytest.mark.parametrize(["value", "expected"], [["utf8", "utf_8"], ["utf16", "utf_16"]])
    def test_normal(self, tmpdir, value, expected):
        data = dedent(
            """\
            # ほげほげ -----
            print(con.fetch_attr_name_list(table_name))
            result = con.select(select="*", table_name=table_name)
            for record in result.fetchall():
            print(record)
            """
        )
        p_csv = tmpdir.join("test_detect_file_encoding")

        with open(str(p_csv), "wb") as f:
            f.write(data.encode(value))

        assert detect_file_encoding(str(p_csv)) == expected

    @pytest.mark.skipif(platform.system() == "Windows", reason="platform dependent tests")
    def test_normal_fifo(self, tmpdir):
        fifo = tmpdir.join("test_fifo")

        os.mkfifo(str(fifo))

        assert detect_file_encoding(str(fifo)) is None

    def test_abnormal(self, tmpdir):
        fifo = tmpdir.join("not_exist_fifo")

        assert detect_file_encoding(str(fifo)) is None

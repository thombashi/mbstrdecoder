# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

from os.path import splitext

import pytest
from faker import Factory
from mbstrdecoder._binary_ext_checker import binary_exts, is_binary_ext_path


fake = Factory.create()
fake.seed(1)


@pytest.mark.parametrize(
    ["value", "expected"],
    [[".".join([splitext(fake.file_path())[0], binary_ext]), True] for binary_ext in binary_exts]
    + [["hoge.txt", False], ["foo.md", False]],
)
def test_is_binary_ext_path(value, expected):
    assert is_binary_ext_path(value) == expected

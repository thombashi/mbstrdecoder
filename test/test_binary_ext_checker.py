"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from os.path import splitext

import pytest

from mbstrdecoder._binary_ext_checker import binary_exts, is_binary_ext_path


try:
    from faker import Factory  # noqa

    FAKER_INSTALLED = True
except ImportError:
    FAKER_INSTALLED = False

if FAKER_INSTALLED:
    fake = Factory.create()
    fake.seed(1)

    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            [".".join([splitext(fake.file_path())[0], binary_ext]), True]
            for binary_ext in binary_exts
        ]
        + [["hoge.txt", False], ["foo.md", False]],
    )
    def test_is_binary_ext_path(value, expected):
        assert is_binary_ext_path(value) == expected

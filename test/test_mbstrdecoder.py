# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import unicode_literals

import pytest

from mbstrdecoder import *


nan = float("nan")
inf = float("inf")


class Test_to_MultiByteStrDecoder_unicode:

    @pytest.mark.parametrize(["value", "expected"], [
        ["abcdefgh", "abcdefgh"],
        ["吾輩は猫である", "吾輩は猫である"],
        [None, "None"],
        ["", ""],
        [True, "True"],
        [[], u"[]"],
        [1, u"1"],
    ])
    def test_normal(self, value, expected):
        assert MultiByteStrDecoder(value).unicode_str == expected

    @pytest.mark.parametrize(["value", "codec"], [
        ["いろはにほへと", "utf_7"],
        [
            "RKBTqn1G9HIZ9onY9mCklj3+8ye7WBmu0xKMqp3ORT3pMgR5m73VXAR/5YrTZTGernMYLCPYdwIMewFY+6xOZmWwCrXjfw3sO2dYLubh9EIMrc/XEvAhMFd969G2yQkyFTNf9M8Ag94QCuBk51yQLSbxgmxJTqEw6bdC4gNTI44=",
            "ascii"
        ],
        ["マルチバイト文字", "utf_8"],
        ["ＡＢＣ", "utf_8"],
        ["吾輩は猫である", "utf_16"],
    ])
    def test_normal_encoding(self, value, codec):
        decoder = MultiByteStrDecoder(value.encode(codec))

        assert decoder.codec == codec
        assert decoder.unicode_str == value

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import pytest

from mbstrdecoder import MultiByteStrDecoder


nan = float("nan")
inf = float("inf")


class Test_to_MultiByteStrDecoder_repr:
    @pytest.mark.parametrize(["value", "expected"], [["吾輩は猫である", "codec=unicode, unicode=吾輩は猫である"]])
    def test_normal(self, value, expected):
        decoder = MultiByteStrDecoder(value)

        assert str(decoder) == expected


class Test_to_MultiByteStrDecoder_unicode:
    @pytest.mark.parametrize(["value", "expected"], [[b"", ""], [b"abcd", "abcd"]])
    def test_normal_unicode_str(self, value, expected):
        decoder = MultiByteStrDecoder(value)
        assert decoder.unicode_str == expected

    @pytest.mark.parametrize(
        ["value", "encode", "expected"],
        [["", "utf8", "unicode"], ["abcdefgh", "ascii", "ascii"], ["吾輩は猫である", "utf8", "utf_8"]],
    )
    def test_normal_codec(self, value, encode, expected):
        decoder = MultiByteStrDecoder(value.encode(encode))
        assert decoder.codec == expected
        assert decoder.unicode_str == value

    @pytest.mark.parametrize(
        ["value", "encode", "expected", "codec_candidates"],
        [
            ["abcdefgh", "ascii", "ascii", ["utf_32_le", "utf_32"]],
            ["吾輩は猫である", "utf8", "utf_8", ["utf_32_le", "ascii"]],
            ["吾輩は猫である", "utf8", "utf_8", None],
            ["吾輩は猫である", "utf8", "utf_8", []],
            ["Bob’s Burgers", "windows-1252", "windows_1252", []],
        ],
    )
    def test_normal_codec_candidate(self, value, encode, expected, codec_candidates):
        decoder = MultiByteStrDecoder(value.encode(encode), codec_candidates)
        assert decoder.codec == expected
        assert decoder.unicode_str == value

    @pytest.mark.parametrize(
        ["value", "codec"],
        [
            ["いろはにほへと", "utf_7"],
            [
                "RKBTqn1G9HIZ9onY9mCklj3+8ye7WBmu0xKMqp3ORT3pMgR5m73VXAR/5YrTZTGernMYLCPYdwIMewFY+6xOZmWwCrXjfw3sO2dYLubh9EIMrc/XEvAhMFd969G2yQkyFTNf9M8Ag94QCuBk51yQLSbxgmxJTqEw6bdC4gNTI44=",  # noqa
                "ascii",
            ],
            ["マルチバイト文字", "utf_8"],
            ["ＡＢＣ", "utf_8"],
            ["吾輩は猫である", "utf_16"],
        ],
    )
    def test_normal_encoding(self, value, codec):
        decoder = MultiByteStrDecoder(value.encode(codec))

        assert decoder.codec == codec
        assert decoder.unicode_str == value

    @pytest.mark.parametrize(
        ["value", "expected"],
        [[None, ValueError], [True, ValueError], [[], ValueError], [1, ValueError]],
    )
    def test_exception(self, value, expected):
        with pytest.raises(expected):
            MultiByteStrDecoder(value)

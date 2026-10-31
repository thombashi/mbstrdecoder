"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import pytest

from mbstrdecoder import MultiByteStrDecoder


nan = float("nan")
inf = float("inf")


class Test_to_MultiByteStrDecoder_repr:
    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            ["吾輩は猫である", "codec=unicode, unicode=吾輩は猫である"],
        ],
    )
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
        [
            ["", "utf8", "unicode"],
            ["abcdefgh", "ascii", "ascii"],
            ["吾輩は猫である", "utf8", "utf_8"],
        ],
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
        [
            [None, ValueError],
            [True, ValueError],
            [[], ValueError],
            [1, ValueError],
        ],
    )
    def test_exception(self, value, expected):
        with pytest.raises(expected):
            MultiByteStrDecoder(value)


class Test_codec_candidates:
    @pytest.mark.parametrize("value", ["", "plain", "吾輩は猫である", b"", b"plain"])
    @pytest.mark.parametrize("container", [list, tuple])
    def test_caller_candidates_unchanged(self, value, container):
        candidates = container(["utf_8", "ascii", "utf_8"])
        before = candidates[:]

        first = MultiByteStrDecoder(value, candidates)
        second = MultiByteStrDecoder(value, candidates)

        assert candidates == before
        assert (first.unicode_str, first.codec) == (second.unicode_str, second.codec)

    @pytest.mark.parametrize("detected", [None, "latin_1", "detected_codec"])
    def test_order_and_independent_lists(self, monkeypatch, detected):
        monkeypatch.setattr(
            MultiByteStrDecoder,
            "_MultiByteStrDecoder__detect_encoding_helper",
            staticmethod(lambda value: detected),
        )
        defaults = MultiByteStrDecoder._MultiByteStrDecoder__CODECS[:]
        candidates = ["utf_8", "utf_8", "unknown_codec", ""]
        decoder = MultiByteStrDecoder("plain", candidates)
        other = MultiByteStrDecoder("other")
        expected = defaults[:]
        if detected:
            if detected in expected:
                expected.remove(detected)
            expected.insert(0, detected)
        expected = candidates + [name for name in expected if name not in candidates]

        first = decoder._MultiByteStrDecoder__get_codec_candidate_list(b"plain")
        assert first == expected
        first.reverse()
        first.append("another_codec")
        assert decoder._MultiByteStrDecoder__get_codec_candidate_list(b"plain") == expected
        assert other._MultiByteStrDecoder__get_codec_candidate_list(b"other") == (
            ([detected] if detected else []) + [name for name in defaults if name != detected]
        )
        assert MultiByteStrDecoder._MultiByteStrDecoder__CODECS == defaults
        assert candidates == ["utf_8", "utf_8", "unknown_codec", ""]

    def test_unknown_candidate_error(self):
        with pytest.raises(LookupError, match="unknown encoding"):
            MultiByteStrDecoder(b"plain", ["unknown_codec"])

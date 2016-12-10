# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals
import sys


class MultiByteStrDecoder(object):
    __CODEC_LIST = (
        'utf_7',
        'utf_8', 'utf_8_sig',
        'utf_16', 'utf_16_be', 'utf_16_le',
        'utf_32', 'utf_32_be', 'utf_32_le',

        'big5', 'big5hkscs',
        'cp037', 'cp424', 'cp437', 'cp500', 'cp720',
        'cp737', 'cp775', 'cp850', 'cp852', 'cp855',
        'cp856', 'cp857', 'cp858', 'cp860', 'cp861',
        'cp862', 'cp863', 'cp864', 'cp865', 'cp866',
        'cp869', 'cp874', 'cp875', 'cp932', 'cp949',
        'cp950', 'cp1006', 'cp1026', 'cp1140', 'cp1250',
        'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255',
        'cp1256', 'cp1257', 'cp1258',
        'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr',
        'gb2312', 'gbk', 'gb18030',
        'hz',
        'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
        'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr',
        'latin_1',
        'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6',
        'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 'iso8859_11',
        'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16',
        'johab',
        'koi8_r', 'koi8_u',
        'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish',
        'ptcp154',
        'shift_jis', 'shift_jis_2004', 'shift_jisx0213',
    )

    @property
    def unicode_str(self):
        return self.__unicode_str

    @property
    def codec(self):
        return self.__codec

    def __init__(self, value):
        self.__encoded_str = value
        self.__codec = None

        self.__unicode_str = self.__to_unicode()

    def __to_unicode(self):
        if sys.version_info.major <= 2:
            is_buffer = isinstance(self.__encoded_str, buffer)
        else:
            is_buffer = isinstance(self.__encoded_str, memoryview)

        if is_buffer:
            value = str(self.__encoded_str)
        else:
            value = self.__encoded_str

        for codec in self.__CODEC_LIST:
            try:
                self.__codec = codec
                return value.decode(codec)
            except UnicodeDecodeError:
                continue
            except UnicodeEncodeError:
                # already a unicode string
                return value
            except AttributeError:
                try:
                    return "{}".format(value)
                except UnicodeDecodeError:
                    # some of the objects that cannot convertible to a string
                    # may reach this line
                    raise TypeError("argument must be a string")

        self.__codec = None

        try:
            message = "unknown codec: value={}".format(value)
        except UnicodeDecodeError:
            message = "unknown codec: value-type={}".format(type(value))

        raise UnicodeDecodeError(message)

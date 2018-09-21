# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <>
"""

from __future__ import absolute_import, unicode_literals

import os
import stat

from chardet.universaldetector import UniversalDetector


def is_fifo(file_path):
    return stat.S_ISFIFO(os.stat(file_path).st_mode)


def to_codec_name(name):
    if not name:
        return None

    return name.lower().replace("-", "_")


def detect_file_encoding(file_path):
    if not os.path.isfile(file_path) or is_fifo(file_path):
        return None

    detector = UniversalDetector()
    READ_SIZE = 4 * 1024

    try:
        with open(file_path, mode="rb") as f:
            while True:
                binary = f.read(READ_SIZE)
                if not binary:
                    break

                detector.feed(binary)
                if detector.done:
                    break
    except IOError:
        return None
    finally:
        detector.close()

    return to_codec_name(detector.result.get("encoding"))

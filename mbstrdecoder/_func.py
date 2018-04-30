# encoding: utf-8

'''
.. codeauthor:: Tsuyoshi Hombashi <>
'''

from __future__ import absolute_import, unicode_literals

from chardet.universaldetector import UniversalDetector


def to_codec_name(name):
    if not name:
        return None

    return name.lower().replace("-", "_")


def detect_file_encoding(file_path):
    detector = UniversalDetector()
    READ_SIZE = 4 * 1024

    try:
        with open(file_path, mode='rb') as f:
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

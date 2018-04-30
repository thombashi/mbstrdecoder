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

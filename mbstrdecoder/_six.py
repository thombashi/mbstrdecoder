"""
Code from six:
    https://github.com/benjaminp/six/blob/master/LICENSE
"""

from __future__ import absolute_import

import sys


PY3 = sys.version_info[0] == 3


if PY3:
    string_types = (str,)
    text_type = str
    binary_type = bytes
else:
    string_types = (basestring,)
    text_type = unicode
    binary_type = str


if PY3:

    def b(s):
        return s.encode("latin-1")


else:

    def b(s):
        return s

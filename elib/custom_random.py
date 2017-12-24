# coding=utf-8
"""
Utilities to obtain random values
"""

import random
import os
import string


def random_string(size=6, chars=string.ascii_uppercase + string.digits) -> str:
    """
    Creates a random string

    :param size: len of str
    :param chars: character pool
    :return: random string
    """
    return ''.join(random.choice(chars) for _ in range(size))


def random_bytes(length=1024):
    return os.urandom(length)

"""
The NimbeLink modem package

(C) NimbeLink Corp. 2021

All rights reserved except as explicitly granted in the license agreement
between NimbeLink Corp. and the designated licensee. No other use or disclosure
of this software is permitted. Portions of this software may be subject to third
party license terms as specified in this software, and such portions are
excluded from the preceding copyright notice of NimbeLink Corp.
"""

from .exception import Error
from .exception import AtError

from . import skywire
from . import nano
from . import src7611
from . import tg1wwg

__all__ = [
    "Error",
    "AtError",

    "skywire",
    "nano",
    "src7611",
    "tg1wwg",
]

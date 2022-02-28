"""
All the things I commonly use to help solve LeetCode problems
"""


import bisect
import collections
import copy
import functools
import heapq
import itertools
import os
from pprint import pprint as pp
import re
import random
import string
import time
import typing
from typing import *

try:
    import sortedcontainers
except ImportError:
    print('failed to import sortedcontainers')
    print('consider installing with pip')
    print('or switching virtual environments')


from . import constructors
from . import objects
from . import my_decorators
from .aliases import *
from .constructors import *
from .objects import *
from .my_decorators import *
"""
All the things I commonly use to help solve LeetCode problems
"""


import array
import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import os
from pprint import pprint as pp
import queue
import re
import random
import string
import time
import typing
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    Generator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
    defaultdict,
)

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

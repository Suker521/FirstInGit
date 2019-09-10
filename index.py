# -*- encoding: utf-8 -*-

import ctypes
from ctypes import *

def run(first, second):
    lib = ctypes.CDLL("./lib/lib.so")
    f = lib.multiply
    f.argtypes = [c_int, c_int]
    f.restype = c_int
    return f(first, second)


if __name__ == "__main__":
    result = run(12, 3)
    print(result)


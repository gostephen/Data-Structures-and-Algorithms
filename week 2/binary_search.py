# Binary search function for an ordered list
import math


def binary_search(a, lo, hi, val):

    if lo >= hi:
        return -1

    # calculate middle index while avoiding int overflow
    mid = lo + math.floor((hi - lo)/2)
    # print(mid)

    if val == a[mid]:
        return mid

    if val > a[mid]:
        lo = mid
        return binary_search(a, lo, hi, val)
    else:
        hi = mid
        return binary_search(a, lo, hi, val)


test = [2, 4, 6, 8, 10]
print(binary_search(test, 0, 5, 2))
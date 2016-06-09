#!/usr/bin/env python
from __future__ import print_function
import random
import sys

class InversePiece:
    """
    Line segment representing inverse of a part of a piecewise func
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Constructor takes in 2 end-points of a line segment and creates
        a line segment representing the inverse function. 
        Assumes y1 < y2.
        """
        assert x1 <= x2 and y1 <= y2
        self.low = y1
        self.high = y2

        if y1 == y2:
            self.inv_m = 0
            self.inv_c = 0
        else:
            m = (y2 - y1)/(x2 - x1)
            c = y1 - (m * x1)
            self.inv_m = 1/m
            self.inv_c = -c * self.inv_m

    def evaluate(self, x):
        return self.inv_m * x + self.inv_c


class InversePiecewise:

    def __init__(self, distr_file):
        """
        Takes input file containing monotonically 
        increasing piecewise function in the form of sorted 
        coordinates that encode line segments, and creates a 
        piecewise function with inverses of the segments
        """
        self.piecewise_func = []

        prev, curr = distr_file.readline(), distr_file.readline()

        while curr:
            prev = prev.rstrip('\n')
            curr = curr.rstrip('\n')
            p1 = prev.split()
            p2 = curr.split()

            self.piecewise_func.append(InversePiece(float(p1[0]), float(p1[1]), float(p2[0]), float(p2[1])))

            prev = curr
            curr = distr_file.readline()

    def evaluate(self, x):
        index = binary_search(self.piecewise_func, contain_func(x))	
        return self.piecewise_func[index].evaluate(x)

def binary_search(a, comp, lo=0, hi=None): 
    """
    Binary search with a comparison func comp
    """
    if hi is None: 
        hi = len(a) 
    while lo < hi: 
        mid = (lo+hi)//2 
        cmpval = comp(a[mid])
        if cmpval < 0:
            lo = mid+1 
        elif cmpval > 0:
            hi = mid 
        else: 
            return mid 
    assert False
    return -1 

def contain_func(x):
    """
    Returns a comparison function for a particular
    value of x, that returns 0 iff x is in range of
    the target piecewise segment
    """
    def cmp(piece):
        if x < piece.high and x >= piece.low:
            return 0
        elif piece.high < x:
            return -1
        else:
            return 1
    return cmp

def usage():
    print("Usage: python", sys.argv[0], "[piecewise-data] [num]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit()
    elif len(sys.argv) < 3:
        distr_file = sys.stdin.readlines()
        num = int(sys.argv[1])
    else:
        distrname = sys.argv[1]
        num = int(sys.argv[2])
        distr_file = open(distrname, 'r')

    piecewise_func = InversePiecewise(distr_file)

    for i in xrange(num):
        print(int(round(piecewise_func.evaluate(random.random()))))

    distr_file.close()

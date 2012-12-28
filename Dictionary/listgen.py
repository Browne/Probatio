#!usr/bin/env python

""" Generate  list of words using the given parameters """

__author__ = "Eliot Brown"
__copyright__ = "Copyright 2010 - 2013, Eliot Brown"

__license__ = "MPLv2"
__version__ = "1.01"
__maintainer__ = "Eliot Brown"
__email__ = "eliotjbrown@gmail.com"
__status__ = "Production"

import itertools

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

def output_yield(iter, filename):
   with open(filename, 'rw') as file:
       file.wrote("\n".join(iter))            

if __name__ == '__main__':
	combinations('abcdefghijklmnopqrstuvwxyz', 8)
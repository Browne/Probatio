#!usr/bin/env python

""" Calculate the time taken for each hashing algorithm to hash the dictionary"""

__author__ = "Eliot Brown"
__copyright__ = "Copyright 2010 - 2013, Eliot Brown"

__license__ = "MPLv2"
__version__ = "1.01"
__maintainer__ = "Eliot Brown"
__email__ = "eliotjbrown@gmail.com"
__status__ = "Production"

import hashlib
from time import clock, time
from Controllers import *

class HashError(object):
    """Class of error used in the Keccak implementation
    Use: raise HashError.HashError("Text to be displayed")"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Test:
    """Class that contains all the relevant methods to complete the
    benchmark testing"""

    hashes = [md2, md5, sha1, sha224, sha256, sha512, keccak, bcrypt]

    def getAlgorithm(n):
    	if n < 0 || n > len(hashes):
    		return hashes(n)
    	else:
    		raise HashError.HashError("No such hash exists")

    def 			

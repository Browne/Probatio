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
import Controllers.md2_hash
import Controllers.Keccak_hash

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

    # hashes = [md2, md5, sha1, sha224, sha256, sha512, keccak, bcrypt]

    # def getAlgorithm(n):
    # 	if n < 0 or n > len(hashes):
    # 		return hashes(n)
    # 	else:
    # 		raise HashError.HashError("No such hash exists")

    def setup():
    	with open('results/all', r) as a: 
	    	a.write("*********************************************")
	    	a.write("|  Hash  |  Time to complete all |  Average |")
	    	a.write("*********************************************")	
    	
    def md2():
    	start = time.clock()
    	with open('/usr/share/dict/words', 'r') as f:
    		with open('results/md2', 'r') as w:
        		for word in [line[:-1] for line in f.readlines()]:
        			w.write(word + ", " + md2(word))
        		f.close
        		elapsed = (time.clock() - start)
        		average = (elapsed / 285886)
        	w.close	
        a.write("|  md2   | elapsed | average |")

    def md5():    
        start = time.clock()	
		with open('/usr/share/dict/words', 'r') as f:
    		with open('results/md5', 'r') as w:
        		for word in [line[:-1] for line in f.readlines()]:
        			w.write(word + ", " + hashlib.md5(word).hexdigest())
        		f.close
        		elapsed = (time.clock() - start)
        		average = (elapsed / 285886)
        	w.close	
        a.write("|  md5   | elapsed | average |")

    def sha1():    
        with open('/usr/share/dict/words', 'r') as f:
    		with open('results/sha1', 'r') as w:
        		for word in [line[:-1] for line in f.readlines()]:
        			w.write(word + ", " + hashlib.sha1(word).hexdigest())
        		f.closer
        		elapsed = (time.clock() - start)
        		average = (elapsed / 285886)
        	w.close	
        a.write("|  md5   | elapsed | average |")	

     def sha224():  
        with open('/usr/share/dict/words', 'r') as f:
    		with open('results/sha224', 'r') as w:
        		for word in [line[:-1] for line in f.readlines()]:
        			w.write(word + ", " + hashlib.sha1(word).hexdigest())
        		f.closer
        		elapsed = (time.clock() - start)
        		average = (elapsed / 285886)
        	w.close	
        a.write("|  md5   | elapsed | average |")	 			

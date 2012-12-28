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
# import Controllers.Keccak_hash

def setup():
	# with open('results/main', 'r+') as a:
	a.write("*********************************************\n")
	a.write("|  Hash  |  Time to complete all |  Average |\n")
	a.write("*********************************************\n")	
	
def md2():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/md2', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + md2(word))
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	a.write("|  md2   | elapsed | average |")

def md5():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/md5', 'r') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + hashlib.md5(word).hexdigest())
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	with open('results/main', 'r') as a:	
    		a.write("|  md5   | elapsed | average |")

def sha1():
	start = time()    
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha1', 'r') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + hashlib.sha1(word).hexdigest())
    		f.closer
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	with open('results/main', 'r') as a:	
    		a.write("|  sha1   | elapsed | average |")	

def sha224():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha224', 'r') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + hashlib.sha224(word).hexdigest())
    		f.closer
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	with open('results/main', 'r') as a:
    		a.write("|  sha224   | elapsed | average |")

def sha256():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha224', 'r') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + hashlib.sha256(word).hexdigest())
    		f.closer
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	with open('results/main', 'r') as a:	
    		a.write("|  sha256   | elapsed | average |")

def sha512():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha224', 'r') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(word + ", " + hashlib.sha512(word).hexdigest())
    		f.closer
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	with open('results/main', 'r') as a:	
    		a.write("|  sha256   | elapsed | average |")   

    # def __init__(self):
    # 	x = Test()
    # 	with open('results/main', 'r') as a:
    # 		setup()

if __name__ == '__main__':
	with open('results/main', 'r+') as a:
		setup()
		md2()
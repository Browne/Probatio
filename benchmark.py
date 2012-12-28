#!usr/bin/env python

""" Calculate the time taken for each hashing algorithm to hash the dictionary, plus creates a rainbow table"""

__author__ = "Eliot Brown"
__copyright__ = "Copyright 2010 - 2013, Eliot Brown"

__license__ = "MPLv2"
__version__ = "1.01"
__maintainer__ = "Eliot Brown"
__email__ = "eliotjbrown@gmail.com"
__status__ = "Production"

import hashlib
from time import clock, time
from Controllers import md2_hash
# import Controllers.Keccak_hash

def setup():
	a.write("*********************************************\n")
	a.write("|  Hash  |  Time to complete all |  Average |\n")
	a.write("*********************************************\n")	
	
def md2():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/md2', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(md2_hash.md2(word) + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    		if elapsed == 0:
    			skip
    		else:
    			a.write("|  md2   | " + str(elapsed) + "| " + str(average) + "|\n")

def md5():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/md5', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(hashlib.md5(word).hexdigest() + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)	
    	a.write("|  md5   | " + str(elapsed) + " | " + str(average) + " |\n")

def sha1():
	start = time()    
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha1', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(hashlib.sha1(word).hexdigest() + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	a.write("|  sha1   | " + str(elapsed) + " | " + str(average) + " |\n")	

def sha224():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha224', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(hashlib.sha224(word).hexdigest() + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)
    	a.write("|  sha224  | " + str(elapsed) + " | " + str(average) + " |\n")

def sha256():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha256', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(hashlib.sha256(word).hexdigest() + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)	
    	a.write("|  sha256   | " + str(elapsed) + " | " + str(average) + " |\n")

def sha512():
	start = time()
	with open('/usr/share/dict/words', 'r') as f:
		with open('results/sha512', 'r+') as w:
			for word in [line[:-1] for line in f.readlines()]:
				w.write(hashlib.sha512(word).hexdigest() + "\n")
    		f.close
    		elapsed = (time() - start)
    		average = (elapsed / 285886)	
    	a.write("|  sha512   | " + str(elapsed) + " | " + str(average) + " |\n")  

if __name__ == '__main__':
	with open('times', 'r+') as a:
		setup()
		md2()
		md5()
		sha1()
		sha224()
		sha256()
		sha512()
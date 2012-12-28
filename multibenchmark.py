#!usr/bin/env python

""" Calculate the time taken for each hashing algorithm to hash the dictionary - runs the test several times before giving averages """

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

def md2():
	total = 0
	with open('times/md2', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("                          md2                        \n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					md2_hash.md2(word)
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
		f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))		

def md5():
	total = 0
	with open('times/md5', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("|                         md5                       |\n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					hashlib.md5(word).hexdigest()
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
			f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))


def sha1():
	total = 0
	with open('times/sha1', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("|                        sha1                       |\n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					hashlib.sha1(word).hexdigest()
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
			f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))

def sha224():
	total = 0
	with open('times/sha224', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("|                       sha224                      |\n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					hashlib.sha224(word).hexdigest()
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
			f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))

def sha256():
	total = 0
	with open('times/sha256', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("|                       sha256                      |\n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					hashlib.sha256(word).hexdigest()
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
			f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))

def sha512():
	total = 0
	with open('times/sha512', 'r+') as a:
		a.write("*****************************************************\n")
		a.write("|                       sha512                      |\n")
		a.write("|  Pass  | Time to complete all |      Average      |\n")
		a.write("*****************************************************\n")
		with open('/usr/share/dict/words', 'r') as f:
			for x in range (10):
				start = time()
				for word in [line[:-1] for line in f.readlines()]:
					hashlib.sha512(word).hexdigest()
				elapsed = (time() - start)
				average = (elapsed / 285886)
				total = total + elapsed
				a.write(str(x) + " | " + str(elapsed) + "| " + str(average) + "|\n")
			f.close	
		a.write("Total time: " + str(total))
		a.write("Average time: " + str(total/(2858860)))

if __name__ == '__main__':
	sha1()
	sha224()
	sha256()
	sha512()
	md5()

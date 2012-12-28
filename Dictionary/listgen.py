#!usr/bin/env python

""" Generate  list of words using the given parameters """

__author__ = "Eliot Brown"
__copyright__ = "Copyright 2010 - 2013, Eliot Brown"

__license__ = "MPLv2"
__version__ = "1.01"
__maintainer__ = "Eliot Brown"
__email__ = "eliotjbrown@gmail.com"
__status__ = "Production"

f=open('largedictionary', 'w')

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

numb = range(48,58)
cap = range(65,91)
low = range(97,123)
choice = 0
while int(choice) not in range(1,8):
    choice = raw_input('''
    1) Numbers
    2) Capital Letters
    3) Lowercase Letters
    4) Numbers + Capital Letters
    5) Numbers + Lowercase Letters
    6) Numbers + Capital Letters + Lowercase Letters
    7) Capital Letters + Lowercase Letters
    : ''') 

choice = int(choice)
poss = []
if choice == 1:
    poss += numb
elif choice == 2:
    poss += cap
elif choice == 3:
    poss += low
elif choice == 4:
    poss += numb
    poss += cap
elif choice == 5:
    poss += numb
    poss += low
elif choice == 6:
    poss += numb
    poss += cap
    poss += low
elif choice == 7:
    poss += cap
    poss += low

bigList = []
for i in poss:
    bigList.append(str(chr(i)))

MIN = raw_input("What is the min size of the word? ")
MIN = int(MIN)
MAX = raw_input("What is the max size of the word? ")
MAX = int(MAX)
for i in range(MIN,MAX+1):
	for s in xselections(bigList,i): f.write(''.join(s) + '\n')
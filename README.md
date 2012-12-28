Probatio
========

A set of benchmark tests against different hashing algorithms, using Python implementations.
These include:

1. md2
+ md5
+ sha1
+ sha224
+ sha256
+ sha512
+ keccak
+ bcrypt

Timing Method
-------------

Timing will all be done using clock() in Python, starting the 'clock' at the beginning and stopping at the end. I'll be hashing the standard dictionary on a Unix system which is 285886 words.

### Generic specifications of the testing computer
* 2.5GHz
* 8GB of RAM

Licensing
---------
This project is licensed under the Mozilla Public License version two (MPLv2). The md2, keccak and bcrypt algorithms are all subject to the individual licenses of the producers.

A copy of the license is distributed with this project, it is also available online [here](http://www.mozilla.org/MPL/2.0/).

Parts
-----
###benchmark.py
This is the test bed designed to run each test once - as it does the test it puts the hash into a newfile to create a rainbow table for the dictionary.

###multibenchmark.py
This is the test bed designed to run each test multiple times, unlike benchmark it doesn't create a rainbow table

###Times
This folder contains all the time results. Individually named files are the results for multibenchmark.py. Main is the results from benchmark.py.

###Dictionary
This folder contains the standard dictionary and a password permutation calculator. On the localhost it also contains subsequent testing dictionaries, but given their size they are not hosted on github.

###License
This contains a copy of the license for this project

Authors
-------
This project is produced by:

* Eliot Brown - <support@eliotbrown.co.uk>

Known Bugs
----------
###multibench.py
The script allows data to be cached meaning subsequent results after the first pass are quicker than they should be. A solution is under investigation

Troubleshooting
---------------
Please contact the author.

Credits and Acknowledgements
----------------------------
Currently there are no acknowledgements

Changelog
---------
Currently there are no changes

#!/usr/bin/python
#A program to send files remotely between two computers
#Created on Saturday, March 30, 2013

import socket
import sys
import os
import pprint
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

if sys.argv[1] == "-l":
  while True:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(('', 6012))	#Runs on port 6012 (completely random)
		s.listen(5)
		c, con_addr = s.accept()
		
		r = c.recv(33554432)	#Receive up to 2^25 bytes of file + pathname
		pprint.pprint(r)
		r_split = re.split("\(\*\)", r)	#Split pathname and actual file contents
		
		pprint.pprint(r_split[0]);
		
		f = open(r_split[0], 'w')
		f.write(r_split[1])
		f.close()
		
		c.close()
		s.close()
		sys.exit(0)
else:
	f = open(sys.argv[2], 'r')
	fs = f.read()

	s.connect((socket.gethostbyname(sys.argv[1]), 6012))
	s.send(sys.argv[3] + "(*)" + fs)
	print sys.argv[3]
	s.close()
	sys.exit(0)

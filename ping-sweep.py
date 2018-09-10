#! /usr/bin/python3
#used Python CookBook 3rd Ed. section 13.6 for reference

import subprocess

for n in range(1,255):
	try:
		ping=subprocess.check_output (["ping","-c 1","-W 1","10.11.1."+str(n)])
	except subprocess.CalledProcessError as e:
		ping=e.output
		code=e.returncode
	pingtext=ping.decode('utf-8')
	if pingtext.find('bytes from') !=-1:
		print("10.11.1."+str(n),"is alive!")


#!/usr/bin/env python3

""" 
This code based on a great description of the basics of infrared from
Brian Schwind https://blog.bschwind.com/ and the pyA20 GPIO Library

Detlev Aschhoff === www.midias.de/projekte === info@vmais.de

"""

import time
import sys
from pyA20.gpio import gpio
from pyA20.gpio import port


def irBin(port):
	pin = int(port)	#PA0 =0 PA1 =1 PA2 =2 ......
	gpio.init()
	gpio.setcfg(pin, gpio.INPUT)
	value = 1
	binString=""	# binäryString
	command = []	# List of pulse
	num1 = 0		# 
	state = 0		 # for change 1 0
	rec = 0
	
	# waiting of first 0 key pressed    Input rec = 1 => Gap    0 => Puls

		
	startTime = int(time.time()*1000000)
	while True:

		if value != state:			# Value has change, calculate pulselenght
		
			now = int(time.time()*1000000)
			pulse = now - startTime
			startTime = now
			
			if pulse > 8000 and state == 0:	# Start
				rec =1
			if rec == 1 and state == 1:
				command.append(pulse)		# add pulse
				if pulse > 8000:			#Stop
					break
					
		state = value
		value = gpio.input(pin)
		
	if len(command)>30:
		command.pop(0)	# Startcode  delete

		binString = "".join(map(lambda x: "1" if x > 1000 else "0", command))
	return binString
	
if __name__=="__main__":
	port=str(sys.argv[1])
	print("\033[2J")			#Clear screen
	print("\033[H")	
	print("\033[0;30m;\033[42m        Waiting for IR signal       \033[0m")

	while -1:
		binString = irBin(port)
		if binString != "":
			print("\033[2J")	#Clear screen
			print("\033[H")
			col0="\033[0;97m"
			col1="\033[0;93m"
			col2="\033[0;94m"
			print("\033[2J")
			print("\033[0;30m\033[42m  Received:                                       \033[0m\n")
			print(col0+"  Binary:",binString,"\n")			
			print(col1+"  ID 1   ",binString[0:8],"  NEC Protocol valid if:  ")
			print(col1+"  ID 2   ",binString[8:16],"  invert from ID 1")
			print(col2+"  Code 1 ",binString[16:24])
			print(col2+"  Code 2 ",binString[24:32],"  invert from Code 1")
			print("\033[4;94m                                                 \n")
			print("\033[0m  stop ==> Strg C")
			print("\033[0m")
	
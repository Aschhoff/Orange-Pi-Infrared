#!/usr/bin/env python3
""" 
This code based on a great description of the basics of infrared from
Brian Schwind https://blog.bschwind.com/ and the  pyA20 GPIO Library

Detlev Aschhoff === www.midias.de/projekte === info@vmais.de
"""
import json
import time
import sys
from pyA20.gpio import gpio
from pyA20.gpio import port


# call the module with output port PA0 =0 PA1 =1    and the code as binäry String "11110000.....
def irfile(port, code):
	delay = 5						# Value from OPiSpeed to generate 38Khz impuls
	i=0
	y=0
	port=int(port)
	gpio.init()
	gpio.setcfg(port, gpio.OUTPUT)
	delay = delay * 0.000001
	code=code+"111111111" 			# extend the code with a short gap
	
	
	while i<360:					# Start 360 * 26 microsec = 9000 Pulse
		gpio.output(port, 1)		# 26 microsec Pulse on
		a=time.time()+delay
		while time.time() < a:
			pass
		gpio.output(port, 0)		# Pulse off
		a=time.time()+delay
		while time.time() < a:
			pass		
		i+=1
	a=time.time()+0.004500			# 4500 microsec Pause
	while time.time() < a:
		pass		
	i=0

	while y < 33:					# Output 4 * 8bit code

		while i<20:					#Fix 520 microsec  ==> 20 * 26 microsec
			gpio.output(port, 1)
			a=time.time()+delay
			while time.time() < a:	#26 microsec pulse ==> 38KHz
				pass
			gpio.output(port, 0)
			a=time.time()+delay
			while time.time() < a:
				pass		
			i+=1
			
		shift=0.000500+0.001000*int(code[y])	# 1 0 from code
		a=time.time()+shift			# Gap 0.000500sec is 0    0.0001500sec is 1
		while time.time() < a:
			pass
		
		i=0	
		y+=1	

		
 
if __name__=="__main__":
# Call the module with filename of the remote-control  and the name of the key  and the output port

	nameFB=str(sys.argv[1])		
	nameKey=str(sys.argv[2])
	port=str(sys.argv[3])
	print(nameKey)
	if nameFB == "raw":
		code = nameKey
	else:
		file = open(nameFB, 'r')	# File open /root/... or /home/opi
		txt=file.readline()
		Keys = json.loads(txt)		# json format to Dic
		file.close()
		code=(Keys[nameKey])

	for i in range(2):				#  2 Repeats
		irfile(port,code)
		time.sleep(0.5)
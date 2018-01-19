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
	i=0
	y=0
	tp=0.000005
	led=int(port)
	gpio.init()
	gpio.setcfg(led, gpio.OUTPUT)
	
	code=code+"111111111" 			# code extention short gap
	
	# Startsequenz					  360 * 26 microsec = 9000 Pulse
	while i<360:
		gpio.output(led, 1)			# 26 microsec Pulse ein
		a=time.time()+tp
		while time.time() < a:
			pass
		gpio.output(led, 0)			# Pulse aus
		a=time.time()+tp
		while time.time() < a:
			pass		
		i+=1
	a=time.time()+0.004500			# 4500 microsec Pause
	while time.time() < a:
		pass		
	i=0

	while y < 33:

		while i<20:					#Fix 520 microsec  = 20 * 26 microsec
			gpio.output(led, 1)
			a=time.time()+tp
			while time.time() < a:	#26 microsec pulse 38KHz
				pass
			gpio.output(led, 0)
			a=time.time()+tp
			while time.time() < a:
				pass		
			i+=1
			
		shift=0.000500+0.001000*int(code[y])	# 1 0 from File
		a=time.time()+shift			# gap  0.000500sec ist 0  0.0001500sec ist 1
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
		file = open(nameFB, 'r')	#File öffnen /root/...
		txt=file.readline()
		Keys = json.loads(txt)		# von json Format zurueck in Dic
		file.close()
		code=(Keys[nameKey])

	for i in range(2):
	irfile(port,code)
		time.sleep(0.5)
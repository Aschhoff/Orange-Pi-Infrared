#!/usr/bin/env python3
""" for Pi1 and Pi2 delete marked Lines
they need full Speed
"""

import time
from pyA20.gpio import gpio
from pyA20.gpio import port

i=0
y=0
port=13
port=int(port)
gpio.init()
gpio.setcfg(port, gpio.OUTPUT)

tp=0.000013			# begin with 13 microsec
pulse = 100000
p=0
best="\033[0;31msorry to slow!!!!"

for i in range(12):

	ta= time.time()
	while i<100:
		gpio.output(port, 1)
		a=time.time()+tp		
		while time.time() < a:	
			pass				
		gpio.output(port, 0)
		a=time.time()+tp		
		while time.time() < a:	
			pass					
		i+=1
	te= time.time()
	
	pulse= (te-ta)*10000
	print("Pulselenght:",int(pulse),"microsec   Delay= ",int(tp*1000000))
	if pulse < 27 and p==0:
		best=int(tp*1000000)
		p=1
	tp -= 0.000001

		
print("\033[0;32mBest Value for tp = ",best,"microsec")
print("\033[0m") 
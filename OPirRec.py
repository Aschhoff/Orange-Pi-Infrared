#!/usr/bin/env python3
"""
Detlev Aschhoff === www.midias.de/projekte === info@vmais.de

"""
import json
import time
import OPirRx

port="3"		#!!! here the Pin where Opi received the signal   PA0 = 0 PA1 = 1 ........
ende=0
binString1=""
binString2=""
FB={}
nameKey=""
noNEC=0
col0="\033[0;93m"
col1="\033[0;92m"
col2="\033[0;91m"
try:
	print("\033[2J")			#Clear screen
	print("\033[H")
	nameFB=input("Name of remote control: ")
	while 1:
		while ende==0:
			print("\033[2J")			#Clear screen
			print("\033[H")
			print(col1+"Name of remote- control: ",nameFB)
			print("used keys: ",end="")
			for key, value in FB.items() :
				print (key, end=" ")
			print("")
			print(col0+"\npress a key on remote- control ---- or Strg C to save file\n")
			while len(binString1) < 30:
				binString1 = OPirRx.irBin(port)
				
			#print("Binär",binString1[:32])
						
			id= binString1[0:8]
			idinv= binString1[8:16]
			code= binString1[16:24]
			codeinv= binString1[24:32]
			
			for x in range(8):			# check if its a valid NEC protocoll
				if id[x] == idinv[x] or code[x] == codeinv[x]:
					noNEC=1
				else:
					ende=1
				
			if noNEC==1:
				print(col0+"== no NEC protokoll == ")
								
				time.sleep(0.5)

				print(col0+"to validate: press same key again\n")
				while len(binString2) < 30:
					binString2 = OPirRx.irBin(port)

				if binString2[:32] == binString1[:32]:
					print(col1+"Key valid")
					noNEC=0
					ende=1
				else:
					print("---------------------------------------\n")
					print(col2+"Key not valid!  please again\n")
					binString1=""
					binString2=""
					noNEC=0
					time.sleep(2)
			
		nameKey=input("Code valid! Name of this key: ")
		keyn={nameKey:binString1}
		FB.update(keyn)
		ende=0
		binString1=""
		binString2=""
		print("\033[0m")
except KeyboardInterrupt:
	file = open(nameFB, 'w')	#File speichern /root/
	file.write(json.dumps(FB))	# in json Format
	file.close()
	print("   File saved!",nameFB)
	print("\033[0m")
	
	
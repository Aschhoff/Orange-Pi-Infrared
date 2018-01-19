# Orange-Pi-Infrared


With this Python3 Programs your can record, save and transmit infrared signal from a remote-control.

Development environment:

Orange Pi -testet on Orange Pi zero H2
Armbian stable
GPIO Library pyA20 - is faster then other

IR receiver
IR transmitter - break-out board or DIY

Notiz for using the GPIO:

it is used the pyA20 numbering. ==> PA01 =0 PA04 =4
Attention: most of the GPIO are used by the kernel for UARTs I2C SPI.
in my case i disabled the UART2 to get free the PA01 PA00 and PA03 pins

Usage:
All programs need root or sudo because of the pyA20 library!

Depending of the Board we have to generate the 38Khz pulse. Therefor we use at first the testprogram
OPiSpeed.py to get the right delay time.
This value put in program OPirTx.py line 17 eg. delay = 5 
Ok the transmiter is calibrated.

Learn from your Remote-Control:

In line 10 of the Program enter your receive GPIO in my case 3 thats PA03
start sudo python3 /home/pi/OPirRec.py
It will learn the commands from a remote-control and save it on a file.

Transmit whis Orange Pi:

start sudo python3 /home/pi/OPirTX.py File command GPIO
start sudo python3 /home/pi/OPirTX.py myRemote Power 0

it will sent the command Power from the file myRemote to your Device

viel Spass
Detlev Aschhoff

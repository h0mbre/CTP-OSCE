import os
import sys
import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-x", "--hex", help="enter offset in hexidecimal, example: 3b",
                    action="store_true")
parser.add_argument("-d", "--decimal", help="enter offset in decimal, example: 124",
                    action="store_true")
parser.add_argument("-j", "--jump", help="get jump short opcodes for decimal offset, example: 124",
                    action="store_true")
args = parser.parse_args()

positiveSeed = [0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,0x3c,0x3d,0x3e,0x3f,0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4a,0x4b,0x4c,0x4d,0x4e,0x4f,0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5a,0x5b,0x5c,0x5d,0x5e,0x5f,0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,0x6c,0x6d,0x6e,0x6f,0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7a,0x7b,0x7c,0x7d,0x7e,0x7f]

negativeSeed = [0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87,0x88,0x89,0x8a,0x8b,0x8c,0x8d,0x8e,0x8f,0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0x99,0x9a,0x9b,0x9c,0x9d,0x9e,0x9f,0xa0,0xa1,0xa2,0xa3,0xa4,0xa5,0xa6,0xa7,0xa8,0xa9,0xaa,0xab,0xac,0xad,0xae,0xaf,0xb0,0xb1,0xb2,0xb3,0xb4,0xb5,0xb6,0xb7,0xb8,0xb9,0xba,0xbb,0xbc,0xbd,0xbe,0xbf,0xc0,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,0xd5,0xd6,0xd7,0xd8,0xd9,0xda,0xdb,0xdc,0xdd,0xde,0xdf,0xe0,0xe1,0xe2,0xe3,0xe4,0xe5,0xe6,0xe7,0xe8,0xe9,0xea,0xeb,0xec,0xed,0xee,0xef,0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8,0xf9,0xfa,0xfb,0xfc,0xfd]

offsetNegative = [126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def default():
	global positiveSeed
	global negativeSeed
	global offsetNegative
	add1 = raw_input("Enter Address #1: ")
	add2 = raw_input("Enter Address #2: ")

	add1 = int(add1, 16)
	add2 = int(add2, 16)
	if add1 > add2:
		offset = add1 - add2
		if offset in range(1,16):
			print "[+] Hex offset: " + str(hex(offset)).replace("0x", "0x0")
		else:
			print "[+] Hex offset: " + str(hex(offset))
		print "[+] Decimal offset: " + str(offset)
		if offset in offsetNegative:
			index = offsetNegative.index(offset)
			answer = negativeSeed[index]
			answer = str(hex(answer))
			answer = answer.replace("0x", "\\x")
			print "[-] Negative jump opcodes: \\xeb" + answer
		if offset in positiveSeed:
			if offset in range(1,16):
				print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x0")
			else:
				print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x")
		
	else:
		offset = add2 - add1
		if offset in range(1,16):
			print "[+] Hex offset: " + str(hex(offset)).replace("0x", "0x0")
		else:
			print "[+] Hex offset: " + str(hex(offset))
		print "[+] Decimal offset: " + str(offset)
		if offset in offsetNegative:
			index = offsetNegative.index(offset)
			answer = negativeSeed[index]
			answer = str(hex(answer))
			answer = answer.replace("0x", "\\x")
			print "[-] Negative jump opcodes: \\xeb" + answer
		if offset in positiveSeed:
			if offset in range(1,16):
				print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x0")
			else:
				print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x")
	x = offset
	if x in range(1,256):
		if x > 127:
			remainder = x % 2
			if remainder == 1:
				x = x/2
				y = x + 1
				if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
				else:
					x = str(hex(x)).replace("0x", "\\x")
				if y in range(1,16):
					y = str(hex(y)).replace("0x", "0x0")
					y = y.replace("0x", "\\x")
				else:
					y = str(hex(y)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + y + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + y + "\\x50\\x5c"
			else:	
				x = x/2			
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + x + "\\x50\\x5c"
		else:
			if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
					print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
					print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"
			else:
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"

def hexOff():
	global positiveSeed
	global negativeSeed
	global offsetNegative
	offset = raw_input("Enter hex offset: ")
	offset = int(offset, 16)
	print "[+] Decimal offset: " + str(offset)
	if offset in offsetNegative:
		index = offsetNegative.index(offset)
		answer = negativeSeed[index]
		answer = str(hex(answer))
		answer = answer.replace("0x", "\\x")
		print "[-] Negative jump opcodes: \\xeb" + answer
	if offset in positiveSeed:
		if offset in range(1,16):
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x0")
		else:
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x")
	x = offset
	if x in range(1,256):
		if x > 127:
			remainder = x % 2
			if remainder == 1:
				x = x/2
				y = x + 1
				if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
				else:
					x = str(hex(x)).replace("0x", "\\x")
				if y in range(1,16):
					y = str(hex(y)).replace("0x", "0x0")
					y = y.replace("0x", "\\x")
				else:
					y = str(hex(y)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + y + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + y + "\\x50\\x5c"
			else:	
				x = x/2			
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + x + "\\x50\\x5c"
		else:
			if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
					print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
					print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"
			else:
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"

def decOff():
	global positiveSeed
	global negativeSeed
	global offsetNegative
	offset = raw_input("Enter decimal offset: ")
	offset = int(offset)
	if offset in range(1,16):
		print "[+] Hex offset: " + str(hex(offset)).replace("0x", "0x0")
	else:
		print "[+] Hex offset: " + str(hex(offset))
	if offset in offsetNegative:
		index = offsetNegative.index(offset)
		answer = negativeSeed[index]
		answer = str(hex(answer))
		answer = answer.replace("0x", "\\x")
		print "[-] Negative jump opcodes: \\xeb" + answer
	if offset in positiveSeed:
		if offset in range(1,16):
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x0")
		else:
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x")
	x = offset
	if x in range(1,256):
		if x > 127:
			remainder = x % 2
			if remainder == 1:
				x = x/2
				y = x + 1
				if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
				else:
					x = str(hex(x)).replace("0x", "\\x")
				if y in range(1,16):
					y = str(hex(y)).replace("0x", "0x0")
					y = y.replace("0x", "\\x")
				else:
					y = str(hex(y)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + y + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + y + "\\x50\\x5c"
			else:	
				x = x/2			
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x04" + x + "\\x50\\x5c"
		else:
			if x in range(1,16):
					x = str(hex(x)).replace("0x", "0x0")
					x = x.replace("0x", "\\x")
					print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
					print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"
			else:
				x = str(hex(x)).replace("0x", "\\x")
				print "[-] ESP Sub Adjust Opcodes: \\x54\\x58\\x2c" + x + "\\x50\\x5c"
				print "[+] ESP Add Adjust Opcodes: \\x54\\x58\\x04" + x + "\\x50\\x5c"
		

def jump():
	global positiveSeed
	global negativeSeed
	global offsetNegative
	offset = raw_input("Enter offset in decimal: ")
	offset = int(offset)
	if offset in offsetNegative:
		index = offsetNegative.index(offset)
		answer = negativeSeed[index]
		answer = str(hex(answer))
		answer = answer.replace("0x", "\\x")
		print "[-] Negative jump opcodes: \\xeb" + answer
	if offset in positiveSeed:
		if offset in range(1,16):
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x0")
		else:
			print "[+] Positive jump opcodes: \\xeb" + str(hex(offset)).replace("0x", "\\x")
	if offset > 128:
		print "[-] Offset is too large for a jump short." 
	
if args.hex:
	hexOff()
elif args.decimal:
	decOff()
elif args.jump:
	jump()
else:
	default()	

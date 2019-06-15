## Offset.py

Just thought I'd show a few use cases for a little helper script I created to automate some things for CTP. DISCLAIMER: Outside of the testing I did during writing the script and this post, the script hasn't been fully vetted. Definitely reach out to me if you find anything wrong with the calcuations and opcodes. 

I couldn't quite get alphanumeric ESP adjustments to work in the script for larger offsets (256-9999) the way I wanted, hopefully I'll be able to add those at some point soon.

## Help!

The help for the script looks like this:
```terminal_session
root@kali:~/ # offset -h                                                                                                                
usage: offset.py [-h] [-x] [-d] [-j]

optional arguments:
  -h, --help     show this help message and exit
  -x, --hex      enter offset in hexidecimal, example: 3b
  -d, --decimal  enter offset in decimal, example: 124
  -j, --jump     get jump short opcodes for decimal offset, example: 124
```
Each option will be explained below. 

## Default Mode

In default mode, we simply feed the script two addresses and if our offset is in the 1-255 decimal range, we should get back the following:
+ hex offset,
+ decimal offset,
+ negative jump short opcodes (if offset in jump short range),
+ positive jump short opcodes (if offset in jump short range),
+ ESP adjustment opcodes using `SUB` for alphanumeric encoded shellcode, and
+ ESP adjustment opcodes using `ADD` for alphanumeric encoded shellcode. 

**FYI:** The `ESP` adjustment opcodes use `EAX` to manipulate the values of `ESP`. 

### Example (Offset 1-255)

In this example we use the addresses `0174FFFF` and `0174FFCC`. 

```terminal_session
Enter Address #1: 0174FFCC
Enter Address #2: 0174FFFF
[+] Hex offset: 0x33
[+] Decimal offset: 51
[-] Negative jump opcodes: \xeb\xcb
[+] Positive jump opcodes: \xeb\x33
[-] ESP Sub Adjust Opcodes: \x54\x58\x2c\x33\x50\x5c
[+] ESP Add Adjust Opcodes: \x54\x58\x04\x33\x50\x5c
```

### Example (Offset 256 - 9999)

If the offset is in the range 256 - 9999, then the script will simply give you the offset in hex and decimal since you cannot do a jump short and the alphanumeric ESP adjustment is slightly out of my python skill range at the moment hehe. 

In this example we use the addresses `0176FFC4` and `0176F74E`.

```terminal_session
Enter Address #1: 0176FFC4
Enter Address #2: 0176F74E
[+] Hex offset: 0x876
[+] Decimal offset: 2166
```

## Hex Offset (`-x`, `--hex`)

In this mode, we simply feed the script an offset in hexidecimal and get back: 
+ decimal offset, 
+ negative jump opcodes (if in jump short range),
+ positive jump opcodes (if in jump short range),
+ ESP adjustment opcodes using `SUB` for alphanumeric encoded shellcode, and
+ ESP adjustment opcodes using `ADD` for alphanumeric encoded shellcode.

### Example (Offset 1- 255)

In this example we use the hexidecimal offset value of `7a`.

```terminal_session
Enter hex offset: 7a
[+] Decimal offset: 122
[-] Negative jump opcodes: \xeb\x84
[+] Positive jump opcodes: \xeb\x7a
[-] ESP Sub Adjust Opcodes: \x54\x58\x2c\x7a\x50\x5c
[+] ESP Add Adjust Opcodes: \x54\x58\x04\x7a\x50\x5c
```

### Example (Offset 256 - 9999)

In this example we use the hexidecimal offset value `fff`. No need for a .gif on this one, just gives back a decimal offset equivalent since it's out of range for a jump short and there is no support for `ESP` adjustments for alphanumeric shellcode that large yet.

```terminal_session
Enter hex offset: fff
[+] Decimal offset: 4095
```

## Decimal Offset (`-d`, `--decimal`)

In this mode, we simply feed the script an offset in decimal and get back: 
+ hexidecimal offset, 
+ negative jump opcodes (if in jump short range),
+ positive jump opcodes (if in jump short range),
+ ESP adjustment opcodes using `SUB` for alphanumeric encoded shellcode, and
+ ESP adjustment opcodes using `ADD` for alphanumeric encoded shellcode.

### Example (Offset 1 - 255)

In this example we use the hexidecimal offset value of `121`.

```terminal_session
Enter decimal offset: 121
[+] Hex offset: 0x79
[-] Negative jump opcodes: \xeb\x85
[+] Positive jump opcodes: \xeb\x79
[-] ESP Sub Adjust Opcodes: \x54\x58\x2c\x79\x50\x5c
[+] ESP Add Adjust Opcodes: \x54\x58\x04\x79\x50\x5c
```

### Example (Offset 256 - 9999)

In this example we use the decimal offset value `4095`. No need for a .gif on this one, just gives back a hexidecimal offset equivalent since it's out of range for a jump short and there is no support for `ESP` adjustments for alphanumeric shellcode that large yet.

```terminal_session
Enter decimal offset: 4095
[+] Hex offset: 0xfff
```

## Jump (`-j`, `--jump`)

In this mode, we simply feed the script an offset in decimal and get back:
+ Negative jump short opcodes,
+ Positive jump short opcodes. 

If the offset is outside the range of a jump short for either negative or positive, the script will tell you so. 

The script takes into account that on negative jumps, if your offset is `n`, you actually have to jump backwards `n + 2` bytes since you have to jump back through your two-byte opcode for a negative jump short. :)

### Example
```terminal_session
root@kali:~/ # offset -j 
Enter offset in decimal: 111
[-] Negative jump opcodes: \xeb\x8f
[+] Positive jump opcodes: \xeb\x6f
```

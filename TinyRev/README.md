## TinyRev

This is just a wrapper on absolomb's reverse shell they describe [on their blog](https://www.absolomb.com/2018-07-24-VulnServer-GTER/). This will literally just create the shellcode based on configurable syscall addresses, LHOST, and LPORT arguments, you still have to make sure your stack-alignment is correct. 

**Warning**, this wrapper is very hacky and probably not very useful lol. I'm pretty sure ASLR kills this approach, but I was very bored today.

## Usage

Default usage:
`python tinyrev.py`

To get the command line syntax you need for arwin.exe to find the syscall addresses:
`python tinyrev.py -a, --arwin`

## Thanks to absolomb who is a genius. 



#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("request", type=str, help="request template to fuzz")
parser.add_argument("-f", "--filename", default="http.py", type=str, nargs="?", help="select name of fuzzing script (default is http.py)", metavar='filename')
parser.add_argument("-g", "--get", help="for GET request",
                    action="store_true")
parser.add_argument("-p", "--post", help="for POST request",
                    action="store_true")

args = parser.parse_args()
request = args.request
filename = args.filename

myfile = open(request, "rt")
contents = myfile.read()
myfile.close()

host = contents.splitlines()[1]
host = host.split(":")[1]
host = host.replace(" ", "")

URI = contents.split(" ")[1]

contents = contents.replace('\r', '')
list1 = contents.split("\n")[1:-2]
list2 = contents.split("\n")[-1]
list2 = list2.split("&")

Return = 2
space = 3


def post():
	global Return
	global space
	global host
	global method
	global URI
	fuzz = open(filename, "w")
	fuzz.write('''#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("''' + host + '''", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["POST"])
        s_delim(" ", name='space-1', fuzzable = False)
        s_string("''' + URI + '''", name='Request-URI', fuzzable = False)
        s_delim(" ", name='space-2', fuzzable = False)
        s_string("HTTP/1.1", name='HTTP-Version', fuzzable = False)
	s_delim("\\r\\n", name='return-1', fuzzable = False)\n''')
	fuzz.close()

	for x in list1:
		first = x.split(" ", 1)[0]
		second = x.split(" ", 1)[1]
		fuzz2 = open(filename, "a")
		fuzz2.write('''	s_string("''' + first + '''", name="''' + first.strip(":") + '''", fuzzable = False)
	s_delim(" ", name="space-''' + str(space) + '''", fuzzable = False)
	s_string("''' + second + '''", name="''' + first.strip(":") + '''-Value", fuzzable = False)
	s_delim("\\r\\n", name="return-''' + str(Return) + '''", fuzzable = False)\n''')
		Return = Return + 1
		space = space + 1
		fuzz2.close()
	equal = 0
	amp = 0
	fuzz3 = open(filename, "a")
	fuzz3.write('''	s_delim("\\r\\n", name="return-''' + str(Return) + '''", fuzzable = False)\n''')
	fuzz3.close()
	for x in list2:
		first = x.split("=")[0]
		second = x.split("=")[1]
		fuzz4 = open(filename, "a")
		fuzz4.write('''	s_string("''' + first + '''", name="''' + first + '''-Param", fuzzable = False)
	s_delim("=", name="Equal-''' + str(equal + 1) + '''", fuzzable = False)
	s_string("''' + second + '''", name="''' + first + '''-Value", fuzzable = False)
	s_delim("&", name="Ampersand-''' + str(amp + 1) + '''", fuzzable = False)\n''')
		equal = equal + 1
		amp = amp + 1
		fuzz4.close()
	fuzz5 = open(filename, "a")
	fuzz5.write('''
    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
	    main()''')
	fuzz5.close()
		
def get():
	global Return
	global space
	global host
	global method
	global URI
	fuzz = open(filename, "w")
	fuzz.write('''#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("''' + host + '''", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["GET"])
        s_delim(" ", name='space-1', fuzzable = False)
        s_string("''' + URI + '''", name='Request-URI', fuzzable = False)
        s_delim(" ", name='space-2', fuzzable = False)
        s_string("HTTP/1.1", name='HTTP-Version', fuzzable = False)
	s_delim("\\r\\n", name='return-1', fuzzable = False)\n''')
	fuzz.close()

	for x in list1:
		first = x.split(" ", 1)[0]
		second = x.split(" ", 1)[1]
		fuzz2 = open(filename, "a")
		fuzz2.write('''	s_string("''' + first + '''", name="''' + first.strip(":") + '''", fuzzable = False)
	s_delim(" ", name="space-''' + str(space) + '''", fuzzable = False)
	s_string("''' + second + '''", name="''' + first.strip(":") + '''-Value", fuzzable = False)
	s_delim("\\r\\n", name="return-''' + str(Return) + '''", fuzzable = False)\n''')
		Return = Return + 1
		space = space + 1
		fuzz2.close()

	fuzz3 = open(filename, "a")
	fuzz3.write('''        s_static("\\r\\n", name="Request-Line-CRLF")
    s_static("\\r\\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()''')

	fuzz3.close()

if args.post:
	post()
elif args.get:
	get()
else:
	print("Specify the type of HTTP request with the --post or --get flags!")	

## Boo-Gen!

This is just a little helper that takes a saved HTTP request from a file and then uses that to generate an HTTP Boofuzz script. 

## Usage

```terminal_session
root@kali:~/ # python boo-gen.py get.txt
```

If you want to specify an output file name (the name of your boofuzz script), you can use the `-f, --filename` args. **Default output file is called 'http.py'**

```terminal_session
root@kali:~/ # python boo-gen.py get.txt -f demo.py
```

## Example

### Saved HTTP Request
```terminal_session
root@kali:~/ # cat get.txt                                                    
GET / HTTP/1.1
Host: 192.168.1.201
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sat, 15 Jun 2019 01:36:09 GMT
Cache-Control: max-age=0

```

### Saving Output Boofuzz Script to 'demo.py'
```terminal_session
root@kali:~/ # python boo-gen.py get.txt -f demo.py
```

### demo.py
```python
#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("127.0.0.1", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ['GET', 'POST'])
        s_delim(" ", name='space-1', fuzzable = False)
        s_string("/index.html", name='Request-URI', fuzzable = False)
        s_delim(" ", name='space-2', fuzzable = False)
        s_string("HTTP/1.1", name='HTTP-Version', fuzzable = False)
	s_delim("\r\n", name='return-1', fuzzable = False)
	s_string("Host:", name="Host", fuzzable = False)
	s_delim(" ", name="space-3", fuzzable = False)
	s_string("192.168.1.201", name="Host-Value", fuzzable = False)
	s_delim("\r\n", name="return-2", fuzzable = False)
	s_string("User-Agent:", name="User-Agent", fuzzable = False)
	s_delim(" ", name="space-4", fuzzable = False)
	s_string("Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0", name="User-Agent-Value", fuzzable = False)
	s_delim("\r\n", name="return-3", fuzzable = False)
	s_string("Accept:", name="Accept", fuzzable = False)
	s_delim(" ", name="space-5", fuzzable = False)
	s_string("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", name="Accept-Value", fuzzable = False)
	s_delim("\r\n", name="return-4", fuzzable = False)
	s_string("Accept-Language:", name="Accept-Language", fuzzable = False)
	s_delim(" ", name="space-6", fuzzable = False)
	s_string("en-US,en;q=0.5", name="Accept-Language-Value", fuzzable = False)
	s_delim("\r\n", name="return-5", fuzzable = False)
	s_string("Accept-Encoding:", name="Accept-Encoding", fuzzable = False)
	s_delim(" ", name="space-7", fuzzable = False)
	s_string("gzip, deflate", name="Accept-Encoding-Value", fuzzable = False)
	s_delim("\r\n", name="return-6", fuzzable = False)
	s_string("Connection:", name="Connection", fuzzable = False)
	s_delim(" ", name="space-8", fuzzable = False)
	s_string("close", name="Connection-Value", fuzzable = False)
	s_delim("\r\n", name="return-7", fuzzable = False)
	s_string("Upgrade-Insecure-Requests:", name="Upgrade-Insecure-Requests", fuzzable = False)
	s_delim(" ", name="space-9", fuzzable = False)
	s_string("1", name="Upgrade-Insecure-Requests-Value", fuzzable = False)
	s_delim("\r\n", name="return-8", fuzzable = False)
	s_string("If-Modified-Since:", name="If-Modified-Since", fuzzable = False)
	s_delim(" ", name="space-10", fuzzable = False)
	s_string("Sat, 15 Jun 2019 01:36:09 GMT", name="If-Modified-Since-Value", fuzzable = False)
	s_delim("\r\n", name="return-9", fuzzable = False)
	s_string("Cache-Control:", name="Cache-Control", fuzzable = False)
	s_delim(" ", name="space-11", fuzzable = False)
	s_string("max-age=0", name="Cache-Control-Value", fuzzable = False)
	s_delim("\r\n", name="return-10", fuzzable = False)
        s_static("\r\n", name="Request-Line-CRLF")
    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
```



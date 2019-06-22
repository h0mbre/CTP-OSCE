## Boo-Gen!

This is just a little helper that takes a saved HTTP request from a file and then uses that to generate an HTTP Boofuzz script. It has been updated to handle POST requests and fuzz the post data. 

## Usage

`boo-gen.py request.txt <method> <output filename(optional)>`

### Examples
`boo-gen.py get.txt --get -f fuzz.py`

`boo-gen.py post.txt --post -f fuzz.py`

## GET Requests

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

### Running Boo-Gen
```terminal_session
root@kali:~/ # python boo-gen.py get.txt --get
```

### Output (http.py)
```python
#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.1.201", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["GET"])
        s_delim(" ", name='space-1', fuzzable = False)
        s_string("/", name='Request-URI', fuzzable = False)
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
        s_static("\r\n", name="Request-Line-CRLF")
    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
```

## POST Requests

### Saved HTTP Request
```terminal_session
root@kali:~/ # cat post.txt                                                    
POST /registresult.htm HTTP/1.1
Host: 192.168.1.201
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.1.201/register.ghp
Content-Type: application/x-www-form-urlencoded
Content-Length: 197
Connection: close
Upgrade-Insecure-Requests: 1

UserName=hopeful&Password=hopeful&Password1=hopeful&Sex=2&Email=hopeful%40hopeful.com&Icon=0.gif&Resume=null&cw=1&RoomID=%3C%21--%24RoomID--%3E&RepUserName=%3C%21--%24UserName--%3E&submit1=Register
```

### Running Boo-Gen
```terminal_session
root@kali:~/ # python boo-gen.py post.txt --post
```

### Output (http.py)
```python
#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.1.201", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["POST"])
        s_delim(" ", name='space-1', fuzzable = False)
        s_string("/registresult.htm", name='Request-URI', fuzzable = False)
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
	s_string("Referer:", name="Referer", fuzzable = False)
	s_delim(" ", name="space-8", fuzzable = False)
	s_string("http://192.168.1.201/register.ghp", name="Referer-Value", fuzzable = False)
	s_delim("\r\n", name="return-7", fuzzable = False)
	s_string("Content-Type:", name="Content-Type", fuzzable = False)
	s_delim(" ", name="space-9", fuzzable = False)
	s_string("application/x-www-form-urlencoded", name="Content-Type-Value", fuzzable = False)
	s_delim("\r\n", name="return-8", fuzzable = False)
	s_string("Content-Length:", name="Content-Length", fuzzable = False)
	s_delim(" ", name="space-10", fuzzable = False)
	s_string("197", name="Content-Length-Value", fuzzable = False)
	s_delim("\r\n", name="return-9", fuzzable = False)
	s_string("Connection:", name="Connection", fuzzable = False)
	s_delim(" ", name="space-11", fuzzable = False)
	s_string("close", name="Connection-Value", fuzzable = False)
	s_delim("\r\n", name="return-10", fuzzable = False)
	s_string("Upgrade-Insecure-Requests:", name="Upgrade-Insecure-Requests", fuzzable = False)
	s_delim(" ", name="space-12", fuzzable = False)
	s_string("1", name="Upgrade-Insecure-Requests-Value", fuzzable = False)
	s_delim("\r\n", name="return-11", fuzzable = False)
	s_delim("\r\n", name="return-12", fuzzable = False)
	s_string("UserName", name="UserName-Param", fuzzable = False)
	s_delim("=", name="Equal-1", fuzzable = False)
	s_string("hopeful", name="UserName-Value", fuzzable = False)
	s_delim("&", name="Ampersand-1", fuzzable = False)
	s_string("Password", name="Password-Param", fuzzable = False)
	s_delim("=", name="Equal-2", fuzzable = False)
	s_string("hopeful", name="Password-Value", fuzzable = False)
	s_delim("&", name="Ampersand-2", fuzzable = False)
	s_string("Password1", name="Password1-Param", fuzzable = False)
	s_delim("=", name="Equal-3", fuzzable = False)
	s_string("hopeful", name="Password1-Value", fuzzable = False)
	s_delim("&", name="Ampersand-3", fuzzable = False)
	s_string("Sex", name="Sex-Param", fuzzable = False)
	s_delim("=", name="Equal-4", fuzzable = False)
	s_string("2", name="Sex-Value", fuzzable = False)
	s_delim("&", name="Ampersand-4", fuzzable = False)
	s_string("Email", name="Email-Param", fuzzable = False)
	s_delim("=", name="Equal-5", fuzzable = False)
	s_string("hopeful%40hopeful.com", name="Email-Value", fuzzable = False)
	s_delim("&", name="Ampersand-5", fuzzable = False)
	s_string("Icon", name="Icon-Param", fuzzable = False)
	s_delim("=", name="Equal-6", fuzzable = False)
	s_string("0.gif", name="Icon-Value", fuzzable = False)
	s_delim("&", name="Ampersand-6", fuzzable = False)
	s_string("Resume", name="Resume-Param", fuzzable = False)
	s_delim("=", name="Equal-7", fuzzable = False)
	s_string("null", name="Resume-Value", fuzzable = False)
	s_delim("&", name="Ampersand-7", fuzzable = False)
	s_string("cw", name="cw-Param", fuzzable = False)
	s_delim("=", name="Equal-8", fuzzable = False)
	s_string("1", name="cw-Value", fuzzable = False)
	s_delim("&", name="Ampersand-8", fuzzable = False)
	s_string("RoomID", name="RoomID-Param", fuzzable = False)
	s_delim("=", name="Equal-9", fuzzable = False)
	s_string("%3C%21--%24RoomID--%3E", name="RoomID-Value", fuzzable = False)
	s_delim("&", name="Ampersand-9", fuzzable = False)
	s_string("RepUserName", name="RepUserName-Param", fuzzable = False)
	s_delim("=", name="Equal-10", fuzzable = False)
	s_string("%3C%21--%24UserName--%3E", name="RepUserName-Value", fuzzable = False)
	s_delim("&", name="Ampersand-10", fuzzable = False)
	s_string("submit1", name="submit1-Param", fuzzable = False)
	s_delim("=", name="Equal-11", fuzzable = False)
	s_string("Register", name="submit1-Value", fuzzable = False)
	s_delim("&", name="Ampersand-11", fuzzable = False)

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
	    main()
```



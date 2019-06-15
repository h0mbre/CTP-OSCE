## HTTP GET/POST Fuzzer

This is just a simple addition to the standard boofuzz http fuzzing script where I added `s_string` entities for both the `Host: ` and `User-Agent: `.

Right now, all of the parameters are set to `fuzzable = False`, simply delete that part for every parameter you want to fuzz. Right now, the script will make a GET or POST request that looks like the following:
```terminal_session
GET /index.html HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
```

Let me know if you get any use out of it! I'll probably add more parameters to it at a later time. 

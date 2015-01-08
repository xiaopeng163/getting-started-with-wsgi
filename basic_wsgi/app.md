# App

## 定义

WSGI App就是一个普通的`callable`对象，当有请求到来时，WSGI server会调用这个WSGI App。
这个对象接收两个参数，通常为`environ`, `start_response`。

`environ`可以理解为环境变量，跟一次请求相关的所有信息都保存在了这个环境变量中，包括服务器信息，
客户端信息，请求信息(https://www.python.org/dev/peps/pep-0333/#environ-variables)

`start_response`是一个`callback`函数，WSGI application通过调用`start_response`，
将`response headers/status` 返回给WSGI server。此外这个WSGI app会return 一个iterator对象 ，
这个iterator就是response body。

## Hello World


``` python
#!/usr/bin/env python

""" Our tutorial's WSGI server"""


from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    """
    :param environ: environ points to a dictionary containing
    CGI like environment variables which is filled by the server
    for each received request from the client
    :param start_response: start_response is a callback function
    supplied by the server which will be used to send the HTTP
    status and headers to the server
    :return: Return the response body, and iterator object, could
    be a list or yield object
    """

    # build the response body possibly using the environ dictionary
    response_body = 'The request method was %s\nThe request path infor was %s\n' \
                    'The remote host was %s\nThe query string was %s\n' \
                    % (environ['REQUEST_METHOD'], environ['PATH_INFO'],
                       environ['REMOTE_ADDR'], environ['QUERY_STRING'])
    # HTTP response code and message
    status = '200 OK'

    # These are HTTP headers expected by the client.
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]

    # Send them to the server using the supplied function
    start_response(status, response_headers)

    # Notice it is wrapped in a list although it could be any iterable.
    return [response_body]

# Instantiate the WSGI server.
# It will receive the request, pass it to the application
# and send the application's response to the client
httpd = make_server(
    '',  # The host name.
    8000,  # A port number where to wait for the request.
    demo_app  # Our application object name, in this case a function.
    )
try:
    print "Serving on port 8000..."
    httpd.serve_forever()
except KeyboardInterrupt:
    print 'exit'
```

运行脚本，使用`curl`做测试：

```
curl 127.0.0.1:8000/get/prefix?ip=1.1.1.1\&mask=32       
The request method was GET
The request path infor was /get/prefix
The remote host was 127.0.0.1
The query string was ip=1.1.1.1&mask=32
```

## callback Function and Class

TODO
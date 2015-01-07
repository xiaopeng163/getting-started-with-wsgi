# CGI入门

通用网关接口（`Common Gateway Interface/CGI`）是客户端和服务器程序之间进行数据传输的一种标准。

`CGI`程序可以使用任何语言（`shell/Python/Perl/Ruby/PHP/C/C++`等）编写，通常它会放到Web服务器（如`Apache`）目录下的`cgi-bin`目录里。

使用`CGI`能够动态的生成网页或者网络应用，当用户访问Web服务器的时候，服务器和`应用程序`通过`CGI`接口来传递数据，最终把数据转换成网页动态的呈现在用户面前。

本文将以`Python`和`Apache`为例来演示`CGI`。
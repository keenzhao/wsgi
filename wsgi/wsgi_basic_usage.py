#!/usr/bin/python
# coding=utf-8

# WSGI应用
# 是一个接受两个参数的可调用对象

# 两个参数
# 1、environ 参数是个字段对象，包含CGI风格的环境变量
# 2、start_response 参数是一个接受两个固定参数和一个可选参数的可调用者。

# WSGI服务器
#   为每一个HTTP请求，调用WSGI应用
# 简单的服务器实现（标准库，方便开发、调试之用）
#   wsgiref  -   WSGI Utilities and Reference Implementation

# 示例演示
# wsgi app

# 最简单的WSGI Web应用框架


def application(environ, start_response):
    """
    FLASK框架的基础原理
    :param environ:
    :param start_response:
    :return:
    """
    # 定义返回值
    response_body = "<h1>Hello world!</h1>"
    # 定义header
    header = [('Content-Type', 'text/html')]
    # 定义返回状态
    status = "200 OK"
    # 启动响应方法
    start_response(status, header)
    print("environ", environ)
    # 返回响应结果
    return [response_body]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    # 最简单的WSGI服务器，把应用传递给服务器
    httpd = make_server('0.0.0.0', 8080, application)
    print("httpd run on :", httpd.server_port)
    # 运行服务器
    httpd.serve_forever()

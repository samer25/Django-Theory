"""
HTTP Protocol
(HTML Forms, HTTP Request & HTTP Response)

http://
Web Communication Explained
Web server work model:

Web Client(Chrome) --request-->Web server <---> technology(like: Django)
Web Client <--response-- Web server          |
                                             |
                            Web resources  <-|---> database
                        (HTML, PDF,IPG, etc..)


Hyper text Transfer Protocol

Computer --request--> <--Response --- server
http  |                                | http
TCP   |                                | TCP
IP    |<-----------------------------  | IP
ETHERNET|-------------|--------------->|Ethernet
                Media(wires/air/fiber)


HTTP Request Methods

Method | Description
-------|------------
POST   | Create/store a resource
-------|------------
GET    | Read/retrieve a resource
-------|------------
PUT    | Update/ modify a resource
-------|------------
DELETE | Delete/remove a resource
-------|------------
(The four basic function of persistence storage)
"""

"""
HTTP Conversation: Example
-Http request:
GET /course/javascript HTTP/1.1
Host: www.softuni.bg
User-Agent: Mozilla/5.0
<CRLF> (The empty line denotes the end of the request headers)

-HTTP response
HTTP/1.1 200 OK
Date: Mon, 5 Jul 2020 13:09:03 GMT
Server: Microsoft-HTTPAPI/2.0
Last-Modified: Mon, 12 Jul 2021 15:33:23 GMT
Content-Length: 54
<CRLF> (The empty line denotes the end of the response headers)
<html><title>Hello</title>
Welcome to our site<html>
"""

"""
Tools for Developers
(Dev Tools)

Chrome Developer Tools, Postman, Postman(desktop)
"""

"""
Form Method and Action(html forms)
HTML Forms - Action Attribute

<form action="home.html">
    <input type="submit" value="Go to homepage">
</form>


HTML Forms - Method attribute

Specifies the HTTP method to use when sending form data
<form method="get">
    Name: <input type="text" name="name">
            <br/> <br/>
          <input type="submit" value="submit">
</form>  
The form data will appear in the url: index.html/name=Sammy


URL Encoded form data - Example:

<form method="post">
    Name:   <input type="text" name="name">
            <br/> 
    Age:    <input type="text" name="age">
            <br/>
            <input type="submit" value="submit">
</form>

POST http://localhost/cgi-bin/index.cgi HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded (File uploads are not supported)
Content-Length: 23

name=Maria+smith&age-19

"""

"""
Multi-purpose internet mail extensions
(MIME and Media Type)

MIME = Multi-Purpose Internet Mail Extensions
-Internet standard for encoding resources
-Originally developed for email attachments
-Used in many Internet protocols like HTTP and SMTP


Content-Disposition - Example

Content-Type: text/plain
Content-Length: 19
Content-Disposition: inline
filename=example.txt
    in browser
        |
        |
http://content-disposition-inline.html :

This is inline view


Content-Disposition - Example(2)

Content-Type: text/plain
Content-Length: 19
Content-Disposition: attachment;
filename=example.txt
        |
        |
Opening example.txt
you have chosen to open:
    example.txt
    which is: TXT file (19 bytes)
    form: http://localhost
"""
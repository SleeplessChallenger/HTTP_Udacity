<h2>Requests & Responses</h2>

Server - program that accepts connections from other programs on the network
Browser sends HTTP request to the server

Web address == URL/URI. Every URI can be broken into smaller subsections:
- scheme: https/http/file
Tells the client how to access the resource
- hostname: en.wikipedia.org/localhost
But not every URI has a hostname. Also, : comes after scheme and // before
hostname, hence if hostname is absent -> no //
- path: identifies a particular resource on a server. Resource can be either 
video or web page or API.
Note: http://udacity.com/ that last slash is called root path which browser
autofills if you write simply http://udacity.com

Other URI parts: 1) # is a fragmnet (relates to `id` in html) 2) ?q=something is a
query part of the URI which get sent to the server

Every piece of network traffic on the internet is labeled with the IP addresses of
sending and receiving computers. So, to connect to web server, like www.udacity.com,
1. client translates the hostname into an IP address by looking up for that IP in
DNS (domain network dervice) [set of servers maintained by the Internet Service Providers]

IPv4 127.0.0.1 & IPv6 ::1 are IP addresses of your computer. So, when client, for ex browser, accesses a server on your own computer -> hostname `localhost` refers to those IP addresses.
0.0.0.0 includes every IPv4 address on this computer. That includes the localhost address, but it also includes your computer's regular IP address.

Everything on the net is transferred by `packets`. Every packet has IP addresses of
the computer sending the request and receiving the request. And within that packet
there is a `port number` for the sender and the recipient. "IP addresses distinguish
computers, port numbers distinguish programs on those computers". Also, there are 
default port numbers which client figres out from the URI scheme: HTTP - 80, HTTPS - 
443

HTTP verbs: get/post/put/delete/patch
Ex: GET /readme.png HTTP/1.1
GET request has three parts:
1. method/verb itself 2. path (note that relative path not absolute)
3. protocol: HTTP/1.1

Start up a server: python3 -m http.server 8000, then ncat 127.0.0.1 8000 to
connect to the demo server. Then type follwoing GET request   GET / HTTP/1.1
															  Host: localhost
You'll receive an HTTP response. It consists of 3 parts: 1. status line 2. headers 3. response body (piece of HTML)

1. Status line: HTTP/1.0 200 OK or HTTP/1.1 301 Moved Permanently
2. Headers: sort of metadata for the response (Ex. Location, Content-type). 
Note: cookie is a header to make user stay logged in. `Set-Cookie` header
3. Response body: if the Request was successful -> it's a copy of the resource client
asked for (i.e. web page/image etc). If error -> error appears on the screen

data = self.rfile.read(weight).decode()
is for decoding encoded string message




<h2>The Web from Python</h2>

look at the following files to see code implementation:


Queries & strings: '?' is a query parameter. Usually, they're written in `key=value` fashion and separated by `&`.

- urlparse is for separating string into chunks and then we can see the desired
  parts, like: `print(u.query)` to see the very query part
- parse_qs is for dividing those very string queries into key-value pairs: `print(parse_qs(u.query))`

`+` sign in query is a so-called **URL-encoding or URL-escaping**. But when we use `parse_qs`, it'll be replaced with `spaces`. Other special characters are translated into hexadecimal codes that begin with the percent sign.

To take the data from HTLM form, you need to pay attention to `name=` in the very form.

When a browser submits a form as a POST request, it doesn't encode the form data in the URI path, the way it does with a GET request. Instead, it sends the form data in the request body, underneath the headers. The request also includes Content-Type and Content-Length headers, which we've previously only seen on HTTP responses.

If the requests.get call can reach an HTTP server at all, it will give you a Response object. If the request failed, the Response object has a status_code data number — either 200, or 404, or some other code.
But if it wasn't able to get to an HTTP server, for instance because the site doesn't exist, then requests.get will raise an exception.



<h2>HTTP in the Real World</h2>

The basic, built-in http.server.HTTPServer class can only handle a single request at once. The bookmark server tries to fetch every URI that we give it, while it's in the middle of handling the form submission.

Look at `concurrent_bookmark.py` for tweaked server.

Nginx/Apache/IIS are web server programs. They can act as **reverse proxy** and do **load balancers**. Also, manage **request routing** when web application has several server components where each runs as a separate process (i.e. dispatch requests to the particular server)

in-flight requests, meaning that the request has "taken off" from the client, but the response has not "landed" again back at the client.


About caching:

Web systems can perform caching in a number of places — but all of them are under control of the server that serves up a particular resource. That server can set HTTP headers indicating that a particular resource is not intended to change quickly, and can safely be cached.


HTTP/1.1 :

Since the early days of HTTP, browsers have kept open multiple connections to a server. This lets the browser fetch several resources (such as images, scripts, etc.) in parallel, with less waiting. However, the browser only opens up a small number of connections to each server. And in HTTP/1.1, each connection can only request a single resource at a time

HTTP/2:

HTTP/2 changes this around by `multiplexing` requests and responses over a single connection. The browser can send several requests all at once, and the server can send responses as quickly as it can get to them. There's no limit on how many can be in flight at once.
+ Server push
	When you load a web page, your browser first fetches the HTML, and then it goes back and fetches other resources such as stylesheets or images. But if the server already knows that you will want these other resources, why should it wait for your browser to ask for them in a separate request? HTTP/2 has a feature called server push which allows the server to say, effectively, "If you're asking for index.html, I know you're going to ask for style.css too, so I'm going to send it along as well."


Cookies

1. Cookies are a way that a server can ask a browser to retain a piece of information, and send it back to the server when the browser makes subsequent requests. Every cookie has a name and a value, much like a variable in your code; it also has rules that specify when the cookie should be sent back.

What are cookies for?
A few different things. If the server sends each client a unique cookie value, it can use these to tell clients apart. This can be used to implement higher-level concepts on top of HTTP requests and responses — things like sessions and login. Cookies are used by analytics and advertising systems to track user activity from site to site. Cookies are also sometimes used to store user preferences for a site.

2. How cookies happen
The first time the client makes a request to the server, the server sends back the response with a Set-Cookie header. This header contains three things: a cookie name, a value, and some attributes. Every subsequent time the browser makes a request to the server, it will send that cookie back to the server. The server can update cookies, or ask the browser to expire them.



`http://localhost:8000/`

`http://localhost:8080/hello`

`http://localhost:8080/restaurants`

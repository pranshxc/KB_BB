---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-06_dom-xss-walkthrough.md
original_filename: 2020-05-06_dom-xss-walkthrough.md
title: DOM XSS Walkthrough
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: d14ba8e09393cf1ae637592fad2d6eb0694f001d9d1fdb23b24f3b94e59ebffe
text_sha256: 48d92ea8998bd9329c5e9db3c5514890ee28f5fdf140133944261cab48eb65c7
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# DOM XSS Walkthrough

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-06_dom-xss-walkthrough.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `d14ba8e09393cf1ae637592fad2d6eb0694f001d9d1fdb23b24f3b94e59ebffe`
- Text SHA256: `48d92ea8998bd9329c5e9db3c5514890ee28f5fdf140133944261cab48eb65c7`


## Content

---
title: "DOM XSS Walkthrough"
url: "https://medium.com/@youssefla/dom-xss-walkthrough-4d60c45ffb21"
authors: ["Youssef Lahouifi (@YLahouifi)"]
bugs: ["DOM XSS"]
publication_date: "2020-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4603
scraped_via: "browseros"
---

# DOM XSS Walkthrough

DOM XSS Walkthrough
Youssef Lahouifi
Follow
4 min read
·
May 7, 2020

140

Introduction :

I was checking my email and i found a DOM XSS vulnerability that I have reported to a program long time ago which isn’t patched yet , and i thought why not writing about this …

Please ignore grammar errors i m not that good

What Is An XSS Vulnerability ?

If you can execute your javascript code into a web page you’ve got an xss.
There are basically three types of xss :reflected , stored and DOM-based .
in this article we re going to talk about the DOM-based type.

What Is Dom XSS ?

it’s a client side vulnerability which happens when javascript code takes the source and mishandling it in a way that causes execution of it in sink(execution function).

Enough theory let’s see an example :

<html>
 <head>
  <title>dom xss example</title>
 </head>
 <body>
  <script>
  var x = document.location.hash.substr(1);
  window.location=x;
  </script>
</body>
</html>

suppose there’s an html page that’s using the code above . it basically takes what’s after the hash in the URL and use it to redirect the user to it using window.location .

If the attacker supplies the value javascript:alert(1) after the hash , this will result in the execution of alert(1) function as proof of DOM XSS vulnerability.

So the exploit would be : http://victim/domxss.html#javascript:alert(1)

In the previous part I’ve used two keywords which i didn’t explain yet : source and sink . What are these , and how could they help us find a DOM XSS vulnerability ?

Source And Sink Concept :

There are two main things you should focus on when you look for DOM XSS vulnerabilities :

Source and Sink .

Source is the location from which untrusted data is taken by the application (which can be controlled by user input) and passed to the sinks which are places where untrusted sources is actually getting executed .

Click here for more on the topic !

So finding a dom xss vulnerability is finding a way to pass the source to the sink .

Get Youssef Lahouifi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When we talk about javascript there are mainly 4 categories of sources :

URL-Based sources such as : document.url , document.location.hash
Navigation based sources such as : document.referer , window.name
communication sources such as : ajax , websockets and webmessaging
storages sources such as : cookies , localstorage ,session storage.

And 4 main categories of sinks :

javascript execution sinks as : eval(payload) , setTimout(payload,100) , <div onclick=”payload”>
HTML execution sinks as : htmlElement.innerHTML= payload , document.write(payload)
javascript URI sinks as : document.location = payload , location.href = payload
HTML modification to behaviour change : (element).src or (element).href (in certain elements)
DOM XSS Example :

For seek of demonstration we re going to use a public instance of firing range here .

Let’s see this example here :

If you open this simple HTML page in the browser, it won’t render any content and you won’t see anything from what’s in it. But when you take a look at source code, things are going to become much more interesting :

It seems that there’s a postMessage() event listener which expect a message in JSON format and then checks for the value of msg.data.action and if it’s equal to ‘exec’ it executes the function eval(msg.data.payload).

open the chrome developer tool console tab and try :

window.postMessage({“action”:”exec”,”payload”:”alert(document.domain)”},”*”)

And as you will see the javascript code we’ve provided will get executed .

So all we gotta do to exploit this vulnerability , is host publicly a malicious HTML page containing the following code :

<iframe onload="send()" id="f" src="https://public-firing-range.appspot.com/dom/toxicdom/postMessage/complexMessageDocumentWriteEval"></iframe>
<script>
 function send(){
  var x = {"action":"exec","payload":"alert(document.domain)"}
  document.getElementById('f').contentWindow.postMessage(x,"*");
 }
</script>
Bad sender

Visit the page , and as you will see we’ve got an alert box containing document.domain value as proof of XSS.

Real World Example Of DOM XSS Vulnerability :

Notice: I’m not going to mention the target here , since the vulnerability isn’t patched yet .

While doing recon on the target, I came across a simple html page which shows a simple link , and after investigating the source code I saw this:

It seems that javascript is expecting a ‘url’ parameter , takes its value , check if it matches some predefined values , if not it includes that value in a ‘href’ attribute of an ‘a’ tag as javascript:window.open(‘“+newurl+”’) where newurl is the value of ‘url’ parameter . Once you click the link the browser will open a new window tab with the ‘url’ value we’ve provided, so all we gotta do is add ?url=javascript:alert(document.domain)

And the exploit will be https://victim.com/vulnerable.html?url=javascript:alert(1)

And once clicking that link the javascript code we’ve entered will get executed!

It worth mentioning a small tip here : Don’t ignore HTML pages they might be vulnerable !

References :

In this section I’ll just leave some references I think they might be useful:

- https://hackerone.com/reports/297968
- https://public-firing-range.appspot.com/dom/index.html
- https://domgo.at/cxss/intro
- https://portswigger.net/web-security/cross-site-scripting/dom-based
- https://opnsec.com/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome/
- https://github.com/wisec/domxsswiki/wiki

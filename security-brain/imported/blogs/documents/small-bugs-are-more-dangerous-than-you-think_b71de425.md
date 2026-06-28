---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-01_small-bugs-are-more-dangerous-than-you-think.md
original_filename: 2022-04-01_small-bugs-are-more-dangerous-than-you-think.md
title: Small bugs are more dangerous than you think
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- csrf
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- csrf
- clickjacking
- api-security
language: en
raw_sha256: b71de42500b6b21eae0ad06dc8ab7ba559df59a96584a216c9048c70b741d8ec
text_sha256: e94a0c600253cc0d77665f4b46991c430b05c1f19000a6608f215f9aa26c325a
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Small bugs are more dangerous than you think

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-01_small-bugs-are-more-dangerous-than-you-think.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, csrf, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `b71de42500b6b21eae0ad06dc8ab7ba559df59a96584a216c9048c70b741d8ec`
- Text SHA256: `e94a0c600253cc0d77665f4b46991c430b05c1f19000a6608f215f9aa26c325a`


## Content

---
title: "Small bugs are more dangerous than you think"
url: "https://medium.com/@terminatorLM/small-bugs-are-more-dangerous-than-you-think-9411618191ab"
authors: ["Liv Matan (@terminatorLM)"]
bugs: ["Self-XSS", "Stored XSS", "Open redirect", "CSRF"]
publication_date: "2022-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2763
scraped_via: "browseros"
---

# Small bugs are more dangerous than you think

Small bugs are more dangerous than you think
Liv
Follow
5 min read
·
Apr 1, 2022

53

5

Hello hackers, I am Liv, a web security researcher and a full-stack developer.

The useless open redirect
Let’s cut straight to the chase, I was presented with a stock marketing target which seems pretty strange at first glance at the login page -

Press enter or click to view image in full size

If you are familiar with Open Redirects vulnerability, it would be intriguing for you to see the Remote Page Layout URL Redirect input at first.
Well… not so easy -
I started testing by putting some URLs in the input to test the behavior of the functionality, is there a whitelist of approved URLs? or is it just straightforward no filter redirect to any website I want.
After some testing, it seems like nothing is there, the page is not redirected after logging in, no nothing!

I moved on and tried to test for the other parameters, then I figured out an odd behavior. When putting any character which is not null in the field Remote Page Layout URL, combined with the Redirect field, I got an open redirect when logging in.

Ok, nice, very strange and weird, but nice! When trying to escalate further, seems like the web application returns an error code in the GET parameter as follows:

Press enter or click to view image in full size
PII is not leaked

*javascript:alert() did not work either :(

I tried to put the variables with the payload in the URL to craft an open redirect phishing link to send, but again this strange target did not reflect the value from the GET parameter to the HTML input even after testing the JS, HTML, and debugging it. Useless open redirect with no way to even pass it to other users?
Not quite, stay with me.

Stored XSS, but a selfish one
Later on, I tested the nickname input field for XSS, again, GET params does not reflect on the login page. I tried injecting the payload and search for a second-order XSS on the index page after logging in. Unfortunately, all the inputs seemed filtered or HTML encoded but wait a second… I went back to the login page for more testing and I saw something interesting!

Press enter or click to view image in full size

The nickname parameter is not sanitized, and even better, it is stored on the server after logging in. Let’s fix the payload and execute XSS -

Press enter or click to view image in full size
“><script>print()</script>

We got a Stored XSS this is it right?
1. Self Stored XSS :(
2. The XSS fires only when the user navigates back to the login page which can be good to steal his cookies after he logged in but not so doable.

Get Liv’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Chaining bugs for the win
And then it hit me… What if I combine a Login CSRF (This type of CSRF is usually not protected due to the nature of the attack), the open redirect I found before, and the Stored XSS all together?
It goes like this:
1. The victim enters my website, POST Login CSRF is fired automatically with the open redirect payload in it, and the XSS payload.
2. The open redirect payload is the login page of the website.
3. Victim logins to the website, redirected after logging in back to the login page and the XSS executes instantly.

I talked with my fellow partner 
Osher Zbadi
 to make it happen together and we coded a POC.
Remember the error code from the redirect before?

Press enter or click to view image in full size

The attack failed. We were very disappointed but there is no way I am giving up on this.

Tricking the parser
We thought about how can we bypass this error code, the point is I control the redirect URL. The error code is added as a GET parameter, what if I add a fragment at the end of the open redirect URL to make the server ignore the error code when parsing the URL?
For those of you who are not familiar- “A fragment is an internal page reference, sometimes called a named anchor. It usually appears at the end of a URL and begins with a hash (#) character followed by an identifier.”
This trick can work because the browser ignores everything after the fragment is declared in the URL.

Therefore, the server interprets the URL as a regular login URL, the saved parameters with the XSS are returned as a response from the server and the XSS executes :)

Note: The CSRF can be automatically executed by auto submit

Me and 
Osher Zbadi
 were so happy to see it worked!
We reported it to the target and it got fixed ASAP.

Considering the final impact and a key takeaway
The website uses HTTP basic authentication, so if the victim is logged in, attackers can potentially restrict him from logging in by redirecting him every time he enters the login page. Also, stealing his cookies and even popping up an iframe to make a clickjacking attack or phishing the HTTP basic auth creds.

The key takeaway to take from this writeup is to never underestimate a low severity bug, sometimes it can be escalated by chaining it with other bugs and getting you a bounty or a smile on your face.

Thank you for your time reading my writeup, I hope you learned something new or at least had a smile or two (see what I did there?)

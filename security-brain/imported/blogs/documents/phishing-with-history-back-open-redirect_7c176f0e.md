---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-09_phishing-with-historyback-open-redirect_2.md
original_filename: 2017-09-09_phishing-with-historyback-open-redirect_2.md
title: Phishing with history.back() open redirect
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 7c176f0e3388a96bcaf920b9e37cba0070677f2fb73eed7bd16b0a22dfc3b201
text_sha256: d847d1b378a35678b186410c697966a81f52eb61148c202fc1eb622e5861ad7b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Phishing with history.back() open redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-09_phishing-with-historyback-open-redirect_2.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7c176f0e3388a96bcaf920b9e37cba0070677f2fb73eed7bd16b0a22dfc3b201`
- Text SHA256: `d847d1b378a35678b186410c697966a81f52eb61148c202fc1eb622e5861ad7b`


## Content

---
title: "Phishing with history.back() open redirect"
url: "https://medium.com/@0xHyde/exploiting-history-back-3ec789c124dd"
authors: ["Brian Hyde (@0xHyde)"]
bugs: ["Open redirect"]
publication_date: "2017-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6107
scraped_via: "browseros"
---

# Phishing with history.back() open redirect

Phishing with history.back() open redirect
hyde
Follow
2 min read
·
Sep 9, 2017

106

2

While participating in a private bug bounty program I ran into a WAF error page that contained details about the request as well as a hyperlink that would send the user back one page. After playing around with some javascript, I was able to use this technique as an open redirect on all buttons that use the history.back() or history.go(-int) function for web applications that use a back button controlled by the history.back() or history.go(-1) function, assuming the payload is the page you are being sent back to.

Payload (index.html):

<html>
  <head>
  <title>Continue</title>
  </head>
  <body>
  <a onclick=exploit() href="example_of_vuln.html">Continue...</a>
  <script>
  function exploit(){
  history.replaceState({page: 1}, "Exploit", "index.htm");
  }
  </script>
  </body>
</html>

Example of a vulnerable page (example_of_vuln.html):

<script>alert('Going Back!');history.back()</script>

After Exploitation (index.htm):

<html>
  <head>
  <title>Exploited</title>
  </head>
  <body>
  <h1>Your browser history was manipulated to send you to a page you never even visited!</h1>
  </body>
</html>

I didn’t think this would be very applicable to a real life threat scenario until I discovered that google.com has a page located below which allows a user to determine how many times they would go backwards in their history using the javascript function history.go(-n), ‘n’ being the integer provided in the backstep GET parameter.

https://accounts.google.com/_/back?backstep=1

In a lab environment I was able to use this bug as a phishing vector. I found out that I could lead a target from my payload linking directly to a Google Sites blog which contained the following url as a hyperlink:

https://accounts.google.com/_/back?backstep=2

And finally, onto the ‘Malicious Page’.

Get hyde’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To better show the flow:

Payload -> Google Sites Blog -> Click on the URL: https://accounts.google.com/_/back?backstep=2 -> Demo Phishing Page

I submitted a report to Google about this through their bug bounty program without much luck, however it was still fun to research and develop a potential attack scenario.

Initial Payload:

Press enter or click to view image in full size

Vulnerable Page:

Press enter or click to view image in full size

Exploit Successful, note that the first image is /index.html and page is sent back to a page that you never even visited (index.htm).

Press enter or click to view image in full size

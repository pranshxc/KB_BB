---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-18_xss-bypass-using-meta-tag-in-realestatepostnlnl.md
original_filename: 2018-11-18_xss-bypass-using-meta-tag-in-realestatepostnlnl.md
title: XSS bypass using META tag in realestate.postnl.nl
category: blogs
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- blogs
- xss
- command-injection
- api-security
language: en
raw_sha256: 107754f3e77de536bdb6a5941175753153d0d7d0cde1932c4ee931af5c72d3dd
text_sha256: cc5e3131c923930d8ced6074b4367acae7a3b86cd5860f2a934c034dcf65dc8f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSS bypass using META tag in realestate.postnl.nl

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-18_xss-bypass-using-meta-tag-in-realestatepostnlnl.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `107754f3e77de536bdb6a5941175753153d0d7d0cde1932c4ee931af5c72d3dd`
- Text SHA256: `cc5e3131c923930d8ced6074b4367acae7a3b86cd5860f2a934c034dcf65dc8f`


## Content

---
title: "XSS bypass using META tag in realestate.postnl.nl"
url: "https://medium.com/bugbountywriteup/xss-bypass-using-meta-tag-in-realestate-postnl-nl-32db25db7308"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["post.nl"]
bugs: ["XSS"]
publication_date: "2018-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5575
scraped_via: "browseros"
---

# XSS bypass using META tag in realestate.postnl.nl

Top highlight

XSS bypass using META tag in realestate.postnl.nl
Prial Islam Khan
Follow
3 min read
·
Nov 18, 2018

366

7

Hi readers ,

Today I will write about a XSS Vulnerability I reported to postnl.nl bug bounty Program .

Vulnerable Endpoint :- http://realestate.postnl.nl/?Lang=

To test a normal Reflected XSS I Input “><xsstest> in the Lang parameter and in source it was reflected properly inside META tag like below :-

<meta name="language" content=""><xsstest>" />

Looks simple right ? Then wait a little :’) . Then I Inputted “><img src=x> and I got :-

Press enter or click to view image in full size
Surprise you nigga 🥳🥳🥳

I tried with many HTML tags and I got 2 points here :-

Any Valid HTML tag is not allowed .
I can created any attributes here .

So I googled for meta tag attributes and got :-

Press enter or click to view image in full size
looks interesting 🤔🤔🤔

The http-equiv attribute took my attention . Now I again google more about it and learned that :-

META tag has the http-equiv directive. This directive allows you to define the equivalent of an HTTP header in the HTML code . The http-equiv directive can take a value of refresh , which can be used to redirect a user to another page.

Get Prial Islam Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I input 0;http://evil.com"HTTP-EQUIV="refresh" and response was :-

<meta name="language" content="0;http://evil.com"HTTP-EQUIV="refresh"" />

And I got redirected to evil.com . So I have open redirection now . Now we can try for Data URI XSS . So I input :- 0;javascript:alert(1)"HTTP-EQUIV="refresh" and response was :-

Press enter or click to view image in full size

This was again Triaged for the keyword javascript used in payload . So I used Base64 encoded payload :- 0;data:text/html;base64,PHNjcmlwdD5wcm9tcHQoIlJlZmxlY3RlZCBYU1MgQnkgUHJpYWwiKTwvc2NyaXB0Pg=="HTTP-EQUIV="refresh" and response source was :-

<meta name="language" content="0;data:text/html;base64,PHNjcmlwdD5wcm9tcHQoIlJlZmxlY3RlZCBYU1MgQnkgUHJpYWwiKTwvc2NyaXB0Pg=="HTTP-EQUIV="refresh"" />

And now when I visit http://realestate.postnl.nl/?Lang=0%3Bdata%3Atext%2fhtml%3Bbase64%2CPHNjcmlwdD5wcm9tcHQoIlJlZmxlY3RlZCBYU1MgQnkgUHJpYWwiKTwvc2NyaXB0Pg%3D%3D%22HTTP-EQUIV%3D%22refresh%22 I got XSS popup .

Press enter or click to view image in full size

I reported it to their Zerocopter report form . Then they deployed a Fix by blacklisting the data:text/html;base64 keyword like they have blacklisted JavaScript keyword but still I can do Open Redirect when a user visits :- http://realestate.postnl.nl/?Lang=0%3Bhttp%3A%2f%2fevil.com%22HTTP-EQUIV%3D%22refresh%22

Press enter or click to view image in full size
Looks cool 🙄🙄🙄

They again Fixed the issue and listed My name on their Hall Of Fame page & also offered to send some goodies 😍😍😍 .

Press enter or click to view image in full size
😍😍😍

Thanks for reading .

Follow me on twitter

If you have any query ask me on Facebook

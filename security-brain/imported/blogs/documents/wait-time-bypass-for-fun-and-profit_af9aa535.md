---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_wait-time-bypass-for-fun-and-profit_2.md
original_filename: 2023-03-10_wait-time-bypass-for-fun-and-profit_2.md
title: Wait Time Bypass for fun and Profit
category: documents
detected_topics:
- rate-limit
- idor
- access-control
- xss
- sqli
- command-injection
tags:
- imported
- documents
- rate-limit
- idor
- access-control
- xss
- sqli
- command-injection
language: en
raw_sha256: af9aa5351520fd5eec7a703424c3477c5484044e1320366a26245a799a03a322
text_sha256: 6e7b06646501f4a8669661f6fa3025010ef8669dd79a41d510ac71607761b258
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Wait Time Bypass for fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_wait-time-bypass-for-fun-and-profit_2.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, access-control, xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `af9aa5351520fd5eec7a703424c3477c5484044e1320366a26245a799a03a322`
- Text SHA256: `6e7b06646501f4a8669661f6fa3025010ef8669dd79a41d510ac71607761b258`


## Content

---
title: "Wait Time Bypass for fun and Profit"
url: "https://vijetareigns.medium.com/wait-time-bypass-for-fun-and-profit-c3837e6bb8ed"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
programs: ["Automattic"]
bugs: ["Rate limiting bypass"]
publication_date: "2023-03-10"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1400
scraped_via: "browseros"
---

# Wait Time Bypass for fun and Profit

Wait Time Bypass for fun and Profit
the_unlucky_guy
Follow
3 min read
·
Mar 10, 2023

256

3

Hello hackers, I am back with another bug bounty write-up. In today’s blog, I am going to show you how I was able to bypass a ban time of 20 Minutes.

This bug was on one of the domains from the Automattic. *.intensedebate.com is in scope. I started hunting for issues on the main application, which is a debate platform with a variety of features like creating posts, sharing opinions, and more.

I created an account and spent 2 hours looking for bugs such as IDOR, XSS, Business Logic bugs, Access control related bugs, SQLi, Account Takeover and Information Disclosure but not got anything in my hand. During performing password brute force on http://intensedebate.com/ login page, I got banned for 20 Min.

Press enter or click to view image in full size

My all time habit is to capture each and every request in burp suite. So, I started looking for all HTTP request of http://intensedebate.com/ in my target tab of burp suite. I came across one GET endpoint that seemed particularly interesting to me.

The URL is http://intensedebate.com/js/commentAction/?data={"request_type":"2", "params":{"blogpostid":1, "acctid":1, "email":"user_email_id", "pass":"user_password", "firstCall":true}} As you can see, the path is having email and pass as a parameter in the GET request. I open the URL in the browser with the correct credentials and landed on a JS page.

Press enter or click to view image in full size

I notice that the JavaScript page have several clickable links, including a ‘Send password reset’ link (as you see in the image). I clicked on it without entering anything and was redirected to a 404 page but at the same time i got logged into my account.

Press enter or click to view image in full size

What I did next is, first I get myself a ban of 20min through brute-forcing and then open the GET endpoint http://intensedebate.com/js/commentAction/?data={"request_type":"2", "params":{"blogpostid":1, "acctid":1, "email":"user_email_id", "pass":"user_password", "firstCall":true}} with my username and password, and clicked on the Send password reset link and got logged in to my account this is how I bypass the 20Min wait time.

Tip: Always capture each and every request in the burp suite and later review it all.

Get the_unlucky_guy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

Jan 19, 2021 — Reported

Feb 4, 2021 — Fixed and $$$ Bounty awarded

Thanks for reading, hope you learned something new. Do clap and share if you like. I will write more of my findings soon so, stay tuned for my next write-up. Happy Hacking!

Twitter: 7he_unlucky_guy
Linkedin: Vijeta

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-13_hacking-a-telecommunication-companymtn.md
original_filename: 2020-04-13_hacking-a-telecommunication-companymtn.md
title: Hacking a Telecommunication company(MTN)
category: documents
detected_topics:
- sqli
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: c32727ee654706e6b0b85632e2d2858e8bc8788aa76574988b240f13f5f53343
text_sha256: 3afbea08e13117bbb435483d2826b2aee3f57a492f2084f881be7c09bec65724
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a Telecommunication company(MTN)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-13_hacking-a-telecommunication-companymtn.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c32727ee654706e6b0b85632e2d2858e8bc8788aa76574988b240f13f5f53343`
- Text SHA256: `3afbea08e13117bbb435483d2826b2aee3f57a492f2084f881be7c09bec65724`


## Content

---
title: "Hacking a Telecommunication company(MTN)"
url: "https://medium.com/@afolicdaralee/hacking-a-telecommunication-company-mtn-c46696451fed"
authors: ["Afolic"]
programs: ["MTN Group"]
bugs: ["OTP bypass", "Bruteforce"]
publication_date: "2020-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4657
scraped_via: "browseros"
---

# Hacking a Telecommunication company(MTN)

Hacking a Telecommunication company(MTN)
Afolic
Follow
4 min read
·
Apr 13, 2020

212

1

Good day folks, hope you all are doing okay?

Today, I will be making a write-up about a vulnerability I found on MTN Nigeria around December of 2019 which could have allowed me to take-over any MTN user web account through their phone number.

About the Target:

According to wikipeida, MTN Group Limited, formerly M-Cell, is a South African multinational mobile telecommunications company, operating in many African, European and Asian countries. Its head office is in Johannesburg. As of 30 June 2016, MTN recorded 232.6 million subscribers, making it the eighth largest mobile network operator in the world, and the largest in Africa. Active in over 20 countries, one-third of company revenue come from Nigeria, where it holds about 35% market share.

Press enter or click to view image in full size

A little back story, I have always wanted to test the security of MTN out but for some reasons I couldn’t bring myself probably because I was too lazy but one night, my PC battery was going low so I quickly decided to check a sub-domain of the MTN web application since I subscribed to their mid-night data bundle and I already exhausted my data and every website I visit redirects me to that sub-domain to buy a new data plan. Luckily for me, I found a SQL injection under 15 minutes of testing which really made me optimistic that I can still find something. Few days after, I decided to test the main MTN Nigeria website out and I found an account take-over which I will be discussing about in this blog post.

About the vulnerability:

This vulnerability falls under CWE-307 which is the weakness ID for Improper Restriction of Excessive Authentication Attempts. This vulnerability occurs when the application fails to limit or restrict the number of trials that can be attempted when trying to authenticate to its server.

Particularly for the MTN web application, in order for you to be authenticated to your MTN web account, an OTP code will be sent to your phone number. Entering the correct OTP code on the web application is only when you will be authenticated. Now where this vulnerability was introduced is the MTN web application did not implement any form or protection against brute forcing but relied on the OTP code to expire thus making it possible for an attacker to be able to successfully brute force an OTP code without getting blocked.

Exploitation Process:

After finding the SQL injection, I decided to test the MTN Nigeria web application out to see what I could find. I was not hoping for much though,so I just decided to playing around. I visited https://www.mtnonline.com/ , this loaded up the MTN webpage up, scrolling down the page I saw a button to login to my mtn account which I clicked on. Clicking on this button redirected me to https://mymtn.com.ng/ , on this page I was asked to enter your phone number after which an OTP code was sent to my phone number. Entering my phone number, a 4 digits OTP code was sent to me. At this point my hacker mindset just clicked in, wait!!! this is a 4 digit OTP code, this should be easy brute forcible rights?. Immediately, I fired-up Burp-suite and configured my browser to send any request from MTN to be logged in Burp-suite. After doing this, I immediately created a wordlists of all possible combinations 4 digits. When this was done, I turned on intercept in Burp-suite and went back to the MTN web application, intentionally entered a wrong OTP code, sent the request, switched to Burp-suite, captured the OTP request, right clicked on the request and sent it to intruder and after sometimes I get getting an error message saying the session ID has expired, I tried requesting for another OTP code and tried brute-forcing again and got the same error message. At this point that was when it hit me that this is an OTP code and it does expire and Burp-suite intruder might not be fast enough to brute force the right OTP code under that time constraint. All thanks to James Kettle of Burp-suite, he already created a tool which is a Burp-suite plugin called Turbo Intruder which basically does the work Burp-suite Intruder but at a faste speed. Quickly I installed Turbo Intruder and perform the process all over again but this time instead of sending the request to Intruder, I sent it to Turbo Intruder and after about a minute, Turbo Intruder brute force the right OTP code and I was able to login to my MTN web account.

Get Afolic’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After this, I made a vulnerability report and submitted it to them via their bug bounty program on Hackerone.

Timeline of the report:

Submitted the initial Report on 18, Dec. 2019

Report triaged by a MTN staff few minutes after

Vulnerability fixed and I was asked to confirm the fix on 19, Dec. 2019

I confirmed the fix few minutes after.

N.B: A lot of changes has been made to the MTN web application from the time of finding this vulnerability to now.

If at any point you get confused, you can refer to links below.

Now when you try to brute force an OTP code, the victim gets a text message notifying them that a bruteforce attack is going on, the attacker gets blocked for some time and also the OTP code sent now is a 6 digit code instead of the previous 4 digit code. Something similar to this:

Press enter or click to view image in full size

References:

My Hackerone Report: https://hackerone.com/reports/761000

POC Video: https://drive.google.com/open?id=16v6NytozaHaqDh3-Ewvps0ezqOSpIAlv

Contact me:

::1
The latest Tweets from ::1 (@itsafolic). Wanna be Hacker

twitter.com

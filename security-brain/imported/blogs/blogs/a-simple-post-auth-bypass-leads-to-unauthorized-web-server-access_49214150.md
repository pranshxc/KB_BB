---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-08_a-simple-post-auth-bypass-leads-to-unauthorized-web-server-access.md
original_filename: 2019-11-08_a-simple-post-auth-bypass-leads-to-unauthorized-web-server-access.md
title: A simple post auth bypass leads to unauthorized web server access
category: blogs
detected_topics:
- command-injection
- api-security
tags:
- imported
- blogs
- command-injection
- api-security
language: en
raw_sha256: 49214150089d1db95e2fa3a178658d7815d3124834ef9206caafe066ddf1e505
text_sha256: b8c269dad95430e08c0c35842daccf8a5b2d8061761fcb876476c91a3851d81b
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# A simple post auth bypass leads to unauthorized web server access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-08_a-simple-post-auth-bypass-leads-to-unauthorized-web-server-access.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `49214150089d1db95e2fa3a178658d7815d3124834ef9206caafe066ddf1e505`
- Text SHA256: `b8c269dad95430e08c0c35842daccf8a5b2d8061761fcb876476c91a3851d81b`


## Content

---
title: "A simple post auth bypass leads to unauthorized web server access"
url: "https://medium.com/@heinthantzin/a-simple-post-auth-bypass-leads-to-unauthorized-web-server-access-483c053c110e"
authors: ["Hein Thant Zin (@H3Lowr)"]
bugs: ["Default credentials"]
bounty: "750"
publication_date: "2019-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4955
scraped_via: "browseros"
---

# A simple post auth bypass leads to unauthorized web server access

A simple post auth bypass leads to unauthorized web server access
Hein Thant Zin
Follow
3 min read
·
Nov 8, 2019

83

1

Hi all, I hope u are doing well. I’m Hein Thant Zin and juat a noob bug bounty hunter from Myanmar.This is my third write up about one of my recent findings on h1.

The story began after local CTF had finished.It was about Sept 1, I did want to go back bug bounty for 1 month . So I decided to hunt bug on AT&T with my fri.

After some days and some duplicate reports passed. The night has come.

It was look like custom developing subdomain there is nothing interesting , just a simple login page for internal user .I’ve tested for auth bypass bug but failed.

After some recons, He said “bro three is a pop-up login page saying “weblogic””.

Press enter or click to view image in full size
http://exapledevlopment.att.com/management/

I did’t even know what the hell is weblogic before.So I found out google and tried to login using default login credentical but failed. Then I got this link https://github.com/lanjelot/kb/blob/master/weblogic

After many attempts failed , I was able log in using one of these credenticals. Unfortunately , the response was look like

Press enter or click to view image in full size

Well , I couldn’t fingure out how the hell is that. I stucked for a while and did’t know how to do then it was about 2 am so I was going bed to sleep.

Get Hein Thant Zin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next day , I wake up at 1 pm and picked up my laptop and tesing again. Tried to bruteforce directory , changing http request methods but all failed.

Press enter or click to view image in full size

I had almost to give up but suddendely I remembered that why I should not give a try “weblogic” as a directory name.It does make sense right?

I put the name as directory and Boom!!! I was completely accessed in their weblogic server. I was able to view all server informations and their internal development app and other sensitive informations.

Press enter or click to view image in full size

Then I reported to HackerOne. They triaged and rewarded after the report resolved . I hope you enjoyed by reading this . Follow me for more write up there.

http://twitter.com/H3Lowr

Timeline -:

Sept , 14, 2019 -Reported

Sept, 15, 2019 -Triaged by h1 team

Oct , 22 , 2019 -Fixed and Bounty awarded $750.

See ya guys. I’ll be back with the next finding soon…… Thank u.

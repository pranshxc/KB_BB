---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-27_bragging-rightspart-1-short-story-of-a-bug-wave.md
original_filename: 2021-01-27_bragging-rightspart-1-short-story-of-a-bug-wave.md
title: 'Bragging Rights(Part 1): Short story of a bug wave'
category: documents
detected_topics:
- idor
- xss
- mobile-security
- ssrf
- command-injection
- rate-limit
tags:
- imported
- documents
- idor
- xss
- mobile-security
- ssrf
- command-injection
- rate-limit
language: en
raw_sha256: 8bc4050eb23f9843f6162dcc2ce20a9264cb2b147b0838791d40aa7c8054eec9
text_sha256: d404dba2dcaced00ae76dd6f1b1877f13a579a743439fa7554f2d3bcee981cf8
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Bragging Rights(Part 1): Short story of a bug wave

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-27_bragging-rightspart-1-short-story-of-a-bug-wave.md
- Source Type: markdown
- Detected Topics: idor, xss, mobile-security, ssrf, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `8bc4050eb23f9843f6162dcc2ce20a9264cb2b147b0838791d40aa7c8054eec9`
- Text SHA256: `d404dba2dcaced00ae76dd6f1b1877f13a579a743439fa7554f2d3bcee981cf8`


## Content

---
title: "Bragging Rights(Part 1): Short story of a bug wave"
url: "https://medium.com/bugbountywriteup/bragging-rights-part-1-short-story-of-a-bug-wave-dbb88f48b604"
authors: ["Manas Harsh (@ManasH4rsh)"]
bugs: ["IDOR", "Stored XSS", "SSRF", "Subdomain takeover", "Hardcoded credentials"]
bounty: "1,550"
publication_date: "2021-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3962
scraped_via: "browseros"
---

# Bragging Rights(Part 1): Short story of a bug wave

Bragging Rights(Part 1): Short story of a bug wave
Manas Harsh
Follow
5 min read
·
Jan 27, 2021

271

3

Press enter or click to view image in full size

Hi my fellow hacker buddies, I hope you all are doing well. We have entered in a new year(finally) and probably we all have set some goals for this year. I pray those come true for you. I am starting a series of articles and blogs where I will be posting my findings & some interesting reads. I am calling it Bragging Rights! I hope you enjoy and learn from it.

Well, the first part is based on my recent bug hunts where I found 6 bugs on a single target. I will try to explain the bugs and let me be clear my motive is not to tell you for eg. what is an IDOR. You probably already know that, the bug types. This blog is about where are the places you can look for them in wild and that’s why we love write-ups and articles don’t we? So let’s move ahead:)

Alright, so let’s call the target “target.com”(due to their policies and NDA). I chose a target from some google dorks (i.e “responsible disclosure reward”) and started scrapping the data whatever I could recon for that target. I chose weekends so that I could get more time to hunt on it. After 2 weekends and almost 30 hours of work, I found this:

2 IDORs

1 Stored XSS

1 Azure subdomain takeover

1 SSRF

and hardcoded credentials for a third party in their android app

Honourable mention: “wp-json/wp/v2/users” xD

Let’s start with the 1st one and my favorite. IDORs. Before we start, I had got some usernames with the WordPress username enumeration and sometimes it will help you to chain cool bugs. So the application had a single user role. You can only create multiple users with low privileges. If you’re thinking it was a simple 2004 ->2005 IDOR, it wasn’t. Let me tell you, once you login to the application, there was a functionality where you can generate and download your report cards which will contain your PII. So, once you click on generate report card, a POST request with JSON will look like this:

{request ID: “username_base64 value”}

Did you get it? Yes, you did! If not, simply decode the base64 value and change it to another ID. Encode it again and we get our 1st IDOR once you download someone else’s report card :) Takeaway? Make sure to check the base64/hashed values:)

2nd IDOR was quite simple. I could change the password by swapping the user IDs. Like we do in normal scenarios. But since there were authentications on the website I couldn’t take them over. Anyways, I changed the passwords. Again it was base64 decoded and did the same thing. The only difference was it was serialized where the report cards were based on the users who had one.

3rd bug was stored XSS. We had a kind of discussion box where we can put our suggestions about medical hospitals and services. It was a cool bypass and I have learned it recently. I would suggest you all learn the XSS bypass techniques i.e some Javascript instead of throwing a ton of payloads here and there. So the website was filtering the special characters and script tag along with prompt. I played with it for a while and then crafted this payload:

‘’;! — “<xsshere>=&{()}

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I took references from Intigriti’s XSS challenges and I must say those are awesome. You can find a good article here:- Challange. There are a few more of them. Just google it, buddy :)

4th on the list was an azure subdomain takeover and I had done it for my company earlier with the help of a colleague. That helped me here. I did some recon with subfinder and found a bunch of subdomains. Going forward, I used Nuclei for low hangings and ended up with this subdomain which was hosted on Azure cloud services. Want a good blog on it? Here we go- Takeover. So, I checked the CNAME and it was vulnerable so went ahead and owned it on azure services. That was cool.. and easy :P

5th was the most time taking and most rewarded bug in this list. Yes, an SSRF! My first SSRF came from this target. The website had an option where you can add your website link and yeah I was thinking the same way you are doing right now. Can we put our own domain and try there or can we blast an internal SSRF? So this worked and I got an HTTP pingback with the help of a collaborator everywhere extension. What ate my time was, it was not accepting the simple SSRF payloads like http://localhost, http://127.1 etc. I tried it for almost a whole day and just when I was about to give up, I remembered we can actually make a combination of IP addresses and try if it works, and boom!!!! It worked. The payload will go like this:

http://1.1.1.1 &@2.2.2.2#@3.3.3.3/

I don’t understand how this works and If anyone knows please DM on Twitter with a solution. I went ahead and did a port scan, took ss, and sent it.

This was my research for the web part. They had an android app as well and I thought to give it a go if I can find anything. So the final and 6th bug was hardcoded credentials under the web app. I downloaded the APK and decompiled it with apktool. Since we first go to strings.xml, I did the same and there was nothing. While searching here & there I found a folder under assets and oh boy! There were some app_key and secert_key. I had literally no idea what to do and I simply reported it.

So these were the bugs I found there. Luckily I got a good bounty. It was:

2 IDORs: 300+300= 600$

1 Azure takeover = 150$

XSS: 300$

SSRF: 450$

and hardcoded creds: 50$

{Total 1550$)

The main thing is, how far you can go with your thinking power and hacking is all about the unique ways to exploit stuff. The more curious you are, the better results you will get. Sticking with a program has really helped me to improve myself in a better way and I am sure it will do the same to you. Also, I bet you can get good bugs once you spend some time on a target. However, it completely depends on what suits your mentality:)

So this will be it for this write-up. It's been a while I didn’t post any of them so I typed it today. I hope it helps you in some way. Don’t get demotivated if you don’t find bugs. I didn’t get a single bug for 3 months. It didn’t do anything to me. However, I wish you find bugs on regular basis :p

If you liked it and learned something, you can hit the clap icon down below. You can also follow me on Twitter with this username: @manash4rsh.

Take care hackers! Happy hunting :)

Adios ❤

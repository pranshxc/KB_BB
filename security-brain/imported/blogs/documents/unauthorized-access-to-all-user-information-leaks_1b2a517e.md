---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-13_unauthorized-access-to-all-user-information-leaks.md
original_filename: 2019-09-13_unauthorized-access-to-all-user-information-leaks.md
title: Unauthorized access to all user information leaks
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: 1b2a517e6ae78d3924b674d00da2b4edff9ebda9311181cc512b8e5f881f80ad
text_sha256: f5e4bfdd65eaa09efbae28a499d73fcd867a97078e88046bcec41d794ce03b66
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized access to all user information leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-13_unauthorized-access-to-all-user-information-leaks.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1b2a517e6ae78d3924b674d00da2b4edff9ebda9311181cc512b8e5f881f80ad`
- Text SHA256: `f5e4bfdd65eaa09efbae28a499d73fcd867a97078e88046bcec41d794ce03b66`


## Content

---
title: "Unauthorized access to all user information leaks"
url: "https://medium.com/@cc1h2e1/unauthorized-access-to-all-user-information-leaks-5db95746aecf"
authors: ["C1h2e1 (@C1h2e11)"]
bugs: ["Information disclosure"]
publication_date: "2019-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5031
scraped_via: "browseros"
---

# Unauthorized access to all user information leaks

Top highlight

Unauthorized access to all user information leaks
C1h2e1
Follow
4 min read
·
Sep 13, 2019

178

2

Now is the Mid-Autumn Festival in China. I returned to school from school. Today is the first day of the three-day holiday. I got up late on this day because I was so stressed that between school and work.I recorded only two interesting bugs, others did not write, LET’S GO

Press enter or click to view image in full size
Workflow
Recon

I used my shell script at the beginning to do Recon. Even though this script is not well written, I still like to use it.

Press enter or click to view image in full size
Recon.sh

Thank you very much for sharing and gave me a lot of help.@
TomNomNom
 @
Behrouz Sadeghipour

This site has five subdomains, the port is only 80 an

d 443, I checked censys.io and so on and only got very little information. At this time I find out the Logic flaw and successfully got a account takeover (I didn’t have Submit it because there is no interesting idea)

I checked 2 subdomains

api.redacted.com
console.redacted.com

As you can see from the name, one is the api site and the other is the management site.Both sites open are 404 NOT FOUND,I used WFUZZ for directory brute forcing

started on api.redacted.com
Press enter or click to view image in full size

I am very happy to see this result.After the visit, I discovered the monitoring system (JavaMelody)This is the first time I have met this, so I am looking around for ways to make further exploit.

Get C1h2e1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found this thing and leaked some endpoints.But there is no sensitive information,In addition to system information, etc.

Press enter or click to view image in full size

Then I found this

Press enter or click to view image in full size

Yes, it leaks sensitive information such as accesskey, which allows me to log in to the account, but it is only a -time access record.If I want more, I need to find other points again.I just wondered if this site exists or is there another console.redacted.com?

Advanced on console.redacted.com

I visited console.redacted.com/monitoring Found the same result,I also started searching around again.At first I found an endpoint to calculate the user’s transaction amount….But when I requested
After that, I was redirected to the administrator login page.So I started searching again. Then I Found this page console.redacted.com/monitoring?part=sessions…

Press enter or click to view image in full size

Boom I guess the administrator’s session ID, so I wrote this seesion into my cookie.And requested the above endpoint,This is my successful acquisition of sensitive information from the user.But the new problem has once again appeared, and the endpoint record in the access record disappears.I thought for a moment and took a cup of coffee. When I came back, my mother told me that it was already 12 o’clock and let me go to bed early.

What? 12 o’clock?I re-read the error and other information was refreshed, then I found the time filter at the top.I understand that this point only records the access log of the day, so I set the time to ALL, I found more information, more seesion, more errors, more endpoints. . . .

Press enter or click to view image in full size
Press enter or click to view image in full size

Yep, I successfully got a critical vulnerability！！！

My twitter @C1h2e11

./Logout

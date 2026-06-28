---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-05_if-its-a-feature-lets-abuse-it-for-750.md
original_filename: 2022-06-05_if-its-a-feature-lets-abuse-it-for-750.md
title: If It’s a Feature!!! Let’s Abuse It for $750
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: bfab6ddc1f075edddb1aa9be6dd3f3987b9125c414626497541d2d4b96c69896
text_sha256: 92066516ecb86c7163ca983851d7389c53843613e755b54d3b9193fc0442fb2b
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# If It’s a Feature!!! Let’s Abuse It for $750

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-05_if-its-a-feature-lets-abuse-it-for-750.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `bfab6ddc1f075edddb1aa9be6dd3f3987b9125c414626497541d2d4b96c69896`
- Text SHA256: `92066516ecb86c7163ca983851d7389c53843613e755b54d3b9193fc0442fb2b`


## Content

---
title: "If It’s a Feature!!! Let’s Abuse It for $750"
url: "https://medium.com/@shakti.gtp/if-its-a-feature-let-s-abuse-it-for-750-19cfb9848d4b"
authors: ["Shakti Mohanty (@3ncryptSaan)"]
bugs: ["CSRF"]
bounty: "750"
publication_date: "2022-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2586
scraped_via: "browseros"
---

# If It’s a Feature!!! Let’s Abuse It for $750

If It’s a Feature!!! Let’s Abuse It for $750
shakti mohanty
Follow
4 min read
·
Jun 5, 2022

365

8

Hello mates,

Thank You so much for being here. Hope You all are doing well on your respective goals. I am Shakti Ranjan Mohanty (aka 3ncryptsaan). I am a part time security researcher on Hackerone. On this write-up, i will be sharing the details of a bug i have found recently related to CSRF.

Before starting , i would like to suggest the beginners that

“While reporting any kind of bug, first think like a program owner that why he will pay you something. What’s the impact here. Don’t rely too much on the low hanging fruits , this will lead you to temporary happiness with a permanent burnout.”

LET’s Start

Cause I Love Pet

On the start of the last month, i picked a private program to hack on. The app was all about managing meetings, events , invoices etc. After few reports of XSS and privilege escalation bugs. The program staff replied me to test for bugs which will be a threat to the organisational data.

So after some test i have found a CSRF on adding any google calendar to the application.While connecting the google calendar , the flow will work like below

Sample of how google gives access

After the Google authorise the web app with a token to access his service, The final request will look like

GET /app/google/auth_callback?code=4/0RAX4YfWgvjaHxzYX4FNLO-QvFVgDmMsSA0_IvL0FxAptS2mHJAXM-L4bMiZmKGhI6Mz-o3A&scope=https://www.googleapis.com/auth/calendar HTTP/1.1
Host: target.com
Cookie: cookie here

The above request has a code parameter containing auth value from google, this will add that respective google calendar with the target.com. Then target.com will sync and exchange data to that google calendar.

If you have noticed the Request is in GET method and there is no additional CSRF checks, That means , we can trick the victim to click on the GET url

https://target.com/app/google/auth_callback?code=4/0RAX4YfWgvjaHxzYX4FNLO-QvFVgDmMsSA0_IvL0FxAptS2mHJAXM-L4bMiZmKGhI6Mz-o3A&scope=https://www.googleapis.com/auth/

and the google calendar will be linked to the victim account( the victim need to open the link on the same browser where he is already logged in with target.com).

BUT… BUT… As you know “auth_callback?code=” will have a auth token value from google and you can only get your google auth token. That mean through the csrf , only your google account can be linked to the victim’s account in target.com.

What’s the impact Here????

As before my test i am always serious about knowing the application first, i have already aware about the google calendar. This will add the google account with the application and all the scheduled meetings , events , invoices etc will be synced to that respective google calendar. Then Through google calendar the organisational owner can able to view the scheduled data in a detailed manner.

Get shakti mohanty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The impact here will be when attacker’s google account will be connected to victim’s account on target.com, target.com will sync all meetings, events, invoice data to the google calendar along with the the date, invited users name , email( there is an option in G-calendar to copy the guest email), mobile number(if owner have added it on the guest details), attached file, location, meeting credentials and notes etc.

Press enter or click to view image in full size
This is a sample of one meeting added by victim synced to attacker’s google calendar

Attack Scenario:

1- Navigate to your account as an attacker

2- Navigate to https://target.com/profile/settings the Google calendar app will be disabled. Enable it, this will ask to connect with google account.

3- Connect with attacker’s google account and capture the final request containing google auth token.

GET /app/google/auth_callback?code=4/0RAX4YfWgvjaHxzYX4FNLO-QvFVgDmMsSA0_IvL0FxAptS2mHJAXM-L4bMiZmKGhI6Mz-o3A&scope=https://www.googleapis.com/auth/calendar HTTP/1.1
Host: target.com
Cookie: cookie here

As the request in GET method, you can directly share the link to any organisational owner ( also you can make a tiny url for the above link, this will be helpful for tricking the victim), This will connect the google account with that organisation’s account.

4- Now share the link to victim organisation employee, let him click and your google calendar will be added to his organisation.

5- Now all the scheduled data will be synced to your google calendar and you can see all the data synced to your google calendar.

Reported: May 11th, 2022

Triaged and Rewarded: May 27th, 2022

Press enter or click to view image in full size

Please share your feedbacks, This will help me to rectify the errors on the next writeup.

Stay Tuned. I will be posting another interesting writeup within few days.

Follow me for more write-ups and information sharing, I will be happy to share my knowledge and my DMs are always open for the genuine help seekers.

Instagram: https://www.instagram.com/3ncryptsaan/

Twitter: https://twitter.com/3ncryptSaan

Linkedin: https://www.linkedin.com/in/shakti-ranjan-mohanty/

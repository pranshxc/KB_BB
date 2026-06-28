---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-13_account-takeover-on-airbnb-acquisition-an-unusual-bug-part-2-.md
original_filename: 2019-07-13_account-takeover-on-airbnb-acquisition-an-unusual-bug-part-2-.md
title: Account takeover on Airbnb acquisition | An Unusual Bug Part-2 🐛
category: documents
detected_topics:
- oauth
- sso
- idor
- xss
- command-injection
- api-security
tags:
- imported
- documents
- oauth
- sso
- idor
- xss
- command-injection
- api-security
language: en
raw_sha256: 79c9ffb137121840961aea10649d8b8b9d53abdfead55856cf356a00b3a2c645
text_sha256: 3e6fcd8a5d5114b48a5c9f4fb49bbc6543fb4f60ca115df476ef5cc7c4129646
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover on Airbnb acquisition | An Unusual Bug Part-2 🐛

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-13_account-takeover-on-airbnb-acquisition-an-unusual-bug-part-2-.md
- Source Type: markdown
- Detected Topics: oauth, sso, idor, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `79c9ffb137121840961aea10649d8b8b9d53abdfead55856cf356a00b3a2c645`
- Text SHA256: `3e6fcd8a5d5114b48a5c9f4fb49bbc6543fb4f60ca115df476ef5cc7c4129646`


## Content

---
title: "Account takeover on Airbnb acquisition | An Unusual Bug Part-2 🐛"
url: "https://medium.com/@princechaddha/account-takeover-on-airbnb-acquisition-an-unusual-bug-part-2-45fab11dc407"
authors: ["PRince CHaddha (@princechaddha)"]
programs: ["Airbnb"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2019-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5154
scraped_via: "browseros"
---

# Account takeover on Airbnb acquisition | An Unusual Bug Part-2 🐛

Account takeover on Airbnb acquisition | An Unusual Bug Part-2 🐛
PRince CHaddha
Follow
3 min read
·
Jul 13, 2019

502

1

Hello, Everyone this is my second blogpost about one of my finding on Airbnb acquisition during HackTheWorld and I was awarded with special swagpack from Airbnb for submitting high impact and well written report https://www.hackerone.com/blog/Hacking-Planet-Hack-World-2017-Recap.

This should be a part-2 of unusual bug series because I haven’t encountered something like this before.You can read about my previous bug here : https://medium.com/@princechaddha/an-unusal-bug-on-braintree-paypal-b8d3ec662414.

During HackTheWorld I was looking for a target to hack and that time Airbnb was Offering nice rewards so after looking at their scope I found a domain luxuryretreats.com.

Upon visiting luxuryretreats.com I noticed there were two options Signup via Email and Signup Via Facebook. I signed up via Facebook ezz right ? After testing the application I found an interesting Misconfigured OAuth to Account Takeover but thats the story for another blogpost.

Now it was the time to hunt for some IDOR’s so i signed up for another account but this time using Sign Up by Email.I used the same email as of my Facebook Account and then I was logged into my Luxury Retreats account that I previously created using Signup Via Facebook without any verification. I was like ok lets try again 🙃

Get PRince CHaddha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I created another account using Signup Via Facebook and Signed Up via Email using the same email associated with my Facebook account and Yes Account Takeover I was again logged into my previous account.Now I can just use that email and the password I entered during Signup via Email to log into that account.

Impact :

So if the user signed up via Facebook then attacker just need his email ID to log into his and set his password.

Takeaway :

Every application and their developers are different and they do make silly misktakes so don’t just test for IDORs, XSS and other usual bugs.Play around the application for a little longer and the bugs will find you.

In the above case we can also try Signing up via Facebook and then try logging into the application using the email and password as [blank], 123456, 0, 1, 000000, undefined, etc if the oauth password is hardcoded or using the case below

CASE 1 : If the application is creating the entry without any password when we signed up via Facebook

Press enter or click to view image in full size

CASE 2 : If the application is sending FALSE when user is signed up via Facebook then entering 0 as password can let you login into the account.

Press enter or click to view image in full size

I hope you liked this. Feedbacks are always welcome, reach me out on twitter @princechaddha .Thanks to 
Harsh Jaiswal

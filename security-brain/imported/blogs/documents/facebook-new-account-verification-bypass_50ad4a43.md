---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-13_facebook-new-account-verification-bypass.md
original_filename: 2019-12-13_facebook-new-account-verification-bypass.md
title: Facebook New Account Verification Bypass
category: documents
detected_topics:
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- api-security
language: en
raw_sha256: 50ad4a4359343e14675256222b782edce053dbdf9993faf4c671586ee4092932
text_sha256: 102a0b40221aa468acf2dff813d7fef4b0939fae09901e8d4f5b30908c472523
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook New Account Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-13_facebook-new-account-verification-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `50ad4a4359343e14675256222b782edce053dbdf9993faf4c671586ee4092932`
- Text SHA256: `102a0b40221aa468acf2dff813d7fef4b0939fae09901e8d4f5b30908c472523`


## Content

---
title: "Facebook New Account Verification Bypass"
url: "https://medium.com/@santoshbrl5/facebook-new-account-verification-bypass-c589017f2faf"
authors: ["Santosh Baral (@santoshbrl5)"]
programs: ["Meta / Facebook"]
bugs: ["Authentication bypass"]
publication_date: "2019-12-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4891
scraped_via: "browseros"
---

# Facebook New Account Verification Bypass

Facebook New Account Verification Bypass
Santosh Baral
Follow
3 min read
·
Dec 13, 2019

35

On September 22, 2019, at 11:30 pm, I was preparing for my board exam and I feel tired reading all those stuff. Then I think to open Facebook and see some news-feed but I don’t know what comes in my mind that I opened a new private tab in my Firefox and tried to create a new account. Firstly I filled the new account form with all correct and valid details and all of a sudden I thought what if I give wrong email address can I verify it somehow and I fill the form with the wrong email and clicked for sign up. Then I was redirected to a new page/verification page. I thought I can’t do anything without verification but I saw an option to see our profile I thought it won’t work if I click that option, also it will redirect me to verification page again but I was surprised when I tried that I was able to visit my profile and do anything I want like change profile pictures, posting status and other things. But the thing was there was no more option than that like no option for search and others.

Press enter or click to view image in full size

Then I thought what if I change the URL and try to visit someone profile and I change the URL to my original account profile and boom I was able to visit my profile and I was able to see an option for search and all other options what we see in a verified account.

Press enter or click to view image in full size

I was more shocked when I got to know that I can send a friend request, comment, share and like any public or friends post. Then I sent a friend request to my original id and I accept that friend request to see what more can I do. After accepting the friend request I was also able to send messages to my real account.

Press enter or click to view image in full size

It took me around 15 minutes to find all those stuff. I immediately report it to Facebook at around 11:50–12:00. After waiting for 3 days they finally reply to me I was happy with that notification but all of a sudden all my happiness was stolen from me I got a reply that Facebook team know about it internally and are working to improve the verification flow.

Though I didn’t receive any bounty I thought it will be good if I share my finding to you all. Thanks for reading all till last. This is my first write-up on such topic so there may be some mistakes so I am sorry for those silly mistakes.

Get Santosh Baral’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

========================================

PoC Video Link:- https://youtu.be/UDetCErBD9E

========================================

Find Me On:-
Facebook:- https://facebook.com/santoshbrl5
Instagram:- https://instagram.com/santoshbrl5
Twitter:- https://twitter.com/santoshbrl5

========================================

My Site:-

https://santoshbrl.com.np

If you ever visit Pokhara Nepal do Visit my Restaurant for dinner

Vrikshya Cafe Restaurant and Bar — Best Dinner in Pokhara

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-26_how-re-signing-up-for-an-account-lead-to-account-takeover.md
original_filename: 2018-06-26_how-re-signing-up-for-an-account-lead-to-account-takeover.md
title: How re-signing up for an account lead to account takeover
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 572a45d58b64b57b28ddb3918d4efdeb9ffb39861da5b7e1d78cb46fefb85b47
text_sha256: c2b0eb23244793f897aeaef03e71671d08edbe4dcef29f022878b40f62b048a7
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How re-signing up for an account lead to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-26_how-re-signing-up-for-an-account-lead-to-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `572a45d58b64b57b28ddb3918d4efdeb9ffb39861da5b7e1d78cb46fefb85b47`
- Text SHA256: `c2b0eb23244793f897aeaef03e71671d08edbe4dcef29f022878b40f62b048a7`


## Content

---
title: "How re-signing up for an account lead to account takeover"
url: "https://zseano.medium.com/how-re-signing-up-for-an-account-lead-to-account-takeover-3a63a628fd9f"
authors: ["Zseano (@zseano)"]
bugs: ["Logic flaw", "Account takeover"]
publication_date: "2018-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5825
scraped_via: "browseros"
---

# How re-signing up for an account lead to account takeover

Top highlight

How re-signing up for an account lead to account takeover
Sean (zseano)
Follow
3 min read
·
Jun 26, 2018

815

5

This is a quick write-up about an interesting bug I found on a bounty program which lead to unauthorised access to any account you knew the email of (no password needed!). I believe some other researchers may of overlooked the functionality of the site and some of the requests that were made.

Tip: when testing a site you will be surprised at how many act different depending on user agent,device,language, session (logged in/out). When testing you should test from as many different angles as possible to check if anything is different / discover new endpoints. Some responses will display different links, ads, sections of the site, etc.

It’s all in the detail

With the tip above in mind, I decided to signup for an account on this site and went through all the steps to verify it. After signing up I will always simply re-visit the signup page because sometimes if it renders, entering another users email / changing some details can lead to unexpected results (another post another time :D).

In this case upon re-visiting the signup page it only wanted my email, so upon submitting the form I was sent an email saying I already had an account with them, and an option to reset my password if I had forgot it. Upon clicking the link it redirected me to the homepage with the following:

Press enter or click to view image in full size

Weird. The button said “Reset password”, yet I was automatically logged into my account and it just redirected me to my profile. I went back to check what requests were made and this one stood out:

My first thought is: what happens if I re-visit this link? Sadly, it gave me a 404 error (tried on old session, still 404, figured token expired etc), however after submitting the form above again I visited the link again, except this time I tried it on a brand new session. The result: logged into my account without entering my password!

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So now i’m starting to think, is that value just the users id? We need to submit that form for the link to work, but if it IS my userid, how do we find another users id? I checked profiles, image urls, everything. I couldn’t find anything. Not wanting to give up, I decided to retrace my steps and to try find out where this parameter may be set (was it set in just the email, or anywhere else?). I quickly realised I should of paid more attention to what was infront of me as I decided to hunt in the response and there it was:

And there is the last piece to the puzzle. Our repo steps look like this:

Submit users’ email you wish to takeover.
Grab id in response
Visit the /api/create url and…. we’re in!

It is extremely easy to overlook such basic things, especially with so many different types of bugs to look for. Just take your time, understand your target, and understand what you’re trying to achieve. Stick to one thing at a time.

Until next time.. ;)

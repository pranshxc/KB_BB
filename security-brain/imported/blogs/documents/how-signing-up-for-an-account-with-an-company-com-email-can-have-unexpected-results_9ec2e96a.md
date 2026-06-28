---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-15_how-signing-up-for-an-account-with-an-companycom-email-can-have-unexpected-resul.md
original_filename: 2017-11-15_how-signing-up-for-an-account-with-an-companycom-email-can-have-unexpected-resul.md
title: How signing up for an account with an @company.com email can have unexpected
  results
category: documents
detected_topics:
- command-injection
- mfa
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- business-logic
- api-security
language: en
raw_sha256: 9ec2e96a058ccf1c39efcf67f07ab0dcd0078c8dd402b31665cf202d35bf901e
text_sha256: 527e5e6e0dead6f2781dbc7d6de3240b07cbde81eb86fb2f4962d26f26955711
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How signing up for an account with an @company.com email can have unexpected results

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-15_how-signing-up-for-an-account-with-an-companycom-email-can-have-unexpected-resul.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, business-logic, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9ec2e96a058ccf1c39efcf67f07ab0dcd0078c8dd402b31665cf202d35bf901e`
- Text SHA256: `527e5e6e0dead6f2781dbc7d6de3240b07cbde81eb86fb2f4962d26f26955711`


## Content

---
title: "How signing up for an account with an @company.com email can have unexpected results"
url: "https://zseano.medium.com/how-signing-up-for-an-account-with-an-company-com-email-can-have-unexpected-results-7f1b700976f5"
authors: ["Zseano (@zseano)"]
bugs: ["Logic flaw"]
publication_date: "2017-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6053
scraped_via: "browseros"
---

# How signing up for an account with an @company.com email can have unexpected results

How signing up for an account with an @company.com email can have unexpected results
Sean (zseano)
Follow
3 min read
·
Nov 15, 2017

776

3

Something so simple can have unexpected results. It was a late evening and I was fed up of looking at Burp so I decided to just try some things manually on random programs. The result? I ended up with a P1 :)

The site was pretty simple as it was similar to an appstore and users could sign up and claim they were apart of the organisation or create new their own. When setting up a new organisation you were required to enter a valid phone number and whoever created it first was the root owner. When a new user attempted to join an organisation, a unique code was sent to the organisation’s phone number which is then used as the 2FA code. So ultimately the root owner had the final say on who can join. Pretty straight forward, right?

Press enter or click to view image in full size
I really didn’t fancy social enigneering a phone company to take over that mobile number. tip: don’t rely on 2fa via sms

As every researcher will know, sometimes you think of random things to try. I don’t know why but I just randomly thought, “This site doesn’t require us to verify our account/email, so what would happen if our account email is *@organisation.com?”. 2 minutes later, armed with a sean@organisation.com account, I clicked “Claim”. This time I was presented with a different screen:

Press enter or click to view image in full size

Interesting, this is new! So according to this, all I need to do is press “submit”, check my email and then verify I own that email (presuming by clicking a link). The problem is, I don’t own this email, therefore I can’t click the special link. Hmm.

I sat and stared at the screen and suddenly thought, “I wonder what will happen if we change our account email to one we control BEFORE pressing the submit button?” — So I did just that. With the email changed in my account settings, and the “Submit” button sitting there waiting to be pressed, I went for it.

It worked! Soon my phone lights up and i’ve received an email: “Please verify your identity and confirm your membership of zseano test by clicking the following link”. Things however weren’t working as planned just yet. I clicked the link to verify my ownership but i’m presented with an error: “Sorry, this email cannot signup with this organisation!”.

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then it hits me: I need to change my email BACK to sean@organisation.com before clicking the link.

Press enter or click to view image in full size

We’re in! :) Now I can automate this process and join any organisation I wish.
(Sadly no screenshot on what you can do when you’re in, too much private information to hide that there won’t be much else to see..)

tdlr:

Signup using *@organisation.com email
Click “Claim” on organisation.
Change email to one we control & press submit.
Change email back to *@organisation.com and click link.
We’re in! :)

A similar method was found by @securinti which enabled him to access internal communications on some companies via their helpdesk.

When was the last time you signed up with an @company.com email and started poking? :)

(note: I made these screenshots to hide the identity of the program.)

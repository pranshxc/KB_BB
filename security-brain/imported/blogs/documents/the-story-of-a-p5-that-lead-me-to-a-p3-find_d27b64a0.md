---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_the-story-of-a-p5-that-lead-me-to-a-p3-find.md
original_filename: 2022-10-13_the-story-of-a-p5-that-lead-me-to-a-p3-find.md
title: The story of a [P5] that lead me to a [P3] find
category: documents
detected_topics:
- command-injection
- password-reset
- mfa
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- mfa
- api-security
language: en
raw_sha256: d27b64a0cc7051817b34546411b5b05cfb96b6ccf07535ad5e0f9e2cf1dc3264
text_sha256: 0532bfee215af02d93b91a02310aa3640ee1e7b22ef6b11b6e573f7a1665e3d3
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# The story of a [P5] that lead me to a [P3] find

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_the-story-of-a-p5-that-lead-me-to-a-p3-find.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, mfa, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `d27b64a0cc7051817b34546411b5b05cfb96b6ccf07535ad5e0f9e2cf1dc3264`
- Text SHA256: `0532bfee215af02d93b91a02310aa3640ee1e7b22ef6b11b6e573f7a1665e3d3`


## Content

---
title: "The story of a [P5] that lead me to a [P3] find"
url: "https://medium.com/@nireshpandian19/the-story-of-a-p5-that-lead-me-to-a-p3-find-3f8a5ea2c6e1"
authors: ["JAI NIRESH J"]
bugs: ["Pre-account takeover"]
publication_date: "2022-10-13"
added_date: "2022-11-03"
source: "pentester.land/writeups.json"
original_index: 2053
scraped_via: "browseros"
---

# The story of a [P5] that lead me to a [P3] find

The story of a [P5] that lead me to a [P3] find
JAI NIRESH J
Follow
4 min read
·
Oct 13, 2022

122

Helloo,

To all my fellow hackers and bug hunters. This is my third writeup and i assure you this will be a lot intersting one. You can ready my previous two reports from my profile or here :

MY FIRST AND SECOND BUGS ARE — 2FA BYPASS
Hey there guys,

medium.com

HOW A SLOW INTERNET, GOT ME 50$
Hellooo there to all my fellow hackers and readers, as promised i’m back with another writeup, and this would be too…

medium.com

LET’S get down to business !

As usual i was hunting on my favourite domain “bluedacted.com”, and it all started with a button called “ADD USER”.

This feature allows us to add other users, to our work with three privileges (Administrator, User, Single Server Access).

FIRST, LET ME EXPLAIN THE FEATURE :

On clicking the Add user button, we can enter an email .i.e., the email of the user whom we wish to allow access on our work or project.

Then we have the privileges option, where we can assign each user a privilege as mentioned above.

If the email entered by you is valid and if there is an user connected using the provided email in the application, he will be listed and will be given the privilege. Else not, an invite to open an account on the application will be sent to the email.

THE P5 FIND :

When i tested the feature, it was clearly malfunctioning. If i enter an email which is already registered on the platform, it through me an error

“Enter a valid email”

And when i enter a non existing email in the application, it gets added with the privilege. When i check the inbox for the corresponding email, it had an invite to open an account on the application.

Basically, it the actions are reversed and malfunctioning, and yea it was a bug, but i was not too happy about it ! as it did not have any security impact.

I reported the bug and soon i got a response that goes like :

Hello,

Thank you for reporting this bug. It has been fixed. This has no security impact, so we are not paying any bounty on this.

Regards

Okay now what !

Get JAI NIRESH J’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I left for college the next day, and when i was travelling back to my home later that evening, something told me to check the feature again.
When i came back to my home, I fired up my laptop, rushed to the website, went to the ACCOUNTS tab -> USERS TAB -> and tested the feature.

They fixed it.

AWAITING PART OF THE STORY [the P3 find] :

This was an interesting find. I entered an email in the ADD USER featured column.

The email was listed (unverified).

And as usual an invite to the email was sent to my inbox, and i clicked that and i verified my account, and now the “Unverified” flag disappeared.

Now, when i click the newly created user account, i get a form where we can edit the email and password of the account.

Press enter or click to view image in full size

Here, i changed the email to another email and gave my usual password on the password field, and GUESS WHAT ?

BOOM ! My email changed to the new email and i did not get the “Unverified flag”.

No unverified flag

I told to myself, not to keep my hopes too high, and i went on to the LOGIN page, and i used the credentials

Email : The new email (victim’s email) that i changed to.

Password=***REDACTED*** password i just typed in.

WOW ! i was logged into the account ! No registration, No email verification and No password setting !

TIME TO BE HAPPY NOW !

Basically, the ADD USER feature allowed me to verify an email known to me, and when i change the email to another victim’s one, the victim’s one too is marked as verified.

Thanks to the password field in the update form, i could change the email as well as set the password to the new email.

Therefore i created the credentials of a victim’s account and i did a PRE-ACCOUNT TAKEOVER.

SOON i reported it with a proper video POC and IMPACT, and i was rewarded.

IF U HAD MADE THIS FAR, I hope u liked the writeup ! More to come up in the coming months ! THANK YOU !

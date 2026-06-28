---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-11_got-easiest-bounty-with-html-injection-via-email-confirmation.md
original_filename: 2020-03-11_got-easiest-bounty-with-html-injection-via-email-confirmation.md
title: Got Easiest Bounty with HTML injection via email confirmation!
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: ad95a2e1210634105e3906bf722267ef75c1f54cb96101ef3e2ce48ab79f25c1
text_sha256: 0c654ebf2b2cc1ed69547312b632488b66bc68e7bb0452e2911aa96081bcf141
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Got Easiest Bounty with HTML injection via email confirmation!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-11_got-easiest-bounty-with-html-injection-via-email-confirmation.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `ad95a2e1210634105e3906bf722267ef75c1f54cb96101ef3e2ce48ab79f25c1`
- Text SHA256: `0c654ebf2b2cc1ed69547312b632488b66bc68e7bb0452e2911aa96081bcf141`


## Content

---
title: "Got Easiest Bounty with HTML injection via email confirmation!"
url: "https://medium.com/cyberverse/got-easiest-bounty-with-html-injection-via-email-confirmation-b1b10575a105"
authors: ["Shaurya Sharma (@ShauryaSharma05)"]
bugs: ["HTML injection"]
publication_date: "2020-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4724
scraped_via: "browseros"
---

# Got Easiest Bounty with HTML injection via email confirmation!

Got Easiest Bounty with HTML injection via email confirmation!
Shaurya Sharma
Follow
2 min read
·
Mar 12, 2020

330

Press enter or click to view image in full size

HTML injection is an attack very similar to Cross-site Scripting (XSS), whereas in XSS the attacker can inject and execute Javascript code, in HTML injection attack it allows only the injection of certain HTML tags.

LET’S GO HUNTERS!!
I register on the site, with the name “Shaurya” surname “Sharma” email {xxxx@mail.com} Temp-Mail (Disposable Email)
After registration, comes a message asking the user to validate their account through an email confirmation.

“-Please Shaurya Sharma, validate your account through a link sent to xxxxx@mail [.] Com”

HTML Code -:

<h1> Email confirmation </h1>

<p> Hello Shaurya Sharma, here is the link to confirm your email.

http://xxxxxx.org.in/Login/id=8829234?q

Get Shaurya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

</p>

We noticed that the site recorded the user’s name as HTML in the database, and now when requesting confirmation, the HTML injected by the user is able to break the original email sent by the system.

Testing HTML injection:
I created a new account, named ` ”> <img src = (Link/Location) `and surname test, then the site returns the answer:-

“Please“> <img src =” https://i.redd.it/l1yy7vaasqv31.jpg “> test, validate your account using a link sent to xxxxxx@mail [.] Com ”

OUTPUT >

Hello,

Press enter or click to view image in full size

, here is the link to confirm your email http://xxxxxx.org.in/Login/id=8829234?q

DONE !! Now you can inject any malicious input/code in the “Name” field text box, ant the output is reflected in the confirmation email.

Impact Example-: In banking systems, it can be used to obtain information about the victim’s card or request some unusual payment.

KEEP HUNTING …

#CyberVerse #Togtherwehitharder #bugbounty #webapplication

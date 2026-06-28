---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-17_crashing-your-linkedin-app-with-a-connection-request.md
original_filename: 2021-06-17_crashing-your-linkedin-app-with-a-connection-request.md
title: Crashing your LinkedIn app with a connection request.
category: documents
detected_topics:
- command-injection
- business-logic
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- cloud-security
- mobile-security
language: en
raw_sha256: 2af4a3410b7327c440effa2f8e4dacacb696c1281303351d53b16c8fc6c0c832
text_sha256: 3e61f9a7656554af7ed5a62083c1188081027675b750b6ed46ebab4256dd2a92
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Crashing your LinkedIn app with a connection request.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-17_crashing-your-linkedin-app-with-a-connection-request.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `2af4a3410b7327c440effa2f8e4dacacb696c1281303351d53b16c8fc6c0c832`
- Text SHA256: `3e61f9a7656554af7ed5a62083c1188081027675b750b6ed46ebab4256dd2a92`


## Content

---
title: "Crashing your LinkedIn app with a connection request."
url: "https://infosecwriteups.com/crashing-your-linkedin-app-with-a-connection-request-257f9b484550"
authors: ["Renganathan (@IamRenganathan)"]
programs: ["LinkedIn"]
bugs: ["Application-level DoS"]
publication_date: "2021-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3567
scraped_via: "browseros"
---

# Crashing your LinkedIn app with a connection request.

Renganathan
 highlighted

Crashing your LinkedIn app with a connection request.
Renganathan
Follow
2 min read
·
Jun 17, 2021

172

Hi There,

Renganathan here.

This write-up is about an accidental bug that I found on LinkedIn.

So that was the early time when I joined LinkedIn and I didn’t know much about the working functionalities. I’ve used only Instagram in my life *_*

I was trying to send a connection request to a person and I noticed I can give a personalized note with the requests. I added a message with around 650 characters approximately.

But LinkedIn allows, only 300 characters. So As a noob, what I did was, I used inspect element to change the maxlength=300 value. And then I sent the request.

BOOM!

It didn’t work, what else did you expect :/

Then I thought of using Burp Suite to add more content, which is more than 300 characters in the POST request. Something like below

“message”:{“values”:[{“value”:”follow me on Instagram”}]}

And I clicked forward, and the connection request was sent successfully. Then I went to mynetwork/invitation-manager/sent/ to see the sent connection requests.

BOOM!

Get Renganathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This worked :)

POC

So, the characters I sent were more than 300 obviously and it was sent successfully.

So, Reporting this as a business logic error won’t be good. So I tried adding a very huge request to my test account with a kind of hundred thousand characters.

I opened it from my android phone and the app was crashed.

I was like “IS THIS A DOS? VULNERABILITY”

Press enter or click to view image in full size

TimeLine:

Oct 10, 2020- Reported

Oct 14, 2020- Triaged

Dec 20, 2020- Retested

Dec 22, 2020- Patched & Acknoweldgedment received

Press enter or click to view image in full size
Acknowledgment from LinkedIn

Thanks for reading :)
Stay Safe.

https://www.instagram.com/renganathanofficial/

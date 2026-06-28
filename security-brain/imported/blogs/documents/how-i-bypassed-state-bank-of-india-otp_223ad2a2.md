---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-bypassed-state-bank-of-india-otp.md
original_filename: 2017-02-20_how-i-bypassed-state-bank-of-india-otp.md
title: How I bypassed State Bank of India OTP.
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 223ad2a2142daa582aac9aac98d04b8214e12133db68410ddcd92a63fa13061b
text_sha256: dbccaec63a0bd713f67a5f98853087e38dfed1b7a5b61f6296422caa3b871d9d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed State Bank of India OTP.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-bypassed-state-bank-of-india-otp.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `223ad2a2142daa582aac9aac98d04b8214e12133db68410ddcd92a63fa13061b`
- Text SHA256: `dbccaec63a0bd713f67a5f98853087e38dfed1b7a5b61f6296422caa3b871d9d`


## Content

---
title: "How I bypassed State Bank of India OTP."
url: "https://hackernoon.com/how-i-bypassed-state-bank-of-india-otp-f145469a9f1d"
final_url: "https://hackernoon.com/how-i-bypassed-state-bank-of-india-otp-f145469a9f1d"
authors: ["Neeraj Sonaniya (@neeraj_sonaniya)"]
programs: ["State Bank of India"]
bugs: ["OTP bypass"]
publication_date: "2017-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6220
---

Discover Anything __

[![Hackernoon logo](https://hackernoon.imgix.net/hn-icon.png?auto=format%2Ccompress&w=128)Hackernoon](/)

Signup[Write](/new)

 ______

__ 41,909 reads

# How I bypassed State Bank of India OTP.

by

[**Neeraj Sonaniya**](/u/neerajedwards)

[![Neeraj Sonaniya](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=96) byNeeraj Sonaniya@neerajedwards](/u/neerajedwards)

Information Security Consultant

Subscribe

[February 20th, 2017](/archives/2017/02/20)

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

TLDR __

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

__![featured image - How I bypassed State Bank of India OTP.](https://hackernoon.imgix.net/fallback-feat.png?auto=format%2Ccompress&w=3840)

Your browser does not support the`audio` element.

__

Speed 1x

Voice

Dr. One ![Dr. One \(en-US\)](https://hackernoon.imgix.net/avatars/robot-b5.png)

![Neeraj Sonaniya](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=96)

byNeeraj Sonaniya@neerajedwards

[![Neeraj Sonaniya](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=96)byNeeraj Sonaniya@neerajedwards](/u/neerajedwards)

Information Security Consultant

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

![Neeraj Sonaniya](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=3840)

[![Neeraj Sonaniya](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=96)by Neeraj Sonaniya@neerajedwards](/u/neerajedwards)

Information Security Consultant

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

### About Author

[![Neeraj Sonaniya HackerNoon profile picture](https://hackernoon.imgix.net/avatars/robot-a2.png?auto=format%2Ccompress&w=3840)](/u/neerajedwards)

[**Neeraj Sonaniya** | @neerajedwards](/u/neerajedwards)

Subscribe

Information Security Consultant

[Read my stories](/u/neerajedwards)[Learn More](/about/neerajedwards)

#### Comments

![avatar](https://hackernoon.imgix.net/images/fallback-feat.png?auto=format%2Ccompress&w=3840)

#### TOPICS

[business](/c/business)

[#cybersecurity](/tagged/cybersecurity)[#security](/tagged/security)[#bug-bounty](/tagged/bug-bounty)[#demonetization](/tagged/demonetization)[#politics](/tagged/politics)

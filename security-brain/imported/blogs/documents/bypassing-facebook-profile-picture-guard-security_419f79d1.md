---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-09_bypassing-facebook-profile-picture-guard-security.md
original_filename: 2017-09-09_bypassing-facebook-profile-picture-guard-security.md
title: Bypassing Facebook Profile Picture Guard Security.
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 419f79d199e2456fa611b1eeab5d50b12d59910d93cb2eb81ef1715aa11bdddf
text_sha256: ce4a39299e3a3635745648b878749d1cd49b63936b98117e2cf838fef19bbaaa
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Facebook Profile Picture Guard Security.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-09_bypassing-facebook-profile-picture-guard-security.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `419f79d199e2456fa611b1eeab5d50b12d59910d93cb2eb81ef1715aa11bdddf`
- Text SHA256: `ce4a39299e3a3635745648b878749d1cd49b63936b98117e2cf838fef19bbaaa`


## Content

---
title: "Bypassing Facebook Profile Picture Guard Security."
url: "https://hackernoon.com/bypassing-facebook-profile-picture-guard-security-f0676550f089"
final_url: "https://hackernoon.com/bypassing-facebook-profile-picture-guard-security-f0676550f089"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2017-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6106
---

Discover Anything __

[![Hackernoon logo](https://hackernoon.imgix.net/hn-icon.png?auto=format%2Ccompress&w=128)Hackernoon](/)

Signup[Write](/new)

 ______

__ 26,324 reads

# Bypassing Facebook Profile Picture Guard Security.

by

[**Armaan Pathan**](/u/armaanpathan)

[![Armaan Pathan](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96) byArmaan Pathan@armaanpathan](/u/armaanpathan)

Subscribe

[September 9th, 2017](/archives/2017/09/09)

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

TLDR __

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

__![featured image - Bypassing Facebook Profile Picture Guard Security.](https://hackernoon.imgix.net/hn-images/1*wn4YtW_T3xJhxHuONpZQCQ.png?auto=format%2Ccompress&w=3840)

![Armaan Pathan](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)

by Armaan Pathan@armaanpathan

[![Armaan Pathan](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)byArmaan Pathan@armaanpathan](/u/armaanpathan)

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

![Armaan Pathan](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=3840)

[![Armaan Pathan](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)by Armaan Pathan@armaanpathan](/u/armaanpathan)

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

### About Author

[![Armaan Pathan HackerNoon profile picture](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=3840)](/u/armaanpathan)

[**Armaan Pathan** | @armaanpathan](/u/armaanpathan)

Subscribe

[Read my stories](/u/armaanpathan)[Learn More](/about/armaanpathan)

#### Comments

![avatar](https://hackernoon.imgix.net/images/fallback-feat.png?auto=format%2Ccompress&w=3840)

#### TOPICS

[Software Engineering](/c/engineering)

[#facebook](/tagged/facebook)[#bug-bounty](/tagged/bug-bounty)[#hacking](/tagged/hacking)[#owasp](/tagged/owasp)

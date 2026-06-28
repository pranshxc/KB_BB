---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-12_confirm-an-email-address-belonging-to-a-specific-user.md
original_filename: 2020-12-12_confirm-an-email-address-belonging-to-a-specific-user.md
title: Confirm an email address belonging to a specific user
category: documents
detected_topics:
- sso
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- sso
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: 4918ac132ecf4a202095aa399e23d2ac222a804260bbc6c15cdc4a813980a0d7
text_sha256: 4de2e308ba2ef2932d04b37b08eadaac89b5295b90508d8092fc18d098571d88
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Confirm an email address belonging to a specific user

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-12_confirm-an-email-address-belonging-to-a-specific-user.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4918ac132ecf4a202095aa399e23d2ac222a804260bbc6c15cdc4a813980a0d7`
- Text SHA256: `4de2e308ba2ef2932d04b37b08eadaac89b5295b90508d8092fc18d098571d88`


## Content

---
title: "Confirm an email address belonging to a specific user"
url: "https://medium.com/@yaala/confirm-an-email-address-belonging-to-a-specific-user-fe9c305e0af"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "5,000"
publication_date: "2020-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4070
scraped_via: "browseros"
---

# Confirm an email address belonging to a specific user

abdellah yaala
Follow
Dec 12, 2020

156

Confirm an email address belonging to a specific user

Privacy is important, and after reading this vulnerability, you will know that Facebook gives privacy a great priority

One link enables me to exploit this vulnerability and got $ 5k. alhamdulilah

Too many emails received from facebook contain link to unsubscribe from notifications :

https://www.facebook.com/o.php?k=AS3fdO_cSPoc5dlMxoE&u=userid&mid=midparameter

I look at html form i see e parameter i add it to the previous link, i notice if email is belonging given user in u parameter the response was normal (including secondary emails ), but if i enter the wrong email i get <this page isn’t available > as response

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.facebook.com/o.php?k=AS3fdO_cSPoc5dlMxoE&u=userid&e=email&mid=midparameter

Then I reported the vulnerability,

I received a bounty of 5000$

Press enter or click to view image in full size

Thanks facebook security team .

Thanks .

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-14_idor-vulenebility-with-empty-response-still-exposing-sensitive-details-of-custom.md
original_filename: 2021-03-14_idor-vulenebility-with-empty-response-still-exposing-sensitive-details-of-custom.md
title: IDOR Vulenebility with empty response still exposing sensitive details of customers!
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: df60466a9694a60e17190a36b51548ec97ebf519e08a1522496302b27eaa0d14
text_sha256: 11906fbcb6622d88eedd86c2242c961f06e81f3fa60212811ef36eaf84614f15
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR Vulenebility with empty response still exposing sensitive details of customers!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-14_idor-vulenebility-with-empty-response-still-exposing-sensitive-details-of-custom.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `df60466a9694a60e17190a36b51548ec97ebf519e08a1522496302b27eaa0d14`
- Text SHA256: `11906fbcb6622d88eedd86c2242c961f06e81f3fa60212811ef36eaf84614f15`


## Content

---
title: "IDOR Vulenebility with empty response still exposing sensitive details of customers!"
url: "https://rahulvarale.medium.com/idor-vulenebility-with-empty-response-still-exposing-sensitive-details-of-customers-bdce0a6a1b07"
authors: ["Rahul Varale"]
bugs: ["IDOR"]
publication_date: "2021-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3819
scraped_via: "browseros"
---

# IDOR Vulenebility with empty response still exposing sensitive details of customers!

IDOR Vulenebility with empty response still exposing sensitive details of customers!
Rahul Varale
Follow
1 min read
·
Mar 14, 2021

190

Hello there👋!
For many days I was thinking of sharing my bug bounty experience with the community and finally writing my first write-up.

After basic recon, I started testing functionalities on the main domain.
It was an e-commerce website, say https://redacted.com.

As it was an e-commerce site, there is a shipping address. While updating the address, I noticed that the address_id parameter is the unique ID for each address. I tried IDOR (who dont know what is IDOR, check https://portswigger.net/web-security/access-control/idor), but it validated the session and only gave the respective user’s address. I tried changing the method GET, POST, PUT, but nothing worked.

Get Rahul Varale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then, I clicked on set as default address button, POST request sent on https://redacted.com/c/def_addr with the address_id and got 200 Response with an empty body.

I repeated the same POST request with sequential address_id and got 200 response for that and an empty response body.

After playing with address APIs, There was no success. 😞

I moved to cart and checkout functionality. After clicking on the checkout page, I was redirected to https://redacted.com/payment, and surprise!!

I noticed that there was a different address of some other user! It contains the Customer Name, Full Address, Mobile Number.
So, all user’s addresses and mobile numbers were exposed!

Thank you for reading. As this is my first write-up, suggestions are most welcome.

Connect with me on https://www.linkedin.com/in/rahulvarale/

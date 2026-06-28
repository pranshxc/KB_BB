---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-30_idor-in-jwt-and-the-shortest-token-you-will-ever-see-uid-1234567890.md
original_filename: 2018-10-30_idor-in-jwt-and-the-shortest-token-you-will-ever-see-uid-1234567890.md
title: 'IDOR in JWT and the shortest token you will ever see {}.{“uid”: “1234567890”}'
category: documents
detected_topics:
- jwt
- xss
- api-security
- sso
- idor
- access-control
tags:
- imported
- documents
- jwt
- xss
- api-security
- sso
- idor
- access-control
language: en
raw_sha256: a1a030f41af42623db1efd14a9f8c354ef0654c803c17f799bb9e3dc7c0cee99
text_sha256: 5ec518a86e3a1ee8164132824be919c578612fd948c77ab9f7311bedfbf2571f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR in JWT and the shortest token you will ever see {}.{“uid”: “1234567890”}

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-30_idor-in-jwt-and-the-shortest-token-you-will-ever-see-uid-1234567890.md
- Source Type: markdown
- Detected Topics: jwt, xss, api-security, sso, idor, access-control
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `a1a030f41af42623db1efd14a9f8c354ef0654c803c17f799bb9e3dc7c0cee99`
- Text SHA256: `5ec518a86e3a1ee8164132824be919c578612fd948c77ab9f7311bedfbf2571f`


## Content

---
title: "IDOR in JWT and the shortest token you will ever see {}.{“uid”: “1234567890”}"
page_title: "IDOR IN JWT AND THE SHORTEST TOKEN YOU WILL EVER SEE {}.{“uid”: “1234567890”} | by Plenum | InfoSec Write-ups"
url: "https://medium.com/@plenumlab/idor-in-jwt-and-the-shortest-token-you-will-ever-see-uid-1234567890-4e02377ea03a"
authors: ["Plenum (@plenumlab)"]
bugs: ["IDOR"]
bounty: "1,500"
publication_date: "2018-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5619
scraped_via: "browseros"
---

# IDOR in JWT and the shortest token you will ever see {}.{“uid”: “1234567890”}

IDOR IN JWT AND THE SHORTEST TOKEN YOU WILL EVER SEE {}.{“uid”: “1234567890”}
Plenum
Follow
2 min read
·
Oct 30, 2018

296

5

TL;DR, JWT is in use by many of the big companies but some implementations are not that safe here is a bug that got me 1,500$

Earlier this year i was participating in a bugbounty program on 
HackerOne
, the app allowed customers to order products, it seemed pretty solid, i managed to find some interesting character transformation issue so i spent hours trying to get stored xss but no luck so after a couple of days i was a bit let down. I closed burpsuite started a new project and decided to start over from the beginning.

I typed the address lets say http://example.com and logged in using my girlfriends account (i didn’t want to order anything) upon login i noticed a crossorigin pre-flight request to an api endpoint which looked something like

OPTIONS / HTTP/1.1
Host: customer-order-status.example.net
Content-Type: application/json
Connection: close

Later on using the app my girlfriend ordered a product on this app and she could check the status of her order, the check order request looked something like this

GET /api/v1/order_statuses/{order_id} HTTP/1.1
Host: customer-order-status.example.net
Authorization: Bearer JWT TOKEN
Content-Type: application/json
Connection: close

The JSON response contained personal account information including delivery address, order details, payment method, payment amount… All the juicy stuff

Get Plenum’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The JWT token had the session id and user id and signed with HS256, pretty good right but no the api did not validate any of that

{“alg”: “HS256”,“typ”: “JWT”}.{“uid”: “1234567890”,“sessionid”: “ALPHANUMERIC ID”}.SIGNATURE

The shorter version i ended up using of the authorization Token looked like

{}.{“uid”: “1234567890”}

So i could query this api endpoint using the above JWT token and the response was valid. This also worked when using past order ids

To exploit this effectively by an attacker some level of brute-forcing was needed to query random users information given the fact that there are two variables the user id and the order id this was a bit hard to exploit, what made this dangerous however is that the server did not implement request limits so it could potentially make the brute-force attack feasible.

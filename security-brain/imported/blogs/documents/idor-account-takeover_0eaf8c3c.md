---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-14_idor-account-takeover.md
original_filename: 2019-06-14_idor-account-takeover.md
title: IDOR — Account Takeover
category: documents
detected_topics:
- sso
- idor
- command-injection
- cloud-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- cloud-security
language: en
raw_sha256: 0eaf8c3c9516346215f3169bf6efd82d0dd3135a073778692b1361c8e161641a
text_sha256: 15dfc14c94096b1d803401557ec2d61390e18861d052f64bd01335956c33de51
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR — Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-14_idor-account-takeover.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0eaf8c3c9516346215f3169bf6efd82d0dd3135a073778692b1361c8e161641a`
- Text SHA256: `15dfc14c94096b1d803401557ec2d61390e18861d052f64bd01335956c33de51`


## Content

---
title: "IDOR — Account Takeover"
page_title: "IDOR — Account Takeover. Hi Guy, | by Saad Ahmed | Medium"
url: "https://medium.com/@saadahmedx/idor-account-takeover-1ff5a2d03b8b"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["IDOR"]
bounty: "500"
publication_date: "2019-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5218
scraped_via: "browseros"
---

# IDOR — Account Takeover

IDOR — Account Takeover
Saad Ahmed
Follow
2 min read
·
Jun 14, 2019

300

1

Hi Guy,

After a long time i decided to share some of my finding & contribute to this awsm community. This write up is all about the IDOR that i found in PRIVATE program that I hunting from past 1 Year.

So there is a request that update the account username https://www.site/dataentities/CL/documents/0e84b3b2-c65f-11e8–822e-0edf00549f0a` contain the following data {“firstName”:”john”,”lastName”:”account”,”document”:”32132132132",”birthDate”:”2019–05–30T00:00:00",”gender”:”male”,”homePhone”:”1000000000"}

so I notice 0e84b3b2-c65f-11e8–822e-0edf00549f0a is the user ID I created another account and replace the other account & able to change the first & last name of my 2nd account. But the USER-ID is hard to guess after spending the alot of time crawling the web i notice that there is a req that web send to server just to verify that if this email is registered or not the request look like this https://www.site.com/site/dataentities/CL/search/?email=attacker@gmail.com & the response look like this [{“email”:”attacker@gmail.com”,”id”:”0e84b3b2-c65f-11e8–822e-0edf00549f0a”}] so USER-ID problem is solved :D

I try to dig more & try to change the email i notice that the input field code is this <input type=”email” name=”email” value=”attacker@gmail.com” /> so in the update account detail this is the JSON data that send to the server {“firstName”:”john”,”lastName”:”account”,”document”:”32132132132",”birthDate”:”2019–05–30T00:00:00",”gender”:”male”,”homePhone”:”1000000000"} i add email parm & value so that JSON data look like this {“firstName”:”john”,”lastName”:”account”,”document”:”32132132132",”birthDate”:”2019–05–30T00:00:00",”gender”:”male”,”homePhone”:”1000000000", “email”:”attacker2@gmail.com”} & boom i able to change any one email which lead to Account Takeover

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Without wasting time i make a good report & reported to the team and this is the response that is get from

Press enter or click to view image in full size

and after some time the Analyst come

Press enter or click to view image in full size

Lesson : Alway try harder :D hope you like it

./LOGOUT

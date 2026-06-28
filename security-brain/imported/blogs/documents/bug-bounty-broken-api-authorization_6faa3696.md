---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-12_bug-bounty-broken-api-authorization.md
original_filename: 2019-11-12_bug-bounty-broken-api-authorization.md
title: 'Bug Bounty: Broken API Authorization'
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
language: en
raw_sha256: 6faa3696f8f883a423b2c0964abd68a03f5ec59d080cfe93c66d212453f82114
text_sha256: fc43ca2b68ac7fe62d263c1d69b1f0f5282d0216d1288f2bf2cff9b283d6e038
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty: Broken API Authorization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-12_bug-bounty-broken-api-authorization.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6faa3696f8f883a423b2c0964abd68a03f5ec59d080cfe93c66d212453f82114`
- Text SHA256: `fc43ca2b68ac7fe62d263c1d69b1f0f5282d0216d1288f2bf2cff9b283d6e038`


## Content

---
title: "Bug Bounty: Broken API Authorization"
url: "https://medium.com/@th3hidd3nmist/bug-bounty-broken-api-authorization-d30c940ccb42"
authors: ["Th3hidd3nmist (@th3_hidd3n_mist)"]
bugs: ["Broken authorization"]
bounty: "440"
publication_date: "2019-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4949
scraped_via: "browseros"
---

# Bug Bounty: Broken API Authorization

1

Bug Bounty: Broken API Authorization
Omkar Bhagwat (th3_hidd3n_mist)
Follow
3 min read
·
Nov 12, 2019

524

2

I’ve moved my blog to https://th3hidd3nmist.github.io/

Hey everyone, I’d like to share how I found a simple API authorization bug in a private program, which affected thousands of sub-domains and allowed me to exploit a plethora of unprotected functionality without user interaction, from account deletion to takeovers and leaking limited information(Full name, e-mails ids and employer).

Tl;dr: The server wasn’t checking if the authorization bearer token belonged to a regular user or a poweruser.

It’s a private program, so some information will be redacted and I’ll refer to the site as “target.com”.

I had a dirsearch scan running in the background while skimming through
academy.target.com, to get an overview of the sites functionality.
I noticed an interesting endpoint like: academy.target.com/api/docs
Endpoints like these are a goldmine because they have API documentation and specify the structure of requests and responses.

On browsing to the endpoint, I found the page to be extremely similar to Swagger UI (this site didn’t use swagger though). It also had a button simply called “Authenticate”, and clicking on it navigated to a login page but it threw a “Account not authorized” message, if I tried logging in.

There were some interesting endpoints like:
/poweruser/add
/poweruser/delete
/user/delete
/user/create
/user/user_logged_in
/user/profile

Press enter or click to view image in full size
The page kinda looked like this.

This caught me off guard because it seemed like these endpoints should be reserved for internal/power users use only.
Directly calling the endpoints without any API token or authorization header resulted in:

Press enter or click to view image in full size
An unsurprisingly disappointing response

The website didn’t seem to offer any API, and I couldn’t find any way to generate an API token, so I decided to check it out later.
After extensively searching the site, I still couldn’t find a single API token in the requests or the response.
However, I noticed many requests had an authorization bearer token.

Get Omkar Bhagwat (th3_hidd3n_mist)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I decided to simply copy the header and include it in the calls to the API endpoints I found.
I created another account and tried to change its password, with a POST request to api/user/edit.

HTTP request to change another users password, this time with the bearer token.
Successful response lol.

Voilà! It worked like a charm. Apart from escalating my account to a power-user, I could successfully invoke almost all the other API endpoints.
The documentation detailed the parameters I needed to delete/take over/create new accounts and do some other bad things.

I decided to report the vulnerability directly to the vendor and it turned out they had a private bug bounty program and awarded me a $440 bounty.

Thanks for reading!

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

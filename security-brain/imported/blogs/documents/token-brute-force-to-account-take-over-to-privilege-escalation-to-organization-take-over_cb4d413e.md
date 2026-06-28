---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-10_token-brute-force-to-account-take-over-to-privilege-escalation-to-organization-t.md
original_filename: 2018-12-10_token-brute-force-to-account-take-over-to-privilege-escalation-to-organization-t.md
title: Token Brute-Force to Account Take-over to Privilege Escalation to Organization
  Take-Over
category: documents
detected_topics:
- access-control
- command-injection
- otp
- rate-limit
- cors
- csrf
tags:
- imported
- documents
- access-control
- command-injection
- otp
- rate-limit
- cors
- csrf
language: en
raw_sha256: cb4d413e244edacfd23df8034c0636ca6953748a8cbcb2da558ade3096fae167
text_sha256: 64c42acd6f8fc8a38820c43cdd9d73e93dc37f49919a87b1ab2e0297dfe68de8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Token Brute-Force to Account Take-over to Privilege Escalation to Organization Take-Over

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-10_token-brute-force-to-account-take-over-to-privilege-escalation-to-organization-t.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, rate-limit, cors, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `cb4d413e244edacfd23df8034c0636ca6953748a8cbcb2da558ade3096fae167`
- Text SHA256: `64c42acd6f8fc8a38820c43cdd9d73e93dc37f49919a87b1ab2e0297dfe68de8`


## Content

---
title: "Token Brute-Force to Account Take-over to Privilege Escalation to Organization Take-Over"
url: "https://medium.com/bugbountywriteup/token-brute-force-to-account-take-over-to-privilege-escalation-to-organization-take-over-650d14c7ce7f"
authors: ["Plenum (@plenumlab)"]
bugs: ["Account takeover", "Privilege escalation", "Bruteforce"]
publication_date: "2018-12-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5536
scraped_via: "browseros"
---

# Token Brute-Force to Account Take-over to Privilege Escalation to Organization Take-Over

Token Brute-Force to Account Take-over to Privilege Escalation to Organization Take-Over
Plenum
Follow
3 min read
·
Dec 10, 2018

184

Press enter or click to view image in full size

TL;DR, Not all web vulnerabilities are a result of a technical issue, functional bugs can have critical business impact. Here is the story of how chaining simple issues and poor design flaws can result in account take over, privilege escalation and ultimately organization take-over.

While working on a private program i was testing a product on redacted.com which is basically an app to view and manage all business data collected from several apps in one place (just imagine how much valuable data is in there). Companies are able to create a work space or organization within this app, an admin would then invite users to join.

I often start with testing the invite functionality as it often result in critical issues. There are only two possible roles either user or admin, at first the invite flow seemed solid CSRF protection was in place CORS were configured properly it seemed like nothing was there and everything worked fine until, i found the first issue, there was a huge problem with the invite system, if an admin invites an external user the invitation link looked like this

https://login.redacted.com/accounts/?service=product&digest=saaOBeXStZDRqgVlSRPAgPSY0

Pretty solid right?

Next I tried to invite a user that has an existing account on redacted.com and as it turns out the resulting invitation was quite different the link looked like this

https://product.redacted.com/invitations?inviteId=160000002637191&type=accept&source=mail

No signature no hash nothing!!! Wait WHAAAAAAT!!!!!

You can see where this is going. First, let me putin on my special glasses before we dive in.

With further inspection i came to a conclusion that the first 12 digits refers to the organization and the last 3 are the invitation id in this case 160000002637 is the organization id while 191 is the invitation id. That is easily brute-forceable.

Get Plenum’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With some more tests i figured that not only this id is bruteforceable it didn’t expire if another person used it so if admin sends invitation to X email but attacker bruteforce the token he could join the organization with email Y, Z and N emails the invite would sill be valid until email X is used. It meant that an attacker can bruteforce token infiltrate organization and the admin would still see invitation as pending, cool ha! So to summarize this part here is the scenario

Admin of org sends invitation to User A with email X
Attacker bruteforce invitation ID
Attacker signup with email Y
Attacker is inside org
Admin will see that the invitation is still pending

You would think OK how this would result in an organization takeover or privilege escalation, the app had also another issue, a user can view pending invitations and their roles once he finds an admin invitation he could exploit it and takeover the hole thing using the disclosed email address. In other words this would drastically decrease bruteforce attack, once he found a single valid token he would stop bruteforcing join the organization if the invite was for an admin then he hit a jackpot if the invite was for a user he would simply keep checking the pending invites section until he finds an admin invite, given the fact that an org can have large number of users, there is a great chance he would remain unnoticed.

As a bounty hunter you should look into functional bugs too as these bugs can result in a critical business impact.

Till next time,
Happy hunting everyone,

Plenum

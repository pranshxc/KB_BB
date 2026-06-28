---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-09_what-is-bola-3-digit-bounty-from-topcoder-.md
original_filename: 2021-08-09_what-is-bola-3-digit-bounty-from-topcoder-.md
title: What is BOLA? 3-digit bounty from Topcoder ($$$)
category: documents
detected_topics:
- idor
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 94344563678001a6d0567acb58623c8b34f6f87721836aa8e7b96a5399477995
text_sha256: d4af3fc34bde5b056e67902d5240ce85e5dbedfb3cd0fb9025a1388409ea0ac0
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# What is BOLA? 3-digit bounty from Topcoder ($$$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-09_what-is-bola-3-digit-bounty-from-topcoder-.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `94344563678001a6d0567acb58623c8b34f6f87721836aa8e7b96a5399477995`
- Text SHA256: `d4af3fc34bde5b056e67902d5240ce85e5dbedfb3cd0fb9025a1388409ea0ac0`


## Content

---
title: "What is BOLA? 3-digit bounty from Topcoder ($$$)"
url: "https://infosecwriteups.com/what-is-bola-3-digit-bounty-from-topcoder-a25e7fae0d64"
authors: ["can1337 (@canmustdie)"]
programs: ["Topcoder"]
bugs: ["IDOR"]
publication_date: "2021-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3432
scraped_via: "browseros"
---

# What is BOLA? 3-digit bounty from Topcoder ($$$)

What is BOLA? 3-digit bounty from Topcoder ($$$)
can1337
Follow
4 min read
·
Aug 9, 2021

180

Hello everyone.

This write-up will be about Broken Object Level Authorization (BOLA), which is #1 topic of API Security (OWASP). I will also consider a case where I found this vulnerability. Well, without further ado, let’s get it started.

What is Broken Object Level Authorization (BOLA)?

Press enter or click to view image in full size
(Defense against BOLA)

Broken Object Level Authorization (BOLA) relies on the ability of a sensitive request sent by a user on the application to be accessed by other resources. This is often the result of missing/incorrect access controls by the developers. Technically it can basically be likened to IDOR. When this security configuration is not done correctly, it has a wide attack surface (from information disclosure to account takeover).

As can be seen from the image, if we try to make a typical attack scenario, it will be like this:

The victim and attacker will be given specific identities by the API and given access to their sensitive data. (https://redacted.com/exposed/v1/profiles/self-id)
The attacker will notice the weakness in the API and will be able to access the victim’s PII data using the victim’s user-id. (https://redacted.com/exposed/v1/profiles/target-id)

However, these user-specific variables do not always need to be kept in the GET request. Some APIs may also carry user-specific variables in the POST request. In some cases, the vulnerability API may be configured based on more than one control point.

A BOLA case in Topcoder

Press enter or click to view image in full size

Depending on this situation, I will tell you about the vulnerability I found in Topcoder. This vulnerability will be about multiple checkpoints on an API. (This report was made public on hackerone: https://hackerone.com/reports/1073420)

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I started looking for a vulnerability on Topcoder, I first created an account on topcoder.com, while I was checking all HTTP requests via Burp, I noticed my forum user-id information during membership opening, I could also access this value in the source code of member page. Also when I entered the profile of any other user, I could see the forum user-id.

Press enter or click to view image in full size

I couldn’t find much on the main site and started looking for sub-domains (I sent some reports but duplicate :/) I got the subdomains list and decided to analyze the Topcoder forum. (apps.topcoder.com/forums). It was using my account directly on the main site. So, my PII information on the main site was also valid for my forum account.

After browsing the forum for a while, I entered a thread and noticed the “Watch Thread” part. I opened the Intercept and started reviewing the requests.
An API from a different host was sending a POST request without an Authorization header. In this case, I decided to take a closer look at the API and some information in the POST data caught my attention. It was taking an ID information defined by the API (I guess) in the header of the request and my forum user-id in the data section. In the response section, I could see my email, name-surname and account_id that were not reflected in my Topcoder profile.

I immediately created another user and changed my Topcoder ID in the data section. However, nothing changed. The API was taking multiple values ​​and could be using all of them to control the user.
The ID reflected in the header of the request caught my attention, I changed the last digit with another letter and at the same time I replaced my Topcoder id with the victim’s Topcoder id and sent the request.

Press enter or click to view image in full size

BINGO! I was able to access the target’s PII information. The API was trying to authenticate the target user using multiple checkpoints. However, this information was publicly displayed on Topcoder.com and the ID given by the API reflected sensitive data when changed to a random value.

Topcoder confirmed this vulnerability and rewarded me with $$$.

Resources:
https://blog.shiftleft.io/api-security-101-broken-object-level-authorization-fe8720c779ec

What is Broken Object Level Authorization (BOLA) and how can affect you?
According to the OWASP (Open Web Application Security Project) 2019 API Security Project, Broken Object Level…

heimdalsecurity.com

https://github.com/OWASP/API-Security/blob/master/2019/en/src/0xa1-broken-object-level-authorization.md

Thanks!!

Twitter: https://twitter.com/canmustdie

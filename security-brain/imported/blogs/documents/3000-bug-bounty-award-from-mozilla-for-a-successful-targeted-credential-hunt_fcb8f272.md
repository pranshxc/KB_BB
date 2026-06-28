---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-13_3000-bug-bounty-award-from-mozilla-for-a-successful-targeted-credential-hunt.md
original_filename: 2020-05-13_3000-bug-bounty-award-from-mozilla-for-a-successful-targeted-credential-hunt.md
title: $3000 Bug Bounty Award from Mozilla for a successful targeted Credential Hunt
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: fcb8f2720c0c0b8569a5e40f8b9ecc57c2c99ba3604f5917d52446ed46eef992
text_sha256: f2e81c7c807a7fc0e1fbbd906ee79e8da35bc66f2aba613e7fadfcd1741907a7
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# $3000 Bug Bounty Award from Mozilla for a successful targeted Credential Hunt

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-13_3000-bug-bounty-award-from-mozilla-for-a-successful-targeted-credential-hunt.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `fcb8f2720c0c0b8569a5e40f8b9ecc57c2c99ba3604f5917d52446ed46eef992`
- Text SHA256: `f2e81c7c807a7fc0e1fbbd906ee79e8da35bc66f2aba613e7fadfcd1741907a7`


## Content

---
title: "$3000 Bug Bounty Award from Mozilla for a successful targeted Credential Hunt"
page_title: "$3000 Bug Bounty Award from Mozilla for a successful targeted Credential Hunt ·  Embrace The Red"
url: "https://embracethered.com/blog/posts/2020/mozilla-bug-bounty-credential-hunt-phabricator-token/"
final_url: "https://embracethered.com/blog/posts/2020/mozilla-bug-bounty-credential-hunt-phabricator-token/"
authors: ["Johann Rehberger (wunderwuzzi23)"]
bugs: ["Information disclosure"]
bounty: "3,000"
publication_date: "2020-05-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4591
---

# $3000 Bug Bounty Award from Mozilla for a successful targeted Credential Hunt

Posted on  May 13, 2020 

[#red](https://embracethered.com/blog//tags/red) [#ttp](https://embracethered.com/blog//tags/ttp) [#book](https://embracethered.com/blog//tags/book) [#bugbounty](https://embracethered.com/blog//tags/bugbounty)

Last month I did some research on Firefox, specifically I was learning more about it’s remote debugging features. As part of that I was reading Bugzilla bug information and learned more about Mozilla’s infrastructure.

One thing I noticed reading up on details was that Mozilla uses **Phabricator**.

### What is Phabricator?

**Phabricator** is a collaborative web-based toolset for code reviews, checkins, bugs, work items, wiki, pastes, credentials and many other useful things. It was orginally developed by Facebook as far as I know.

### API Tokens

From past red teaming experience I know that its common for developers to create API tokens for command line usage to interact with Phabricator.

There is a tool called **arcanist** that is used to perform checkins via `arc land` and so forth. These tokens usually start with `api-` or `cli-` followed by number of random characters.

**Mozilla actively encourages security research and bounty hunting to help improve the security posture of their software and services.**

[Here](https://www.mozilla.org/en-US/security/bug-bounty/) an excerpt from Mozilla’s bug bounty page:

> Mozilla strongly supports security research into our products and wants to encourage that research.

Equipped with this intel and knowing that Mozilla encourages security research, I decided to perform a **targeted Phabricator Credential Hunt** for Mozilla.

### Targeted Credential Hunting

**[Credential Hunting](/blog/posts/2020/hunting-for-credentials)** is a dedicated and **targeted activity** that I recommend performing during red teaming and penetration testing. After gaining some basic intel about systems used and what to specifically look for, targeted credential hunting can be fruitful.

Using the information and techniques from the previous post about Credential Hunting and related ones described in my book, **I had identified a valid Mozilla Phabricator API token, along with a Bugzilla token** in a Github repo.

### Token Validation

To validate the token, I used the Phabricator **whoami** API.
  
  
  curl https://<phabricator>/api/user.whoami -d api.token=api-xxxx
  

The response of the request showed that the token impersonated a Mozilla account. At that point I knew, what I needed to know - there was no need to perform any other action.

### Reporting

**I promptly reported this issue to Mozilla and they fixed it basically immediatley**. They also performed investigations to ensure no misuse had occured and searched for variants.

It was impressive to watch Mozilla’s professionalism during the response.

### The power of credential hunting

This is an example to show how useful it is to perform **active and targeted credential hunts** for your clients or organization. Tokens often are out there but automated scanning tools might not be able to identify or validate them yet (because of parsing or lack of intel, or other reasons).

**Mozilla awarded a $3000 bug bounty reward for this. :)**

### Red Team Strategies

If you liked this post and found it informative or inspirational, you might be interested in my book [“Cybersecurity Attacks - Red Team Strategies”](https://www.amazon.com/gp/product/1838828869/ref=as_li_tl?ie=UTF8&tag=wunderwuzzi-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1838828869&linkId=07bfd6b729fbc2b2904160e0e16c337f). It is filled with further ideas, research and fundamental techniques, as well as red teaming program and people mangement aspects.

Also, feel free to follow or DM me on Twitter: [@wunderwuzzi23](https://twitter.com/wunderwuzzi23)

### References

  * [Mozilla Bug Bounty](https://www.mozilla.org/en-US/security/bug-bounty/)
  * [Credentials Reference - Markdown](https://github.com/wunderwuzzi23/scratch/blob/master/creds.md)
  * [Credentials Reference - CSV](https://github.com/wunderwuzzi23/scratch/blob/master/creds.csv)
  * [Phabricator](https://phacility.com/phabricator)

![Hacker](/blog/images/2020/hacker.png)

* * *

  * [Newer →](https://embracethered.com/blog/posts/2020/phishing-stats/)
  * [ __Contact me](mailto:security@wunderwuzzi.net)
  * [← Older](https://embracethered.com/blog/posts/2020/cookie-crimes-on-mirosoft-edge/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-07_github-organization-takeover-by-claiming-owner-invitation.md
original_filename: 2021-01-07_github-organization-takeover-by-claiming-owner-invitation.md
title: Github Organization Takeover By Claiming Owner Invitation
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: ae8ce15d0fe974aaf56bb50e95b08b2e6bb0239819d27fa11c8c4f2449abfc64
text_sha256: f3ef44db3a29ee77d3f78e4d35dbf56e864a7b1c29eb8463cf3cc0053f40215b
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Github Organization Takeover By Claiming Owner Invitation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-07_github-organization-takeover-by-claiming-owner-invitation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `ae8ce15d0fe974aaf56bb50e95b08b2e6bb0239819d27fa11c8c4f2449abfc64`
- Text SHA256: `f3ef44db3a29ee77d3f78e4d35dbf56e864a7b1c29eb8463cf3cc0053f40215b`


## Content

---
title: "Github Organization Takeover By Claiming Owner Invitation"
page_title: "Github Organization Takeover By Claiming Owner Invitation - Abss"
url: "https://abss.me/posts/github-org-takeover/"
final_url: "https://abss.me/posts/github-org-takeover"
authors: ["Abss (@absshax)"]
programs: ["GitHub"]
bugs: ["Account takeover", "Logic flaw"]
bounty: "5,000"
publication_date: "2021-01-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4021
---

# [Abss](/)

## My write-up’s, Discoveries & Open Source Contributions

[__](https://github.com/abss0x7tbh "Github")[__](https://twitter.com/absshax "Twitter")

  * [Home](/)
  * [Blog](../posts)
  * [Open-Source](../open-source)
  * [Press Appearances](../press-appearances)

# Github Organization Takeover By Claiming Owner Invitation

Posted on — Jan 7, 2021

* * *

## TL;DR

_courtesy -<https://bounty.github.com/researchers/Abss0x7tbh.html>_

A malicious user could leverage 3 things to takeover a Github Organization :

  * An invitation to owner from the organization.
  * No email verification.
  * No check on email verification prior to accepting invitation.

This bug was reported on Nov 17,2017 and was one of my very first bugs.

* * *

## The Invitation feature

Through github.com one can create an organization within their personal account and invite team members. I was hard on checking for any account privilege escalations here.

So whilst surfing through github.com, i created an organization and started testing. I noticed that only the team maintainer or the owner can invite people to the organization. When sending the invite, the invitee could either be a github user or someone who is new to github.

If the user is new to github then the invitation has to be sent via their email only. If they are already a github user we have an option to choose their username and then send the invitation.

As seen below, we can also chose the privilege of the invitee and send the invitation. The owner has complete control over the organization.

![Inviting owner](../inviting_owner.png)

With the invite sent, i intuitively created a new github account with the invitee email instead of the `basic email invitation > account creation + accepting invitation`.

I noticed that at the `github.com/org_name` page, i had my invitation displayed.

![Web Invitation](../web_invitation.png)

Well this was normal as github does display invitations as such. The next thing that hit me was that i forgot the email verification part whilst creating the above account. So this meant I can be someone impersonating this invitee.

As I hadn’t verified my email yet the invitation could just be a client-end display notification and not a legit endpoint with the invitation token?

Well that wasn’t the case! I was able to accept the invitation and join the org as the new owner!

![Accept Invitation](../accept_invitation.png)

## Scenario

It was time to file the report by first creating a scenario.

Here’s what would happen :

  * Assume an organization invites the new owner through their email. This means they aren’t a github user and would likely have to create a new github account.
  * This means a malicious user could set-up a new account with the invitee email.
  * The invitation endpoint does not verify if the invitee has their email verified. This means anyone can impersonate the invitee. The web invitation is displayed on the organization page i.e `github.com/org_name` without any checks also revealing the invitation_token.
  * The malicous user just has to accept invitation before the actual owner does(via their email) ,claiming the invitation,impersonating the invitee owner in the process and gaining control over the organization.

I was able to find a couple of similar bugs henceforth.

## Timeline

Bug reported - Nov 8th 2017

Bug Resolved/Bounty/Swag - $5000 - Nov 16th 2017

* * *

adiós!

Share on: 

Abss© Copyright notice | [Ezhil theme](https://github.com/vividvilla/ezhil) | Built with [Hugo](https://gohugo.io/)

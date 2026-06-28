---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-24_messenger-rooms-bug-bounty-write-up.md
original_filename: 2020-04-24_messenger-rooms-bug-bounty-write-up.md
title: Messenger Rooms Bug Bounty Write-up
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: d538401ade0c1fcb55b84bcae1a960706cd5a8db92cfdf29e3131dc2cee70b67
text_sha256: 8a8e966643135f5f5e07bfa80e7770565b194417cc3cbb0c4500d3c9cbf73e37
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Messenger Rooms Bug Bounty Write-up

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-24_messenger-rooms-bug-bounty-write-up.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `d538401ade0c1fcb55b84bcae1a960706cd5a8db92cfdf29e3131dc2cee70b67`
- Text SHA256: `8a8e966643135f5f5e07bfa80e7770565b194417cc3cbb0c4500d3c9cbf73e37`


## Content

---
title: "Messenger Rooms Bug Bounty Write-up"
url: "https://wongmjane.com/blog/messenger-rooms-writeup"
final_url: "https://wongmjane.com/blog/messenger-rooms-writeup"
authors: ["Jane Manchun Wong (@wongmjane)"]
programs: ["Meta / Facebook"]
bugs: ["Privilege escalation", "Broken authorization"]
publication_date: "2020-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4636
---

[Writing](/blog)

April 24, 2020·2 min read·[Jane Manchun Wong](/)

# Messenger Rooms Bug Bounty Write-up

## Timeline (TL;DR)

Report Sent

By Jane Manchun Wong

Oct 10, 2019

Report Triaged

By Facebook

Oct 10, 2019

Requested for status update

By Jane Manchun Wong

Apr 8, 2020

Mitigated with a temporary fix

By Facebook

Apr 15, 2020

Vulnerability Patched

By Facebook

Apr 21, 2020

Bug Bounty Awarded

By Facebook

Apr 22, 2020

Embargo Lifted

Apr 24, 2020

Heads up!

This security vulnerability report was submitted 6 months before Messenger Rooms was released. There might be slight terminology differences, for instance, “Video Meetup Link” and “Messenger Call” at the time are now branded as “Messenger Rooms”

## Introduction

Messenger is developing “Video Meetup Link”, a feature that allows anyone to join a Messenger Call through an invite link even without a Facebook account.

This anonymous Messenger call joining is authenticated by creating a special kind of User named  [REDACTED] .

Although [REDACTED] is created for the sole purpose of joining the Messenger Call, this guest user is capable of doing more than what it is supposed to do. For example, (anonymously) creating a “Video Meetup Link” as a video meetup guest user.

The guest user is also capable of other queries, such as browsing Facebook without having a real Facebook account.

[REDACTED] should only be capable of joining the Messenger Call, nothing else. Other operations than joining the call should be unauthorized.

## Repro Steps

Supposedly, the only thing a [REDACTED] can do is join the Messenger Call the guest user is created for. But here, we can create another Messenger Call using the guest user.

From the response of the above request, we can see it is possible to create another Messenger Call Invite Link without a real Facebook account. A [REDACTED] is not supposed to have that capability.

Other than creating the invite link, [REDACTED] is also capable of browsing Facebook, when it is supposed to only be able to join the Messenger Call it is created for. It does not bypass the usual privacy checks per se, but [REDACTED] is not even supposed to be able to browse any content whose privacy setting is set to “Public”. Again, the only job this user has is to join the Messenger Call.

## Further Comments from Facebook

After this security vulnerability has been resolved, I reached out to Facebook for further comments. Facebook’s Security Team told me via Facebook Tech Comms Manager [Alexandru Voica (opens in new window)](https://x.com/alexvoica) with the following statement:

> The issue you found was in an early test of Messenger video chat links, which we’ve fixed in Messenger Rooms. To address the issue, we made the permission checks on our API more restrictive. People who join a Room call without a Facebook or Messenger account will only be able to access the video chat. They will not be able to access Facebook or Messenger without creating an account first. Rooms links can only be created by people with Facebook or Messenger accounts, and soon through WhatsApp and Instagram too. As always, we appreciate you submitting the report to our bug bounty program and helping us strengthen the security of our products!

Share

[Twitter (opens in new window)](https://twitter.com/intent/tweet?text=Messenger%20Rooms%20Bug%20Bounty%20Write-up&url=)Copy link

[Jane Manchun Wong](/) © 2010-2026

[All writing](/blog)

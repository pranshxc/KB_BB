---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-31_this-is-how-i-was-able-to-permanently-crash-all-mapillary-users-within-minutes.md
original_filename: 2021-10-31_this-is-how-i-was-able-to-permanently-crash-all-mapillary-users-within-minutes.md
title: This is how i was able to Permanently Crash all Mapillary users within minutes
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- graphql
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- graphql
- mobile-security
language: en
raw_sha256: ab97dc7a1ba3cab46a641403e06903d8d0b7fbcd749230075c5f88c4fc4c922f
text_sha256: e59733f441c50cf20d7236efb5d6a48f04476eb4f94ad8111b383de432cd46a5
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# This is how i was able to Permanently Crash all Mapillary users within minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-31_this-is-how-i-was-able-to-permanently-crash-all-mapillary-users-within-minutes.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ab97dc7a1ba3cab46a641403e06903d8d0b7fbcd749230075c5f88c4fc4c922f`
- Text SHA256: `e59733f441c50cf20d7236efb5d6a48f04476eb4f94ad8111b383de432cd46a5`


## Content

---
title: "This is how i was able to Permanently Crash all Mapillary users within minutes"
url: "https://pathleax.medium.com/this-is-how-i-was-able-to-permanently-crash-all-mapillary-users-within-minutes-c7276def5a94"
authors: ["Abhishek Pathak (@pathleax)"]
programs: ["Meta / Facebook"]
bugs: ["Application-level DoS"]
publication_date: "2021-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3201
scraped_via: "browseros"
---

# This is how i was able to Permanently Crash all Mapillary users within minutes

This is how i was able to Permanently Crash all Mapillary users within minutes
ecstasy
Follow
4 min read
·
Oct 31, 2021

121

2

Hello everyone! This is my first Bug Bounty from Facebook Social Media Platform (Meta, Inc)

About Mapillary

Mapillary is a street level imagery platform acquired by Facebook (Meta, Inc) in June 2020, It combines street images from any camera into a visualisation to improve maps.

Description

This bug could allow an attacker to remotely permanent crash Mapillary Android app users by supplying their account’s UID (Unique ID).

Impact

An attacker can crash it’s main feature called “Capture” and “Organization” options of a particular user without doing any interaction. Which can permanently stop an user to capture and upload images.

Story and Repro Steps

One day i was talking to my friend Mayur Fartade, He told me about Facebook’s new acquisition “Mapillary” that got listed in their Bug Bounty page. So, i instantly took my laptop and started digging it.

After some time i saw a feature called “Organization” which allows users to create their own private organization and add members to contribute.

Created a test organization and started trying XSS (Cross Site Scripting) by putting javascript prompt and alert codes in description and name but at the end got no success.

After sometime, clicked “Edit Name” and typed random lengthy stuffs (as i was bored) and submitted it. But unfortunately i was not able to change it’s name due to max length limit set in input box.

PS: This bug applies to both input box (Name and Description) so screenshots may vary.

Press enter or click to view image in full size

As it was client side error so i thought let’s try if it throws the same error by server side too.

Entered a short text in the input box, submitted by clicking “Change” and intercepted the request.

While intercepting i got this POST request with JSON body, So sent it to repeater for testing.
Endpoint: https://graph.mapillary.com/graphql

Body: {“operationName”:”update_organization”,”variables”:{“id”:”[ORG_ID]”,”description”:”[D_TEXT]”,”name”:”[N_TEXT]”},”query":”[REDACTED]”}

Where [ORG_ID] is the Organization ID, [REDACTED] is query, [D_TEXT] is description text value and [N_TEXT] is name text value.

As max length for description was 160 characters and 15 characters for name, So i entered lengthy characters for description and name, pressed send request and got this response.

So i immediately checked my Organization page and Guess what? The max length limitation was not implemented on the server.

Press enter or click to view image in full size

But wait, What’s the impact of doing this? First question came in my mind before submitting the report, “Triager might mark this bug as Informative or N/A, as there is no Impact. So i have to find a good impact first, Then i’m ready to go!”

Get ecstasy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After searching for sometime, I found that Json Parsing Exception can crash Android apps.

So, downloaded Mapillary android application and logged in my secondary Mapillary test account.

Added that secondary test account into my Organization to check whether it shows or not.

Press enter or click to view image in full size

A new organization account was added into “Organization” section on my secondary account. Also got to know that, organization is connected with it’s main feature Called “Capture” because it is required to upload images.

Press enter or click to view image in full size

I was pretty sure that this app can be crashed easily by triggering Json Parser Exception. So, Now let’s begin!

Coded a Python script which creates 30 dummy organization accounts, renames description and name with a large Json Payload or Malformed big/lengthy text.

Press enter or click to view image in full size

Created another Python script which adds a targeted user by UID to those all 30 dummy organization. Later added my secondary test account using it.

Now when i opened my Mapillary app and clicked “Capture” button, Boom! This happened.

Press enter or click to view image in full size

It got remotely crashed, Now this affected user can’t access this main feature via an Android smartphone anymore.

It was a permanent crash, As there was no feature to remove yourself from someone’s organization.

After few days i got a way to scrape UID of almost all Mapillary users by intercepting requests of street images and checking responses for uploader/owner UID.

Timeline

02 Oct 2021 — Initial Report

03 Oct 2021 — Triaged

06 Oct 2021 — Fixed

06 Oct 2021 — Confirmation of Fix

11 Oct 2021 — Bounty Awarded $$$

20 Oct 2021 — Updated Hall of Fame

Thank you for reading this write-up!

You can follow me on Twitter @hi_ecstasy

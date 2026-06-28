---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-04-03_facebook-invitees-email-address-disclosure.md
original_filename: 2016-04-03_facebook-invitees-email-address-disclosure.md
title: Facebook Invitees Email Address Disclosure
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 5160d6b279c8f50c2765a8a7ef4c10446c5b2e12973d4c12ec881d9559cc2e3d
text_sha256: a8195f5a3f53220b627c8d2574c194e8e7a1b311c767e1ed2ca9c4d5d1ae45eb
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Invitees Email Address Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-04-03_facebook-invitees-email-address-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5160d6b279c8f50c2765a8a7ef4c10446c5b2e12973d4c12ec881d9559cc2e3d`
- Text SHA256: `a8195f5a3f53220b627c8d2574c194e8e7a1b311c767e1ed2ca9c4d5d1ae45eb`


## Content

---
title: "Facebook Invitees Email Address Disclosure"
url: "https://medium.com/@albeckshahar/facebook-invitees-email-address-disclosure-25059ae93725"
authors: ["Shahar Albeck"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2016-04-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6306
scraped_via: "browseros"
---

# Facebook Invitees Email Address Disclosure

Facebook Invitees Email Address Disclosure
Shahar Albeck
Follow
3 min read
·
Jan 22, 2019

17

Note: The following article was published on 03/04/2016 on https://FogMarks.com

Press enter or click to view image in full size
Sinking boat painting by Willy Stöwer

W

hen Facebook was just a tiny company with only a few members, it needed a way to get more members.

Today, when you want more visitors to your site, you advertise on Facebook, because everybody is there.

Back then, the main advertising options were manually post advertisements on popular websites (using Google, for instance), or getting your members invite their friends using their email account.

Facebook’s Past Invitation System

When a user joined Facebook at its early days, there was literally nothing to see. Therefore, Facebook asked their members to invite their friends using an email invitation that was created by the registered user.

The user supplied his friends email addresses, and they received an email from Facebook saying that ‘Mister X is now on Facebook, you should join too!’.

Fun Part

As I came across this feature of Facebook I immediately started to analyze it.

I thought it would be nice to try and fool people that a user Y invited them to join, although the one who did it was the user X.

Get Shahar Albeck’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As I kept inviting people over and over again I have noticed something interesting: each invitation to a specific email address contained an invitation ID: ent_cp_id.

Press enter or click to view image in full size

When clicking on Invite to Facebook a small windows pops up and shows the full email address of the invitee.

I wrote down the ent_cp_id of some email I would like to invite, and invited him once.

At this point I thought: “OK, I have invited this user, the ent_cp_id of him should not be accessible anymore”. But I was wrong. The ent_cp_id of it was still there. In fact, by simply re transmitting the HTTP request I could invite the same user again.

But the most interesting part of this vulnerability is the fact that any user could have seen the email address that was behind an ent_cp_id.

That means that anyone who was ever invited to Facebook via email was vulnerable to email address disclosure, because that invitation was never deleted and it was accessible to any user. All an attacker had to do next was to randomly guess ent_cp_ids. As I said, old ent_cp_ids aren’t deleted, so the success rate is very high.

Conclusion

When you are dealing with sensitive information like email address you should always limit the number of times that an action could be done. In addition, it is recommended to wipe any id that might be linked to that sensitive information, or at least hash-protect it.

Facebook quickly solved this issue and awarded a kind bounty.

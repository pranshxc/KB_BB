---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-04_senstive-information-leak-lead-to-join-any-organisation_2.md
original_filename: 2017-11-04_senstive-information-leak-lead-to-join-any-organisation_2.md
title: Senstive Information Leak Lead To join any Organisation
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: bcc84ee8eeb646f3477c92b3acdd1b762e3e3f33cc803caaf2427251048f67da
text_sha256: a69941979f49a8ddd05df63fd4b19215a235eadcdbef6afd057e8c0279cecda1
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Senstive Information Leak Lead To join any Organisation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-04_senstive-information-leak-lead-to-join-any-organisation_2.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `bcc84ee8eeb646f3477c92b3acdd1b762e3e3f33cc803caaf2427251048f67da`
- Text SHA256: `a69941979f49a8ddd05df63fd4b19215a235eadcdbef6afd057e8c0279cecda1`


## Content

---
title: "Senstive Information Leak Lead To join any Organisation"
url: "https://medium.com/bugbountywriteup/senstive-information-disclose-lead-to-join-any-organisation-40ab549011"
authors: ["Shivbihari Pandey (@ninja_pandit_)"]
bugs: ["Information disclosure"]
publication_date: "2017-11-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6065
scraped_via: "browseros"
---

# Senstive Information Leak Lead To join any Organisation

Senstive Information Leak Lead To join any Organisation
Shivbihari Pandey
Follow
3 min read
·
Nov 4, 2017

127

2

Disclaimer:

The sole purpose of this article is educational and for testing of your own applications. This is not intended for piracy or any other non-legal use.

Description:

This is my first blog,so their may be mistakes but Learning From Mistakes make you Expert.

So story About this issue that, i was testing the

site: XYZ.com [Sorry can’t disclose the Name]

After messing hour , i got an point where data disclosed.

In site You can Follow The User , Organisation ,Tag etc. Etc.

So when-ever You Follow Any User . in response[Usually i Use Browser console]. its simply said:

{“outcome”:”followed”}

Request:

Press enter or click to view image in full size
follow any user

Response:

Response when you follow the user

but here you don’t see any thing which make it Sensitive Info.

So i just replay the request [from the chrome console] by opening the Follow request in new tab. in the response it disclose all the information of the user profile.

URL Like https://XYZ.com/follow

Get Shivbihari Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Disclosed Information About User:

Email (it may be GitHub Or Twitter Email)
Secret Key
all the profile setting like their notification ,[i didn't test for the Payment section, but i am sure it will disclose the CARD information too]
Press enter or click to view image in full size
Email and Secret Key Disclose

but Wait i didn't know what i can do with this secret key. so i try to find the developer section of the site where I can get the information about the secret key[what we can do with this key].

Sadly they Don’t have any.

So i decided to Explore more features of site.

and in Setting Section i find that you can make an Organisation and their you can invite user by sharing the Secret Key.

Organisation member

Here We Go ..Now i know what i can do with that Secret Key.

but wait we have to cross_checked whether disclose Key Matched with Invitation Key.

See their is one more feature in site that , you can Follow the organisation . So From Previous We see that ,When-ever you follow any user ..It will disclose that user Information.

So i try the same And BINGO.!!

Press enter or click to view image in full size
Organisation Secret Key

It disclose the Secret Key of the Organisation Too.

So..Without Any Invitation We Able to Join the Organisation.

We Can Change the Organisation Settings,Post any Article , Invite any User to Organization[Off-course We have Secret Key], Delete Org. Too.

Quickly I Contact Them and they patched it within Hour.

That’s It for Now .Hope You Enjoy It.

Happy Hacking :)

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

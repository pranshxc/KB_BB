---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-15_this-is-how-i-was-able-to-see-private-archived-postsstories-of-users-on-instagra.md
original_filename: 2021-06-15_this-is-how-i-was-able-to-see-private-archived-postsstories-of-users-on-instagra.md
title: This is how I was able to see Private, Archived Posts/Stories of users on Instagram
  without following them
category: blogs
detected_topics:
- idor
- command-injection
- otp
- graphql
- supply-chain
tags:
- imported
- blogs
- idor
- command-injection
- otp
- graphql
- supply-chain
language: en
raw_sha256: 1847c91b360160ee8985ae84ac71992d765ac8a1b3760faa581bac4451e3f132
text_sha256: bbc98c0fa54381dd8f8b81d855b6e2da31c316a069944a89bab5fd45742951f0
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# This is how I was able to see Private, Archived Posts/Stories of users on Instagram without following them

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-15_this-is-how-i-was-able-to-see-private-archived-postsstories-of-users-on-instagra.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `1847c91b360160ee8985ae84ac71992d765ac8a1b3760faa581bac4451e3f132`
- Text SHA256: `bbc98c0fa54381dd8f8b81d855b6e2da31c316a069944a89bab5fd45742951f0`


## Content

---
title: "This is how I was able to see Private, Archived Posts/Stories of users on Instagram without following them"
url: "https://fartademayur.medium.com/this-is-how-i-was-able-to-see-private-archived-posts-stories-of-users-on-instagram-without-de70ca39165c"
authors: ["Mayur Fartade (@mayurfartade)"]
bugs: ["IDOR", "GraphQL"]
bounty: "30,000"
publication_date: "2021-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3575
scraped_via: "browseros"
---

# This is how I was able to see Private, Archived Posts/Stories of users on Instagram without following them

Top highlight

This is how I was able to see Private, Archived Posts/Stories of users on Instagram without following them
Mayur Fartade
Follow
3 min read
·
Jun 15, 2021

3.6K

18

I am Mayur Fartade from Maharashtra. This is my first bug in the Facebook Bug bounty program.

Description

This bug could have allowed a malicious user to view targeted media on Instagram. An attacker could have been able to see details of private/archived posts, stories, reels, IGTV without following the user using Media ID.
Details include like/comment/save count, display_url, image.uri, Facebook linked page(if any) and other.

Impact

Data of users can be read improperly. An attacker could able to regenerate valid CDN URL of archived stories & posts. Also by brute-forcing Media ID’s, the attacker could able to store the details about specific media and later filter which are private and archived.

Repro steps

Steps:

Obtain target’s post/reel/IGTV/story media id (By brute-forcing or other technique)
Send a POST request to https://i.instagram.com/api/v1/ads/graphql/
Parameters:
doc_id=[REDACTED]&query_params={“query_params”:{“access_token”:””,”id”:”[MEDIA_ID]”}}
Where [MEDIA_ID] is the media_id of any post/reel/IGTV/story.
doc_id is redacted.
In the response, display_url, save_count & other details of a particular media disclosed.
Press enter or click to view image in full size

After few days, I found another endpoint with doc_id=[REDACTED] which discloses the same information. access_token was passed through the POST request so when I tries to access media’s of different accounts I got data:null in the response.

Get Mayur Fartade’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps:

1. Send a POST request to https://i.instagram.com/api/v1/ads/graphql/
Parameters:
access_token=[REDACTED]&variables={“query_params”:{“access_token”:””,”id”:”[MEDIA_ID]”},”fetch_actor_id”:false}&server_timestamps=true&doc_id=[REDACTED]

Where [MEDIA_ID] is the media_id of any post/reel/IGTV/story.
doc_id is redacted.
Other parameters are not included.
access_token is valid Facebook access token.

Response

2. Then I changed the access_token to null and I got access to the information.
Also same endpoint is disclosing Facebook Page linked to a Instagram account but Facebook page & Instagram account link is public. You can see here
https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&view_all_page_id=PAGE_ID&search_type=page
Where PAGE_ID is the Facebook page ID.

Parameters:
access_token=null&variables={“query_params”:{“access_token”:””,”id”:”[MEDIA_ID]”},”fetch_actor_id”:false}&server_timestamps=true&doc_id=[REDACTED]

Response:

Fix

Instagram has changed the above endpoints.

Timeline

16 April 2021 : Report sent
19 April 2021 : Reply from Facebook Security Team — Need more info
19 April 2021 : Information Sent
22 April 2021 : Report Triaged
23 April 2021 : Found another endpoint disclosing the same info
29 April 2021 : Fixed
29 April 2021 : Vulnerability not completely patched. Sent the information to FB Security Team
…. some messages exchanged …
15 June 2021: Awarded $30000 bounty.

Press enter or click to view image in full size

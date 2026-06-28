---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-01_api-based-idor-to-leaking-private-ip-address-of-6000-businesses.md
original_filename: 2021-01-01_api-based-idor-to-leaking-private-ip-address-of-6000-businesses.md
title: API based IDOR to leaking Private IP address of 6000 businesses
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
language: en
raw_sha256: 8e717b59ca48c3abe47365fedc8d2b6f2aff57f8ca87dfae8735ad378b994801
text_sha256: 31683b6cf99bdc50c5154e553bde8ce4726c567fc3d316fa86f745fcdb3052a4
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# API based IDOR to leaking Private IP address of 6000 businesses

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-01_api-based-idor-to-leaking-private-ip-address-of-6000-businesses.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `8e717b59ca48c3abe47365fedc8d2b6f2aff57f8ca87dfae8735ad378b994801`
- Text SHA256: `31683b6cf99bdc50c5154e553bde8ce4726c567fc3d316fa86f745fcdb3052a4`


## Content

---
title: "API based IDOR to leaking Private IP address of 6000 businesses"
url: "https://rafi-ahamed.medium.com/api-based-idor-to-leaking-private-ip-address-of-6000-businesses-6bc085ac6a6f"
authors: ["Rafi Ahamed (Leonidas D. Ace)"]
bugs: ["IDOR"]
publication_date: "2021-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4034
scraped_via: "browseros"
---

# API based IDOR to leaking Private IP address of 6000 businesses

API based IDOR to leaking Private IP address of 6000 businesses
Rafi Ahamed (Leonidas D. Ace)
Follow
3 min read
·
Jan 1, 2021

387

1

Hello fellow researchers,

Myself, Rafi Ahamed. I am a Cyber Security Researcher from Bangladesh. I love to break security. Anyway, without further ado let’s get to today’s topic.

Get Rafi Ahamed (Leonidas D. Ace)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Before I start, I wanna thank Katie Paxton for her videos. I learned a lot about IDORs from her videos. I actually earned my whole year’s bounty target just form IDORs that I learned from her videos.

What is IDOR?

Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly.

What is an API?

API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

So, I was testing a NDA (Non-disclosure Agreement) program and I noticed that the Web Application had an option to view the access logs of the users. Seems so simple right?

I have a bad habit of turning on Interception and see every request that the browser sends to the server while browsing an web application. When I visited the same page again, I noticed that my access-logs were not being displayed even though other contents of the page already has load already. Then I noticed that the my Interception was on and there was an API request intercepted which was trying to fetch the access-logs of the users.

Press enter or click to view image in full size
The intercepted request

If you take a closer at the POST data, you will see that it has a UserID in it.

Press enter or click to view image in full size
User ID request

Then I sent the request to Intruder and Brute-forced the UserID and I got the access-logs of 6000 businesses.

The Dev’s reaction

I quickly reported the bug and the company fixed the bug within 48hours. I got a nice $4digit bounty for the bug.

Hope you guys enjoyed this one . PM me at Facebook, LinkedIn or Twitter anytime if you have any questions.

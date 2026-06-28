---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-01_stored-xss-in-bug-bounty.md
original_filename: 2018-11-01_stored-xss-in-bug-bounty.md
title: Stored XSS in Bug Bounty
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 55ee4469a8b5205f3d7bf18529e1b7d54feb95792422469617fb4b7b32f8e1c1
text_sha256: f6f9cac305aef0c33aac9bf0a7721d3bb78b2e81984993cdd65a24fff022ce6f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-01_stored-xss-in-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `55ee4469a8b5205f3d7bf18529e1b7d54feb95792422469617fb4b7b32f8e1c1`
- Text SHA256: `f6f9cac305aef0c33aac9bf0a7721d3bb78b2e81984993cdd65a24fff022ce6f`


## Content

---
title: "Stored XSS in Bug Bounty"
url: "https://medium.com/bugbountywriteup/stored-xss-in-bug-bounty-13c08e6f5636"
authors: ["KatsuragiCSL (@ZuuitterE)"]
bugs: ["Stored XSS"]
publication_date: "2018-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5615
scraped_via: "browseros"
---

# Stored XSS in Bug Bounty

Stored XSS in Bug Bounty
KatsuragiCSL
Follow
3 min read
·
Nov 1, 2018

176

Foreword

So I started to participate in bug bounty programs not so long before, and soon I found at least 2 places are vulnerable for stored XSS on a (quite big, I believe? They have many users and having some big banks and firms being their partner.) website which helps users to prepare their interviews.

Summary

The website’s dashboard shows meeting proposal submitted by users. XSS payloads can be added into the meeting proposal and trigger XSS on the browser of any users visiting the dashboard (OMG).

Press enter or click to view image in full size

When a logged in user visits the profile of a specific user(my testing account in this case), XSS triggered.

Press enter or click to view image in full size
How did I discover

After I found that this website is running a bug bounty program, first I look for any reflected XSS entry points like searching function on the website and improper error messages displayed. And I had no luck 😦 . But sometimes misfortune is a blessing in disguise.

Get KatsuragiCSL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After digging a while as a guest, I decided to signup an account to test other functionalities. Soon I found that I can leave something on the dashboard :

Press enter or click to view image in full size

Users can add meeting proposals and every proposal will display on the dashboard (for a while, it reminds me “welcome new members” function on some forums in the old days!). Hmm…so that means we can probably leave some text, such as proposal content, on the dashboard? Good place to test.

I found that a user can add comment for his/her meeting proposal. Let’s see will this simple script work:

Press enter or click to view image in full size

It turns out that it works! The comment is inserted in the HTML without any filtering, so now it keeps alerting ‘1’ every time we visit the dashboard (which is also the homepage of the website — if you are logged in)

Press enter or click to view image in full size

And I decided to explore more. There must be more place which displays user input without filtering. So I visited the profile editing function and I found something called headline (“test” right under the username “pk”)

Hmm…..So that means I can show customized text to every user who visits my profile. What if I insert javascript here?

Press enter or click to view image in full size

And again, the website did not filter this user input and insert it directly into HTML. So we got another stored XSS:

Press enter or click to view image in full size

That’s it. There must be more places vulnerable to XSS. I will keep track on it.

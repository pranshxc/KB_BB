---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-21_1000-p1-pii-disclosure-w-idor.md
original_filename: 2022-10-21_1000-p1-pii-disclosure-w-idor.md
title: '$1,000+ P1: PII Disclosure W/ IDOR'
category: documents
detected_topics:
- idor
- access-control
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- access-control
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: b2910083054cd677deb066a6b087eb7f83b6d94efc4c09db076def857b0355a0
text_sha256: 8b3b874c5f2c0aec98b1146171c40e9b9a34cd005f58187ee820c80f48272e86
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# $1,000+ P1: PII Disclosure W/ IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-21_1000-p1-pii-disclosure-w-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `b2910083054cd677deb066a6b087eb7f83b6d94efc4c09db076def857b0355a0`
- Text SHA256: `8b3b874c5f2c0aec98b1146171c40e9b9a34cd005f58187ee820c80f48272e86`


## Content

---
title: "$1,000+ P1: PII Disclosure W/ IDOR"
page_title: "$750+ Bug Bounties: PII Disclosure W/ IDOR | by Graham Zemel | The Gray Area"
url: "https://medium.com/the-gray-area/1-000-p1-pii-disclosure-w-idor-cb344c55d52e"
authors: ["Graham Zemel (@grahamzemel)"]
bugs: ["IDOR"]
publication_date: "2022-10-21"
added_date: "2022-10-23"
source: "pentester.land/writeups.json"
original_index: 2008
scraped_via: "browseros"
---

# $1,000+ P1: PII Disclosure W/ IDOR

$750+ Bug Bounties: PII Disclosure W/ IDOR
Graham Zemel
Follow
3 min read
·
Oct 21, 2022

31

1

TL;DR- A somewhat simple, everyday IDOR that lead to PII disclosure, and could possibly be used to further exploit the app.

Press enter or click to view image in full size

IDOR, or Insecure Direct Object Reference, is a type of access control bug. This means it can affect permissions of a user, like whether or not they have admin capabilities. IDOR vulnerabilities usually arise in relation to horizontal privilege escalation (to different user but same permissions), but on occasion exhibit vertical privilege escalation (to different user but higher permissions).

On the website we’re trying to hack, the url presented itself like this:

https://website.com/friend-request/?id=MjQzNDU%3D

Interesting. It’s got normal and secure aspects for just about everything. Up until that ‘id’ parameter, where there looks to be a URL encoded string. You’ll need to be a bit knowledgable in ciphers and encodings for the next part, completing CTFs taught me most of this.

I know this because of the %, which tells me that there was some sort of character that was not 0–9, a-z, or A-Z. It must be a special character, and so it is encoded in a special format.

URL Decode and Encode - Online
Decode from URL-encoded format or encode into it with various advanced options. Our site has an easy to use online tool…

www.urldecoder.org

Base64 Decode and Encode - Online
Decode from Base64 format or encode into it with various advanced options. Our site has an easy to use online tool to…

www.base64decode.org

Upon decoding the ‘MjQzNDU%3D’ value of the id parameter, we get ‘MjQzNDU=’. Well, what can we do with this? Based on the notation of one or more ‘=’ at the end, I can tell it may be using Base64 encoding. Plug it into my Base64 decoder, and we get a number! ‘MjQzNDU%3D’ url decoded → ‘MjQzNDU=’ base64 decoded → 24345.

Get Graham Zemel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This means that we’re associating the ID parameter with a number, putting it through a few different encodings, and then when the browser identifies the ID parameter it has been told how to decode the parameter into 24345.

To reverse to process, encode a different number. Use 24344, as it is the most likely to return a valid response. This is because logically, if there is a 24345 it is likely that a number needed to come before it in a sequential sequence. 24344 → base64 encoded ‘MjQzNDQ=’→ url encoded ‘MjQzNDQ%3D’. It look similar, but it’s actually changed the ‘U’ to a ‘Q’ before the ‘%3D’ (‘=’).

Paste it into the URL like so:

https://website.com/friend-request/?id=MjQzNDQ%3D

If you get a different response than your request using ‘MjQzNDU%3D’, there’s the IDOR! It’s low level and only shows a name and a little information on the HTML. Upon further examination though…

Remember, even if you find a decent bug bounty, try and find other vectors in order to get a bigger bounty payout.

We open up the code of the webpage, and what isn’t displayed on the HTML is all your user data that gets imported into the code of the website. First and last name, email address, phone number, and DOB are all visible inside client-side documents. Pretty significant stuff, at least in terms of OSINT type information.

Feel free to take a look at a script I programmed that works for me on this site. It will require revisions for anyone else using it, but it’s a simple 20 line parser program to make your job easier.

GitHub - grahamzemel/idorAutomation
You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com

Thanks for reading about finding IDORs and then chaining them to PII disclosure. If you’d like to read more about cybersecurity and programming, head over to The Gray Area. To read all of my articles (and everyone else’s on Medium), and support me, become a member using my link →

Join Medium with my referral link - Graham Zemel
Read all of Graham Zemel's posts, and any other post from thousands of Medium writers! You'll get full access to every…

grahamzemel.medium.com

Thanks!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-09_js-is-l0ve-.md
original_filename: 2020-10-09_js-is-l0ve-.md
title: JS is l0ve ❤️.
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- supply-chain
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- supply-chain
language: en
raw_sha256: 0df67c1c5316833ac8fc25a1a24fcc459a935cb989062697a4f1fefa47abe95f
text_sha256: 66c6f26bb6b497b71408ab522417d0f94d796cacd13d2803f921a2a514eb62dc
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# JS is l0ve ❤️.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-09_js-is-l0ve-.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `0df67c1c5316833ac8fc25a1a24fcc459a935cb989062697a4f1fefa47abe95f`
- Text SHA256: `66c6f26bb6b497b71408ab522417d0f94d796cacd13d2803f921a2a514eb62dc`


## Content

---
title: "JS is l0ve ❤️."
url: "https://medium.com/@sechunter/js-is-love-%EF%B8%8F-ca393a4849e9"
authors: ["Shivam Kamboj Dattana (@sechunt3r)"]
bugs: ["Information disclosure", "API key leakage"]
bounty: "5,000"
publication_date: "2020-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4205
scraped_via: "browseros"
---

# JS is l0ve ❤️.

Top highlight

JS is l0ve ❤️.
Shivam Kamboj Dattana
Follow
3 min read
·
Oct 9, 2020

503

1

Hello Everyone (Ram Ram Ji),

In this article, I will share one of my recent finding which is basically related to JS files. In which, i will tell you that how these JS files will help you to find a High Severity bugs.

If you are too lazy then I suggest you please use this tool i.e LinkFinder. It’s a tool to discover JS endpoints which is written by GerbenJavado. You can find it here, LinkFinder.

But, I personally prefer doing this stuff as manually. Because sometimes Automated tools don’t come out useful & they skipped out some important things. So, Let’s get Started.

Phase 1: Extracting JS Files & Beautify them :
Extract JS Files from source code of redacted.com
Bash I used for extracting .js files using waybackurl:

Extraction(){

waybackurl $1| grep -iE “\.js$” | uniq | sort

}

3. For Beautifying the JS Code I used js-beautify for pretty print js code (Quite Easy).

js-beautify <file.js> | tee -a <beautify.js>

You can install it from the given link below:

js-beautify
beautifier.io for node

www.npmjs.com

Phase 2: Searching for Patterns & Endpoints in JS files:
These are few patterns that i use while reading any JS file.

{api_key, api-key, apikey , api , access , AccessToken , gmap , gmaps , algolia_api_key , credentials, etc..}

2. Mapping of Endpoints that you found while reading the JS file. (Important one)

Get Shivam Kamboj Dattana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Most of the bug hunter’s skip the second point just because they can’t map out the correct endpoints which leads to high severity security bugs & loses their chances to getting High severity bugs.

NOTE: Read every path and try to mapping that endpoints until you succeed. Because JS file contains all the solutions related to mapping of endpoints.

Phase 3. Searching for Respective Documentation:
If you found any Rest-Api-Key then go for it’s Api Documentation (search on google about respective Api docs) & understand how it works & how you will use it to gain access of target system.
Keyhacks (This will help you for quick exploitation. Because this Repository contain’s 50+ Working Exploitable Endpoints of Different Rest-API-Keys).

Now, lets take a look at my disclosed report where i found a HelpShift-Rest-Api-Key using that i can modified the content of accounts & also i can delete the accounts of redacted.com

Steps to Reproduce (Acc. to Report):
Finding API Key:
Go to “https://redacted.com/dist/main.7be5c75d761008c183e6.min.js".
Analyzing the JS Code & you will found base64 value in HelfShiftApiKey parameter.
Press enter or click to view image in full size
HelpShift Rest API Key
Full Exploitation:
Go to “https://apidocs.helpshift.com" & Enter Required details that is needed.
You got Swagger API & Successfully Logged In. Now do whatever you want to do.

Note: You can also use curl command :

curl -X PUT — header ‘Content-Type: application/x-www-form-urlencoded’ — header ‘Accept: application/json’ — header ‘Authorization: Basic <base64_API_Key>’ -d ‘username=<username>’ ‘https://api-a.helpshift.com/v1/<domain_name>/users/<profile_id>'

you can get all profile id’s from getUser query.

Timeline:
Press enter or click to view image in full size
Bounty Rewarded

Sept 26, 2020 — Reported to private program
Sept 26, 2020 — Report Triaged
Sept 29, 2020 — Vulnerability Fixed
Oct 08, 2020 — Bounty of $5000 USD awarded

Special thanks to nullr3x for this (Big Bad Brother 🤑)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-01_stealing-0auth-token-mitm_2.md
original_filename: 2017-09-01_stealing-0auth-token-mitm_2.md
title: Stealing 0Auth Token (MITM)
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
language: en
raw_sha256: d2b3df2618e36917ac5226c5eb19454c2e1e67f42648e35c47e58c71d71bdca3
text_sha256: f75fd787940284e98cfdeaae3716ebb951fe27b54157c127948b94785a5a0d4e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing 0Auth Token (MITM)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-01_stealing-0auth-token-mitm_2.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d2b3df2618e36917ac5226c5eb19454c2e1e67f42648e35c47e58c71d71bdca3`
- Text SHA256: `f75fd787940284e98cfdeaae3716ebb951fe27b54157c127948b94785a5a0d4e`


## Content

---
title: "Stealing 0Auth Token (MITM)"
url: "https://medium.com/@arbazhussain/stealing-0auth-token-mitm-3eeab46e96cf"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["OAuth"]
publication_date: "2017-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6113
scraped_via: "browseros"
---

# Stealing 0Auth Token (MITM)

Stealing 0Auth Token (MITM)
Arbaz Hussain
Follow
2 min read
·
Sep 1, 2017

89

Severity: Low

Complexity: Medium

Weakness: partial 0Auth redirect_uri path

While Testing one of the Target on Hackerone ,I’m gonna call it as REDACTED.COM

Following Test Case Tried for OAuth redirect_uri :

https://www.thirdparty.com/oauth?client_id=35346545675475754&display=popup&redirect_uri=https://connect.REDACTED.com/auth/thirdparty/callback&response_type=code
Only Modified Thing’s Accepted at thridParty Site OAuth:
Scheme Protocols
Pre Subdomain Under *.connect.REDACTED.com

redirect_uri=<ANYTHING>://<ANYTHING>.connect.REDACTED.com

Possibilites Here:
I Need to find any Valid Subdomain under https://*.connect.REDACTED.COM to see what i can do further for exploitation.
So I Started Bruteforcing for any available Pre-Subdomain’s under connect subdomain and Came across

https://pages.connect.REDACTED.COM which is Nothing but hosted with Static Page .

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

~Tried Bruteforcing for Directories or Any other Open Redirect Possibilities But Failed~

Then i checked the Header For pages.connect.REDACTED.com and found HSTS Missing .

For Those Who Don’t Know what HSTS :

It Redirect from HTTP to HTTPS on the same host first , before making valid Request to HOST to ensure not to leak Anything in HTTP.
Final Exploit :
https://www.thirdparty.com/oauth?client_id=35346545675415754&display=popup&redirect_uri=http://pages.connect.REDACTED.com/&response_type=code
End up Making Request to :
http://pages.connect.REDACTED.com/?code=XXXXXXXXXXXXXXXXXX
Press enter or click to view image in full size
We have Leak the Token to HTTP on Invalid Path to keep the Token Usable.
Since Most of the Program Includes Man In Middle Attacks as OUT OF SCOPE.
Press enter or click to view image in full size
They have Fixed the Redirect_uri Path to Strict Path , And Reopened my Report and Marked it as Resolved for Detailed Explanation .
How to Avoid This Type of Bugs Situation:
Simply by Enforing HSTS Header :
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Here includeSubDomains; Tag will instruct to Serve all subdomains over HTTPS.
By Setting Strict Redirect_uri in OAuth Callbacks.

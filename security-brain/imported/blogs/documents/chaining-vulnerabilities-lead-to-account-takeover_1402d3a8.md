---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-01_chaining-vulnerabilities-lead-to-account-takeover.md
original_filename: 2020-12-01_chaining-vulnerabilities-lead-to-account-takeover.md
title: Chaining vulnerabilities lead to account takeover
category: documents
detected_topics:
- oauth
- rate-limit
- command-injection
- password-reset
tags:
- imported
- documents
- oauth
- rate-limit
- command-injection
- password-reset
language: en
raw_sha256: 1402d3a844d6b1cda0e56c43e934d2e65e6abca0c25eb14f4810f00ddc9d6068
text_sha256: 08cd8db2432b793a6a1ce0d5e6a91d1e2f349b6c54714a840bf18a0b79851b3b
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining vulnerabilities lead to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-01_chaining-vulnerabilities-lead-to-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, rate-limit, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `1402d3a844d6b1cda0e56c43e934d2e65e6abca0c25eb14f4810f00ddc9d6068`
- Text SHA256: `08cd8db2432b793a6a1ce0d5e6a91d1e2f349b6c54714a840bf18a0b79851b3b`


## Content

---
title: "Chaining vulnerabilities lead to account takeover"
page_title: "The Domino Effect: How Vulnerability Chains Lead to Account Takeover | by AHZ | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/chaining-vulnerabilities-lead-to-account-takeover-b583f0c10591"
authors: ["Ahmed (@ahzsec)"]
bugs: ["Account takeover", "Password reset", "Open redirect", "Lack of rate limiting"]
publication_date: "2020-12-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4098
scraped_via: "browseros"
---

# Chaining vulnerabilities lead to account takeover

The Domino Effect: How Vulnerability Chains Lead to Account Takeover
AHZ
Follow
4 min read
·
Dec 1, 2020

145

In this write-up, I will explain how I was able to chain five vulnerabilities that led to one link click account takeover.

Press enter or click to view image in full size

I discovered these vulnerabilities in a private program, I will name it: target.com, Before we keep going on explaining we should consider that these vulnerabilities occurred due to wrong application of the reset-password method via API and other internal functions.

W
hile I was doing recon in this target, I realized that this app uses different API’s to manage functionalities and methods, So I chose to test main methods such as sign-in and reset-password methods, I wasn’t able to recognize weird implementations in the sign-in method, So I directly tried to reset my account password via the reset-password method.

After resetting my account password, I realized that there is a weird “to” JSON parameter in the reset-password method request.

Press enter or click to view image in full size
Reset password request

And after checking my reset-password email, I was able to validate that this parameter is reflected in the reset-password link.

Press enter or click to view image in full size
Reset password email

I made further requests to make sure the parameter is reflected in the reset-password link, And I was right.

Press enter or click to view image in full size
Reset password email

I thought about escalating this into open-redirect which leads to the leakage of the reset-password secret code, So I tried Host header injection via Host header, Referer header, Origin header, and Host injection in “to” JSON parameter value, I wasn’t able to inject my own host, This means I should find internal open-redirect in the same target host which leads to the leakage of the reset-password secret code.

After testing some different methods and functionalities, I was able to identify two internal open-redirects in those endpoints:

https://target.com/api/otc/login?response_type=code&client_id=web&redirect_uri=https://host/
https://target.com/api/oidc/preauthorized?response_type=code&client_id=web&redirect_uri=https://host/

Those open-redirects leaked another secret code and it’s a vulnerability by itself, But I chose to escalate this into a one link click account takeover.

Get AHZ’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After injecting one of the open-redirects into the reset-password link via the “to” JSON parameter value.

Press enter or click to view image in full size
Reset password request

I was able to redirect the reset-password secret code and other secret code to my own host by one reset-password link click via the reset-password email.

Press enter or click to view image in full size
Reset password email

And here we are, The code in the path is the reset-password secret code, And the code in the query is the other secret code, All leaked into my host.

Press enter or click to view image in full size
My Host event

But wait, While I was testing the reset-password method, I was able to identify two other vulnerabilities, Those vulnerabilities made it obvious that I will be able to force the user to click on the poisoned link, Which leads to the user full account takeover.

The first vulnerability is the lack of rate-limiting in the reset-password method, I was able to send more than 2000 requests, Which will DDOS the user email, And force them to click on the poisoned reset-password link, Which leads to the leakage of the reset-password secret code.

The other vulnerability is the lack of invalidating the reset-password secret code, And therefore I was able to use the reset-password secret code as much as I want, And this secret code wouldn’t be invalidated, Even if the user requested another reset-password secret code and did reset their password, The reset-password secret code leaked to my host will be valid and usable.

Summary

I was able to chain five vulnerabilities: Two internal open-redirect, Resources injecting in the reset-password link, Lack of rate-limiting in the reset-password method, And lack of invalidating the reset-password secret code, I was able to escalate them into one link click account takeover.

Timeline

Report (Nov 23rd).
First response (Nov 24th).

Don’t forget to follow me on Twitter so you don’t miss my new writeups and articles. Thank you for reading my writeup, Appreciated.

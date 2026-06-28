---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-13_api-secret-key-leakage-leads-to-disclosure-of-employees-information.md
original_filename: 2020-03-13_api-secret-key-leakage-leads-to-disclosure-of-employees-information.md
title: API secret key Leakage leads to disclosure of Employee’s Information
category: documents
detected_topics:
- api-security
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- api-security
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: 00f9cb871edd794a1716a3968f92526fa309d364d738f52265be85a3088d41c8
text_sha256: b091e575ad4d3e928d608ca39af1dccb5a7c23894a0c882a5e9cb82ed2fb32db
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# API secret key Leakage leads to disclosure of Employee’s Information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-13_api-secret-key-leakage-leads-to-disclosure-of-employees-information.md
- Source Type: markdown
- Detected Topics: api-security, idor, command-injection, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `00f9cb871edd794a1716a3968f92526fa309d364d738f52265be85a3088d41c8`
- Text SHA256: `b091e575ad4d3e928d608ca39af1dccb5a7c23894a0c882a5e9cb82ed2fb32db`


## Content

---
title: "API secret key Leakage leads to disclosure of Employee’s Information"
url: "https://medium.com/@spade.com/api-secret-key-leakage-leads-to-disclosure-of-employees-information-5ca4ce17e1ce"
authors: ["Ace Candelario (@phspades)"]
bugs: ["Information disclosure"]
bounty: "2,000"
publication_date: "2020-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4714
scraped_via: "browseros"
---

# API secret key Leakage leads to disclosure of Employee’s Information

API secret key Leakage leads to disclosure of Employee’s Information
Ace Candelario
Follow
3 min read
·
Mar 13, 2020

150

4

Wednesday afternoon after watching Nahamsec with Th3G3nt3lman. I came up in my mind if I can find some sensitive stuff, and after some Google Dorking, I found one quite good site that can hack on and I will name it redacted.com.

SUBDOMAIN ENUMERATION

I used assetfinder to check the subdomains of redacted.com and pipe it with httprobe, get-title, and sort -u command. After a minute, the result comes out, and I noticed the first subdomain on the output.

quickie () { assetfinder -subs-only $1 | httprobe | get-title }

The subdomain ( smh.internal.redacted.com ) is very simple. It has a Sign-In tab of the employee, which redirects from google for authentication stuff.

RECON

So for you to enter that domain’s dashboard is you need a valid @redacted.com email or if you are an employee. Upon viewing the source, I noticed that there is only one JS file.

Press enter or click to view image in full size

I opened that ‘main.js’, and what made me surprise is, it is not minified like I always encounter from different sites. I always check for specific keywords like company name, domain (for hidden or internal subdomains), file extensions, or obvious API paths (for hidden endpoints), ‘secret’, ‘access[_|-]’, ‘access[k|t]’, ‘api[_|-]’, ‘[-|_]key’, ‘https:’, ‘http:’. And after searching for the keyword ‘redacted’ (company name).

Press enter or click to view image in full size
**Drum rolls**
PoC

I found a Base64 Authentication Credentials, and I found out that this is the exact API key of the bamboohr API key of the company. Their API documentation is easy to understand, and that is how I quickly verify that the API key that is leaking in the JS file is still working. With curl command, I can easily dump the employee list from the bamboohr.com API endpoint. Also, I can view, delete, remove, and update all existing employees, and it’s like I have a login of redacted.com to bamboohr.com, and below is the screenshot of example dump of employees.

Press enter or click to view image in full size

I submit it to the company, and in less than 24 hours, they already revoked the API key, which I confirm that the issue is fixed.

Tip: If you found a sensitive API Keys, secret, or something, make sure that you can use it or validate that this is not expired. Also, make sure that this API key is disclosing or leaking some credentials, updating, removing, deleting some kind. Always review their documentation so that you will not confuse on what to do.

And for looking at sensitive credentials, be creative about your keywords.

Timeline

February 5, 2020 — Report Submitted, and they replied within the day for acknowledgment, and they Triaged of the issue as well.

Get Ace Candelario’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

February 6, 2020 — Retest if the API is still working. Token already revoked.

February 11, 2020 — Reward $2,000 — High Severity issue

February 13, 2020 — Reward received.

*flies away*

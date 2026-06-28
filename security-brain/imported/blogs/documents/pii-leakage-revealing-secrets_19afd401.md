---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-25_pii-leakage-revealing-secrets.md
original_filename: 2021-06-25_pii-leakage-revealing-secrets.md
title: PII Leakage - Revealing Secrets
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 19afd40127c2702c074b15e5ec409a2b2c6d72508fc509a1c16da38ecd9d38e2
text_sha256: bf8c8f9a68eb1b6eb0c94d6397b236691138760cfd0e17048f43d9695d02b866
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# PII Leakage - Revealing Secrets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-25_pii-leakage-revealing-secrets.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `19afd40127c2702c074b15e5ec409a2b2c6d72508fc509a1c16da38ecd9d38e2`
- Text SHA256: `bf8c8f9a68eb1b6eb0c94d6397b236691138760cfd0e17048f43d9695d02b866`


## Content

---
title: "PII Leakage - Revealing Secrets"
url: "https://shahjerry33.medium.com/pii-leakage-revealing-secrets-8b617071bd1c"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Information disclosure"]
publication_date: "2021-06-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3546
scraped_via: "browseros"
---

# PII Leakage - Revealing Secrets

PII Leakage - Revealing Secrets
Jerry Shah (Jerry)
Follow
4 min read
·
Jun 24, 2021

562

4

Summary :

PII stands for Personally Identifiable Information. It is a kind of data which helps us to identify ones identity, for instance your full name, social security number, taxpayer identification number, driver’s license number, PAN card number, mobile number, address, etc. This kind of issues can breach the privacy of anyone on the internet.

Description :

I have found this issue on one of the private program of HackerOne where it was leaking customer name and pending invoice amount. At first I used google dorks to find the information and found some PDF reports but after in-depth search I noticed that those PDF information is public.

There was one thing common in all PDF reports, it has not mentioned to whom the particular report belongs and is there any pending amount or not as the information was regarding the bill payments. After enumerating sub-domains using google dorks I found a domain which was having the functionality of “Invoice No”, so I randomly entered an invoice number but it gave me an error.

I noticed that the PDF reports that I found were having the year and some random numbers (for eg. <year>–13659) as their name so I entered the number without year and got the result and I was able to see the customer names and there pending or paid amounts.

How I found this vulnerability ?

I used google dorks for checking invoice but found PDF reports which were already public
Press enter or click to view image in full size
Google Dork
Press enter or click to view image in full size
Google Dorks

2. After that I enumerated the subdomains and found “Invoice” functionality on one domain

Press enter or click to view image in full size
Subdomain
Press enter or click to view image in full size
Invoice Functionality

3. I entered random number but got an error

Press enter or click to view image in full size
Invalid Invoice

4. Then I opened the publicly available PDF report’s directory

Press enter or click to view image in full size
Publicly Available Reports
Press enter or click to view image in full size
Report Files with IDs

5. Then I entered an invoice number from the file name “13656” and got the result

Press enter or click to view image in full size
Invoice ID
Press enter or click to view image in full size
Result

6. Then I entered another invoice ids to check the results

Press enter or click to view image in full size
Result
Press enter or click to view image in full size
Result

Why it happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion the main reason for this kind of data leaks is improper security policy related to that data. When this type of data is uploaded on the server with access enabled from anywhere, they are indexed by web search crawlers. The indexing of this data was not avoided and necessary security policy was not set which led to this vulnerability.

Dorks Used :

site:target.gov “invoice” - for identifying invoices of users from one domain
site:*.target.gov - for enumerating subdomains
site:*.target.gov “invoice” - for identifying invoices of users from all domains

Impact :

This kind of data can breach the privacy of any user on the internet. An attacker can steal all the personal information of the victim using this vulnerability.

Mitigation :

Use robots.txt file

Example 1 :

User-agent: *

Disallow: /

This entry will not allow anyone to view the directories

Example 2 (My case) :

User-agent: *

Disallow: /reports/

This entry will not allow anyone to view /report/ directory

2. Use Meta Tag

Example 1 :

<META NAME=”ROBOTS” CONTENT=”NOINDEX, NOFOLLOW”>

It will prevent site scanning from web crawlers

Example 2 :

<META NAME=”GOOGLEBOT” CONTENT=”NOINDEX, NOFOLLOW”>

It will deny certain web crawl spiders to crawl the site

3. Do not use invoice ids as filename (My case)

Special Thanks To : Ravi Raj Rao

Press enter or click to view image in full size

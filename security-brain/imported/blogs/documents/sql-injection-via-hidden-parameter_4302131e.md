---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-24_sql-injection-via-hidden-parameter.md
original_filename: 2021-01-24_sql-injection-via-hidden-parameter.md
title: Sql Injection via hidden parameter
category: documents
detected_topics:
- sqli
- command-injection
- otp
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- otp
- api-security
language: en
raw_sha256: 4302131e454aee91bb0b919bf12663bff79a3f0588864eb1ad467825ab510ff0
text_sha256: 6d73a2d6ab944b9114bc22409e704fa1d04e55064878a436a747e1ae85d59114
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Sql Injection via hidden parameter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-24_sql-injection-via-hidden-parameter.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4302131e454aee91bb0b919bf12663bff79a3f0588864eb1ad467825ab510ff0`
- Text SHA256: `6d73a2d6ab944b9114bc22409e704fa1d04e55064878a436a747e1ae85d59114`


## Content

---
title: "Sql Injection via hidden parameter"
url: "https://hajarerutik9.medium.com/sql-injection-via-hidden-parameter-6da7699248fc"
authors: ["Rutvik Hajare (@HajareRutvik)"]
bugs: ["SQL injection"]
publication_date: "2021-01-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3972
scraped_via: "browseros"
---

# Sql Injection via hidden parameter

Sql Injection via hidden parameter
Rutvik
Follow
2 min read
·
Jan 24, 2021

273

3

Hello Everyone, I am Rutvik Hajare and I am new in the cyber field.This is my first write-up on one of critical findings. usually i hate blog writing but anyways.

SQL INJECTION:

Ok everyone knows what is sql injection.For those who are new in this field or don’t know what is it the Owasp has very good and short description about sql injection.

Without wasting time get to findings.

FINDINGS:

The target was the trading company let’s call it redacted.com, Without doing any kind of recon i simply register on target and it redirected to me on the dashboard. I refresh the page while running burp proxy for checking requests. After checking i found nothing interesting. But in web app their was another option where i can see/downloads my trading reports. I generate the example report and download it while running burp proxy.

The interesting part i found that for downloading report web app was requesting for fetching the bank id, user id and etc. After lot of request checking i came up on the following request.

Press enter or click to view image in full size

To access the resource of the above request i’ve to provide the token ( which i don’t have )

Get Rutvik’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i stated directory bruteforcing on the above endpoint and found the valid directory “bankacc”. But the response was empty. So i thought for finding hidden parameter and started param miner.

And found the status parameter. i tried to send some arbitrary value and boom !! i got the sql error.

Press enter or click to view image in full size

I quickly injected 1' AND sleep(5) — payload in status parameter and yay i got the 5 sec delay and confirmed the vulnerability.

Immediately I fired up sqlmap and pass this request to it ! Within a minute I dumped there all database :) !!

Press enter or click to view image in full size

Small tip never forget to try sql injection on hidden parameters.

Hope you like this ! and sorry for bad English :)

Thanks for reading !!

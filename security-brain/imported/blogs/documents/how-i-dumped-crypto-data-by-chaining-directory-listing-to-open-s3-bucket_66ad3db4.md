---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-05_how-i-dumped-crypto-data-by-chaining-directory-listing-to-open-s3-bucket.md
original_filename: 2020-02-05_how-i-dumped-crypto-data-by-chaining-directory-listing-to-open-s3-bucket.md
title: How, I dumped crypto data by chaining directory listing to open S3 Bucket
category: documents
detected_topics:
- information-disclosure
- cloud-security
- sso
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- information-disclosure
- cloud-security
- sso
- idor
- command-injection
- rate-limit
language: en
raw_sha256: 66ad3db432ba0b8df14e65e676b11d12dfa9f984a2919c996fa4ba5521a084a1
text_sha256: 385ca84c1628b62e6f54435842d29c803c9be5ec11d570311958ca9eeafbac40
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How, I dumped crypto data by chaining directory listing to open S3 Bucket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-05_how-i-dumped-crypto-data-by-chaining-directory-listing-to-open-s3-bucket.md
- Source Type: markdown
- Detected Topics: information-disclosure, cloud-security, sso, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `66ad3db432ba0b8df14e65e676b11d12dfa9f984a2919c996fa4ba5521a084a1`
- Text SHA256: `385ca84c1628b62e6f54435842d29c803c9be5ec11d570311958ca9eeafbac40`


## Content

---
title: "How, I dumped crypto data by chaining directory listing to open S3 Bucket"
url: "https://medium.com/@ddigvijay29/how-i-dumped-millions-of-crypto-currencies-accounts-28d388053713"
authors: ["Ddigvijay"]
bugs: ["AWS misconfiguration", "Directory listing", "Information disclosure"]
publication_date: "2020-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4791
scraped_via: "browseros"
---

# How, I dumped crypto data by chaining directory listing to open S3 Bucket

How, I dumped crypto data by chaining directory listing to open S3 Bucket
Digvijay
Follow
4 min read
·
Feb 5, 2020

70

1

Hello Everyone,

Today, I am gonna share one of my interesting private bug Bounty finding and very Unique s3 Bucket finding but before starting, Let’s just understand what is S3 Bucket and why it is very important.

What Is S3 Bucket:

An Amazon s3 (Simple Storage service) is a service from AWS (Amazon Web Services) which is like a cloud storage used to store file, folders, objects , etc. It is used to mostly store images, videos, PDFS, text files, and in rare cases to store source backups, credentials in plain text, etc. AWS can be used using the website or using the CLI (which we will be using).

Also, S3 Transfer Acceleration helps execute fast, secure transfers from a client to an S3 bucket via AWS edge locations.

What Is problem:

Problems with AWS S3 buckets’ permissions are as old as the service itself. I think that 2 the most known researches about this issue were performed by Skyhigh pointing that 7% of all S3 buckets are open and by Rapid7 pointing that even 17% are open.

How I found an open S3 Bucket:

There are multiple ways to find an associated Amazon s3 bucket of the target application, It can be found by brute forcing target using many tools.

During my recon using Amass subdomain enumeration tool, I found a domain https://dbXXX.xyz.org/, which seems very interesting to me and i started browsing it and found out that domain is vulnerable to Directory listing vulnerability and quickly, I started to check each directories but ended up with nothing because all mentioned directories were listing the data but i was unable to download it, not Sure why!!!!

I was totally frustrated because i wasted around 5–6 hour and started to looking around and was trying to find out bypasses by using various methods such curl command, Wget and other methods. But nothing worked!!!!

I was about to drop an idea to look around more in same subdomain but i just want to give a last chance to myself. During browsing domain, i noticed that a unique request i.e.

https://XXXXX-dbXXX-public.s3.eu-central-1.amazonaws.com

serving content to domain “https://dbXXX.xyz.org/” and data was nothing but the same data listed on directory, I understood that data validation is on domain “https://dbXXX.xyz.org/” side but not from S3 bucket side.

I quickly checked above domain “https://XXXXX-dbXXX-public.s3.eu-central-1.amazonaws.com”, as it was a S3 bucket and found out that the bucket is open to public and contain same data. which was present on . “https://dbXXX.xyz.org/”.

Get Digvijay’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, i understood completely, how application is behaving.

I, quickly open my terminal and fire S3 bucket commands, it was completely working fine and was able to browse the data and able to download data, not only download but i was able to list, cp and move the data, because the bucket was open to world and Open S3 Bucket is also a part of OWASP serverless top 10 and serving all the content to domain, i.e. https://dbXXX.xyz.org/.

Proof-of-concept:
Configure AWS CLI in your Windows/Linux/Mac machine.
Execute the below commands from the CLI

Listing a file — aws s3 ls s3://<xyz>-uploads/

Deleting a file — aws s3 rm s3://<xyz>-uploads/test.html

Press enter or click to view image in full size

Now I have so many zip file and after extraction of those zip files, i got DB config file containing so many information, few of them mentioned but can’t mentioned all because of data criticality.

DB Version and tables details
Meta data and table details

Hope you enjoyed my write!!!

Recommendation:

Review the bucket ACLs to verify WRITE and WRITE_ACP are only set on specific users, never on groups such as AllUsers or AuthenticatedUsers.
Take a look and see how you are uploading objects to S3 buckets and make sure you set the proper ACLs on both buckets and objects.

Note: Newly created Amazon S3 buckets and objects are private and protected by default.

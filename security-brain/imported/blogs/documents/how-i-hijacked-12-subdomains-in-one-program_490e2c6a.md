---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-17_how-i-hijacked-12-subdomains-in-one-program.md
original_filename: 2021-05-17_how-i-hijacked-12-subdomains-in-one-program.md
title: How i hijacked 12 Subdomains in one Program
category: documents
detected_topics:
- cloud-security
- command-injection
- supply-chain
tags:
- imported
- documents
- cloud-security
- command-injection
- supply-chain
language: en
raw_sha256: 490e2c6a9cedec946337d848b4da01e76afe107d69ea0b737b9e689da1d759b6
text_sha256: 0db3b36c7e28f8c025c92708eec13c2f4612dd2cfa02a2c6ea24fafd8b2332ed
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How i hijacked 12 Subdomains in one Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-17_how-i-hijacked-12-subdomains-in-one-program.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `490e2c6a9cedec946337d848b4da01e76afe107d69ea0b737b9e689da1d759b6`
- Text SHA256: `0db3b36c7e28f8c025c92708eec13c2f4612dd2cfa02a2c6ea24fafd8b2332ed`


## Content

---
title: "How i hijacked 12 Subdomains in one Program"
url: "https://nvk0x.medium.com/how-i-hijacked-12-subdomains-in-one-program-eea468bcd64f"
authors: ["Naveen kumawat (@nvk0x)"]
bugs: ["Subdomain takeover"]
publication_date: "2021-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3649
scraped_via: "browseros"
---

# How i hijacked 12 Subdomains in one Program

How i hijacked 12 Subdomains in one Program
Naveen kumawat
Follow
3 min read
·
May 17, 2021

118

5

Morning, 4th march, I woke up and cheked my phone.

There was a Facebook notification “8 new certificates for redacted.com or its subdomain were issued by ##########”

Press enter or click to view image in full size
Facebook notification for new certificates

I reported couple of bugs to this program three months before, I thought, i should start again reconnaissance on this program.

so i fired my recon script for redacted.com in my VPS.

I use a script that enumerate subdomains, resolve all of them using massdns and check status:NXDOMAIN of Dangling DNS records of subdomains pointing to Azure and ElasticBeanstalk services.

Press enter or click to view image in full size
Dangling DNS record of subdomain

After that i have to mannually check azure and ElasticBeanstalk instances are available to claim or not.

after 5–6 hours, i got a notification that “Recon completed for redacted.com”. I am starting to check vulnerable.txt file, there was 14 subdomains, that could be vulnerable.

Dangling DNS records of all the subdomains were pointing to AWS ElasticBeanstalk instances in us-east region.

Get Naveen kumawat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I went over to AWS Console at the us-east-1 region and started the environment creation process. There are Two types of Environment, We have to select web server environment.

Press enter or click to view image in full size
selecting environment type

Final step to check the subdomain is vulnerable if we are allowed to use the dangling DNS domain for our environment.

Press enter or click to view image in full size
using danging DNS domain

I checked all the instances one by one and I was shocked 11 out of 14 instances were available to claim.

I immediately claim all the instances and uploaded my POC page.

Press enter or click to view image in full size
uploading POC

We can also use code pipeline and connect it to ElasticBeanstalk instance for POC generation.

I confirmed all the subdomains was showing my POC page

Press enter or click to view image in full size

After 2 days, I got another notification “3 new certificates for redacted.com or its subdomain were issued by ##########”.

So I have quick recon script for quickly enunmerate subdomains, resolve the subdomains using massdns, check the subdomain takeovers and put the vulnerable subdomains to vulnerable.txt file.

I was able to takeover 1 another subdomain which were pointing to AWS ElasticBeanstalk in us-east-1 region.

Reported and earned $$$$

Drop a clap 👏, If you like this writeup and follow me on

Twitter: @nvk0x

Linkedin: @naveenkmt

Instagram: @nvk0x

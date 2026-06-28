---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-01_how-i-found-a-goldmine-but-got-no-gold_2.md
original_filename: 2022-06-01_how-i-found-a-goldmine-but-got-no-gold_2.md
title: How I found a GoldMine but got No Gold
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- api-security
- cloud-security
language: en
raw_sha256: 824bb2a481b1d11d2c91985748c381196c609baafe792537ea9dcc0bb3aa3851
text_sha256: 07bc903efe13e65eb922b0e9793b9c7e712a4e3ebeecdd1e161ed10e1d7678d4
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# How I found a GoldMine but got No Gold

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-01_how-i-found-a-goldmine-but-got-no-gold_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `824bb2a481b1d11d2c91985748c381196c609baafe792537ea9dcc0bb3aa3851`
- Text SHA256: `07bc903efe13e65eb922b0e9793b9c7e712a4e3ebeecdd1e161ed10e1d7678d4`


## Content

---
title: "How I found a GoldMine but got No Gold"
url: "https://medium.com/@mahitman1/how-i-found-a-goldmine-but-got-no-gold-e912a89fa522"
authors: ["Muhammad Abdullah"]
bugs: ["Old components with known vulnerabilities"]
publication_date: "2022-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2591
scraped_via: "browseros"
---

# How I found a GoldMine but got No Gold

How I found a GoldMine but got No Gold
Muhammad Abdullah
Follow
4 min read
·
Jun 2, 2022

88

2

Background:

In the last 2 months, I have been testing a private program with a Big Scope. It includes multiple Domains and Brands. Testing in a large scope is fun and rewarding. Devs are constantly developing things and many bugs and holes are left by them.

Vulnerability:

The issue I found was a vulnerable Nacos Instance which allowed attacker to create new users with admin privileges leading access to Nacos Management panel which disclosed a Goldmine of Backend Credentials.Including Database creds, OSS Bucket creds, Blob Storage Creds, and more.

Testing:

Recon is the key here. “The first rule of war and business is to know your enemy”.

Press enter or click to view image in full size

It's critical to understand about what is the development structure of the company. I observed that REDACTED was divided into divisions based on countries and then different teams for those countries. It opens more attacking areas.

As the standard procedure, I ran Subdomain Enumeration on the Redacted. I found many subdomains. One that caught my attention was

https://crm-stg.REDACTED.com

The reason is the default page of the page.

Press enter or click to view image in full size

What's a Baidu Search engine is doing as Default Page, Then I ran ffuf on the domain. The interesting endpoint I found was

https://crm-stg.REDACTED.com/nacos

Press enter or click to view image in full size
Nacos Login Page

I haven’t encountered Nacos Instance before so I did a quick google search.

“Nacos provides a set of simple and useful features enabling you to realize dynamic service discovery, service configuration, service metadata and traffic management.Nacos makes it easier and faster to construct, deliver and manage your microservices platform. It is the infrastructure that supports a service-centered modern application architecture with a microservices or cloud-native approach.”

Now above description is interesting as there is a possibility of disclosure of configuration files if somehow I get access to the management panel.

Get Muhammad Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While doing a search on any exploits related to Nacos I stumbled upon a great blog.

https://unsafe.sh/go-56947.html

So apparently in version <= 2.0 of Nacos , attacker can view the accounts registered on the instance but passwords are encrypted.

curl -XGET -H ‘User-agent: Nacos-Server’ ‘https://crm-stg.redacted.com/nacos/v1/auth/users?pageNo=1&pageSize=900'

It was possible to register new users on the platform.

curl -XPOST ‘https://crm-stg.REDACTED.com/nacos/v1/auth/users?username=testing&password=***REDACTED*** -H ‘User-Agent: Nacos-Server’

Via above I registered a new user “testing” and got access to the Nacos Panel.

Press enter or click to view image in full size

What I found next blew my mind as it was literally a GoldMine. There was a total of 59 Configurations files in the panel which was disclosing Database Creds, OSS bucket Keys, Blob Storage SAS tokens, and many more secret keys.

Following is just one example of the creds i.e Blob Storage SAS token which got me access to all the transactions done across all the stores of the company in the world.

Press enter or click to view image in full size
Blob SAS token Disclosure
Press enter or click to view image in full size
Azure Storage Explorer
Result:

In Bug Bounties always be prepared to receive the unexpected.

Press enter or click to view image in full size

Following is the reply I received from the company, disappointed as the issue was of P1 and got nothing for it. However, it was fun riding in the enemy territory xD

I hope the above write-up helps someone in finding similar issues in Nacos Instance.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-11_a-tale-of-a-full-business-takeover-red-team-diaries.md
original_filename: 2023-02-11_a-tale-of-a-full-business-takeover-red-team-diaries.md
title: A tale of a full Business Takeover — Red Team Diaries
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: fc4ca3cca4b311d5df0af19482317be2595ac54f0e19867db45d03faac4c2594
text_sha256: 48711bd96ea6747da6847a0a471ca114dcdc8150eda39da31beaa3e2295cbc64
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of a full Business Takeover — Red Team Diaries

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-11_a-tale-of-a-full-business-takeover-red-team-diaries.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `fc4ca3cca4b311d5df0af19482317be2595ac54f0e19867db45d03faac4c2594`
- Text SHA256: `48711bd96ea6747da6847a0a471ca114dcdc8150eda39da31beaa3e2295cbc64`


## Content

---
title: "A tale of a full Business Takeover — Red Team Diaries"
url: "https://infosecwriteups.com/a-tale-of-a-full-business-takeover-red-team-diaries-fe7a6a7acaef"
authors: ["Dhanesh Dodia - HeyDanny (@Dhanesh_Dodia)"]
bugs: ["MITM", "Credential stuffing", "Password spraying"]
publication_date: "2023-02-11"
added_date: "2023-02-11"
source: "pentester.land/writeups.json"
original_index: 1545
scraped_via: "browseros"
---

# A tale of a full Business Takeover — Red Team Diaries

A tale of a full Business Takeover — Red Team Diaries
Dhanesh Dodia - HeyDanny
Follow
5 min read
·
Feb 11, 2023

30

This story is going to be about a Red Team engagement conducted on a big fashion brand that is owned and ran by a small family in India. The parent company owned a lot of business divisions such as Jewellery, Cloths, Food and Supermarket stores. Long way short, the scope was to identify any potential way to steal customers PII, other business sensitive information or see if business downtime could be possible.

TL;DR

Collected clear-text credentials from data-breaches > Walked in as a regular customer > Checked out the premise > Created a fake WiFi phishing access point > Identified all areas where LAN ports were available > Started MITM + Scanned internal network > Performed password spray leveraging the credentials I collected and BOOM !!! > Identified multiple local admin account were using a same password > Added local admin backdoor account on multiple endpoints for persistence > Performed password spray and BOOM !!! found READ & WRITE access on multiple workstation shares> Found a MASTER password file that contained keys for the kingdom > Rest is History

RECON JOURNEY:

Before going to the store location, I initially started doing passive recon on the store to understand the premise and identify all areas of entry and exits. Simultaneously I also started collecting all available credentials from data breaches. I was given access to the guest area in their backend office where I connected my workstation with a LAN port available. At this point I noted their was no NAC authentication present, hence this way I directly became part of the main corporate network. I started performing MITM attacks, simultaneously I also performed a quick scans to understand the assets present in clients network inventory. At this point I noted that the network size was not that big and only 2 subnets were present. Also the network was kind of old school where Domain was not configured. Access to the shared drives were managed through WORKGROUPS.

Whats the difference between Domain and Workgroup?

Press enter or click to view image in full size
Difference between Domain and Workgroup

After having sufficient knowledge about the network I moved to the next phase to perform various test case. I had the knowledge of few usernames basis on the results of MITM attack which I initially performed. Also I had the knowledge of password patterns of the users based on the cleartext credentials I collected from data breaches.

ATTACKING PHASE

I started performing password spray across the network and BOOM !!! I found multiple endpoints which had a default local admin account configured with the same password. I created backdoor users with local admin privileges. During the other test case I identified a couple of machines running obsolete operating systems also vulnerable to the famous exploit EternalBlue, however I was not able to exploit and take remote access.

Also I identified other OT IOT and services were being used. These OT IOT devices sent sensors and actuators data in real time updates to a centralized monitoring system. This was useful to monitor activities of customers coming in and out of store, stores billing counter, product details, alerts raised against anyone leaving store without paying the bill, and other kinds of alerts. In this way the store was managed and all business operations were monitored. The main thing I noted here was that major portals to manage such IOT devices were running default passwords.

COLLECTION PHASE:

After holding administrative access I started looking for files with keywords that included — passwords, admin, credentials, confidential, etc. I collected the saved browser passwords.

Get Dhanesh Dodia - HeyDanny’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this stage as I had create backdoor accounts on multiple workstations, later I got the access to a shared WORKGROUP with full READ & WRITE access. At this stage it was possible for me to lockout entire business data that included a backups too and put all the business operations to stop working.

Press enter or click to view image in full size

After having access to multiple workstations, I jumped on identifying business sensitive data I had access to. So this time I did some Uber style data lookup and BOOM !!! I end up finding a master password excel file that contained keys to kingdom.

CONCLUSION:
I had local administrative access on multiple workstation.
I had administrative access on multiple IOT managing portals.
Identified RCE on multiple obsolete systems.
Admin access to multiple internet facing digital assets such as E-Commerce website, Bank account, Supply chain portal, G-Suite Admin, and many more.
Press enter or click to view image in full size
Press enter or click to view image in full size
EXFILTRATION:

I end up having access to 95% of the business sensitive data with READ & WRITE access. I discovered sensitive files that included purchase, sales, accounts, customer’s PII, passwords, UPI transactions records or any other sensitive file.

Press enter or click to view image in full size
FINAL CONCLUSION:

The network architecture was kind of old school and without no proper access control across the network. The stakeholders and employees of the company proved weak against basic security practice. Also the company did not have any good EDR / AV / SIEM tool to monitor sensitive endpoints where their all business data reside. A lot of changes in terms of people, process and technology was recommended to improve the security posture.

REFERENCE:

https://bitvijays.github.io/

https://www.geeksforgeeks.org/difference-between-domain-and-workgroup/

https://kylemistele.medium.com/impacket-deep-dives-vol-2-attacking-kerberos-922e8cdd472a

https://0xsp.com/offensive/red-team-cheatsheet/

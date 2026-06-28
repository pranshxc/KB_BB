---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-05_how-attacker-could-have-suffocated-the-company-staff.md
original_filename: 2022-06-05_how-attacker-could-have-suffocated-the-company-staff.md
title: How Attacker could have suffocated the company staff
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 151b35fe68a382bf6b9b8945b023c3f2a2255068fc5cfb891fca7bb3e2661e40
text_sha256: 4dc51dee34332639a41e5cc6e0919bd359a88e18a611ad734e1f50d9a8408176
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# How Attacker could have suffocated the company staff

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-05_how-attacker-could-have-suffocated-the-company-staff.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `151b35fe68a382bf6b9b8945b023c3f2a2255068fc5cfb891fca7bb3e2661e40`
- Text SHA256: `4dc51dee34332639a41e5cc6e0919bd359a88e18a611ad734e1f50d9a8408176`


## Content

---
title: "How Attacker could have suffocated the company staff"
url: "https://medium.com/@mahitman1/how-attacker-could-have-suffocated-the-company-staff-37a6b7192f12"
authors: ["Muhammad Abdullah"]
bugs: ["Default credentials"]
bounty: "1,400"
publication_date: "2022-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2587
scraped_via: "browseros"
---

# How Attacker could have suffocated the company staff

How Attacker could have suffocated the company staff
Muhammad Abdullah
Follow
2 min read
·
Jun 6, 2022

25

1

Background:

In the last 2 months, I have been testing a private program with a Big Scope. It includes multiple Domains and Brands. Testing in a large scope is fun and rewarding. Devs are constantly developing things and many bugs and holes are left by them.

Vulnerability:

Mitsubishi Electric provides an Air condition monitoring system for commercial use. Any connected air conditioning systems can be operated or monitored on the AE-200A/AE-50A/AE-200E/AE-50E’s LCD or the Web browser. Each AE-200A/AE-50A/EW-50A/AE-200E/AE-50E/EW-50E can control up to a total of 50 indoor units and other equipment. Functions like operating Air Conditions can be performed on the panel.

I found multiple instances running Mitsubishi Air Conditioning Control System with default logins being used.

Testing:

Nowadays companies are constantly deploying new technologies in their working environment. These especially include IOTs. To view the IOTs attack surface we have no other than SHODAN. Shodan is a great tool while looking for exposed IOTs.

Get Muhammad Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While my recon process, I did the following query on SHODAN.

org:”REDACTED”

The above query gave me a large set of results, which one can narrow down by using additional filters. One filter which I found useful was the product filter. I found 9 instances of the Mitsubishi Air Conditioning Control System. One thing we pentester do is to use default logins admin:admin or admin:password, but it's always good to consult the manual of the product too. I found the following credentials as default logins

Username: Administrator

Password=***REDACTED***

and Boom I was into panels. I had the ability to see all the ACs and Ventilations installed at various sites of the company.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Result:

The vulnerability was quickly triaged by the company and a bounty of 1400$ was awarded.

Takeaway:

Shodan is a great tool for recon, don’t neglect the IOTs of the company even if not listed on the scope.

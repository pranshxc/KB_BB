---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-26_obtained-a-bunch-of-sensitive-data-in-just-few-steps-hacking.md
original_filename: 2020-07-26_obtained-a-bunch-of-sensitive-data-in-just-few-steps-hacking.md
title: Obtained a bunch of sensitive data in just few steps — Hacking
category: documents
detected_topics:
- cloud-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- cloud-security
- command-injection
- information-disclosure
language: en
raw_sha256: c0135c37e71ee8aa0e6e144f7fd695eeca6320ab9846d25cabba3cfa5cd066bb
text_sha256: 11af69b3269017a78975a6776f22d016715f8efd2350dea8e61d15350954499b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Obtained a bunch of sensitive data in just few steps — Hacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-26_obtained-a-bunch-of-sensitive-data-in-just-few-steps-hacking.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `c0135c37e71ee8aa0e6e144f7fd695eeca6320ab9846d25cabba3cfa5cd066bb`
- Text SHA256: `11af69b3269017a78975a6776f22d016715f8efd2350dea8e61d15350954499b`


## Content

---
title: "Obtained a bunch of sensitive data in just few steps — Hacking"
url: "https://medium.com/@airlanggamurthi/obtained-a-bunch-of-sensitive-data-in-just-few-steps-hacking-1a474200a8c2"
authors: ["Airlangga Visnhu Murthi"]
bugs: ["AWS misconfiguration", "Information disclosure"]
bounty: "550"
publication_date: "2020-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4385
scraped_via: "browseros"
---

# Obtained a bunch of sensitive data in just few steps — Hacking

Obtained a bunch of sensitive data in just few steps — Hacking
Airlangga Visnhu Murthi
Follow
4 min read
·
Jul 26, 2020

8

1

During my hacking activity, I always try to learn the Apps business process / flow. I’ll start with the flow one by one. For example : if my target was an e-commerce platform, then I will start by seeking Bug/Vulnerability on “checkout flow — from choosing goods to be buy until it’s successfully checkout”. And if you can’t find Bugs/Vulnerability inside you can try it from outside “other services/3rd party apps used by the system”.

This is our main topics today “services called AWS”.

My target now was Company XYZ which is an e-commerce platform. After one week play around with their API “following their apps flow one by one” I still got nothing there. So i’ll try to find another ways, luckily for me i have friends that’s also my mentor. He told me if you find nothing inside and why not just try the outsides attack “I think their system using AWS”. Such a good clue yay!

let’s talk a bit about AWS.

Amazon Web Services (AWS) is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

Mostly, company uses this services to make it easier for them to store any user data without invest in real server. But, sometimes they always forget to setup this environment properly and it can cause unauthorized user get in to their Bucket/Folder/Cloud Storage.

Now, we’re started to test all of their AWS services. During my first scanning, I found 3 url that represent their cloud storage. I try to confirm to my mentor, have you test it ? and he said “yes”. Well okay, we try to look again maybe he missed something. After few hours finally I found one another url. Again, I try to confirm to my mentor and he said “I’ve never tested it”. finally yeay!

On AWS testing, basically we just need to hit certain url to see if its return all file stored or not. I try the manual method and it’s seems this url allow anyone to get in to their bucket. It will looks like this :

the URL return all file stored in the Bucket

So i fired up my tools and try to do penetration test to this url. You can easily dealing with AWS services using several command such as :

LS (to list all file stored) ->ex: aws s3 ls s3://infosec-startup.com/
CP (to download sensitive files from the s3 bucket to your system) ->ex: aws s3 cp s3://infosec-startup.com/credenitals.txt
RM (to remove/delete any contents from bucket) -> ex: aws s3 rm s3://infosec-startup.com/credenitals.txt
SYNC (to download all files to your system) -> ex: aws s3 sync s3://infosec-startup.com/
etc

I try to tested all command and it seems that the command allowed is only
(ls, cp, and sync).

Get Airlangga Visnhu Murthi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i just directly download whatever files inside and see if it’s contain sensitive data or not. and the result will looks like this :

Press enter or click to view image in full size
file downloaded

I just realized that all file stored is file without extension. So, i just try to open it using file opener such as pdf and boom result will looks like this :

Press enter or click to view image in full size

We just spotted the cloud storage with all invoice transaction (contains full name, email, user address, amount, phone number, etc) inside and we’re able to download it. “Critical”

Further more when i do sync command I’ll try to filter it using certain extension it returns more sensitive data “their monthly report sales data “ BOOM:

Press enter or click to view image in full size
AWS command to filter certain file
their monthly report data

It’s contains sales data per “channel, order type, region etc”:

after all of this we’re a white hat so Itry to report my findings to their management. Luckily they are fully aware about security vulnerability and they appreciate my work. Thanks for them !! really appreciate that !!

Here is my timeline :

25/03/2020 : Findings.
01/04/2020 : Create a report and submit it.
02/04/2020 : Management validate and confirmed.
15/04/2020 : Bug Fixed & re-test.
27/04/2020 : they award me $550.

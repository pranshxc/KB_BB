---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-22_how-i-was-able-to-get-critical-bug-on-google-by-get-full-access-on-google-cloud-.md
original_filename: 2023-01-22_how-i-was-able-to-get-critical-bug-on-google-by-get-full-access-on-google-cloud-.md
title: How i was able to get critical bug on google by get full access on [Google
  Cloud BI Hackathon]
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 825981c46a63a06a427492c40e9a9868f2b4ee41f80a8c0be9b09d45b8c0dc47
text_sha256: 211508931c592d7ff95e4979f992445505899429f8b69ebadcdb9c253df31819
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to get critical bug on google by get full access on [Google Cloud BI Hackathon]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-22_how-i-was-able-to-get-critical-bug-on-google-by-get-full-access-on-google-cloud-.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `825981c46a63a06a427492c40e9a9868f2b4ee41f80a8c0be9b09d45b8c0dc47`
- Text SHA256: `211508931c592d7ff95e4979f992445505899429f8b69ebadcdb9c253df31819`


## Content

---
title: "How i was able to get critical bug on google by get full access on [Google Cloud BI Hackathon]"
url: "https://orwaatyat.medium.com/how-i-was-able-to-get-critical-bug-on-google-by-get-full-access-on-google-cloud-bi-hackathon-f779fce29900"
authors: ["Orwa Atyat (@GodfatherOrwa)"]
programs: ["Google"]
bugs: ["Information disclosure"]
publication_date: "2023-01-22"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1637
scraped_via: "browseros"
---

# How i was able to get critical bug on google by get full access on [Google Cloud BI Hackathon]

Top highlight

How i was able to get critical bug on google by get full access on [Google Cloud BI Hackathon]
Orwa Atyat
Follow
3 min read
·
Jan 22, 2023

732

4

Hello Hunters , Hello Infosec Community

To Introduce My Self

My Name Orwa Atyat Full Time Bug Bounty Hunter

From Jordan
And Hunting On BugCrowd For Full Time With A Current Rank 54th & P1 Bugs Current Rank 4th
https://bugcrowd.com/orwagodfather
https://hackerone.com/mr-hakhak
https://twitter.com/GodfatherOrwa

google launch a event for developers Cloud BI Hackathon https://cloud.google.com/blog/products/data-analytics/join-the-google-cloud-bi-hackathon

Press enter or click to view image in full size
data experiences on Looker and Looker Studio

so i see thats its running on Looker Service

looker owned by google And I have a strong background on this application from previous testing and reports

Bug I Found it was

Credentials For Looker Instance On Github By [Google Employee] Led To Critical Access Perform All Api Calls For [Cloud BI Hackathon ]

i was able to find client id & client secret for looker All that instance led to critical Access and Info and perform all api calls on Cloud BI Hackathon event

Now theres 3 parts for this find

Part 1 this app running on looker service of login and looker owned by google

Part 2 access and impact here for Google Cloud Bl Hackathon

Part 3 Leak here was by google employee work of company X That also owned by Google

so now we have leaked data
by company X Google employee

in looker that owned by google

affect on google Cloud BI Hackathon

Leaked Data:
base_url=https://GoogleAPP.looker.com/:19999
client_id=XXXXXXXXXXXXXXXXX
client_secret=XXXXXXXXXXXX
POC:

normal POC it was for looker by usin this curl command

curl -d "client_id=ENTERHERE&client_secret=ENTERHERE" https://DOMAIN.looker.com:19999/login

but that command not working anymore when you try use it its give wrong credentials this happened after dropping lot of reports on looker leaks i was able to Validate data by another way

For looker Leaks testing POC

Install gazer By This Command In Linux

sudo gem install gazer

Next Step

Check If This Data Valid

Get Orwa Atyat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

gzr user me --host X.looker.com --client_id XXXXXXXXX --client_secret XXXXXXXXXX

if data valid you will have a response by

id|email|last_name|first_name|personal_space_id|home_space_id

and from here i was able to get this impact on Google Cloud Bl Hackathon

Access to all google employees info

Access to all google groups on Google Cloud Bl Hackathon

Add anyone for stuff

Remove anyone from stuff

Access to all logs there

Removing the complete dashboard

Impact:

An attacker has access to Credentials looker instance with which he can ==>list all the groups of looker ==>Access all the employees of each group ==>Access all the spaces,Dashbaords,Looks,Models including some of Google related ==>Dump all the available spaces,Dashbaords,Looks,Models ==>Delete/Remove available spaces,Dashbaords

Report sent

next day

Report TRIAGED Report ACCEPTED and Mark As P1/S1

With a very good bounty from google team

Press enter or click to view image in full size

BugBounty Tip Here

serch for leaks in

google groups , gitlab , github

target.looker.com sercet

and test credentials in gazer tool

i was able to get same find on google , uber , and about 9 private programs

and its mark directly as Critical

Thanks all

I Hope you guys have enjoyed the Reading

and hope you learn and found bugs and tweet by that for me that will make my happy

Stay safe dears

Orwa

https://twitter.com/GodfatherOrwa

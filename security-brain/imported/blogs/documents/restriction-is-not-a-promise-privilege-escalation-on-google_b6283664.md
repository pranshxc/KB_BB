---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-30_restriction-is-not-a-promise-privilege-escalation-on-google.md
original_filename: 2020-03-30_restriction-is-not-a-promise-privilege-escalation-on-google.md
title: 'Restriction is not a promise : Privilege escalation on Google.'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: b6283664da5d7d18d807854953a7f4a46801a6b68de4456e832713bca6237b9d
text_sha256: b873f7b76b9c7a06c3de3f46c2eae244911f06c6e56fc7e6fe7bb837292f8f56
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Restriction is not a promise : Privilege escalation on Google.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-30_restriction-is-not-a-promise-privilege-escalation-on-google.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b6283664da5d7d18d807854953a7f4a46801a6b68de4456e832713bca6237b9d`
- Text SHA256: `b873f7b76b9c7a06c3de3f46c2eae244911f06c6e56fc7e6fe7bb837292f8f56`


## Content

---
title: "Restriction is not a promise : Privilege escalation on Google."
page_title: "Restriction is not a promise: Privilege escalation on Google. | by Hariharan S | Medium"
url: "https://medium.com/@hariharan21/restriction-is-not-a-promise-privilege-escalation-on-google-2a35104ded5a"
authors: ["Hariharan.s (@DJHARIZ1)"]
programs: ["Google"]
bugs: ["Privilege escalation", "Broken authorization"]
bounty: "500"
publication_date: "2020-03-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4681
scraped_via: "browseros"
---

# Restriction is not a promise : Privilege escalation on Google.

Restriction is not a promise: Privilege escalation on Google.
Hariharan S
Follow
3 min read
·
Mar 30, 2020

166

Hi guys im Hariharan.s aka P5YCHO.

Since you guys loved my previous writeups I decided to share one of my recent findings on google data studio.

Press enter or click to view image in full size

What is google data studio?

Google Data Studio is a dashboard and reporting tool that is easy to use, customize, and share. It allows you to transform your data into appealing and informative reports for your audience.

Let's get to the Bug :)

While i was doing some recon on the working of the website and its functions. The report sharing feature caught my eye, It had two options…

Sharing options for editors and viewers

I got more information about the working of these functions from here. After learning what is does i decided to test whether i could bypass the restriction on the viewer side.

How these restriction works

If the Disable downloading, printing and copying for viewers is not turned on, Then there will be a option to create a copy of the report on the viewer side. Viewers click on the option a request is sent to create the copy of the report.
Option to create a copy

2. If the Disable downloading, printing and copying for viewers is turned on , Then the option to create a copy of the report is disabled on the viewer side. So no request to sent.

No option to create a copy

The Bug ;)

The first thing that came to my mind was a thought of “What if i”

So the idea here was to sent the “Create a copy of the report” request when the Disable downloading, printing and copying for viewers is turned on.

Get Hariharan S’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i created a report and captured the request of the “Create a copy of the report” option. The request was like :

POST u/0/copyReport/Report ID

Then i turned on Disable downloading, printing and copying for viewers for that report and replayed the same request above on the viewer side. And it happened, A copy of the report was created for the viewer.

Why You ask..

Because there was no validation on the server side for that request. And i was like ..

So i reported this issue to google and the issue was fixed on the below timeline:

Feb 5, 2020 :- Issue reported to google

Feb 7, 2020 :- Triaged as P2

Feb 10, 2020 :- Nice Catch

Feb 20, 2020 :- Accepted → Fixed

Feb 26, 2020:- Reward of $500 Issued and was added to their hall of fame

Press enter or click to view image in full size
Bounty :)

A Few things to say :

Think out of the box.
If you like my write up please do share so that others could learn something as well.
If you need to connect with me → Linkedin, Twitter, Facebook.

Hope you guys liked this write up and Happy Hunting :)

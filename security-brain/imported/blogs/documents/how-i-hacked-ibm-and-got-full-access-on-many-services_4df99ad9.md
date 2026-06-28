---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-16_how-i-hacked-ibm-and-got-full-access-on-many-services.md
original_filename: 2020-12-16_how-i-hacked-ibm-and-got-full-access-on-many-services.md
title: How I hacked IBM and got full access on many services?
category: documents
detected_topics:
- cloud-security
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 4df99ad9707d0447e9437204dfae5096a6e026127bf4a8e10e1295fb6301d60d
text_sha256: f9e2f594c0acaa70267b113b748228bf09bbefe5c6b50ebc1d33f16ede0f9034
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked IBM and got full access on many services?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-16_how-i-hacked-ibm-and-got-full-access-on-many-services.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4df99ad9707d0447e9437204dfae5096a6e026127bf4a8e10e1295fb6301d60d`
- Text SHA256: `f9e2f594c0acaa70267b113b748228bf09bbefe5c6b50ebc1d33f16ede0f9034`


## Content

---
title: "How I hacked IBM and got full access on many services?"
url: "https://medium.com/@3bodymo/how-i-hacked-ibm-and-got-full-access-on-many-services-ecf1dab4a054"
authors: ["Abdullah Mohamed (@3bodymo_)"]
programs: ["IBM"]
bugs: ["Information disclosure"]
publication_date: "2020-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4065
scraped_via: "browseros"
---

# How I hacked IBM and got full access on many services?

How I hacked IBM and got full access on many services?
Abdullah Abdelrazek
Follow
4 min read
·
Dec 15, 2020

282

1

Press enter or click to view image in full size

Hi
everyone, today I’m gonna talk about vulnerability that I found it in IBM that allowed me to get full access on many services.

At first, I opened shodan and searched for: Org:'ibm' tomcat

I browsed some servers, but I didn’t find anything interesting, until I found this server and let’s call it x.x.x.x, when I ran ffuf on it, I found “logs” as exposed endpoint. So I opened my browser to visit this endpoint, and as expected, I found more than one folder containing logs file for employees.

Press enter or click to view image in full size

I opened some files to make sure that they actually contain information worth reporting, and indeed there were some tokens and emails for IBM employees.
in fact, I checked the tokens but it were expired.
However, these files are not supposed to be exposed, so I opened hackerone to report this bug.

Less than a day later I received this reply..

Press enter or click to view image in full size

They want a real exploitation from data in logs to triage my report.

So I opened the logs file to read them, and the thing that intrigued me was that the logs file of the today were there, so I collected all the logs file in one txt file to grep all tokens and tried them.

Note: When I browsed through the logs file, I found admin control URL, and when I clicked on it, it showed me a message saying “There is a missing token”. Then I sent this request to the burp and added a header called “token” and I gave it a random value. Then the response changed to “The token is invalid or expired”. I wanted to say this point so that you know how to I make sure this tokens are working or not.

Press enter or click to view image in full size

One of them was valid and I was able to get some information about an employee.

Press enter or click to view image in full size

Also I found Credentials for AWS and Azure.

Press enter or click to view image in full size

Here I finished interim and I added an update to the report with what I found, and the report was triaged.

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that I decided to dive into the logs file to find something I could present on a separate report. And I found URL of Services DevOps Commander and when I opened it I tried to login with admin as username and pass as password, the surprise was that it was a true credential and I managed to get in.

Press enter or click to view image in full size

A small note: I later found that these credentials are being leaked in the logs file as clear text.

I browsed through the control panel, and I found credentials for services like gitlab, jenkins and many other services.

Press enter or click to view image in full size
Press enter or click to view image in full size

I stopped there and I report this bug in a separate report, and the report was triaged.

Thanks for your reading, I hope my story was useful.

Timeline:

[Jul 21, 2020] — Bug reported

[Jul 22, 2020] — Triaged

[Dec 08, 2020] — Bug fixed

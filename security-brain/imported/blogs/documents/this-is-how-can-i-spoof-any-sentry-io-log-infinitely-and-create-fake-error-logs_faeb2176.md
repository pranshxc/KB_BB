---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-09_this-is-how-can-i-spoof-any-sentryio-log-infinitely-and-create-fake-error-logs.md
original_filename: 2018-08-09_this-is-how-can-i-spoof-any-sentryio-log-infinitely-and-create-fake-error-logs.md
title: This is how can I spoof ANY Sentry.Io log infinitely and create fake error-logs
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: faeb217642d19cbf35b7f7ec8d1cd0f5754c89b0827d4b73a074d09d476bdda1
text_sha256: 5779d2875f572fdc719ec1bb3c1a351dd86c520844aca6a377f948c517316053
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# This is how can I spoof ANY Sentry.Io log infinitely and create fake error-logs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-09_this-is-how-can-i-spoof-any-sentryio-log-infinitely-and-create-fake-error-logs.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `faeb217642d19cbf35b7f7ec8d1cd0f5754c89b0827d4b73a074d09d476bdda1`
- Text SHA256: `5779d2875f572fdc719ec1bb3c1a351dd86c520844aca6a377f948c517316053`


## Content

---
title: "This is how can I spoof ANY Sentry.Io log infinitely and create fake error-logs"
url: "https://medium.com/@carlosdanielgiovanella/this-is-how-can-i-spoof-any-sentry-log-infinitely-and-create-fake-error-logs-74406367f4ba"
authors: ["Carlos Daniel Giovanella"]
programs: ["HackerOne", "Sentry"]
bugs: ["Content spoofing"]
publication_date: "2018-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5763
scraped_via: "browseros"
---

# This is how can I spoof ANY Sentry.Io log infinitely and create fake error-logs

This is how can I spoof ANY Sentry.Io log infinitely and create fake error-logs
Carlos Daniel Giovanella
Follow
3 min read
·
Aug 9, 2018

69

2

Ok. First of all: I reported this on HackerOne, 45 days ago. 10 days after, someone filled a duplicate. And they said if I believe this is a security issue, I should report to 
Sentry.io
. So, I did!

Press enter or click to view image in full size
Report details on HackerOne.
Why I still don’t accepted sentry answers, and, I hard believe that this is a security issue:

This vulnerability allows me to create infinitely error-logs, and spoof ANY DATA, title, description, tags, bug information, user, anything.
So, I can generate any log, any fake-error log, and I can cause to phishing sys-admins or the people who will read those logs.
I can also create fake error-logs, with fake id’s and titles, fake my ip, fake EVERYTHING. Every data. Without requests limit.

What is Sentry.Io?

Sentry.io is a software created to help people track their errors. But what is the use, if you can create fake error-logs, infinitely, with fake id’s?
Sentry.Io became useless. Just generate 10.000 fake reports with 50 different ip’s (I can do that in 5 minutes), and admins of system will believe and look for a error where don’t exist. And here, we can fish the fish. :]

Press enter or click to view image in full size
Here is a sentry screen, that the users see. We can spoof and change any data, infinitely, without problems.
Get Carlos Daniel Giovanella’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What I did?:

I contacted them! And said the details about the error:
1 — My first point: Parameter “event_id” isn’t is required. If you don’t fill it, the system generates it automatically for you. They specified the 128bit’s identifier (uuid4), and said that wasn’t was a security issue. They said that is the way the service should work.

Press enter or click to view image in full size

2 — I said that the noise logs can affect their customers. They said that it is not a security concern, and I’m just “causing an annoyance for a customer and generating some noisy logs”

Press enter or click to view image in full size

3 — Ok, after I was tired of trying to explain, I showed that my point was useless data and phishing potential. They said that they “understand”, but it’s not a security concern. They can’t stop this. And they can use tools to stop abuse (I sent 20.000 fake error logs to HackerOne in 10 minutes, great tools.), and if you have access to the API key, you can’t prevent this. (That sounds comforting)

Press enter or click to view image in full size

4 — My last try, was saying about the size of requests, which I can do requests of MB’s and… they said that their job is “Ingest data” and I “can’t hurt their service”. Even with the phishing potential.
What I did? Spoofed 100.000 error-logs to HackerOne with 1 IP Address within 10 minutes, with fake errors.

Final Words:

I’ll not say anything further. HackerOne said that I could share. And, i’m disclosing this because they said that this is not a security issue.
So, let’s fake error-logs and do phishing attacks, to prove them? (I’m just kidding, but I hope someone read this and fix it.)

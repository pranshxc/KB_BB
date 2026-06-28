---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-20_denial-of-servicedos-by-regex.md
original_filename: 2020-07-20_denial-of-servicedos-by-regex.md
title: Denial of Service(DoS) By Regex
category: documents
detected_topics:
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 62560f04cdb1b9546cf9d7a90e407896e0f40bbe20edb1f9228eed28bcd400d5
text_sha256: 6024368d09e50b32de538b1dd229c1f37c64590899cea732febbbb1812f26d5b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Denial of Service(DoS) By Regex

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-20_denial-of-servicedos-by-regex.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `62560f04cdb1b9546cf9d7a90e407896e0f40bbe20edb1f9228eed28bcd400d5`
- Text SHA256: `6024368d09e50b32de538b1dd229c1f37c64590899cea732febbbb1812f26d5b`


## Content

---
title: "Denial of Service(DoS) By Regex"
url: "https://medium.com/@ashikbhaskar94/denial-of-service-dos-by-regex-205536c8dcd0"
authors: ["Ashik B"]
bugs: ["DoS"]
publication_date: "2020-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4394
scraped_via: "browseros"
---

# Denial of Service(DoS) By Regex

Denial of Service(DoS) By Regex
Ashik
Follow
3 min read
·
Jul 20, 2020

56

1

Press enter or click to view image in full size

Hola everyone,

This is a small write-up on how I recently came across Regex DoS (a.k.a ReDoS) in a web application and how I exploited it.

Disclaimer: The pentest related data involved is confidential and hence I have not shared any actual screenshots/data.

The Radix

It all started with a search for Cross-Site Scripting in the web application which was being tested. I was checking for server-side validation, whether the server accepts special characters in the items/objects being created and if there was any encoding being done on the server side.

But there was a regex evaluation happening in the back-end. It wasn’t allowing any special characters. But alphanumeric characters were allowed. Any special characters entered in the string, were Unicode encoded in the response and rest of the string was evaluated by the regex expression. No matter what I tried, every bypass attempt lead me to a disappointing ‘400 Bad request’ or ‘422 Unprocessable Entity’ response.

The parameters I was fuzzing were located in a JSON body of a POST request. It looked something like below:

{ version: “3.111”, metadata: { name: “test+0”, type: “pipe”, repo: “sample” } }

When I appended a “+0” to the value of ‘name’ parameter, the server responded with ‘422 Unprocessable Entity’ and surprisingly, in the response body the application revealed a message which said something like below:

Status: Failure; <some_exception_here> test+0 should consist of lower case alphanumeric characters, ‘-’ or ‘.’, and must start and end with an alphanumeric character (e.g. ‘example.com’, regex used for validation is ‘[a-z0–9]([-a-z0–9]*[a-z0–9])?(.[a-z0–9]([-a-z0–9]*[a-z0–9])?)*’),field:metadata.name}]},code:422}

The Corroboration

This made two things clear:
1. Regex is being used to sanitize the input.
2. The parameter value is being reflected in the response as it is.

Get Ashik’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next thing I thought of was to check if there was any validation on the length/size of the parameter value and fortunately, there was none!

I generated a legit but lengthy parameter value and tried it. The server took longer than the usual time, around 3200ms to respond, i.e 3 seconds.

I increased its length ten times more and server responded in 7320ms, i.e 7 seconds.

These attempts made one thing concrete, that regardless of the size of value I provide, the server checks it against the regex expression and sends out the parameter value back in the response.

I increased the size of the value further and the character length was 2689780 in this attempt and the server took around 15–20 seconds to respond.

Press enter or click to view image in full size
The character count of the Huge value used.

The Final Showdown

This was the right way and time to bring the application down.
> Since Curl could not handle such a huge request, a bash script to attack did not work out.
> Since Burp Intruder was slow(due to huge request, again) and did not work out either.

The possible options to DoS this application were using Burp Turbo Intruder plugin or manually invoking the same/similar requests simultaneously.

Either way, I did send the huge request 30–40 times simultaneously and given below are the observations I made right after:
→ The response time increased to 30 |60 |90 seconds.
→ The server started responding with 500 Internal Server Error with some private IP disclosed in the body.
→ The application finally went down (bloop!)

Press enter or click to view image in full size
The server responds after 60-90 seconds when multiple such requests were hit simultaneously.
The server is down indicating a successful DoS attack.

The issue was reported as a High severity issue, although the attack was carried out by an authenticated user, as the DoS was persistent.

I hope this was insightful in some way or the other, for all you security enthusiasts out there!

Ciao, until next time!

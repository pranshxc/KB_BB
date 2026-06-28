---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-02_breaking-business-logic-part-27-1.md
original_filename: 2022-10-02_breaking-business-logic-part-27-1.md
title: 'Breaking Business Logic - Part: 2^7 = 1'
category: documents
detected_topics:
- race-condition
- command-injection
- business-logic
- api-security
- supply-chain
tags:
- imported
- documents
- race-condition
- command-injection
- business-logic
- api-security
- supply-chain
language: en
raw_sha256: 5a85dfdb8383c9264d2550f45342609e0ba2f50d3cd850ac46b5ddf03098606f
text_sha256: c12a8e2654dc9daa470bcbbfcaf49395aa8a94d44327cd33062c5fd3ec46bccb
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Business Logic - Part: 2^7 = 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-02_breaking-business-logic-part-27-1.md
- Source Type: markdown
- Detected Topics: race-condition, command-injection, business-logic, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `5a85dfdb8383c9264d2550f45342609e0ba2f50d3cd850ac46b5ddf03098606f`
- Text SHA256: `c12a8e2654dc9daa470bcbbfcaf49395aa8a94d44327cd33062c5fd3ec46bccb`


## Content

---
title: "Breaking Business Logic - Part: 2^7 = 1"
url: "https://thehemdeep.medium.com/breaking-business-logic-part-2-7-1-f19924b18783"
authors: ["Hemdeep Gamit"]
bugs: ["Race condition"]
publication_date: "2022-10-02"
added_date: "2022-10-04"
source: "pentester.land/writeups.json"
original_index: 2093
scraped_via: "browseros"
---

# Breaking Business Logic - Part: 2^7 = 1

Breaking Business Logic - Part: 2^7 = 1
Hemdeep Gamit
Follow
3 min read
·
Oct 2, 2022

161

1

Hello Hunters & Ninjas, In a very short span of time this article has been published because I’m a very consistent person in writing blogs as I’ve maintained my consistency in publishing a single write-ups after 4-5 months…LOL. Okay, Jokes apart. Today I’m going to write about Race Conditions which I found in one of the programs. Now without taking to much let’s just start with the attack.

Press enter or click to view image in full size

So this application allows its users to create a team, in which admin can create team and add others users in his team and perform developers related tasks.
A premium user has permission to add multiple teams but for free account, user allow to add only one team not more than that. If you try to add multiple times application denies to add more than one team.

So Now It’s time break the logic.

1. First off all I’ve click on add team form and fill up the form and click on submit.

2. I just intercepted the request and send to Turbo-Intruder and after that drop the current request.
Those who doesn’t aware about the Turbo Intruder, It’s an very awesome addon of burp-suite to perform Race-Condition and Brute-Forcing Tasks, this also available in Burp-Suite Community addition as well, you can use below screen-shot for your reference.

Press enter or click to view image in full size

3. Now the code for the Race Condition which is I’ve used is looks like below. You can find this anywhere on internet but I’ve paste code here for your convenience.

# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=30,
  requestsPerConnection=30,
  pipeline=False
  )
# the 'gate' argument blocks the final byte of each request until openGate is invoked
  for i in range(30):
  engine.queue(target.req, target.baseInput, gate='race1')
# wait until every 'race1' tagged request is ready
  # then send the final byte of each request
  # (this method is non-blocking, just like queue)
  engine.openGate('race1')
engine.complete(timeout=60)
def handleResponse(req, interesting):
  table.add(req)

4. The above code will create 30 concurrent request with the 30 concurrent connections, you can increase or decrease as per you convenience.

Get Hemdeep Gamit’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. To perform this type of race condition you have to add Payload in request header indicated as (%s), it will add extra header as payload. Which look like below.

Press enter or click to view image in full size

6. Now just click on attack and the output looks like below.

Press enter or click to view image in full size

The application has Race Condition. Application is not validate the resource state on multiple requests at the same time.

Okay that’s it for this articles guys the second one will come soon. Soon means soon not after the months . )

Thank you for reading guys, Keep Sharing your knowledge and experiences with the community and Stay Safe, Stay Happy and Be Positive.

Jai Hind, Vande Mataram. 🙏

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-05_business-logic-errors-must-vote.md
original_filename: 2021-09-05_business-logic-errors-must-vote.md
title: Business Logic Errors - Must Vote
category: documents
detected_topics:
- business-logic
- command-injection
tags:
- imported
- documents
- business-logic
- command-injection
language: en
raw_sha256: 685b15a991b260e348a945d1d9eead28fb533156a636e2072c69b2df24c50ba8
text_sha256: e7f919188779c9a07aff33b3552797fe6ef60c7405f6cef7e1b463dd236452d1
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Errors - Must Vote

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-05_business-logic-errors-must-vote.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `685b15a991b260e348a945d1d9eead28fb533156a636e2072c69b2df24c50ba8`
- Text SHA256: `e7f919188779c9a07aff33b3552797fe6ef60c7405f6cef7e1b463dd236452d1`


## Content

---
title: "Business Logic Errors - Must Vote"
url: "https://shahjerry33.medium.com/business-logic-errors-must-vote-68f642b60fb7"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Logic flaw"]
publication_date: "2021-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3345
scraped_via: "browseros"
---

# Business Logic Errors - Must Vote

Business Logic Errors - Must Vote
Jerry Shah (Jerry)
Follow
3 min read
·
Sep 4, 2021

438

Summary :

Business logic vulnerabilities are ways of using the legitimate processing flow of an application in a way that results in a negative consequence.

Description :

I found this vulnerability on a private program of Bugcrowd where there was a comment section. I noticed that whenever any person makes a comment he/she gets an option to vote but only one time, either negative or positive. After reviewing the request using burp I found a vote parameter which was having a voting value and the same value was reflected in response. I changed the value of vote parameter from 1 to 1000 and it also got changed in the response. For double verification I reloaded the page and the value was still 1000. I reported the vulnerability but unfortunately it was a duplicate.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I made a normal comment and found that it had a voting option
Press enter or click to view image in full size
Comment

2. Then I normally voted up and it was working perfectly

Press enter or click to view image in full size
Voted Up

3. Then I voted down to check whether it is working or not and it was working perfectly

Press enter or click to view image in full size
Voted Down

4. In the next step, I voted up and intercepted the request using burp and changed the value of vote parameter from 1 to 1000 and also used the option Do intercept > Response to this request to check the server response

Press enter or click to view image in full size
Manipulated Votes - Request
Press enter or click to view image in full size
Manipulated Votes - Response

5. For double check I reloaded the page and still the votes were 1000

Press enter or click to view image in full size
1000 Votes

6. In the next step, I voted down and intercepted the request using burp and changed the value of vote parameter to -1000 and also used the option Do intercept > Response to this request to check the server response

Press enter or click to view image in full size
Manipulated Vote - Request
Press enter or click to view image in full size
Manipulated Votes - Response

7. For double check I reloaded the page again and still the votes were -1000

Press enter or click to view image in full size
-1000 Votes

Why it happened ?

In my opinion,

The the validation check for voting was only done on the client side and not at the server side, so it was easy to manipulate the request by sending 1000 votes by a single user instead of only 1 vote.

Impact :

All the users can vote multiple times, abusing the voting system which will affect the voting results.

Mitigation :

Every user input should be validated on client side as well as server side to mitigate this type of issues.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-20_how-i-could-delete-facebook-ask-for-recommendations-posts-place-objects-in-comme_2.md
original_filename: 2019-11-20_how-i-could-delete-facebook-ask-for-recommendations-posts-place-objects-in-comme_2.md
title: How I could delete Facebook Ask for Recommendations post’s place objects in
  comments
category: blogs
detected_topics:
- idor
- command-injection
tags:
- imported
- blogs
- idor
- command-injection
language: en
raw_sha256: 36cee65246e6bc17f717fa7dba829931c80cca9ac55607e78e11d7509f73558e
text_sha256: 646eef6d44bd8797ce417f0fa718a407e897cf5ed3e68cab08c800332750be23
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I could delete Facebook Ask for Recommendations post’s place objects in comments

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-20_how-i-could-delete-facebook-ask-for-recommendations-posts-place-objects-in-comme_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `36cee65246e6bc17f717fa7dba829931c80cca9ac55607e78e11d7509f73558e`
- Text SHA256: `646eef6d44bd8797ce417f0fa718a407e897cf5ed3e68cab08c800332750be23`


## Content

---
title: "How I could delete Facebook Ask for Recommendations post’s place objects in comments"
url: "https://medium.com/@rajasudhakar/how-i-could-delete-facebook-ask-for-recommendations-posts-place-objects-in-comments-b7c9bcdf1c92"
authors: ["Raja Sudhakar (@Rajasudhakar)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2019-11-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4930
scraped_via: "browseros"
---

# How I could delete Facebook Ask for Recommendations post’s place objects in comments

How I could delete Facebook Ask for Recommendations post’s place objects in comments
Raja Sudhakar
Follow
2 min read
·
Nov 19, 2019

86

Press enter or click to view image in full size

Summary:

This blog post is about an Insecure direct object reference vulnerability in Facebook Ask for Recommendations post. using attacker could have remove place object card in comments.

Vulnerability Type :

IDOR (Insecure Direct Object References)

Reference: https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References

Steps to reproduce:

1) Visit any Victim’s Facebook Recommendation post and find out place objects in comments.

2) Copy victim place object’s comment_id and rec_id (which is available in inspect).

3) Now goto your recommendation post’s place objects.

4) Now on the right corner click on “Delete” option.

5) Now before posting make sure Burp Suite’s Interceptor is turned on to capture the request.

Get Raja Sudhakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Click on “Delete” now, you will see below kind of request in Burp suite:

POST 
/async/place_list/remove_rec/?comment_fbid=1119570281585744&is_spotlight=false&map_state=1&rec_id=110535478973670&rec_type=place&av=100022637353520 HTTP/1.1
Host: www.facebook.com
Connection: close
Content-Length: 668
Origin: https://www.facebook.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0)

6) Now change the comment_id parameter value to victim’s comment_id and Forward the request.

7) Then now change rec_id parameter value to victim’s rec_id and Forward the request.

8) Done.

Video POC:

Timeline:

September 20, 2018 — Initial Report

September 20, 2018 — Report Triaged

October 05, 2018 — Vulnerability Fixed By Facebook

October 09, 2018 — Fixed Confirmed

October 10, 2018 — Bounty awarded by Facebook

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-26_how-i-got-easy-for-sql-injection-bug_2.md
original_filename: 2020-11-26_how-i-got-easy-for-sql-injection-bug_2.md
title: How i got easy $$$ for SQL Injection Bug
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 530eed48a7b82d1b62f751031216bdca8853d5b870e49d30166577c6d9c67bd7
text_sha256: 7613cc87ffec76d1c08b6a7c9d367d437eb0dc49e9888fdd4bf7e59f03b8d823
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How i got easy $$$ for SQL Injection Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-26_how-i-got-easy-for-sql-injection-bug_2.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `530eed48a7b82d1b62f751031216bdca8853d5b870e49d30166577c6d9c67bd7`
- Text SHA256: `7613cc87ffec76d1c08b6a7c9d367d437eb0dc49e9888fdd4bf7e59f03b8d823`


## Content

---
title: "How i got easy $$$ for SQL Injection Bug"
page_title: "Medium"
url: "https://rafipiun.medium.com/how-i-got-easy-for-sql-injection-bug-7ff622236e4c"
authors: ["Rafi Andhika Galuh"]
bugs: ["SQL injection"]
publication_date: "2020-11-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4105
scraped_via: "browseros"
---

# How i got easy $$$ for SQL Injection Bug

How i got easy $$$ for SQL Injection Bug
Rafi Andhika Galuh
3 min read
·
Nov 27, 2020

--

4

1

Press enter or click to view image in full size

Hello guys,
This is my first Write Up and i want to share about “How i got easy $$$ for SQL Injection Bug”

Note : call the target as Redacted.com

Tools : Burpsuite

Get Rafi Andhika Galuh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proof of Concept :

1. Sign up for a new account

2. Follow the instruction, and then i got this page :

Press enter or click to view image in full size

3. So i got the url like this :
https://redacted.com/user/activation/xxx/1325589
1325589 is my user id. And the i try to add single quote ( ‘ ) to try if the website has SQL Injection or not.
but it didn’t :(

4. But if you see the page again, the page has the Button “Resend Activation Link” so now I turn on my intercept and click the Button.

5. I got the request and the response like this :

Press enter or click to view image in full size

The response is redirected me to :
https://redacted.com/user/resendactivation/xxx/1325589/?smsg=green

6. So i try to modified the request with added a single quote like this :
https://redacted.com/resend/activation/1325589'
and this is the response :

Press enter or click to view image in full size

i got redirect to :
https://redacted.com/signup_page/xxx

7. Now i try to edit the request and added --+- and the response like this :

Press enter or click to view image in full size

the response is turn into the default request so i can confirm maybe its a SQL Inejction :D

8. Now i try to edit the response and added “order+by+5” like this :

Press enter or click to view image in full size

The response is turn to False condition, so the column doesn’t reach 5

9. Try “order+by+4” → Still False

10. Try “order+by+3” → True !!! :D

Press enter or click to view image in full size

so it meaning the column is till number 3

11. So now i try to “union select” like this :

Press enter or click to view image in full size

If you see the response i got redirect to :
https://www.redacted.com/user/resendactivation/xxx/3/?smsg=green

Yeah !!! I got the number 3.

12. Now try to inject a sql query on number 3, like this:

Press enter or click to view image in full size

BOOM !!! I got the user.

13. Now try to got the database name and the version, like this:

Press enter or click to view image in full size

Reward : $$$

That’s it for this write up from me, i hope you enjoying it.
And sorry for my bad English :( ,
See you again in the next story

Follow me on :

Linkedin
Facebook
Instagram
and also Subscribe my Youtube Channel :
Youtube

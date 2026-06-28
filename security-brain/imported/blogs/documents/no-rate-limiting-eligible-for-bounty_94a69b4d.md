---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-03_no-rate-limiting-eligible-for-bounty.md
original_filename: 2019-08-03_no-rate-limiting-eligible-for-bounty.md
title: No Rate limiting eligible for bounty ?
category: documents
detected_topics:
- idor
- rate-limit
- command-injection
- password-reset
- csrf
tags:
- imported
- documents
- idor
- rate-limit
- command-injection
- password-reset
- csrf
language: en
raw_sha256: 94a69b4d251b3788a6c46677a7789f0cdfc163e065cb99420202aceb6fcdfbe1
text_sha256: 247ff31cff98bd4c80eef6045368bfe3ce547447e9591e1b7660770a85740bf8
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# No Rate limiting eligible for bounty ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-03_no-rate-limiting-eligible-for-bounty.md
- Source Type: markdown
- Detected Topics: idor, rate-limit, command-injection, password-reset, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `94a69b4d251b3788a6c46677a7789f0cdfc163e065cb99420202aceb6fcdfbe1`
- Text SHA256: `247ff31cff98bd4c80eef6045368bfe3ce547447e9591e1b7660770a85740bf8`


## Content

---
title: "No Rate limiting eligible for bounty ?"
page_title: "No Rate limiting eligible for bounty ? – Smaran Chand"
url: "https://smaranchand.com.np/2019/08/no-rate-limiting-eligible-for-bounty"
final_url: "https://smaranchand.com.np/2019/08/no-rate-limiting-eligible-for-bounty/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["Lack of rate limiting"]
publication_date: "2019-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5102
---

[August 3, 2019](https://smaranchand.com.np/2019/08/no-rate-limiting-eligible-for-bounty/)

# No Rate limiting eligible for bounty ?

I have seen most of the peoples searching for No rate limiting issue at endpoints like password reset resulting into mass email triggering, SMS triggering or sometimes abusing it for other common activities.

When it comes regarding No rate limiting issue in API or web endpoints I must say “**All you need to do is make an impact** “. And also i couldn’t forget the issue one of my talented friend (Name Removed) 😀 found in one of the ISP site resulting to free internet usage for a lifetime. That was a nice issue regarding No Rate Limiting/Security Misconfiguration.

Although I am not happy writing this blog post because the same endpoint had Insecure Direct Object Reference(IDOR) issue which got duplicate. I wanted to let you know all peoples that how I used my common sense and got the bounty.

I found an IDOR at one of the public programs in bugrowd with which I was able to see the personal information as well as cancel some of their pending operations. 
  
  
  POST /api/action/cancelAction HTTP/1.1
  Host: sub.xyzcompany.com
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0
  Accept: application/json, text/javascript, */*; q=0.01
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Content-Length: 98
  Connection: close
  Referer: https://sub.xyzcompany.com/page/login/app
  Cookie: __cfduid=peepdipeepdibaambaam; REMEMBER_ME_COOKIE=somebiscuitshere
  ActionId=25296&&csrf=somethinghere&apiClient=WEB

Descending the value of ActionId to valid numeric id canceled the pending actions from respective account having the ActionID. So the bug confirmed and i reported it, unfortunately, it got duplicate after they triaged it

![](https://smaranchand.com.np/wp-content/uploads/2019/08/Screen-Shot-2019-08-03-at-9.38.36-PM.png)This hurts bro.

And then I thought to explore some more information so I sent the API request to intruder tab and discovered that I was able to brute the requests at the same time. 

I filtered the response of the request by using some regex for printing useful information only. The No Rate Limiting actually led to the disclosure of the user’s information in mass. It also resulted in a mass number of emails to the individual’s mailbox having the same ActionID as reference.

![](https://smaranchand.com.np/wp-content/uploads/2019/08/Screen-Shot-2019-08-03-at-9.26.09-PM.png)Bruting the requests.

All i meant to say that the main root for disclosing information of mass users was no ratelimit issue due the absence of Rate Limiting I was able to perform two actions at the same time which were canceling others pending operations and spam mass number of emails to any individuals inbox.

![](https://smaranchand.com.np/wp-content/uploads/2019/08/Screen-Shot-2019-08-03-at-9.53.06-PM.png)Emails arrived. ![](https://smaranchand.com.np/wp-content/uploads/2019/08/Untitled-Diagram-4.png)Total Scenario

They rewarded me an amount with which I can pay my bills for a month. 

![](https://smaranchand.com.np/wp-content/uploads/2019/08/Screen-Shot-2019-08-03-at-11.18.40-PM.png)

Do share if this post helped you.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)

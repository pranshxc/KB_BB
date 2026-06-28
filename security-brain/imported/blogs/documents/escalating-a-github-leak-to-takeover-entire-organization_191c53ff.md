---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-18_escalating-a-github-leak-to-takeover-entire-organization.md
original_filename: 2020-08-18_escalating-a-github-leak-to-takeover-entire-organization.md
title: Escalating a GitHub leak to takeover entire organization
category: documents
detected_topics:
- automation-abuse
- command-injection
- mfa
- information-disclosure
tags:
- imported
- documents
- automation-abuse
- command-injection
- mfa
- information-disclosure
language: en
raw_sha256: 191c53ffd59e50a99b76e1eb6a061ce456aec63ca4f4f0a0b857a52fe66bbdae
text_sha256: 3c8f71a5b7947295e03e1dbd48b0b44e7b4c5c64eab23eec02127c7c6e18703b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Escalating a GitHub leak to takeover entire organization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-18_escalating-a-github-leak-to-takeover-entire-organization.md
- Source Type: markdown
- Detected Topics: automation-abuse, command-injection, mfa, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `191c53ffd59e50a99b76e1eb6a061ce456aec63ca4f4f0a0b857a52fe66bbdae`
- Text SHA256: `3c8f71a5b7947295e03e1dbd48b0b44e7b4c5c64eab23eec02127c7c6e18703b`


## Content

---
title: "Escalating a GitHub leak to takeover entire organization"
page_title: "Shashank's Security Blog: Escalating a GitHub leak to takeover entire organization"
url: "https://blog.shashank.co/2020/08/escalating-github-leak-to-takeover.html"
final_url: "https://blog.shashank.co/2020/08/escalating-github-leak-to-takeover.html"
authors: ["Shashank (@cyberboyIndia)"]
bugs: ["Information disclosure"]
bounty: "4,000"
publication_date: "2020-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4306
---

I was hunting on a private program. One of the common things I do is look for leaked credentials on Github. I give special attention to deleted files. Because many people are not aware that just deleting a file doesn't remove it from your repository. 

  

One of the YAML files caught my attention. 

  

> data:  
>  matrixbot-username: {{ .Values.matrixbot.username | default "some_leaked_username" | b64enc }}  
>  matrixbot-password=***REDACTED*** .Values.matrixbot.password | default "some_leaked_password" | b64enc }}

  

Initially, I had no clue what were these passwords. So I started searching about the matrix thing.  
I stumbled upon https://matrix.org and realized this is a communication client. 

  

> Matrix is an open-source project that publishes the Matrix open standard for secure, decentralized, real-time communication, and its Apache-licensed reference implementations.

  

So, here's the plan. Find the client and try to log in and see if I was lucky enough. I found a web-based client at https://app.element.io/#/login attempted to log in, but it didn't work. 

  

I almost gave up, but then I noticed that there is an option to have a self-hosted server. And it somehow summed up my theory that a DevOps person might have used it for some automation, so there was a YAML file, and hence it should be self-hosted.

  

Now I had to find the hosted server. And the most obvious step was to look for subdomains.  
There were multiple subdomains, and, one that caught my attention was matrix.thewebsite.com

  

Visting the URL showed this, which was very convincing I am at the right place. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAYKNpdu66ZfMj8944IRS3-EQvBt6RUGNs8muAMY5Gz6Xpr7Z_wks9cvVFnIU7YpmzvhQjoRCjVsdGGzXREupLJsAyRpt7zmrEOstHy4mdy9iv50TY-khS6XVPNmF-U_8uFZLubE6xlVIb/s640/matrix.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAYKNpdu66ZfMj8944IRS3-EQvBt6RUGNs8muAMY5Gz6Xpr7Z_wks9cvVFnIU7YpmzvhQjoRCjVsdGGzXREupLJsAyRpt7zmrEOstHy4mdy9iv50TY-khS6XVPNmF-U_8uFZLubE6xlVIb/s1500/matrix.png)

  

  

So, I visited https://app.element.io/#/login again. Added the custom server. Entered the leaked username and password. To my surprise, I was in. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0wxPi6oQ2SyOGROvLYP7Cgtw5FNCB7INVEnkYLQ2OELVno8QnuiBiDJi0ASlDKjerX3Cq1wmsnNW36LICP9cpoQ0uyn5q0GlpPlKCrCbnktq8dLceUDl_U8Ad8DqGN5-Gxq9MZsIENPwf/s640/matrix3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0wxPi6oQ2SyOGROvLYP7Cgtw5FNCB7INVEnkYLQ2OELVno8QnuiBiDJi0ASlDKjerX3Cq1wmsnNW36LICP9cpoQ0uyn5q0GlpPlKCrCbnktq8dLceUDl_U8Ad8DqGN5-Gxq9MZsIENPwf/s2112/matrix3.png)

  

  

As I logged in, I understood the creds were of a matrix bot. There was a hell lot of information like Grafana passwords, server logs, private keys, etc. in channel description itself. However, I immediately logged out and filed a report. 

  

Reward 4000$

  

  

  

  
  
Takeaway for hackers:  
\- Do not give up or conclude too early. Try and research more.  
\- Try to escalate leaks but with caution. Do not go very deep.

  

Takeaway for companies:  
\- Purge the files just deleting a file doesn't work.  
\- Implement 2FA for all accounts.

  

  

  

Timeline:  
7th Aug: Filed the report.  
7th Aug: Bug was fixed by removing the file as well as refreshing the credentials. Additionally, 2FA was implemented.  
11th Aug: 4000$ bounty reward.

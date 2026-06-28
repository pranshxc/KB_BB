---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-04_from-multiple-idors-leading-to-code-execution-on-a-different-host-container.md
original_filename: 2019-10-04_from-multiple-idors-leading-to-code-execution-on-a-different-host-container.md
title: From Multiple IDORs leading to Code Execution on a different Host Container
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: e433880a5aebe472e781f96e661388cb5eeb5858fcc0e323100b60744f6c9262
text_sha256: abf24e145043d08955f56c31475954fc3337546f70e7ac7cd8f7022dd3d0155e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# From Multiple IDORs leading to Code Execution on a different Host Container

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-04_from-multiple-idors-leading-to-code-execution-on-a-different-host-container.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e433880a5aebe472e781f96e661388cb5eeb5858fcc0e323100b60744f6c9262`
- Text SHA256: `abf24e145043d08955f56c31475954fc3337546f70e7ac7cd8f7022dd3d0155e`


## Content

---
title: "From Multiple IDORs leading to Code Execution on a different Host Container"
page_title: "From Multiple IDORs leading to Code Execution on a different Host Container - Rahul R"
url: "https://rahulr.in/idor-to-rce/"
final_url: "https://rahulr.in/idor-to-rce/"
authors: ["Rahul (@Rahul_R95)"]
bugs: ["IDOR", "RCE"]
publication_date: "2019-10-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4996
---

# From Multiple IDORs leading to Code Execution on a different Host Container 

__ October 04, 2019 

Here is a short write-up on an interesting bug that I found while testing a Site there won’t be many screenshots of the bug as I can’t disclose any detail about the target.

Let’s talk about the target now the site is somewhat similar to any web hosting platform instead of providing a domain name and hosting web services like WordPress or Joomla. In this platform, we can host services such as Wordpress or Joomla and point that to our domain the backend uses docker as a medium to host the service which means that when we create a new service a docker container is created and the service is isolated within the docker container.

![](/assets/images/idor-to-rce/arc.png)

This is what I think of how the backend system creates a new service. So where is the vulnerability then in that platform I was able to find multiple IDORs such as stopping or starting any users hosted service and enabling and diabling security features but what made the application vulnerable to IDOR or Access Control Issues.The site uses a cookie called access_token to verify the session but there were no additional cookies that checked for Access Control Validations which made it vulnerable .This is how the IDOR request looked like.
  
  
  GET /site/ID HTTP/1.1
  Host: sub.redacted.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://sub.redacted.com/
  X-Requested-With: XMLHttpRequest
  Connection: close
  Cookie: access_token=random-access-token; user_time_zone=Asia%2FKolkata
  

By changing the ID to another user’s ID I was able to get into their site dashboard. So I was sure that every end point is vulnerable but starting or stopping a service is not what I wanted but something more which was the api after fuzzing for sometime I was able to find an endpoint which I think was for debugging because of the information it displayed.
  
  
  GET /sites/ID/container?access_token=some-random-access-token HTTP/1.1
  Host: api.redacted.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://sub.redacted.com/
  Connection: close
  

The response had a long json data with so much information such as their rancher cluster url the version of the service private ip of loadbalancer and docker container but the thing that caught my eye was MYSQL.

![](/assets/images/idor-to-rce/mysql_info.png)

Now with this endpoint I was able to gather the MYSQL and SFTP username and password of any user by just changing the ID so I created two wordpress demo sites to see if i can change the data that is stored in the database, Inorder to do that I needed to execute code on the container which was easy and the container had mysql installed but when I tried to connect to a remote host it failed, I also tried to connect to my own database but it still failed WTF so where is the database after reading the whole json data I got an idea of how the database connects to the website.

![](/assets/images/idor-to-rce/mysql_arc.png)

So the database is actually on a different instance as a container and it is using a proxy to establish a connection with the website.So for every website there is a MYSQL database container and we can only connect to that container only and now we need to escape out mysql container and here is IDOR to the rescue we can use phpmyadmin to login to the database when the request is processed the backend verifies the user with the site ID so if I could change the site ID to the victim’s ID the backend server takes it as a valid request and logs me in.
  
  
  GET /site/ID/pmalogin HTTP/1.1
  Host: sub.redacted.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://sub.redacted.com/
  Connection: close
  Cookie:access_token=random-access-token; user_time_zone=Asia%2FKolkata;
  Upgrade-Insecure-Requests: 1
  

![](/assets/images/idor-to-rce/mysql_alert.png)

![](/assets/images/idor-to-rce/phpmyadmin.png)

![](/assets/images/idor-to-rce/db.png)

And I was able to take control of the whole site which also means code execution.The company was also generous enough to fix the issue and reward me $$$.

**__Tags:** [bugbounty](/tags/#bugbounty),  [idor](/tags/#idor),  [rce](/tags/#rce)

**__Categories:** [bugbounty](/categories/#bugbounty),  [infosec](/categories/#infosec)

**__Updated:** October 04, 2019

[Previous](/C0C0N-XII-CTF-Walkthrough/ "COCON XII DOME CTF Walkthrough
") [Next](/Ra-Tryhackme-Walkthrough/ "Tryhackme Ra Walkthrough
")

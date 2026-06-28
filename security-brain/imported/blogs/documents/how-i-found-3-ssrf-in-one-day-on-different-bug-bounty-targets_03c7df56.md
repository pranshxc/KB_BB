---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-25_how-i-found-3-ssrf-in-one-day-on-different-bug-bounty-targets.md
original_filename: 2020-02-25_how-i-found-3-ssrf-in-one-day-on-different-bug-bounty-targets.md
title: How i found 3 SSRF in one day on different bug bounty targets
category: documents
detected_topics:
- ssrf
- rate-limit
- oauth
- idor
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- rate-limit
- oauth
- idor
- command-injection
- otp
language: en
raw_sha256: 03c7df563383f2fe064694d2cf22b673dd5aff31cb372b0d62108b2d067cc9a9
text_sha256: 967dd3b9708c92edb91b339124260e739a832686f74a7417cd3eaa63ba7fc84c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How i found 3 SSRF in one day on different bug bounty targets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-25_how-i-found-3-ssrf-in-one-day-on-different-bug-bounty-targets.md
- Source Type: markdown
- Detected Topics: ssrf, rate-limit, oauth, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `03c7df563383f2fe064694d2cf22b673dd5aff31cb372b0d62108b2d067cc9a9`
- Text SHA256: `967dd3b9708c92edb91b339124260e739a832686f74a7417cd3eaa63ba7fc84c`


## Content

---
title: "How i found 3 SSRF in one day on different bug bounty targets"
url: "https://medium.com/@Mr.Daman.Singh/how-i-found-3-ssrf-in-one-day-on-different-bug-bounty-targets-62e91b4268f8"
authors: ["-"]
bugs: ["SSRF"]
publication_date: "2020-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4753
scraped_via: "browseros"
---

# How i found 3 SSRF in one day on different bug bounty targets

How i found 3 SSRF in one day on different bug bounty targets
Damanpreet Singh
Follow
4 min read
·
Aug 25, 2020

320

Hey guys!,

My name is damanpreet singh. This is my first write-up, so please forgive me for my mistakes. So, lets start:

I started bug bounties after about a year. I was only learning, still i am learning. So, some days ago i thought , now i should start to looking for bugs. So, on 21 august, i chose some bounty targets, and started hunting. Now lets talk about those 3 ssrf’s one by one.

1 case- ssrf via image fetching:

lets assume target as target.com , that target was for shopping gift cards etc. So, i signed up , they were sending a 6 digit otp for verification. I tried rate limiting for brute forcing otp, but no success. but i got no rate limiting on sending unlimited otps.

Then i uploaded profile picture, after uploading, i tried to delete it to know, if its still stored on their server or not, or if i could delete someone else’s picture or not. I got no success there, they were properly removing deleted picture from there server, also there was no idor in deleting pictures.

i was like

After it, i checked my proxy history, there was some requests like:

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

POST /user/dashboard/profile HTTP/1.1
Host: target.com
Connection: close
Content-Length: 132
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Origin: https://target.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://target.com/signin
Cookie: xxxxxxxxxxxxxxxxx

[{“userid”:”21452",”imgurl”:”https://api.target.com/images/profiles/MjE0NTI=","type":"jpeg"}]

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

they were fetching profile pictures from their api, i changed “imgurl” parameter value to my burp collaborator client , but i got response as “There is an error while fetching this image, please try again” . also i got some requests on my collaborators.

Press enter or click to view image in full size
hmmmmmm

Then i removed “type:jpeg”, and sent the request and booooom , there was my collaborator’s subdomain.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

HTTP/1.1 200 OK
Server: Apache/2.4.46 (cPanel) OpenSSL/1.1.1g mod_bwlimited/1.4
X-Powered-By: PHP/5.6.40
Connection: close

<body>zg4w1rswxl5nazutwziseczjigz</body>

Get Damanpreet Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Target was using aws , so i requested http://169.254.169.254/latest/meta-data/ , and booom again, i got their aws instances metadata.

Timeline:

Reported on: 21 august

Triaged: after 6 7 hours

Rewarded on: 24 august $$$$

2 Case- SSRF in JIRA Instance:

Another target was using JIRA instance at

jira.reports.target.com

I checked the version, it was 7.x.x something, then i added vulnerable path ,

jira.reports.target.com/plugins/servlet/oauth/users/icon-uri?consumerUri=https://bing.com

and boom, it loaded the bing homepage.

I reported it, but it was duplicate.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

3 Case-

After finding this jira ssrf, i remembered that i had a target that was also using JIRA. I found that target > tested > ssrf confirmed > reported > first they thanked me, but after some hours, they mailed me that this is out of scope.

I hope, you enjoyed my first write-up, if yes then follow me on my social media accounts.

https://instagram.com/hacking_devta

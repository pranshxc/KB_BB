---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-12_no-rate-limit-2k-bounty.md
original_filename: 2020-01-12_no-rate-limit-2k-bounty.md
title: No Rate Limit - 2K Bounty
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
language: en
raw_sha256: 66d67a83de0188af58485bd17ac6cec3f312e3beaa4bc757d6741c5606c11d0c
text_sha256: dc03f08567a0f7af36226b507b6b6017fd76c8529c9c80b82390879ed4dad111
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# No Rate Limit - 2K Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-12_no-rate-limit-2k-bounty.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `66d67a83de0188af58485bd17ac6cec3f312e3beaa4bc757d6741c5606c11d0c`
- Text SHA256: `dc03f08567a0f7af36226b507b6b6017fd76c8529c9c80b82390879ed4dad111`


## Content

---
title: "No Rate Limit - 2K Bounty"
page_title: "No Rate Limit - 2K$ Bounty. Summary : | by Jerry Shah (Jerry) | Medium"
url: "https://medium.com/@shahjerry33/no-rate-limit-2k-bounty-642720ffba99"
authors: ["Shrey Shah (@ShreySh43332033)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Lack of rate limiting"]
bounty: "2,000"
publication_date: "2020-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4832
scraped_via: "browseros"
---

# No Rate Limit - 2K Bounty

Top highlight

No Rate Limit - 2K$ Bounty
Jerry Shah (Jerry)
Follow
3 min read
·
Jan 12, 2020

643

5

Summary :

In computer networks, rate limiting is used to control the rate of traffic sent or received by a network interface controller and is used to prevent DoS attacks.

Rate limiting is used to control the amount of incoming and outgoing traffic to or from a network. For example, let’s say you are using a particular service’s API that is configured to allow 100 requests/minute. If the number of requests you make exceeds that limit, then an error will be triggered

No rate limit means their is no mechanism to protect against the requests you made in a short frame of time. Say for example you have a forget password page and a victim’s email, now enter the victim’s email and intercept the request using burp suite (a proxy tool) and send that request to repeater or intruder for repeating it. If the repetition doesn’t give any error after 50, 100, 1000 repetitions then their will be no rate limit set.

Now the scope of this vulnerability is not limited only to forget password page you can also use it in comments, adding user (where you need to send an invite email), sending GIFs or messages, sending OTPs etc.

While searching for No Rate Limit I came across a comment section on yahoo.com where I was able to make 100–200 comments in less than 60 seconds and it was a GIF flood.

Press enter or click to view image in full size
GIF flooding
Press enter or click to view image in full size
GIF flooding

I found it on 4 different endpoints on yahoo.com and I was paid with good amount. All the endpoints have been fixed

How to attack using Intruder :

Go to any endpoint where you can comment or you can send messages etc.
Now make a comment and intercept the request using burp suite
Send that request to intruder and click on clear
Select the comment you made and click on add
Press enter or click to view image in full size
Burp Intruder

5. Now to payload section and you can simply add a payload file which contains various words or you can use “Add from list option”

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. Click on start attack

Press enter or click to view image in full size
Attacking

7. Refresh the page and you’ll find the flood

Press enter or click to view image in full size
Comment Flood

How to attack using Repeater :

Send the request to repeater
Press enter or click to view image in full size
Repeater

2. Click on go as many times as you want the comment to be posted

3. Refresh the page

Thank You :)

Instagram : jerry._.3

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-10_ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-.md
original_filename: 2020-11-10_ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-.md
title: SSRF (Server Side Request Forgery) worth $4,913 | My Highest Bounty Ever !
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- otp
- cors
- csrf
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- otp
- cors
- csrf
language: en
raw_sha256: 75078434b6389f379714c90dab8d76ddf1958e1dae57a518f99ee10049239dec
text_sha256: f75caa33b43032ab2b193840f3080a0bbdfe377d0ae9d7133bdf8739ab4aac32
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF (Server Side Request Forgery) worth $4,913 | My Highest Bounty Ever !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-10_ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, otp, cors, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `75078434b6389f379714c90dab8d76ddf1958e1dae57a518f99ee10049239dec`
- Text SHA256: `f75caa33b43032ab2b193840f3080a0bbdfe377d0ae9d7133bdf8739ab4aac32`


## Content

---
title: "SSRF (Server Side Request Forgery) worth $4,913 | My Highest Bounty Ever !"
url: "https://medium.com/techfenix/ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-7d733bb368cb"
authors: ["Sayaan Alam (@ehsayaan)"]
programs: ["Dropbox"]
bugs: ["SSRF"]
bounty: "4,913"
publication_date: "2020-11-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4147
scraped_via: "browseros"
---

# SSRF (Server Side Request Forgery) worth $4,913 | My Highest Bounty Ever !

SSRF (Server Side Request Forgery) worth $4,913 | My Highest Bounty Ever !
Sayaan Alam
Follow
4 min read
·
Nov 10, 2020

1.6K

4

Press enter or click to view image in full size

Hi Everyone! ,

Hope you’re doing well , today I am doing another write-up about one of my best findings and my highest bounty ever. It’s an SSRF — Server Side Request Forgery vulnerability I discovered in Dropbox Bug Bounty Program.

On First Glance , Dropbox Program looked very interesting to me as it was having best payout and good response time , so I choose to hunt on Hellosign mentioned on Dropbox Bug Bounty Program’s Policy.

I started hunting on main application at app.hellosign.com , I found that there was a feature of importing document from Dropbox , GDrive , BOX , OneDrive , EverNote. At this point SSRF came up in my mind already , so I started with Dropbox Import Feature , I saw the following request :-

Press enter or click to view image in full size

I changed the value of file_reference parameter to my burp collaborator URL , But I got 404 😫 , at this point I thought they already have SSRF Protection there , I gave up and closed my P.C

On Next Day with fresh mind , I thought to Dig-In Again and I tried with OneDrive Feature and I saw this request :-

GET /attachment/externalFile?service_type=O&file_reference=MYONEDRIVEFILELINKHERE&file_name=FILENAME.ANYTHING&c=0.8261955039214062 HTTP/1.1
Host: app.hellosign.com
Connection: close
Accept: application/json
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
X-CSRF-Token: 
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: REDACTED
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7
Cookie:REDACTED

You’ll see that above request is having a service_type paramter value O which means onedrive it’s making it different from the first request which is from dropbox and having Din that parameter. Now value of file_reference parameter changed to my collaborator link and luckily i got a ping this time.

After this a PDF got generated on HelloSign which contained the content of my collaborator page. At this moment I got too much happy 😍

Now I moved to get localhost content , At first I checked which cloud service they’re using on whatismyipaddress.com , I found that they're using AWS/EC2 , So tried getting http://169.254.169.254/latest/ , But I got :-

404 Not Found

Sadly Request Didn’t Go through , Now I tried http://127.0.0.1 , that too got the same response.

Now I got lil sad but I tried to find more ways through Hackerone Hacktivity and Found this GEM Report :- https://hackerone.com/reports/247680 where reporter used 303 Redirect to Bypass SSRF Protection.

Get Sayaan Alam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I quickly hosted the following code on my server :-

<?php header('Location: http://169.254.169.254/latest/meta-data/', TRUE, 303); ?>

Now I tried again with my server redirect link and Finally!!! I got the content of AWS Instance (Metadata) 😍 😍 😍

Press enter or click to view image in full size

Now I got too much happy and shocked too as found full read SSRF on one of the biggest and best bug bounty programs around the world, I was able to retrieve everything from AWS metadata like access_keys, tokens, etc.

I reported the bug immediately and It got triaged in 3 hours :)

Press enter or click to view image in full size
Press enter or click to view image in full size

It was the happiest moment for me. 😄 😄 😄

Now Team asked me to check if RCE was possible there or not. I got the access key , token and Tried Executing this commands:- AWS ec2 stop-instances — instance-ids intsanceidhere , But it didn’t worked as that role was not having enough permissions to execute the command.

But I was still too happy and was excited for Bounty 😙

Finally, on the 9th Day, Dropbox Rewarded me with $4913

Press enter or click to view image in full size

It was all about my first SSRF and the highest bounty till now. 😄

If you have questions and anything about the post you want to ask me, please contact me via Twitter (ehsayaan) My DMs are always open.

Kudos to Sean(zseano) , Sam Curry , Jenish Sojitra and Shubham Patel for reviewing this blog.

Special thanks to Dropbox Security Team for helping me throughout the whole process.

Until Next Time!

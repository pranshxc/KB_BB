---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-30_story-about-my-first-bug-bounty.md
original_filename: 2018-11-30_story-about-my-first-bug-bounty.md
title: Story about my first bug bounty
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 91bcc36b8df70596f1dac61ce7ebe23f2ecf6e7c42b67c50effd7a6c6fe2f9a1
text_sha256: bf410a0cfc9f31297f275d4c06295a13fe93ea338958b06b3ee209254190425b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Story about my first bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-30_story-about-my-first-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `91bcc36b8df70596f1dac61ce7ebe23f2ecf6e7c42b67c50effd7a6c6fe2f9a1`
- Text SHA256: `bf410a0cfc9f31297f275d4c06295a13fe93ea338958b06b3ee209254190425b`


## Content

---
title: "Story about my first bug bounty"
url: "https://medium.com/@sudhanshur705/story-about-my-first-bug-bounty-9fe710be8241"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Alibaba"]
bugs: ["XSS"]
bounty: "100"
publication_date: "2018-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5554
scraped_via: "browseros"
---

# Story about my first bug bounty

Top highlight

Story about my first bug bounty
Sudhanshu Rajbhar
Follow
4 min read
·
Dec 1, 2018

1K

12

2 Dom Based XSS in ucweb.com

Hey Everyoneee,

I am Sudhanshu Rajbhar, today I am going to share the story of my two dom based xss which I found in Alibaba’s Bug Bounty Programme.

I just came to know about Alibaba’s Bug Bounty Programme and also that they have a large scope.So I decided that I will take a look at it.It was the first week of August.After two days my maths exam was there but I was busy with this.

After reading their policy and checking scope.I went on youtube and was searching for the bugs which were already found in Alibaba websites to get an idea about my target, most of the pocs were about xss.After watching the pocs I picked out some domains randomly that included alipay.com,ucweb.com and some more.

Here we go..

I started my recon by first checking the available subdomains for that purpose I went to https://virustotal.com and started going through them one by one. Didn’t get any interesting subdomains at first so I started looking for ucweb.com subdomains here and found this subdomain samsung.ucweb.com, samsung ahh let’s see what’s there.I opened that subdomain and got this

Press enter or click to view image in full size

What most people will do here? they will just ignore it.I was also going to do the same thing at that time then I remember about an article which I read that if you encounter any page like this google the site you may find a endpoint which is accessible.

So that’s what I did I used this simple dork site:samsung.ucweb.com and the results really suprised me

Press enter or click to view image in full size

I opened this url http://samsung.ucweb.com/webstore/classify.html?dataKey=LifeStyle&title=LifeStyle and started testing the parameters , the title parameter was reflecting the input so for checking if there is any filter or something I used <b></b> and found out that there was no filter.

Press enter or click to view image in full size

I used the payload <script>alert(1)</script> but it didn’t work then I tried <img src=x onerror=alert(‘XSS’)> and boooom yeah the I got the xss popup.

Press enter or click to view image in full size

This was my first bug in a bounty programme , so I was really excited and I was even screaming at that time.

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I submitted this on https://security.alibaba.com and their response was really fast, I opened the report and saw that I was rewarded with $50.

This time I was screaming a little bit louder than before.So here’s the end of the story of my first bugbounty.Soon after that I was rewarded with $100 on hackerone on vhx.

Now it’s time for the second xss

The 2nd xss I found this month only, in the same domain.For fixing the previous xss they removed that endpoint and if I try to open that endpoint now I will get a 404 error not found.

I just thought of using a tool like dirbuster or gobuster on this subdomain so that I can find a new endpoint.I tried dirbuster and gobuster but both of them were not working here they were giving some errors on this subdomain.So I moved on.

After some days I got to know about dirsearch,so I thought of giving it a try and it was working perfectly , from the result I got one more endpoint /test/

I opened http://samsung.ucweb.com/test/ and from here I found this http://samsung.ucweb.com/test/classify.html?dataKey=New&title= same url just like before, I used the payload and yeah you guess it right the xss popup was there.

Press enter or click to view image in full size

Again this time also $50 bounty from Alibaba.It was really simple.

So guys don’t forget to use directory bruteforce tools on the subdomains of your target you might get lucky just like me.

Thanks a lot for reading it till the end. I hope you will find this article interesting. Sya

Video POC

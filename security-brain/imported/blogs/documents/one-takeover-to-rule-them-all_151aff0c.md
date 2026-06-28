---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-21_one-takeover-to-rule-them-all.md
original_filename: 2022-09-21_one-takeover-to-rule-them-all.md
title: One takeover to rule them all
category: documents
detected_topics:
- command-injection
- graphql
tags:
- imported
- documents
- command-injection
- graphql
language: en
raw_sha256: 151aff0cbf061a4f13f4d92455c2dae8cd550e80627f7330566a86967851e494
text_sha256: bcb3d71f63406755e879434e8a19e6f2f6b58a01b1860d137a16a09be1561713
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# One takeover to rule them all

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-21_one-takeover-to-rule-them-all.md
- Source Type: markdown
- Detected Topics: command-injection, graphql
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `151aff0cbf061a4f13f4d92455c2dae8cd550e80627f7330566a86967851e494`
- Text SHA256: `bcb3d71f63406755e879434e8a19e6f2f6b58a01b1860d137a16a09be1561713`


## Content

---
title: "One takeover to rule them all"
page_title: "One takeover to rule them all · Gwendal Le Coguic"
url: "https://10degres.net/one-takeover-to-rule-them-all/"
final_url: "https://glc.st/posts/one-takeover-to-rule-them-all/"
authors: ["Gwendal Le Coguic (@gwendallecoguic)"]
programs: ["EDF"]
bugs: ["Subdomain takeover"]
publication_date: "2022-09-21"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2137
---

# One takeover to rule them all

__ September 21, 2022  __3 minutes read

__[tools](https://glc.st/tags/tools/) • [subdomain takeover](https://glc.st/tags/subdomain-takeover/)

Because of Covid, the first quarantaine in France occured in March 2020. During that time I wrote a Python script to detect Subdomain Takeover. As I have been successful several times with the tool, one hit was especially beautiful.

_The story of how I have been able to take control of 450+ subdomains of the national french electricity company[EDF](https://www.edf.fr/)._

[![edf subdomain takeover](https://glc.st/images/edf-subto.png)](https://glc.st/images/edf-subto.png)

  

* * *

I'm not going to explain what is subdomain takeover so take a look at the following articles if you want to know more: 

[OWASP test guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/10-Test_for_Subdomain_Takeover)  
[Hackerone guide](https://www.hackerone.com/application-security/guide-subdomain-takeovers)  
[0xpatrik basics](https://0xpatrik.com/subdomain-takeover-basics/)

* * *

  
As we all know there are several ways to takeover a subdomain but the easiest way is probably to buy an expired domain which is available for purchase.  
  
  

**Finding:**  
Using my tool [dnspy](https://github.com/gwen001/dnspy), I found that `nucleaire.edf.fr` was an alias of `edf-linkbynet.com`. A quick search on Gandi and I realized that last one was available for purchase for about 12€/year. Not knowing what would happen next, I bought the domain and configured it on my server to serve a nice PoC page. 

![edf nuclaire subdomain takeover](https://glc.st/images/edf-subto-nucleaire.png)

  

**Traffic incoming!**  
A few days later, I checked my server logs to see if anyone requested the stolen subdomain. What was my surprise when I noticed all those requests for different subdomains I didn't know anything about. 

[![edf subdomain takeover logs](https://glc.st/images/edf-subto-logs.png)](https://glc.st/images/edf-subto-logs.png)

  
  
At that time EDF had a private bug bounty program on the french platform YesWeHack. I was not invited so I used the dedicated contact form on their website. 6 weeks later and several tries to get in touch with them, the problem was magically and silently fixed.

At the end more than 450 subdomains were redirected to my server. Exploited by a malicious user, it could have been devastating: social engineering, phishing, cookies manipulation, fake payment system, company reputation… (a simple _“thank you”_ would have been appreciated).

Regardind the issue itself, my guess is a bad communication between tech team leaders. One admin bought `edf-linkbynet.FR` and the other one configured all CNAMEs to point to `edf-linkbynet.COM`, as simple as that!

## The tool

The tool, called [dnspy](https://github.com/gwen001/dnspy), is composed of 3 modules:

1/ the grabber tries to find subdomains using external tools like subfinder, oneforall, github, amass… then alterations are created using altdns or dnsgen.

2/ the resolver performs DNS queries on all subdomains grabbed and generated using massdns, trying to detect dead hosts, cnames…

3/ the interpreter reads the output of the resolver and looks for possible takeover using the fingerprint file. It’s inspired of subjack with some extra features like regexps support and an ignore list.

The whole thing is daemon based and can be independently launched. Below some good findings.

![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-acef.png) ![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-bred.png) ![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-ce-picardie.png) ![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-bpce.png) ![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-jeunesse-gouv.png) ![edf nuclaire subdomain takeover](https://glc.st/images/dnspy-hillary.png)

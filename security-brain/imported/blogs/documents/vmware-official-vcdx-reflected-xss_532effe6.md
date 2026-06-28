---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-19_vmware-official-vcdx-reflected-xss.md
original_filename: 2017-11-19_vmware-official-vcdx-reflected-xss.md
title: VMware Official VCDX Reflected XSS
category: documents
detected_topics:
- xss
- sqli
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- sqli
- command-injection
- supply-chain
language: en
raw_sha256: 532effe647891c509246469be25afea5f81eeaa61bf3030e39b97544f725cd66
text_sha256: 99ad2406e5acb767a9afe69aa513a01495f2e16f290539405374420486db0cb3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# VMware Official VCDX Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-19_vmware-official-vcdx-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, supply-chain
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `532effe647891c509246469be25afea5f81eeaa61bf3030e39b97544f725cd66`
- Text SHA256: `99ad2406e5acb767a9afe69aa513a01495f2e16f290539405374420486db0cb3`


## Content

---
title: "VMware Official VCDX Reflected XSS"
url: "https://medium.com/@honcbb/vmware-official-vcdx-reflected-xss-90e69a3c35e1"
authors: ["Honc (@honcbb)"]
programs: ["VMware"]
bugs: ["Reflected XSS"]
publication_date: "2017-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6046
scraped_via: "browseros"
---

# VMware Official VCDX Reflected XSS

VMware Official VCDX Reflected XSS
Honc
Follow
2 min read
·
Nov 20, 2017

I was browsing the HackerOne bug bounty Project.

I want to try to find the loophole of big Enterprise first! I choose VMware.

Before you begin, see if the VMware vulnerability policy has something to pay attention to, This is what you should pay attention to in participating in any loophole reward program.

After reading the VMware vulnerabilities policy, there is not much to be aware of (or accept those vulnerabilities or those who do not)

Only Note:

Press enter or click to view image in full size

In the case of vulnerabilities found in third-party software components used in VMware products, please also notify VMware as described above.

Policy: https://www.vmware.com/support/policies/security_response

－－－－－－－－－－－－－－－－－－－－－－－－

Don’t talk much, we start looking for a loophole.

Because I was using VMware products, I was thinking that each product has a certification expert badge and so on, whether this has, curious to find this site

Press enter or click to view image in full size

Liste：https://vcdx.vmware.com/

is a VMware certification expert！！

But there seems to be no place to register. Go to the login page

At first a lot of people will try SQL injection some statements, but I didn’t think too much! Because big companies will not have such a clear loophole exists, the existence of the words have been found out

Based on occupational diseases, I try to enter a XSS string “><img src=x Onerror:alert (1)/>

Get Honc’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I use grab data to modify

POST /login HTTP/1.1

Host: vcdx.vmware.com

User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Referer: https://vcdx.vmware.com/login

Cookie: connect.sid=s%3AwU84EnNnabqCyW98coEEFYTZLhYkitff.al1Ce9v8xNZNBnZIhvDJ8IDQzDHVDBXlgb8%2BxV%2By2gg

X-Forwarded-For: 8.8.8.8

Connection: close

Upgrade-Insecure-Requests: 1

Content-Type: application/x-www-form-urlencoded

Content-Length: 75

redirectTo=&email=%22%3E%3Csvg%2Fonload%3Dalert%28domain%29%3E%22&password=***REDACTED***

Press enter or click to view image in full size

Indeed request response XSS I’m sure this is a loophole

Timeline
2017/02/13 08:46 Provide vulnerability details to VMware Security Team
2017/02/14 11:35 Receive response from Vinay that inspection is in progress
2017/03/25 02:09 Yes, it fixes
2017/03/31 05:18 Tell me there will be VMware Swag memorabilia

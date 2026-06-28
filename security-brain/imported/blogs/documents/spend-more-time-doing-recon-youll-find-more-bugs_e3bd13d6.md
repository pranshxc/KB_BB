---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-03_spend-more-time-doing-recon-youll-find-more-bugs.md
original_filename: 2020-10-03_spend-more-time-doing-recon-youll-find-more-bugs.md
title: Spend more time doing recon, you’ll find more BUGS.
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- information-disclosure
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- information-disclosure
language: en
raw_sha256: e3bd13d6baa71f8f90760f4ec483b7be493066d27d0d8421cb4212004edec828
text_sha256: fa5fd66b487941b2d2d0f2f632bb8c986a29815035a18564cc797019eafb4d2d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Spend more time doing recon, you’ll find more BUGS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-03_spend-more-time-doing-recon-youll-find-more-bugs.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e3bd13d6baa71f8f90760f4ec483b7be493066d27d0d8421cb4212004edec828`
- Text SHA256: `fa5fd66b487941b2d2d0f2f632bb8c986a29815035a18564cc797019eafb4d2d`


## Content

---
title: "Spend more time doing recon, you’ll find more BUGS."
url: "https://medium.com/@vedanttekale20/spend-more-time-doing-recon-youll-get-more-bugs-e7ffd5bf9202"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["Reflected XSS", "Information disclosure"]
publication_date: "2020-10-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4221
scraped_via: "browseros"
---

# Spend more time doing recon, you’ll find more BUGS.

Vedant Tekale
 highlighted

Spend more time doing recon, you’ll find more BUGS.
Vedant Tekale
Follow
3 min read
·
Oct 3, 2020

644

3

Hello again great #bugbounty community! My name is Vedant(Also known as Vegeta on Twitter😁) and I’m a cybersecurity enthusiast and an aspiring Bug hunter :) I’m learning and doing bug hunting for about 6 months now and I really love what I do. So from August I spent more time learning different methodologies of doing “Recon” and recon is the most important phase of bug hunting. Today I’ll share a story about my recent findings and a way of recon that I tried for first time. So lets begin.

So whenever I pick a program and start recon I always try collect all of its subdomains and then start fingerprinting, fuzzing and all other things. But this time I used a different approach. I recently watched a video of Jason Haddix about the bug hunting methodology and I learned about the ASNs and CIDR. So I was hunting on a private program which had all of its assets owned in scope and I already found some great bugs like information disclosure, SSRF and XSS on some of its subdomains but some of them got duped. So one day I decided to take a different approach and I visited https://whois.arin.net/ui/ and searched for the target name and got some results. There I got the CIDR of my target which is nothing but the range of IPs the target company owns. Then I used a tool known as masscan to scan the range of IPs and I used the following command :-

Command:- bin/massscan — range CIDR_here -p 80, 443, 8080, 8443 -oG results.txt — rate 10000

After the scan completed there were about 140 IPs in the output file so I used aquatone to screenshot all the IPs and for that I used the following command:-

Command:- cat results.txt | aquatone -out ~aquatone/target

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I was checking all the screenshots one by one and after some time I saw that some IPs had JIRA dashboard running on them. I checked the version and it was 7.3.3 , I quickly googled for Jira 7.3.3 vulnerabilities and got the results and I was like,

I read some of the CVEs and after going through each of them one by one I got the CVE-2018–20824 which is a reflected XSS vulnerability. I quickly googled about its exploits and got one. I copied the exploit path and appended it to one IP which had JIRA dashboard and YEAHH!! XSS triggered successfully. After that I tried for the same on all other IPs which had JIRA dashboard running and all of them were vulnerable :)

So instead of manually checking for all other CVEs I used the tool known as Nuclei . I used the following command :-

Command:- nuclei -t /path/to/nuclei-templates/cves/ -l results.txt -o nuclei_cve.txt -c 200

And after some time I got some IPs which were vulnerable to the CVEs such as CVE-2019–8449 and CVE-2020–14179 which lead to information disclosure. This was the first time I got so many bugs in very short time and I was very happy with this.

I made some good reports and sent it to the target company. Some of them got duped and few of them got accepted 😂😂😂 but I learned a lot from this and I always say to myself that “I never lose, I either win or I learn”.

I hope you learned something new from this writeup and if you have any doubts or questions about it you can get in touch with me HERE. I daily learn a lot of new things from this awesome community so I’m trying to give something back to the commnity by sharing such writeups and #bugbountytips on Twitter.

Thank you so much for reading and happy breaking!

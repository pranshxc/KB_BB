---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-22_how-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash.md
original_filename: 2024-04-22_how-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash.md
title: How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash
category: documents
detected_topics:
- cloud-security
- idor
- xss
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- cloud-security
- idor
- xss
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 3ad0b4320eaa10fbf1ceea1574861561765cf6e47a6bd323f36d773c2483ce2f
text_sha256: adbd88dd70c8d609aa58180120d65190d49e94f05dc305f137ab37209ab2c8a4
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-22_how-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, xss, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `3ad0b4320eaa10fbf1ceea1574861561765cf6e47a6bd323f36d773c2483ce2f`
- Text SHA256: `adbd88dd70c8d609aa58180120d65190d49e94f05dc305f137ab37209ab2c8a4`


## Content

---
title: "How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash"
url: "https://ph-hitachi.medium.com/how-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash-f43a0dae3ec1"
authors: ["Ph.Hitachi"]
programs: ["Globe Telecom (Gcash)"]
bugs: ["Information disclosure", "File disclosure"]
publication_date: "2024-04-22"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 327
scraped_via: "browseros"
---

# How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash

Top highlight

How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash
Ph.Hitachi
Follow
6 min read
·
Apr 23, 2024

783

10

Hi guys,

so iwill share this second finding on gcash VDP Channel & share tips on some recon methodologies such as subdomain enumation, wappalyzer mapping, mass recon & scoping with automated tools.

What is recon scoping?

Reconnaissance (or recon) scoping is the initial phase of a vulnerability assessment or penetration testing engagement. It involves identifying and gathering information about the target systems, networks, and infrastructure. The primary goal is to understand the scope of the environment to be tested and to gather intelligence that might be useful during subsequent phases of the assessment.

Start:

before we start my recon methodologies mostlikely separated per categories, so i created multiple directory on my local machine by running this:

mkdir -p gcash.com ~/recon/targets/gcash.com/subdomains/
mkdir -p gcash.com ~/recon/targets/gcash.com/endpoints/
mkdir -p gcash.com ~/recon/targets/gcash.com/aws/
mkdir -p gcash.com ~/recon/targets/gcash.com/dns/
Recon workflow:

- subdomain enumeration
- information gathering (network, dns, tech, ports)
- automated testing

Subdomain mapping/enumeration:

Subdomain gathering is very crucial interms of bug bounty/pentesting, you need to gather a subdomains as you can, so will show you how to find a subdomains with different methods with correct tools.

Note: some method will not work all the time you use it on any target, but i will show the methods here that i commonly use to gather subdomains.

Tools:
subfinder: passive and active methods
assetfinder: certificate transparency logs
alterx: dynamic & permutation/alterations
asnmap: to map ASN and find subdomains
ffuf: to find subdomains on vhosts

# passive & active subdomain enumation using subfinder
subfinder -d gcash.com -o ~/recon/targets/gcash.com/subdomains/subfinder.txt
# subdomain enumeration via certificate transparency logs with assetfinder
assetfinder --subs-only gcash.com >> ~/recon/targets/gcash.com/subdomains/assetfinder.txt
# dynamic subdomain enumeration with alterx
echo gcash.com | alterx -enrich | dnsx > ~/recon/targets/gcash.com/subdomains/alterx-dynamic.txt

# for high chance to find subdomain 
# you can generate patterns based on existing subdomains
subfinder -d tesla.com | alterx | dnsx
# subdomain enumaration via Permutation/Alterations with alterx
echo gcash.com | alterx -pp 'word=subdomains-top1million-50000.txt' | dnsx > ~/recon/targets/gcash.com/subdomains/alterx-permutation.txt
# subdomain enumeration via ASMapping
asnmap -d gcash.com | dnsx -silent -resp-only -ptr > ~/recon/targets/gcash.com/subdomains/dnsx.txt
# subdomain enumeration via vhost
cat subdomains-top1million-50000.txt | ffuf -w -:FUZZ -u http://gcash.com/ -H 'Host: FUZZ.gcash.com' -ac

after we enumerate subdomains using different tools their are some duplicates subdomains, to optimize the subdomains we will merge it using anew and will it actively remove duplicate subdomains.

# Merging subdomains from ~/recon/targets/gcash.com/subdomains/* into one file and remove duplicates
cat ~/recon/targets/gcash.com/subdomains/*.txt | anew ~/recon/targets/gcash.com/subdomains/subdomains.txt

after we merge subdomains we need to filter live subdomains using httpx to filter https/http on lists of subdomain.

# Probe for live HTTP/HTTPS servers
cat ~/recon/targets/gcash.com/subdomains/subdomains.txt | httpx -o ~/recon/targets/gcash.com/subdomains/httpx.txt
Information Gathering:

after we filter live subdomains we will start a information gathering using httpx to gather infomation about the domains using wappalyzer mapping techniques to identify technologies that are used to websites.

Press enter or click to view image in full size
Automated testing:

after we gather information about tech we will start using nuclei.

Nuclei is used to send requests across targets based on a template, leading to zero false positives and providing fast scanning on a large number of hosts. Nuclei offers scanning for a variety of protocols, including TCP, DNS, HTTP, SSL, File, Whois, Websocket, Headless, Code etc. With powerful and flexible templating, Nuclei can be used to model all kinds of security checks.

using nuclei i scan all subdomains using this code:

cat ~/recon/targets/gcash.com/subdomains/httpx.txt | nuclei -config ~/nuclei-templates/config/custom.yml

in nuclei i build my own custom configurations for scoping, its include finding senstive informations (e.g, secret keys, tokens, credentials) on configurations and compiled assets like javascript or tcp (e.g, docker misconfig) and some type of fuzzing overall, this configurations focused on finding sensitive data, you can also make custom config for wappalyzer using nuclei to detect technologies.

# nuclei -config ~/nuclei-templates/config/custom.yml -list target_list_to_scan.txt

severity:
  - critical
  - high
  - medium
  - low

type:
  - http
  - tcp
  - javascript

include-tags:
  - generic
  - config
  - misconfig
  - exposures
  - exposure
  - disclosure
  - file
  - logs
  - traversal
  - xss
  - lfi
  - crlf
  - cache
  - takeovers
  - wordpress

exclude-tags:
  - tech
  - dos
  - fuzz
  - creds-stuffing
  - token-spray
  - osint
  - headers # exlude finding missing HTTP security headers

After the scanning is done, i check the results and i find this:

This the database credentials that exposed due to misconfigurations.

actually this weird because this not detected by gobuster and disearch when im doing fuzz.

Note: mass scanning will take an hours depending on how many domains you scan, plus how many templates do you have and also on a internet speed, that’s why scoping based on gathered informations are important but there’s nothing wrong with “scanning everywhere” to find valid bugs.

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

in this case i have a private VPS and i run the nuclei inside VPS using docker so even i have something todo, the scanning will continue in the background of VPS even you’re sleeping and VPS have more internet speed so its much better to use VPS than your local machine if you have poor connection.

AWS S3 bucket:

since we see on the httpx that they use aws, lets filter the s3 bucket using nuclei.

#filter s3 buckets and save to ~/recon/targets/gcash.com/aws/butcket.txt
cat ~/recon/targets/gcash.com/subdomains/httpx.txt | \
nuclei -t technologies/aws/aws-bucket-service.yaml | \
awk -F’://’ ‘{print $2}’ | \
awk -F’/’ ‘{print $1}’ > ~/recon/targets/gcash.com/aws/butcket.txt
Press enter or click to view image in full size
# save open buckets as open_buckets.txt from ~/recon/targets/gcash.com/aws/butcket.txt
cat ~/recon/targets/gcash.com/aws/butcket.txt | \
xargs -I {} sh -c ‘if aws s3 ls “s3://{}” — no-sign-request 2>/dev/null; \
then echo “{}” >> ~/recon/targets/gcash.com/aws/open_buckets.txt; \
fi’
Press enter or click to view image in full size
Passive Open Port Scanning:

on open port scanning i always use naabu, it allows you to enumerate valid ports for hosts in a fast and reliable manner.

# scan all open ports except on port 80 & 443
cat ~/recon/targets/gcash.com/subdomains/subdomains.txt | naabu --passive
Press enter or click to view image in full size

after we scanned all ports lets look for expoitable ports, in my case i always look for SMTP ports like ssl or tls, if you find this ports you can test a email spoofing on your self using swaks to make PoC.

Press enter or click to view image in full size
Press enter or click to view image in full size

in this case this configured corectly, so even the ports are open it doesn’t mean its expoitable, so please make sure to test it before you report.

another example of not vulnerable:

Press enter or click to view image in full size
Press enter or click to view image in full size

After i found multiple vulnerability, ireported it and they ackowledged me and got invited to YesWeHack Program as a private bug bounty program that separate to VDP channel.

Press enter or click to view image in full size
Press enter or click to view image in full size

Only BBP are have monetary reward, but on VDP they only give token or swag as appreciation.

for endpoints/path recon you can refer on this article that published by Khaledyassen this was the great article so far.

How I Found Multiple XSS Vulnerabilities Using Unknown Techniques
Hello, everyone. I hope you are well.

infosecwriteups.com

Press enter or click to view image in full size

actually im not sure about this on credentials but since the port was only open on docker we can’t escalate it if we don’t have access to local network.

Timeline:
- March 16, 2024 — VDP Annouced
- March 17, 2024 — Initial Report
- March 25, 2024 — Triaged
- March 27, 2024 — Fixed

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: https://x.com/PhHitachi
LinkedIn: www.linkedin.com/in/phhitachi

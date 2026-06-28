---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-21_fastly-subdomain-takeover-2000.md
original_filename: 2022-11-21_fastly-subdomain-takeover-2000.md
title: Fastly Subdomain Takeover $2000
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- api-security
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- api-security
language: en
raw_sha256: b040d9f084dd8199a1cd98651db278a2f5ef7c25ea67be53a2fd43aa7afad684
text_sha256: 328cec26616927bc0e831e7ad9ff155cfa9722441aefb967369ebe291c2c4aa3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Fastly Subdomain Takeover $2000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-21_fastly-subdomain-takeover-2000.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `b040d9f084dd8199a1cd98651db278a2f5ef7c25ea67be53a2fd43aa7afad684`
- Text SHA256: `328cec26616927bc0e831e7ad9ff155cfa9722441aefb967369ebe291c2c4aa3`


## Content

---
title: "Fastly Subdomain Takeover $2000"
url: "https://medium.com/@valluvarsploit/fastly-subdomain-takeover-2000-217bb180730f"
authors: ["ValluvarSploit (@ValluvarSploit)"]
bugs: ["Subdomain takeover"]
bounty: "2,000"
publication_date: "2022-11-21"
added_date: "2022-11-22"
source: "pentester.land/writeups.json"
original_index: 1883
scraped_via: "browseros"
---

# Fastly Subdomain Takeover $2000

Fastly Subdomain Takeover $2000
Bug Bounty — From zero to HERO
ValluvarSploit
5 min read
·
Nov 21, 2022

--

13

--

WHOAMI

My name is Alexandar Thangavel AKA ValluvarSploit, a full-time bug hunter and trainer. I love recon. I am the founder and CEO of ValluvarSploit Security. At ValluvarSploit Security, we are providing Bug Bounty training in one-to-one online session. For more information, please check our LinkedIn page.

OBJECTIVE

Today, I am going to share how I found Fastly subdomain takeover vulnerability and earn my first four digits bounty. Let’s get started.

BACKSTORY

This was started on October 2nd, 2022 Sunday. The day started as usual. I woke up at 6 AM, finished routine work, checked my Mobile data balance (1.3 GB was remaining), enabled my Mobile Hotspot, connected my Laptop, and resumed hunting on a private program. I spent a few hours on the target application but found nothing so took a short break. I used to revisit my old private programs at least once in six months. So, I reviewed my private invites, picked an old program and started performing subdomain enumeration (Let’s call our target as redacted.com).

SUBDOMAIN TAKEOVER

Subdomain takeover occurs when an attacker take control over a subdomain of a domain. It happens because of DNS misconfiguration / mistakes.

SUBDOMAIN ENUMERATION

I started subdomain enumeration with Google Dorking, OWASP Amass and Gobuster tools.

# Passive Subdomain Enumeration using Google Dorking
site:*.redacted.com -www -www1 -blog
site:*.*.redacted.com -product

# Passive Subdomain Enumeration using OWASP Amass
amass enum -passive -d redacted.com -config config.ini -o amass_passive_subs.txt

# Subdomain Brute force using Gobuster
gobuster dns -d redacted.com -w wordlist.txt - show-cname - no-color -o gobuster_subs.txt

After enumerating subdomains, removed duplicate entries and merged them into a single file (subdomains.txt) using the Anew tool.

# Merging subdomains into one file
cat google_subs.txt amass_passive_subs.txt gobuster_subs.txt | anew subdomains.txt

Then passed the subdomains.txt file to my cname.sh shell script, enumerated CNAME records and stored in cnames.txt.

# Enumerate CNAME records
./cname.sh -l subdomains.txt -o cnames.txt

# We can use HTTPX tool as well
httpx -l subdomains.txt -cname cnames.txt

Then passed the subdomains.txt file to the HTTPX tool. probed live websites and stored in servers_details.txt.

# Probe for live HTTP/HTTPS servers
httpx -l subdomains.txt -p 80,443,8080,3000 -status-code -title -o servers_details.txt
ANALYSIS

I started analyzing the cnames.txt file and found one subdomain that was pointing to two different CNAME records. I ran dig command on the subdomain and got followings,

dig next.redacted.com CNAME
Press enter or click to view image in full size
DNS query for CNAME record

This subdomain had two CNAME records. The first CNAME record was pointing to webflow.io domain and the second CNAME record was pointing to fastly.net (Fastly Service) domain. Whenever we have multiple CNAME records, the first CNAME record will redirect us to next CNAME record and so on. The redirection would continue until we reach last CNAME record.

I started analyzing the servers_details.txt file for interesting stuff and found this line. Notice status code and website title.

https://next.redacted.com [500] [246] [Fastly error: unknown domain next.redacted.com]

The status code was “500" and the title was “Fastly error: unknown domain next.redacted.com”. By taking a look at CNAME record (“redacted.fastly.net”) and website fingerprint “Fastly error: unknown domain”, we can confirm that this is Fastly Subdomain Takeover. If a website has this fingerprint then it may be vulnerable. However, I came across this Fastly fingerprint many times before and it was not vulnerable. It’s vulnerable only when certain conditions are met, so it’s an edge case.

Get ValluvarSploit’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In most cases, we cannot takeover the Fastly service. For example below case,

Press enter or click to view image in full size

But if the domain is not already taken by another customer then we can claim the domain and takeover the subdomain completely.

CONFIRMING THE VULNERABILITY

I went to Fastly official website and performed below steps,
1. I created an account on fastly.com using a temporary mail.
2. Logged in to my Fastly Dashboard and clicked on the “Create a Delivery Service” button.
3. Entered target subdomain name(next.redacted.com) and clicked on Add button.

I was expecting the error message (“domain is already taken by another customer”) to appear but there was no error message. I was redirected to the next page “Hosts page”. I was surprised.

Press enter or click to view image in full size
Claimed domain on Fastly
POC CREATION STEPS

Once the vulnerability was confirmed, I logged into my VPS server and created a directory called “hosting”. Then within the “hosting” directory created a simple HTML file called “index.html”.

mkdir hosting

cd hosting

nano index.html

“index.html” file contains below code,

<!DOCTYPE html>

<html>
  <head><title>STO PoC</title></head>
  <body>
  <h1>ValluvarSploit PoC</h1>
  </body>
</html>

After that, I started a simple Python web server on port 80 within the current working directory,

python3 -m http.server 80

Then I went to the Fastly dashboard and Added the public IP address of my VPS server in the Hosts page.

Press enter or click to view image in full size
VPS Configuration

After a few seconds, I opened up a new browser window and visited “http://next.redacted.com/index.html” page. My PoC file was rendered successfully. I have written a detailed report and submitted it on HackerOne.

Press enter or click to view image in full size
Proof of Concept
LEARNING BY MONITORING SERVER LOGS

I kept my Fastly service running for 3 days and monitored server logs for sensitive information. It was fun watching other bug hunters methodology.

Monitoring server logs for fun
REWARD

My report was triaged as a HIGH severity vulnerability and rewarded $2000 within 10 days.

Press enter or click to view image in full size
Reward
KEY TAKEAWAYS

1. Revisit your old targets at least once in 6 months.
2. Subdomain Enumeration is key. Enumerate subdomains as much as possible.
3. Don’t give up.

Thanks for taking time to read my write-up.

Follow Me on:

Twitter

LinkedIn

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

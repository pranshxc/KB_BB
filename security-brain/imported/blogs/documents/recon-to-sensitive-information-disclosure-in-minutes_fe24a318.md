---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-28_recon-to-sensitive-information-disclosure-in-minutes.md
original_filename: 2020-04-28_recon-to-sensitive-information-disclosure-in-minutes.md
title: Recon to Sensitive Information Disclosure in Minutes
category: documents
detected_topics:
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: fe24a318f158b666b6680ebbc8651b68871e3caa57df700468457c79cce4bb5e
text_sha256: 5146b4059213d490e3763cbfce7a4bfe188ab1f4fba0080ec45aa29c24af5d65
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Recon to Sensitive Information Disclosure in Minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-28_recon-to-sensitive-information-disclosure-in-minutes.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `fe24a318f158b666b6680ebbc8651b68871e3caa57df700468457c79cce4bb5e`
- Text SHA256: `5146b4059213d490e3763cbfce7a4bfe188ab1f4fba0080ec45aa29c24af5d65`


## Content

---
title: "Recon to Sensitive Information Disclosure in Minutes"
url: "https://medium.com/@hbothra22/recon-to-sensitive-information-disclosure-in-minutes-503fc7ccdf0b"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["Information disclosure", "Outdated component with a known vulnerability"]
publication_date: "2020-04-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4625
scraped_via: "browseros"
---

# Recon to Sensitive Information Disclosure in Minutes

Top highlight

Recon to Sensitive Information Disclosure in Minutes
Harsh Bothra
Follow
3 min read
·
Apr 28, 2020

414

1

Previously at this Post, I talked about a critical security vulnerability as a result of Recon. Reconnaissance plays an important role and this blog focuses on building your recon strategy and talks about a Medium Severity security vulnerability discovered while performing initial reconnaissance.

Bigger Picture

Subdomain → Running older version of Splunk → Google Search → Found CVE-2018–11409 → Not for the version I found but still tried → Sensitive Information Disclosed!

The below infographic is also details the issue I found:

Press enter or click to view image in full size
Splunk Sensitive Information Disclosure

Now, let’s take a deeper dive into how I found this domain and how should you approach the similar-looking endpoints while doing recon. The original report is resolved but not yet disclosed so let’s call the company target.com

I bumped into this program and it had a wide scope of domains. One of the domains was target.com and all subdomains were in-scope. Whenever I see, *.target.com, the only thing I focus on major is to finding bugs with Recon.

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here’s a little strategy that I use:

Subdomain Enumeration with Multiple Tools (Aquatone, Amass, Subfinder)
List all subdomains in a file say target.txt and grab all unique subdomains with the following command (Linux): cat target.txt |sort -u
Manually visit each domain and create a separate list of domains which hosts some third party applications, some micro applications, blogging or CMS platforms, gateways (like VPN gateways), SSO Authentication pages, etc.
In the end, from a huge list of domains, I am left with some specific domains which might have the juicy stuff.
Start picking up third-party services because the main way you can get your report accepted is if the third party application deployed is known as vulnerable and exploitable to that vulnerability. For example- Splunk, in this case, was not under the control of the organization but the organization was not using the latest version of Splunk which makes the report valid.
Report — Triage — Accepted — Bounty — Thank me Later ;)

So, keeping the above strategy in mind, I did the same stuff with this *.target.com and found risk.target.com to be using an older version of Splunk.
Performed some google search to find out the CVEs and Public Exploits for the Splunk version. Some of the search terms I used are:

Splunk <version_goes_here> CVEs
Splunk <version_goes_here> Exploit-DB
Splunk <version_goes_here> Security Bulletins

But no luck :/

Further, I removed the version and found a CVE and Exploit but they were not applicable to the version I found. But what’s bad in trying the exploit right, you never know your lucky day :P

So, I went ahead and tried the exploit mentioned here https://www.exploit-db.com/exploits/44865.

Navigated to “risk.target.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json” and another easy win!

We have the underlying server information, license keys, licensing information and other things.

Prepared a report and reported via Bugcrowd. The submission was accepted as a P3 and fixed the same day.

Takeaways
Always look out for EXPLOITS and CVEs
Keep an eye on trending & new Exploits and CVEs
Create your own Recon Process to fasten up things

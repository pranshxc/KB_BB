---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-24_from-recon-to-p1-critical-an-easy-win.md
original_filename: 2020-04-24_from-recon-to-p1-critical-an-easy-win.md
title: From Recon to P1 (Critical) — An Easy Win
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: 7801303ca0a2296b5a4cfd5c9e75949b2e45e5dff60d2cfe6de5d831587e8908
text_sha256: 27832881d2bed395e0fce8f69267d842962db0478e9c2a0932c54bebaf47322c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# From Recon to P1 (Critical) — An Easy Win

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-24_from-recon-to-p1-critical-an-easy-win.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `7801303ca0a2296b5a4cfd5c9e75949b2e45e5dff60d2cfe6de5d831587e8908`
- Text SHA256: `27832881d2bed395e0fce8f69267d842962db0478e9c2a0932c54bebaf47322c`


## Content

---
title: "From Recon to P1 (Critical) — An Easy Win"
url: "https://medium.com/@hbothra22/from-recon-to-p1-critical-an-easy-win-6ca93d5b6e6d"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["Exposed registration page"]
publication_date: "2020-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4634
scraped_via: "browseros"
---

# From Recon to P1 (Critical) — An Easy Win

From Recon to P1 (Critical) — An Easy Win
Harsh Bothra
Follow
3 min read
·
Apr 24, 2020

500

4

Reconnaissance is an important phase when you do an application assessment, especially to gather in-depth knowledge about your target application. For obvious reasons, Reconnaissance holds importance especially when it comes to a huge scope. From discovering more attack surface to getting critical data with no complexations, reconnaissance is always an easy win.
Hey Fellow Pentesters, I will be talking about an easy discovery for a critical severity (P1) security issue just with Recon. It was a private program on Bugcrowd, to keep confidentiality, let’s call it “target.com”

Bigger Picture

— — — — — —

The application had a huge scope — *.target.com
No specific application URL was out of scope
Subdomain Enumeration to increase the attack surface
Finding juicy domains to work on
Discovering directories with directory Bruteforce
Discovering hidden endpoints with Bruteforce
Manipulating application logic to bypass Email Validation
Critically Sensitive Data ~ Easy Win!

During the initial phase of testing, whenever I see something like “*.target.com”, I start subdomain discovery with multiple tools like Aquatone, Subfinder, Amass. (Multiple tools sometimes vary in 2–3 domains not discovered in others, so always ensure at least to run two tools).

While going through each of the subdomains, I found one interesting subdomain — “portal-intra.target.com”. Upon inspection, I came to the conclusion that this portal is meant to be used for the internal use of the company. Okay, so time to gear up. :D

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
I fired dirsearch and interestingly found a directory named “administration”. Visiting this directory, it had the login URL which looked like — “portal-intra.target.com/administration/login.php”. Again, tried some default credentials to login but failed :/

Next thing that came up in the mind was to find if the application by chance have the “registration page” and on further Bruteforcing, found the endpoint — “portal-intra.target.com/administration/reg.php”

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and that’s where your blood starts pumping high.

I tried registering a new account but failed because there was validation which was allowing only emails with “@target.com”. Fired Burp Suite & captured the request, changed the email from “harsh@target.com” to my “Gmail account”, forwarded the request and, logged in.

I was logged in to their intranet portal which had all their customer sensitive information, inventories, marketing plans, and critically sensitive business information. It was surely going to be a critical and easy win :D ;)

Created a good looking report and submitted it to the organization on Bugcrowd.

{P.S.: This is my first public writeup, please share your views to improve}

Few Takeaways

— — — — — — -
1. Make your Recon Strong

2. Try to think out of the box while trying to exploit your target

3. I always start with Subdomain whenever there is a huge scope and I keep my notes, shortlist all the subdomains which feels juicy. I start parallel recon on those juicy subdomains like parameter search, directory Bruteforce, CVE, and exploit search.

4. If you know how to Recon properly, you will be a step ahead and it’s always an easy win. :)

Bug Timeline

— — — — — — —

Reported — 19th April 2020

Triaged — 21st April 2020

Accepted — 21st April 2020

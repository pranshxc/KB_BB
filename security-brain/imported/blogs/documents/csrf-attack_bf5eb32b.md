---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-04_csrf-attack.md
original_filename: 2020-07-04_csrf-attack.md
title: CSRF Attack!!!
category: documents
detected_topics:
- api-security
- idor
- command-injection
- otp
- rate-limit
- csrf
tags:
- imported
- documents
- api-security
- idor
- command-injection
- otp
- rate-limit
- csrf
language: en
raw_sha256: bf5eb32bcd97ad8dfb299a57044543f489bfb47a77500984ab9db17c6a02f5ee
text_sha256: 24ff3cb33a0d75be83fb3b004a050f86361a52439b3892702a204ca44ba43acd
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF Attack!!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-04_csrf-attack.md
- Source Type: markdown
- Detected Topics: api-security, idor, command-injection, otp, rate-limit, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `bf5eb32bcd97ad8dfb299a57044543f489bfb47a77500984ab9db17c6a02f5ee`
- Text SHA256: `24ff3cb33a0d75be83fb3b004a050f86361a52439b3892702a204ca44ba43acd`


## Content

---
title: "CSRF Attack!!!"
url: "https://balapraneeth.medium.com/csrf-attack-e7bb9f3f36e1"
authors: ["Bala Praneeth (@Begin_hunt)"]
bugs: ["CSRF"]
bounty: "500"
publication_date: "2020-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4445
scraped_via: "browseros"
---

# CSRF Attack!!!

CSRF Attack!!!
Bala Praneeth (Begin_hunt)
Follow
2 min read
·
Jan 4, 2021

59

1

Hey guys, Hope you are doing well.

In this article, I’m going to share my recent finding which was mostly about the enumeration part. So without any further delay let’s dive in.

Enumeration -
I picked a target from Bug crowd assume it as redacted.com (coz everyone mentions that way :). The specialty of this program is you are able to view any previously submitted vulnerabilities by other security researchers. On viewing this list there were no CSRF bugs reported. This gave me a better opportunity to look for CSRF.
Press enter or click to view image in full size
Type of Vulnerability!!
Tools Used -

The main tool I use for finding a CSRF vulnerability is Burp. Burp has a CSRF POC generator which makes our work easier.

Attacking -

1. Started enumerating the application directly without any reconnaissance ( not a recon guy ).

2. The application had a development domain wherein it implements the same backend logic as that of the main application. The only difference here is you get to choose a demo version.

3. Started to register to create an account and checked every request in burp.

Get Bala Praneeth (Begin_hunt)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. The application’s data was transferred in JSON. So tried to bypass CSRF token protection but had no luck.

5. On successful registration, the application offered a feature to link a demo Bank. This seemed interesting. Instantly started to check this feature.

6. At the final bank login endpoint I saw something missing ( Guess what. It’s a CSRF token )

Finally!!!

7. Simply crafted the payload using burp POC generator and made the victim click on it.

8. This allowed linking a demo bank account with respect to the victim. Reported the bug to the company and was awarded with $500

Press enter or click to view image in full size
Submission Reward!!!
Takeaways -
While hunting for CSRF the best technique is to check for every API endpoint which might be vulnerable.

Hope this write-up was helpful. Collaboration and networking is something that I always enjoy. Let’s connect

Twitter — https://twitter.com/Begin_hunt

Linkedin — https://www.linkedin.com/in/balapraneeth/

Happy hacking !!!
If you have reached this far, thank you for reading this article. Kindly feel free to point out any mistakes and do let me know where I can improve in writing and explaining in detail. Appreciate it!!. All the best. God bless

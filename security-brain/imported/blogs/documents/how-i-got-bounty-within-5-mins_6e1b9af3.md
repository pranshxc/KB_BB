---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-09_how-i-got-bounty-within-5-mins_2.md
original_filename: 2023-02-09_how-i-got-bounty-within-5-mins_2.md
title: How I got $$$$ Bounty within 5 mins
category: documents
detected_topics:
- command-injection
- file-upload
tags:
- imported
- documents
- command-injection
- file-upload
language: en
raw_sha256: 6e1b9af3deaff29c393b9ed02250993b1fc4741484d634b98fb6e4141a6f0d31
text_sha256: 8733502e77d1e3b8cfdfb10894e337c952ce646de88cdf53978fa3e7aad3246b
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $$$$ Bounty within 5 mins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-09_how-i-got-bounty-within-5-mins_2.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `6e1b9af3deaff29c393b9ed02250993b1fc4741484d634b98fb6e4141a6f0d31`
- Text SHA256: `8733502e77d1e3b8cfdfb10894e337c952ce646de88cdf53978fa3e7aad3246b`


## Content

---
title: "How I got $$$$ Bounty within 5 mins"
page_title: "RCE — Telerik UI. Hi folks, Usually I don't do writeups… | by p4n7h3rx | Medium"
url: "https://p4n7h3rx.medium.com/how-i-got-bounty-within-5-mins-f1448f6db9b5"
authors: ["Hashir Khan (@P4n7h3Rx)"]
bugs: ["RCE", "Components with known vulnerabilities"]
publication_date: "2023-02-09"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1555
scraped_via: "browseros"
---

# How I got $$$$ Bounty within 5 mins

Top highlight

RCE — Telerik UI
p4n7h3rx
Follow
2 min read
·
Feb 9, 2023

367

5

Hi folks, Usually I don't do writeups or share anything related to bug bounty. From now I will be sharing my experience and knowledge & hope it will add some value to your Bug Bounty journey ❤

Who I am?

My name is hashir khan aka p4n7h3rx and I’m a Self Learned Penetration Tester & Bug Bounty Hunter. I have performed Penetration Testing on many national and international Banking, Financial, Government, Health, and many tech giant organizations.

Summary

I was hunting on a bug bounty target while fuzzing I saw the website is using Telerik UI and it was vulnerable to Base64-based encryption oracle exploit for CVE-2017–9248 (Telerik UI for ASP.NET AJAX dialog handler). In which the attacker can upload a shell on the website file manager. I have used the dp_crypto tool for exploitation.

Vulnerable Endpoint

Telerik.Web.UI.DialogHandler.aspx

Vulnerability

Get p4n7h3rx’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This exploit attacks a weak encryption implementation to discover the dialog handler key for vulnerable versions of Telerik UI for ASP.NET AJAX, then provides an encrypted link that gives access to a file manager, and arbitrary file upload (e.g. web shell) if remote file permissions allow. Works up to and including version 2017.1.118.

python3 dp_crypto.py k -u https://test.example.com/Telerik.Web.UI.DialogHandler.aspx
Press enter or click to view image in full size
dp_crypto Exploitaion

After visiting the URL

Press enter or click to view image in full size
File Manager

Now upload the Aspx shell on the file manager .

Shell I used :

https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/asp/cmd.aspx
Press enter or click to view image in full size
Navigate to aspnet_cmd/cmd.aspx

Final Notes:

if you have any queries feel free to reach out to me on Linkedin or Twitter till then happy hacking!

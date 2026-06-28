---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-17_stored-xss-with-arbitrary-cookie-installation.md
original_filename: 2017-09-17_stored-xss-with-arbitrary-cookie-installation.md
title: Stored XSS] with arbitrary cookie installation
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 5e523ea4419d9d3a5cd624121b121d1296b3655b371194b8ee53c9f8931faa33
text_sha256: c2eb4a5ed0bdfa00b6ecb31e97d436ab603a9afe0aec44a78cbba8910bc2802d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS] with arbitrary cookie installation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-17_stored-xss-with-arbitrary-cookie-installation.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5e523ea4419d9d3a5cd624121b121d1296b3655b371194b8ee53c9f8931faa33`
- Text SHA256: `c2eb4a5ed0bdfa00b6ecb31e97d436ab603a9afe0aec44a78cbba8910bc2802d`


## Content

---
title: "Stored XSS] with arbitrary cookie installation"
page_title: "[Stored XSS] with arbitrary cookie installation | by Arbaz Hussain | Medium"
url: "https://medium.com/@arbazhussain/stored-xss-with-arbitrary-cookie-installation-567931433c7f"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["XSS"]
publication_date: "2017-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6103
scraped_via: "browseros"
---

# Stored XSS] with arbitrary cookie installation

[Stored XSS] with arbitrary cookie installation
Arbaz Hussain
Follow
1 min read
·
Sep 17, 2017

122

1

Severity : Medium
Complexity : Easy
Weakness : Trusting the cookies values without sanitizing malicious input.
While Testing one of the Hackerone Program , the value of the Parameter refclickid from url was getting stored in response cookie’s.
https://redacted.com/mobile-app/?refclickid=xxxxxxxxxxxxxx
Press enter or click to view image in full size
Here problem was the value of refclickid is getting stored in Set-Cookie:Referral=CLICKID=XXXXXX

And Application was storing the same Reference Click ID taking from cookie value to Response of the Body in JSON format under <SCRIPT> TAG’s without any sanitizing user input on each and every page.

Attack Scenario :
Attacker Send’s Victim Following URL to Set Refclickid value as XSS Payload in the cookies.
https://redacted.com/mobile-app/?refclickid=%3C%2FScRipt%3E%3CScRipt%3Eprompt(document.domain)%3B%2F%2F.

2. Set-Cookie Value has been Saved with XSS Payload .

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. When Victim Visit’s https://redacted.com/ or Any Page Under Redacted.com without any parameter XSS is Fired because Response of the Body Takes the Value of Stored Cookie and Saves them under <script> Tag’s.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-31_credential-disclosure-in-lastpass.md
original_filename: 2024-07-31_credential-disclosure-in-lastpass.md
title: Credential Disclosure in LastPass
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- clickjacking
- api-security
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- clickjacking
- api-security
language: en
raw_sha256: 3e198f74475c4abd18e2b4c6f08f7f38705b0c2b28e02e73fc1d3fbbd4441a9a
text_sha256: 6a7a8c447e9229a247d48f1a916ecd147808eb9ff2d0ebc0bb43155d9668c7de
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Credential Disclosure in LastPass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-31_credential-disclosure-in-lastpass.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `3e198f74475c4abd18e2b4c6f08f7f38705b0c2b28e02e73fc1d3fbbd4441a9a`
- Text SHA256: `6a7a8c447e9229a247d48f1a916ecd147808eb9ff2d0ebc0bb43155d9668c7de`


## Content

---
title: "Credential Disclosure in LastPass"
page_title: "Credential Disclosure in LastPass – Certitude Blog"
url: "https://certitude.consulting/blog/en/credential-disclosure-in-lastpass/"
final_url: "https://certitude.consulting/blog/en/credential-disclosure-in-lastpass/"
authors: ["Wolfgang Ettlinger"]
programs: ["LastPass"]
bugs: ["Clickjacking"]
publication_date: "2024-07-31"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 118
---

# Credential Disclosure in LastPass

Written by [Wolfgang Ettlinger](https://certitude.consulting/blog/en/author/wet/) on [31.07.202431.07.2024](https://certitude.consulting/blog/en/credential-disclosure-in-lastpass/)

**LastPass was susceptible to a clickjacking attack. By intercepting traffic, an attacker would have been able to harvest login credentials of LastPass users. LastPass rejected the issue.**

In October 2022, Certitude discovered an issue in the LastPass password manager browser plugin. We analyzed the security properties of this plugin, particularly, we analyzed how LastPass deals with unencrypted connections (i.e. `http://`-connections). We found that the LastPass browser plugin, automatically fills in credentials on HTTPS sites. For example, when visiting `https://accounts.google.com`, LastPass automatically fills in the Google login credentials.

An interesting case is if the user accesses an unencrypted page, i.e. `**http** ://accounts.google.com`. As the domain matches Google’s, LastPass identifies the Google account credential entry as the one to fill in. However, as the page is unencrypted, LastPass refuses to **automatically** fill out the account details.

This behavior is e.g. necessary as it is impossible to verify that pages served through unencrypted connections are legitimate – anyone intercepting your traffic can pretend to be `**http** ://accounts.google.com`.

However, LastPass still offers to fill in these credentials manually, i.e. when a user manually selects the stored credential from the LastPass user interface. The user simply has to click the LastPass symbol shown inside the username or password filed, after which, the following dialog appears, allowing a user to insert the credentials anyway:

![](https://certitude.consulting/blog/wp-content/uploads/2024/03/image-2.png)

In the situation where an attacker impersonates the unencrypted version of google.com to gather the credentials, an attacker would have to bring the user to manually select the stored credential from this dialog (highlighted red). One way to bring a user to do something they don’t intend to do is via clickjacking.

Clickjacking makes user interface elements invisible and then brings users to interact with the, now hidden, user interface. As it turns out, LastPass’s account selection dialog can be hidden and clickjacking is possible!

Combining everything we discovered, we can create a scenario where an attacker harvests Google credentials in a public Wi-Fi:

  1. The attacker intercepts all traffic on the wireless network (e.g. using ARP spoofing, DHCP spoofing, etc.). 
  2. Whenever the attacker receives an unencrypted HTTP request, they respond with an HTTP redirect to `http://botprotect.google.com`, a non-existent site.
  3. The victim’s browser follows the redirect.
  4. The attacker serves a malicious website as a response to this request.
  5. The LastPass plugin identifies `http://botprotect.google.com` as a Google website, but does not auto-fill the credentials.
  6. The malicious page shows a fake CAPTCHA:  
![](https://certitude.consulting/blog/wp-content/uploads/2024/03/image-1-1024x327.png)  
The user is requested to click on a number of red dots. In reality, the user interacts with the LastPass user interface that is made invisible. The user inadvertently opens the LastPass account selection dialog and requests LastPass to fill in their Google credentials on the malicious site.
  7. The malicious site can now forward the victim’s Google credentials to the attacker.

## Responsible Disclosure

Certitude reported this issue in October 2022 through LastPass’s Bugcrowd program1. LastPass responded stating that only clickjacking submissions are accepted if a proof-of-concept is provided (this was provided with the initial submission). After clarifying that the vulnerability is not a typical clickjacking vulnerability one would identify on a website and referring to the initial proof-of-concept, no response was received.

In March 2023 we resubmitted the same advisory. After clarifying some questions, LastPass rejected the issue, referring to the then stipulation in their program’s terms rejecting these kinds of vulnerabilities:

> Attacks that rely on/have as a prerequisite successfully placing a man in the middle between our servers and the client. We take precautions in order to make these attacks difficult or infeasible (e.g. using HTTPS exclusively), but some aspects are out of our control and thereby excluded from eligibility.
> 
> <https://web.archive.org/web/20221201075948/https://bugcrowd.com/lastpass>

After re-checking the vulnerability, Certitude found that this vulnerability has since been fixed since. Certitude has not been credited with identifying this vulnerability.

  1. <https://web.archive.org/web/20221201075948/https://bugcrowd.com/lastpass> ↩︎

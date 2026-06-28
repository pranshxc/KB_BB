---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-26_hyperlink-injection-on-irc-cloud.md
original_filename: 2022-06-26_hyperlink-injection-on-irc-cloud.md
title: Hyperlink Injection On IRC Cloud
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 7eb5a7b0d093c23d27b50470fecbcec6b05d796f8ad061b91965db10f3186a99
text_sha256: c69def848fcd8b7de35a8ad5ef916fa6a4c6187d8cb02fdf4f54afe615dd8c1b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hyperlink Injection On IRC Cloud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-26_hyperlink-injection-on-irc-cloud.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `7eb5a7b0d093c23d27b50470fecbcec6b05d796f8ad061b91965db10f3186a99`
- Text SHA256: `c69def848fcd8b7de35a8ad5ef916fa6a4c6187d8cb02fdf4f54afe615dd8c1b`


## Content

---
title: "Hyperlink Injection On IRC Cloud"
page_title: "#hyperlink #hyperlink injection #what is hyperlink injection # sql injection #injection # penetration testing #bug bounty #hackerone #bugcrowd #html | Medium"
url: "https://medium.com/@deepmarketer/hyperlink-injection-on-irc-cloud-809e5243406f"
authors: ["Aswin K V (@deep_marketer_)"]
programs: ["IRCCloud"]
bugs: ["Hyperlink injection"]
publication_date: "2022-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2516
scraped_via: "browseros"
---

# Hyperlink Injection On IRC Cloud

Hyperlink Injection On IRC Cloud
Aswin K V
Follow
2 min read
·
Jun 26, 2022

363

What is Hyperlink Injection, its basically spoofing or injecting a link when sending an email invitation. Its a P5 according to bugcrowd, but some companies might consider it as a serious issue so report if you find it, might get paid.

Description

Hyperlink Injection vulnerability arises when the attacker’s injected hyperlink gets successfully sent in the emails. Majority of the times, this attack involves user interaction.

A user can change their name to a URL in order to send notification emails containing malicious hyperlinks.

Using this vulnerability, an attacker can abuse the target email system to send malicious emails to any user.

Impact:

It might lead to redirecting victim to a malicious website or download trojans/viruses on victim’s system.
proof of concept:
summary:

irccloud is such a trusted website.But there is a bug in the signup form where attacker can inject malicious links(html)and effect any user whim they targeted through email id.This results in the bad reputation to the company.

steps To Reproduce

Go to url :https://www.irccloud.com
Fill up the sign up form giving first names with malicious link or html code,

example :

Get Aswin K V’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

→ go to this link ​https://www.evil.com

→ <a href="evil.com">click here for pass</a>

3. Now give the victims email id and submit the form.

4. The victim will get mails from irccloud with malicious link injected.

Press enter or click to view image in full size
Impact

It might lead to redirecting victim to a malicious website or download trojans/viruses on victim’s system.

References:
HYPERLINK INJECTION/EMAIL INJECTION
Nginx is such a trusted website.It is famous for the security nginx is providing the customers.But there is a bug in…

trac.nginx.org

Instacart disclosed on HackerOne: Hyperlink Injection in Friend...
Description A user can change their name to a URL in order to send email invitations containing malicious hyperlinks. #…

hackerone.com

Helium disclosed on HackerOne: Hyperlink Injection on Email Invitation
DESCRIPTION Found an hyperlink injection of the name of Organization when the attacker invites the victim to his…

hackerone.com

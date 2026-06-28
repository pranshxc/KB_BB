---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-23_secstory-how-i-found-multiple-p1-vulnerabilities-without-recon_2.md
original_filename: 2022-07-23_secstory-how-i-found-multiple-p1-vulnerabilities-without-recon_2.md
title: 'SecStory: How I Found Multiple P1 Vulnerabilities without Recon'
category: documents
detected_topics:
- oauth
- sso
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- sso
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: e2b7e8d71e3a9590283ba83847e5981721924c297d90a22022b69053eb6bcc4a
text_sha256: 2a52cf9f6bcfedc59acad653e1f4b32e221168cb64e5abed7ed5a8fc518c14fc
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# SecStory: How I Found Multiple P1 Vulnerabilities without Recon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-23_secstory-how-i-found-multiple-p1-vulnerabilities-without-recon_2.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `e2b7e8d71e3a9590283ba83847e5981721924c297d90a22022b69053eb6bcc4a`
- Text SHA256: `2a52cf9f6bcfedc59acad653e1f4b32e221168cb64e5abed7ed5a8fc518c14fc`


## Content

---
title: "SecStory: How I Found Multiple P1 Vulnerabilities without Recon"
url: "https://medium.com/@rival.rvdt/secstory-how-i-found-multiple-p1-vulnerabilities-without-recon-c9f3a19cad45"
authors: ["rvdt (@rival_rvdt)"]
bugs: ["Broken authentication"]
publication_date: "2022-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2413
scraped_via: "browseros"
---

# SecStory: How I Found Multiple P1 Vulnerabilities without Recon

SecStory: How I Found Multiple P1 Vulnerabilities without Recon
rvdt
Follow
5 min read
·
Jul 23, 2022

180

2

Hello everyone. Nowadays, there are numerous bug hunting stories on the internet. For me, I’ve dubbed my experiences as my “SecStory,” which stands for “Security Story” wkwkwkwk.

Just to provide some context, I don’t dedicate all my time to bug hunting. I currently work full-time as a Jr. IT Security professional for a company. Furthermore, I’m not a part of the red team.

For those unfamiliar with bug hunting or red team concepts, terms like “Recon” and “P1” might be unfamiliar. Before we dive into my story, let’s clarify these terms.

Here are the terms used in this story:

“P” stands for “Priority,” so “P1” refers to “Priority One.” This indicates a vulnerability that needs immediate attention due to its high impact. Bugcrowd, a bug hunting platform, has released a table of vulnerability ratings known as the “vulnerability rating taxonomy.” You can find it at https://bugcrowd.com/vulnerability-rating-taxonomy.
“Recon” is short for “Reconnaissance.” You engage in reconnaissance when you gather information about a target, including its IP address, port, path, subdomain, tech stack, etc. This can involve using vulnerability assessment tools for tasks like fuzzing or scanning to identify vulnerabilities on the target. For more information, visit https://www.jigsawacademy.com/blogs/cyber-security/reconnaissance-in-hacking/

One of the largest platforms in Indonesia has a Responsible Disclosure program on their site. There are a total of 16 rules, consisting of 15 rules plus an additional one.

Responsible Disclosure Program
Background

Founded in 1999, this platform’s history includes clashes with hackers. The “Brontok” virus attack in 2006 and its prominence in cyber warfare in 2008 are notable, though I was just a child then.

How the story began

Due to its history, obtaining a P1 on their site could be challenging, given that they likely learned from their past experiences.

In 2022, 14 years later, I challenged myself to discover P1 vulnerabilities on the target without engaging in reconnaissance. I did this for two reasons:

To push my own boundaries
To meet the requirements of responsible disclosure
Using automation tools or scanners was not allowed.

As a result, I reported four vulnerabilities in a month without reconnaissance:

Two were P1 vulnerabilities (one was valid and fixed, while the other was not validated)
The remaining two were not P1 vulnerabilities

This story will focuses on the resolved P1 vulnerability. The Broken Authentication.

U
pon visiting the target site, the first thing I noticed was the responsible disclosure message. After reading it, I began analyzing the main apps, starting with the “forgot password” and login pages. Here are my findings:

The forgot password is protected by Captcha
Login page is not protected by Captcha
Register account is not protected by Captcha

With these observations in mind, I focused on the feature that wasn’t safeguarded by Captcha. At first glance, I saw they had an “oAuth” feature, which I believed had a small chance of being bypassed. Consequently, I moved past the second option and proceeded to the third.

oAuth (Facebook, Google & Twitter)

After investing time, I discovered my first P1 vulnerability. Unfortunately, this vulnerability didn’t get validated later on. So, I continued my search for another P1 vulnerability and found:

“Broken Authentication via Race Condition led to Bypass OTP”.

The normal flow happen when user requesting an OTP code, it was sent to the associated email address. This behavior seemed normal, prompting me to dig deeper. Eventually, I stumbled upon a way to change my email address, leading me to request another OTP code. Here’s what I discovered:

The OTP code in the previous and new email was identical.

This signaled a broken OTP authentication. Despite using a new email, the OTP code remained the same.

Input OTP Code

After inputting the OTP code, I successfully registered an account.

Registration Complete

So now, I have an account registered by using victim’s email. But I’m not yet finished and keep looking for the impact. Elon says “Keep shocking them”.

Get rvdt’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s go to the settings “privasi profil” in order to display victim’s email on the profile page.

Press enter or click to view image in full size
Settings menu “Privacy Profile”
Press enter or click to view image in full size
Display email on the profile

On the above picture I thick the checkbox on “Tampilkan di profil” or “Display in profile” which would make the victim’s email visible to the public. The public view of the profile account showed the displayed email as below picture.

Press enter or click to view image in full size
Profile account viewed as public

As shown in the picture above, displaying the email publicly can indicate that the registered account appears genuine as long as an attacker has information about the target email address.

Done.

Impact:
Theft identity
The ability for an attacker to register an account using the victim’s email.
Impersonation of various individuals, including celebrities, popular figures, VIPs, organizations, etc.
Potential damage to the reputation of celebrities, public figures, VIPs, and organizations by posting sensitive content, as the public would discover that the account has a legitimate email address.
Remmediation:
Generate a new OTP for each request.
At 19:53, the OTP was sent to the mailbox, and the attacker input the OTP code at 22:08. This means the OTP code remained valid for almost 3 hours. After conducting my research, I found that OTP codes usually expire after 12 hours. To enhance security, it’s advisable to limit the usage window of the OTP code to just 5 to 30 minutes.
References:
CWE-287: Improper Authentication
CWE-301: Reflection Attack in an Authentication Protocol
OWASP Top 10 (2017): Broken authentication
OWASP Top 10 (2021): Insecure Design
Eligible for Hall of Fame 2022

Currently, I stand alone in the Hall of Fame for 2022.

The company has granted me permission to share this story but certain details remain undisclosed.

Keep following along for my upcoming chapter where I explore another P1 vulnerability.

Stay alert, and may a sense of calm prevail.

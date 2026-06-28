---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-12_how-i-got-150-on-hackerone-for-my-first-bug.md
original_filename: 2024-08-12_how-i-got-150-on-hackerone-for-my-first-bug.md
title: How I Got $150 on HackerOne for My First Bug
category: documents
detected_topics:
- mfa
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- mfa
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: 64184a209c776d4a4a8ee3e1f3cce441696bbc2b438bd10007c9a7f0d595a589
text_sha256: 82b66d4b923f346a987454e9d5e82dd213788c6a677347a4d5453c6892f995d5
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got $150 on HackerOne for My First Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-12_how-i-got-150-on-hackerone-for-my-first-bug.md
- Source Type: markdown
- Detected Topics: mfa, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `64184a209c776d4a4a8ee3e1f3cce441696bbc2b438bd10007c9a7f0d595a589`
- Text SHA256: `82b66d4b923f346a987454e9d5e82dd213788c6a677347a4d5453c6892f995d5`


## Content

---
title: "How I Got $150 on HackerOne for My First Bug"
url: "https://medium.com/@likithteki76/how-i-got-150-on-hackerone-for-my-first-bug-8af0ed515e79"
authors: ["Likith Teki (@likith_teki)"]
bugs: ["2FA / MFA bypass"]
bounty: "150"
publication_date: "2024-08-12"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 78
scraped_via: "browseros"
---

# How I Got $150 on HackerOne for My First Bug

How I Got $150 on HackerOne for My First Bug
Likith Teki
Follow
3 min read
·
Aug 12, 2024

510

2

Hello everyone, I’m Likith Teki A bug bounty Hunter and Ethical Hacker

Getting started in bug bounty hunting can be both thrilling and challenging. When I discovered my first vulnerability on a private program and reported it, I wasn’t just excited about finding a flaw. I was also pleasantly surprised to receive $150 for my efforts. Here’s the story of how I found and reported this bug and what made it such a rewarding experience

Title: Incorrect 2FA Recovery Code Hygiene

In June 2024, I came across a issue in the management of 2FA (two-factor authentication) recovery codes within a private program on HackerOne. The vulnerability emerged when a user disabled and then re-enabled 2FA on their account. Unfortunately, the system continued to accept old recovery codes that were generated before the re-enabling of 2FA. This flaw allowed attackers to bypass the 2FA requirement entirely and gain unauthorized access to user accountsSteps to Reproduce the Bug

Enable 2FA: Set up 2FA on the account and generate recovery codes.
Save Codes: Securely store these recovery codes.
Disable 2FA: Disable turn off 2FA.
Re-enable 2FA: Reactivate 2FA on the account.
Sign Out: Log out of the account.
Login Attempt: Try logging back in using one of the old recovery codes.

Despite re-enabling 2FA, the old recovery codes still worked, making it easy for an attacker to bypass the security measure.

The Impact:

This vulnerability could have serious consequences. An attacker with old recovery codes could bypass 2FA, leading to unauthorized account access. This could result in data breaches, loss of sensitive information, and unauthorized actions taken on behalf of users.

How I Reported It and What Happened Next

After discovering this issue, I promptly reported it on HackerOne. The process was straightforward: I provided a detailed description of the bug, steps to reproduce it, and its potential impact. The response from the security team was positive, and I was awarded $150 for my findings. This was not just a financial reward but also a significant milestone in my bug bounty journey.

Press enter or click to view image in full size
Lessons Learned and Recommendations
Always Test Thoroughly: Even after re-enabling security features like 2FA, make sure to test the entire system thoroughly.
Be Detail-Oriented: Provide clear and comprehensive reports to help the security team understand the issue and its implications.
Stay Updated: Keep an eye on security practices and updates to ensure vulnerabilities are promptly addressed.
Conclusion

Reporting my first bug and receiving a reward was an incredibly gratifying experience. It underscored the importance of meticulous security testing and reinforced my commitment to finding and reporting vulnerabilities. If you’re considering diving into bug bounty hunting, remember that every bug you find and report contributes to a safer online environment for everyone.

Get Likith Teki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thank you So much for reading! Happy Hacking!

Connect with me:

Twitter: @likith_teki
LinkedIn: likithteki

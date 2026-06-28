---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-23_staff-and-triage-can-modify-the-initial-post-of-a-report.md
original_filename: 2023-09-23_staff-and-triage-can-modify-the-initial-post-of-a-report.md
title: Staff and Triage can modify the initial post of a report
category: blogs
detected_topics:
- command-injection
- business-logic
tags:
- imported
- blogs
- command-injection
- business-logic
language: en
raw_sha256: 6ed7ca6ff38ede8c80b3f915557751be428f991b3b6621b08aeb393b6349b422
text_sha256: aac1d02a5dc02bce230b9e6f428ddba439d2c3d4f83afc97151121100fb44c1c
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Staff and Triage can modify the initial post of a report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-23_staff-and-triage-can-modify-the-initial-post-of-a-report.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `6ed7ca6ff38ede8c80b3f915557751be428f991b3b6621b08aeb393b6349b422`
- Text SHA256: `aac1d02a5dc02bce230b9e6f428ddba439d2c3d4f83afc97151121100fb44c1c`


## Content

---
title: "Staff and Triage can modify the initial post of a report"
url: "https://medium.com/@abhinavsecondary/staff-and-triage-can-modify-the-initial-post-of-a-report-ed99b1f1d9d3"
authors: ["Abhinav Kumar (@abhinavsecond)"]
programs: ["HackerOne"]
bugs: ["Logic flaw"]
publication_date: "2023-09-23"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 750
scraped_via: "browseros"
---

# Staff and Triage can modify the initial post of a report

Staff and Triage can modify the initial post of a report
Abhinav Kumar
Follow
2 min read
·
Sep 22, 2023

21

Introduction:

In the world of cybersecurity and bug bounty programs, maintaining trust and integrity is paramount. Hackers and security researchers submit their findings in the form of reports, and these reports serve as a critical piece of the puzzle in identifying and addressing vulnerabilities. However, I hhave discovered a vulnerability within bug bounty platforms(HackerOne) that could compromise this trust. This article explores one of my finding about an issue where triagers or team members can edit a hacker’s report without their consent and discusses the importance of ensuring report integrity.

The Vulnerability:

I highlighted a significant concern within HackerOne platforms — the ability of triagers or team members to edit a hacker’s report. The vulnerability is simple to reproduce, making it a serious cause for concern.

Steps to Reproduce:

1. Create a dummy report on your dummy program.
2. Open the report as a team member.
3. You will see an edit option near the hacker’s report.
4. Using that option, edit the report.

Get Abhinav Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Anyone triager/team member with access to the report can modify its contents without the hacker’s knowledge or consent.

The Impact:

When a triager or team member can edit a hacker’s report, it jeopardizes the report’s integrity. The hacker has no way of knowing whether their submitted report was altered, potentially changing the nature of the vulnerability or its severity. This means that a hacker’s meticulously documented findings can be tampered with without any indication that changes have been made.

Thanks for reading

Abhinav

HackerOne Report Id — https://hackerone.com/reports/2061367

Twitter — https://twitter.com/abhinavsecond

Linkedin — https://www.linkedin.com/in/abhinav-kumar-6946b3221/

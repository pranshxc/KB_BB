---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-17_a-big-company-admin-panel-takeover-4500.md
original_filename: 2023-04-17_a-big-company-admin-panel-takeover-4500.md
title: A Big company Admin Panel takeover $4500
category: documents
detected_topics:
- oauth
- sqli
- command-injection
- mobile-security
tags:
- imported
- documents
- oauth
- sqli
- command-injection
- mobile-security
language: en
raw_sha256: 09c432d79650a62c80544b4350d1b7718c03beeaf156c87999390bd324827e4f
text_sha256: 9c2f7731f01ef96e6a2ac244e3073dd6e46b233427f433d190e838e2f3aae222
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# A Big company Admin Panel takeover $4500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-17_a-big-company-admin-panel-takeover-4500.md
- Source Type: markdown
- Detected Topics: oauth, sqli, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `09c432d79650a62c80544b4350d1b7718c03beeaf156c87999390bd324827e4f`
- Text SHA256: `9c2f7731f01ef96e6a2ac244e3073dd6e46b233427f433d190e838e2f3aae222`


## Content

---
title: "A Big company Admin Panel takeover $4500"
url: "https://medium.com/@nanwinata/a-big-company-admin-panel-takeover-4500-9520a6c83430"
authors: ["nanwn"]
bugs: ["Authentication bypass", "40x bypass", "Account takeover"]
bounty: "4,500"
publication_date: "2023-04-17"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1260
scraped_via: "browseros"
---

# A Big company Admin Panel takeover $4500

Top highlight

A Big company Admin Panel takeover $4500
nanwn
Follow
5 min read
·
Apr 17, 2023

326

Press enter or click to view image in full size
How does the story go?

It’s always starts with Shodan ( Again ) and it was simply a dork :

ssl:redacted.com "200"

And I think there are about 18 IPs listed on the list, then I randomly pick one of the IPs. After browsing the IP, it always redirects to Google login.

Press enter or click to view image in full size

Before running another test, I was not aware that the CVE mentioned was related to this vulnerability.

After conducting two tests on the following URLs:

redacted.com/admin
redacted.com/dashboard

I was redirected back to the OAuth login page, as shown in the screenshot. I did not expect that the next test would result in bypassing the OAuth login.

Then, I added a (/;/) in front of the admin page during another test. The page displayed as follows.

Press enter or click to view image in full size

I was surprised and immediately checked if it was just a page display or if the admin page had actually been bypassed. When I clicked on another page, the URL path returned to /auth/login. At this point, I was confused again :))). Then, I tried to make a request using Burp and got this result.

I apologize if the steps seem to jump around a bit after this point, because after checking the host on https://securitytrails.com, the subdomain that was pointed to the host/IP was the IP of an admin subdomain of this company. So, the next Burp request was for the subdomain, not the IP as before.

Press enter or click to view image in full size

As can be seen, the bypass was indeed valid and I was able to clearly read all the configurations in this admin panel. What surprised me was that this was a large company with millions of customer data.

I quickly reported this discovery, as I was already part of their private bug bounty program. After writing a detailed report, the HackerOne triage team processed the finding and forwarded it to the redacted team.

Press enter or click to view image in full size

And it was triaged.

However, I read the rules of this program. Several points made me wonder why the score changed to HIGH. I presented several facts that:

Get nanwn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Critical:

Unauthorized access to gain full control over any systems, sub-systems, end-user account
Ability to access or modify end-user’s financial information (credit card ) or PII Information
Code execution on production systems housing sensitive data and functionality
Unauthorized access to administrative portals used in production
SQL Injection with significant impact on production systems or mobile applications
Authentication bypass to access production system or database

Points 1, 2, 4, and 6 have been met, so is not difficult to obtain a score of Critical 10.0. The CVE is 3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H.

And security team confirm it :

Press enter or click to view image in full size

Yes, I succeeded and was entitled to receive maximal cvs score.

Then, the security team confirmed that this vulnerability is related to CVE-2022–41923. The vulnerability found in the unpatched Grails Spring Security Core (GSSC) plugin can result in improper privilege management.

GitHub - grails/GSSC-CVE-2022-41923
The vulnerability CVE-2022-41923 found in the unpatched Grails Spring Security Core (GSSC) plugin can result in…

github.com

1–2 weeks after being triaged, the company awarded me the maximal bounty.

The team also confirmed that the patch deployment had been completed and after I tried to log in again, I could no longer access the admin panel. Patched!

Actually, this could be a big news story because if it were discovered by a malicious actor, it could lead to a major data breach starting in 2023. The data breach in question includes customer data such as credit cards, virtual cards, a 21 million database of redacted, 5 million transaction, company server configurations, and other important data.

CVE-2022–41923

bypass : /;/role/show/1 or /;/admin

Shodan : http.title:”Welcome to Grails”

Conclusion:

The security of web applications is crucial for any organization, especially when it comes to sensitive data. Recently, Redacted Company has been found to have a vulnerability in Admin Panel endpoints, which can lead to an Admin Panel takeover. This vulnerability has been assigned CVE-2022–41923, and it is critical for the company to patch it immediately.

In the story, we can see the importance of having a bug bounty program in a company to detect and fix security vulnerabilities in their systems. A security researcher participating in a bug bounty program was able to discover a vulnerability in the Grails Spring Security Core (GSSC) plugin that could cause improper access management in a large company. After being reported, the vulnerability was addressed by the security team and a patch was implemented to fix it. This demonstrates that bug bounty programs can help companies improve their system security and encourage better security testing practices overall.

Timeline:

Reported: Apr 3rd

Triaged: Apr 4th.

Bounty: Apr 12th

Have fun.

Nan Winata

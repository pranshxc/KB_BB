---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-24_flywheel-subdomain-takeover.md
original_filename: 2021-06-24_flywheel-subdomain-takeover.md
title: Flywheel Subdomain Takeover
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: ccb13ca430d998bacf890ae90170ea364c67613178fd5716f7a7a799cac3dbc1
text_sha256: ebd4a643cfccd42841ccc5960d7c8600c51165b4e7cba5b7e0083a2ee2947bb3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Flywheel Subdomain Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-24_flywheel-subdomain-takeover.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `ccb13ca430d998bacf890ae90170ea364c67613178fd5716f7a7a799cac3dbc1`
- Text SHA256: `ebd4a643cfccd42841ccc5960d7c8600c51165b4e7cba5b7e0083a2ee2947bb3`


## Content

---
title: "Flywheel Subdomain Takeover"
page_title: "Flywheel Subdomain Takeover – Smaran Chand"
url: "https://smaranchand.com.np/2021/06/flywheel-subdomain-takeover/"
final_url: "https://smaranchand.com.np/2021/06/flywheel-subdomain-takeover/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["Subdomain takeover"]
publication_date: "2021-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3548
---

[June 24, 2021](https://smaranchand.com.np/2021/06/flywheel-subdomain-takeover/)

# Flywheel Subdomain Takeover

Flywheel is managed WordPress hosting built for designers and creative agencies to build, scale, and manage hundreds of WordPress sites with ease. One can set up a WordPress site in less than two minutes without any complex configuration. But Flywheel PaaS is vulnerable to subdomain takeover issues, I am publishing this write-up because I didn’t find any [fingerprints](https://github.com/EdOverflow/can-i-take-over-xyz)/[writeups](https://www.google.com/search?q=flywheel+subdomain+takeover) regarding this anywhere on the internet. So thought to do it for the infosec community.

I discovered this issue last year during the security assessment/ VAPT project; since I didn’t found any resources or information about the Flywheel subdomain takeover issue, I chose to give it a try on my own.

By reading the [Flywheel Documentation](https://getflywheel.com/wordpress-support/how-to-point-your-domain-or-dns-to-flywheel/) and mechanism to verify domains, I was almost sure that this is a potential subdomain takeover but I planned to create a proper proof of concept.

The vulnerable subdomain homepage looked like this:

![](https://smaranchand.com.np/wp-content/uploads/2021/06/1.png)Flywheel default 404 landing page.

The vulnerable subdomain had an A record pointed to Flywheel PaaS.

![](https://smaranchand.com.np/wp-content/uploads/2021/06/2.png)Subdomain pointed to Flywheel PaaS IP address.

I created an account at <https://getflywheel.com/> and purchased a plan to test the subdomain takeover issue. (It was a gamble of $15)

Created a simple wordpress site with minimal effort.

![](https://smaranchand.com.np/wp-content/uploads/2021/06/test-700x251.png)Test instance at flywheel.

Tried connecting subsdomain with wordpress instance.

![](https://smaranchand.com.np/wp-content/uploads/2021/06/sbd-1.png)Add subdomain to wordpress site.

And here we go.

![](https://smaranchand.com.np/wp-content/uploads/2021/06/tko.png)Subdomain takeover successful.

Since there aren’t any resources or writeups regarding the Flywheel subdomain takeover issue, I planned to do a writeup as well as create a [nuclei template](https://github.com/projectdiscovery/nuclei-templates) for the detection of this vulnerability. Hope to see this template in the nuclei repository soon. For now, below is the template to use.
  
  
  id: Flywheel-Takeover
  
  info:
  name: Flywheel Subdomain Takeover
  author: smaranchand
  severity: high
  tags: takeover
  reference: https://smaranchand.com.np/2021/06/flywheel-subdomain-takeover
  
  requests:
  - method: GET
  path:
  - "{{BaseURL}}"
  matchers:
  - type: word
  words:
  - "We're sorry, you've landed on a page that is hosted by Flywheel"
  - "<h1>Oops! That's not the site<br>you're looking&nbsp;for.</h1>"
  condition: and

Save the content as anything.yaml and use it with [nuclei](https://github.com/projectdiscovery/nuclei).

![](https://smaranchand.com.np/wp-content/uploads/2021/06/Screen-Shot-2021-06-24-at-4.13.08-PM.png)Running nuclei template to detect flywheel subdomain takeover 

**Severity:** High

**Impacts:** An attacker can use this misconfiguration to takeover the subdomain, publish arbitrary contents, run malicious javascript code at the user’s end, harvest credentials using phishing attack, deface a website, etc also steal the cookies of the user if cookies are scoped to the parent domain and escalate to account takeover.

**Remediation:** The DNS entry for the subdomain should be removed from DNS records if not in use.

Do share if you liked, Let me know if you have any questions regarding this.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/), [Research](https://smaranchand.com.np/writeups/researchs/)

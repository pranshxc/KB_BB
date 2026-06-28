---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-01_denial-of-service-in-the-protection-service-provided-by-avast-security-premium.md
original_filename: 2020-09-01_denial-of-service-in-the-protection-service-provided-by-avast-security-premium.md
title: Denial of Service in the protection service provided by Avast Security Premium.
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: cf2a3b11a34463368a9ffec9ee6287b5c3b8788ed3f63a58111a42b25c360e4a
text_sha256: 9d0ab59737c9df37852d3d59eb819e6969e94d1a6b4a3c4b00921b3e0149e93a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Denial of Service in the protection service provided by Avast Security Premium.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-01_denial-of-service-in-the-protection-service-provided-by-avast-security-premium.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `cf2a3b11a34463368a9ffec9ee6287b5c3b8788ed3f63a58111a42b25c360e4a`
- Text SHA256: `9d0ab59737c9df37852d3d59eb819e6969e94d1a6b4a3c4b00921b3e0149e93a`


## Content

---
title: "Denial of Service in the protection service provided by Avast Security Premium."
url: "https://medium.com/stolabs/denial-of-service-in-the-protection-service-provided-by-avast-security-premium-284dfd5ab40"
authors: ["Silton Santos"]
programs: ["Avast"]
bugs: ["DoS"]
publication_date: "2020-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4284
scraped_via: "browseros"
---

# Denial of Service in the protection service provided by Avast Security Premium.

Denial of Service in the protection service provided by Avast Security Premium.
Silton Santos
Follow
3 min read
·
Sep 2, 2020

85

1

That’s my first blog post in Stolabs, and I would like to share with you a bug that I found in the Avast Sandbox, allowing a denial of service (DoS) attack against the protection service.

For those who don’t know, Avast has a security suite called Avast Premium Security, including a Sandbox promising to run binaries in a virtual environment and preventing any (malicious) changes from being made in the host machine.

Although it looks simple, this bug is interesting as it reflects a phrase of Koret and Bachaalany in The Antivirus Hacker’s Handbook:

[…]A typical computer user may view the AV software as a simple software suite, but an attacker must be able to view the AV on a deeper level.[2015]

In short, an attacker must look beyond the normal antivirus operation, searching for all the exploitation possibilities.

The following report describes a corner case — a software operating condition not predicted by the developer — that, as mentioned, results in a denial of service in all the protection applications offered by the security suite.

While performing an analysis in the Sandbox and realizing that it can virtualize any software execution, the following idea came up: What would happen if all the protection service binaries were to be executed in the sandbox itself?

Get Silton Santos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Performing the aforementioned action and restarting the computer, the sandbox attempted to insert the entire security system into the sandbox itself, resulting in raising an exception and stopping all services. It is worth mentioning that, in normal conditions, an unprivileged user has no permission to stop/interrupt the service or end the process (using Windows task manager).

However, the following question arises: How to automate this action? Luckily, Avast offers a feature that allows you to always run a binary in the sandbox. This feature can be accessed through the Windows check menu by right-clicking any .EXE binary, as shown below:

Press enter or click to view image in full size
Image 1. Check menu functionality to include executable in Sandbox

In order to include all the Avast executables in the Sandbox in an automated way (by enabling the Always run in sandbox option), a Powershell script was created, as depicted in the following image:

Press enter or click to view image in full size
Image 2. Powershell script allowing to include all Avast protection binaries in the Sandbox

By executing this exploit in an unprivileged user session, all Avast protection binaries were successfully included in the Sandbox and, after restarting the computer, the service was no longer started. As proof of concept, the following video illustrates the script execution on a Powershell terminal. However, this script could easily be incorporated into a malware causing denial of service to the entire Avast protection system:

The aforementioned vulnerability was responsibly disclosed to Avast, which in turn accepted the bug, requested some time to create a fix, and offered a reward.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-25_outdated-php-version-leads-to-rce.md
original_filename: 2022-07-25_outdated-php-version-leads-to-rce.md
title: Outdated PHP Version leads to RCE
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 02e80c76c00314796ff582f6d7055249f193310790b2bc1d9a6beb1c2831870d
text_sha256: 097c7564b42278caa04be49030f71ee9518004cff57fb3aff08353a68af08634
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Outdated PHP Version leads to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-25_outdated-php-version-leads-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `02e80c76c00314796ff582f6d7055249f193310790b2bc1d9a6beb1c2831870d`
- Text SHA256: `097c7564b42278caa04be49030f71ee9518004cff57fb3aff08353a68af08634`


## Content

---
title: "Outdated PHP Version leads to RCE"
url: "https://medium.com/@iamdevansharya/outdated-php-version-leads-to-rce-380fb4db32f4"
authors: ["iamdevansharya (@iamdevansharya)"]
bugs: ["RCE", "Old components with known vulnerabilities"]
publication_date: "2022-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2402
scraped_via: "browseros"
---

# Outdated PHP Version leads to RCE

Outdated PHP Version leads to RCE
iamdevansharya
Follow
3 min read
·
Jul 25, 2022

115

2

Hi Everyone, back again with my one more Bug Bounty write-up. This time i got a Remote code execution vulnerability in a Private Bug Bounty Program.

Press enter or click to view image in full size
What is RCE?

RCE is a vulnerability in which an attacker can execute malicious code or commands on a target machine.

Types of RCE
Generic RCE: The output of the command/code executed is returned in the response. An id or whoami commands are enough to validate this type of Remote Code Execution.
Blind RCE: The output of the command/code executed will not be displayed in the response. A best way to validate a Blind RCE is to execute the sleep command and check if the application actually sleeps for a specified time before returning the response.

Impact of Remote Code Execution

Add, read, modify, delete files
Change access privileges
Turn on and off configurations and services
Communicate to other servers
My Scenario of RCE:-

During the recon on the program, I saw that the server header leak the PHP version.

Press enter or click to view image in full size

So i search it over google to see if I can see anything interesting.

Press enter or click to view image in full size

Looking at the results, I saw that there is a backdoor that allows us to perform remote code execution. This backdoor was related to the Zend PHP framework.

Reference: https://www.exploit-db.com/exploits/49933

This appears to be a remote command execution vulnerability due to a backdoor that was left in this version of the software.

Get iamdevansharya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Basically, if “zerodium” was added as a user agent (this header needs to be renamed or add a new header i.e “User-Agentt” for this to work), any text after it would be interpreted and executed as a system command.

So i tried to enter one more User-Agent,

User-Agentt: zerodiumsystem(“id”);

Press enter or click to view image in full size
Press enter or click to view image in full size

BOOM ..!! 🤩🤩…Got the RCE

Bounty=$$$$

Mitigation
Operating Systems and third-party software need to be updated regularly.
Validate and sanitize user entries and inputs.

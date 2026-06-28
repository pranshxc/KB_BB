---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-26_sd-pwn-part-4-vmware-velocloud-the-last-takeover.md
original_filename: 2020-11-26_sd-pwn-part-4-vmware-velocloud-the-last-takeover.md
title: SD-PWN Part 4 — VMware VeloCloud — The Last Takeover
category: documents
detected_topics:
- command-injection
- path-traversal
- sqli
- file-upload
- password-reset
- otp
tags:
- imported
- documents
- command-injection
- path-traversal
- sqli
- file-upload
- password-reset
- otp
language: en
raw_sha256: 5f3b2222c1462ff4aeafddfb0edb234fbea9687528fb9cd9361c956132209624
text_sha256: f37f4744eb17b5fcbcdb1bae0c748440e7e29be571d27782bb02e69ffe097350
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# SD-PWN Part 4 — VMware VeloCloud — The Last Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-26_sd-pwn-part-4-vmware-velocloud-the-last-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, sqli, file-upload, password-reset, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `5f3b2222c1462ff4aeafddfb0edb234fbea9687528fb9cd9361c956132209624`
- Text SHA256: `f37f4744eb17b5fcbcdb1bae0c748440e7e29be571d27782bb02e69ffe097350`


## Content

---
title: "SD-PWN Part 4 — VMware VeloCloud — The Last Takeover"
url: "https://medium.com/realmodelabs/sd-pwn-part-4-vmware-velocloud-the-last-takeover-a7016f9a9175"
authors: ["Realmode Labs (@RealmodeLabs)"]
programs: ["VMware"]
bugs: ["RCE", "Authentication bypass", "Default credentials", "SQL injection", "Path traversal", "LFI"]
publication_date: "2020-11-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4107
scraped_via: "browseros"
---

# SD-PWN Part 4 — VMware VeloCloud — The Last Takeover

SD-PWN Part 4 — VMware VeloCloud — The Last Takeover
Ariel Tempelhof
Follow
5 min read
·
Nov 27, 2020

8

This is the last part of our SD-PWN series where we present severe vulnerabilities in four of the leading SD-WAN vendors. This time focusing on VMware’s SD-WAN platform.

If you haven’t read the previous posts you’re highly encouraged to:

Part 1 — Silver Peak Unity Orchestrator

Part 2 — Citrix SD-WAN Center

Part 3 — Cisco Viptela vManage

If you use VMware VeloCloud Orchestrator make sure you update immediately. As we’re going to demonstrate, the issues below lead to unauthenticated remote code execution. The ramifications, as with the other products we covered in this series, can be used to disrupt the entire international network of a company.

VMware VeloCloud Orchestrator

VMware VeloCloud Orchestrator connects to the edge routers and centrally controls the network topology. This is why it is a crucial single point of failure from a security perspective.

Press enter or click to view image in full size

The VeloCloud infrastructure consists of nginx serving mainly as a reverse proxy for node.js servers.

If it looks random, swims like it’s random, and quacks like it’s random, is it random?

One of the first steps in a security survey of a product is to map out the unauthenticated interfaces it exposes. The obvious ones are the login & password reset.

The general password reset concept is pretty straightforward:

Generate one of the two:
• A random unique key that can’t be predicted
• A signed token
Send it using a predefined side channel that is assumed to be in the sole possession of the user (E-mail or SMS)
Prompt the user to enter the random key

In step 1 Velocloud made two grave mistakes.

Velocloud, instead of generating random bytes for the reset key, probably looked at the users table in their database and said to themselves “Hey, we need some random bytes, here are some seemingly random bytes — the user’s hashed password, why not use this?”

Furthermore, they did implement an encrypted, signed token, but also added an option to use an unsigned cleartext one using the {CLEAR} prefix.

These two issues constitute what is known as Pass The Hash Attack.

But how do we know the hashed password you ask? Normally, we will try and find other vulnerabilities for DB data extraction, namely SQL injections.

But this is where it becomes interesting. Velocloud has used a practice we’ve seen less of in the past years. They added predefined backdoor users.

To be fair, the backdoor users are disabled by default, and probably no one except Velocloud knows their passwords, only their hashed values. However, the PTH Attack allows us to use the hashed password during the password reset procedure which also reenables the user.

These three issues lead to the first CVE.

Authentication bypass using PTH + default accounts — CVE-2020-4001

Using the previously described procedure we were able to reset the super@velocloud.net account possessing the highest admin rights in the system and after doing so it was no longer disabled. The attacker’s prior knowledge is:

super@velocloud.net’s hashed password
A parameter called logicalId

Both are predefined and can be obtained from the installation files. These values do not change between instances of the system.

Get Ariel Tempelhof’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This issue leverages all the rest and allows them to be run by an unauthenticated party.

Modulus parameter SQL Injection — CVE-2020-3984

This is a standard SQL injection vulnerability in which user controlled data is being concatenated to an SQL query without escaping any characters. One of the places this is happening is the softwareUpdate/getSoftwareUpdates method using the modulus parameter. This SQLi enables us to extract any data from the DB (it is non-blind).

Rest Meta Dir Traversal + Unauthenticated File Inclusion — CVE-2020-4000

The portal/rest/meta handler uses req.originalUrl to get the request method. The originalUrl is then being used to require a file. Now, putting a .. sign in the path itself will be resolved by the webserver and omitted, but originalUrl includes the full GET query string, including the GET parameters. Using urls with .. after the ? sign will result in directory traversal.

/portal/rest/meta/none?test/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/%2E%2E/somefile.js

This primitive enables us to execute almost any JavaScript file on the local disk.

Although this issue is exposed to an unauthenticated attacker, we haven’t found an unauthenticated way to upload a file so that it can be included. We tried to think about ways to deliver js code from the network instead of the disk (e.g. using /proc/self/fd/*), but that didn’t work and we already found the other vulnerabilities which were enough. If you have any voodoo Linux tricks that can help require controlled content without dropping a file to disk we would love to hear from you.

RCE Chain

We haven’t found any straightforward shell injections. Our main approach was to utilize the file inclusion vulnerability by uploading a JavaScript file with controlled content. Still, all places involving a file upload had restrictions on the content. Then we looked at the generic file upload module and we’ve noticed that uploaded files which didn’t pass the content verification are not being deleted.

The filename is randomly generated and not being returned to the user. The only part that was aware of the filename was the logger module. Thankfully Velocloud added the feature of setting the syslog server of the device. So this is our RCE chain:

Reset super@velocloud.net’s password (thus enabling it)
Login using the newly enabled account
Set our own server as the system’s syslog server
Upload a JavaScript file
Receive the random filename using an incoming syslog message
Use the Rest Meta file inclusion to require the JavaScript file

This will lead to our JavaScript code running in node.js . Here is the POC script:

RealmodeLabs/SD-PWN
VMware Velocloud Orchestrator RCE

github.com

Closing Remarks

This concludes our SD-PWN series. If you look at the SD-WAN products that are out there, there’s something they have in common that we thought should get some notice. Many of them are products that originated in startups and were later acquired by large companies.

Silver Peak was acquired by HPE, Viptela by Cisco and VeloCloud by VMware. Talari was acquired by Oracle but it looks like Citrix shares some of their codebase.

The thing is that startup companies usually put less emphasis on securing their products. They need to build a system from scratch, they have tight development schedules, code is often left unreviewed and sometimes shortcuts are made.

The truth of the matter is that some of the issues were trivial, some were more complicated, but they were all bugs that could have been found and fixed by a standard security review.

This is why a security focused pair of eyes need to inspect crucial parts of the code. No one wants to read about their product having vulnerabilities like these in a post on a security blog, or much worse, discover it being used in the wild.

If you are interested in auditing your products, or performing special security research you can find us on Twitter, LinkedIn or contact us at contact@realmodelabs.com

This is not a goodbye. Our next post will be focused on an everyday gadget many of us use (we would love to hear your guesses) and how we found some interesting, yet disturbing, issues with it. Stay tuned.

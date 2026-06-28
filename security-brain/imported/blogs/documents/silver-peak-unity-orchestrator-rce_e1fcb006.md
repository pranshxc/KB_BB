---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-08_silver-peak-unity-orchestrator-rce.md
original_filename: 2020-11-08_silver-peak-unity-orchestrator-rce.md
title: Silver Peak Unity Orchestrator RCE
category: documents
detected_topics:
- command-injection
- api-security
- ssrf
- sqli
- path-traversal
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- ssrf
- sqli
- path-traversal
- cloud-security
language: en
raw_sha256: e1fcb0065c5f2214734b6d8a82bfe615a6b2632258046c024ada58810482be16
text_sha256: 7cc664f983c845804c7c40ca4e7005c5827ba449d253491d376927aecba23e57
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Silver Peak Unity Orchestrator RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-08_silver-peak-unity-orchestrator-rce.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, ssrf, sqli, path-traversal, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e1fcb0065c5f2214734b6d8a82bfe615a6b2632258046c024ada58810482be16`
- Text SHA256: `7cc664f983c845804c7c40ca4e7005c5827ba449d253491d376927aecba23e57`


## Content

---
title: "Silver Peak Unity Orchestrator RCE"
url: "https://medium.com/realmodelabs/silver-peak-unity-orchestrator-rce-2928d65ef749"
authors: ["Realmode Labs (@RealmodeLabs)"]
programs: ["Silver Peak"]
bugs: ["RCE", "Authentication bypass", "Path traversal", "SQL injection"]
publication_date: "2020-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4151
scraped_via: "browseros"
---

# Silver Peak Unity Orchestrator RCE

Silver Peak Unity Orchestrator RCE
Ariel Tempelhof
Follow
3 min read
·
Nov 8, 2020

112

SD-WAN is a big deal. Gartner calls it the “replacement for traditional WAN routers”. But with great power comes great responsibility. Here at Realmode Labs, we researched the top four SD-WAN products on the market and found major remote code execution vulnerabilities. The vulnerabilities require no authentication whatsoever to exploit. In the best case scenario, an attacker can use these vulnerabilities to intercept or steer traffic. However, if an attacker desires, they can instead shutdown a company’s entire international network.

This is a four part series — in each post we’ll disclose another vulnerability in a major SD-WAN vendor. First up is Silver Peak. Gartner calls Silver Peak a “leader in the Magic Quadrant for WAN Edge Infrastructure” and they were recently acquired by HPE. But are they secure?

SD-PWN Part 1 — Silver-Peak Unity Orchestrator

Silver Peak is mostly remembered by us for having the best commercials of the lot:

First, some background. These vulnerabilities are in the Silver-Peak SD-WAN Orchestrator. An Orchestrator is the main management interface centrally controlling the SD-WAN topology of the company. This is obviously a crucial point from a security perspective. In order to gain remote code execution we discovered three different CVEs which join together to allow an attacker to SD-PWN the network.

Apart from Wayne McFarkus, examining Silver-Peak Unity Orchestrator revealed that the system runs on CentOS with JAVA applets running as the web server.

Authentication Bypass — CVE-2020–12145

Looking at the code handling the API calls, we’ve noticed special treatment for API calls originating from localhost where no authentication is being performed. Putting aside that this is probably a bad idea (it can really help in case of SSRF), after further examination we reached the point where the localhost check is being performed:

request.getBaseUri().getHost().equals(“localhost”)

Any requests with “localhost” as their HTTP Host header will satisfy this check. This can be easily forged in remote requests of course.

File Delete Path Traversal — CVE-2020–12146

Some of the API endpoints, which are now accessible thanks to the authentication bypass, allow the ability to upload debug logs to an S3 bucket to be examined by Silver Peak. This mechanism prepares the logs, uploads them and then deletes the locally hosted file. The /gms/rest/debugFiles/delete endpoint performing the deletion does not check for path traversal, creating the ability to delete any file on the system (if permissions allow).

Arbitrary SQL Query Execution — CVE-2020–12147

A special API endpoint exists to run arbitrary SQL queries. This endpoint is accessible only by localhost but same as in the Authentication Bypass this can be easily executed remotely.

Get Ariel Tempelhof’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The /gms/rest/sqlExecution endpoint can be leveraged to an arbitrary file write by utilizing an INTO DUMPFILE clause. INTO DUMPFILE does not allow overwriting a file but one can use the “File Delete Path Traversal” issue to first delete the file and then rewrite it.

Full RCE Chain

We didn’t find straightforward shell injections. But, by utilizing the three vulnerabilities, one can run arbitrary code using the following steps:

Look for a file being run by the web server
Delete it using the File Delete Path Traversal issue
Recreate it using the SQL Query Execution endpoint
Trigger the execution of the file

One such file found by us is /home/gms/gms/phantomGenImg.js. It’s part of a report generation process and it’s being run by PhantomJS. PhantomJS contains the child_process module making it possible to run arbitrary shell commands on the system.

The Script:

RealmodeLabs/SD-PWN
You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com

All issues found were disclosed to the respective vendors and resolved by the time of publication.

If you want to hear about the next SD-PWN vulnerability before everyone else then make sure you follow us on LinkedIn or contact us at contact@realmodelabs.com

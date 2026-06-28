---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-30_lfi-to-command-execution-deutche-telekom-bug-bounty.md
original_filename: 2017-11-30_lfi-to-command-execution-deutche-telekom-bug-bounty.md
title: 'LFI to Command Execution: Deutche Telekom Bug Bounty'
category: documents
detected_topics:
- command-injection
- sqli
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- sqli
- path-traversal
- api-security
language: en
raw_sha256: e766510b9307ff9ff782639b09cd9c7a87bc03ba8bc4f293a5574d6f2bdcb2ed
text_sha256: 27d61ab5deb78c10e74f9fddf37ff1280dfdd70f16338dbd357c33d3827f0156
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# LFI to Command Execution: Deutche Telekom Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-30_lfi-to-command-execution-deutche-telekom-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `e766510b9307ff9ff782639b09cd9c7a87bc03ba8bc4f293a5574d6f2bdcb2ed`
- Text SHA256: `27d61ab5deb78c10e74f9fddf37ff1280dfdd70f16338dbd357c33d3827f0156`


## Content

---
title: "LFI to Command Execution: Deutche Telekom Bug Bounty"
url: "https://medium.com/@maxon3/lfi-to-command-execution-deutche-telekom-bug-bounty-6fe0de7df7a6"
authors: ["Daniel Maksimovic"]
programs: ["Deutche Telekom"]
bugs: ["LFI", "RCE"]
publication_date: "2017-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6038
scraped_via: "browseros"
---

# LFI to Command Execution: Deutche Telekom Bug Bounty

LFI to Command Execution: Deutche Telekom Bug Bounty
Daniel Maksimovic
Follow
3 min read
·
Nov 30, 2017

406

11

Few months ago I did a little subdomain bruteforce on telekom.de , to see if there are new subdomains which, if I’m luck enough, could have some high severity vulnerabilities, since Deutche telekom only accepts SQL injection and Remote Code Execution.

After running aquatone, dnsenum, recon-ng and sublist3r, I collected all of the subdomains and removed duplicates, created a simple bash script to iterate over them and run dirb on every subdomain, and went on with my usual stalking of /r/netsec to read new interesting things.

Few hours later, I checked to see how dirb was doing and something caught my eye. I saw one subdomain had info.php page available. I just love php, developers usually mess up something, and leave some doors for hackers to come in. Opening info.php gave me some info that will be useful when Code Execution part comes.

Get Daniel Maksimovic’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After opening page I was greeted with login page. It was time to fire up BurpSuite and do some spidering. Few seconds later nice URL showed in burp :

https://netweb.telekom.de/netweb/gui/help.php?HELPFILE=logon.hlp

Oh, I just had to replace that logon.hlp with ../../../../../../../../etc/passwd=***REDACTED***

And Bingo:

Press enter or click to view image in full size
/etc/passwd output.

Some more files:

Press enter or click to view image in full size
/etc/release output.
Press enter or click to view image in full size
Part of report with LFI examples.

So LFI is fun, but it is not in scope, time to execute some command. I choose error.log poisoning option. So remember that info.php ( phpinfo()) file in the site root. It showed the location of error.log file, and made my job a lot easier, all the locations from SecList LFI list, gave 0 hits on the error.log file location. And in info.php it was:

https://netweb.telekom.de/netweb/gui/help.php?HELPFILE=../../../../../../../../../../../../../pkg/moip/netinfo/logs/apache-netweb-P/error.log

Press enter or click to view image in full size
error.log output

So while running dirb on host I found file soap.php, that showed some errors that ended inside error.log , and one of the data inside log was referer value.

Press enter or click to view image in full size
soap.php error inside error.log

Running simple test to see if referer value is executed:

Press enter or click to view image in full size
Running curl with referer value 0f 58–8 to see if value 50 is inside output.

And again Bingo:

58–8 evaluated and 50 is output inside error.log.

And for POC let’s run phpinfo() :

Press enter or click to view image in full size
setting referer to phpinfo() .

And output:

Press enter or click to view image in full size
phpinfo() executed inside error.log file

And the full report:

Press enter or click to view image in full size
Full report sent to Deutche Telekom Bug Bounty

Reported: April 10 2017
Fixed: Sometime in August

Daniel Maksimovic ( maxonebt4@gmail.com )
https://www.linkedin.com/in/daniel-maksimovic-73537882/

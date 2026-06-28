---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-04-26_magix-bug-bounty-magixcom-rce-sqli-and-xaracom-lfi-xss.md
original_filename: 2014-04-26_magix-bug-bounty-magixcom-rce-sqli-and-xaracom-lfi-xss.md
title: 'Magix Bug Bounty: magix.com (RCE, SQLi) and xara.com (LFI, XSS)'
category: documents
detected_topics:
- xss
- sqli
- command-injection
- path-traversal
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- command-injection
- path-traversal
- automation-abuse
language: en
raw_sha256: 301a108599e7213d577c02c3794429f001dd6948d810c7342c607c80d0f92e1e
text_sha256: c25a00c8414640a35f3f43ac12440312e30e7a0441b299e14a006b63558b3e87
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Magix Bug Bounty: magix.com (RCE, SQLi) and xara.com (LFI, XSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-04-26_magix-bug-bounty-magixcom-rce-sqli-and-xaracom-lfi-xss.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `301a108599e7213d577c02c3794429f001dd6948d810c7342c607c80d0f92e1e`
- Text SHA256: `c25a00c8414640a35f3f43ac12440312e30e7a0441b299e14a006b63558b3e87`


## Content

---
title: "Magix Bug Bounty: magix.com (RCE, SQLi) and xara.com (LFI, XSS)"
page_title: "Magix Bug Bounty: magix.com (RCE, SQLi) and … | RCE Security"
url: "https://www.rcesecurity.com/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/"
final_url: "https://www.rcesecurity.com/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Magix"]
bugs: ["RCE", "SQL injection", "LFI", "XSS"]
publication_date: "2014-04-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6373
---

# Magix Bug Bounty: magix.com (RCE, SQLi) and xara.com (LFI, XSS)

Apr 26, 2014 · By [Julien Ahrens](/about/)

The German Magix Software GmbH rewarded me with a [Hall of Fame](https://research.magix.com/) listing and a free Magix Music Maker 2014 Premium license for my reports of several serious security issues in the online infrastructures of magix.com and xara.com, which could be used to break both sites entirely:

![magix-hof](/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/images/magix-hof.24b5b7c581c05da5b6b67e59d0b0f3f302f9abeff083ebee4709320804a5c523.png)

At this point, I’d like to thank the Magix Security Team for their really fast and always transparent responses and the good coordination process as a whole. This is a perfect example of how the communication between the bug bounty operator and the researcher can satisfy both parties. The fixes for the critical vulnerabilities (RCE, SQLi, LFI) were implemented quite fast within only a few days after my initial report **(!)** , the fix for the XSS took a bit longer, but it’s still acceptable for a medium-severity issue.

Bug Bounty programs are always a great challenge and sometimes you’re rewarded with pretty cool stuff and great references like this - now here’s a short write-up about the discovered vulnerabilities, which already have been fixed by Magix.

### Remote Code Execution on europe.magix.com

This is the most dangerous flaw, I’ve found while working on this bug bounty program. I’ve discovered a script, that allows an attacker to upload zip files via a HTTP POST request. The script accepts any zip file, renames it to some temporary name and finally extracts the .zip file to a worker directory without checking if the zip file contains a valid file. Additionally, the extracted contents were accessible via www - I think the problem is quite obvious.

To prove the exploitability to Magix, I wrote a short Python script. The following snippet shows how the quite handy Python ZipFile function can be used to dynamically generate a zip file in memory. The .zip file contains one single file named “/tmp/test.php” with a custom PHP payload.
  
  
   #!/usr/bin/python
  import zipfile
  from StringIO import StringIO
  import zlib
  
  inMemoryFile = StringIO()
  
  zipFile = zipfile.ZipFile(inMemoryFile, 'w', zipfile.ZIP_DEFLATED) 
  zipFile.writestr('./tmp/test.php', '<?php echo \"www.rcesecurity.com\"; ?>')
  zipFile.close()
  

In case of Magix, the target script echoes some additional (and hazardous) debugging output after POSTing an arbitrary zip file: looks like Magix missed to deactivate this output - without this I wouldn’t have probably found this flaw :-)

![magix-rce-1](/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/images/magix-rce-1.b3e3458dc64e8d046cfdcca2ae5094340442ff22aaca4761c1d1c549d6f86373.png)

Since the debugging output also discloses the full-path of the extracted file, this leads to a nice RCE condition:

![magix-rce-2](/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/images/magix-rce-2.1c9353bc3611cb5c63617787ab02782aa54f7d9fab21c7e99c22396a23ff291e.png)

Now imagine an attacker who’d upload some malicious C99…

### SQL Injection on europe.magix.com

This vulnerability is more or less based on the same condition like the previously described RCE flaw. If the zip file contains a specially prepared .ini file, the same script, that is responsible for the RCE flaw, uses the .ini values unfiletered in a SQL query:

![magix-sqli](/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/images/magix-sqli.2ec891aa75e569433e4e7ec76f6139ac6ac4ecc39ed4be18b26a78831fda7e9b.png)

### Local File Inclusion on downloadsv9.xara.com

A local file inclusion could become as dangerous as a RCE flaw, because an attacker may read sensitive system files like /etc/passwd=***REDACTED***

…and if you’ve got a lazy sysadmin who likes to chmod 777 on files and directories, even more might by revealed ;-)

### Cross-Site Scripting on downloadsv9.xara.com

OK - I promised not to write about a XSS in detail anymore, so I’ll leave you with the PoC screenshot:

![magix-xss](/2014/04/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss/images/magix-xss.3a55fc291ad55c6118944ed3305793af9444a006fee3876316b7397a59a6e7e0.png)

A real happy day for bug bounty hunters and Magix!

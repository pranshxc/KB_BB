---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-17_openemr-5013-arbitrary-file-actions.md
original_filename: 2020-11-17_openemr-5013-arbitrary-file-actions.md
title: OpenEMR 5.0.1.3 Arbitrary File Actions
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
raw_sha256: 32393b4c67a710d41d5c5a779a60d48ec83678c7399bd44a38724ff481973661
text_sha256: e5add17e03de238691aba1796f6e3decc79df66d69589b4ab66a418c87ce6325
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# OpenEMR 5.0.1.3 Arbitrary File Actions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-17_openemr-5013-arbitrary-file-actions.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `32393b4c67a710d41d5c5a779a60d48ec83678c7399bd44a38724ff481973661`
- Text SHA256: `e5add17e03de238691aba1796f6e3decc79df66d69589b4ab66a418c87ce6325`


## Content

---
title: "OpenEMR 5.0.1.3 Arbitrary File Actions"
page_title: "OpenEMR 5.0.1.3 Arbitrary File Actions | JSECU"
url: "https://jsecu.github.io/2020/11/17/openemr/"
final_url: "https://jsecu.github.io/2020/11/17/openemr/"
authors: ["Josh Fam (@Pullerze)"]
programs: ["OpenEMR"]
bugs: ["Arbitrary file write", "Arbitrary file read", "Security code review"]
publication_date: "2020-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4123
---

## OpenEMR 5.0.1.3 Arbitrary File Actions

17 Nov 2020

![](../../../../images/openemr.png)

Back in 2018, a group of security researchers and I decided to try our hands at OpenEMR and find security vulnerabilities.The full report can be found [here](https://www.open-emr.org/wiki/images/1/11/Openemr_insecurity.pdf).This a very good read and I recommend reading it in its entirety. However this blog post is just documenting my contribution to the project.The following are the three CVEs I received in the collaboration. These were all responsibly disclosed and patched so upgrading to the latest version would be well advised.

1.CVE-2018-15140-Authenicated Arbitrary Read

Vulnerable Code:
  
  
  if ($_POST['mode'] == 'get'){
  echo file_get_contents($_POST['docid']);
  exit;
  }
  

This is a vulnerability that allows an attacker to make a malicious request to /portal/import_template.php on a unpatched instance of OpenEMR.The result of this request is an arbitrary file read of a local file located on the file system.This vulnerability was possible due to the application passing user input into file_get_contents() without any sanitization if the parameter mode is set with get as its value. This result of this input,which is the local file, was then echoed back in the html response.

2.CVE-2018-15142-Authenicated Arbitrary Write

Vulnerable Code:
  
  
  } else if ($_POST['mode'] == 'save') {
  file_put_contents($_POST['docid'], $_POST['content']);
  exit(true);
  }
  

This is an vulnerability in /portal/import_template.php which allows an attacker to write php files to a local file system.This works if the parameter mode is set to save.If that is the case the post parameters docid and content are passed to file_put_contents() without any sanitization.The docid is the file name and the content includes the malicious php code. This by itself doesn’t have that much impact since you cannot execute the file, but when paired up with the previously found arbitrary file read, leads to remote code execution.

3.CVE-2018-15141- Authenticated Arbitrary File Delete

Vulnerable Code:
  
  
  } else if ($_POST['mode'] == 'delete') {
  unlink($_POST['docid']);
  exit(true);
  }
  

This is an vulnerability also in /portal/import_template.php which allows an attacker to delete any file in the system if the filename is known and the permissions to delete are allowed.This is possible when the post parameter mode is set to delete. The docid parameter which contains the file name specified by the attacker is then passed to unlink() without sanitization.

Thank you for reading and hope you enjoyed.You can find Pocs for any one of these on ExploitDB, [here](https://www.exploit-db.com/exploits/45202)

  * [ __](https://www.facebook.com/sharer/sharer.php?u=jsecu.github.io)
  * [__](https://twitter.com/intent/tweet?&text=OpenEMR 5.0.1.3 Arbitrary File Actions+https://jsecu.github.io)
  * [__](https://plus.google.com/share?url=https://jsecu.github.io)
  * [__](https://www.linkedin.com/shareArticle?mini=true&source=OpenEMR 5.0.1.3 Arbitrary File Actions&summary=&url=https://jsecu.github.io)
  * [__](https://www.stumbleupon.com/badge/?url=https://jsecu.github.io)
  * [__](https://www.reddit.com/submit?url=https://jsecu.github.io)
  * [__](https://www.tumblr.com/share/link?url=https://jsecu.github.io)
  * [__](https://www.pinterest.com/pin/create/link/?description=&media=https://jsecu.github.io&url=https://jsecu.github.io)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-20_bug-writeup-fbctf-idor.md
original_filename: 2019-02-20_bug-writeup-fbctf-idor.md
title: 'Bug Writeup: FBCTF IDOR'
category: blogs
detected_topics:
- idor
- sso
- command-injection
- rate-limit
tags:
- imported
- blogs
- idor
- sso
- command-injection
- rate-limit
language: en
raw_sha256: a14e08cdb990112fff7dc1ce99362f854f13b623ab986d4738fc2213882d25f4
text_sha256: 8633ac7d2ebd2b0b3584dbbd426aa99163367f7a823c3041d578a7d882914775
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Writeup: FBCTF IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-20_bug-writeup-fbctf-idor.md
- Source Type: markdown
- Detected Topics: idor, sso, command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `a14e08cdb990112fff7dc1ce99362f854f13b623ab986d4738fc2213882d25f4`
- Text SHA256: `8633ac7d2ebd2b0b3584dbbd426aa99163367f7a823c3041d578a7d882914775`


## Content

---
title: "Bug Writeup: FBCTF IDOR"
url: "https://georgeosterweil.com/2019-02-20-fbctf-idor/"
final_url: "https://georgeosterweil.com/2019-02-20-fbctf-idor/"
authors: ["George Osterweil"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2019-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5399
---

### Introduction

This is a writeup for a bug I found a few months ago in Facebook’s Capture the Flag Platform (FBCTF). It was a fixed a while ago, so I’ll describe the bug and how I found it. I discovered this bug when participating in Facebook’s 2018 CTF and Bug Bounty Competition, an invite-only CTF for students involved with Facebook Security’s university initiatives. As the CTF was intended to test improvements to the FBCTF platform, bonus points were awarded to contestants who reported valid security vulnerabilities in the platform. Reporting the bug gave me a significant point advantage and ultimately helped me finish first place in the CTF.

The CTF organizers informed me that I could also submit the finding to Facebook’s regular bug bounty program. I did so, but was informed it had unfortunately already been reported a couple months prior.

### Background

FBCTF is a Capture the Flag platform written in Hack, a programming language written by Facebook which is based on PHP. As with most CTF platforms, FBCTF allows for flags to be set as inactive, meaning that they aren’t accessible to competitors yet. This allows new flags to be rolled out gradually during the competition, a common practice in CTF events. Flags can also have associated attachments, usually files like Wireshark .pcaps. These attachments usually will hide the flag somewhere in their content.

### POC URL

As an authenticated regular user, request:  
<https://example.com/data/attachment.php?id=xxx>  
Replace xx with the id of an inactive attachment, and it will be accessible. This parameter is sequential and easily brute forced.

### Vulnerability Description

The FBCTF platform prior to the most recent commit has an Insecure Direct Object Reference (IDOR) vulnerability in the endpoint `/data/attachment.php`.  
By changing the `id` GET parameter, any registered team can access a flag’s attachment, even if that flag is not active.

As mentioned in the introduction, flag attachments in a CTF event usually contain the flag itself. As such, teams exploiting this vulnerability could gain an unfair advantage in a CTF event by finding the flag before it’s active, and then submitting it the moment the flag becomes active. This would seriously compromise the competitive integrity of a CTF event due to the time advantage granted by early access to attachments.

### Exploit Steps

To reproduce this vulnerability, I used a Ubuntu 16.04 VM running the previous commit of FBCTF. I created two flags, one active and one inactive.  
![active flag](active_flag.png)

![inactive flag](inactive_flag.png)

To exploit the IDOR:

  1. Log in as a non-admin user
  2. From the gameboard, select an active flag.  
![flag dialog](active_modal.png)
  3. Click the attachment link below the description, and view the captured request in Burp. Right click and choose “Send to Repeater”.  
![active flag request](burp_1.png)
  4. Change the id parameter to the id of an inactive flag.
  5. You will see the flag’s attachment.  
![inactive flag request](burp_2.png)

### Affected Source

The vulnerability exists in the function genGenerateData() in [/data/Attachment.php](https://github.com/facebook/fbctf/blob/eb06ec4490593e14d6a2d2f09e3b1cd2229800ab/src/data/attachment.php#L6)  
The code does not check whether the flag is active before serving the attachment.
  
  
  $attachment_id = idx(Utils::getGET(), 'id', '');
  if (intval($attachment_id) !== 0) {
  $attachment_exists =
  await Attachment::genCheckExists(intval($attachment_id));
  if ($attachment_exists === true) {
  $attachment = await Attachment::gen(intval($attachment_id));
  $filename = $attachment->getFilename();
  // Remove all non alpahnum characters from filename - allow international chars, dash, underscore, and period
  $filename = preg_replace('/[^\p{L}\p{N}_\-.]+/u', '_', $filename);
  $data = file_get_contents(Attachment::attachmentsDir.$filename);
  }
  }
  $this->downloadSend($filename, $data);
  

In the fixed version, the developers added an active flag check:
  
  
  $attachment_exists =
  await Attachment::genCheckExists(intval($attachment_id));
  $active = await Attachment::checkActive(intval($attachment_id));
  if ($attachment_exists === true && $active === true)
  

### Disclosure Timeline

Sep 4, 2018: Reported to Facebook CTF and Bug Bounty Competition

Sep 5, 2018: Bug hotfixed in CTF event, bonus points awarded

Sep 6, 2018: Re-submitted report to Facebook Whitehat program

Sep 11, 2018: Response from Facebook: “We are working to reproduce your report”

Sep 11, 2018: Further response from Facebook: “The vulnerability was already reported to us by another researcher and we are working on a fix” Report closed

Sep 11, 2018: Fix pushed to FBCTF master branch on Github

Feb 19, 2019: Publicly disclosed

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232614'
original_report_id: '232614'
title: Uploaded XLF files result in External Entity Execution
weakness: XML External Entities (XXE)
team_handle: weblate
created_at: '2017-05-28T11:12:25.002Z'
disclosed_at: '2017-06-02T11:24:15.907Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- xml-external-entities-xxe
---

# Uploaded XLF files result in External Entity Execution

## Metadata

- HackerOne Report ID: 232614
- Weakness: XML External Entities (XXE)
- Program: weblate
- Disclosed At: 2017-06-02T11:24:15.907Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
========
 Weblate users in the Translate group (or those with the ability to upload translation files) can trigger XML External Entity Execution. This is a well known and high/critical vector of attack that often can completely compromise the security of a web application or in some cases lead to Remote Code Execution (although I do not expect it to be an easy RCE in this case).

Description:
========
The XML External Entity Execution allows for arbitrary reading of files on the server using a relatively obscure aspect of the XML language. It is generally considered high or critical severity, most notably Google places it at the same severity as remote code execution because of the potential for Server-Side Request Forgery, Remote Code Exection, and arbitrary File Read.

The mitigating factors here for you are that some account priveleges are required to upload tranlation files, although by default this gets rolled into the @Translate group. Also because your web server is python based it is not vulnerable to the trivial RCE that PHP servers are commonly vulnerable to.

The core of the vulnerability is in how the translate-toolkit processes .XLF files. The XLIFF standard is XML based, and thus supports by default standard XML functionality including external entity execution.

In my proof of concept, I dowloaded as .XLF the translations of the "hello" project which is being pointed to by my local Weblate instance. A minor modification shown in the steps below results in the /etc/passwd file out through the UI for review as a translation, although much worse things can be done - this is just to prove the vulnerability exists. For more details search for "XML External Entity Exploit"

See the attached screenshots and exploit XML file for evidence of the vulnerability.

Version:
========

I tested this against the latest stable source available a couple fo days ago (~May 26) running "Weblate 2.15-dev"

Steps to Reproduce
========
(I have included a live exploit testproject-testcomponent-en_GB.xlf that works with the "hello" data backing the demo website.)

* Log in as a user that has permission to upload translation files.
* Go to a component, and download its translations as XLF
* Add the following two lines after the "<?xml" tag, and replace one of the translation texts with "&xxe;" :

```
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
```
* Upload the file back to the server
* Observe the contents of the passwd file as a translation

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

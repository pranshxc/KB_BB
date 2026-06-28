---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-03_write-up-xss-stored-in-filesslackcom-via-xmlsvg-file-ios-1000-usd.md
original_filename: 2021-12-03_write-up-xss-stored-in-filesslackcom-via-xmlsvg-file-ios-1000-usd.md
title: Write Up – XSS Stored In files.slack.com Via XML/SVG File (iOS) – $1,000 USD
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 0616e1b8b84bc4816aef0ccffe43406f5c6220815ab4c5f4e06ee1bbaf53dc7e
text_sha256: 6705908b5f2bdd358e6d3af281c1824ed686d2fb4eadb4639bc2caa2f8646377
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – XSS Stored In files.slack.com Via XML/SVG File (iOS) – $1,000 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-03_write-up-xss-stored-in-filesslackcom-via-xmlsvg-file-ios-1000-usd.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `0616e1b8b84bc4816aef0ccffe43406f5c6220815ab4c5f4e06ee1bbaf53dc7e`
- Text SHA256: `6705908b5f2bdd358e6d3af281c1824ed686d2fb4eadb4639bc2caa2f8646377`


## Content

---
title: "Write Up – XSS Stored In files.slack.com Via XML/SVG File (iOS) – $1,000 USD"
page_title: "XSS STORED IN FILES.SLACK.COM VIA XML/SVG FILE (IOS) –  $1,000 USD – @omespino"
url: "https://omespino.com/write-up-xss-stored-in-files-slack-com-via-xml-svg-file-ios-1000-usd/"
final_url: "https://omespino.com/write-up-xss-stored-in-files-slack-com-via-xml-svg-file-ios-1000-usd/"
authors: ["Omar Espino (@omespino)"]
programs: ["Slack"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2021-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3117
---

MOBILE$1,000 USD[December 2021](/write-up-xss-stored-in-files-slack-com-via-xml-svg-file-ios-1000-usd/)

# XSS STORED IN FILES.SLACK.COM VIA XML/SVG FILE (IOS) – $1,000 USD

**Introduction**

Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about the Slack bug bounty program and why you can always check the basic payloads because you will surprise that some times will work 

**Title** XSS stored in https://files.slack.com iOS app / iOS browsers via xml/svg file.  
**Product / URL: ​** Slack iOS app / iOS browsers  
  
**Report sent via Slack’s hackerone program (this is the actual report):**

Hi ​Slack Security team.

I’ve found a XSS stored on file https://files.slack.com on iOS app / iOS browsers via xml/svg file.

**POC**

1.- Login to the slack team space and upload a xml file with the following content to any slack channel (slack-xss.xml file attached):
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <svg xmlns="http://www.w3.org/2000/svg">
  <script>prompt(document.location)</script>
  </svg>
  

2.- Look up for the xml file in the iOS app, see the snippet, click it to open the “raw view” and then open the option “View in Browser” and see the XSS.

3.- Also in the “raw view” you can copy the link to quick access to that file. (Note, if you want send the link in slack channel you need paste the copied link and append a space+string, for example “https:// files[dot]slack[dot]com/files-pri/XXXXXXXXX-XXXXXXXXX/slack-xss.xml[SPACE]xss”.

![](/assets/images/2021/07/slack_xss_omespino.webp)

Something important to highlight is: At this time you have a “magic” link that points directly to the special crafted XML document. ​

​4.- Open the link directly slack iOS app and the XSS shows up (if you open the link in any iOS browser like Safari, Firefox, Chrome, Opera the XSS works, you just need to be logged in your slack account, only works in iOS).

**Impact:**

Stored XSS allows an attacker to embed a malicious and arbitraries scripts into a vulnerable page, which is then executed when a victim views the page.

**Environment**

\- iPhone 6 – iOS v11.2.5.  
\- Safari Lastest version  
\- Google Chrome Lastest version  
\- My personal slack workspace / account and all testing was seding files to myself.

**Slack HOF (June 2019):  
**

<https://hackerone.com/slack/thanks/2018?type=team>

**Report Timeline**

****

**Feb 5, 2018: Sent the report to Slack team  
Feb 13, 2018: Got a message from the Slack team that the bug was triaged [ High (7 ~ 8.9)]  
Feb 14, 2019: $1,000 bounty rewarded (one year later! w0000t!)  
Jun 5, 2019: Fixed by Slack team**

[](/bug-bounty-writeups-collection/)

[](/write-up-apple-bug-bounty-n-a-arbitrary-local-file-read-via-zip-file-and-symlinks-usd/)

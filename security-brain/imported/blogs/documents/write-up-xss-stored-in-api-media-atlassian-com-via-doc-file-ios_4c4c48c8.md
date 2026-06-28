---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-28_write-up-xss-stored-in-apimediaatlassiancom-via-doc-file-ios.md
original_filename: 2021-10-28_write-up-xss-stored-in-apimediaatlassiancom-via-doc-file-ios.md
title: Write Up – XSS Stored In api.media.atlassian.com Via Doc File (iOS)
category: documents
detected_topics:
- xss
- sso
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- mobile-security
language: en
raw_sha256: 4c4c48c87847091004a1895a9fc2ab2369362096143edd995b482a9dcf2fc183
text_sha256: 272c41b3eace108548de692044c93e41898ff479f4e506b725399b96e1ecdf79
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – XSS Stored In api.media.atlassian.com Via Doc File (iOS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-28_write-up-xss-stored-in-apimediaatlassiancom-via-doc-file-ios.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `4c4c48c87847091004a1895a9fc2ab2369362096143edd995b482a9dcf2fc183`
- Text SHA256: `272c41b3eace108548de692044c93e41898ff479f4e506b725399b96e1ecdf79`


## Content

---
title: "Write Up – XSS Stored In api.media.atlassian.com Via Doc File (iOS)"
page_title: "ATLASSIAN BUG BOUNTY – XSS STORED IN API.MEDIA.ATLASSIAN.COM VIA DOC FILE (IOS) – @omespino"
url: "https://omespino.com/write-up-xss-stored-in-api-media-atlassian-com-via-doc-file-ios/"
final_url: "https://omespino.com/write-up-xss-stored-in-api-media-atlassian-com-via-doc-file-ios/"
authors: ["Omar Espino (@omespino)"]
programs: ["Atlassian"]
bugs: ["Stored XSS"]
publication_date: "2021-10-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3206
---

MOBILE$,$$$ USD[October 2021](/write-up-xss-stored-in-api-media-atlassian-com-via-doc-file-ios/)

# ATLASSIAN BUG BOUNTY – XSS STORED IN API.MEDIA.ATLASSIAN.COM VIA DOC FILE (IOS)

**Introduction**

Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about the Atlassian bug bounty program and why you can always check the basic payloads because you will surprise that some times will work: 

**Title** XSS stored on file https://api.media.atlassian.com on iOS browsers via msoffice (doc) file.Product / URL: ​Any associated *.atlassian.com or *.atl-paas.net domain that can be exploited DIRECTLY from the *.atlassian.net instanceReport sent via Bugcrowd Atlassian Program

Hi Atlassian team.

I’ve found a XSS stored on file https://api.media.atlassian.com on iOS browsers via msoffice (doc) file

**POC**

1.- Create a msoffice document per example a word office document with an hyperlink pointing to the url address “javascript:alert(1)//%22onclick=alert(2)//” and save as “Word 97-2003 Document”, Is very important save the doc as 97-2003, if you don’t save the document as this version the bug reproduction may not work.

2.-Look to any confluence public page (In my case I created a confluence test page with anonymous permissions https://bugbounty-test-omespino.atlassian.net) that allow post comments via anonymous user and post the document as a comment (XSS-iOS-omespino.doc file attached):

Something important to highlight is: At this time you have a “magic” link that points directly to the doc special crafted document. ​

3.- Copy the URL to the word document and paste it in any iOS browser like Safari, Firefox, Chrome, or Opera, then click the hyperlink and see the XSS shows up, since is a confluence public page, you don’t need to be logged in. 

**Impact:**

Stored XSS allows an attacker to embed a malicious and arbitraries scripts into a vulnerable page, which is then executed when a victim views the page.

**Environment**

\- iPhone 6 – iOS v11.2.5.  
\- Safari Lastest version  
\- Google Chrome / Safaria Lastest version  
\- My personal email account and all testing was seding emails to myself.

**Report Timeline**

Feb 19, 2018: Sent the report to Atlassian team  
Feb 21, 2018: Got a message from Atlassian team that they could not replicate the bug  
Feb 22, 2018: Sent clarification to Atlassian team  
Mar 05, 2018: Report triaged  
Mar 19, 2018: Fixed and rewarded

Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

****

****

****

****

****

****

****

****

[](/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/)

[](/write-up-google-vrp-n-a-arbitrary-local-file-read-macos-via-a-tag-and-null-byte-in-google-earth-pro-desktop-app/)

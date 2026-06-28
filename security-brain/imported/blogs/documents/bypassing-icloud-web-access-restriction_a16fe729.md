---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-21_bypassing-icloud-web-access-restriction.md
original_filename: 2024-06-21_bypassing-icloud-web-access-restriction.md
title: Bypassing iCloud Web Access Restriction
category: documents
detected_topics:
- access-control
- command-injection
- mfa
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- mfa
- api-security
- mobile-security
language: en
raw_sha256: a16fe729fd1de31345a12d0f6887cc74b6dbf6b8027a78c92fbd969c23fd9e4a
text_sha256: fe08083c659420d8a026eddf032e96f7a1669c8162d592f44a5737dc64131fae
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing iCloud Web Access Restriction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-21_bypassing-icloud-web-access-restriction.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `a16fe729fd1de31345a12d0f6887cc74b6dbf6b8027a78c92fbd969c23fd9e4a`
- Text SHA256: `fe08083c659420d8a026eddf032e96f7a1669c8162d592f44a5737dc64131fae`


## Content

---
title: "Bypassing iCloud Web Access Restriction"
url: "https://ltsirkov.medium.com/bypassing-icloud-web-access-restriction-30cdf12b979c"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["Apple (iCloud)"]
bugs: ["HTTP response manipulation", "iOS"]
publication_date: "2024-06-21"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 235
scraped_via: "browseros"
---

# Bypassing iCloud Web Access Restriction

Bypassing iCloud Web Access Restriction
Lyubomir Tsirkov
Follow
4 min read
·
Jun 21, 2024

61

Press enter or click to view image in full size

Today, I am going to share a short story about discovering a vulnerability in www.icloud.com that allowed me to bypass a security restriction using simple response manipulation.

It all started while I was browsing on my iPhone 14 Pro Max when I noticed an interesting feature called “Access iCloud Data on the Web.”

Press enter or click to view image in full size

When this feature is disabled, it’s supposed to restrict access to iCloud data via web browser.

Nevertheless, my analysis revealed that it was possible to bypass this restriction and access iCloud data through icloud.com, even when web access is disabled on a trusted device.

Thanks to Apple for allowing me to share this report.

Understanding the Feature

According to Apple’s support page https://support.apple.com/en-mt/102630, this feature ensures that “For additional security and to give you more control over your personal data, you can choose to turn off web access to your iCloud data so that your data is available only on your trusted devices.”

https://support.apple.com/en-mt/102630
Exploitation:

Prerequisites

“IOS 16.2, IpadOS 16.2, MacOS 13.1” with Access iCloud Data on the Web” turned off.
Browser.
Burp Suite (or a similar tool) to intercept and modify response.
The victim’s credentials
Access to the victim’s iPhone if 2FA is enabled
Steps to Reproduce

Note: The vulnerability has been fixed.

Disable Web Access:
On your iPhone, go to Settings -> iCloud and turn off the setting Access iCloud Data on the Web.

2. Open a web browser and go to iCloud.com.

3. Log in to your account.

4. You will be prompted with the following page:

Note: At this stage, you won’t be able to access any endpoints such as:

Icloud.com/mail
Icloud.com/notes
Icloud.com/iclouddrive

If you try, you would simply be redirected to the same “Restriction” page.

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. Now, the interesting part. Refresh the page and intercept response of request: “setup.icloud.com/ws/1/validate”

Change “isWebAccessAllowed” from false to true.

Or simply:

After modifying the response, you will be granted with access to iCloud data on the web as follows:

Mail
Photos
Drive
Notes
Reminders
Numbers
Keynote
Apps that had access control implemented and were not accessible:
Calendar
Contacts

Having such access allowed me to view and download files from Mail, Photos, Drive, Notes, Reminders, Numbers, and Keynote meaning that it’s not just front-end bypass.

Press enter or click to view image in full size
Press enter or click to view image in full size
Impact

If an attacker gets access to victim credentials, he can access iCloud data via www.icloud.com despite web access being restricted via “Manage Web Access To Your Icloud Data” on the device.

Interestingly, by changing a value in the response, access is granted to all of the mentioned apps.

In many cases, even if you steal Icloud credentials, you might need 2FA and because of this Apple lowered the severity.

Timeline:

· Reported on: 10/12/23

· Additional information requested by Apple: 10/13/23

· Additional information provided: 10/13/23

· I’ve noticed issue was fixed on: 12/11/23

· Final decision: 12/21/23

Press enter or click to view image in full size

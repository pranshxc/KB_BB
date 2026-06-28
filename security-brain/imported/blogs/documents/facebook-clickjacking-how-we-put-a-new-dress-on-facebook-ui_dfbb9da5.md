---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-04-22_facebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui.md
original_filename: 2016-04-22_facebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui.md
title: Facebook ClickJacking – How we put a new dress on Facebook UI
category: documents
detected_topics:
- clickjacking
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- clickjacking
- command-injection
- mfa
- api-security
language: en
raw_sha256: dfbb9da58232eb413772a1af1aaddb1dd3dad2119992c5c2b3cf0a33d5db3d12
text_sha256: 7a8a7c6f5ee19dce274a7eb53f842145c0ff6c3da1f0d453fb7ef6598be1a32a
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook ClickJacking – How we put a new dress on Facebook UI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-04-22_facebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui.md
- Source Type: markdown
- Detected Topics: clickjacking, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `dfbb9da58232eb413772a1af1aaddb1dd3dad2119992c5c2b3cf0a33d5db3d12`
- Text SHA256: `7a8a7c6f5ee19dce274a7eb53f842145c0ff6c3da1f0d453fb7ef6598be1a32a`


## Content

---
title: "Facebook ClickJacking – How we put a new dress on Facebook UI"
page_title: "Facebook ClickJacking – How we put a new dress on Facebook UI – Seekurity"
url: "https://www.seekurity.com/blog/write-ups/facebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui/"
final_url: "https://seekurity.com/blog/2016/04/22/admin/poc-gallery/facebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui"
authors: ["Mohamed A. Baset"]
programs: ["Meta / Facebook"]
bugs: ["Clickjacking"]
publication_date: "2016-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6303
---

Hi Bug Hunters,

Today we will explain how we redressed facebook ui and made it so easy to fool a victim to for example, Add the attacker as a member in one of his own secret groups on facebook.

Here’s some details about the issue:

**  
Vulnerability Type:**  
[ClickJacking](https://www.owasp.org/index.php/Clickjacking)

**The vulnerable url:**  
[https://www.facebook.com/ajax/home/generic.php?dpr=1&sidecol=true&path=/groups/](https://www.facebook.com/ajax/home/generic.php?dpr=1&sidecol=true&path=%2Fgroups%2F)559357440894888/&endpoint=/ajax/home/generic.php&__user=

100000152886101&__a=1&__dyn=&__req=jsonp_8&__be=0&__pc=EXP1:DEFAULT&__rev=2286573&__cid=

**Where:**  
1\. 559357440894888 is the targeted resource (group)  
2\. 100000152886101 is the targeted user who owns the resource, (Just a parameter value sent along with the first GET request to be included in the form action to successfully complete the request)

**The problem:**  
When this endpoint (/ajax/home/generic.php) calling an client side facebook path (path=) related to a facebook resource (pages, groups, etc..) this resource lacks the “X-Frame-Options” and became iframable. The fact is that all the actions inside the iframable response are depending on another resource that has not been loaded to complete the AJAXed requests to be made but LUCKILY we found that the iframable resource contains some “Forms” that are able to be submitted by the victim.

**The PoC Impact:**  
Fooling a victim to add a specific user to a targeted secret group or even any other resource!!

**PoC Code (In case you need it):  
**<div style=”overflow: hidden; width: 145px; height: 28px; position: relative;” >  
<iframe src=”URL” style=”border: 0pt none ; left: -7px; top: -807px; position: absolute; width: 1406px; height: 1321px;” scrolling=”no”></iframe></div></br>

**PoC Video:**

**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F04%2F22%2Fadmin%2Fpoc-gallery%2Ffacebook-clickjacking-how-we-put-a-new-dress-on-facebook-ui&linkname=Facebook%20ClickJacking%20%E2%80%93%20How%20we%20put%20a%20new%20dress%20on%20Facebook%20UI "Gmail")[](https://www.addtoany.com/share)

Bug  ClickJacking  Facebook  Security  UI  UI Redressing

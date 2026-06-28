---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-02_iphone-camera-hack.md
original_filename: 2020-04-02_iphone-camera-hack.md
title: iPhone Camera Hack
category: documents
detected_topics:
- command-injection
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- cloud-security
- mobile-security
language: en
raw_sha256: 9ebb8efb72995bd7cffb93ddbb4122c8b9787ca63dfaeafe84b48a4c46cf3c17
text_sha256: 71c03f457cd7b3188a3a9fd69d65c495cefe30951efa3f369d7eff8b4b83a686
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# iPhone Camera Hack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-02_iphone-camera-hack.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `9ebb8efb72995bd7cffb93ddbb4122c8b9787ca63dfaeafe84b48a4c46cf3c17`
- Text SHA256: `71c03f457cd7b3188a3a9fd69d65c495cefe30951efa3f369d7eff8b4b83a686`


## Content

---
title: "iPhone Camera Hack"
page_title: "Webcam Hacking | Ryan Pickren"
url: "https://www.ryanpickren.com/webcam-hacking-overview"
final_url: "https://www.ryanpickren.com/webcam-hacking-overview"
authors: ["Ryan Pickren"]
programs: ["Apple"]
bugs: ["Zero-Click Unauthorized Access to Sensitive Data"]
bounty: "75,000"
publication_date: "2020-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4670
---

# iPhone Camera Hack

![camera-hack-final.png](https://static.wixstatic.com/media/149864_084ea01f60bc4dbcb785a02a14d70ff7~mv2.png/v1/crop/x_0,y_7,w_3156,h_2025/fill/w_900,h_577,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/camera-hack-final.png)

## I discovered a vulnerability in Safari that allowed unauthorized 

## websites to access your camera on iOS and macOS 

Imagine you are on a popular website when all of a sudden an ad banner hijacks your camera and microphone to spy on you. That is exactly what this vulnerability would have allowed.

​

This vulnerability allowed malicious websites to masquerade as trusted websites when viewed on Desktop Safari (like on Mac computers) or Mobile Safari (like on iPhones or iPads).

​

Hackers could then use their fraudulent identity to invade users' privacy. This worked because Apple lets users permanently save their security settings on a [per-website basis](https://support.apple.com/guide/safari/customize-settings-per-website-ibrw7f78f7fe/mac).

​

If the malicious website wanted camera access, all it had to do was masquerade as a trusted video-conferencing website such as Skype or Zoom.

![badads.png](https://static.wixstatic.com/media/149864_f3f2f367ac724735ac4281012f1d44ea~mv2.png/v1/fill/w_519,h_292,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/badads.png)

Is an ad banner watching you?

I posted the technical details of how I found this bug in a lengthy walkthrough [here](https://www.ryanpickren.com/webcam-hacking).

​

My research uncovered seven zero-day vulnerabilities in Safari (CVE-2020-3852, CVE-2020-3864, CVE-2020-3865, CVE-2020-3885, CVE-2020-3887, CVE-2020-9784, & CVE-2020-9787), three of which were used in the kill chain to access the camera.

​

Put simply - the bug tricked Apple into thinking a malicious website was actually a trusted one. It did this by exploiting a series of flaws in how Safari was parsing [URIs](https://developer.mozilla.org/en-US/docs/Glossary/URI), managing web [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin), and initializing [secure contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts).

​

If a malicious website strung these issues together, it could use JavaScript to directly access the victim's webcam without asking for permission. Any JavaScript code with the ability to create a popup (such as a standalone website, embedded ad banner, or browser extension) could launch this attack.

I reported this bug to Apple in accordance with the [Security Bounty Program rules](https://developer.apple.com/security-bounty/) and used [BugPoC](http://bugpoc.com) to give them a live demo. Apple considered this exploit to fall into the "[Network Attack without User Interaction: Zero-Click Unauthorized Access to Sensitive Data](https://developer.apple.com/security-bounty/payouts/)" category and awarded me $75,000.

​

The below screen recording shows what this attack would look like if clicked from Twitter.

![macos-poc.gif](https://static.wixstatic.com/media/149864_b6a9268cffe34047a4797c88068e7669~mv2_d_1736_1380_s_2.gif)

![ios-poc.gif](https://static.wixstatic.com/media/149864_f088f74e64334c199a9dd4738555ffbc~mv2.gif)

* victim in screen recording has previously trusted skype.com

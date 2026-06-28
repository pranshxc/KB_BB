---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-14_third-party-android-app-storing-facebook-data-insecurely-facebook-data-abuse-pro.md
original_filename: 2019-02-14_third-party-android-app-storing-facebook-data-insecurely-facebook-data-abuse-pro.md
title: Third Party Android App Storing Facebook Data Insecurely (Facebook Data Abuse
  Program)
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- mobile-security
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- mobile-security
- supply-chain
language: en
raw_sha256: 7e57be58efbb192e75ba3e581737d824392d4adad77ee39ad5531e4f02a9d968
text_sha256: ff78c26a3ea6135688acfd7a329a56167ce9bd3b892169496ae5a4297c9963d9
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Third Party Android App Storing Facebook Data Insecurely (Facebook Data Abuse Program)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-14_third-party-android-app-storing-facebook-data-insecurely-facebook-data-abuse-pro.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7e57be58efbb192e75ba3e581737d824392d4adad77ee39ad5531e4f02a9d968`
- Text SHA256: `ff78c26a3ea6135688acfd7a329a56167ce9bd3b892169496ae5a4297c9963d9`


## Content

---
title: "Third Party Android App Storing Facebook Data Insecurely (Facebook Data Abuse Program)"
page_title: "Third Party Android App Storing Facebook Data Insecurely (Facebook Data Abuse Program) | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2019/02/14/third-party-android-app-storing-facebook-data-insecurely/"
final_url: "https://wwws.nightwatchcybersecurity.com/2019/02/14/third-party-android-app-storing-facebook-data-insecurely/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Missing authentication"]
publication_date: "2019-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5415
---

# Third Party Android App Storing Facebook Data Insecurely (Facebook Data Abuse Program)

[February 14, 2019February 15, 2019](https://wwws.nightwatchcybersecurity.com/2019/02/14/third-party-android-app-storing-facebook-data-insecurely/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Research](https://wwws.nightwatchcybersecurity.com/category/research/)[Android](https://wwws.nightwatchcybersecurity.com/tag/android/), [facebook](https://wwws.nightwatchcybersecurity.com/tag/facebook/)

## Summary

A third-party Android application with Facebook API access was found to be copying user data into storage outside of Facebook, and storing it insecurely in two separate locations. This issue was reported to Facebook via their Data Abuse Bounty program and the insecure storage locations have been secured on November 12th, 2018. The Facebook app associated with this application has been removed from the Facebook platform but the Android application remains available in Google’s Play Store. The number of affected users is unknown. **[ADDED: 02/15/2019 – Google has been notified].**

## Background

In April 2018, FaceBook announced [a new Data Abuse Bounty program](https://newsroom.fb.com/news/2018/04/data-abuse-bounty/) that rewards “ _people with first-hand knowledge and proof of cases where a Facebook platform app collects and transfers people’s data to another party to be sold, stolen or used for scams or political influence_ “.

In September 2018, we found an Android application in the Google Play store that purports to provide additional functionality to Facebook users that is not available through the platform. At the time of writing, the application had more than 1,000,000 downloads. After downloading the application, and examining it using [JADX](https://github.com/skylot/jadx), we found that the application was using Facebook APIs to access data for the logged in user and copying to several storage locations outside of Facebook. Upon further examination, it was clear that at least two of such locations (a Firebase database and an API server) were making this data available without any authentication and without HTTPS. This would allow an attacker to mass download the user data accumulated by the application from its users.

We do not know for sure how many users have been impacted or exposed, but one of the databases accessed contained over 1,000,000 records. **[ADDED: 02/15/2019 – The application purported to provide additional statistical information about the logged-in user’s Facebook account. There is a privacy policy within the application but it is ambiguous about the transfer of data].**

### Issue #1 – Storing user data in an public Firebase database

During our examination of the application, we located a Firebase database that the application was communicating with. The database was configured in test mode, which allowed anonymous public access by visiting the URL of “**<https://DATABASE.firebaseio.com/.json>** “. As seen in the attached screenshot, the database contained data obtained from Facebook. Aside from confirming the initial permission issue, we did not access or explore this database any further.

Screenshot:

![likulator1](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2019/02/likulator1-1.png?w=700)

### Issue #2 – Storing user data in a non-SSL server without authentication

During our examination of application, it become clear that the server that the application was communicating with, did not use SSL and was being accessed without authentication. As seen below, this would allow an attacker to download the data collected by the application from Facebook via a regular browser as well as spy on any connections between the application and the server. Aside from confirming the initial permission issue, we did not access or explore this database any further.

![likulator2](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2019/02/likulator2.png?w=700)

![likulator3](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2019/02/likulator3.png?w=700)

## Vendor Response and Mitigation

We contacted the Facebook Data Abuse Bounty program but did not contact the vendor directly. After Facebook completed its review, the two insecure locations have been secured on November 12th, 2018. The Facebook app associated with this application has been removed from the Facebook platform but the Android application remains available in Google’s Play Store. **[ADDED: 02/15/2019 – Google has been notified]**.

This discovery qualified under the terms of the Facebook Data Abuse Bounty Program and a bounty payment has been received.

## References

Facebook report # 10101718616795015  
Google reference # 8-7487000025062

## Credits

This advisory was written by Yakov Shafranovich.

## Timeline

2018-09-17: Initial report submitted to Facebook, initial response received  
2018-11-12: Issued fixed  
2018-11-27: Bounty decision received; sent disclosure request  
2018-11-30: Facebook asked for additional time before disclosure  
2019-01-15: Investigation has been finalized, FaceBook asked for a copy of the disclosure  
2019-02-03: Draft disclosure shared for review  
2019-02-14: Public Disclosure  
2019-02-15: Minor updates; notification sent to Google

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2019/02/14/third-party-android-app-storing-facebook-data-insecurely/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2019/02/14/third-party-android-app-storing-facebook-data-insecurely/?share=facebook)
  * 

Like Loading...

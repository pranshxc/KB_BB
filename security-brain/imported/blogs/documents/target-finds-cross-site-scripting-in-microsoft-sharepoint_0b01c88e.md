---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-15_target-finds-cross-site-scripting-in-microsoft-sharepoint.md
original_filename: 2019-03-15_target-finds-cross-site-scripting-in-microsoft-sharepoint.md
title: Target Finds Cross-Site Scripting in Microsoft SharePoint
category: documents
detected_topics:
- xss
- sso
- command-injection
tags:
- imported
- documents
- xss
- sso
- command-injection
language: en
raw_sha256: 0b01c88efe86bb477aebb5300bfd4cd2c60027b20ee73a4552e4b57737befb4e
text_sha256: 15705a037b254898f7d3596f7b2ab59363dae6f1c51e66e96c3db945a2a56141
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Target Finds Cross-Site Scripting in Microsoft SharePoint

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-15_target-finds-cross-site-scripting-in-microsoft-sharepoint.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0b01c88efe86bb477aebb5300bfd4cd2c60027b20ee73a4552e4b57737befb4e`
- Text SHA256: `15705a037b254898f7d3596f7b2ab59363dae6f1c51e66e96c3db945a2a56141`


## Content

---
title: "Target Finds Cross-Site Scripting in Microsoft SharePoint"
url: "https://tech.target.com/2019/03/15/SharePoint-Cross-Site-Scripting.html"
final_url: "https://tech.target.com/blog/target-finds-cross-site-scripting-in-microsoft-sharepoint"
authors: ["Target"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2019-03-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5356
---

Cross-site scripting has been an OWASP Top 10 classic for more than a decade, but it still comes as a surprise to find it out in the wild, especially in a well-known product. During a recent penetration test, Target's Security Testing Services team found that Microsoft's SharePoint was vulnerable to a unique attack that, unlike typical cross-site scripting, could be exploited without any interaction from the victim user.

Some quick background: SharePoint is part of the Microsoft Office 365 product line, providing an online web interface for Outlook, Excel, Word and other Microsoft resources. This portal notifies users within their browsers about new emails, Lync/Skype messages and upcoming meetings. It was this notification system that enabled attackers to inject code into a victim's browsers by simply sending the victim an email.

Detection

This vulnerability was discovered by accident during a pentest of an unrelated application. At one point during the assessment, we performed an action that made the application send a notification email to the assessor containing a basic cross-site scripting payload. Soon after, the assessor’s SharePoint session was interrupted by the iconic alert(1) box:

![screenshot from a SharePoint OneDrive window showing an alert message with just a "1" in the alert area](https://target.scene7.com/is/image/Target/alert1image_upload-210907_1631043373258?scl=1&qlt=80&fmt=png)

After some digging, we found that around once a minute, the browser sends a GET request for the following URL:
  
  
  https://outlook.office365.com/owa/ev.owa2?ns=PendingRequest&ev=PendingNotificationRequest&UA=0&cid=[cid]&X-SuiteServiceProxyOrigin=https://[company].sharepoint.com

The SharePoint server responds with information about any new emails in some JSON data, which will be dynamically incorporated into the user’s open SharePoint page:
  
  
  HTTP/1.1 200 OK
  
  [TRUNCATED]
  
  
  
  <script>[{"__type":"NewMailNotificationPayload:#Exchange","id":"NewMailNotification","Sender":"SenderInformation","Subject":"Email Subject","PreviewText":"Preview Text","ItemId":"[itemID]","ConversationId":"[conversationID]","IsClutter":false,"SenderSmtpEmailAddress":"johndoe@example.com","InferenceClassification":"Focused","EventType":"0"}]</script>

The PreviewText parameter contains the contents of the email but fails to sanitize potentially troublesome characters like < > /. SharePoint does properly escape the apostrophe ’ and doublequote ” characters, though backticks made it through unescaped. Given this, an email containing the payload </script><script>alert('hello')</script> generates the following notification:
  
  
  <script>[{"__type":"NewMailNotificationPayload:#Exchange","id":"NewMailNotification","Sender":"SenderInformation","Subject":"Email Subject","PreviewText":"</script><script>alert('hello')</script>","ItemId":"[itemID]","ConversationId":"[conversationID]","IsClutter":false,"SenderSmtpEmailAddress":"johndoe@example.com","InferenceClassification":"Focused","EventType":"0"}]</script>

Note that the payload closes the existing open script tag, allowing our injected script to function properly:

![screenshot of OneDrive instance with an alert message that reads "hello"](https://target.scene7.com/is/image/Target/helloAlertimage_upload-210907_1631043913444?scl=1&qlt=80&fmt=png)

Exploitation

This flaw could be exploited in any number of ways. We created this basic proof-of-concept attack when disclosing this vulnerability to Microsoft:

An attacker crafts an innocent-looking email by shrinking and recoloring the malicious code to look invisible to the reader:

![zoomed-in screenshot of an Outlook email message with the salutation "Hello" highlighted to show malicious code embedded](https://target.scene7.com/is/image/Target/maliciousEmailimage_upload-210907_1631044137348?scl=1&qlt=80&fmt=png)

If the victim is signed into SharePoint when they receive the email, the payload will open an alert box in the victim’s browser stating that their session has expired and they need to reauthenticate:

![screenshot from OneDrive with error message prompting "Session expired. Please log in again."](https://target.scene7.com/is/image/Target/alertimage_upload-210907_1631044211082?scl=1&qlt=80&fmt=png)

The payload will then redirect them to the attacker’s webpage, set up as a fake Microsoft login page:

![screenshot of malicious URL spoofing a normal Microsoft sign-in page](https://target.scene7.com/is/image/Target/attackerSiteimage_upload-210907_1631044280130?scl=1&qlt=80&fmt=png)

To be successful, an attacker only needs a single employee who is signed into Sharepoint to receive the malicious email. Note that the victim user doesn't need to actually open the email for the attack to work - the notification alone triggers the exploit.

Conclusion

Target's Security Testing Services team responsibly disclosed the vulnerability to Microsoft. After completing our working proof of concept, we documented detailed steps and the exploit's requirements and sent them to Microsoft, following Microsoft's [security vulnerability disclosure process](https://www.microsoft.com/en-us/msrc/faqs-report-an-issue?rtc=1).

Email confirmation was given from Microsofot Security Response Center reporting the issue has been resolved. To fix the issue, a serializer was modified to properly encode script tags to prevent cross-site scripting payloads from executing from within the notifications in the SharePoint application.

By identifying this vulnerability and working with the Microsoft team to properly get the issue resolved, Target's Security Testing Services team was able to identify and eliminate Target's risk to the cross-site scripting attack vector within the Sharepoint application.

## PUBLISHED BY

Steven Kaun

Engineer, Security Testing Services

Jamie Feist

Lead Engineer, Cyber Solutions

![Sydney Delp's profile photo](https://target.scene7.com/is/image/Target/sydney-delpimage_upload-210930_1633017905540)

Sydney Delp

Director, Cybersecurity

## CATEGORIES

Cybersecurity

## SHARE

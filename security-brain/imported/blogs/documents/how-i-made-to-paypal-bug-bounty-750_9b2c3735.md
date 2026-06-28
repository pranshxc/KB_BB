---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-28_how-i-made-to-paypal-bug-bounty-750.md
original_filename: 2021-03-28_how-i-made-to-paypal-bug-bounty-750.md
title: How I made to Paypal Bug Bounty $750
category: documents
detected_topics:
- xss
- command-injection
- otp
tags:
- imported
- documents
- xss
- command-injection
- otp
language: en
raw_sha256: 9b2c3735688adff4815db57a58b1bbe4c51c7bc811701b897d97d02a593a44d9
text_sha256: 6a0d67ccf6ba68de18ee3165408d117d4d110a2ac11fc12f2b339ed02e6f8e49
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I made to Paypal Bug Bounty $750

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-28_how-i-made-to-paypal-bug-bounty-750.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9b2c3735688adff4815db57a58b1bbe4c51c7bc811701b897d97d02a593a44d9`
- Text SHA256: `6a0d67ccf6ba68de18ee3165408d117d4d110a2ac11fc12f2b339ed02e6f8e49`


## Content

---
title: "How I made to Paypal Bug Bounty $750"
page_title: "How I made to Paypal Bug Bounty $750 - Pethuraj's Blog"
url: "https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/"
final_url: "https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/"
authors: ["Pethuraj (@Pethuraj)"]
programs: ["Paypal"]
bugs: ["Open redirect"]
bounty: "750"
publication_date: "2021-03-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3785
---

![Paypal Bug Bounty writeup](https://www.pethuraj.com/blog/wp-content/uploads/2021/03/Paypal-BugBounty.png)

[Uncategorized](https://www.pethuraj.com/blog/category/uncategorized/)

# How I made to Paypal Bug Bounty $750

[28/03/202125/05/2021](https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/) by [admin](https://www.pethuraj.com/blog/author/admin/)

Hey Guys,

This blog is all about how I made to PayPal Bounty $750 with simple bug as **Open Redirect Vulnerability**. After deciding my target as PayPal, I read their responsibility disclosure program carefully and went through its scope.

Xoom was acquired by the PayPal and was in scope so I thought to make my hands dirty with Xoom domains.

The very first and obvious step I did was recon. I gathered all the valuable information and subdomains of the target Xoom. This vulnerability was found on Xoom Dashboard. Before proceeding to POC lets just understand about Open Redirect vulnerability.

**_**Open Redirect Vulnerability**_**

Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behaviour can be leveraged to facilitate phishing attacks against users of the application, perform XSS attacks and also stealing tokens.

**Vulnerable URL:**[_https://refer.xoom.com_](https://refer.xoom.com)

**Vulnerable Parameter** : redirect

> The most strange part of this vulnerability is wherever I use **redirect=** parameter in the target domain, the website redirects. 

Steps to Reproduce the vulnerability

  1. I opened up refer.xoom.com and navigated to pages which contains sensitive details in parameters as I can be able to perform open redirect and as well as token stealing.
  2. I randomly appended the URL with ‘**& redirect=https://www.pethuraj.in**’ which leads to redirection to the target domain. And I tried this in all the pages of Xoom dashboard and it worked.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/03/paypal-open-redirect.gif)

> In simpler words, wherever the application is having redirect= parameter in the GET method – the redirect occurs.

Apart from Open Redirect, I was able to steal the tokens (campaign id) of the target website.

And regarding the token stealing, I set up a php code on my website which automatically logs all the incoming requests and then filter the campaign id separately.

I had reported the bug to Paypal immediately. Thanks to the Paypal team that they acknowledged the bug and rewarded me with bounty and acknowledgement on their Wall of Fame page.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/03/Paypal-Bug-Bounty-1.png)

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/03/PayPal-Acknowledgements-1024x662.jpeg)Note: This writeup is from 2017 and hence the Honorable Mention page is broken currently.

I hope aforementioned blog about open redirect vulnerability is easier to understand and hope there would be more blog coming on the way. Hope you like it.

**Get in touch with me –**

<https://twitter.com/Pethuraj>  
<https://www.linkedin.com/in/pethu/>

## You may like!

[![](https://www.pethuraj.com/blog/wp-content/uploads/2025/01/Use-Burp-Suite-like-a-PRO-Part-2-300x150.png)](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

#### [How to use Burp Suite Like a PRO? PART – 2](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

Ready to level up your Burp Suite skills? In part 2, I've compiled some awesome tips and tricks to help ...  

[Read More](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

[![burp suite advanced tutorials](https://www.pethuraj.com/blog/wp-content/uploads/2022/07/Mastering-Burp-suite-300x150.png)](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

#### [How to use Burp Suite Like a PRO? PART – 1](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

This blog series is an advanced tutorial of the popular web application security and penetration testing tool Burp Suite, to help ...  

[Read More](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

Share on Social Media

[x](https://x.com/share?url=https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/&text=How+I+made+to+Paypal+Bug+Bounty+%24750)[facebook](https://www.facebook.com/sharer.php?u=https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/)[linkedin](https://www.linkedin.com/shareArticle?url=https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/&title=How+I+made+to+Paypal+Bug+Bounty+%24750)[email](mailto:?subject=How+I+made+to+Paypal+Bug+Bounty+%24750&body=https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/)[whatsapp](https://api.whatsapp.com/send?text=How+I+made+to+Paypal+Bug+Bounty+%24750%20https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/)

## Post navigation

[BMW Bug Bounty – Account Verification Bypass writeup](https://www.pethuraj.com/blog/bmw-bugbounty-writeup/)

[Edmodo Bug Bounty Writeup](https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/)

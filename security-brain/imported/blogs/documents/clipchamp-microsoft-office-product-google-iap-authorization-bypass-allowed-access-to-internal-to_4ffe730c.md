---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_clipchamp-microsoft-office-product-google-iap-authorization-bypass-allowed-acces.md
original_filename: 2023-03-10_clipchamp-microsoft-office-product-google-iap-authorization-bypass-allowed-acces.md
title: Clipchamp ( Microsoft Office Product) - Google IAP Authorization bypass allowed
  access to Internal Environment Leading to Zero Interaction Account takeover
category: documents
detected_topics:
- jwt
- access-control
- ssrf
- command-injection
- mfa
- otp
tags:
- imported
- documents
- jwt
- access-control
- ssrf
- command-injection
- mfa
- otp
language: en
raw_sha256: 4ffe730ce410240c0f9c0d56327df90959a7b5192ebec8db9bafaa3608474173
text_sha256: 9972a990c1d567963b7e8a7b4589151090c7362e341b7248c6623004cacdd0b7
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Clipchamp ( Microsoft Office Product) - Google IAP Authorization bypass allowed access to Internal Environment Leading to Zero Interaction Account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_clipchamp-microsoft-office-product-google-iap-authorization-bypass-allowed-acces.md
- Source Type: markdown
- Detected Topics: jwt, access-control, ssrf, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `4ffe730ce410240c0f9c0d56327df90959a7b5192ebec8db9bafaa3608474173`
- Text SHA256: `9972a990c1d567963b7e8a7b4589151090c7362e341b7248c6623004cacdd0b7`


## Content

---
title: "Clipchamp ( Microsoft Office Product) - Google IAP Authorization bypass allowed access to Internal Environment Leading to Zero Interaction Account takeover"
page_title: "Clipchamp ( Microsoft Office Product) - Google IAP Authorization bypass allowed access to Internal Environment Leading to Zero Interaction Account takeover | Agilehunt's Blog - Guarding your innovation"
url: "https://blog.agilehunt.com/blogs/security/msrc-critical-google-iap-authorization-bypass-allows-access-to-internal-envirnment-leading-to-zero-interaction-account-takeover"
final_url: "https://blog.agilehunt.com/blogs/security/msrc-critical-google-iap-authorization-bypass-allows-access-to-internal-envirnment-leading-to-zero-interaction-account-takeover"
authors: ["Vikas Anil Sharma (@vikzsharma)"]
programs: ["Microsoft (ClipChamp)"]
bugs: ["Authorization bypass", "JWT", "Account takeover"]
publication_date: "2023-03-10"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1399
---

Published on
  Friday, March 10, 2023

# Clipchamp ( Microsoft Office Product) - Google IAP Authorization bypass allowed access to Internal Environment Leading to Zero Interaction Account takeover

Authors
  

  * ![avatar](/_next/image?url=%2Fstatic%2Fimages%2Favatar.png&w=96&q=75)

Name
  Vikas Anil Sharma
Twitter
  [@vikzsharma](https://twitter.com/vikzsharma)

![tailwind-nextjs-banner](/_next/image?url=%2Fstatic%2Fimages%2Fclipchamp.png&w=750&q=75)

IMPORTANT

**Your Business is Only as Secure as its Weakest Point.**  
Don’t risk exposing your data to attackers—**Contact Us Now** for a free consultation and find out how Agilehunt can protect your digital assets.

## Vulnerability Description

During an in-depth security analysis of **Clipchamp** , Agilehunt identified a critical flaw that allowed attackers to bypass Google IAP authorization, granting unauthorized access to Clipchamp’s **internal/test/smoke/beta** environments.

Despite being protected by Google IAP (ensuring only Clipchamp or Microsoft employees could access these environments), we discovered that the **API endpoints** lacked sufficient back-end authorization checks. This opened a door for attackers to steal JWT tokens and execute **Zero Interaction Account Takeover** for any user in the Smoke environment.

**This means attackers could access internal Clipchamp accounts, exploit sensitive data, and cause significant reputational and financial damage.**

* * *

## Risk Breakdown

  * **Risk:** **Critical**
  * **Difficulty to Exploit:** **Easy**

* * *

## Affected URLs

  * `app.smoke.clipchamp.com`
  * `app.beta.clipchamp.com`
  * `app.test.clipchamp.com`
  * `app.demo.clipchamp.com`

* * *

## Steps to Reproduce

**Step 1:** Navigate to any of the Affected URLs above e.g <https://app.smoke.clipchamp.com/> and observe user is redirected to Google IAP Login , using any random credentials gives the screen below "**Access blocked: Clipchamp Smoke can only be used within its organisation** ".

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/Step-1_1024x1024.png?v=1678187414)

**Step 2:** Send the POST request below with the desired victim user email you want access to on the ClipChamp platform e.g (_[vikz.sharma1996@gmail.com](mailto:vikz.sharma1996@gmail.com)_).

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/step-2.png?v=1678187566)

Observe the response has the JWT Token in the response (  _Meaning we have bypassed the Google IAP Authroization_ ) allowing us access to internal envirnoment which leaks the JWT Token for any user in the response itself.

**Step 3:** Pass the JWT Token received above to the "code" parameter in the request below and send it :

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/step-3.png?v=1678187629)

Observe the response for request from ( ** _Step 3_** ) has the master Authroization JWT Token for the victim account (  _[vikz.sharma1996@gmail.com](mailto:vikz.sharma1996@gmail.com)_) which can be utilized on platform wide - > Access all API endpoints of Clipchamp like /v2/user/ , /v2/user/workspaces , Projects , PII data.

**Step 4:** For verifying the obtained JWT Token for requested user is valid , send the request below :

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/step-4.png?v=1678187724)

**RESPONSE** \- reveals all the details about the victim user :

**Step 5:** In order to verify the impact of this critical vulnerability, I had to proof if an attacker can read / edit / add existing user information on the internal server , Clicking the Contact the Developer button on the Google IAP block page gives us email address of the potential employee of ClipChamp / Microsoft which was "[Redacted@clipchamp.com](mailto:Redacted@clipchamp.com)" who is an employee of Microsoft .

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/2023-03-07_15-17.png?v=1678187914)

**Step 6:** Repeat the **Step 2** but with the email of an internal employee which is [Redacted@clipchamp.com](mailto:Redacted@clipchamp.com) as email parameter value like below :

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/2023-03-07_15-17_0d3328d3-8564-4297-a03b-a4e66c67b1cf.png?v=1678188122)

Observe the response has the MAGIC Login LINK - JWT Token for an potential employee of Microsoft.

**Step 7:** Repeat **Step 3** with the JWT Token from **Step 6** (  _Which is JWT Token of Internal an Employee of Microsoft_ ) to the "_code_ " parameter and send the request like below :

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/2023-03-07_15-17_d7bfdb83-499c-496d-b8ea-aa24addd5f06.png?v=1678188239)

Observe the response for request above has the master Authroization JWT Token for the **victim account a Microsoft Employee in this case** **(_[redacted@clipchamp.com](mailto:redacted@clipchamp.com)_)** which can be utilized platform wide - > all accessible endpoints like /v2/user/ , /v2/user/workspaces , projects , pii data , add email , change email ,all other actions etc.

**Step 8:** To validate the exploit - Send the request below with the Authorization Bearer JWT Token received above like below :

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/2023-03-07_15-17_ab2366ff-8c7c-4ef4-99c0-10458e43d4cf.png?v=1678192027)  
Observe we are now able to access information of an existing internal user who is an potential employee of Microsoft using the internal platform :

The employee user accout was created_at": "2021-09-17T02:28:25.359582+00:00" which means this was an existing account.

## Impact

  1. Unauthorized actions or access to sensitive data within the vulnerable application or other connected systems.
  2. An attacker could access internal user data, including confidential information, leading to **financial and reputational damage**.
  3. Potential to further abuse the system to access accounts with **premium features** , causing significant financial loss.

## Recommendation

  * Implement strict authorization checks to avoid external access to internal networks / platforms completely.

## References

For more information check out reference [[1]]

  * [1] [WSTG - v4.2 | OWASP Foundation](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema "Testing for Bypassing Authorization Schema")

## TIMELINES

  * **Jan 9, 2023** \- Case Opened
  * **Jan 9, 2023** \- Moved to Develop ( Fixing )
  * **Jan 20, 2023** \- Out of Scope Email
  * **March 7, 2023** \- Issue Fixed / Listed on acknowledgement page.

[Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fblog.agilehunt.com%2Fblogs%2Fsecurity%2Fmsrc-critical-google-iap-authorization-bypass-allows-access-to-internal-envirnment-leading-to-zero-interaction-account-takeover)

## Tags

[bug-bounty](/tags/bug-bounty)[security](/tags/security)[Microsoft](/tags/microsoft)[cybersecurity](/tags/cybersecurity)

## Previous Article

[Race Condition vulnerability in Azure Video Indexer allowed trial account users use Advance / Premium feature](/blogs/security/race-condition-vulnerability-in-azure-video-indexer-allowed-trial-account-users-use-advance-premium-feature)

## Next Article

[CVE-2023-1906 - Heap-based Buffer Overflow in ImageMagick](/blogs/security/cve-2023-1906-heap-based-buffer-overflow-in-imagemagick)

[← Back to the blog](/blogs)

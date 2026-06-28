---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_parameter-pollution-issue-in-api-resulting-xxx.md
original_filename: 2019-06-17_parameter-pollution-issue-in-api-resulting-xxx.md
title: Parameter Pollution issue in API resulting $XXX
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
language: en
raw_sha256: 4a690ef0d101b4ee51696f09603e30bc096fa7e51e19a2ae6cd254dd3e4e0455
text_sha256: 75e987a065702f5dd9982e376c1ee7dae7e8c9bd3140162ae6af2927dc786511
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Parameter Pollution issue in API resulting $XXX

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_parameter-pollution-issue-in-api-resulting-xxx.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `4a690ef0d101b4ee51696f09603e30bc096fa7e51e19a2ae6cd254dd3e4e0455`
- Text SHA256: `75e987a065702f5dd9982e376c1ee7dae7e8c9bd3140162ae6af2927dc786511`


## Content

---
title: "Parameter Pollution issue in API resulting $XXX"
page_title: "Parameter Pollution issue in API resulting $XXX – Smaran Chand"
url: "https://smaranchand.com.np/2019/06/parameter-pollution-issue-in-api-resulting-xxx/"
final_url: "https://smaranchand.com.np/2019/06/parameter-pollution-issue-in-api-resulting-xxx/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["HTTP parameter pollution"]
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5205
---

[June 17, 2019](https://smaranchand.com.np/2019/06/parameter-pollution-issue-in-api-resulting-xxx/)

# Parameter Pollution issue in API resulting $XXX

When it comes regarding API pentesting, I am always eager to test it even though I don’t succeed to find critical issues.

It was one of the private programs from bugcrowd. It’s the same program where my P1 bug got duplicate. 🙁 And I decided to give it a final try.

Without wasting time I checked the scope and discovered that Android, IOS app and serving API were in the scope.

Once again I fired up my best SSL unpinning tool Frida 😀 and started intercepting the network traffic of Android app. Although I wasn’t able to test the scope fully because of some regional issues and resources required.

While making changes to the account information I found that API was using PUT method to update profile details.

Below is the API request for updating Name
  
  
  PUT /api/v2/user/xxxxxxxxxxxxxxxxxx/profile HTTP/1.1
  Accept: application/vnd.api+json
  Authorization: Bearer ***REDACTED***
  api-key=***REDACTED***
  Content-Type: application/json; charset=UTF-8
  Content-Length: 244
  Host: api.redacted.com
  Connection: close
  Accept-Encoding: gzip, deflate
  User-Agent: okhttp/3.10.0
  
  {"EmailAddress":"[[email protected]](/cdn-cgi/l/email-protection)","FirstName":"Smaran","Parameter1":"12345","MobileVerified":true,"Mobile":"1234567890","Parameter2":"67890","Surname":"SO","UserId":"xxxxxxx"}

The response part disclosed a new parameter “XPoint”:”” without any value.

![](https://smaranchand.com.np/wp-content/uploads/2019/06/Reflected.png)Image: API Request reflecting a new parameter with null value in response covered in blue.
  
  
  {"EmailAddress":"[[email protected]](/cdn-cgi/l/email-protection)","FirstName":"Smaran","Parameter1":"12345","MobileVerified":true,"Mobile":"1234567890","XPoint":"","Parameter2":"67890","Surname":"SO","UserId":"xxxxxxx"}
  

As it is clearly seen that a new parameter Xpoint was reflected in the response.

In order to check for parameter pollution issue, I added Xpoint parameter and sent the API request with value 1500 and it reflected “XPoint”:”1500″ in the response 😀

In order to verify the issue, I logged out of the mobile app and logged in again. I found that the Xpoints were still reflecting in my account.

Note: XPoints are the loyalty points collected. So in that scenario i was able to generate any amount of Loyalty points in my account.

![](https://smaranchand.com.np/wp-content/uploads/2019/06/replyfrom.png)Image: Reply from Programs developer

This issue might seem easy to find and exploit but you will never know until you don’t do it yourself.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)

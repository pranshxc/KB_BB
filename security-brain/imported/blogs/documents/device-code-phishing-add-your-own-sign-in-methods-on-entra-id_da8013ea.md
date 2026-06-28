---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-28_device-code-phishing-add-your-own-sign-in-methods-on-entra-id.md
original_filename: 2024-01-28_device-code-phishing-add-your-own-sign-in-methods-on-entra-id.md
title: Device Code Phishing – Add Your Own Sign-In Methods on Entra ID
category: documents
detected_topics:
- oauth
- mfa
- otp
- access-control
- command-injection
- password-reset
tags:
- imported
- documents
- oauth
- mfa
- otp
- access-control
- command-injection
- password-reset
language: en
raw_sha256: da8013ead5c4624f2ae9324b214855fd031eed81ce455c795b9ae9f252c02dff
text_sha256: ed2278b8b74e4a90c33d03a0fa8edfd9e0f888ca1a55e5404e47b5e8b437ec49
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Device Code Phishing – Add Your Own Sign-In Methods on Entra ID

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-28_device-code-phishing-add-your-own-sign-in-methods-on-entra-id.md
- Source Type: markdown
- Detected Topics: oauth, mfa, otp, access-control, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `da8013ead5c4624f2ae9324b214855fd031eed81ce455c795b9ae9f252c02dff`
- Text SHA256: `ed2278b8b74e4a90c33d03a0fa8edfd9e0f888ca1a55e5404e47b5e8b437ec49`


## Content

---
title: "Device Code Phishing – Add Your Own Sign-In Methods on Entra ID"
page_title: "Device Code Phishing – Add Your Own Sign-In Methods on Entra ID – Compass Security Blog"
url: "https://blog.compass-security.com/2024/01/device-code-phishing-add-your-own-sign-in-methods-on-entra-id/"
final_url: "https://blog.compass-security.com/2024/01/device-code-phishing-add-your-own-sign-in-methods-on-entra-id/"
authors: ["Felix Aeppli"]
programs: ["Microsoft"]
bugs: ["Phishing"]
publication_date: "2024-01-28"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 488
---

TL;DR An attacker is able to register new security keys (FIDO) or other authentication methods (TOTP, Email, Phone etc.) after a successful device code phishing attack. This allows an attacker to backdoor the account or perform the self-service password reset for the account with the newly registered sign-in methods. Although we see a great security risk, Microsoft deemed this not a vulnerability.

# Device Code Phishing

For those of you who have never heard of device code phishing, the following blogs are very insightful:

  * <https://aadinternals.com/post/phishing/>
  * <https://0xboku.com/2021/07/12/ArtOfDeviceCodePhish.html>

In short, device code phishing is the misuse of the OAuth2 Device Authorization Grant flow (RFC 8628). This flow is intended for devices with limited or no keyboard interaction, such as TVs or desk phones. Basically, a user can start a login flow on one device and finish it on another device with better keyboard input. As an attacker, we can also initiate the flow and have the victim complete it. To do this, the attacker impersonates an existing application (client) on Azure and, if the phishing is successful, gains the application’s permissions combined with the user’s permissions for the requested resource.

[![](https://blog.compass-security.com/wp-content/uploads/2023/10/image-8.png)](https://blog.compass-security.com/wp-content/uploads/2023/10/image-8.png)Delegated access from https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http

We recently published our tooling to perform device code phishing, for more information read the following article: <https://blog.compass-security.com/2023/10/device-code-phishing-compass-tooling/>.

## mysignins.microsoft.com – Self-Service

Users in Entra ID can normally manage their own login methods via <https://mysignins.microsoft.com/security-info>. A user can manage authentication methods such as TOTP, phone, email, security key, etc., depending on what the tenant’s administrator has allowed.

[![](https://blog.compass-security.com/wp-content/uploads/2023/10/image-9-1024x404.png)](https://blog.compass-security.com/wp-content/uploads/2023/10/image-9.png)Security-Info for a user in Entra ID

By intercepting the OAuth 2 calls while accessing the mysignins web application, we were able to identify the access token requirements.

The scope and audience must be set to `Microsoft App Access Panel (0000000c-0000-0000-c000-000000000000)`. The client ID can be set to any member of the FOCI1 family. It is not clear why FOCI1 group has the necessary permissions. One explanation for this could be that the `Microsoft Authenticator App (4813382a-8fa7-425e-ab75-3b753aab3abb)` is member of the FOCI1 group and allows to update the security info.

[![](https://blog.compass-security.com/wp-content/uploads/2024/01/image-1.png)](https://blog.compass-security.com/wp-content/uploads/2024/01/image-1.png)Microsoft Authenticator App – Update security info 

### Family of Client IDs (FOCI)

Normally, a refresh token for application Y cannot be used to get an access token for application X. But in Azure there is something called “Family of Client IDs”. Microsoft “groups” some applications into the same family. Members of the same family can exchange their refresh token for tokens of another family member. Check out this [GitHub ](https://github.com/secureworks/family-of-client-ids-research/)repository for a list of clients and their permissions on various APIs.

## ngcmfa claim

To set a new security key, the ngcmfa claim must be present in the access token. This is not required to add other authentication methods such as phone, email or TOTP. The ngcmfa claim is only valid for ~15 minutes after authentication. This gives the attacker a short window of time after the user has authenticated to register their own security key.

# PoC – deviceCode2SecurityKey

With the required scope, client ID, token requirements and web application calls, we were able to write a PoC that allows to initiate a device code flow and register a security key for the victim’s account when it is completed. You can find the PoC code here: <https://github.com/CompassSecurity/deviceCode2SecurityKey>

This allows you to authenticate to services without a password or additional 2FA method. It is also possible to register email, phone or TOTP tokens, but this is not implemented in the PoC. Here is a brief description of the PoC:

  1. Our code initiates the device code flow with the required parameters.
  2. The user code is sent to the victim. The victim logs in and provides the required consent.
  3. We then request the required tokens (sessionCtx) and initiate the registration of a new security token.
  4. For that, we open Chrome which is used to interact with the security key (webauthn interface).
  5. When the security key is registered, the PoC completes the registration.
  6. It is now possible to log in as a user without a password or 2FA key.

The following video shows the whole process:

# Disclosure process

This issue was raised with the Microsoft Security Response Center (MSRC) on September 14th 2023 and we didn’t hear back from them until 8 December 2023.

Their response states that:

> “The functionality for adding authentication methods is behaving as designed in that it validates the MFA claim and ensures it was created within 15 minutes. The core vulnerability here is the Device Code Phishing attack, which results in a valid MFA claim being generated. This is already known and well documented.”
> 
> MSRC

From our point of view, even though Device Code Phishing is already known and well documented, our attack is new and allows persistence into the account of the target victim. As the ngcmfa claim is only necessary when adding a security key, this seems to be a special operation. Furthermore the fact that the FOCI1 group has the permissions to add such authentication methods is in our opinion concerning.

# Prevention and Detection of Device Code Phishing

As mentioned in our previous post, it is not currently possible to disable device code flow for Microsoft’s first-party applications.

The most effective way to limit the risk is to set restrictive Conditional Access (CA) policies so that only MDM/MAM managed devices are allowed to connect. Another option is to restrict logins from known IP addresses. This works because the IP address of the flow initiator is checked against the CA.

Detection, on the other hand, is fairly straightforward. Monitor the Sign-In logs for authentication protocol = device code

[![](https://blog.compass-security.com/wp-content/uploads/2023/10/image-5.png)](https://blog.compass-security.com/wp-content/uploads/2023/10/image-5.png)

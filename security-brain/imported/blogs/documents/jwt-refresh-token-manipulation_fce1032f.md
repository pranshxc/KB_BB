---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-16_jwt-refresh-token-manipulation.md
original_filename: 2017-11-16_jwt-refresh-token-manipulation.md
title: JWT Refresh Token Manipulation
category: documents
detected_topics:
- jwt
- sso
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- jwt
- sso
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: fce1032f9457e17b6e0b75d8a2a10054bddd830edbcb416e62ceece884d41ce4
text_sha256: 500e2d4119e8ecc815161393d521b3742154781d8782ba9cf2563803a8159c46
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# JWT Refresh Token Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-16_jwt-refresh-token-manipulation.md
- Source Type: markdown
- Detected Topics: jwt, sso, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `fce1032f9457e17b6e0b75d8a2a10054bddd830edbcb416e62ceece884d41ce4`
- Text SHA256: `500e2d4119e8ecc815161393d521b3742154781d8782ba9cf2563803a8159c46`


## Content

---
title: "JWT Refresh Token Manipulation"
page_title: "JWT Refresh Token Manipulation – Mikail's Blog"
url: "https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/"
final_url: "https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/"
authors: ["Mikail Tunç (@emtunc)"]
bugs: ["JWT", "Authentication bypass", "Account takeover"]
publication_date: "2017-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6049
---

Categories 

[Tech](https://emtunc.org/blog/category/tech/)

# JWT Refresh Token Manipulation

  * Post author  By [Mikail](https://emtunc.org/blog/author/e-mikail-t/)
  * Post date  [November 16, 2017](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/)
  * [1 Comment on JWT Refresh Token Manipulation](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/#comments)

This is a quick blog about a bug I found in a private bounty program on [Bugcrowd](https://bugcrowd.com/emtunc). The reason for me writing about it is to increase awareness around these issues and implementation flaws so that fellow bug bounty hunters/people in Infosec/developers can use the information in this article for the betterment of security.

The bug I found was in an application’s implementation of the [JSON Web Token (JWT)](https://jwt.io/) refresh token.

Usually, in response to a JWT authentication/refresh request you’ll get something that looks like this:
  
  
  {"code":0,"data":{"access_token":"XXX.YYY.ZZZ","access_token_expiration":"Thursday, November 9th, 2017, 10:27:33 PM","refresh_token":"ABC123"}}

Here you have an access token and a refresh token. Both are very sensitive and should never be leaked… in an ideal world 🙂

The access token in this example expires on the 9th November 2017 at 10:27:33PM. Usually a (proactive/well designed) mobile/web/client application will use the refresh token to refresh/get a new access token before the expiry date. That request goes to an Authorization Server and looks a bit like this:
  
  
  POST /auth/refresh HTTP/1.1
  Host: auth.example.com
  Content-Type: application/json
  Authorization: Bearer XXX.YYY.ZZZ
  
  {"refresh_token":"ABC123"}

The current access token goes in the Authorization header and the refresh token in the POST body. In return you get a brand new access token, expiry date and refresh token. All good so far.

But what happens if the access token gets leaked or compromised? Well it shouldn’t matter because that would mean the refresh token would also have had to be leaked **and** be valid **and** not be used already (refresh tokens should be one-time use) **and** not be revoked.

All of this relies on the Authorization Server doing its job, properly.

In the case of the bug that I had found, the Authorization Server was  _not_ checking the refresh token <–> access token association. What this meant was that I could refresh someone else’s access token using **my** refresh token.

In theory this could have allowed an attacker to grab an old JWT access token (it doesn’t matter if it’s a day old or a year old – the token is cryptographically signed by the server so it would still be valid even if it has expired) and use a refresh token of a test account to get a brand new, valid access token for the victim account. The impact here is significant and it would be very difficult to revoke an access token in this scenario. Here’s what the JWT handbook has to say about refresh tokens:

_“Refresh tokens, by virtue of being long-lived, must be protected from leaks. In the event of a leak,  
blacklisting may be necessary in the server (short-lived access tokens force refresh tokens to be used  
eventually, thus protecting the resource after it gets blacklisted and all access tokens are expired)”_

In the above, misconfigured scenario… the remediation step of revoking a token makes no difference because an attacker can use any refresh token.

The fix? Make sure the Authorization Server validates the refresh token belongs to the user submitting the access token. An access token should never be refreshed without the corresponding, correct refresh token.

### Share this:

  * [ Email a link to a friend (Opens in new window) Email ](/cdn-cgi/l/email-protection#8eb1fdfbece4ebedfab3abbbccdde6effcebeaabbcbedee1fdfaabbbcaabbcbec4d9daabbcbedcebe8fcebfde6abbcbedae1e5ebe0abbcbec3efe0e7fefbe2effae7e1e0a8adbebdb6b5ece1eaf7b3e6fafafefdabbdcfabbcc8abbcc8ebe3fafbe0eda0e1fce9abbcc8ece2e1e9abbcc8bfbfabbcc8bcbebfb9abbcc8e4f9faa3fcebe8fcebfde6a3fae1e5ebe0a3e3efe0e7fefbe2effae7e1e0abbcc8a8adbebdb6b5fde6effcebb3ebe3efe7e2)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=twitter)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=jetpack-whatsapp)
  * [ Share on Reddit (Opens in new window) Reddit ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=reddit)
  * [ Share on Telegram (Opens in new window) Telegram ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=telegram)
  * [ Share on Facebook (Opens in new window) Facebook ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/?share=facebook)
  * [ Print (Opens in new window) Print ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/#print?share=print)
  * 

* * *

[ ← Bypassing Safe Links in Exchange Online Advanced Threat Protection ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/) [ → My Research on Misconfigured Jenkins Servers ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/)

* * *

##  One reply on “JWT Refresh Token Manipulation” 

![](https://secure.gravatar.com/avatar/28175e09b9fc38a454dde969413507dcbafa7a7a2c626523f7d23dd6177603bb?s=120&d=monsterid&r=g)Neil Andersonsays:

[November 19, 2017 at 6:08 PM](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/#comment-5299)

Mikail, you are a rock. Personally, I have gotten a lot of information through the post. Great article thanks and keep up the great work!

* * *

Comments are closed.

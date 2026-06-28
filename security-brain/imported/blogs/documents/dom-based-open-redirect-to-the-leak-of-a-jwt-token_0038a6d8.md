---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-20_dom-based-open-redirect-to-the-leak-of-a-jwt-token.md
original_filename: 2020-04-20_dom-based-open-redirect-to-the-leak-of-a-jwt-token.md
title: DOM based open redirect to the leak of a JWT token
category: documents
detected_topics:
- oauth
- jwt
- command-injection
- otp
- api-security
tags:
- imported
- documents
- oauth
- jwt
- command-injection
- otp
- api-security
language: en
raw_sha256: 0038a6d859091c73d70db864485fc445a07fdc5ae36819e39862067e9b65bfd7
text_sha256: 3bd4bc1dad4ebe89f3ec104baad7c4095a24b3e6bde752a63b7cd9b8f4016598
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# DOM based open redirect to the leak of a JWT token

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-20_dom-based-open-redirect-to-the-leak-of-a-jwt-token.md
- Source Type: markdown
- Detected Topics: oauth, jwt, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `0038a6d859091c73d70db864485fc445a07fdc5ae36819e39862067e9b65bfd7`
- Text SHA256: `3bd4bc1dad4ebe89f3ec104baad7c4095a24b3e6bde752a63b7cd9b8f4016598`


## Content

---
title: "DOM based open redirect to the leak of a JWT token"
url: "https://medium.com/@adam.adreleve/dom-based-open-redirect-to-the-leak-of-a-jwt-token-1b1dd2ced9a1"
authors: ["Adolphoramirez"]
bugs: ["Open redirect", "DOM-based open redirect", "Token leak"]
publication_date: "2020-04-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4643
scraped_via: "browseros"
---

# DOM based open redirect to the leak of a JWT token

Adolphoramirez
 highlighted

DOM based open redirect to the leak of a JWT token
Adolphoramirez
Follow
2 min read
·
Apr 20, 2020

9

1

Dom-based open redirects can be underestimated on pentests/bug bounty programs. However, depending on the application’s context, this kind of security vulnerability can lead to critical impacts as some information can leak through the referrer header.

On a private program on Hackerone i noticed that when logging out of your session, you reached /logout/landing.html?originalUrl=/logina log out page with only a “Click here” <a> tag. When analyzing the DOM of the page i saw that the following JS event listener was attached to the ”Click here” button :

The redirection was JS based to the login flow and lead us to a OAuth API that signed the pathname provided on the originalUrl parameter and concatenated it with window.location.host’s value. So, inserting hello in the originalurl parameter will then lead to the following redirection when the “Click here” button is clicked :

Get Adolphoramirez’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://redacted.comhello/?logincallback=true

On modern browsers ( FF, Chrome, etc ), domain.com@anotherdomain.com will lead to anotherdomain.com

So i tried to inject the originalurl parameter with @burpcollaborator.net and when the click here button was clicked i directly reached my collaborator.

At this point i have a DOM-based open redirect. Though, as the Oauth API was operating the redirection and the response type was set to code, the authentication JWT token was leaking through the referrer header of the request made to my server.

A potential attacker could then use the JWT token to log into the victim’s account, this leading to a account takeover.

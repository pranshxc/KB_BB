---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-06_how-we-escalated-a-dom-xss-to-a-sophisticated-1-click-account-takeover-for-8000-.md
original_filename: 2024-04-06_how-we-escalated-a-dom-xss-to-a-sophisticated-1-click-account-takeover-for-8000-.md
title: How we escalated a DOM XSS to a sophisticated 1-click Account Takeover for
  $8000 - Part 1
category: documents
detected_topics:
- oauth
- xss
- sso
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- oauth
- xss
- sso
- access-control
- command-injection
- mfa
language: en
raw_sha256: 38b597fd6720cfccd8e5499d88aecff676b58f8d908a2628ffd882a31805790c
text_sha256: 5f17c4b94ba4a9d4f0f1f8eb12749fae3ce6bd04d32ead6c20af6540122865f7
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# How we escalated a DOM XSS to a sophisticated 1-click Account Takeover for $8000 - Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-06_how-we-escalated-a-dom-xss-to-a-sophisticated-1-click-account-takeover-for-8000-.md
- Source Type: markdown
- Detected Topics: oauth, xss, sso, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `38b597fd6720cfccd8e5499d88aecff676b58f8d908a2628ffd882a31805790c`
- Text SHA256: `5f17c4b94ba4a9d4f0f1f8eb12749fae3ce6bd04d32ead6c20af6540122865f7`


## Content

---
title: "How we escalated a DOM XSS to a sophisticated 1-click Account Takeover for $8000 - Part 1"
url: "https://thefrogsec.github.io/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-1/"
final_url: "https://thefrogsec.github.io/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-1/"
authors: ["Benasin (@Benasin3)", "LongTheShrimp (@LongShrimp0812)"]
bugs: ["DOM XSS", "Account takeover", "OAuth"]
bounty: "8,000"
publication_date: "2024-04-06"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 351
---

#  How we escalated a DOM XSS to a sophisticated 1-click Account Takeover for $8000 - Part 1 

Benasin, LongTheShrimp

2024-04-06

__[ato](/tags/ato/), [bugbounty](/tags/bugbounty/), [client-side](/tags/client-side/), [dom-xss](/tags/dom-xss/), [oauth2](/tags/oauth2/), [xss](/tags/xss/)

## I. Introduction

Today Frog Sec Team will dive into a fascinating case study where we escalated a seemingly simple DOM XSS into a sophisticated 1-click Account Takeover. 

This attack allows the attacker to send a legitimate login link from the application’s email. When the victims (whether unauthenticated or authenticated) clicks on the link from their email, the attacker will be able to compromised the accounts.

We will take you through our thought process, the obstacles we encountered, and how we overcame them to execute this full chain exploit.

Because this is quite a long read, we will split this blog post into 2 parts:

  * Part 1: Understanding the OAuth login flow and the initial attack surface
  * [Part 2: Exploiting the DOM XSS and escalating it to a 1-click Account Takeover](/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-2/)

Let’s goooo 😤😤😤

## II. Understanding the OAuth login flow and the text-book OAuth attack

It would have been impossible to find this vulnerability if we hadn’t understood deeply about the underlying architecture and potential attack vectors of the system.  
Let’s first have a clear understanding of the target.

We will refer the target as `account.redacted.com` and their partner sites as `account.partner.com` because we didn’t have the permission to disclose the program’s name. 

### 1\. Investigating the login flow of the application 👀

Out of all functionalities, we chose to test for the login flow first because this might be where the High/Critical vulnerabilities are hidden from plain sight.

`account.redacted.com` will have a Single Sign On (SSO) portal where other partner sites will integrate this portal to log the users in their services. 

Here is the sequence diagram of the complete OAuth flow:

![](/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-1/Untitled.png)

  1. The user will click login to `account.partner.com`

2,3. `account.partner.com` will generate and return the `code_verifier` through the `xxxxx-pkce` cookie and redirect the browser to `https://account.redacted.com/authorize` with the `redirect_uri` parameter
  
  
  1  
  2  
  3  
  

| 
  
  
  HTTP/2 302 Found  
  Set-Cookie: xxxxx-pkce=<code_verifier>; Path=/; Expires=Tue, 26 Mar 2024 11:25:07 GMT  
  Location: https://account.redacted.com/authorize?redirect_uri=https%3A%2F%2Faccount.partner.com%2Foauth_callback%3Fnext%3D%2Fabc&response_type=code&code_challenge=<code_challenge>  
  
  
---|---  
  
  * Particularly, this `redirect_uri` is

  
  
  1  
  

| 
  
  
  https://account.partner.com/oauth_callback?next=/abc  
  
  
---|---  
  
  * If you wonder what is `code_verifier`, according to [auth0.com](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce)

> The PKCE-enhanced Authorization Code Flow introduces a secret created by the calling application that can be verified by the authorization server; this secret is called the Code Verifier. Additionally, the calling app creates a transform value of the Code Verifier called the Code Challenge and sends this value over HTTPS to retrieve an Authorization Code. This way, a malicious attacker can only intercept the Authorization Code, and they cannot exchange it for a token without the Code Verifier.

  * So basically, `code_verifier` is an additional layer to protect the `Authorization Code`, in order to exchange for the access token, we also need the `code_verifier` associated with that `authorization_code`

4,5. User will be prompted a login page at the `account.redacted.com` SSO Portal, or redirected if already logged in.

  6. The `redirect_url` will be formed by concatenating the `authorization_code` after the previously supplied `redirect_uri`
  
  1  
  

| 
  
  redirect_url = redirect_uri + "<authorization_code>"  
  
  
---|---  
  7. Then, the browser will be redirected to the `redirect_url`

  8. Next `account.partner.com` will be able to get the authorization code through the redirection from `account.redacted.com`. 

  * The redirection URL will look something like this:
  
  1  
  

| 
  
  https://account.partner.com/oauth_callback?next=/abc&code=<authorization_code>  
  
  
---|---  
  * `next`: is the URL to be redirected after the `authorization_code` is used and verified successfully
  * `code`: is where the application will get the `authorization_code`
  * The front end Javascript will then use the `code` to exchange for the access token at `POST / access_token`
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  

| 
  
  POST /access_token HTTP/2  
  Host: account.partner.com  
  Cookie: xxxxx-pkce=<code_verifier>  
  Content-Length: 306  
  Content-Type: application/x-www-form-urlencoded  
  
  code=<authorization_code>&grantType=authorization_code&redirect_url=<redirect_url>  
  
  
---|---  
  9. Notice that the `code_verifier` must be associated with the `authorization_code` in order for the exchange of access token to be successful.

If the `code_verifier` and `authorization_code` are valid, the access token will be returned and set as the cookie.
  
  1  
  2  
  

| 
  
  HTTP/2 201 Created  
  Set-Cookie: accessToken=na3+CYtH7TAt+kjebEZgjJ4m37V8Qkxb+GhMw1FlU7gnELDBevy3qGJADAsNfBKSjoujZhgILLU+M8n49DrRd8+yZS1Jco2M04KWqbp64B8ASHPM6llTqZc=; Domain=partner.com  
  
  
---|---  
  10. Finally, the application will redirect the page to the URL at the `next` parameter of the `oauth_callback` endpoint from step 3, which is redirecting to `https://account.partner.com/abc`

### 2\. Trying out the text-book OAuth attack 📚

![](/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-1/Untitled%201.png)

Our first approach ís to tamper the `redirect_uri` parameter at step 3 of the login flow. For example:
  
  
  1  
  

| 
  
  
  https://account.redacted.com/authorize?redirect_uri=https://attacker.com&response_type=code  
  
  
---|---  
  
We will then send this tampered link to the victim.

If the login flow is successful, the code will be attached to the `https://attacker.com` domain at step 7, thus the attacker can obtain the authorization code.
  
  
  1  
  

| 
  
  
  https://attacker.com/?code=<authorization_code>  
  
  
---|---  
  
However, things aren’t that easy ¯\_(ツ)_ /¯

The application would reject any `redirect_uri` which isn’t having the domain name [account.partner.com](http://account.partner.com/) and only accepts `http` and `https` protocol. 

Fortunately, we can still modify the URL path to anything we want. For example:
  
  
  1  
  

| 
  
  
  https://account.redacted.com/authorize?redirect_uri=https://account.partner.com/<anything_here>&response_type=code  
  
  
---|---  
  
Another way to exploit this is to find an Open Redirect on `https://account.partner.com` so we can redirect the authorization code to our server.

In step 10 of the login flow, we have mentioned that there is another redirect at `https://account.partner.com/oauth_callback?next=`

One interesting thing is there isn’t any `302` or redirecting status code from the server, indicating that the application is being redirected using JavaScript.

Let’s examine the redirect sink!

### [Click here to read part 2 and see how we escalated the DOM XSS to a 1-click Account Takeover.](/2024/04/06/How-we-escalated-a-DOM-XSS-to-a-sophisticated-1-click-Account-Takeover-for-8000-Part-2/)

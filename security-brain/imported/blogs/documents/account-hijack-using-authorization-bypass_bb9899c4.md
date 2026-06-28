---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-28_account-hijack-using-authorization-bypass-.md
original_filename: 2020-02-28_account-hijack-using-authorization-bypass-.md
title: Account Hijack using Authorization bypass $$$$
category: documents
detected_topics:
- access-control
- sso
- jwt
- oauth
- saml
- command-injection
tags:
- imported
- documents
- access-control
- sso
- jwt
- oauth
- saml
- command-injection
language: en
raw_sha256: bb9899c492e62e073b2c4c02b5d6dc5d59e3eefece346628b6061433db623c80
text_sha256: 7d367362493b49ddd6a773bac92fb3bc1bc49a55fbba428e15af2b3462fd029a
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Account Hijack using Authorization bypass $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-28_account-hijack-using-authorization-bypass-.md
- Source Type: markdown
- Detected Topics: access-control, sso, jwt, oauth, saml, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `bb9899c492e62e073b2c4c02b5d6dc5d59e3eefece346628b6061433db623c80`
- Text SHA256: `7d367362493b49ddd6a773bac92fb3bc1bc49a55fbba428e15af2b3462fd029a`


## Content

---
title: "Account Hijack using Authorization bypass $$$$"
url: "https://medium.com/@bhaveshthakur2015/account-hijack-using-authorization-bypass-which-made-me-richer-by-ba9dace72682"
authors: ["Bhavesh Thakur (@Bhavesh_Thakur_)"]
bugs: ["Account takeover", "Broken authorization"]
publication_date: "2020-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4745
scraped_via: "browseros"
---

# Account Hijack using Authorization bypass $$$$

Account Hijack using Authorization bypass $$$$
Bhavesh Thakur
Follow
7 min read
·
Feb 29, 2020

404

2

Hello readers,

Today I am going to share one of my findings by which I was able to perform complete account takeover. Before proceeding let’s understand what authorization is. It’s a mechanism by which application decides that authenticated user is eligible to access a particular resource or not. This can be understood in a simpler way by the following example:

There are two employees in a company. They both have access to their office but they can’t access someone’s locker except their own. Also, these employees can’t see someone’s salary slip or personal details except their own. Now think if an employee can see someone’s personal details or salary slip or any confidential data which he is not authorized to? This will be a great threat to the confidentiality of the company. Here this is called vulnerability into the system.

One more example is the driver’s license of someone. A photograph on driver license proves who you are (Authentication) and the vehicle mentioned on it which you are allowed to drive is nothing but Authorization. It can be clearly understood that both Authentication and Authorization are an integral part of any mechanism which follows role-based access.

To understand Authorization more clearly let’s understand authentication first because I have seen many of the developers are not seeing both as different entities leaving their application vulnerable to broken access control.

Popular Authentication Mechanisms

1. HTTP Basic Authentication: This approach requires username and password through HTTP Header itself which is encoded in base64. It is not recommended because it sends username and password in plain text which can easily be obtained through main in the middle attack. To avoid this situation developers need to encrypt this data. But again this will affect the speed of the application because the server has to decrypt each HTTP request.

2. Digest Authentication: In this method, the authorization header takes username and password which is sent to the hash function which uses MD5 cryptographic hashing with nonce before sending it to the server. This mechanism is vulnerable to brute force attacks and MD5 collision attacks.

3. Cookies: Whenever a user logs in to the application server generates session cookies in the user’s browser. As you know HTTP is a stateless protocol so there is a requirement to send these session cookies in each request to the server. Once the server receives any request from the user it checks for the valid session cookies. If cookies are valid application identifies who is the logged-in user.

4. Bearer Tokens: In this mechanism, authentication is performed via tokens. After providing the correct credentials server generates a token that is sent to the server in every request.

The only identification of the logged-in user can’t help to define access related issues. Now to identify the roles and user rights for that authenticated user application needs to perform authorization checks. This can be done in the following ways.

1. JWT Tokens: It’s a method to transmit data as a JSON object. This information is digitally signed. It can be signed using a SECRET or Public/private key using the RSA encryption algorithm. A JSON Web Token consists of three parts: Header, Payload, and Signature. The header and payload are Base64 encoded, then concatenated by a period, finally, the result is algorithmically signed producing a token in the form of [HEADER].[CLAIMS].[SIGNATURE]. The header consists of metadata including the type of token and the hashing algorithm used to sign the token.

2. OAuth: This mechanism defines a delegation protocol that is useful for conveying authorization decisions across a network of web-enabled applications and APIs. OAuth standards for open-standard authorization protocol or framework that describes how distributed and non-connected servers and services can safely allow authenticated access to their assets without actually sharing the initial, related, single login credential.

3. SAML (Security Assertion Mark-up Language): Security Assertion Mark-up Language (SAML) is a framework for authorization between two parties. It has two mechanisms Service Provider and Identity Provider. Identity provider provides authentication to the application and service provider trusts this information to provide authorization. This is done through an exchange of digitally signed XML documents.

Now I will explain to you how I was able to bypass the authorization mechanism of an application and was able to access someone’s data.

Now I am going to describe one of my findings in which I was able to bypass authorization on a particular module. The same vulnerability was exploited using improper validation of the old password to hijack the account of any end-user!

In the profile section of that application, there was an option to get details of the end user’s activity. I found that there were multiple activities performed already like password reset, image upload, first name updated, etc. I noticed that whenever I am clicking on any activity it is showing me the date, IP, information related to the action performed, and activity ID. From this information what I was supposed to do I can validate if I have performed these activities or not? Or I else if I see any malicious activity, I can change my password. When I clicked any particular activity, I observed the URL was like below:

URL: https://example.com/account/activities/

Get Bhavesh Thakur’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Below was the actual request

Press enter or click to view image in full size

Below was the response:

Press enter or click to view image in full size

By observing the response, I noticed that each activity has an ID. Luckily numerical only. Also, there was a link to report if that activity was found suspicious. While hitting the report link there was an option to reset password and also log out from all devices. One strange behavior I observed in the below request.

Press enter or click to view image in full size

This request was changing the password if the activity was found malicious. I sent an original request to the server and observed that the current session became invalidated immediately. What!! this was pretty cool. I performed the same activity but changed parameter report-block to false. This time nothing happened. I was not thrown out of the session. But I observed the response which was the same as the previous response. To verify the same, I logged- and tried to log in again. Strangely I was successfully logged in. I thought the report-block parameter was responsible for this behavior. I set it to false that’s why this request was not entertained by the server even though the response was the same.

But wait … why my account activity is showing that I just reset my password.

Press enter or click to view image in full size

Okay according to the application my password was changed. But how, I did not enter my current password while reporting. I performed the same action and concluded that the report module was not verifying the old password at all! This was a finding but still, severity was low.

I tried to brute force report ID but was getting a 403 response.

Now, this was the time to check authorization for this request. I observed there are 3 headers in the request which are having random IDs. First, I removed the Authorization header and sent the request to the server. The application immediately threw an error. Okay, this header is essential. Now I removed HUXID and AUXID and sent the request to the server.

Press enter or click to view image in full size

Still, I got a 403 response from the server. Now there was no other option than URL tampering. I removed the report id from the request I got below response from the server.

Press enter or click to view image in full size

I tried multiple things to bypass this restriction and finally, I got success using the below method.

Press enter or click to view image in full size

I just appended blah/../../../report/<activity id of another account>/ to the original URL and voila!! I got a 200 OK response. I immediately tried to log in with my other account with the newly set password and yes I was successfully logged in!

I verified this vulnerability multiple times and observed the same behavior! I quickly created a video POC and reported it. They patched the same within three days and awarded me $$ in 4 digits.

The vulnerability which was exploited: Improper validation of old password in a module + bypass authorization using URL manipulation

For any feedback or suggestions reach out to me @ Bhavesh

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

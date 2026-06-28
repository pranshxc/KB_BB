---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-15_this-is-why-you-shouldnt-trust-your-federated-identity-provider.md
original_filename: 2021-09-15_this-is-why-you-shouldnt-trust-your-federated-identity-provider.md
title: This is why you shouldn’t trust your Federated Identity Provider
category: documents
detected_topics:
- oauth
- sso
- password-reset
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- oauth
- sso
- password-reset
- command-injection
- mfa
- api-security
language: en
raw_sha256: 19d14a8b7fd8b506b723dd446dbf1a4d8cdb35818e501e1c2587f5eab12ad240
text_sha256: 11150808288fd72948da98e911a76dc9b09421624abeb8ce693cc4bf5f4ea03b
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# This is why you shouldn’t trust your Federated Identity Provider

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-15_this-is-why-you-shouldnt-trust-your-federated-identity-provider.md
- Source Type: markdown
- Detected Topics: oauth, sso, password-reset, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `19d14a8b7fd8b506b723dd446dbf1a4d8cdb35818e501e1c2587f5eab12ad240`
- Text SHA256: `11150808288fd72948da98e911a76dc9b09421624abeb8ce693cc4bf5f4ea03b`


## Content

---
title: "This is why you shouldn’t trust your Federated Identity Provider"
url: "https://medium.com/@soufianehabti/this-is-why-you-shouldnt-trust-your-federated-identity-provider-62160f50d8b2"
authors: ["Soufiane Habti (@wld_basha)"]
bugs: ["OAuth", "Account takeover", "Authentication bypass"]
bounty: "1,500"
publication_date: "2021-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3312
scraped_via: "browseros"
---

# This is why you shouldn’t trust your Federated Identity Provider

This is why you shouldn’t trust your Federated Identity Provider
Soufiane Habti
Follow
4 min read
·
Sep 14, 2021

273

1

Last year, while taking my daily dose of 
HackerOne
’s Hacktivity, I stumbled upon this amazing writeup of cache-money where he demonstrated the ability to take over accounts on third party apps that are using ‘sign with Gitlab’ just by bypassing email verification on GitLab, during that time I was interested in Oauth2.0 misconfigurations, therefore I tried to understand how an identity provider can prove that the identity’s email is verified and it really belongs to the person who is trying to access it resources.

According to Auth0 documentation there’s a field called email_verified provide the information about the email used in the flow is verified or not, and as the documentation said :

The email_verified field of a user profile indicates whether the user has verified their email address. Email verification is optional, but valid email addresses are required for certain actions, such as sending email communications, password reset/recovery links, and passwordless magic links to users.

An email is usually verified immediately after the user account is created or when the user logs in to the application for the first time. It’s a good way to know that the person signing up actually owns the email at that moment.

Pitfalls of an innocent field :

Let’s get back again to Auth0 documentation:

Press enter or click to view image in full size

As you see on the screenshot the documentation is showing developers possible attack scenarios, and the field should be checked by the application using the federated identity provider. Before this we already know how the field is set :

When users authenticate with a federated identity provider (e.g. a social or enterprise connection), the value of the email_verified field will match what the identity provider returns in the user profile. If the identity provider does not return any value, it will be set to false.

Many famous identity providers are handling this perfectly (jk someone will hack them it in future m sure :) ) as an example when trying to authenticated with Facebook using an unverified email, the authentication flow will redirect you to the verification page if the email still not verified.

Press enter or click to view image in full size

But some identity providers don’t add the email_verified field to the flow and it isn’t checked from the application side, therefore the possibility to perform an account take over is high since some applications use the linking accounts mechanism, so when you authenticate for example from Facebook using test@example.com the app will automatically redirect you to an account that registered under this email.

Case Study in bug bounty :

While going through a web application from a private program let’s call it target.com I noticed it is using multiple authentication mechanism including such as authentication using Google, Facebook, and a third one which appeared unfamiliar, we will call it provider.com, so I tried to apply what I learned I tried to register using an email ‘victim@gmail.com’ which is already registered on target.com during the registration flow on provider.com I found that you can access your profile and application resources without completing the email verification, after trying to authenticated using this provider the application logged me to victim@gmail.com without any restrictions.

Maybe worse ?

After this successful ATO, I remembered that the company has an asset called admin.target.com that is using [at]target.com for authentication as well as Oauth2.0 using the vulnerable provider, so I looked on GitHub for emails of target.com and I found couple of them, luckily enough those emails weren’t registered on provider.com then I managed to bypass the authentication but the admin panel was protected with 2FA so I stopped there.

Get Soufiane Habti’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After reporting the account take over through HackerOne, the security team of target.com implemented a step of email verification where they send a code that expires in 5 mins to your email, they reported the issue to the identity provider but it hasn’t been fixed yet, and the bug is still there in the wild used by many developers.

The company awarded me 1500$ for this ATO

Resources :

Use Verified Email in User Profiles
The email_verified field of a user profile indicates whether the user has verified their email address. Email…

auth0.com

GitLab disclosed on HackerOne: Ability to bypass email verification...
Summary There's a limitation that requires a validated email before going through the OAuth flow, however this is…

hackerone.com

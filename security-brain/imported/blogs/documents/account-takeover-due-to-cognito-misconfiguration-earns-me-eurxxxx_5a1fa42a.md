---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-29_account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx.md
original_filename: 2022-12-29_account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx.md
title: Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx
category: documents
detected_topics:
- sso
- jwt
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- sso
- jwt
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 5a1fa42a4f1bfa6c58d94ba0800b0ffb4997f58691dfd1d094bed1a50f12fec9
text_sha256: 45c0aef44b4e4d89570af7ad5b9338595f4d93afd9d8350b43550be72704e943
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-29_account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx.md
- Source Type: markdown
- Detected Topics: sso, jwt, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `5a1fa42a4f1bfa6c58d94ba0800b0ffb4997f58691dfd1d094bed1a50f12fec9`
- Text SHA256: `45c0aef44b4e4d89570af7ad5b9338595f4d93afd9d8350b43550be72704e943`


## Content

---
title: "Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx"
url: "https://medium.com/@mukundbhuva/account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx-3a7b8bb9a619"
authors: ["Mukund Bhuva (@MukundBhuva)"]
bugs: ["Amazon cognito misconfiguration", "Account takeover"]
publication_date: "2022-12-29"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1721
scraped_via: "browseros"
---

# Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx

Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx
Mukund Bhuva
Follow
3 min read
·
Dec 29, 2022

73

1

Hello Guys, I haven’t written anything in a long time.

Press enter or click to view image in full size
Photo by Arget on Unsplash

Vulnerability : Cognito Misconfiguration

Impact : Account Takeover

Severity : Critical

TL;DR

I was looking for a target late at night. I find a target with a medium scope. So I picked the target. I was doing my reconnaissance and found that the target was using AWS services, and more specifically, cognito, for customer identity and access management. I recall an exercise I did a while back.

Misconfigured AWS Cognito Attributes | Kontra
With Amazon Cognito "User Pools", developers can quickly add authentication features and workflows including sign up…

application.security

While looking into the application workflow, I discovered that the data was fetched from execute-api by email.

So I grabbed an access token and tried to get user details from the AWS CLI.

aws cognito-idp get-user --region $REGION --access-token $TOKEN

And I got the details as expected.

So, created 2 account :

Attacker : mukundbhuva+attacker@tld.me
Victim : mukundbhuva+victim@tld.me

I created a new token for the account mukundbhuva+attacker@tld.me and tried to change the email to mukundbhuva+victim@tld.me.

aws cognito-idp update-user-attributes --region $REGION --access-token $TOKEN --user-attributes Name=email,Value=mukundbhuva+victim@tld.me

I got an error :

An error occurred (AliasExistsException) when calling the UpdateUserAttributes operation: An account with the given email already exists.

I’m not able to change an email.

Problem : If the email is already registered.

However, the congito email structure is case-insensitive. So, I tried to change my email to MUKUNDbhuva+victim@tld.me

aws cognito-idp update-user-attributes --region $REGION --access-token $TOKEN --user-attributes Name=email,Value=MUKUNDbhuva+victim@tld.me 

Now, I was able to change attacker’s email to the victim’s.

But there was a problem: the API was not fetching victim details.

I recheck the details

aws cognito-idp get-user --region $REGION --access-token $TOKEN

The email was changed, but I was perplexed as to why the app couldn’t retrieve the victim’s information. After some research, I decoded the token in jwt.io. I found that the email was still the attacker’s email.

Get Mukund Bhuva’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And execute-api will decode the token, grab the email, and then fetch the details.

So I’m curious what would happen if I could create a token using the victim’s email address, but JWT signature validation was a problem.

After reading some documentation, I grab the token and craft a new token from the refresh token using the AWS cli.

aws cognito-idp initiate-auth --region $REGION --auth-flow REFRESH_TOKEN_AUTH --client-id $CLIENT_ID --auth-parameters REFRESH_TOKEN=$REFRESH_TOKEN

I got the new access token, checked the token with jwt.io, and the email was changed to mukundbhuva+victim@tld.me.

The problem was solved. I tried to access account details with execute-api, and it worked. Now I could access all the details about the victim.

When it was reported to the appropriate bug bounty program, it was quickly triaged and received a €XXXX bounty.

Resolve :

Press enter or click to view image in full size

I got an invite to have a drink with the team.

Press enter or click to view image in full size

Timeline :

Press enter or click to view image in full size
Timeline
References
Misconfigured AWS Cognito Attributes | Kontra
With Amazon Cognito "User Pools", developers can quickly add authentication features and workflows including sign up…

application.security

Thanks For Reading✌️, Keep Hunting! 😇

👏

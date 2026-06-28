---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_post-account-takeover-account-takeover-of-internal-tesla-accounts.md
original_filename: 2023-04-04_post-account-takeover-account-takeover-of-internal-tesla-accounts.md
title: Post Account Takeover? Account Takeover of Internal Tesla Accounts
category: blogs
detected_topics:
- sso
- jwt
- command-injection
- automation-abuse
- api-security
tags:
- imported
- blogs
- sso
- jwt
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6acd3d2886a9fd6fdf44898801668465cbe7537ca411422fc3673ae7542cdaf9
text_sha256: c8820a8d765f39663e735f279419f6d9a8b98c661ff206040a931b3337091adb
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Post Account Takeover? Account Takeover of Internal Tesla Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_post-account-takeover-account-takeover-of-internal-tesla-accounts.md
- Source Type: markdown
- Detected Topics: sso, jwt, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `6acd3d2886a9fd6fdf44898801668465cbe7537ca411422fc3673ae7542cdaf9`
- Text SHA256: `c8820a8d765f39663e735f279419f6d9a8b98c661ff206040a931b3337091adb`


## Content

---
title: "Post Account Takeover? Account Takeover of Internal Tesla Accounts"
url: "https://medium.com/@evan.connelly/post-account-takeover-account-takeover-of-internal-tesla-accounts-bc720603e67d"
authors: ["Evan Connelly (@Evan_Connelly)"]
programs: ["Tesla"]
bugs: ["Account takeover", "SSO"]
publication_date: "2023-04-04"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1301
scraped_via: "browseros"
---

# Post Account Takeover? Account Takeover of Internal Tesla Accounts

Post Account Takeover? Account Takeover of Internal Tesla Accounts
Evan Connelly
Follow
4 min read
·
Apr 5, 2023

141

1

In testing various Tesla web applications as part of the Tesla Bug Bounty Program, I’ve created many Tesla user accounts. At some point, while creating a new account, I became curious if I could register an account using a Tesla email address.

For background, Tesla has many web apps. When it comes to SSO for all of these apps, Tesla has two main Identity Providers (IDPs), auth.tesla.com for external users and sso.telsa.com for employees. My testing involved the public auth.tesla.com.

auth.tesla.com (Tesla’s External IDP)

I discovered the external auth.tesla.com allowed users to register new accounts using @tesla.com and @teslamotors.com email addresses. Furthermore, there was no email validation, which meant it was possible to create an account with an email address that I did not have access to.

Now, initially this was not all that exciting. Through further testing any attempts to register an external account with a valid internal Tesla email address reported that the email address is taken. So at best, my thought was this could possibly be leveraged for a pre-account takeover with the right conditions, which is a fairly low impact issue.

So, how can we increase the impact of this or leverage it in another way?

Well, what about essentially the opposite of a pre-account takeover? Instead of creating an account with an email address I hope will be used in the future, what if I was able to register an account that was used in the past, is no longer active on Tesla’s internal IDP, but may still have privileges assigned within various web apps? Post-account takeover, if you will.

Due to a previous bug I found, I was fairly familiar with the Tesla Retail Tool (TRT). TRT stores confidential IT and business information such as network circuit info, local device logins, web logins for ISP and utility accounts, financial information, and details about current, upcoming, and previous Tesla locations such as lease terms, internal and external contact info, building plans and internal photos of restricted areas of Tesla properties.

Press enter or click to view image in full size
Tesla Retail Tool (TRT)

I knew that TRT allowed both access from internal and external accounts. That for authentication, it used a JWT which specifies an email address that was authenticated against a list of users manually defined within the application. At Tesla’s scale, it would be hard to manually update that list every time an employee leaves. And in theory, it should be okay if past employees have access defined within a web app, as their IDP account would be disabled or deleted and thus unable to login to the app through Tesla’s internal IDP.

But, what if it was possible to register external accounts with the internal email address of a former Tesla employee that would have had access to TRT and gain access to the web app with privileges still assigned to the now defunct email address? Would this give me a valid JWT with the victim email address that would be treated the same as if I logged in via the internal IDP?

I used Google Dorks to search LinkedIn profiles of former Tesla employees who served in roles that should have had access to TRT, especially with access to sensitive information.

Get Evan Connelly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For example,

site:linkedin.com inurl:/in “field systems” “tesla motors” -intitle:tesla -inurl:posts

This found former field IT staff that should have access to network information.

Moment of truth…In testing, it was possible to register an account at auth.tesla.com (External IDP) with a past Tesla employee’s email which still had privileges assigned in TRT.

I was able to then access the Tesla Retail Tool with the identity and privileges of a former employee whose internal IDP account had likely been purged, by creating an account with the same email on the public IDP. This worked on multiple attempts with several email addresses of former employees.

Press enter or click to view image in full size
TRT — Logged in

TL;DR Tesla has two Identity Providers (IDPs), auth.tesla.com for external users and sso.telsa.com for employees. Tesla Retail Tool (TRT) allows logins from both and was not checking what IDP the user logged-in with (auth.tesla.com vs sso.tesla.com). This made for a condition where via Google Dorks, I was able to identify names and extrapolate email addresses of former Tesla staff and then register accounts with the external IDP using the email addresses of former employees whose accounts had been disabled on the internal IDP but who still had privileges defined by their internal Tesla email address within TRT and ultimately log into TRT with the privileges of those users.

Timeline

19 Nov 2022 — Reported

20 Nov 2022 — Tesla validated the bug and began the remediation process

21 Nov 2022 — I informed Tesla that I could confirm the accounts I created in my report could no longer access TRT

29 Nov 2022 — Tesla marked as resolved and awarded a bounty

Bugcrowd Disclosure Summary
Summary by Evan Connelly — Tesla has two Identity Providers (IDPs), auth.tesla.com for external users and sso.telsa.com…

bugcrowd.com

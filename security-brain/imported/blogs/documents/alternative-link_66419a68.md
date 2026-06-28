---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_alternative-link.md
original_filename: 2023-04-04_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- sso
- jwt
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- jwt
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 66419a68837601daf74790bc598f49966f6ca68868617ea2c375137a64bc4d70
text_sha256: 6b53fc60da1bbb55086de6cf52cd8d7c93903712c8021d2aa755eb0c040c71cd
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_alternative-link.md
- Source Type: markdown
- Detected Topics: sso, jwt, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `66419a68837601daf74790bc598f49966f6ca68868617ea2c375137a64bc4d70`
- Text SHA256: `6b53fc60da1bbb55086de6cf52cd8d7c93903712c8021d2aa755eb0c040c71cd`


## Content

---
title: "Alternative link"
page_title: "Post Account Takeover? Account Takeover of Internal Tesla Accounts | Evan Connelly"
url: "https://evanconnelly.github.io/post/tesla-account-takeover/"
final_url: "https://evanconnelly.github.io/post/tesla-account-takeover/"
authors: ["Evan Connelly (@Evan_Connelly)"]
programs: ["Tesla"]
bugs: ["Account takeover", "SSO"]
publication_date: "2023-04-04"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1301
---

# Post Account Takeover? Account Takeover of Internal Tesla Accounts

April 4, 2023

In testing various Tesla web applications as part of the [Tesla Bug Bounty Program](https://bugcrowd.com/tesla), I’ve created many Tesla user accounts. At some point, while creating a new account, I became curious if I could register an account using a Tesla email address.

For background, Tesla has many web apps. When it comes to SSO for all of these apps, Tesla has two main Identity Providers (IdPs), auth.tesla.com for external users and sso.telsa.com for employees. My testing involved the public auth.tesla.com.

![auth.tesla.com](auth.tesla.webp)

I discovered the external auth.tesla.com allowed users to register new accounts using @tesla.com and @teslamotors.com email addresses. Furthermore, there was no email validation, which meant it was possible to create an account with an email address that I did not have access to.

Now, initially this was not all that exciting. Through further testing any attempts to register an external account with a valid internal Tesla email address reported that the email address is taken. So at best, my thought was this could possibly be leveraged for a pre-account takeover with the right conditions, which is a fairly low impact issue.

So, how can we increase the impact of this or leverage it in another way?

Well, what about essentially the opposite of a pre-account takeover? Instead of creating an account with an email address I hope will be used in the future, what if I was able to register an account that was used in the past, is no longer active on Tesla’s internal IdP, but may still have privileges assigned within various web apps? Post-account takeover, if you will.

Due to a previous bug I found, I was fairly familiar with the Tesla Retail Tool (TRT). TRT stores confidential IT and business information such as network circuit info, local device logins, web logins for ISP and utility accounts, financial information, and details about current, upcoming, and previous Tesla locations such as lease terms, internal and external contact info, building plans and internal photos of restricted areas of Tesla properties.

![TRT](TRT.webp)

I knew that TRT allowed both access from internal and external accounts. That for authentication, it used a JWT which specifies an email address that was authenticated against a list of users manually defined within the application. At Tesla’s scale, it would be hard to manually update that list every time an employee leaves. And in theory, it should be okay if past employees have access defined within a web app, as their IdP account would be disabled or deleted and thus unable to login to the app through Tesla’s internal IdP.

But, what if it was possible to register external accounts with the internal email address of a former Tesla employee that would have had access to TRT and gain access to the web app with privileges still assigned to the now defunct email address? Would this give me a valid JWT with the victim email address that would be treated the same as if I logged in via the internal IdP?

I used Google Dorks to search LinkedIn profiles of former Tesla employees who served in roles that should have had access to TRT, especially with access to sensitive information.

For example, `site:linkedin.com inurl:/in “field systems” “tesla motors” -intitle:tesla -inurl:posts`

This found former field IT staff that should have access to network information.

Moment of truth…In testing, it was possible to register an account at auth.tesla.com (External IdP) with a past Tesla employee’s email which still had privileges assigned in TRT.

I was able to then access the Tesla Retail Tool with the identity and privileges of a former employee whose internal IdP account had likely been purged, by creating an account with the same email on the public IdP. This worked on multiple attempts with several email addresses of former employees.

![TRT — Logged in](trt-logged-in.webp)

TL;DR Tesla has two Identity Providers (IdPs), auth.tesla.com for external users and sso.telsa.com for employees. Tesla Retail Tool (TRT) allows logins from both and was not checking what IdP the user logged-in with (auth.tesla.com vs sso.tesla.com). This made for a condition where via Google Dorks, I was able to identify names and extrapolate email addresses of former Tesla staff and then register accounts with the external IdP using the email addresses of former employees whose accounts had been disabled on the internal IdP but who still had privileges defined by their internal Tesla email address within TRT and ultimately log into TRT with the privileges of those users.

## Timeline#

19 Nov 2022 — Reported

20 Nov 2022 — Tesla validated the bug and began the remediation process

21 Nov 2022 — I informed Tesla that I could confirm the accounts I created in my report could no longer access TRT

29 Nov 2022 — Tesla marked as resolved and awarded a bounty

[Bugcrowd Disclosure Summary](https://bugcrowd.com/disclosures/4d9d22af-3a9f-45ce-8eef-8d4fba06a205/auth-tesla-com-account-takeover-of-internal-tesla-accounts)

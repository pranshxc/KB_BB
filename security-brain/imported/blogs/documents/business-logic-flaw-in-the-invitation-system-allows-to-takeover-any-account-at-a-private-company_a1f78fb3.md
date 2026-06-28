---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-15_business-logic-flaw-in-the-invitation-system-allows-to-takeover-any-account-at-a.md
original_filename: 2020-06-15_business-logic-flaw-in-the-invitation-system-allows-to-takeover-any-account-at-a.md
title: Business logic flaw in the invitation system allows to Takeover any account
  at a private company
category: documents
detected_topics:
- business-logic
- idor
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- business-logic
- idor
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: a1f78fb3b8f3ede0bdd82fa030e47bf21f24903fbd0f2a061fe8d796944833c8
text_sha256: 2691094fc888d998191a797f570644c3791c7768d04f400d351126760da06f05
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Business logic flaw in the invitation system allows to Takeover any account at a private company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-15_business-logic-flaw-in-the-invitation-system-allows-to-takeover-any-account-at-a.md
- Source Type: markdown
- Detected Topics: business-logic, idor, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a1f78fb3b8f3ede0bdd82fa030e47bf21f24903fbd0f2a061fe8d796944833c8`
- Text SHA256: `2691094fc888d998191a797f570644c3791c7768d04f400d351126760da06f05`


## Content

---
title: "Business logic flaw in the invitation system allows to Takeover any account at a private company"
url: "https://medium.com/bugbountywriteup/business-logic-flaw-in-invitation-system-allows-to-takeover-any-account-at-private-company-daaf898966b0"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["Account takeover", "IDOR"]
publication_date: "2020-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4496
scraped_via: "browseros"
---

# Business logic flaw in the invitation system allows to Takeover any account at a private company

Business logic flaw in the invitation system allows to Takeover any account at a private company
Daniel "V" Morais
Follow
3 min read
·
Jun 16, 2020

256

1

Hello Friends,

In this post, I’ll explain how I could exploit a business logic flaws under the invitation system from a private company to take over any account in their services without user’s consent.

First things first:

I have a team named “Vendetta” and there was a new target that launched a public bug bounty program that we found trough google dork, so we decided to take the first “critical” look

Normally I start to use the application as a normal user while I capture and read ALL requests using a traffic interceptor tool (e.g. Burp Suite).

The application allowed us to invite new users to the organization account under “Users” section

Press enter or click to view image in full size

The invited user will then receive an email in their mail box with a token as below

https://app.redacted.com/reset-multi-user-password/INVITE-TOKEN-HERE

If you are a Bug hunter then the above endpoint should get your attention as it drew mine, especially in reset-multi-user-password

As I explained, the function was created to add a user to the company’s account, why are they calling this “reset password” endpoint?

With this question in mind, I decided to go deeper, when accepting the invitation , the application sent a POST request to the endpoint/activate-invited-user along with the invited email in the request body.

Press enter or click to view image in full size

The problem lies here, where the invited user has control over the email and password in the request body, I thought:

“The invited user receives the invite token by thereset-multi-user-password endpoint, the user controls the invited email and new password, what If I change the invited email to owner@victim.com and forward the request along with a new password?”

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, I captured the “accept invite” request and change the email to “owner@victim.com” along with a new password as follows

Press enter or click to view image in full size

And the server accepted my request, next I logged in as “owner@victim.com” with the new password to confirm the takeover.

Finally, I sent an email describing the vulnerability and the impact with below Proof of Concept to the security team:

Login to your account at https://app.redacted.com
Now invite any email that you also control under “Users” section
Click in the invite link and you’ll see a page where it will ask for you to create a new password for the account, intercept the request
Just change the email to any other user account at your application and forward the request
You have now set a new password for the “victim” email using an invitation token

The security team quickly triaged and resolved this vulnerability.

Takeaways:

Always observe all the endpoint names, if you see something different than the usual, try to go deeper, you may find some interesting behaviours with them.

Thanks for your time :)

Daniel_v

Vendetta White hat Team

Twitter | BugCrowd Profile | H1 Profile | Linkedin

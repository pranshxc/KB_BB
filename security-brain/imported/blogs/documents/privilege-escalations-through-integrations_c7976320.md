---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-04_privilege-escalations-through-integrations.md
original_filename: 2023-05-04_privilege-escalations-through-integrations.md
title: Privilege Escalations through Integrations
category: documents
detected_topics:
- sso
- jwt
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- jwt
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: c79763206d73b779aafb455cda5cfd2f7499e0f69a98792f558252ca8ca1f4c1
text_sha256: 3e306776609325ff09e1ddd6d870d248375701cd78d73070c23897a58d19525a
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalations through Integrations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-04_privilege-escalations-through-integrations.md
- Source Type: markdown
- Detected Topics: sso, jwt, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c79763206d73b779aafb455cda5cfd2f7499e0f69a98792f558252ca8ca1f4c1`
- Text SHA256: `3e306776609325ff09e1ddd6d870d248375701cd78d73070c23897a58d19525a`


## Content

---
title: "Privilege Escalations through Integrations"
url: "https://blog.stratumsecurity.com/2023/05/04/integration-fails/"
final_url: "https://blog.stratumsecurity.com/2023/05/04/integration-fails/"
authors: ["Colin McQueen"]
bugs: ["Privilege escalation", "Amazon cognito misconfiguration", "JWT", "Account takeover"]
publication_date: "2023-05-04"
added_date: "2023-05-06"
source: "pentester.land/writeups.json"
original_index: 1189
---

# Privilege Escalations through Integrations

  * [ ](/author/colin/)

#### [Colin McQueen](/author/colin/)

04 May 2023 • 5 min read

Share

This assessment was interesting as multiple issues while integrating Okta, Amazon Cognito, and Tableau led to privilege escalations. Both unauthenticated and authenticated users can escalate their privileges to become administrative users.

## Application Background

The purpose of this application is to allow financial institutions to create dashboards using their financial data for analytical purposes.

This application is a wrapper of Tableau with some custom code to integrate Amazon Cognito and Okta for authentication, Tableau for the dashboard functionality, and a custom web page to list the accessible dashboards for the user and share dashboards with other users.

## Amazon Cognito Misconfigurations

Amazon Cognito has an option that allows users to self-register, confirm their account, and then log in to retrieve their tokens (access, ID, and refresh).

This application didn't have a registration option as the intended purpose is to have administrators provision accounts.

To abuse this misconfiguration as an unauthenticated user, the Cognito client ID has to be retrieved from the /static/js/main.js file.

The self-registration in Cognito for the application client was enabled, allowing users to create accounts and log into the application bypassing the Okta integration.

Correct profile and role values are necessary for successful access to the application.

The public dev environment mentioned later can be used by unauthenticated users to disclose these values. The formatting for these values is easy to enumerate as an authenticated user. The Cognito registration can be used to enumerate emails.

Below are the steps used to create the account, log in, and update the user attributes to forge JWTs as another user. 

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-1.png)Figure 1 - Confirmation Cognito Self-Registration is enabled for application client![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-3.png)Figure 2 - Confirmed the account using the code sent in the email![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-4.png)Figure 3 - Logged into application using Cognito bypassing the Okta integration![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-5.png)Figure 4 - Set user attributes to another user's email, role, and profile![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-6.png)Figure 5 - Logged in using another user's email and attacker's password![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/signup-account-takeover-9.png)Figure 6 - Confirmation registered account can access application

## Tableau Trusted Auth Privilege Escalation

The application uses Tableau's trusted authentication to integrate Tableau. The custom code in the Amazon API gateway only checked if a valid JWT was present but didn't confirm the identity. The email address in the URL was used to confirm the identity and retrieve a valid Tableau ticket.

Unauthenticated users can register accounts with Cognito and then use another user's email address (a Tableau server admin user) from Figure 6 to retrieve a valid Tableau ticket leading to privilege escalation in Tableau.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/priv-escalation-3.png)Figure 7 - Retrieved another user's Tableau ticket![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/priv-escalation-4.png)Figure 8 - Exchanged Tableau ticket for Tableau session![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/priv-escalation-5.png)Figure 9 - Confirmation escalated Tableau privileges to Site Administrator Explorer![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/priv-escalation-7.png)Figure 10 - List all site users to find Tableau Server Admin to escalate privileges again

## Privilege Escalation to Server Admin in Tableau Development Environment

In the /static/js/main.js file, the Cognito client IDs and Tableau URLs for every environment (dev, QA, UAT, and production) was available. The dev environment didn't require a JWT to retrieve a Tableau ticket. An unauthenticated user can provide the default Tableau admin username to retrieve the ticket and become a Tableau server admin. The dev environment was also publicly accessible.

As mentioned in the Cognito misconfiguration, an attacker could retrieve profile and role values to escalate their privileges in other environments.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/dev-env-access-1.png)Figure 11 - Dev environment details in JS file![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/dev-env-access-2.png)Figure 12 - Retrieved default Tableau admin Tableau ticket![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/dev-env-access-3.png)Figure 13 - Exchanged ticket for Tableau session![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/dev-env-access-4.png)Figure 14 - Confirmation an unauthenticated user can become a Tableau server admin

## Privilege Escalation to Server Admin in Tableau using Okta

As Okta was being used, I decided to see if it was possible to access the Okta console by visiting [https://idp-redacted.com/login/default](https://idp-redacted.com/login/default?ref=blog.stratumsecurity.com). The goal was to see if I could find any misconfigurations with the Okta integration. Not only was I able to access the console, but I discovered custom fields with Okta.

Using the Okta APIs, a custom field called tableauusername was found. I used the API to update my user's tableauusername to admin to see if I could become the default Tableau admin user. I logged out of Okta, logged into the application, and had access to every Tableau dashboard in the system.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/okta-tableau-priv-escal-1.png)Figure 15 - Access to Okta console![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/okta-tableau-priv-escal-2.png)Figure 16 - Found custom fields under profile in the Okta API![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/okta-tableau-priv-escal-3.png)Figure 17 - Updated the custom tableauusername to admin![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/03/okta-tableau-priv-escal-4.png)Figure 18 - Got Tableau server admin viewing all dashboards

## Remediation

For Amazon Cognito, the two recommendations were to disable the self-registration and update user attributes to prevent authenticated users from forging JWTs as another user.

With the custom code in the Amazon API gateway, the JWT should be used instead of the email query parameter to confirm the user's identity for the Tableau trusted authentication. This remediation relies on Cognito's update user attributes call being disabled to prevent JWT forging.

The recommendations for the development environment were to disable public access at the network layer, remove the environment details in the JavaScript file that don't need to be in the file, and use a JWT similar to other environments for the Tableau trusted authentication.

With the Okta integration, the Okta console doesn't need to be accessible. Validation should be in place to not allow users to update some custom fields.

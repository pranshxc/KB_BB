---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-03_account-takeover-inside-the-tenant.md
original_filename: 2022-12-03_account-takeover-inside-the-tenant.md
title: Account Takeover - Inside The Tenant
category: documents
detected_topics:
- otp
- command-injection
- password-reset
- mfa
- information-disclosure
- api-security
tags:
- imported
- documents
- otp
- command-injection
- password-reset
- mfa
- information-disclosure
- api-security
language: en
raw_sha256: e3bb957a295f15846eb9e2fc0325513a80a7af2d96adaf03c812088338ee65d3
text_sha256: b61859c59f2d122437c98bbf34df44587b214d056ff7c58c4a2def385c383a5c
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover - Inside The Tenant

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-03_account-takeover-inside-the-tenant.md
- Source Type: markdown
- Detected Topics: otp, command-injection, password-reset, mfa, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `e3bb957a295f15846eb9e2fc0325513a80a7af2d96adaf03c812088338ee65d3`
- Text SHA256: `b61859c59f2d122437c98bbf34df44587b214d056ff7c58c4a2def385c383a5c`


## Content

---
title: "Account Takeover - Inside The Tenant"
url: "https://shahjerry33.medium.com/account-takeover-inside-the-tenant-6101a3cafbee"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Account takeover", "Information disclosure"]
bounty: "150"
publication_date: "2022-12-03"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1820
scraped_via: "browseros"
---

# Account Takeover - Inside The Tenant

Account Takeover - Inside The Tenant
Jerry Shah (Jerry)
Follow
4 min read
·
Dec 3, 2022

326

3

Press enter or click to view image in full size

Summary :

Account Takeover (ATO) is an attack using which an attacker cat take ownership of another person’s account. There are multiple ways for an account takeover attack, namely brute forcing credentials, credentials stuffing, response manipulation, password reset poisoning, social engineering and phishing, 2FA bypass attacks etc.

Description :

I have found a vulnerability on a private program on one of the bug bounty platform for which I was awarded 150 USD. While browsing the application I found an invite functionality which was vulnerable to invitation token leakage. I took the advantage of the leaked invitation token to takeover the victim’s account via an unregistered email that was handled by me (attacker).

What is Tenant ?

In simple words a tenant is defined as a group of users from a single organization or company. There is an admin in the tenant who can invite other users to work for the company by which the tenant has been created. A tenant can be of IT department, Accounts department, Sales department etc.

Press enter or click to view image in full size
Tenant - Basic

How I found this vulnerability ?

I logged into the account (admin credentials were provided by the platform) and clicked on the Invite user functionality
Press enter or click to view image in full size
Admin Account

2. I entered victim’s email and clicked on Invite button

Press enter or click to view image in full size
Invitation Functionality

3. Then I intercepted the request using burpsuite and did right click on the request > Do intercept > Response to this request

Press enter or click to view image in full size
Burpsuite - Request
Press enter or click to view image in full size
Burpsuite - Response
Press enter or click to view image in full size
Pending Invitation

4. I crafted the URL for the invitation token and opened it in the browser because the token was already leaked in the response, then I clicked on Accept and it asked me to enter an email

Press enter or click to view image in full size
Invitation Token URL (Victim)
Press enter or click to view image in full size
Asking for Invited Email (Victim’s Email)

5. Then I went to Temp Mail and copied the unregistered email and pasted it on the website and clicked on the button and then I clicked on Approve

Press enter or click to view image in full size
Temp Mail
Press enter or click to view image in full size
Entered the unregistered email (Attacker’s email)
Press enter or click to view image in full size
Approve

6. Then the code was sent to an unregistered email (attacker’s email)

Press enter or click to view image in full size
Verification Code Sent
Press enter or click to view image in full size
Verification Code

7. I used the code and I accepted the invitation sent to the victim

Press enter or click to view image in full size
Verification Code
Press enter or click to view image in full size
Account Takeover
Press enter or click to view image in full size
Invitation Accepted

Why it happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion,

Two flaws were there in the web application

The invitation token was leaked in the response while inviting the user
The validation of the invited user on invitation token was not done

Impact

Any admin can takeover the account of any user who is invited by the admin to the tenant.

The severity would be low to medium because the attack is within the tenant and apart from it the only thing an admin can do here is impersonating the invited user and perform the actions behalf of that user and an admin is not able to impersonate the existing user.

Calculated CVSS

Vector String - CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N

Score - 5.4 (Medium)

Press enter or click to view image in full size
Attack Flow

Mitigation

There will be two mitigations here

The invitation code should not be sent in the response from the server
A checked should be performed against the invite code and invited email address

Secure Code

// Check if the provided email matches the invite code
if (email == inviteCode) {
// Email matches the invite code
// Proceed with the rest of the authentication process
// …
} else {
// Email does not match the invite code
// Return an error message or ask for the correct invite code
// …
}

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-18_misconfiguration-in-change-password-functionality-leads-to-account-takeover.md
original_filename: 2021-04-18_misconfiguration-in-change-password-functionality-leads-to-account-takeover.md
title: Misconfiguration in Change-password Functionality Leads to Account Takeover
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- automation-abuse
- business-logic
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- automation-abuse
- business-logic
language: en
raw_sha256: 15e8bbaaf63919136fe7bc284d6a596ec6035a83c814d0b51b7d0628dbe98b6b
text_sha256: a0a1165e512873a239c8480727881009c6fd137a59a817fc117b3edd48151bcc
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Misconfiguration in Change-password Functionality Leads to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-18_misconfiguration-in-change-password-functionality-leads-to-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `15e8bbaaf63919136fe7bc284d6a596ec6035a83c814d0b51b7d0628dbe98b6b`
- Text SHA256: `a0a1165e512873a239c8480727881009c6fd137a59a817fc117b3edd48151bcc`


## Content

---
title: "Misconfiguration in Change-password Functionality Leads to Account Takeover"
url: "https://0x2m.medium.com/misconfiguration-in-change-password-functionality-leads-to-account-takeover-1314b5507abf"
authors: ["Mahmoud Radwan (@0x___2m)", "Mahmoud samaha (@0x__2m)"]
bugs: ["IDOR", "Logic flaw", "Password reset", "Account takeover"]
publication_date: "2021-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3731
scraped_via: "browseros"
---

# Misconfiguration in Change-password Functionality Leads to Account Takeover

Misconfiguration in Change-password Functionality Leads to Account Takeover
Mahmoud Mohamed
Follow
3 min read
·
Apr 18, 2021

569

2

Misconfiguration in Change-password Functionality Leads to Account Takeover

Hello everyone,

We are Mahmoud Radwan and Mahmoud Samaha (0x2m) and this is our first Write-Up ever.

This Write-Up describes How we could Takeover any account on a site using some misconfigurations in Change-Password Functionality.

We were testing a private program so let’s call it site.com, so let’s start our Journey.

While going throw the sandbox environment that is for testing porous (sandbox.site.com) we notice a change password function.

So we opened the Burb-Suite and intercept the request looking for any issue and we catch this request and start analyzing it

So as you can see we found this Header (X_auth_credentials) that have the same value of the parameter (current Password) in the request body which insure that,

If you want to change your current password you must first enter your current password then enter the new password.

So we start to ask some questions,

What about this header?
Does the Server validate it ?
What will happen if we remove it ?
What if we change our email with anyone email does it change their password?

First we start to play with the request and remove both of [ The Header (X_auth_credentials) and the Parameter (‘ currentPassword ‘) ] and send the request to the server to see the response and we got a 200 OK response without any error so the server doesn’t validate on this Header 😈.

So Now we know that we don’t need [The Header (X_auth_credentials) and the Parameter (‘currentPassword ‘)] in our request.

Again we ask how we can use this issue, Can we takeover on any account?

We created another account (We call it victim@mail.com) and change our email with the victim email and use the same credentials of our account and send the request to the server.
And we were surprised to see that we got a 200 OK and the response tells that the change password function completed but for whom!
So we went to the login page and put the victim email and the credentials that we created for him (test@1234) and guess what we accessed the victim account successfully😎.

Attack Workflow:

Get Mahmoud Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Change the email to the victim email.

2. Remove [The Header (X_auth_credentials) and the Parameter (‘currentPassword ‘)].

3. Put any new password you want

4. Send the request and you got 200 OK as a response.

5. Login to the victim account with the new password and here we go you successfully accessed his account.

Impact

Full Account Takeover without any interaction from the victim.

Press enter or click to view image in full size

When I reported the vulnerability to the company, they reduced the risk from P1 to P2, because I would need to know the victim’s E-Mail

Steps To Reproduce in main report :
Login to attacker account AKA here (test1)
Email = attacker@mail.com
pass = attackerpass@1234
Login to victim account AKA here (test2)
Email = victim@mail.com
pass = victimpass@1234
Go to change password function in the attacker window.
Intercept the request and send the request to Repeter.
Remove (current password parameter and Xauthcredentials header) from the request.
Change the attacker email to the victim email in the request body.
Enter the new password you want AKA => (newpass@1234)
Now I will log out from the victim account and try to log in with the new password.
Now you get full account takeover of the victim .

Reported at April 7, 2021 12:22am
triage at Apr 8th
bounty Apr 15th $$$$

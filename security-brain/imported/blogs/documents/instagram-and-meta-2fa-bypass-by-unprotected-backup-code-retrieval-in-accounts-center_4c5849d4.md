---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-22_instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-c.md
original_filename: 2024-08-22_instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-c.md
title: Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts
  Center
category: documents
detected_topics:
- mfa
- command-injection
- graphql
tags:
- imported
- documents
- mfa
- command-injection
- graphql
language: en
raw_sha256: 4c5849d452d5c09eaf5df9c06d5b5d95ee1ac73f0ea78f2ae75e77a6459ecaae
text_sha256: f6edf1b143bce54f8a34a320e2e1824037ffcf8cb8f0092311a2fdbaab471261
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-22_instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-c.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, graphql
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `4c5849d452d5c09eaf5df9c06d5b5d95ee1ac73f0ea78f2ae75e77a6459ecaae`
- Text SHA256: `f6edf1b143bce54f8a34a320e2e1824037ffcf8cb8f0092311a2fdbaab471261`


## Content

---
title: "Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center"
page_title: "Instagram and Meta 2FA Vulnerability: Unprotected Backup Code Retrieval Exploit in Accounts Center | $10,000 Bounty Awarded | by Shuva Saha | Medium"
url: "https://medium.com/@scriptshuva/instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-center-c735ff650f10"
authors: ["Shuva Saha (@scriptshuva)"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass", "Account takeover"]
bounty: "10,000"
publication_date: "2024-08-22"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 51
scraped_via: "browseros"
---

# Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center

Shuva Saha
Follow
3 min read
·
Aug 22, 2024

359

7

Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center

Hello, I'm Shuva Saha (scriptshuva). Today, I will be discussing a vulnerability I discovered: bypass of two-factor authentication (2FA) mechanisms in Meta and Instagram.

Bounty: $10,000 Awarded for bypassing two-factor authentication (2FA) mechanisms in Meta and Instagram

Meta 2FA Bypass

A hacker who gains access to a victim Facebook or Instagram account can retrieve Meta 2FA backup codes from account center, bypassing Meta two-factor authentication (2FA) and gaining full access to victim Meta account.

Step 1: Login Initiation
Go to Meta Auth.
Log in using compromised Facebook or Instagram accounts.
Step 2: 2FA Handling
If 2FA is enabled on Meta account, select recovery code option when prompted for 2FA.
Step 3: Exploitation Process
Open a new tab in the browser and go to Facebook Accounts Center Two-factor authentication Settings.

2. Click Additional methods and then Click Recovery codes

3. Use a proxy tool, such as Burp Suite, to intercept FXAccountsCenterTwoFactorRecoveryCodesDialogQuery graphql request.

Step 4: Request Modification
Modify the intercepted request by changing the variables and doc_id as shown below:
variables={"account_id":"victim_meta_account_id","account_type":"FRL","interface":"FB_WEB"}&doc_id=6358505927544740

Note: Flaw here is missing meta account password protection.

S
tep 5: Recovery Code Retrieval
Send modified request.
Extract recovery code from response.
Step 6: Account Takeover
Use retrieved 2FA backup code to log in to the victim meta account, effectively bypassing 2FA.
Press enter or click to view image in full size
Instagram 2FA Protection Bypass

A hacker who gains access to a victim Facebook account can retrieve Instagram 2FA backup codes from account center, bypassing Instagram two-factor authentication (2FA) and gaining full access to victim Instagram account.

Step 1: Login Initiation
Go to Instagram.
Log in using compromised Facebook account.
Step 2: 2FA Handling
If 2FA is enabled on Instagram account, select recovery code option when prompted for 2FA.
Step 3: Exploitation Process
Open a new tab in the browser and go to Facebook Accounts Center Two-factor authentication Settings.

2. Click Additional methods and then Click Recovery codes

Get Shuva Saha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Use a proxy tool, such as Burp Suite, to intercept FXAccountsCenterTwoFactorRecoveryCodesDialogQuery graphql request.

Step 4: Request Modification
Modify intercepted request by changing variables and doc_id as shown below:
variables={"account_id":"victim_instagram_account_id","account_type":"INSTAGRAM","interface":"FB_WEB"}&doc_id=6358505927544740

Note: Flaw here is missing Instagram account password protection.

Step 5: Recovery Code Retrieval
Send modified request.
Extract recovery code from response.
Step 6: Account Takeover
Use retrieved 2FA backup code to log in to victim Instagram account, effectively bypassing 2FA.
Outcome

By following these steps, attacker successfully logs into victim Instagram and Meta accounts by bypassing the two-factor authentication, exploiting missing password protection for accessing backup codes.

Technical Details

The vulnerability exists because Instagram and Meta backup code retrieval process in Facebook Accounts Center does not require the Instagram and Meta account password. This lack of password protection allows hacker with access to the victim Facebook account to obtain Instagram and Meta backup codes and bypass 2FA.

Remediation

Now, accessing Instagram and meta backup codes for requires verifying login to Instagram and meta accounts, ensuring that backup codes are protected by an additional layer of security.

Timeline:

Report Created : Monday, June 26, 2023

Bounty Awarded : July 8, 2023 ( $5000 for Meta 2FA bypass )

Bounty Awarded : July 27, 2023 ( $5000 for Instagram 2FA bypass )

Publicly Disclose Approved: August 21, 2024

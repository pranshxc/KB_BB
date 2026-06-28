---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-12_whitehat-test-accounts-can-act-as-hidden-admin-with-business-manager-ad-accounts.md
original_filename: 2019-10-12_whitehat-test-accounts-can-act-as-hidden-admin-with-business-manager-ad-accounts.md
title: Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts.
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
language: en
raw_sha256: 11f66db978dc7ae07fd2d99e3e57a07eecab3e406701e4a307b31bf6273f1817
text_sha256: 2cb42b98bbf8be253284665d457dada321ade0f18c8482b7a8d69a24c74cf285
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-12_whitehat-test-accounts-can-act-as-hidden-admin-with-business-manager-ad-accounts.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `11f66db978dc7ae07fd2d99e3e57a07eecab3e406701e4a307b31bf6273f1817`
- Text SHA256: `2cb42b98bbf8be253284665d457dada321ade0f18c8482b7a8d69a24c74cf285`


## Content

---
title: "Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts."
url: "https://medium.com/@rohitcoder/whitehat-test-accounts-can-act-as-hidden-admin-with-business-manager-ad-accounts-ce75ead5ffff"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4990
scraped_via: "browseros"
---

# Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts.

Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts.
Rohit kumar
Follow
4 min read
·
Oct 12, 2019

141

Again this will be a copy/paste of my whole report nothing fancy gifs and memes in this report 😐

Press enter or click to view image in full size

Title

Whitehat test accounts can act as Hidden Admin with Business manager / Ad Accounts.

Vuln Type

Privacy / Authorization

Product Area

Facebook — Web

Description/Impact

Description
===
Hi Facebook Team,

According to Facebook whitehat, test account is having some limitations like

1. Can interact with other test accounts, but not with real accounts
2. Are exempt from Facebook spam or fake account detection systems
3. Cannot like Facebook pages or post to a page’s Wall
4. Cannot be converted to a real user account

but, I noticed that a malicious admin can perform a lot of actions in a real business manager account and those all action will be not visible to other admins/managers which leads to different kind risk.

I was able to perform and test this vulnerability on different features like

1. Add hidden pages
2. Hidden Ad account managers
3. Hidden pages in partners business
4. Can add a hidden system user

A hidden business manager admin (Which is whitehat test account) can work on above all mentioned features and those all works will be completely hidden by other real admins.

I will reply this same thread if I will be able to perform any more task.

Impact
===
Malicious admins can add pages, give ad accounts access permission to other malicious persons, can add new partners business (with hidden pages inside those businesses) etc..

Repro steps

Setup
===
1 Whitehat test account
1 Real user account
1 Business account created by real user account

Steps
===
1. From real user account send an invite to email someone@email.com
2. Now, click on Resend email button and copy the signup link.
3. Now, from whitehat test account visit that link and join that business
4. Now, add any page from whitehat test account (which was created by you) that page is not visible to other admins.
5. Now, open ad account list and assign yourself in that an account. Other admins can’t see you are managing that ad account.
6. Add system user from a whitehat test account, other admins can’t see that system user.
7. Create another business with few pages linked from a whitehat test account.
8. Add that business to a real business account as a partner, other admins will be not able to see a list of linked pages in that business.

21 Jun

Hi Rohit,

Thank you for your submission.

We’ve managed to reproduce your report and will get back to you once we have had a chance to investigate.

Thanks,

Logan
Security

Your Reply

14 Jul

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hi Logan,

Any updates on this report?

Thanks,
Rohit Kumar

Your Reply

25 Aug

Hi Logan!

Can I get any update on this report, please?

30 Aug

Hi Rohit,

Sorry for the delay. Thank you for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Regards,

Joel
Security

2 Oct

Hi Rohit,

We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.

Thanks,

Joel
Security

Your Reply

3 Oct

Hi Joel,

Yes, I believe this vulnerability has been patched!

Thanks,
Rohit Kumar

Yesterday

After reviewing this issue, we have decided to award you a bounty of $XXX. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.

Whitehat test accounts can be invited to a regular Business Manager.

Thank you again for your report. We look forward to receiving more reports from you in the future!

Having any questions? Let me know at my twitter handle @rohitcoder

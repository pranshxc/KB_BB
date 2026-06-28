---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-02_misconfiguration-lead-to-company-identity-theft-via-bypass-email-verification.md
original_filename: 2024-02-02_misconfiguration-lead-to-company-identity-theft-via-bypass-email-verification.md
title: Misconfiguration lead to company identity theft via bypass email verification.
category: documents
detected_topics:
- xss
- command-injection
- password-reset
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- password-reset
- cloud-security
language: en
raw_sha256: 1828458ae65c0254008d3784612eed9c22ac5324d0bb731be9d1ed0535350611
text_sha256: 858fb90483f0b29a188cfa637f8294dd8d65e3f3b866f7735fbf56acf916aee9
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Misconfiguration lead to company identity theft via bypass email verification.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-02_misconfiguration-lead-to-company-identity-theft-via-bypass-email-verification.md
- Source Type: markdown
- Detected Topics: xss, command-injection, password-reset, cloud-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `1828458ae65c0254008d3784612eed9c22ac5324d0bb731be9d1ed0535350611`
- Text SHA256: `858fb90483f0b29a188cfa637f8294dd8d65e3f3b866f7735fbf56acf916aee9`


## Content

---
title: "Misconfiguration lead to company identity theft via bypass email verification."
url: "https://hamzadzworm.medium.com/misconfiguration-lead-to-company-identity-theft-via-bypass-email-verification-0dd60b61d943"
authors: ["Abdelkader Mouaz (@hamzadzworm)"]
bugs: ["Email verification bypass", "HTML injection"]
publication_date: "2024-02-02"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 460
scraped_via: "browseros"
---

# Misconfiguration lead to company identity theft via bypass email verification.

Top highlight

Misconfiguration lead to company identity theft via bypass email verification.
Hamzadzworm
Follow
4 min read
·
Feb 2, 2024

549

11

Hi all, this is hamzadzworm and today i want to share with you a logic issue that allowed me to bypass email verification then lead to identity theft

I got an invite from private company so i start checking it as a normal user

i updated my name to an htmli payload

after some time i found that iam able to create a support case

Press enter or click to view image in full size

after creating new one i got an email that came from (support@company.com) but htmli in name didnt worked

Press enter or click to view image in full size

because email is received from official company support email i was thinking that i have to get an htmli here to make identity theft

i found the possibility to add new comment on the created case and was directly thinking that i must receive an update in email about my case

and this is what happened after i added new comment

Press enter or click to view image in full size

so as you saw htmli didnt worked when i created new case but it worked after i added a comment to get update about the case, so never stop while testing and keep digging :)

now email is received from company support email and htmli is working on it

Get Hamzadzworm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

did we finished?, not yet this is self htmli untile now and what left is to exploit it against other users

first step you i thinked about is change my email to other user email then make comment on support case and the new victim email will receive the update mail that contain htmli

but when i put other user email page got refreshed and aske me to verify email to make any action like access support case

Press enter or click to view image in full size

i keep thinking for a while to get a logic error so i opened a new account with my email, then verify email

now i can access support cases with my new account and bypass for that was to open two tabs one contain my profile where i will change email and second one contain the support case page there is possibility that support case page won’t get refreshed

Steps:

i will update my email on profile tab

Press enter or click to view image in full size

as you see the profile tab was refreshed and asked me to confirm email to access support cases but the other tab that was already opened didnt get refreshed or asked me to verify email

Press enter or click to view image in full size

so i will add comment on the already opened tab of support cases and update mail with htmli that sent from official support of company will go to the email that it pending verification

thats how i was able to bypass email verification and exploit company supper cases to sent emails with any subject and content i want to any email i want

Result:

Press enter or click to view image in full size

i hope you enjoyed it waiting for your reviews if you liked it i will share more logic issues with unique ways -.-

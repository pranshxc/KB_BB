---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-30_interesting-business-logic-error-leads-to-pre-account-takeover-via-verification-.md
original_filename: 2024-07-30_interesting-business-logic-error-leads-to-pre-account-takeover-via-verification-.md
title: Interesting Business Logic Error leads to Pre-Account Takeover via Verification
  bypass on GoogleVRP
category: documents
detected_topics:
- business-logic
- oauth
- idor
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- business-logic
- oauth
- idor
- command-injection
- otp
- rate-limit
language: en
raw_sha256: abfb80e1fbd36b0912089df6b0c36c2596eb61ec1e2e47261a37a197e96cb5e5
text_sha256: c5d6c671f3c546c01a3936f90a5c6f1649b764375f0afaa753dcb27afdc6f47a
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Interesting Business Logic Error leads to Pre-Account Takeover via Verification bypass on GoogleVRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-30_interesting-business-logic-error-leads-to-pre-account-takeover-via-verification-.md
- Source Type: markdown
- Detected Topics: business-logic, oauth, idor, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `abfb80e1fbd36b0912089df6b0c36c2596eb61ec1e2e47261a37a197e96cb5e5`
- Text SHA256: `c5d6c671f3c546c01a3936f90a5c6f1649b764375f0afaa753dcb27afdc6f47a`


## Content

---
title: "Interesting Business Logic Error leads to Pre-Account Takeover via Verification bypass on GoogleVRP"
url: "https://medium.com/@jerryhackgather/interesting-business-logic-error-leads-to-pre-account-takeover-via-verification-bypass-on-googlevrp-d362f9469e3d"
authors: ["Jerry1319 (@Mdhsan19)"]
programs: ["Google"]
bugs: ["Account takeover", "Logic flaw"]
publication_date: "2024-07-30"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 120
scraped_via: "browseros"
---

# Interesting Business Logic Error leads to Pre-Account Takeover via Verification bypass on GoogleVRP

Interesting Business Logic Error leads to Pre-Account Takeover via Verification bypass on GoogleVRP
Jerry1319
Follow
4 min read
·
Jul 30, 2024

334

4

As-salamu alaykum everyone, It’s me Mohd Hasan Ansari aka Jerry1319 as you guys knows me well via mine handles ( Reality : Nobody cares 😒 ) .

As usually as you guys know that i mostly hunt on GoogleVRP , So it’s a month’s old report of mine which got resolved few weeks ago , therefore i am writing the article today.

On a Fine day as i was looking to subdomains of the targets i have enumerated of GoogleVRP i noticed a weird subdomain , let’s assume it as learn.jerry.com . It seems weird to me as the content length of the subdomain was huge .

NOTE : As i am manual hunter and mostly hunt on main domain or subdomains and don’t do much recon so just only subdomains enumeration and wayback data that’s all , So remember whenever i point recon so it means subs and wayback data.

I started analyzing the subdomain as a normal user create account logged in into the account , explore the features it provides and the services it sells.

After a proper analysis, I thought of let’s run nuclei with mine private templates to get some insights about targets until i am analyzing it manually , The scan detected a tech based open redirection of the domain but unfortunately googlevrp don’t accept Open redirection along with also there was no any available Oauth login used by the domain and it’s sub through which i can chain it to get Open redirect to ATO .

Press enter or click to view image in full size

That’s why I just ignored it and focused on all the manual analysis i did , After a while a feature used for verification of the ownership of the user via OTP took mine attention.

I played a while with it and noticed some weird behavior , So my Spidey senses alerted me that here must be a bug just dig deeper bro.

Press enter or click to view image in full size

I quickly created 2 more account’s for analyzing the handling of the OTP and it’s behavior via multiple unexpected chances made in the verification process .

Actual Exploitation and Deep Understanding of BUG

I created a account with email of User A and quickly a OTP is sent to the email for ownership verification of the email

Get Jerry1319’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I captured the OTP and performed the same steps with User B email and used the OTP of USER A in the verification process of USER B but unfortunately it failed and didn’t worked for me

But the processing it took via the server still made me think that it’s a vulnerable server , maybe i have to try more interesting scenerio.

Again

I opened to browser’s in both browser’s i created account with USER A email and in BROWSER 1 i backed the path where the server ask to input email for sending OTP FOR OWNSERSHIP verification .

Then when the server send the OTP to USER A email from BROWSER 1 i inputed email of USER B ( Victim ) and click on send OTP .

Now again I performed the same steps and changed the email again to USER A ( Attacker ) email and again got the OTP in BROWSER 3 (i.e: I stored the OTP to use it in next step against Victim email)

and once again I changed the email to USER B ( victim )

Now when i enter the otp of email change which we got , server got confused and allocate me the access of USER B account via bypassing the ownership verification .

Here is the FLOW chart for better understanding of the bug

Press enter or click to view image in full size

Conclusion

It was too much confusing so i thought maybe GoogleVRP triager will be unable to reproduce and close it n/a but within 3 days the issue got accepted and I was awarded with 3 digit bounty via the GoogleVRP panel .

Press enter or click to view image in full size

Thank you for reading the article , I hope you guy’s have enjoyed it .

Signing Out Mohd Hasan Ansari aka Jerry1319

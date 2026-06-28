---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-20_how-i-earned-500-from-google-flaw-in-authentication.md
original_filename: 2020-09-20_how-i-earned-500-from-google-flaw-in-authentication.md
title: How I earned $500 from Google - Flaw in Authentication
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: d4a01b0550cde3363d66d98825995052c3e1a40e609e467c164cee9dfc6ccaa3
text_sha256: e36c6ff43c394444edfb93b9728aaed9456e1b55182c431c57d31aa3318a78d8
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $500 from Google - Flaw in Authentication

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-20_how-i-earned-500-from-google-flaw-in-authentication.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `d4a01b0550cde3363d66d98825995052c3e1a40e609e467c164cee9dfc6ccaa3`
- Text SHA256: `e36c6ff43c394444edfb93b9728aaed9456e1b55182c431c57d31aa3318a78d8`


## Content

---
title: "How I earned $500 from Google - Flaw in Authentication"
url: "https://medium.com/bugbountywriteup/how-i-earned-500-from-google-flaw-in-authentication-a40018c05616"
authors: ["Hemant Patidar (@HemantSolo)"]
programs: ["Google"]
bugs: ["Broken authentication"]
bounty: "500"
publication_date: "2020-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4248
scraped_via: "browseros"
---

# How I earned $500 from Google - Flaw in Authentication

How I earned $500 from Google - Flaw in Authentication
Hemant Patidar
Follow
3 min read
·
Sep 20, 2020

505

1

Hello Everyone!

This is my first writeup.

Today I will share the write-up of my first accepted bug in Google, Which is in “Google Cloud Partner Advantage Portal” where I was able to modify personal details for victim account via Broken Authentication.

What does “broken authentication” mean?

If the login functionality of your application can be subverted or bypassed in some way, this is referred to as broken authentication. This is such a common issue that broken authentication is an entry in the Open Web Application Security Project (OWASP) top ten web application vulnerabilities list.

Let’s start...

Let's get straight to the bug. When I was trying to do signup using the User Registration Form I notice that when someone does the registration process, the system does not verify the registered email. Also when we do that the user will get a verification email to verify and if the victim clicks to verify then the new detail will be updated into the victim account.

Summary: Insufficient Security Configurability | Flaw in Authentication

Steps-To-Reproduce:
Go to the https://www.partneradvantage.goog/ and click on Register as a new partner portal user.
Now fill all the details. (i.e. Victim email, which is already registered and the rest of the detail which you want to update in the victim’s account.) and click to submit.

3. Now the victim will receive an email to verify and if he clicks to verify then the above-entered details will get change in the victim account.

4. Boom! You have changed the details in someone else account.

Attack scenario:

The system does not verify the registered email when entered by someone else. Consider the impact of the business if data can be modified and control of the account assumed, other than that the impact of this is that attacker can fill in the data first before the original account owner enters the system.

Get Hemant Patidar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

Jul 20, 2020 - Bug Reported to Google

Jul 21, 2020 - Status changes to Won’t Fix (Not Reproducible) | Explained how to reproduce the bug and Impact

Aug 3, 2020 - Accepted (reopened) ❤

Aug 10, 2020 - Bounty Awarded $500

Press enter or click to view image in full size

So, this was my first bounty from Google. I have reported other minor issues and got Hall Of Fame.

Press enter or click to view image in full size

Thanks for reading :)

Happy Hacking ;)

You can see many writeups coming up…

Hemant Patidar

LinkedIn: linkedin.com/in/HemantSolo

Website:- hemantsolo.in

Twitter:- twitter.com/HemantSolo

Instagram:- instagram.com/hemant_solo

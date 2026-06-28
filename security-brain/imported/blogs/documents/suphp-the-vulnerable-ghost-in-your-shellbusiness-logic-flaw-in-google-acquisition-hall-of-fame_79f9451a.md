---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-21_suphp-the-vulnerable-ghost-in-your-shellbusiness-logic-flaw-in-google-acquisitio.md
original_filename: 2020-09-21_suphp-the-vulnerable-ghost-in-your-shellbusiness-logic-flaw-in-google-acquisitio.md
title: suPHP - The vulnerable ghost in your shell🎯Business Logic Flaw in Google Acquisition!
  (Hall Of Fame)🎯
category: documents
detected_topics:
- business-logic
- cloud-security
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- business-logic
- cloud-security
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 79f9451a02b9108ca0b5dcae1aa2d513db6e7de197b20700e2c1b62553625532
text_sha256: 59910fd81c7aa70aa882fff8652d96c3f0a61d7e0c82b2dc1484337d4fc69a94
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# suPHP - The vulnerable ghost in your shell🎯Business Logic Flaw in Google Acquisition! (Hall Of Fame)🎯

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-21_suphp-the-vulnerable-ghost-in-your-shellbusiness-logic-flaw-in-google-acquisitio.md
- Source Type: markdown
- Detected Topics: business-logic, cloud-security, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `79f9451a02b9108ca0b5dcae1aa2d513db6e7de197b20700e2c1b62553625532`
- Text SHA256: `59910fd81c7aa70aa882fff8652d96c3f0a61d7e0c82b2dc1484337d4fc69a94`


## Content

---
title: "suPHP - The vulnerable ghost in your shell🎯Business Logic Flaw in Google Acquisition! (Hall Of Fame)🎯"
page_title: "🎯Business Logic Flaw in Google Acquisition! (Hall Of Fame)🎯 | by Ritesh Gohil | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/business-logic-flaw-in-google-acquisition-hall-of-fame-1a9af5d3ac04"
authors: ["Ritesh Gohil (@RiteshG37659480)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2020-09-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4245
scraped_via: "browseros"
---

# suPHP - The vulnerable ghost in your shell🎯Business Logic Flaw in Google Acquisition! (Hall Of Fame)🎯

🎯Business Logic Flaw in Google Acquisition! (Hall Of Fame)🎯
Ritesh Gohil
Follow
3 min read
·
Sep 21, 2020

315

Always Try Harder! Because It’s Google!

Hi,

I would like to thank all the Bug Hunters for their tedious effort in improving internet security and reaching out to read my little GOOGLE-Bug Hunting story and my experience on achieving GOOGLE-Hall Of Fame!

I had started my Bug Hunting journey about 3 months ago, for the first three months I practised Bug Hunting on numerous private platforms which enhanced my confidence and my interest in internet-based research for Bug Hunting. As Google is extremely secured platform, it took a few days to understand various Google Domains and Google Acquisition? I have reported total 3 vulnerabilities (P2>S2) in Google and all of them are accepted.

Press enter or click to view image in full size
Hall Of Fame!

You have to understand first, what type of domains are managed by Google and What is an Acquisition of Google!? 🙄 If you have found any other domain which is not listed in Wikipedia, then check that domain on (whois lookup) and remember that Registrant and Administrative contact should be Google LLC

Get Ritesh Gohil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Details of Reported Bug:

I had selected and reported two vulnerabilities on this domain without using any tools: https://edu.workbencheducation.com/.

File/Document is not deleted permanently after deletion documents are still accessible globally. (Does the deleted data get stored permanently on Workbencheducation?)
After understanding the fundamentals of the application, I realized that the uploaded files were stored in AWS S3 bucket. I was curious to know what happens after I have deleted my uploaded file. Certainly, I found that the deleted file was still publicly accessible.
Either you choose accessibility of an uploaded File to be Private or Public, it is still accessible by the public, so anyone can access that File from the internet.
Later I reported this Bug, and after an intense study on the same domain 🧐, I found another Bug. It was observed that the uploaded file was stored in AWS. There was a feature in that application for students to make assignment Public or Private. The logic was clear that if the assignment is set as private then it should not be publicly available. If it is still publicly accessible then it is insensible to provide the feature of making a file public and private in the application.

Steps to follow:
1. Create and login to the account https://edu.workbencheducation.com/.
2. Now, click on create button and select upload file and fill necessary information.
3. Upload any file/document and click on save button.
4. Copy the uploaded document link and open through any web browser and validate it by opening the same link in any incognito mode.
4. Now, Delete the uploaded file and browse again using the uploaded document link, you should be able to access or download the same file.
5. You can still download or access the same file anytime, through the same uploaded document link.

Attack Scenarios and Impacts:
Even if the user has uploaded their personal documents opting Private accessibility yet those files were publically accessible.
1. This directly concerns with the privacy of the user as it stores all the deleted data of the person which is supposed to be deleted permanently.
2. The user may misuse the functionality of the feature of making the uploaded file into Public or Private access, either way, it still remains as public access, this breaches the trust and integrity of the user.
3. The Postsecondary researchers might get adversely affected by this misuse of the functionality due to their tedious data being Plagerised, and Research may lose its Uniqueness.

Suggestion:
Try to be familiar with the targeted domain and understand all its functionalities. Keep exploring and understanding new technologies and never limit your knowledge. There is always something which we don’t know, think out of the box. #TryHarder 🎯 #NeverGiveUp 💪.

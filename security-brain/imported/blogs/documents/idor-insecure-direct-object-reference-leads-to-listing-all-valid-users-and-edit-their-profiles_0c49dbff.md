---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-12_idor-insecure-direct-object-reference-leads-to-listing-all-valid-users-and-edit-.md
original_filename: 2022-04-12_idor-insecure-direct-object-reference-leads-to-listing-all-valid-users-and-edit-.md
title: IDOR (Insecure Direct Object Reference) leads to listing all valid Users and
  edit their Profiles
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 0c49dbff934950850475773a16e193a40f5f2f061e87ff4c915b113ea68180a6
text_sha256: a8813f627112269fd90ca3c910754875a74e0946b553a63fe71db3abc00d2e51
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR (Insecure Direct Object Reference) leads to listing all valid Users and edit their Profiles

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-12_idor-insecure-direct-object-reference-leads-to-listing-all-valid-users-and-edit-.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `0c49dbff934950850475773a16e193a40f5f2f061e87ff4c915b113ea68180a6`
- Text SHA256: `a8813f627112269fd90ca3c910754875a74e0946b553a63fe71db3abc00d2e51`


## Content

---
title: "IDOR (Insecure Direct Object Reference) leads to listing all valid Users and edit their Profiles"
url: "https://medium.com/@Bishoo97x/idor-insecure-direct-object-reference-leads-to-listing-all-valid-users-and-edit-their-profiles-2d7bcba78890"
authors: ["Ahmed Hassan"]
programs: ["Drexel University"]
bugs: ["IDOR"]
publication_date: "2022-04-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2721
scraped_via: "browseros"
---

# IDOR (Insecure Direct Object Reference) leads to listing all valid Users and edit their Profiles

IDOR (Insecure Direct Object Reference) leads to listing all valid Users and edit their Profiles
Ahmed Hassan (Bishoo97x)
Follow
2 min read
·
Apr 12, 2022

30

Hello friends :)
I am happy to write a blog again after finding an Insecure Direct Object Reference Vulnerability in Drexel University Subdomain.

So lets begin i just catched a Website after searching through a lot of subdomains where i can create an account and register with an Email.

After creating my Account i recognized something in the URL Parameter. At the End of the URL you can see an ID Parameter which stands for User Identification. I started trying different ID Numbers to check if i can reach any Users Profile and view sensitive Informations like Email Address, Name etc.

Press enter or click to view image in full size

Here we go i was really able to fetch all the available Users by only changing the IDs in the URL and getting their Email Addresses, Name and also change their Informations.

Press enter or click to view image in full size

After that i just fired Burp Intruder to start enumerating every possible ID Number to automate the Process and at the End i was able to get all valid Users including Email Address, username and changing Functionality of User Informations.

Get Ahmed Hassan (Bishoo97x)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally i submitted this Vulnerability to the Drexel University CERT Team and they were able to validate the Vulnerability and send me an Acknoledgment Letter.

Press enter or click to view image in full size

At the End i hope you enjoyed my Writeup and learned something new and hope hearing from you soon :) stay safe and have a nice day :)

Press enter or click to view image in full size

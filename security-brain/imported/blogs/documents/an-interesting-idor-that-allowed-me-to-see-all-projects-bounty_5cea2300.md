---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-09_an-interesting-idor-that-allowed-me-to-see-all-projects-bounty.md
original_filename: 2022-07-09_an-interesting-idor-that-allowed-me-to-see-all-projects-bounty.md
title: An interesting idor that allowed me to See all projects ($$$$ Bounty)
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: 5cea2300f3fa0eca9b9f5e9619b2e44780b8143fbfc8d29ef6006c0fb9d47117
text_sha256: 612db290573d5f3dbf2f050268e809aef7d34561d1eda3a4d8f37631cf51240a
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# An interesting idor that allowed me to See all projects ($$$$ Bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-09_an-interesting-idor-that-allowed-me-to-see-all-projects-bounty.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `5cea2300f3fa0eca9b9f5e9619b2e44780b8143fbfc8d29ef6006c0fb9d47117`
- Text SHA256: `612db290573d5f3dbf2f050268e809aef7d34561d1eda3a4d8f37631cf51240a`


## Content

---
title: "An interesting idor that allowed me to See all projects ($$$$ Bounty)"
url: "https://hamzadzworm.medium.com/an-interesting-idor-that-allowed-me-to-see-all-projects-bounty-8cd74b5edf72"
authors: ["Abdelkader Mouaz (@hamzadzworm)"]
bugs: ["IDOR"]
publication_date: "2022-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2473
scraped_via: "browseros"
---

# An interesting idor that allowed me to See all projects ($$$$ Bounty)

Top highlight

An interesting idor that allowed me to See all projects ($$$$ Bounty)
Hamzadzworm
Follow
3 min read
·
Jul 10, 2022

446

5

Hi all today i will share an intresting i dor that i found in a one of hackerone private programs that allowed me to disclose all users private projects without there permission : )

intorduction:

it was a normal day as anyday and i get an invite from a private program so i said why dont i take a look on it so i grab a cup of coffee and enter the website and start testing it as a normal user

I made a project and make it private one then i decide to open project link in private browser and that was result

Press enter or click to view image in full size

I notice that it wasnt found but before that i notice that its uploaded on main website, so i keep thinking about what to do next and i decide to go deeper and check some subdomains.

Tio: just because main domain is secure that dosent mean subdomains are also secure : )

After checking few subdomains i notice one of them that contain same login page of the main website so i directly try to login with same credinals i used in the main websites and i was surprised that i was logged in so that mean another chance for idor :D

Get Hamzadzworm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I go to one of projects and that was result

Press enter or click to view image in full size

Still didnt opened so I opened it in a new page and here was the surprise:

Its uploaded in another subdomain like that: uploads.target.com/get_image/project/577213875_282x210.png

Press enter or click to view image in full size

Its clear now that i have to change project id and thats what i did and surprise was that it worked and it taked me to another user project but i wasnt clear if it disclose private projects, so i go to private browser and put my private project id that i created in first time when i opened in the main website and i was able to view it even without login.

I reported that and that was result:

Press enter or click to view image in full size

Accepted rewarded and resolved as critical but i didnt stop here i keep going more deeper and i was able to get another subdomain with another function that allowed me to do same thing and i could double my bounty

Press enter or click to view image in full size
Press enter or click to view image in full size

I hope this article was clear and hope it gonna help some of you follow me on twitter if you want more https://twitter.com/hamzadzworm

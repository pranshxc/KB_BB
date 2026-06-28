---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-13_idor-unpin-posts-for-fun.md
original_filename: 2023-06-13_idor-unpin-posts-for-fun.md
title: IDOR, unpin posts for fun.
category: blogs
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- blogs
- idor
- access-control
- command-injection
language: en
raw_sha256: 04f458e3f1d7221cc9990070587f72da996906f421fef9f1a0b93fa5e0fb5b74
text_sha256: 3b022a6884e4e7bb46882b20e31847dd3028751ee6e9ae4d0d0af5aeca9c12fe
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR, unpin posts for fun.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-13_idor-unpin-posts-for-fun.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `04f458e3f1d7221cc9990070587f72da996906f421fef9f1a0b93fa5e0fb5b74`
- Text SHA256: `3b022a6884e4e7bb46882b20e31847dd3028751ee6e9ae4d0d0af5aeca9c12fe`


## Content

---
title: "IDOR, unpin posts for fun."
url: "https://medium.com/@omarahmed_13016/idor-unpin-posts-for-fun-18f628eaef24"
authors: ["Omar Ahmed (@spaceboy2O)"]
programs: ["LinkedIn"]
bugs: ["IDOR"]
publication_date: "2023-06-13"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1052
scraped_via: "browseros"
---

# IDOR, unpin posts for fun.

IDOR, unpin posts for fun.
Omar Ahmed
Follow
2 min read
·
Jun 13, 2023

311

Hey guys,
I’m here to share my recent IDOR on LinkedIn bug bounty program on h1 which enabled me to unpin any pages/companies’ posts without any permissions.

Prerequisites

What is IDOR?
Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly.

So, I was hunting on LinkedIn for more than 3 weeks but most of the findings were actually closed as duplicates and info so I knew that easy peasy IDORs aren’t the way we needed to find something that simple browsing with AUTHORIZE plugin wouldn’t find ;)

I stumbled on a request that seemed to be odd as it gave me an odd response code

Press enter or click to view image in full size

So the request is simply taking company ID in the URL and an order to delete that pinned post, having this weird response code I decided to go deeper. So I started looking for what is that version tag parameter and how can I get it.

Get Omar Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I made another company page for the attacker and found out that the version tag exists on it, just a different sequence

Press enter or click to view image in full size
version tag for attacker company

and when I tried that version tag it actually gave me the same error code. So I thought like, this must be belonging to each page and there’s no way to get the version tag if we can’t access that URL above that gives us the version tag because .. wait, we can actually try that! And YES when I send a request to https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/ID-OF-Company?decorationId=com.linkedin.voyager.dash.deco.organization.AdminCompany-67

Press enter or click to view image in full size
version tag of victim company

it gives you the version tag that you would use in such case! and when I tried to unpin the post again, 200 was there saying: you say I obey :D

thus, I had the ability to unpin all company posts because company IDs are in a numerical order.

Bug was triaged shortly after reported and was considered LOW due to the limited business impact, they said, but It is a responsive team and I recommend you to go deep dive on this application if you want to sharpen your skills in finding IDORS!

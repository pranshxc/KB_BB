---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-02_idor-in-supportmozillaorg-through-code-review.md
original_filename: 2022-03-02_idor-in-supportmozillaorg-through-code-review.md
title: IDOR in support.mozilla.org through Code Review
category: documents
detected_topics:
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: 4e77a464a029a0239fc9e0578331483e84776fb3c7dcb09166fcce4e32bf2936
text_sha256: 5a7f760f360db6268f94beb2cf5bc7dd28a5f61206482e37a8a331a67b5322c9
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR in support.mozilla.org through Code Review

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-02_idor-in-supportmozillaorg-through-code-review.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `4e77a464a029a0239fc9e0578331483e84776fb3c7dcb09166fcce4e32bf2936`
- Text SHA256: `5a7f760f360db6268f94beb2cf5bc7dd28a5f61206482e37a8a331a67b5322c9`


## Content

---
title: "IDOR in support.mozilla.org through Code Review"
url: "https://noob3xploiter.medium.com/idor-in-support-mozilla-org-through-code-review-ff2aa8ea1201"
authors: ["Brandon Roldan"]
programs: ["Mozilla"]
bugs: ["IDOR"]
bounty: "1,500"
publication_date: "2022-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2856
scraped_via: "browseros"
---

# IDOR in support.mozilla.org through Code Review

IDOR in support.mozilla.org through Code Review
Brandon Roldan
Follow
2 min read
·
Mar 2, 2022

98

I was trying to improve my static analysis code, specifically django apps, so i decided to hack a random project in github. And i found kitsune. https://github.com/mozilla/kitsune

Kitsune is made by mozilla and according to them, it is what powers the support.mozilla.org

So i downloaded it, and tried to hack it.

FINDING THE IDOR

While going through all url endpoints, i found an interesting endpoint url(r”^/(?P<question_id>\d+)/reply$”, views.reply, name=”questions.reply”)

It calls the function, views.reply. What makes this interesting is this part of the code

Press enter or click to view image in full size

Here, you can see that if you provide a delete_images post parameter, it will delete any image with the id you provided in the delete_image parameter with no checks if the user deleting the image is actually the owner of the image. Compare this to the real image delete function

Press enter or click to view image in full size

It has a proper authorization checks. Also, this functionality is not referenced anywhere in the front end since according to the mozilla team, the snippet is old.

Get Brandon Roldan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i reported it to mozilla bug bounty and asked their permission to actually try it in their staging server. And they agreed. After that, i was able to confirm the bug.

At the time of the report, support.mozilla.org is out of scope, but they still decided to reward me $1500 and added the domain in scope. You can read my whole report in https://bugzilla.mozilla.org/show_bug.cgi?id=1754966.

Thanks for reading, join the bounty hunter discord server: https://discord.gg/bugbounty

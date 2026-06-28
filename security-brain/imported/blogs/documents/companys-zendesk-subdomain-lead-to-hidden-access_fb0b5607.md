---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-28_companys-zendesk-subdomain-lead-to-hidden-access.md
original_filename: 2020-07-28_companys-zendesk-subdomain-lead-to-hidden-access.md
title: Company’s zendesk subdomain lead to hidden access.
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
raw_sha256: fb0b5607dbefc8bdd125dce5cf76ab904e2c852962164ccbd9d2b157bd4e5631
text_sha256: 3689233f58a604b9ababb9dfa1954ce539f537c44c30a370e24fa2609af21f2f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Company’s zendesk subdomain lead to hidden access.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-28_companys-zendesk-subdomain-lead-to-hidden-access.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `fb0b5607dbefc8bdd125dce5cf76ab904e2c852962164ccbd9d2b157bd4e5631`
- Text SHA256: `3689233f58a604b9ababb9dfa1954ce539f537c44c30a370e24fa2609af21f2f`


## Content

---
title: "Company’s zendesk subdomain lead to hidden access."
url: "https://hunter-55.medium.com/introduction-fae7c8b3d16c"
authors: ["himanshu pdy (@himanshu_pdy)"]
bugs: ["Exposed registration page"]
publication_date: "2020-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4376
scraped_via: "browseros"
---

# Company’s zendesk subdomain lead to hidden access.

himanshu pdy
Follow
2 min read
·
Jul 28, 2020

133

Company’s zendesk subdomain lead to hidden access.

Introduction:-

Hi guys!
My name is Himanshu Pdy, and I am a security researcher. This is my second blog :)

let’s start without any delay.

About the issue:-

Here is my new unique writeup that i have recently found.
I have never seen such issue so thought of writing it down.

BUG :- company’s zendesk subdomain lead to hidden access.

Let's begin,

Usually support portal doesn’t show any signup or signin option,

Press enter or click to view image in full size

So i started doing some basic recon and found a subdomain xyz.zendesk.com which i found intresting because it was having a signup option.

Get himanshu pdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I thought it will only work for the employees, but i was WRONG. I was able to successfully sign up.

Press enter or click to view image in full size

But after signin, it was just showing a blank page - - - - >> even tried dirsearch and dirb but found nothing.

So i thought of looking at source code, which showed some js file link.
After some try i found that it redirected me to support portal of the company.
I. E. support.xyz.com

I thought something wrong, but after looking closely, i found that i have found hidden way to log in to support portal.

Press enter or click to view image in full size

I thought it was a normal support portal after user signin to its account.

But wait, i tried to signin as a normal user and it said the email id is not registered.

That means i have registered on the company’s hidden place which should only be accessible to the employees or idk for whom.

I reported this issue but they have support.xyz.com out of scope, so this bug was marked as informative.

BAD LUCK 🙂🙂🙂.

Hope you learn something new from this. Sometimes an external vulnerability can lead to internal hidden and important feature issue.

Be safe during this quarentine ( covid situation). 🙂🙂🙂🙂

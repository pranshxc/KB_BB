---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-23_hey-google-delete-my-data-properly-googlevrp.md
original_filename: 2021-08-23_hey-google-delete-my-data-properly-googlevrp.md
title: 'Hey Google ! - Delete my Data Properly — #GoogleVRP'
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 6c53d5c5f1be11e8d5278db3c8594a7da801ca703cec3b9867e01290dbc99c3c
text_sha256: 36d22928b7ee9493149eb5ca25b2c58291a09146c82d0c6b23d6acd1f6591c2f
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Hey Google ! - Delete my Data Properly — #GoogleVRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-23_hey-google-delete-my-data-properly-googlevrp.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6c53d5c5f1be11e8d5278db3c8594a7da801ca703cec3b9867e01290dbc99c3c`
- Text SHA256: `36d22928b7ee9493149eb5ca25b2c58291a09146c82d0c6b23d6acd1f6591c2f`


## Content

---
title: "Hey Google ! - Delete my Data Properly — #GoogleVRP"
url: "https://medium.com/techiepedia/hey-google-delete-my-data-properly-googlevrp-83349ca8e0e1"
authors: ["Sriram Kesavan (@sriramoffcl)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2021-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3397
scraped_via: "browseros"
---

# Hey Google ! - Delete my Data Properly — #GoogleVRP

Hey Google ! - Delete my Data Properly — #GoogleVRP
Sriram Kesavan
Follow
4 min read
·
Aug 23, 2021

393

Press enter or click to view image in full size
Hey Google

Status: FIXED
Reported: May 05, 2021

Hello y’all it was a long break. Some burnouts, depression and blah blah. And after all that shit jumped right into Google VRP to find what i am capable of again. But let me be honest, this is a accidental find and I didn’t even believe this would even be accepted and rewarded by Google ;)

I have a bad habit of pinning multiple tabs in my browsers which might have some of my confidential data like passwords too…

Yah, it might seem pretty bad and awkward but I do that which makes it comfortable for me. And the place I store these data is Blogger which is set to Private. In-order to overcome this bad practice I decided to delete some of my data and also I deleted some of my Gmail ID’s which I used to create such blogs. After a couple of days when I saw one of my pinned tab the blog was still up and it was still accessible to all users even though I deleted the Gmail ID couple of days back.

Initially i thought it might be some cache hanging out in my browsers but it wasn’t, in that case I tried reproducing the issue. So, i used one of my existing account and create a blog named testblog1.blogspot.com posted some random images and tried deleting the gmail account which i used to create the testblog1. After a couple of hours, I checked if it was still available for public, but it was deleted properly including all the images which i tried to access directly from the CDN.

I was totally confused and decided to recall my old settings of my old blog which I used to store my passwords. I noticed i had my another account added as a author on it. So, i restored the deleted blog which can be done within 30 days and added a New user as Admin to manage the blog.

So,this time instead of one now there are two persons to manage the blog. Here’s a simple image to explain the situation.

Press enter or click to view image in full size
In case#1 there’s only one person to manage the blog
In case#2 there’s two person to manage the blog

And when the Admin on case#1 is trying to delete his entire account, the data is properly deleted.

Get Sriram Kesavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But when there are two admins instead of deleting the blog, the ownership is actually transferred to Admin2. The reason i find this interesting is because when I was trying to delete the account there was no proper message displaying whether the blog ownership will be transferred. I felt something awkward since the application actually fails to notify properly.

Press enter or click to view image in full size

I was still wondering if it would be accepted and even if accepted will be it rewarded 🤔 but still I decided to report this on May 28, 2021 and the bug got accepted on May 31, 2021

That’s not only the shocking thing, it was rewarded with a amazing reward which I never expected to happen. And I had no idea why it was even rewarded and when i tried to know why I found this in Google VRP Rules page.

~ Any design or implementation issue that substantially affects the confidentiality or integrity of user data is likely to be in scope for the program. ( Privacy Dudes !! )

And that’s how I earned a new position in Google Hall of Fame 😂

And the issue is now even patched by simply adding a couple of lines during your Google Account deletion !!

Press enter or click to view image in full size

That’s it for today and follow for more cool write-ups coming up !!

UPCOMING WRITE-UPS !!

Hacking into Google’s Ticketing System — #GoogleVRP

Send a Email, get kicked out of Organization — #GoogleVRP

Abusing video Elements in YouTube — Pt.2 | #GoogleVRP

Well if you love this write up drop a clap 👏, let’s connect then:

Twitter: sriramoffcl

Instagram: sriram_offcl

LinkedIn: sriramkesavan

Peace ✌️ !!!

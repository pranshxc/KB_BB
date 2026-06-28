---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-19_dangling-cnameorphaned-cname-leads-p2-on-google-vrp.md
original_filename: 2024-01-19_dangling-cnameorphaned-cname-leads-p2-on-google-vrp.md
title: Dangling CNAME/Orphaned CNAME leads P2 on Google VRP
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 107fda12f72595878706932a819ad7b256fbefb33061cd70919792d9ed090a5a
text_sha256: bd49be72e9732db78ad5ee62ec38b9818875a3414294d411f8d826345a69e0ab
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Dangling CNAME/Orphaned CNAME leads P2 on Google VRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-19_dangling-cnameorphaned-cname-leads-p2-on-google-vrp.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `107fda12f72595878706932a819ad7b256fbefb33061cd70919792d9ed090a5a`
- Text SHA256: `bd49be72e9732db78ad5ee62ec38b9818875a3414294d411f8d826345a69e0ab`


## Content

---
title: "Dangling CNAME/Orphaned CNAME leads P2 on Google VRP"
url: "https://medium.com/@jerryhackgather/dangling-cname-orphaned-cname-leads-p2-on-google-vrp-fca8964d983c"
authors: ["Jerry1319 (@Mdhsan19)"]
programs: ["Google"]
bugs: ["Subdomain takeover"]
publication_date: "2024-01-19"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 516
scraped_via: "browseros"
---

# Dangling CNAME/Orphaned CNAME leads P2 on Google VRP

Dangling CNAME/Orphaned CNAME leads P2 on Google VRP
Jerry1319
Follow
3 min read
·
Jan 19, 2024

71

As-salamu alaykum everyone, It’s me Mohd Hasan Ansari aka Jerry1319 a you guys knows me well via mine handles ( Reality : Nobody cares 😒) .

Before testing this issue i tried to scan subdomain for subdomain takeover using subzy but didn’t found any hit because all CNAME are valid but it’s a different scenario here which was not even detected by any tools . So without wasting any time let’s start this up

I was testing over google for long time and the product of google is ASM product , let’s gave it a name Jerry.com ( everyone put redact.com let’s change it ) . I tried hard to find out how to login or get access to the ASM product as the access is only accessible for paid users only.

I opened the youtube channel of Jerry.com and started viewing all the videos available there . One of the video’s description has a subdomain link when i checked that out it was giving me a weird error, When i checked the CNAME then it was pointing to a service which was previously owned by Jerry.com but in 2021 they sold this product and name to another company due to which this error is occurring when i searched this issue over internet then i got to know that this scenario is known as Dangling CNAME/ Orphaned CNAME .

What is Dangling CNAME / Orphaned CNAME ?

If a service or product which was previously owned by Jerry.com and now sold-out to any other company but due to some issues developer and auditor forget to Change the CNAME to valid DNS and still it is pointing to Old Product then it’s a Dangling CNAME/ Orphaned CNAME issue.

Press enter or click to view image in full size
CNAME DANGLING

As I explained things here similarly the Jerry.com is pointing to another product which is not owned by google and it is causing them Service disruption and potential exploitation of the subdomain via the sold-out company now who owned the product of google .

Get Jerry1319’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What will be the Impact here ??

It is affect the service disruption, potential subdomain abuse and takeover + Reputational damage to the company.

Conclusion

After confirming everything I wrote a well report explaining everything in it with the attack scenario and all and reported it to google and it was accepted by them .

Tip for reporting issue on google : If your report is not much technical/ business logic issue then add attack scenario explaining every issue in it while reporting to google increases your chances to get accepted As P2 .

Press enter or click to view image in full size

That’s all for today hope that it will help you out in your hunting journey .

Signing out Mohd Hasan Ansari aka Jerry1319

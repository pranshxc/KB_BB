---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-16_bugbounty-aws-s3-added-to-my-bucket-list.md
original_filename: 2018-01-16_bugbounty-aws-s3-added-to-my-bucket-list.md
title: '#BugBounty — AWS S3 added to my “Bucket” list!'
category: documents
detected_topics:
- cloud-security
- command-injection
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- api-security
language: en
raw_sha256: 14809c20eb330c7cab3f36c0433e03772f607d7ec77aa5ce76c8f15cacfa69f8
text_sha256: 3336dd17905aba4e1440f874a0541d195558ddff401854e838dbdd63820b20c0
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — AWS S3 added to my “Bucket” list!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-16_bugbounty-aws-s3-added-to-my-bucket-list.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `14809c20eb330c7cab3f36c0433e03772f607d7ec77aa5ce76c8f15cacfa69f8`
- Text SHA256: `3336dd17905aba4e1440f874a0541d195558ddff401854e838dbdd63820b20c0`


## Content

---
title: "#BugBounty — AWS S3 added to my “Bucket” list!"
page_title: "#BugBounty — AWS S3 added to my “Bucket” list! | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-aws-s3-added-to-my-bucket-list-f68dd7d0d1ce"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["AWS misconfiguration"]
publication_date: "2018-01-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6009
scraped_via: "browseros"
---

# #BugBounty — AWS S3 added to my “Bucket” list!

#BugBounty — AWS S3 added to my “Bucket” list!
Avinash Jain (@logicbomb)
Follow
2 min read
·
Jan 16, 2018

280

Hi Guys,

You might remember the Million Dollar Instagram Bug that allowed security researcher Wes Wineberg to access every single image and account on Instagram. This was only possible because he had gained access to Instagram’s S3 bucket, where the company stored everything from source code to images. In this particular blog, I would be explaining you “How misconfigured AWS storage bucket can be a huge security risk”.

Recently during my bug hunting, I came across a misconfigured AWS S3 bucket of an Indian E-commerce Company which gave me full access to their S3 bucket, allowing them to download, upload and overwrite files. Let’s dig deeper into this and see how I was able to do so — So , while in search for some security vulnerabilities in the website , I came across a career page from where users can apply for the relevant jobs and upload their resume. I started testing it out and found an endpoint (let’s name the company out as xyz )-

“https://xyz.s3.amazonaws.com/career%2Ftest.pdf” and there was no ACL restriction set , any non-authenticated user could simply access any file and below was the curl request —

curl -XGET ‘https://xyz.s3.amazonaws.com/career/test.pdf'

and the response was the content of test.pdf. Similarly , I discovered that “PUT” method was enabled on the S3 bucket and I could simply write any file onto the S3 bucket , it was publicly writable.

curl -XPUT -d ‘HACKED’ ‘https://xyz.s3.amazonaws.com/career/test.pdf'

I ran some bruteforcing over filename and I was able to read the resume content of other users. :) , Now, I have to take this one level up , my next target was to list down and read all the files that were available onto S3 bucket. I connected to s3 command line and run the following command

“ root@logicbomb~# aws s3 ls s3://xyz.s3.amazonaws.com”

and to no surprise, I was able to access the complete s3 bucket , all the CVs/Resume of users (also there were more sensitive data and directories ) were publicly accessible and readable :) I tried some more commands -

root@logicbomb:~# aws s3 rm s3://xyz.s3.amazonaws.com/career/test.pdf

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

delete: s3://xyz.s3.amazonaws.com/career/test.pdf

and I was also able to delete the files also.

As a conclusion resides that Misconfigured S3 bucket may take your organisation to expose sensitive data.

Mitigation — Advise you to promptly review your S3 buckets and their contents to ensure that you are not inadvertently making objects available to users that you don’t intend. For reference, you can read the below link —

Amazon S3 Security: master S3 bucket polices and ACLs
Welcome to part 8 of my AWS Security Series. This week I shall be looking at some of the security features around the…

cloudacademy.com

Report details-

08-Dec-2017 — Bug reported to the concerned company.

29-Dec-2017 — Bug was marked fixed.

01-Jan-2018 — Re-tested and confirmed the fix.

07-Jan-2018 — Awarded by company.

Thanks for reading!

~Logicbomb (https://twitter.com/logicbomb_1)

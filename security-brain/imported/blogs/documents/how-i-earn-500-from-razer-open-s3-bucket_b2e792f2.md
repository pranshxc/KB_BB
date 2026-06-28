---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-12_how-i-earn-500-from-razer-open-s3-bucket.md
original_filename: 2020-01-12_how-i-earn-500-from-razer-open-s3-bucket.md
title: How I earn $500 from Razer open S3 bucket
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- file-upload
- mobile-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- file-upload
- mobile-security
language: en
raw_sha256: b2e792f2cdcd5488b5849d7b4ebbfd37f0e466097fbdf43255fd99d5db547cb5
text_sha256: c6dc33e06bf437b370c2a717fadeb6a1bac9f5339a78662ea8ba101b2f77dbd2
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I earn $500 from Razer open S3 bucket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-12_how-i-earn-500-from-razer-open-s3-bucket.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, file-upload, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b2e792f2cdcd5488b5849d7b4ebbfd37f0e466097fbdf43255fd99d5db547cb5`
- Text SHA256: `c6dc33e06bf437b370c2a717fadeb6a1bac9f5339a78662ea8ba101b2f77dbd2`


## Content

---
title: "How I earn $500 from Razer open S3 bucket"
url: "https://medium.com/sourav-sahana/how-i-earn-500-from-razer-open-s3-bucket-fe314e4bbab8"
authors: ["Sourav Sahana (@kernel_rider)"]
programs: ["Razer"]
bugs: ["AWS misconfiguration"]
bounty: "500"
publication_date: "2020-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4833
scraped_via: "browseros"
---

# How I earn $500 from Razer open S3 bucket

How I earn $500 from Razer open S3 bucket
Sourav Sahana
Follow
3 min read
·
Jan 12, 2020

265

1

Hii Hunters ! Hope you all are hunting good. Back again with another write-up. I submitted this report to Razer and they rewarded me $500 for this report. So I have mentioned all the details from the beginning. If you already have good knowledge about AWS then you can skip up to “How Developers leave buckets vulnerable ?”. Let’s begin the show ..

So what is AWS s3 bucket ?

An Amazon s3 bucket is a public cloud storage (Simple Storage Service or s3). Every bucket has an unique name. You probably heard about the AWS subdomain takeover. Where if any domain uses s3 bucket to host a website and if that bucket doesn’t exist in AWS. Then you can claim the bucket, means whatever you upload to the bucket it renders on the website. But this is not limited too. S3 bucket can be used many purposes, like anyone can store personal files, sometimes application store user’s profile pictures, javascript files, etc.

How Developers leave buckets vulnerable ?

There is mainly three access control configuration of s3 bucket.

(1). Bucket can’t be accessed publicly.

(2) People can only show the bucket contains (key). You should always look for sensitive files in this type of bucket.

(3) All access is given publicly. Where you can upload, delete anything from the bucket. I use AWS CLI to see how the bucket is configured.

How I find open bucket in Razer..

Get Sourav Sahana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was playing with this domain : https://api.razer.com . There is a file upload functionality. First I started uploading malicious files if I get any RCE . But That was implemented properly. But when I’m uploading something, in the response showing the picture’s location, where the picture uploaded. And that was a s3 bucket. Immediately I opened the terminal and run this command to upload a txt file:

#aws s3 cp test.txt s3://rzimageupload

Press enter or click to view image in full size

And BaaM !! I can upload and delete files from the bucket. I reported it.

Bucket from android app…

The next day I was testing the Razer Android app. Almost all the programs don’t accept issues that required root access and the physical device. That’s why many hunters don’t check internal files. But I found this bucket: kaizo-s3-public.s3-ap-southeast-1.amazonaws.com in share_prefs directory. And again this was also an open bucket. So I mentioned this in the previous report.

Press enter or click to view image in full size

H1 report: https://hackerone.com/reports/700051

My report had triaged and I got bounty $500 .

Thank you.. Hope you have enjoyed this. Stay tuned with me because I have more web and android reports to share.

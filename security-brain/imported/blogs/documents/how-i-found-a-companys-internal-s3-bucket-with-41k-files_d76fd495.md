---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-24_how-i-found-a-companys-internal-s3-bucket-with-41k-files.md
original_filename: 2022-05-24_how-i-found-a-companys-internal-s3-bucket-with-41k-files.md
title: How I Found a company’s internal S3 Bucket with 41k Files
category: documents
detected_topics:
- cloud-security
- idor
- access-control
- command-injection
- path-traversal
- rate-limit
tags:
- imported
- documents
- cloud-security
- idor
- access-control
- command-injection
- path-traversal
- rate-limit
language: en
raw_sha256: d76fd495a4bfeda1d0613b1a1fb728c14f86bbef8c29cb3aa75fd1fdade8a36a
text_sha256: c87c1c4800a556429a2186d7f9bcc23eb1a9ab089859fce9fc085f34d8d87497
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found a company’s internal S3 Bucket with 41k Files

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-24_how-i-found-a-companys-internal-s3-bucket-with-41k-files.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, access-control, command-injection, path-traversal, rate-limit
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `d76fd495a4bfeda1d0613b1a1fb728c14f86bbef8c29cb3aa75fd1fdade8a36a`
- Text SHA256: `c87c1c4800a556429a2186d7f9bcc23eb1a9ab089859fce9fc085f34d8d87497`


## Content

---
title: "How I Found a company’s internal S3 Bucket with 41k Files"
url: "https://infosecwriteups.com/how-i-found-a-companys-internal-s3-bucket-with-41k-files-94b453e588b5"
authors: ["Tarun Koyalwar (@KoyalwarTarun)"]
bugs: ["AWS misconfiguration"]
bounty: "250"
publication_date: "2022-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2611
scraped_via: "browseros"
---

# How I Found a company’s internal S3 Bucket with 41k Files

How I Found a company’s internal S3 Bucket with 41k Files
Tarun Koyalwar
Follow
4 min read
·
May 24, 2022

218

7

I found a company’s S3 bucket which was used internally and was not referenced anywhere in GitHub or its domain. This was my first valid vulnerability which I reported 7 months ago and was only possible due to manual recon.

About Me —

I’m Tarun, a security researcher and bug hunter from India. You may already know me from my previous article on writing automation scripts without bash Scripting. I hunt for bugs or create some evil software. Follow me on

github = https://github.com/tarunKoyalwar

twitter = https://twitter.com/KoyalwarTarun

medium = https://medium.com/@zealousme

to be updated on new tools and writeups

Recon —

There are many ways to find S3 buckets for a particular program the most common ones would be from burp proxy, hakrawler,gospider, or GitHub. There are some other ways to find s3 buckets maybe I will write a new article about that.

As a Newbie I was following the JHaddix v4 Methodology, The scope was limited and there was no point in doing ASN or Vertical Enumeration Still I visited Crunchbase and I searched for the company name of the program. In the Details section, I found Also Known As Header With FooBar Inc (Redacted). As soon as I found this header I checked if there is a GitHub org with a name something similar to this. I found it but there were no public repos.

GrayHatWarfare

GrayHatWarfare is an excellent place to search for S3 Bucket and Filter them but the only thing that sucks about this is their pricing, especially for Newbies since anyone rarely finds an open S3 Bucket. After I Found an alternative name I searched for it and Some other variations of names such as foodev etc. by visiting the following URL.

https://buckets.grayhatwarfare.com/buckets

This feature is only available if you are registered and has only access to limited buckets . New Buckets are regularly updated but that feature is only to premium subscribers.

Press enter or click to view image in full size

I searched for it and found a bucket with the name foositedev with 41K files. I decided to use aws-cli. You can refer here for setup and config.

S3 Bucket Enum —

Get Tarun Koyalwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can check permissions for the S3 bucket using aws-cli. There are 5 main permissions of S3 Bucket and you can test each permission using the below commands.

LIST = List all Files of S3 Bucket

aws s3 ls s3://bucketName

READ = Read a particular object(file)

aws s3 cp s3://bucketName/PathtoFile  LocalFile

WRITE = Write /Overwrite/Delete a particular Object(file)

aws s3 cp poc.txt s3://bucketName/poc.txt

READ_ACP = Read Access Control Permissions

aws s3api get-bucket-acl --bucket bucketName

WRITE_ACP = Write/Modify Access Control Permissions

aws s3api put-bucket-acl --acl public-read-write --bucket bucketName

Continued —

After using the above commands I was able to find that bucket had READ_ACP,LIST,READ Permissions Enabled. It had 41k files so It was not feasible to download all files I came across the below command which lists all objects in the bucket

aws s3 ls --summarize --human-readable --recursive s3://bucketName

It listed all files with their path and total files and the total size of the bucket which was 23.6 GB. I decided to take a look after viewing some by filtering using grep were node modules, HTML, gif, jpeg, etc. All of those were useless .

Source: Giphy

I saved output to file and created a bash script that outputs different file types and their frequency.

After using the above script, In the output there were different types of files among them I found some CSV with name `users` I grepped and downloaded them with wget -i urls.txt -P directory .

Press enter or click to view image in full size

These CSV files were backups from their database and contained usernames, email, phone numbers, addresses, and a lot of other PII (total 32 columns) a lot of those emails were staff emails and had @companyname emails. I wrote a report and described in detail and submitted it. It was quickly accepted and I was rewarded $250 and submission was marked as high severity.

Even Though It was a million-dollar company it had a very low bounty reward of $500= critical, $250 = High,$100 = Medium, and $0 = Low, and did not accept any P4 or P5 . After this report, I only hunted on the same program for 4 months and I found approx 18 vulns with duplicates, medium, high, and 6 Critical but no Low severity Vulnerabilities.

Follow me on medium & twitter , So you will not miss my upcoming writeups

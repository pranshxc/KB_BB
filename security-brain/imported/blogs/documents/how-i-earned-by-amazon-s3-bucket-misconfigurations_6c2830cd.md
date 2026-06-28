---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-earned-by-amazon-s3-bucket-misconfigurations.md
original_filename: 2021-07-29_how-i-earned-by-amazon-s3-bucket-misconfigurations.md
title: How I earned $$$$ by Amazon S3 Bucket misconfigurations?
category: documents
detected_topics:
- cloud-security
- sso
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 6c2830cd1672346ead96543bf2b1596bfd98b853681eef8d2f1e9012d1bdd73b
text_sha256: fcbd1af4c35a0d2a65d6a217528c1d71c6b02bdb717fd96f71900ee7410661a3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $$$$ by Amazon S3 Bucket misconfigurations?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-earned-by-amazon-s3-bucket-misconfigurations.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6c2830cd1672346ead96543bf2b1596bfd98b853681eef8d2f1e9012d1bdd73b`
- Text SHA256: `fcbd1af4c35a0d2a65d6a217528c1d71c6b02bdb717fd96f71900ee7410661a3`


## Content

---
title: "How I earned $$$$ by Amazon S3 Bucket misconfigurations?"
url: "https://3bodymo.medium.com/how-i-earned-by-amazon-s3-bucket-misconfigurations-29d51ee510de"
authors: ["Abdullah Mohamed (@3bodymo_)"]
bugs: ["AWS misconfiguration", "Subdomain takeover"]
publication_date: "2021-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3469
scraped_via: "browseros"
---

# How I earned $$$$ by Amazon S3 Bucket misconfigurations?

Top highlight

How I earned $$$$ by Amazon S3 Bucket misconfigurations?
Abdullah Abdelrazek
Follow
5 min read
·
Jul 28, 2021

461

1

Press enter or click to view image in full size

Hi
all, in this story I will talk about several misconfiguration that I found related to the Amazon S3 Buckets.

Also I will mention some tricks and tools that will help you to find this type of vulnerability.

What is the important tools?

At first and before use any other tools, you have to install awscli and configure it with your AWS credentials.

Amazon tutorial
Video tutorial

After you installing awscli, and if you want a tool that performs an automatic scan instead of a manual scan, I advise you to use one of these tools.

S3Scanner
s3-buckets-finder
Now I’m going to talk about my finding and some tricks I used.

I browsed one of subdomains, then I found that all images and JS files was uploaded to S3 bucket, let’s call the first bucket I found qa-media.company, so I checked the bucket through awscli.

Surprisingly, I was not given an “AccessDenied” message and I could list the files.

I checked the bucket manually using awscli, I tried copy, move and delete but the bucket seems to be set fine, so I didn’t have any permissions to do that.

The commands I used it to check:
ls command:

aws s3 ls s3://qa-media.company/

This command will list all directories of bucket.

Copy command:

aws s3 cp fileName.txt s3://qa-media.company/

This command will upload fileName.txt file from your computer to the bucket.

Move/Rename command:

aws s3 mv s3://qa-media.company/files/fileName.txt s3://qa-media.company/images/

This command will move fileName.txt file to images directory.

aws s3 mv s3://qa-media.company/fileName.txt s3://qa-media.company/PoC.txt

This command will rename fileName.txt file to PoC.txt.

Delete command:

aws s3 rm s3://qa-media.company/fileName.txt

This command will delete fileName.txt file.

“Listing of S3 Bucket accessible” some of companies consider it a vulnerability and pay for it, but it’s not a high or critical vulnerability so I couldn’t report it because the company I’m working on it accepts only high and critical vulnerabilities. Now I have no choice but to find sensitive files in this bucket to report.

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I walked through files to make sure if there any interesting data worth reporting. I found directory called “invoices” and when I browsed it I found some PDF files. I copied one of PDF files to opened through browser to see the content of file, the surprise is that the response was 200, and as I expected, the file contained an invoice for a customer with his name, number and home address, finally it is PII data and worth reporting.

Press enter or click to view image in full size
Number of exposed invoices

Now I will explain how I found more buckets belonging to the company.

At first I created a wordlist.txt file containing numbers from 0 to 100 and I ran ffuf tool with following command:

ffuf -u https://qaFUZZ-media.company.s3.amazonaws.com/ -w wordlist.txt

Surprisingly, there is another bucket called qa2-media.company and when I checked it I didn’t find any important files but I found that I had all the permissions on it, so I reported it.

Press enter or click to view image in full size
qa2-media.company bucket

After I reporting these two reports, I went back to the company’s main website to see where the files of website were uploaded. As I expected, all site files were uploaded to a bucket called prod-media.company.

As usual I tried copy, move and delete, but I didn’t have permission. I found almost the same files that I found in the first bucket, so I decided to go to the “invoices” directory again. The big surprise is when I counted PDF files by wc -l command, the number was 314,642 and it is public, WoW.

Press enter or click to view image in full size
Number of exposed invoices

My concluded was that the previous bucket that I found contained customer data, but in a temporary period, until this bucket was created and the data became stored in it.

After I found the three previous buckets, I knew how the company chooses their bucket names so I downloaded subdomains wordlist and I ran ffuf tool with the following command:

ffuf -u https://FUZZ-media.company.s3.amazonaws.com/ -w wordlist.txt

The result was that there were two other buckets, the first one called preprod-media.company and the other was dev-media.company.

The first bucket didn’t contain any important files and I didn’t have any permissions on it, so I didn’t report it, but the second bucket I had all the permissions on it so I reported it.

Press enter or click to view image in full size
dev-media.company bucket

Also I want to mention how I found a subdomain takeover in this company using the brute force, but I did not use the brute force randomly, after the stage of collecting subdomains by common methods such as using amass tool, I found subdomains like this:

qa-api.company.com
prod-api.company.com
api.company.com
media.company.com

So I used dnscan to find subdomains by brute force and I used the following command:

python3 dnscan.py -d %%-media.company.com -w wordlist.txt -n

There were many results and when I went through all the results I found this subdomain qa-media.company.com that showed me this error.

Press enter or click to view image in full size
Before I takeover it

Wow it seemed to be a subdomain takeover, I quickly opened my AWS account to register the bucket, and when I back to subdomain I found that its statues code changed to “AccessDenied”, I really got it.

Press enter or click to view image in full size
After I takeover it
Lessons learned
Amazon s3 buckets may contain a lot of misconfiguration so don’t ignore it.
Always check where the images and JS files are uploaded. The company may be using Amazon s3 bucket.
Understand how the subdomains or buckets is named so that you can use brute force in an orderly manner, that will give you more subdomains or more buckets to check them.

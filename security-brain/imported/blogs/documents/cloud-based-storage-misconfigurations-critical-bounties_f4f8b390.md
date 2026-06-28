---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-05_cloud-based-storage-misconfigurations-critical-bounties.md
original_filename: 2021-04-05_cloud-based-storage-misconfigurations-critical-bounties.md
title: Cloud Based Storage Misconfigurations -> Critical Bounties
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: f4f8b390723b9cdd5def5cbf31350d01dbddda53fde18dd561f99ed737d0532d
text_sha256: 8e69c4dd4c6ffd15a42c1164e7e914558b2b25fdd5948cfc964f1181bdc305f6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Cloud Based Storage Misconfigurations -> Critical Bounties

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-05_cloud-based-storage-misconfigurations-critical-bounties.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `f4f8b390723b9cdd5def5cbf31350d01dbddda53fde18dd561f99ed737d0532d`
- Text SHA256: `8e69c4dd4c6ffd15a42c1164e7e914558b2b25fdd5948cfc964f1181bdc305f6`


## Content

---
title: "Cloud Based Storage Misconfigurations -> Critical Bounties"
url: "https://mikey96.medium.com/cloud-based-storage-misconfigurations-critical-bounties-361647f78a29"
authors: ["Mikey (@mikey96_bh)"]
bugs: ["Cloud storage misconfiguration"]
bounty: "7,500"
publication_date: "2021-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3758
scraped_via: "browseros"
---

# Cloud Based Storage Misconfigurations -> Critical Bounties

Cloud Based Storage Misconfigurations -> Critical Bounties
Mikey
Follow
4 min read
·
Apr 5, 2021

697

8

Press enter or click to view image in full size
Critical Bounties from Storage Misconfigurations!

I started looking into cloud-based storage around about a year and a half ago with a friend. I was instantly fascinated with the process behind setting up these storage containers, whether it be AWS S3 Buckets, Azure Blobs or Google Storage Buckets. The process simply involved a series of check boxes which controlled the configuration of the container. My friend and I noticed how easy it was to make a mistake during this process, especially if you were not aware of what each option meant and the consequences of a misconfiguration.

Press enter or click to view image in full size
Part of the setup process for an AWS S3 Bucket.

I had the initial idea that I would develop a tool that would allow me to scan a large number of S3 buckets quickly and look for such a misconfiguration. A very simple tool was written in python which allowed me to subdomain enumerate *.s3.amazonaws.com and iterate through enumerated domains to look for enabled directory listing, which is a great indicator of misconfigured S3 buckets. You can see the difference between a correctly and incorrectly configured S3 bucket below.

Press enter or click to view image in full size
Correctly configured private bucket.
Press enter or click to view image in full size
Incorrectly configured private bucket containing SQL backup.

The tool was very simple to build based upon the fact that distinguishing between correctly and incorrectly configured buckets was easy to implement. Also due to directory listing being enabled on the majority of these misconfigured buckets it was easy to parse for any file extensions and keywords that may be of interest to me. Common extensions and keywords that we implemented into the scanning functionality were: sql, sql.gz, backup.zip, backup.gz, backup.tar, backup.tar.gz and many many more.

Get Mikey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The second image above shows what a real-life positive hit would look like for a misconfigured bucket containing a sensitive file of interest matching our keywords/extensions. You can see the presence of an sql.gz file, which in this case was a back-up to a SQL database. Inside these files there are often sensitive information range from account data, passwords and PII.

Once I had finished developing the tool and analysed the data from the first few scans I decided to conduct more research to try and broaden our attack surface and find more buckets to scan. Upon doing so I stumbled upon https://buckets.grayhatwarfare.com/ which had essentially done my job for me. This site is nothing short of incredible for this area of research, it currently has 347683 S3 buckets scanned and indexed, alongside 24444 Azure Blobs also scanned and indexed. Grayhat is a user friendly web-application that allows you to search through the indexed data using both keywords and extensions, very much like my initial simple python script on steroids. I should add that Grayhat also comes with a very useful API!

Press enter or click to view image in full size
https://buckets.grayhatwarfare.com/

Now the initial issue was solved of attack surface I decided to fully utilize Grayhat and its API. I changed my approach to create a python tool that would allow me to use the API to make a large number of requests and ex-filtrate buckets/blobs which contained interesting files. I would also check if any of the buckets I was reporting were writable using the command: aws s3 cp proof.txt s3://[BUCKET_NAME] — no-sign-request. This would often further increase the impact as you could host malicious files on the companies storage, or even just run them up a pricey AWS bill. This is definitely one to try on any buckets you find that have bounty programs!

In doing so I had tremendous luck, which led to two critical bounties on Bugcrowd (see below). I was not only rewarded for these two that existed on bounty programs, but I have been rewarded with cash payments by around 15 companies privately that were very appreciative of my responsible disclosure. I am still in touch with a small number of these companies and conduct routine tests on new features they are adding to their platforms to ensure they are secure. This research has been a great method for me to build relationships with companies and develop my experience. I would highly recommended it to anyone who is interested!

Press enter or click to view image in full size
Critical Bounties from Storage Misconfigurations!

In conclusion, cloud based storage is great but it is very easy to make catastrophic mistakes. If you are setting them up then please ensure you test the access control yourself before uploading any sensitive files. I would also advise anyone who is keen to start on this research to use Grayhat as it is an incredible asset. There are still many, many public buckets out there with SQL database back-ups sitting on them so do your part and help secure these companies by disclosing your findings responsibly.

I am also happy to share any tools I have developed, so just reach out to me if they will be of interest to you!

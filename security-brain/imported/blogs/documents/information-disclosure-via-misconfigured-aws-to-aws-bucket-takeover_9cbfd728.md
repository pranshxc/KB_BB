---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-08_information-disclosure-via-misconfigured-aws-to-aws-bucket-takeover.md
original_filename: 2019-07-08_information-disclosure-via-misconfigured-aws-to-aws-bucket-takeover.md
title: Information Disclosure via Misconfigured AWS to AWS Bucket Takeover
category: documents
detected_topics:
- cloud-security
- idor
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- cloud-security
- idor
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 9cbfd7280cd02b7f8ba97be2bd819f6f290e81a5046381f14b4db41e0f001775
text_sha256: 7d1fe9eb0c9128c7373857fbbbf4cca823a0969633d958c546c29ee3d7a3ce32
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Information Disclosure via Misconfigured AWS to AWS Bucket Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-08_information-disclosure-via-misconfigured-aws-to-aws-bucket-takeover.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9cbfd7280cd02b7f8ba97be2bd819f6f290e81a5046381f14b4db41e0f001775`
- Text SHA256: `7d1fe9eb0c9128c7373857fbbbf4cca823a0969633d958c546c29ee3d7a3ce32`


## Content

---
title: "Information Disclosure via Misconfigured AWS to AWS Bucket Takeover"
url: "https://medium.com/@pratyush1337/information-disclosure-via-misconfigured-aws-to-aws-bucket-takeover-6a6a66470d0e"
authors: ["Pratyush Anjan Sarangi"]
bugs: ["AWS misconfiguration"]
publication_date: "2019-07-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5162
scraped_via: "browseros"
---

# Information Disclosure via Misconfigured AWS to AWS Bucket Takeover

Pratyush Anjan Sarangi
Follow
5 min read
·
Jul 8, 2019

148

2

Information Disclosure via Misconfigured AWS to AWS Bucket Takeover

Hey! Welcome to a new write up on my recent finding of a Misconfigured AWS bucket and how i was able to Take full control of the AWS bucket.

I was checking out the website mainly for the IDOR Vulnerabilities as those are considered as High priority bugs and are paid in high range. I was trying to check every possible end-points to find any parameter to manipulate the numerical value so i fired up my burp suite and sent the request to spider tab to check out all the endpoints but i failed because they have encrypted every numerical value using salted algorithm.

As it was not possible to find any IDOR , i found an interesting endpoint where i was able to set my organization logo and there was a direct link to the logo which was residing at an AWS bucket. You can check below:

Press enter or click to view image in full size

So i checked this logo by directly coping it and opening it in the new tab:

Press enter or click to view image in full size

Basically i never though that i will find anything like this so i never thought of doing anything in any programs or private programs i have worked on but that day i thought that let’s go to origin directory of the file[in hacker’s language ../ ;)]. so i checked it by going to the origin directory as you can see:

Press enter or click to view image in full size

Bingo! this was a proper Information disclosure due to Misconfigured ACL of the AWS bucket. I was happy and thought of reporting this directly but as a Hacker you are always overwhelmed and curious to find all the juicy information that might be possible to exploit. So without wasting any time , I went ahead to check out all the files getting listed in the Directory but before that i tried to access one of the file to check if the files are real or not.

Press enter or click to view image in full size

Than i opened the file to see what is the content:

Press enter or click to view image in full size

Now i am confident enough that all the files available here are legitimate[Use of sophisticated word to look geeky 🤓] and we can see all the internal files of the xyz company here with small tutorials , screenshot and this was an internal S3 bucket used for training and demonstration purposes, such as sharing screenshots of their products……I guess so now you can see why it’s Critical.

Get Pratyush Anjan Sarangi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At that moment , I felt like it’s enough to report now but i took a chance and thought if there is something else the bucket is offering to compromise itself…Damn Is it possible? Let’s see what happens…. I started checking files with extensions, especially with .zip or .htm or .eml or .doc or .csv and while searching through the entire bucket[which consisted of more than 700+ files] and found the first zip file:

Press enter or click to view image in full size

So i downloaded it and checked the contents:

Press enter or click to view image in full size

After checking on the files of that zip , i figured out that it’s not going to offer me anything to compromise the AWS bucket. So i started searching for other zip files and found an interesting zip file in the AWS bucket:

Press enter or click to view image in full size

Now i downloaded the file and opened to check the contents:

Press enter or click to view image in full size

I checked all the files but the important file was the “document.wflow” , It has everything i required to TAKEOVER the AWS Bucket. Let’s check the content:

Press enter or click to view image in full size

I was so happy to see this credentials but now the funny thing is that i don’t know what to do with that because Zero knowledge in AWS. So the best way i found was i asked one of my office colleague who is a Dev and works on AWS. He told me that , Go to google and download S3 Browser to start browsing the AWS bucket if you have the “access_key” and “secret_key” which was a very new learning experience in the field of my Web Application Penetration Testing. I was like:

So i downloaded it and started providing all the required credentials:

Press enter or click to view image in full size

Boom!

Press enter or click to view image in full size

The next thing i checked on the Access Control List permission on each directory and found a directory with full access:

Press enter or click to view image in full size

With the full access to this directory now I am the Owner of this and i can upload any file i want , I can delete it and i can Delete the whole directory. I had all the access in the world but As you all know we are all ethical in what we do so to make a Proof Of Concept i uploaded a file:

Press enter or click to view image in full size

Now to re-verify it I checked it in the public facing bucket with my uploaded file name.

Press enter or click to view image in full size

Final check I pasted the filename in the URL and checked:

Press enter or click to view image in full size

Damn! AWS Bucket Takeover!

Following my initial report and its review, they had promptly and fairly compensated me for letting them know about this bug. I am really thankful for that :)

Timeline:
May. 21, 2019 — Initial Report
May. 22, 2019 — Report Triaged
May. 22, 2019 — Bug Fixed and Rewarded

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-26_write-up-aws-document-signing-security-control-bypass.md
original_filename: 2020-02-26_write-up-aws-document-signing-security-control-bypass.md
title: 'Write-up: AWS Document Signing Security Control Bypass'
category: documents
detected_topics:
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 3ace3b43d6e275c5e3a533655ccdf823cb63b90b94951cbb47c7d55fa52e2557
text_sha256: d4a064545bd50e551376983481bdce864baf89e4bd3a4f515f0d2854680f93d2
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Write-up: AWS Document Signing Security Control Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-26_write-up-aws-document-signing-security-control-bypass.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `3ace3b43d6e275c5e3a533655ccdf823cb63b90b94951cbb47c7d55fa52e2557`
- Text SHA256: `d4a064545bd50e551376983481bdce864baf89e4bd3a4f515f0d2854680f93d2`


## Content

---
title: "Write-up: AWS Document Signing Security Control Bypass"
url: "https://medium.com/@ozguralp/write-up-aws-document-signing-security-control-bypass-2b13a9c22a4d"
authors: ["Ozgur Alp (@ozgur_bbh)"]
bugs: ["AWS misconfiguration"]
bounty: "1,000"
publication_date: "2020-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4750
scraped_via: "browseros"
---

# Write-up: AWS Document Signing Security Control Bypass

Write-up: AWS Document Signing Security Control Bypass
Ozgur Alp
Follow
3 min read
·
Feb 26, 2020

434

1

While I prefer more to write/talk about far-going topics instead of just one vulnerability write-up, I decided to make an exception for this one because it was definitely an original one.

So, while I was hunting one of the weekly targets of Synack, I found out a document upload section to check out. A good entrance point for a RCE, right?

Press enter or click to view image in full size
Document upload section

On the both document upload and document view sections, I found out that the application is using Amazon AWS as CDN for storing & gathering these uploaded documents. For the view of the document, the request was like on the below:

Press enter or click to view image in full size
Viewing the document

So the application was sending a request to the /s3/preSignedURL endpoint with some parameters such as a payload to define the exact file and an operation name.

For the ones who are not familiar with the technology, AWS has a signing technology which is used on demand, which ensures that access to the sensitive documents are not possible via malicious third parties. These signatures are generated on the back-end with some private information such as AWS secret keys.

Press enter or click to view image in full size
AWS signing process

If you are more interested about this signing technology, you can check it our via: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html

Get Ozgur Alp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So the /s3/preSignedURL endpoint was used for gathered the signed URL’s on the AWS storage for viewing documents. URL encoded payload parameter was having the value below:

payload={"linkType":"Attachment","S3TmpKey":"8f397040-8f08-48a6-a431-8db7ffc8be17/2018_SRT_Calendar.pdf","S3TmpVersion":"mkFzDQmQ3L9sCnzSKbiQE7wYtcGVboJ7","xhr":{},"link":"","linkVersion":"","fileName":"2018_SRT_Calendar.pdf","progress":"100","fileStatus":"Uploaded","size":"6.7 MB","lastModified":1516121201000}

And on the response, the url parameter was generated with the syntax:https://target.attachments.s3.amazonaws.com/<S3TmpKey>?Signatures. How to proceed next?

Well, on all of my testing, I prefer to send requests which are clean and basic all the time for a better understanding, and if the response returns error then add the other parameters one by one to check the behavior on the back-end to see what is that used for. For this one, I deleted all parameters except S3TmpKey which value was equals to my documents path/name and I also deleted that parameters value and send it empty.

Press enter or click to view image in full size
URL decoding the payload parameter, deleting all parameters except S3TmpKey, emptying its value and URL encoding it again

Sending S3TmpKey parameter empty returned the valid signing for the S3 buckets root directory.

Press enter or click to view image in full size
Valid signatures for root directory

Direct access to the URL parameter from browser returned directory listing for all documents names and their exact paths!

Directory listing on AWS S3 bucket

Within assigning S3TmpKey parameter to these paths/filenames to other users, it was possible to gather all documents under this S3 bucket!

This discovery brought me around 1k payout after 4 or 5 hours of my submission (Thanks to 24 hour rule of Synack) and the client fixed it within a week due to the criticality of it.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

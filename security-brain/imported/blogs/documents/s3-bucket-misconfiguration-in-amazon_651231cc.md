---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-11_s3-bucket-misconfiguration-in-amazon.md
original_filename: 2018-08-11_s3-bucket-misconfiguration-in-amazon.md
title: S3 Bucket Misconfiguration in Amazon
category: documents
detected_topics:
- cloud-security
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 651231cc04b54a61cea438f25106926e47b4ef94dcd7b283281468e7fc653454
text_sha256: cf25355b08ad91fb7076efbd2a8a8eaedaac96ed41a1c9076352e90011670ccc
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# S3 Bucket Misconfiguration in Amazon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-11_s3-bucket-misconfiguration-in-amazon.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `651231cc04b54a61cea438f25106926e47b4ef94dcd7b283281468e7fc653454`
- Text SHA256: `cf25355b08ad91fb7076efbd2a8a8eaedaac96ed41a1c9076352e90011670ccc`


## Content

---
title: "S3 Bucket Misconfiguration in Amazon"
url: "https://medium.com/@justmorpheus/s3-bucket-misconfiguration-in-amazon-a7da6a6e02ea"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
programs: ["Amazon"]
bugs: ["AWS misconfiguration"]
publication_date: "2018-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5755
scraped_via: "browseros"
---

# S3 Bucket Misconfiguration in Amazon

S3 Bucket Misconfiguration in Amazon
Description
Divyanshu
Follow
3 min read
·
Aug 12, 2018

177

Summary:

While trying to access one of the contacts us page on https://www.amazon.in , I discovered one misconfigured s3 bucket. In this scenario where the misconfiguration of an S3 bucket allowed any user to upload and delete any file to the s3 bucket: https://bbcomm-mgr-ui-attachments-eu.s3.amazonaws.com

While looking to find out contact customer care, I saw page having upload functionality so why not try uploading some php shell. Turned my burp intercept on and tried to bypass the file upload. It allowed png, jpeg and gif. But everytime I tried to upload, it showed error response but then I started spider to find out any other page linked to this page. I saw there is one s3 bucket with same file I was trying to upload. After copying the link I was able to download my file.
Woaah! I was able to find misconfigured amazon bucket. It was bucket from which customer executives might be able to download attachment sent to them. When you ask retailer about invoice receipt, you can attach image,pdf,etc there. That attachments are uploaded to s3 bucket.

Target :

https://bbcomm-mgr-ui-attachments-eu.s3.amazonaws.com

Proof-of-concept

1) Visit URL:
https://bbcomm-mgr-ui-attachments-eu.s3.amazonaws.com/login2.html

2) Try writing and deleting files in the bucket:

a)Writing Command:
Using Curl writing index.html

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

curl -XPUT -d ‘<html><h1> Upload by justmorpheus</html>’ ‘https://bbcomm-mgr-ui- attachments-eu.s3.amazonaws.com/index.html’

Press enter or click to view image in full size
index.html

b)Using AWS CLI:
Move and Copy Command:

aws s3 mv login.html s3://bbcomm-mgr-ui-attachments-eu — grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers
Press enter or click to view image in full size
aws s3 cp login2.html s3://bbcomm-mgr-ui-attachments-eu — grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers
Press enter or click to view image in full size

Deleting Command:

aws s3 rm s3://bbcomm-mgr-ui-attachments-eu/login.html
aws s3 rm s3://bbcomm-mgr-ui-attachments-eu/index.html
Press enter or click to view image in full size

Result:
We now have full write/execute access to an Amazon.in S3 bucket.
Also tried bruteforcing directories using dirbuster and discovered a folder.
Which can be used to download confidential files and also for phishing purpose.

Solution:

Don’t allow anyone for full read/write/execute access.
See the documentation: https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html

Reference and Thanks:

https://blog.detectify.com/2017/07/13/aws-s3-misconfiguration-explained-fix/
https://medium.com/@jonathanbouman/how-i-hacked-apple-com-unrestricted-file-upload-bcda047e27e3

Special mention @kunal_mahar — Information security Analyst.

Timeline:

10/07/2018: Discovered and reported to Amazon.
10/07/2018: Bug confirmed and case id assigned.
03/08/2018: Bug fixed by the amazon security team.
12/08/2018: Published POC.

PS: No hall of fame or reward from Amazon as it works under coordinated disclosure policy
@justm0rph3u5

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

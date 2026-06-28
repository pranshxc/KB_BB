---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-20_parameters-in-lambda-functions-that-lead-to-xss-and-injection.md
original_filename: 2022-09-20_parameters-in-lambda-functions-that-lead-to-xss-and-injection.md
title: Parameters in Lambda Functions that lead to XSS and Injection
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: e00c84ad7c399990413aeff9542747e9f1ddde2dd249ef54890a990a86e76edc
text_sha256: e012423ec8e8a278afb0e4159f4f5e4b7d15ebdc5977595f8857bbcee6fee89b
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Parameters in Lambda Functions that lead to XSS and Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-20_parameters-in-lambda-functions-that-lead-to-xss-and-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `e00c84ad7c399990413aeff9542747e9f1ddde2dd249ef54890a990a86e76edc`
- Text SHA256: `e012423ec8e8a278afb0e4159f4f5e4b7d15ebdc5977595f8857bbcee6fee89b`


## Content

---
title: "Parameters in Lambda Functions that lead to XSS and Injection"
url: "https://medium.com/cloud-security/parameters-in-lambda-functions-that-lead-to-xss-and-injection-1bc8e14fca6f"
authors: ["Teri Radichel (@TeriRadichel)"]
programs: ["AWS"]
bugs: ["XSS", "Serverless"]
publication_date: "2022-09-20"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2142
scraped_via: "browseros"
---

# Parameters in Lambda Functions that lead to XSS and Injection

Member-only story

Parameters in Lambda Functions that lead to XSS and Injection
ACM.56 How I might abuse your Lambda function on a pentest if you don’t properly secure your inputs
Teri Radichel
Follow
9 min read
·
Sep 20, 2022

17

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

⚙️ Part of my series on Automating Cybersecurity Metrics. The Code.

🔒 Related Stories: Git Security | Application Security | Secure Code | AWS Security | Network Security | Lambda Security | Penetration Testing

💻 Free Content on Jobs in Cybersecurity | ✉️ Sign up for the Email List

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the last post, we looked at how to get started with Python an Boto3.

Using Python and Boto3 in AWS
ACM.55 Boto3 in a Lambda Function and later in AWS Batch

medium.com

Before that we looked at automating the deployment of a Lambda function.

Automating a Lambda Function Deployment
ACM.52 Creating a Lambda function to generate a Job ID

medium.com

One of the things we’re gong to need to modify in the Lambda function we just created earlier is the…

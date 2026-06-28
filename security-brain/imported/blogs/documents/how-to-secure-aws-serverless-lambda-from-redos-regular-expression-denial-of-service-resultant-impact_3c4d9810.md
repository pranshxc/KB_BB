---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-14_how-to-secure-aws-serverless-lambda-from-redosregular-expression-denial-of-servi.md
original_filename: 2020-06-14_how-to-secure-aws-serverless-lambda-from-redosregular-expression-denial-of-servi.md
title: How to Secure AWS ServerLess Lambda from ReDoS(Regular Expression Denial-of-Service)
  & Resultant Financial Impact
category: documents
detected_topics:
- rate-limit
- api-security
- cloud-security
- access-control
- command-injection
- race-condition
tags:
- imported
- documents
- rate-limit
- api-security
- cloud-security
- access-control
- command-injection
- race-condition
language: en
raw_sha256: 3c4d9810a247764a0d7a1f08446d4784233524501e7f832d19c6827ac5ef07a6
text_sha256: 2eb2cc95d8924a9fbe592e28a180e5bb93663b9c5448b116e290ad57f49fbe4b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How to Secure AWS ServerLess Lambda from ReDoS(Regular Expression Denial-of-Service) & Resultant Financial Impact

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-14_how-to-secure-aws-serverless-lambda-from-redosregular-expression-denial-of-servi.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, cloud-security, access-control, command-injection, race-condition
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `3c4d9810a247764a0d7a1f08446d4784233524501e7f832d19c6827ac5ef07a6`
- Text SHA256: `2eb2cc95d8924a9fbe592e28a180e5bb93663b9c5448b116e290ad57f49fbe4b`


## Content

---
title: "How to Secure AWS ServerLess Lambda from ReDoS(Regular Expression Denial-of-Service) & Resultant Financial Impact"
url: "https://medium.com/@ddigvijay29/how-to-secure-aws-serverless-lambda-from-redos-regular-expression-denial-of-service-resultant-12f0401118cd"
authors: ["Ddigvijay (@itsdig)"]
bugs: ["ReDoS"]
publication_date: "2020-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4498
scraped_via: "browseros"
---

# How to Secure AWS ServerLess Lambda from ReDoS(Regular Expression Denial-of-Service) & Resultant Financial Impact

How to Secure AWS ServerLess Lambda from ReDoS(Regular Expression Denial-of-Service) & Resultant Financial Impact
Digvijay
Follow
5 min read
·
Jun 14, 2020

3

The serverless paradigm makes it very easy for product development teams to develop and deploy in AWS cloud. Most of the operational responsibilities like configuring machine images (AMIs), patching the OS, installation of daemons to collect log distribution and gathering metrics for your application, are managed by AWS. Developers should be aware of their responsibility to secure the application as the cloud provider does not protect from cyber threats resulting out of vulnerable code.

I discovered a one-step exploitation vulnerability during my BugBounty exercise for an eCommerce company and I am going to share what I found for ReDoS in Lambda servicers. My post will walk you through how to secure your AWS Serverless Lambda against ReDoS attack that can result in AWS charging you for additional (not authorized) Lambda services or services taking additional time beyond your required time limit.

Before going over the exploit, let’s review the basics of Serverless Lambda.

Serverless Lambda — An Overview

Serverless applications run in stateless compute containers that are event-driven, ephemeral (functions as a service), and fully managed by the cloud provider. These applications scale seamlessly and do not require any server operations. The idea is that you can write your application code in the form of functions. When you deploy your function, you then need a way to invoke it in the form of an event.

Press enter or click to view image in full size
Fig-1: Sample Serverless Design

The event could come from some type of API gateway (http request), if invoking the code from a client application, then an event from another serverless function, or an event from another cloud service (like Amazon S3 for example after something is uploaded). Your cloud provider executes the function code on your behalf. The cloud provider also takes care of provisioning and managing the servers to run the code upon invocation.

Know Your Application: Basic Recon

For that eCommerce site, I needed to find out where it was hosted. With basic recon through Burp Suite — I added regular expression in username I was able to get to 503 error. The subsequent response that I got, revealed that it was hosted on S3/AWS.

Press enter or click to view image in full size
Fig-2 Basic Recon Using Burp Suite

After checking the response, I went to S3 bucket and started to look for open S3 bucket issues, I didn’t find any open S3 Bucket issues.

Like any other security researcher, I always start with Application Security OWASP-10 vulnerabilities, business logic issues then other vulnerabilities. In this case, I did not find those vulnerabilities so I looked into OWASP Serverless Top-10 since it was based on AWS Lambda function. I found out that AWS lambda event function was set as a service for auto scaling.

AWS charges per request/sec. The interesting part was that I already performed application DoS and was unaware of the vulnerability, after reading a few articles, I understood about AWS lambda function and issues related to them. One of the issues was application level DoS, which can cause additional charges to an organisation, based on AWS lambda pricing.

By adding regular expression to username, the unintended consequence was that payload resulted in DoS and the service went down, hence the 503 error.

This led me to the summarize that if the exploit was to be automated in a Python script with a number of requests, it will result in ReDoS attack. That attack will end up in big invoice for AWS S3/Lambda services for that eCommerce company.

Press enter or click to view image in full size
Fig-3: AWS Lambda pricing

The critically of the bug that I found is detailed as below

POC:

The endpoint “https://XXX.com/api/signin" is running over AWS as a micro service/lambda service, with automated scalability and high availability and impose some limitations and issues which require attention.
The endpoint “https://XXX.com/api/signin" was found to be vulnerable to a ReDoS (Regular-Expression Denial of Service) attack vector. The vulnerability enables a malicious user to cause each AWS microservice/Lambda function which uses it to stall until it times out.
In the request param “username”:”ANYNAME”” used and adding an extra double quote is extremely inefficient regular expression as per the attack nature.This string(extra double quote), with a simple request body as the one provided below, will cause a 100% CPU utilisation for a very long period of time & get response such as “Service Unavailable along with 503 HTTP”
An attacker may send numerous concurrent malicious requests to an AWS Lambda function i.e. https://XXX.com/api/signin endpoint, until the concurrent executions limit is reached, and in turn, deny other users access to the application.
An attacker may also push the Lambda or microservice function to “over-execute” for long periods of time, essentially inflating the monthly bill and inflicting a financial loss for the target organisation.
Depending on the type of limit and activity, poorly designed or configured applications may be abused in such a way that will eventually cause latency to become unacceptable or even render it unusable for other users.
Press enter or click to view image in full size
Fig-4: Redos in Serverless AWS Lambda function

Mitigation

Get Digvijay’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are several mitigation steps and best practices approaches for dealing with Denial of Service and Denial of Wallet attacks against serverless architectures.

Set alerts for AWS services thresholds through AWS Cost Optimization tool
Writing efficient serverless functions, which perform discrete targeted tasks. More information can be found in the following:
Setting appropriate timeout limits for serverless function execution.
Setting appropriate disk usage limits for serverless functions.
Applying request throttling on API calls.
Enforcing proper access controls to serverless functions.
Use APIs, modules and libraries which are not vulnerable to application.
Ensure that your VPC Lambda subnet has enough IP addresses to scale.
Use short timeouts on API endpoints as a thumb rule in micro services.
Use cached or default responses when downstream cannot respond in a timely fashion
Press enter or click to view image in full size
Fig-5: Rate limit for AWS Lambda

Reference:

https://github.com/OWASP/Serverless-Top-10-Project/blob/master/2018/en/0xSb-other-risks.md
https://medium.com/hackernoon/many-faced-threats-to-serverless-security-519e94d19dba
https://aws.amazon.com/lambda/pricing/#:~:text=The%20monthly%20compute%20price%20is,tier%20provides%20400%2C000%20GB%2Ds.&text=The%20monthly%20request%20price%20is,provides%201M%20requests%20per%20month.
https://blog.paloaltonetworks.com/2020/03/cloud-securing-serverless/

Disclaimer:

The views and opinions expressed in this blog are those of the author and do not represent the opinions of any entity whatsoever with which I have been, am now or will be affiliated.

Authors Bio:

Digvijay Singh, is a Cybersecurity expert who is engaged in vulnerability assessments for various organizations. An avid WhiteHat Ethical Hacker who is always helping enterprise to protect its information systems and data. His expertises include Threat Modelling, Secure Code Review, Security Architecture and Penetration Testing. He is also Security Advisor for Cyberlogue.

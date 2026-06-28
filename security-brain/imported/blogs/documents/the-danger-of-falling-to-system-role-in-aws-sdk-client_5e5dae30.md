---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-18_the-danger-of-falling-to-system-role-in-aws-sdk-client.md
original_filename: 2022-10-18_the-danger-of-falling-to-system-role-in-aws-sdk-client.md
title: The Danger of Falling to System Role in AWS SDK Client
category: documents
detected_topics:
- cloud-security
- sso
- supply-chain
- oauth
- access-control
- ssrf
tags:
- imported
- documents
- cloud-security
- sso
- supply-chain
- oauth
- access-control
- ssrf
language: en
raw_sha256: 5e5dae30d97f66dadb82964e3f99b6841ae5dafed55d5c28fce50988f312af18
text_sha256: b709768acfa3172b716ae1ede0fa346322cb9bea209bc512061edd9100c0aaf7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# The Danger of Falling to System Role in AWS SDK Client

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-18_the-danger-of-falling-to-system-role-in-aws-sdk-client.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, supply-chain, oauth, access-control, ssrf
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `5e5dae30d97f66dadb82964e3f99b6841ae5dafed55d5c28fce50988f312af18`
- Text SHA256: `b709768acfa3172b716ae1ede0fa346322cb9bea209bc512061edd9100c0aaf7`


## Content

---
title: "The Danger of Falling to System Role in AWS SDK Client"
page_title: "The Danger of Falling to System Role in AWS SDK Client · Doyensec's Blog"
url: "https://blog.doyensec.com/2022/10/18/cloudsectidbit-dataimport.html"
final_url: "https://blog.doyensec.com/2022/10/18/cloudsectidbit-dataimport.html"
authors: ["Fracensco Lacerenza (@lacerenza_fra)", "Mohamed Ouad (@ouadmoha)"]
bugs: ["Cloud", "Privilege escalation", "Security misconfiguration"]
publication_date: "2022-10-18"
added_date: "2022-10-22"
source: "pentester.land/writeups.json"
original_index: 2027
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# The Danger of Falling to System Role in AWS SDK Client

18 Oct 2022 - Posted by Francesco Lacerenza, Mohamed Ouad

![CloudsecTidbit](../../../public/images/cloudsectidbit-logo200.png)

## Introduction to the series

When it comes to Cloud Security, the first questions usually asked are:

  * How is the infrastructure configured?
  * Are there any public buckets?
  * Are the VPC networks isolated?
  * Does it use proper IAM settings?

As application security engineers, we think that there are more interesting and context-related questions such as:

  * Which services provided by the cloud vendor are used?
  * Among the used services, which ones are directly integrated within the web platform logic?
  * How is the web application using such services?
  * How are they combined to support the internal logic?
  * Is the usage of services ever exposed or reachable by the end-user?
  * Are there any unintended behaviors caused by cloud services within the web platform?

By answering these questions, **we usually find bugs**.

Today we introduce the “**CloudSecTidbits** ” series to share ideas and knowledge about such questions.

CloudSec Tidbits is a blogpost series showcasing interesting bugs found by Doyensec during cloud security testing activities. We’ll focus on times when the cloud infrastructure is properly configured, but the web application fails to use the services correctly.

Each blogpost will discuss a specific vulnerability resulting from an insecure combination of web and cloud related technologies. Every article will include an [Infrastructure as Code (IaC) laboratory](https://github.com/doyensec/cloudsec-tidbits/) that can be easily deployed to experiment with the described vulnerability.

## Tidbit # 1 - The Danger of Falling to System Role in AWS SDK Client

Amazon Web Services offers a comprehensive SDK to interact with their cloud services.

Let’s first examine how credentials are configured. The AWS SDKs require users to pass access / secret keys in order to authenticate requests to AWS. Credentials can be specified in different ways, depending on the different use cases.

When the AWS client is initialized without directly providing the credential’s source, the AWS SDK acts using a clearly defined logic. The AWS SDK uses a different credential provider chain depending on the base language. The credential provider chain is an ordered list of sources where the AWS SDK will attempt to fetch credentials from. The first provider in the chain that returns credentials without an error will be used.

For example, the SDK for the Go language will use the following chain:

  1. 1) Environment variables
  2. 2) Shared credentials file
  3. 3) If the application uses ECS task definition or RunTask API operation, IAM role for tasks
  4. 4) If the application is running on an Amazon EC2 instance, IAM role for Amazon EC2

The code snippet below shows how the SDK retrieves the first valid credential provider:

Source: [aws-sdk-go/aws/credentials/chain_provider.go](https://github.com/aws/aws-sdk-go/blob/bef02444773a49eaf30cdd615920b56896827c06/aws/credentials/chain_provider.go#L67)
  
  
  // Retrieve returns the credentials value or error if no provider returned
  // without error.
  //
  // If a provider is found it will be cached and any calls to IsExpired()
  // will return the expired state of the cached provider.
  func (c *ChainProvider) Retrieve() (Value, error) {
  var errs []error
  for _, p := range c.Providers {
  creds, err := p.Retrieve()
  if err == nil {
  c.curr = p
  return creds, nil
  }
  errs = append(errs, err)
  }
  c.curr = nil
  
  var err error
  err = ErrNoValidProvidersFoundInChain
  if c.VerboseErrors {
  err = awserr.NewBatchError("NoCredentialProviders", "no valid providers in chain", errs)
  }
  return Value{}, err
  }
  

After that first look at AWS SDK credentials, we can jump straight to the tidbit case.

### Insecure AWS SDK Client Initialization In User Facing Functionalities - The Import From S3 Case

By testing several web platforms, we noticed that data import from external cloud services is an often recurring functionality. For example, some web platforms allow data import from third-party cloud storage services (e.g., AWS S3).

In this specific case, we will focus on a vulnerability identified in a web application that was using the AWS SDK for Go (v1) to implement an “Import Data From S3” functionality.

The user was able to make the platform fetch data from S3 by providing the following inputs:

  * S3 bucket name - Import from public source case;

**OR**

  * S3 bucket name + AWS Credentials - Import from private source case;

The code paths were handled by a function similar to the following structure:
  
  
  func getObjectsList(session *Session, config *aws.Config, bucket_name string){
  
  //initilize or re-initilize the S3 client
  S3svc := s3.New(session, config)
  
  objectsList, err := S3svc.ListObjectsV2(&s3.ListObjectsV2Input{
  Bucket:  bucket_name
  })
  
  return objectsList, err
  }
  
  func importData(req *http.Request) (success bool) {
  
  srcConfig := &aws.Config{
  Region: &config.Config.AWS.Region,
  }
  
  req.ParseForm()
  bucket_name := req.Form.Get("bucket_name")
  accessKey := req.Form.Get("access_key")
  secretKey := req.Form.Get("secret_key")
  region := req.Form.Get("region")
  
  session_init, err := session.NewSession()
  if err != nil {
  return err, nil
  }
  
  aws_config = &aws.Config{
  Region: region,
  }
  
  if len(accessKey) > 0 {
  aws_config.Credentials = credentials.NewStaticCredentials(accessKey, secretKey, "")
  } else {
  aws_config.Credentials = credentials.AnonymousCredentials
  }
  
  objectList, err := getObjectsList(session_init, aws_config, bucket_name)
  
  ...
  

Despite using `credentials.AnonymousCredentials` when the user was not providing keys, the function had an interesting code path when `ListObjectsV2` returned errors:
  
  
  ...
  if err != nil {
  if err, awsError := err.(awserr.Error); awsError {
  aws_config.credentials = nil
  getObjectsList(session_init, aws_config, bucket_name)
  }
  }
  

The error handling was setting `aws_config.credentials = nil` and trying again to list the objects in the bucket.

![](/public/images/cloudsectidbit-fry.png) _Looking at`aws_config.credentials = nil`_

Under those circumstances, the credentials provider chain will be used and eventually the instance’s IAM role will be assumed. In our case, the automatically retrieved credentials had full access to internal S3 buckets.

### The Simple Deduction

If internal S3 bucket names are exposed to the end-user by the platform (e.g., via network traffic), the user can use them as input for the “import from S3” functionality and inspect their content directly in the UI.

![](/public/images/cloudsectidbit-spongebob.jpeg) _Reading internal bucket names list extracted from Burp Suite history_

In fact, it is not uncommon to see internal bucket names in an application’s traffic as they are often used for internal data processing. In conclusion, providing internal bucket names resulted in them being fetched from the import functionality and added to the platform user’s data.

### Different Client Credentials Initialization, Different Outcomes

AWS SDK clients require a `Session` object containing a `Credential` object for the initialization.

Described below are the three main ways to set the credentials needed by the client:

#### NewStaticCredentials

Within the credentials package, the `NewStaticCredentials` function returns a pointer to a new `Credentials` object wrapping static credentials.

Client initialization example with `NewStaticCredentials`:
  
  
  package testing
  
  import (
  "time"
  
  "github.com/aws/aws-sdk-go/aws"
  "github.com/aws/aws-sdk-go/aws/credentials"
  "github.com/aws/aws-sdk-go/aws/session"
  )
  
  var session = session.Must(session.NewSession(&aws.Config{
  Credentials: credentials.NewStaticCredentials("AKIA….", "Secret", "Session"),
  Region:  aws.String("us-east-1"),
  }))
  

Note: The credentials should not be hardcoded in code. Instead retrieve them from a secure vault at runtime.

#### { nil | Unspecified } Credentials Object

If the session client is initialized without specifying a credential object, the credential provider chain will be used. Likewise, if the `Credentials` object is directly initialized to `nil`, the same behavior will occur.

Client initialization example without `Credential` object:
  
  
  svc := s3.New(session.Must(session.NewSession(&aws.Config{
  Region:  aws.String("us-west-2"),
  })))
  

Client initialization example with a `nil` valued `Credential` object:
  
  
  svc := s3.New(session.Must(session.NewSession(&aws.Config{
  Credentials: <nil_object>,
  Region:  aws.String("us-west-2"),
  })))
  

**Outcome** : Both initialization methods will result in relying on the credential provider chain. Hence, the credentials (probably very privileged) retrieved from the chain will be used. As shown in the aforementioned “Import From S3” case study, not being aware of such behavior led to the exfiltration of internal buckets.

#### AnonymousCredentials

The right function for the right tasks ;)

AWS SDK for [Go API Reference](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/#pkg-variables) is here to help:

> “AnonymousCredentials is an empty Credential object that can be used as dummy placeholder credentials for requests that do not need to be signed. This `AnonymousCredentials` object can be used to configure a service not to sign requests when making service API calls. For example, when accessing public S3 buckets.”
  
  
  svc := s3.New(session.Must(session.NewSession(&aws.Config{
  Credentials: credentials.AnonymousCredentials,
  })))
  // Access public S3 buckets.
  

Basically, the `AnonymousCredentials` object is just an empty Credential object:
  
  
  // source: https://github.com/aws/aws-sdk-go/blob/main/aws/credentials/credentials.go#L60
  
  // AnonymousCredentials is an empty Credential object that can be used as
  // dummy placeholder credentials for requests that do not need to be signed.
  //
  // These Credentials can be used to configure a service not to sign requests
  // when making service API calls. For example, when accessing public
  // s3 buckets.
  //
  //  svc := s3.New(session.Must(session.NewSession(&aws.Config{
  //  Credentials: credentials.AnonymousCredentials,
  //  })))
  //  // Access public S3 buckets.
  var AnonymousCredentials = NewStaticCredentials("", "", "")
  

### For cloud security auditors

The vulnerability could be also found in the usage of other AWS services.

While auditing cloud-driven web platforms, look for every code path involving an AWS SDK client initialization.

For every code path answer the following questions:

  1. Is the code path directly reachable from an end-user input point (feature or exposed API)?

_e.g., AWS credentials taken from the user settings page within the platform or a user submits an AWS public resource to have it fetched/modified by the platform._

  2. How are the client’s credentials initialized?

  * credential provider chain - Look for the machine owned role in the chain 
  * Is there a fall-back condition? Look if the end-user can reach that code path with some inputs. If it is used by default, go on \- Look for the role’s permissions
  * `aws.Config` structure as input parameter - Look for the passed role’s permissions
  3. Can users abuse the functionality to make the platform use the privileged credentials on their behalf and point to private resources within the AWS account?

_e.g., “import from S3” functionality abused to import the infrastructure’s private buckets_

### For developers

Use the `AnonymousAWSCredentials` to configure the AWS SDK client when dealing with public resources.

From the official AWS documentations:

> Using anonymous credentials will result in requests not being signed before sending them to the service. Any service that does not accept unsigned requests will return a service exception in this case.

In case of user provided credentials being used to integrate with other cloud services, the platform should avoid implementing fall-back to system role patterns. Ensure that the user provided credentials are correctly set to avoid ending up with `aws.Config.Credentials = nil` because it would result in the client using the credentials provider chain → System role.

## Hands-On IaC Lab

As promised in the series’ introduction, we developed a Terraform (IaC) laboratory to deploy a vulnerable dummy application and play with the vulnerability: <https://github.com/doyensec/cloudsec-tidbits/>

Stay tuned for the next episode!

### Other relevant posts:

  * ###  [ Introducing Session Switcher. Swap Burp Sessions with One Click! 17 Jun 2026 ](/2026/06/17/session-switcher.html)

  * ###  [ Navigating Lax Load Balancers: When an Intersection Gets You Inside 25 May 2026 ](/2026/05/25/cloudsectidbits-elbaph-alb.html)

  * ###  [ The Danger of Multi-SSO AWS Cognito User Pools 05 May 2026 ](/2026/05/05/cloudsectidbits-masso-cognito-sso.html)

  * ###  [ Trivial C# Random Exploitation 19 Aug 2025 ](/2025/08/19/trivial-exploit-on-C-random.html)

  * ###  [ Common OAuth Vulnerabilities 30 Jan 2025 ](/2025/01/30/oauth-common-vulnerabilities.html)

  * ###  [ Applying Security Engineering to Make Phishing Harder - A Case Study 19 Sep 2024 ](/2024/09/19/phishing-case-study.html)

  * ###  [ A Race to the Bottom - Database Transactions Undermining Your AppSec 11 Jul 2024 ](/2024/07/11/database-race-conditions.html)

  * ###  [ Single Sign-On Or Single Point of Failure? 20 Jun 2024 ](/2024/06/20/compromised-idp.html)

  * ###  [ Product Security Audits vs. Bug Bounty 02 May 2024 ](/2024/05/02/products-security-audit-vs-bugbounty.html)

  * ###  [ Messing Around With AWS Batch For Privilege Escalations 13 Jun 2023 ](/2023/06/13/messing-around-with-aws-batch-for-privilege-escalations.html)

  * ###  [ Testing Zero Touch Production Platforms and Safe Proxies 04 May 2023 ](/2023/05/04/testing-ztp-platforms-a-primer.html)

  * ###  [ SSRF Cross Protocol Redirect Bypass 16 Mar 2023 ](/2023/03/16/ssrf-remediation-bypass.html)

  * ###  [ A New Vector For “Dirty” Arbitrary File Write to RCE 28 Feb 2023 ](/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)

  * ###  [ Introducing Proxy Enriched Sequence Diagrams (PESD) 14 Feb 2023 ](/2023/02/14/pesd-extension-public-release.html)

  * ###  [ Tampering User Attributes In AWS Cognito User Pools 24 Jan 2023 ](/2023/01/24/tampering-unrestricted-user-attributes-aws-cognito.html)

  * ###  [ safeurl for Go 13 Dec 2022 ](/2022/12/13/safeurl.html)

  * ###  [ Dependency Confusion 21 Jul 2022 ](/2022/07/21/dependency-confusion.html)

  * ###  [ Apache Pinot SQLi and RCE Cheat Sheet 09 Jun 2022 ](/2022/06/09/apache-pinot-sqli-rce.html)

  * ###  [ Lessons in auditing cryptocurrency wallets, systems, and infrastructures 01 Aug 2019 ](/2019/08/01/common-crypto-bugs.html)

  * ###  [ Jackson gadgets - Anatomy of a vulnerability 22 Jul 2019 ](/2019/07/22/jackson-gadgets.html)

  * ###  [ On insecure zip handling, Rubyzip and Metasploit RCE (CVE-2019-5624) 24 Apr 2019 ](/2019/04/24/rubyzip-bug.html)

  * ###  [ Introducing burp-rest-api v2 05 Nov 2018 ](/2018/11/05/burp-rest-api-v2.html)

  * ###  [ Developing Burp Suite Extensions training 02 Mar 2017 ](/2017/03/02/training-burp.html)

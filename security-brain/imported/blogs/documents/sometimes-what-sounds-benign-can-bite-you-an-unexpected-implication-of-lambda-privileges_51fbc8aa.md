---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-04_sometimes-what-sounds-benign-can-bite-you-an-unexpected-implication-of-lambda-pr.md
original_filename: 2023-07-04_sometimes-what-sounds-benign-can-bite-you-an-unexpected-implication-of-lambda-pr.md
title: 'Sometimes What Sounds Benign Can Bite You: An Unexpected Implication of Lambda
  Privileges'
category: documents
detected_topics:
- cloud-security
- supply-chain
- access-control
- otp
- command-injection
- mfa
tags:
- imported
- documents
- cloud-security
- supply-chain
- access-control
- otp
- command-injection
- mfa
language: en
raw_sha256: 51fbc8aa4138055cbda52ddcf1ada1b15280b6cd12b5492fc5266af9fae2508b
text_sha256: 0c644486bd3c5596b8b4841c68512e8f85272508d9f2194842ec43dd822cf1f1
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Sometimes What Sounds Benign Can Bite You: An Unexpected Implication of Lambda Privileges

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-04_sometimes-what-sounds-benign-can-bite-you-an-unexpected-implication-of-lambda-pr.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, access-control, otp, command-injection, mfa
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `51fbc8aa4138055cbda52ddcf1ada1b15280b6cd12b5492fc5266af9fae2508b`
- Text SHA256: `0c644486bd3c5596b8b4841c68512e8f85272508d9f2194842ec43dd822cf1f1`


## Content

---
title: "Sometimes What Sounds Benign Can Bite You: An Unexpected Implication of Lambda Privileges"
page_title: "An Unexpected Implication of Lambda Privileges - Blog | Tenable®"
url: "https://ermetic.com/blog/aws/sometimes-what-sounds-benign-can-bite-you-an-unexpected-implication-of-lambda-privileges/"
final_url: "https://www.tenable.com/blog/an-unexpected-implication-of-lambda-privileges"
authors: ["Ermetic Team"]
programs: ["AWS"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2023-07-04"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 966
---

#  An Unexpected Implication of Lambda Privileges

[![Team Tenable](/sites/default/files/pictures/2022-04/Profile_Icons_1200x1200-Team-Tenable-circle.png) ]()

By [Team Tenable](/profile/team-tenable)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fan-unexpected-implication-of-lambda-privileges&title=An%20Unexpected%20Implication%20of%20Lambda%20Privileges) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fan-unexpected-implication-of-lambda-privileges&title=An%20Unexpected%20Implication%20of%20Lambda%20Privileges) [ ](https://twitter.com/intent/tweet?urlhttps%3A%2F%2Fwww.tenable.com%2Fblog%2Fan-unexpected-implication-of-lambda-privileges&text=An%20Unexpected%20Implication%20of%20Lambda%20Privileges) Subscribe 

![Tenable Cloud Security](/sites/default/files/images/articles/Blog-Cloud_Banners_4_7.png)

Learn how a combination of AWS service usage and permissions discovered by Tenable Cloud Security may increase risk upon a certain non-compliance.

Tenable Cloud Security researchers recently discovered a specific combination of AWS service usage and permissions that may result in unexpected behavior. The newly unveiled combination could present underlying risk to organizations that have not been meticulous in implementing AWS's Well-Architected Framework. Organizations not in compliance with [SEC01-BP01](https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_securely_operate_multi_accounts.html) (separate workloads using accounts) are at increased risk due to this newly discovered combination.

## TL;DR

AWS Lambda is the Swiss Army knife of the AWS platform. It is used for everything, including building serverless workloads, implementing event-driven tasks and customizing the default behavior of AWS services. In light of this, granting a user the unconstrained permission to update Lambda function code in an AWS account can have unexpected, possibly severe, consequences under certain conditions. These conditions might not be obvious on first pass, particularly to those with less AWS experience. Moreover, it is sometimes not entirely obvious where Lambda might be in use. For example, AWS Amplify uses Lambda under the hood to customize the authentication process of an embedded Amazon Cognito user pool that Amplify employs for user access. In a scenario such as this, granting the permission to update Lambda function code is a very powerful privilege that must be understood.

The purpose of this blog is to educate AWS customers regarding these scenarios and how to use the combination of workload isolation and proper [least privilege to avoid unknowingly introducing underlying risk](https://www.tenable.com/blog/least-privilege-policy-automated-analysis-trumps-native-aws-tools) into their environments.

To demonstrate the possible underlying risk, we will demonstrate abusing this granted permission to modify a provisioned Amplify environment. We chose Amplify specifically because it operates with documented Administrator-equivalent privileges due to its comprehensive nature as a client app development framework and platform.

Since our demonstration requires certain prerequisites to execute – relatively high privileges, a lack of account segregation and a deployed Amplify service – one may be inclined to think this combination poses only marginal risk. In reality, based on our observations, we have found that this particular combination did exist with some frequency within our customer base, which is why we are trying to help educate our customers and the community in general. After educating themselves, organizations should use this knowledge to help implement strict access controls and continuously monitor expected configurations.

## What is AWS Amplify?

AWS Amplify is a development platform that offers web hosting services and helps developers build and deploy full-stack applications in a cloud environment quickly and easily.

One of AWS Amplify’s main features is Amplify Studio, which behaves as the heart of the service. It is a web-based development environment that provides a visual interface for managing data, UI, storage and many functionalities in the user’s web applications on AWS.

![](/sites/default/files/inline/images/image7_3.png)  
_AWS Amplify Studio_

## Technical analysis

Upon inspecting Amplify Studio settings, we infer that we are able to invite external users to our studio and manage team access.

![](/sites/default/files/inline/images/image5_5.png)  
_Amplify Studio - Access control settings_

We appear to have no users in our access control settings. Let’s go straight to trying to launch the studio from the AWS console. We access the “Storage” section which, behind the scenes, sends a request to list all our S3 buckets.

![](/sites/default/files/inline/images/image2_9.png)  
_Request to list S3 buckets inspected in the developer tools_

### Rewinding back to the authentication mechanism

It turns out that behind the scenes, for authentication purposes, Amplify Studio has created Cognito user pools and identity pools, added the Amplify admin user to a “Full Access” group and attached an [IAM role](https://www.tenable.com/blog/taking-notice-of-aws-iam-roles-anywhere) “region-userpoolid-Full access” to it.

![](/sites/default/files/inline/images/image4_8.png)  
_Access control for groups through Cognito user pools_

After a quick check, we see this role has a managed policy attached called “AdministratorAccess-Amplify”.

The AdministratorAccess-Amplify managed policy has many permissions, ranging from

PassRole: * to sts:AssumeRole: *. In fact, [AWS documentation](https://docs.aws.amazon.com/amplify/latest/userguide/security-iam-awsmanpol.html) states: “This [Amplify’s managed policy] allows permissions escalation and this policy should be considered as powerful as the AdministratorAccess policy.”

### Unexpected implications of lambda:UpdateFunctionCode === Administrator

AWS Cognito has several authentication mechanisms a user can implement. One such mechanism is “Custom Authentication,” which we found AWS Amplify uses when orchestrating Cognito within the account. Using custom Lambda triggers, Amplify has configured Cognito to authenticate the user based on a one-time code challenge.

If we follow the underlying configuration a bit further, we find a sequence of Lambda functions that implement the authentication flow.

By diving into the code, we see that token generation by the Lambda function “login-define-auth” is decided by several requirements satisfied by an internal Lambda event. The function then sets a boolean to issue access tokens for the user. In other words, this Lambda function logic controls the authentication flow to the system.

![Amplify-login-define Lambda trigger for Cognito](/sites/default/files/inline/images/image3_6.png)  
_Amplify-login-define Lambda trigger for Cognito_

This brings us back to the original point. If another authorized user within this AWS account has excessive permissions, specifically the ability to update the code of this Lambda function, they can alter or even nullify the authentication logic in any way they please. To demonstrate this point, simply changing the logic from “false” to “true” disables the intended OTP challenge. Should a user perform this alteration, subsequent invocations of the Amplify Studio login process will execute this new code, which could result in unauthorized access to the Amplify Studio environment for the user with “lambda:UpdateFunctionCode” permissions.

## Conclusion

There are two key takeaways from this post. First, while it might sound benign, the variety of ways in which AWS Lambda can be used often makes the AWS permission “lambda:UpdateFunctionCode” a highly privileged operation. This permission should be properly restricted according to the principle of least privilege. As this is often a necessary permission for developers, pay particular attention to the resource element of your [IAM policies](https://www.tenable.com/blog/diving-deeply-into-iam-policy-evaluation-highlights-from-aws-reinforce-iam433) when granting this permission and avoid overly broad scoping, such as resource: * , which would give developers both the ability to update the function code of their own functions, and any other functions that might exist within the same AWS account. Second, use AWS account boundaries to isolate teams and workloads within your overall AWS environment. For Amplify in particular, we recommend that you don’t commingle Amplify and non-Amplify projects within a single AWS account because the Lambda functions provisioned by Amplify govern access to documented full administrative privileges.

In discussing our research with us, AWS agreed with this conclusion and has made account isolation for Amplify an explicit best practice.

## How Tenable Cloud Security can help

The [Tenable Cloud Security](https://www.tenable.com/cloud-security/products/cloud-native-application-protection-platform) platform offers holistic protection for AWS, Azure and Google Cloud and helps organizations keep their cloud environment secure and compliant. The solution provides deep visibility, [risk insight and remediation](https://www.tenable.com/solution-briefs/tenable-for-cloud-risk-prevention-and-remediation) for complex, multi-cloud deployments. It enables effective management of all cloud identities to ensure identities have only the necessary permissions, including justified temporary elevated access, and recommends right-sized permissions to ensure a least-privileged environment. Among other capabilities, the platform detects underlying risks in your environment due to excessive permissions, including those you might not fully appreciate.

By using Tenable Cloud Security you can remove these risks before they manifest themselves – securing your environment and improving your cloud security posture overall.

![Tenable Cloud Security detects and remediates underlying risks -- including permissions-related risks such as privilege escalation -- in AWS and multi-cloud environments](/sites/default/files/inline/images/image6_3.png)  
_Tenable Cloud Security detects and remediates underlying risks -- including permissions-related risks such as privilege escalation -- in AWS and multi-cloud environments_

## Author

## Learn more

[![Team Tenable](/sites/default/files/pictures/2022-04/Profile_Icons_1200x1200-Team-Tenable-circle.png) ]()

### [Team Tenable](/profile/team-tenable)

Array 

[Read more](/profile/team-tenable)

## Learn more

## Related articles

Research

![Download pumping: New npm deception technique for supply chain attacks image](/sites/default/files/images/articles/Download%20pumping%20is%20a%20new%20npm%20deception%20technique%20for%20supply%20chain%20attacks.png)

May 28 2026

#### Download pumping: New npm deception technique for supply chain attacks

By [Ron Popov](/profile/ron-popov)

[ ](/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts)

Cyber Exposure Alerts

![Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI… image](/sites/default/files/images/articles/Mini%20Shai-Hulud.png)

May 21 2026

#### Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI…

By [Research Special Operations](/profile/research-special-operations)

[ ](/blog/mini-shai-hulud-frequently-asked-questions)

AI Security

![Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud… image](/sites/default/files/images/articles/How%20agentic%20AI%20for%20cybersecurity%20helps%20you%20rid%20your%20cloud%20of%20forgotten%2C%20risky%20assets.png)

May 14 2026

#### Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud…

By [Brinton Taylor](/profile/brinton-taylor)

[ ](/blog/agentic-ai-cloud-security-zombie-assets)

  * Cloud

  * Tenable Cloud Security

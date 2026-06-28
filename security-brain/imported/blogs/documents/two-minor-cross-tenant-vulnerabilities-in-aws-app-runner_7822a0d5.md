---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-03_two-minor-cross-tenant-vulnerabilities-in-aws-app-runner.md
original_filename: 2023-04-03_two-minor-cross-tenant-vulnerabilities-in-aws-app-runner.md
title: Two Minor Cross-Tenant Vulnerabilities in AWS App Runner
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 7822a0d5020adcc987ed6d60d1fb18f264f5cfd602d1ebd3176aeae27da1e355
text_sha256: 64665d2963800203ef1532736dbe9967793f9e8f63fde68fed0e76bbb3d70f20
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Two Minor Cross-Tenant Vulnerabilities in AWS App Runner

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-03_two-minor-cross-tenant-vulnerabilities-in-aws-app-runner.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `7822a0d5020adcc987ed6d60d1fb18f264f5cfd602d1ebd3176aeae27da1e355`
- Text SHA256: `64665d2963800203ef1532736dbe9967793f9e8f63fde68fed0e76bbb3d70f20`


## Content

---
title: "Two Minor Cross-Tenant Vulnerabilities in AWS App Runner"
url: "https://frichetten.com/blog/minor-cross-tenant-vulns-app-runner/"
final_url: "https://frichetten.com/blog/minor-cross-tenant-vulns-app-runner/"
authors: ["Nick Frichette (@frichette_n)"]
programs: ["AWS"]
bugs: ["Cross-tenant vulnerability", "Cloud"]
publication_date: "2023-04-03"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1308
---

[Mastodon](https://fosstodon.org/@frichetten)

[![](/images/favicon.ico) Nick Frichette](/)

  * [Home](/)
  * [Blog](/blog/)
  * [Contact Me](/contact/)
  * [RSS](/rss/)
  * [GitHub](https://github.com/frichetten)
  * [Bluesky](https://bsky.app/profile/frichetten.com)
  * [Mastodon](https://fosstodon.org/web/@frichetten)
  * [LinkedIn](https://www.linkedin.com/in/nick-frichette/)
  * [Twitter](https://twitter.com/frichette_n)

  

  
  

# Two Minor Cross-Tenant Vulnerabilities in AWS App Runner

###### April 3, 2023

This is part 2 in a [series](https://frichetten.com/blog/undocumented-amplify-api-leak-account-id/) of blog posts about a research project I am conducting in my free time on undocumented AWS APIs and their security impacts.

As a part of this research, I found two minor cross-tenant vulnerabilities in [AWS App Runner](https://aws.amazon.com/apprunner/). These vulnerabilities leaked configuration information across tenant boundaries. While they are both minor issues, they further demonstrate that undocumented AWS APIs have lacked the scrutiny of AWS as well as the cloud security community. If you’d like to see a more impactful cross-tenant vulnerability, check out my [previous work](https://securitylabs.datadoghq.com/articles/appsync-vulnerability-disclosure/).

This information has been shared with AWS who has since remediated both issues.

## Timeline

  * February 28, 2023: I contacted AWS with technical details of the vulnerabilities.
  * February 28, 2023: AWS responded that they received my report.
  * March 2, 2023: AWS confirmed that fixes were in development for both issues.
  * March 13, 2023: AWS deployed fixes for both issues.
  * April 3, 2023: The disclosure is made public.

Please note: The disclosure was delayed on my part so as not to conflict with [other](https://securitylabs.datadoghq.com/articles/bypass-cloudtrail-aws-service-catalog-and-other/) research.

## Vulnerability Context

  * The two API actions `apprunner:ListVpcConnectorsForAccount` and `apprunner:ListObservability​ConfigurationsForAccount` took an AWS account ID as a parameter.
  * These APIs did not validate that the provided account ID was the same account ID of the calling identity, allowing an adversary to provide ANY account ID and retrieve the information. AWS does not [consider](https://www.lastweekinaws.com/blog/are-aws-account-ids-sensitive-information/) account IDs to be sensitive, and they may be identified or leaked through a number of means. As a result, it is reasonable to assume an adversary could find an account ID of a target organization or business.
  * The information that could be leaked included the security group ID, subnet ID, and VPC connector ARN for each VPC connector, as well as the observability configurations.

## apprunner:ListVpc​ConnectorsForAccount

While hunting for undocumented APIs in the AWS Console I eventually stumbled into AWS App Runner. [App Runner](https://aws.amazon.com/apprunner/) is a managed container service that automatically builds, deploys, and scales container workloads. It simplifies and speeds up the process of deploying applications in containers, removing the need to manage infrastructure or worry about scaling.

While poking around, I found reference to the following action as a part of the AWS App Runner service definition.
  
  
  "ListVpcConnectorsForAccount": {
  "internalonly": true,
  "output": {
  "shape": "S5s"
  },
  "input": {
  "type": "structure",
  "members": {
  "AccountId": {},
  "NextToken": {},
  "MaxResults": {
  "type": "integer"
  }
  }
  }
  }

This stood out for two reasons, one, it had an `internalonly` attribute which piqued my interest. And two, the `members` section (which describes the parameters to send) relied on an `AccountId` being passed in. What happens if I provide an account ID that I don’t own?

As you can guess based on the fact that I’m writing a blog post about this, the API did not check if the entity calling the action belonged to the account ID that was passed as a parameter. As a result, you could invoke this action and provide ANY account ID.

![ListVpcConnectorsForAccount](/images/blog/minor-cross-tenant-vulns-app-runner/1.png)

In the image above you can see that I was able to list VPC Connectors for the account starting with `009` even though I was invoking it with the account starting with `068`. This would leak the security group ID, subnet ID, and VPC connector ARN cross-tenant.

## apprunner:ListObservability​ConfigurationsForAccount

In a very similar story to the previous finding, I also noticed this App Runner API action.
  
  
  "ListObservabilityConfigurationsForAccount": {
  "internalonly": true,
  "output": {
  "shape": "S4v"
  },
  "input": {
  "type": "structure",
  "members": {
  "AccountId": {},
  "NextToken": {},
  "MaxResults": {
  "type": "integer"
  }
  }
  }
  }

Again it had the `internalonly` attribute and only required an `AccountId` as a parameter. Again, the API did not validate the calling identity’s account ID, so I could provide any to it as shown below.

![ListObservabilityConfigurationsForAccount](/images/blog/minor-cross-tenant-vulns-app-runner/2.png)

This leaked the observability configuration ARN cross-tenant.

## Impact and Conclusion

The impact of these specific vulnerabilities are minor, only leaking non-critical information across tenant boundaries about security groups, subnet IDs, and their observability configurations.

What I think is more interesting about these findings is that they show that cross-tenant access control is down to checks on individual APIs by each of the AWS service teams. As a result, It is safe to say there are likely many more APIs which behave this way that have not been scrutinized by AWS or the cloud security community.

I’m excited to share more of my research project soon! Thank you for reading.

## Acknowledgments

Thank you to [Christophe Tafani-Dereeper](https://twitter.com/christophetd) for proof-reading this disclosure and to Ryan S/AWS Security Outreach Team for their assistance.

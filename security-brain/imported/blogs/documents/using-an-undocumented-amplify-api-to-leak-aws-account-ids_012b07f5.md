---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-27_using-an-undocumented-amplify-api-to-leak-aws-account-ids.md
original_filename: 2023-03-27_using-an-undocumented-amplify-api-to-leak-aws-account-ids.md
title: Using an Undocumented Amplify API to Leak AWS Account IDs
category: documents
detected_topics:
- cloud-security
- rate-limit
- sso
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- cloud-security
- rate-limit
- sso
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: 012b07f50fd58452b5438c318f796773a03092306ca958341e3051bbc6879161
text_sha256: 4ac4b9ea8d85429b1dd630c57778652a69bddee2ee9d930f90dd4bfab9948702
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Using an Undocumented Amplify API to Leak AWS Account IDs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-27_using-an-undocumented-amplify-api-to-leak-aws-account-ids.md
- Source Type: markdown
- Detected Topics: cloud-security, rate-limit, sso, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `012b07f50fd58452b5438c318f796773a03092306ca958341e3051bbc6879161`
- Text SHA256: `4ac4b9ea8d85429b1dd630c57778652a69bddee2ee9d930f90dd4bfab9948702`


## Content

---
title: "Using an Undocumented Amplify API to Leak AWS Account IDs"
url: "https://frichetten.com/blog/undocumented-amplify-api-leak-account-id/"
final_url: "https://frichetten.com/blog/undocumented-amplify-api-leak-account-id/"
authors: ["Nick Frichette (@frichette_n)"]
programs: ["AWS"]
bugs: ["Cloud", "Information disclosure"]
publication_date: "2023-03-27"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1336
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

  

  
  

# Using an Undocumented Amplify API to Leak AWS Account IDs

###### March 27, 2023

In a previous [blog post](https://frichetten.com/blog/aws-api-protocols/) I mentioned that I was getting back into AWS vulnerability research in my free time. I’ve been taking a closer look at undocumented AWS APIs, trying to find hidden functionality that may be useful for an attacker or cross tenant boundaries.

While I’m not quite ready to share my findings, tooling, and methodology for this publicly, I did want to share an undocumented, “internalonly”, API I discovered that leaked the AWS account ID associated with an Amplify app, as well as its CloudFront domain under certain configurations. This could have potentially been used by attackers to gain valuable information about AWS accounts, making it easier for them to target specific organizations or launch more sophisticated attacks.

I reported this API to AWS who responded that it did not “represent a security issue”, however, 3 days later, the API was disabled. In this post we will cover how I found this API, how I could use it to leak account IDs associated with an Amplify app and its CloudFront domain, and AWS’s response to it.

Please note; This is not a vulnerability (although I do describe potential risks of an adversary knowing your account ID below). There are a number of ways that an account ID can be found or leaked through normal operation. Instead, this post is an exploration of undocumented APIs and some interesting functionality you may find there.

Prior to the API being disabled, I created a tool to take advantage of it. It can be found [here](https://github.com/Frichetten/appID-2-acctID).

## Timeline

  * March 13th, 2023: I disclosed the API to AWS.
  * March 14th, 2023: AWS confirmed receipt of the report.
  * March 21st, 2023: AWS responded that it does not represent a security issue.
  * March 24th, 2023: AWS disabled the API.
  * March 27th, 2023: This post is made public.

## amplify:GetDistributionDetails

At a high level, I’ve been looking across all AWS services for undocumented APIs. This search brought me to [AWS Amplify](https://aws.amazon.com/amplify/), which is a popular service that makes it easy to quickly spin up full-stack web and mobile applications.

While hunting around in Amplify I stumbled into `amplify:GetDistributionDetails`. Its service definition is below.
  
  
  "GetDistributionDetails": {
  "internalonly": true,
  "output": {
  "type": "structure",
  "members": {
  "awsAccountId": {},
  "appId": {}
  }
  },
  "input": {
  "type": "structure",
  "required": [
  "cloudFrontDomain"
  ],
  "members": {
  "cloudFrontDomain": {
  "locationName": "cloudFrontDomain",
  "location": "uri"
  }
  }
  },
  "http": {
  "method": "GET",
  "requestUri": "/internal/distribution/{cloudFrontDomain}"
  }
  }

There were a few parts of this model that were interesting. The first was the `internalonly` attribute, which seemingly implied that this API should be internal only and not customer facing (spoiler alert: This was not the case).

The second interesting part was the inputs and outputs. This API took a `cloudFrontDomain` as an input and returned an `awsAccountId` as an output. This raised an interesting question, if I provide any [CloudFront](https://aws.amazon.com/cloudfront/) domain, will it return the AWS account ID associated with it?

## Testing This Out

To see what I could do with this API, I selected one AWS account as the “target” account, and another as the “attacker” account. I would invoke the API from the attacker account while specifying parameters for the target account to see if this could be used cross-tenant.

To get started, I created a CloudFront distribution in the target account, and tried to use `amplify:GetDistributionDetails` to see if it returned the AWS account ID.

![Showing a CloudFront distribution](/images/blog/undocumented-amplify-api-leak-account-id/1.png)

(For the folks at home, the tool is adding `.cloudfront.net` to the provided ID)

Okay, so not ANY CloudFront domain it seemed. What if we went at this from another angle? Since this was an Amplify API, it made sense that it could have something to do with Amplify. Looking through the [documentation](https://docs.amplify.aws/cli/hosting/hosting/#stages) it appears that indeed, you can use CloudFront to serve an Amplify application.

So I created an Amplify app and followed the documentation to host it on CloudFront.

![Failed with the Amplify CloudFront app](/images/blog/undocumented-amplify-api-leak-account-id/2.png)

Again, no dice, with a weird error. It was at this point that I was starting to lose hope. Perhaps there was something going on that I didn’t understand? If I provided gibberish I would get a new error further validating that the API was looking for a CloudFront domain.

![CloudFront domain invalid error](/images/blog/undocumented-amplify-api-leak-account-id/3.png)

While going through the console, I took somewhat of a wild guess. Amplify IDs look remarkably similar to the prefix of a CloudFront domain. They both begin with the letter `d` and are both 14 characters long. Were Amplify App IDs the missing link?

![Success!](/images/blog/undocumented-amplify-api-leak-account-id/4.png)

That worked! By sending `<Amplify app ID>.cloudfront.net` to this undocumented API, I could retrieve the associated AWS account ID!! And, again, I was invoking this cross-tenant; from another account meaning that I could seemingly provide any Amplify app ID and get the AWS account ID back for it.

I could not find a good explanation as to why the API would respond to `<Amplify app ID>.cloudfront.net`. If you create an Amplify app and host it with CloudFront, there are two different IDs, so it’s not a situation where a single identifier applies to both. It seems strange that internally it appears that the Amplify app ID is directly tied to a CloudFront domain.

## Finding More App IDs

The next question became, how hard would it be to find these IDs? As it turns out, not difficult at all. By default, they are a part of the URL to access the app.

![Default Amplify app domain](/images/blog/undocumented-amplify-api-leak-account-id/5.png)

By going to Google we can search for `site:amplifyapp.com` and see that we get over twenty-two thousand results!

![Google results for amplifyapp.com](/images/blog/undocumented-amplify-api-leak-account-id/6.png)

It was at this point that I started trying some of these results and things got a little weird. Almost none of them were working. After being stumped for a bit I realized that this was likely because of the [region](https://twitter.com/Frichette_n/status/1638682506785439750?s=20). My script was only being run against us-east-1. After adding in functionality for multiple regions, I could consistently determine the AWS account ID of any Amplify app ID.

For some examples, `https://master.d30jf5gj5vctl9.amplifyapp.com/`:

![Example 1](/images/blog/undocumented-amplify-api-leak-account-id/7.png)

And `https://master.d10wksxjz5w1jv.amplifyapp.com/`:

![Example 2](/images/blog/undocumented-amplify-api-leak-account-id/8.png)

Note: I’ve redacted the full AWS account ID as a courtesy. These examples were only selected because they were at the top of the Google search results.

## Back to CloudFront Domains

It was at this time that I tried a different approach with the CloudFront domains. Let’s look at the previous example which had an Amplify app ID of `d10wksxjz5w1jv`. This website belongs to a company called Omnieyes, which has a primary domain of `www.theomnieyes.com`. We can use a tool like [MXToolBox](https://mxtoolbox.com/SuperTool.aspx?action=a%3awww.theomnieyes.com&run=toolpage) to get CNAME records associated with the domain. This will give us a CloudFront domain that we can look up with the undocumented API.

![MXToolBox site](/images/blog/undocumented-amplify-api-leak-account-id/9.png)

![Showing CloudFront to account ID](/images/blog/undocumented-amplify-api-leak-account-id/10.png)

This represented a more generalized method for leaking the account ID for Amplify apps which used a custom domain.

It is not clear to me why I was unable to use a CloudFront domain I generated with the API. I presume there is an additional configuration or something else required but I was unable to find it before the API was shut down.

## AWS’s Response

I was a little on the fence about whether or not I should report this to the AWS security team. On the one hand, it was concerning that there was an undocumented, “internalonly” API, that would spit out the account ID of any Amplify app. In addition, there didn’t appear to be a way to opt-out of this since the domain would need to be public information.

On the other hand, AWS had previously stated that [they do not consider account IDs to be sensitive](https://www.lastweekinaws.com/blog/are-aws-account-ids-sensitive-information/). As a result, I was confident they would side with their aforementioned stance, consider it a non-issue, and that would be it.

In the end, I figured it would be better to report it. After some time to investigate, I received the following back from AWS, “I wanted to let you know that we’ve completed our investigation into what you’ve reported and determined that it does not represent a security issue”.

Although AWS has stated that account IDs are not sensitive information, I still had some concerns about this issue.

## Assessing the Risk

To be clear, this was not a major vulnerability. This was not something to get up-in-arms about or panic over. However, there was some attack surface to consider.

First, if you could leak the Account ID of any Amplify app, this would have served as excellent phishing material. Imagine getting an email from `[[email protected]](/cdn-cgi/l/email-protection)` saying, “Hey there! We see you’re using Amplify in account 000000000000!….”. Knowing something about an account that theoretically only the account holder and Amazon should know may be enough to trick someone into falling for a phish.

Second, with an account ID an adversary can do things like [enumerating roles and users](https://hackingthe.cloud/aws/enumeration/enum_iam_user_role/) cross account. This would give an attacker an idea of the services in use in the account, as well as provide them additional reconnaissance. Additionally, firms such as [Unit 42](https://unit42.paloaltonetworks.com/iam-roles-compromised-workloads/) have seen [wildcard principals](https://docs.datadoghq.com/security/default_rules/aws-iam-role-trust-policy-wildcard-principal/) in use in IAM trust policies. By being able to selectively target individual organizations, it is easier for an attacker to try these types of long-shot attacks as a part of a larger campaign.

Third, in the event that a cross-tenant 0day vulnerability is found, adversaries now have a quick way to tie an organization to a specific account ID. What would otherwise take some level of sleuthing and enumeration is now a simple Python script away.

If we were to compare this with other techniques, this has some similarities to the technique discovered by [Ben Bridts](https://twitter.com/benbridts) to [enumerate AWS account IDs from public S3 buckets](https://hackingthe.cloud/aws/enumeration/account_id_from_s3_bucket/). However, I think it’s important to recognize the differences as well. In particular, the S3 bucket method involves abusing the `s3:ResourceAccount` condition key. You brute force various account IDs using `*` until you succeed. For example, `1*`, `2*`, `21*`, etc.

Abusing a condition key is a clever technique that takes advantage of the normal functionality to leak the account ID. If you want to enable someone to compare against an account ID, and you want to support `*` as a valid option in that value, then being able to brute force an S3 bucket account ID is a natural conclusion to that. AWS seems to have decided that was a reasonable tradeoff in exchange for that functionality (which it may be).

By comparison, this was a random undocumented API that takes a piece of public information and returns an account ID. There is no clever trick here. I understood why AWS considered it to not be a security issue, but was also a bit surprised that it seemed they weren’t going to fix it.

## The Fix

While working on this blog post and gathering screenshots, I noticed that the API….stopped working. It started responding with just “null”. As it turned out, I must have been working during the rollout of the fix as I could see which regions were still functioning, and which regions were updated.

![Watching the API be disabled](/images/blog/undocumented-amplify-api-leak-account-id/11.png)

20 minutes later:

![Watching the API be disabled part 2](/images/blog/undocumented-amplify-api-leak-account-id/12.png)

For all the reasons I called out in the previous section I’m glad that AWS has disabled the API, preventing an adversary from abusing this in the future. It was surprising to see the API disabled (something AWS is famous for [not doing](https://www.lastweekinaws.com/blog/awss-deprecation-policy-is-like-a-platypus/)) after being told it was not considered a security issue. I’ll chalk it up to a miscommunication, someone changing their mind, or perhaps not enough time to communicate the decision. It is also possible that the API was no longer intended to be used and AWS decided to remove it.

## Conclusion

In this blog post I shared an undocumented API I found that leaked the AWS account ID of an Amplify App, using its domain name. It has been disabled by AWS, preventing future abuse.

This research (and more coming soon) sheds light on the risks and capabilities of undocumented APIs, and how they can potentially be abused to retrieve information cross-account.

I’m excited to share more of my research project soon! Thank you for reading.

## Acknowledgements

Thank you to Alexis Fahrney and the AWS Security Outreach Team for their assistance.

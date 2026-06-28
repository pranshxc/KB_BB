---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-22_no_wildcard-how-i-discovered-the-organization-id-of-any-aws-account.md
original_filename: 2024-07-22_no_wildcard-how-i-discovered-the-organization-id-of-any-aws-account.md
title: 'NO_WILDCARD: How I discovered the Organization ID of any AWS Account'
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 512dfddb26597f45dd855468c7044cfe5f600ba9e3832caf0d363f79af602081
text_sha256: 68c28150192f739c97e712b351d4891b51a974029ab41fe2dc6a4715d0f46af4
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# NO_WILDCARD: How I discovered the Organization ID of any AWS Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-22_no_wildcard-how-i-discovered-the-organization-id-of-any-aws-account.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `512dfddb26597f45dd855468c7044cfe5f600ba9e3832caf0d363f79af602081`
- Text SHA256: `68c28150192f739c97e712b351d4891b51a974029ab41fe2dc6a4715d0f46af4`


## Content

---
title: "NO_WILDCARD: How I discovered the Organization ID of any AWS Account"
page_title: "NO_WILDCARD: How I discovered the Organization ID of any AWS Account | Tracebit"
url: "https://tracebit.com/blog/no-wildcard-how-i-discovered-the-organization-id-of-any-aws-account"
final_url: "https://tracebit.com/blog/no-wildcard-how-i-discovered-the-organization-id-of-any-aws-account"
authors: ["Sam Cox"]
programs: ["AWS"]
bugs: ["Information disclosure", "Cloud"]
publication_date: "2024-07-22"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 148
---

[All posts](/blog)

·

[Research](/blog)

# NO_WILDCARD: How I discovered the Organization ID of any AWS Account

![](https://cdn.prod.website-files.com/664246e98a546954e1135e70/6655c0d1ee275c73b3430424_team_sam-cox.avif)

Sam Cox

July 22, 2024

April 8, 2026

·

10

min read

I am the text that will be copied.

![Diagram showing VPC Endpoint Policies being used to find Organization ID of an arbitrary AWS account](https://cdn.prod.website-files.com/664246e98a546954e1135e70/6957ac688e3d113e2affd60a_669e745d177265c04e5a36b8_Frame%2025%20\(1\).webp)

When I published [how to find the AWS Account ID of any S3 bucket](https://tracebit.com/blog/how-to-find-the-aws-account-id-of-any-s3-bucket) earlier in the year, I felt like I had just scratched the surface of a general technique which might yield even more interesting results with a bit more research. However, building Tracebit keeps me quite busy so I had to put security research on the back burner for a little while!

While preparing notes for my [fwd:cloudsec](https://tracebit.com/blog/fwd-cloudsec-talk-on-s3-bucket-research) talk though, it seemed like there were too many big questions that I wanted to answer for myself and for the audience so I decided to dig deeper. In the process, I made a new finding which led to AWS introducing significant changes to VPC Endpoint behavior.

It seems the fun is now over for information discovery using VPC endpoints!

#### What’s this about VPC Endpoint policies?

For the full details, see the [previous post](https://tracebit.com/blog/how-to-find-the-aws-account-id-of-any-s3-bucket) \- I won’t go over it all again here. Essentially, you could determine the aws:ResourceAccount condition key (i.e. the account ID) by iteratively testing wildcards in S3 VPC Endpoint Policies, while abusing the fact that S3 VPC Endpoint policy denials don’t get logged to CloudTrail.

#### Why don’t VPC Endpoint policy denials get logged to CloudTrail?

VPC Endpoints are a crucial component when implementing a Data Perimeter within AWS. My understanding is that VPC Endpoint Policy denials are not logged to CloudTrail to prevent CloudTrail from being used as a data exfiltration mechanism.

Consider a VPC which has been heavily locked down with no internet access, with a VPC Endpoint Policy restricting access to S3 so that _only_ IAM Principals from the “correct” account can access S3 and only then for a specific bucket:
  
  
  {
  "Effect": "Allow",
  "Action": "*",
  "Resource": "arn:aws:s3:::my-bucket",
  "Principal": "*",
  "Condition": {
  "StringEquals": {
  "aws:PrincipalAccount": "111111111111",
  "aws:ResourceAccount": "111111111111"
  }
  }
  }

The S3 bucket may also be restricted via a Resource Policy to only be accessible via this VPC Endpoint.

If an attacker gains access to the VPC and credentials permitting them access to the S3 bucket, they will still struggle to exfiltrate data without access to the internet. Their access to S3 itself will be restricted by the VPC Endpoint policy to the specific bucket in question, so they can’t just copy data to their own bucket.

One potential avenue for exfiltration might however be CloudTrail. If an attacker brings their own credentials into the VPC, they could make requests to S3 using those credentials. These would of course be denied by the VPC Endpoint Policy, but if the details of the requests were to be logged to the requester’s CloudTrail then data could be exfiltrated via e.g. the user agent used to make the request itself. I think this is why CloudTrail does not log VPC endpoint policy denials:

![S3 does not support delivery of CloudTrail logs to the requester or the bucket owner for VPC endpoint requests when the VPC endpoint policy denies them](https://cdn.prod.website-files.com/664246e98a546954e1135e70/669e3d6c4d5b74f9351317db_AD_4nXe1P7zRRhzPfhwSPRtihOvDzEaVBGLHLYwlujwN6CjgTwVCllQCe-xbuaOeGfkJUVn5C6gWGj5DFUrTsQWjWBlxZCLMf6zQ-xkwuJxR-uztiMDJwX9Qin7C6AikYe9SzB8gP0MrazmuqohueeRQCqqlQRKq.avif)

#### What about services other than S3?

Unlike S3, most services do not create resources in a globally shared namespace. The account ID in which they live is an explicit part of the [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) \- no prizes for guessing which account this resource lives in:
  
  
  arn:aws:dynamodb:us-east-1:123456789012:table/myTable

There are however a number of different [resource context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) we might want to discover about a resource using the same technique, for instance:

![](https://cdn.prod.website-files.com/664246e98a546954e1135e70/669e56c74858a008bcb04be2_AD_4nXczvhoMsdQNjdS-2NN1pTQgjrLEbgefEeNYnM61NPE0UodCnVja4wuU3OpLhESdjNKs4PlstHHosDg7Vhygy5hd16ffWcEEDAm22u3HIwC4rnuVqSJurUElHeXrnbq0xyRMn7uOCgPbSZEnIQmupn07flhH.avif)

This felt like a fairly straightforward extension of the original technique though. It took me a little longer than expected to get a reliable configuration for arbitrary AWS services (other than S3) and by the time I’d done so I had quite a definite aim in mind:

I wanted to find a way to discover the AWS Organization ID of an arbitrary third-party AWS account.

#### The fun begins - the hunt for the Organization ID

An [AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) allows for the centralized management of a number of AWS accounts. Each AWS Organization has an identifier - the Organization ID - that takes the form o-a1b2c3d4e5. What’s significant about this is that even if an org is diligent in segmenting its workloads into different AWS accounts, they likely all fall under one (or a very small number of) AWS Organization for billing and management purposes. It might be powerful to correlate accounts as being associated to the same org without authorization!

We can ask AWS for a list of Endpoint services which support VPC Endpoint Policies to get a list of possibilities - at the time of writing there were 242 such services:
  
  
  $ aws ec2 describe-vpc-endpoint-services \
  --filters Name=service-type,Values=Interface \
  Name=owner,Values=amazon \
  --region us-east-1 \
  --output text \
  --query \
  'ServiceDetails[?VpcEndpointPolicySupported==`true`].[ServiceName]'
  
  aws.api.us-east-1.bcm-data-exports
  aws.api.us-east-1.freetier
  aws.api.us-east-1.kendra-ranking
  aws.api.us-east-1.qbusiness
  aws.sagemaker.us-east-1.notebook
  …
  com.amazonaws.us-east-1.vpc-lattice
  com.amazonaws.us-east-1.wisdom
  com.amazonaws.us-east-1.workflows-omics
  com.amazonaws.us-east-1.workspaces
  com.amazonaws.us-east-1.xray

With so many services, I needed to narrow my focus. For the technique to work in general, I had to be able to make a cross-account call to a resource (whether this is permitted or not). For instance AWS Polly supports a VPC Endpoint Policy, but from looking at each of the [API actions](https://docs.aws.amazon.com/polly/latest/dg/API_Operations.html) there doesn’t seem to be any way to reference a resource in another account.

![Only some AWS services support Resource-based policies](https://cdn.prod.website-files.com/664246e98a546954e1135e70/669e5739433afc5a71b00401_AD_4nXfaKOSTuLGoftpMxQ__sPg8FFZB9x7IeaNQM_5dwEclZxogajQDSgPinaAvMrblbtXhZBWL5QGW__8oDuQfx7xLi3PQZYMWA8T5gZoybaCloFwgSXN0HkHiKLMuQatM4_bHrvxHPkNprSD5BtiwPD4Y6H-d.avif)

I used the list of [AWS Services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html#all_svcs) to identify those that support Resource-based policies as a reasonable starting point for those services which were likely to support some type of cross-account access. This certainly misses some services - for instance EBS snapshots support cross-account access though not via resource policies - but it seemed like a good starting place. What remained were around 25 services, including popular ones such as DynamoDB, Lambda, SQS etc.

## Default resources

It’s not just enough to have a service though - we need a resource to target! For the S3 case - by assumption - we already had a resource of interest (an S3 Bucket). When all we know is an Account ID however, it’s not clear which resources we should make requests to. At this stage I just started going through services with the aim of finding “predictable resources”. For instance, if I’m targeting account 123456789012 then there’s a pretty reasonable chance that the following resource exists which I could use as the target of my requests:
  
  
  arn:aws:iam::123456789012:role/aws-service-role/
  organizations.amazonaws.com/AWSServiceRoleForOrganizations

Similarly it’s possible - but a lot less likely - that this resource exists:
  
  
  arn:aws:ecr:us-east-1:123456789012:repository/ubuntu

However, there was one resource in particular that I quickly focussed on:
  
  
  arn:aws:events:us-east-1:123456789012:event-bus/default

That is, the [Default EventBridge Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html#eb-bus-concepts-buses). This has some interesting properties:

  * It exists in every account (in every region)
  * It [cannot be deleted](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-delete.html)
  * It has an entirely deterministic ARN, which differs only in the account ID segment

This is exactly what I needed! I set to work creating a VPC Endpoint for EventBridge with a policy which would let me discover the Organization ID of an arbitrary Event Bus (that is, of an arbitrary account!) by send a request with a different role session name for each possibility:
  
  
  {
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*",
  "Principal": "*",
  "Condition": {
  "StringLike": {
  "aws:userid": "*:a---------",
  "aws:ResourceOrgId": "o-a?????????"
  }
  }
  },
  {
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*",
  "Principal": "*",
  "Condition": {
  "StringLike": {
  "aws:userid": "*:b---------",
  "aws:ResourceOrgId": "o-b?????????"
  }
  }
  },
  . . .
  {
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*",
  "Principal": "*",
  "Condition": {
  "StringLike": {
  "aws:userid": "*:---------9",
  "aws:ResourceOrgId": "o-?????????9"
  }
  }
  }

The requests that passed the VPC Endpoint policy and subsequently appeared in CloudTrail would then reveal the aws:ResourceOrgId!

![](https://cdn.prod.website-files.com/664246e98a546954e1135e70/669e6f0825b3887f7f972bd8_vpc-endpoints-eventbridge.avif)

This was a bit more complex than the technique for discovering an S3 bucket owner as there are many more possible Organization IDs than Account IDs. The maximum size of a [VPC Endpoint Policy](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) meant I needed to split the possibilities between three separate VPC Endpoints and make sure I sent each request to the correct one. I quickly adapted my [previous code](https://github.com/tracebit-com/find-s3-account) and gave it a try:
  
  
  Finding session names which passed the VPC endpoint in CloudTrail...
  Found ---------5 for 123456789012:event-bus/default in CloudTrail
  Found --------e- for 123456789012:event-bus/default in CloudTrail
  Found ------d--- for 123456789012:event-bus/default in CloudTrail
  Found ----c----- for 123456789012:event-bus/default in CloudTrail
  Found ---2------ for 123456789012:event-bus/default in CloudTrail
  Found a--------- for 123456789012:event-bus/default in CloudTrail
  Found -------4-- for 123456789012:event-bus/default in CloudTrail
  Found -----3---- for 123456789012:event-bus/default in CloudTrail
  Found --b------- for 123456789012:event-bus/default in CloudTrail
  Found -1-------- for 123456789012:event-bus/default in CloudTrail
  Account 123456789012 has Organization ID: o-a1b2c3d4e5

This was capable of discovering the AWS Organization ID of _any_ AWS account within 5 minutes, and there’s nothing the target account could do to prevent it!

#### Impact

I think this presented some pretty interesting possibilities for correlating AWS Accounts as belonging to the same AWS Organization. It could be pretty powerful to be able to definitively confirm or deny that an account is associated with a given AWS Organization. I would imagine many organizations have some sandbox accounts they’d rather third parties couldn’t associate with them!

To give just another example: at Tracebit we deploy AWS Canary Credentials at scale on behalf of our customers, and one particularly concerning use case that I’d [previously identified](https://tracebit.com/blog/deploying-effective-canary-aws-credentials) was to be able to determine that some AWS credentials belong to a particular AWS Organization without using the credentials at all. This could make certain AWS Canary Credentials much less effective. Imagine how much more powerful the technique described [here](https://trufflesecurity.com/blog/canaries) would be if it required only a single Organization ID rather than a potentially stale or incomplete list of Account IDs.

#### Disclosure & Fix

As soon as I discovered this new technique I reported it to AWS Security (the finding was also reported to a vendor offering AWS Canary Credentials who could have been particularly affected).

AWS indicated that they intended to fix this, and ultimately made quite significant changes intended to prevent this new technique, my previous S3 technique, as well as any obvious variants from being created.

AWS have now made a change which prevents wildcards from being used in several locations in a VPC Endpoint policy. Consulting the [documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policy-considerations) for VPC Endpoint policies today, there are some new additions:

  * You can't use wildcard characters (* or ?) or numeric condition operators with global context keys that reference system-generated identifiers (for example, aws:PrincipalAccount or aws:SourceVpc).
  * When you use a string condition operator, you must use at least six consecutive characters before you include a wildcard character.
  * When you specify an ARN in a resource or condition element, the account portion of the ARN can include an account ID or a wild card, but not both.

In practice what this means is if you try to create such a policy today you’ll get a brand new NO_WILDCARD error message:

![An error message indicating that condition key aws:ResourceOrgId with value o-??????z??? is at risk of NO_WILDCARD](https://cdn.prod.website-files.com/664246e98a546954e1135e70/669e58a0a8fca409a6b50af9_AD_4nXckqGzuOK2vuw__BT1q2rpqDoJHMz7TbVn5d5ltvuCdSOlBjpyXQRW8qMyGXykF-1dC652gVwINbjoQ5CJBr9B9C3_3io3P3aIUwdnE3zcFNP6fjbu3-444gVr5HAC_6SQ5_X4Cj-QXdXIGDi6vUjfP08Ud.avif)

This was effectively the change I anticipated during my talk. One aspect that’s quite intriguing is that a wildcard is still permitted after 6 consecutive characters. I wonder if there is some obscure reason to continue to support that?

I feel like there’s quite a lot of awareness of the [Default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html), but before this research I hadn’t given much thought to which other default resources might exist in an AWS account - I’d be interested if anyone has collected a list together?

I was impressed with the speed with which AWS made changes here - four weeks from finding to fix:

  * **4 June** \- Finding reported to AWS security
  * **12 June** \- AWS indicated changes were underway (and that I shouldn’t attempt a live demo at fwd:cloudsec!)
  * **2 July** \- AWS confirmed the IAM team were rolling out the NO_WILDCARD change - by this point it seemed to already have been deployed to the entire aws partition
  * **12 July** \- AWS confirmed documentation had been updated

I’m not sure if this finding was considered more significant than the previous finding about S3. There’s certainly something interesting to the fact that there was no possible mitigation. Perhaps this was just the straw that broke the camel’s back as it demonstrated the wider application of the technique.

#### Thanks

In preparing this post I was very grateful for the advice of [Nick Frichette](https://twitter.com/Frichette_n) and [Rami McCarthy](https://twitter.com/ramimacisabird).

‍

Table of contents

Subscribe to our newsletter

Subscribe to receive the latest research and product updates to your inbox every week.

By subscribing you agree to our [privacy policy](/legal/privacy-policy)

Thank you! Check your inbox for your first edition.

Oops! Something went wrong while submitting the form.

Subscribe to newsletter

Subscribe to receive the latest research and product updates to your inbox every week.

By subscribing you agree to with our [Privacy Policy.](/legal/privacy-policy)

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

## The latest security research straight to your inbox

Subscribe to our newsletter to receive regular updates from our research and product teams

By subscribing you agree to our [privacy policy](/legal/privacy-policy)

Thank you! Check your inbox for your first edition.

Oops! Something went wrong while submitting the form.

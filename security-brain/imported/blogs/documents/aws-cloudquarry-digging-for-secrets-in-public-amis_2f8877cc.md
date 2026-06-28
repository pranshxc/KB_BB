---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-08_aws-cloudquarry-digging-for-secrets-in-public-amis.md
original_filename: 2024-05-08_aws-cloudquarry-digging-for-secrets-in-public-amis.md
title: 'AWS CloudQuarry: Digging For Secrets In Public AMIs'
category: documents
detected_topics:
- cloud-security
- sso
- jwt
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- cloud-security
- sso
- jwt
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 2f8877cc7a44766065d2ff004895a9f1a6aa2b312105bc63c023ce51d27edffb
text_sha256: 2be6304bf4a133fb02a689b8c3ecaccab4b18e69b3a3db553e82182bac2a303c
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: true
---

# AWS CloudQuarry: Digging For Secrets In Public AMIs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-08_aws-cloudquarry-digging-for-secrets-in-public-amis.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, jwt, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: True
- Raw SHA256: `2f8877cc7a44766065d2ff004895a9f1a6aa2b312105bc63c023ce51d27edffb`
- Text SHA256: `2be6304bf4a133fb02a689b8c3ecaccab4b18e69b3a3db553e82182bac2a303c`


## Content

---
title: "AWS CloudQuarry: Digging For Secrets In Public AMIs"
page_title: "AWS CloudQuarry: Digging for Secrets in Public AMIs – Security Café"
url: "https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/"
final_url: "https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/"
authors: ["Eduard Agavriloae (@saw_your_packet)", "Matei Josephs"]
programs: ["AWS"]
bugs: ["Information disclosure"]
publication_date: "2024-05-08"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 299
---

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/479d564d-512e-430f-898c-382c8c0331fd.jpeg?fit=840%2C840&ssl=1)

# AWS CloudQuarry: Digging for Secrets in Public AMIs

[May 8, 2024](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/ "9:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Research](https://securitycafe.ro/category/research/) [2 comments](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#comments)

Money, secrets and mass exploitation: This research unveils a quarry of sensitive data stored in public AMIs. Digging through each AMI we managed to collect 500 GB of credentials, private repositories, access keys and more. The present article is the detailed analysis of how we did it and what the data represents.

We did a coordinated disclosure with AWS’s security team before publishing this article.

Researchers and article authors:

  * Eduard Agavriloae (<https://www.linkedin.com/in/eduard-k-agavriloae/>, [@saw_your_packet](https://twitter.com/saw_your_packet))
  * Matei Josephs (<https://www.linkedin.com/in/matei-anthony-josephs-325ba5199/>)

## Before you begin

The results and methodology of this research could have been presented in a short summary along with 1-2 diagrams. However, we decided to go for a lengthy article that will describe our methodology, our thinking, trade-offs and results.

We invite you to challenge our approach and find aspects that we missed out or could have been improved. You can contact us through our LinkedIn profiles, through the comment section or through the Security Cafe media channels that you can find in the Contact page.

## TABLE OF CONTENTS

  1. [Introduction](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-introduction)
  1. [Some words from AWS security team](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-1-some-words-from-aws-security-team)
  2. [Research Idea – Origins](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-1-research-idea-origins)
  3. [Relevant Details About AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-2-relevant-details-about-amis)
  4. [Previous Work](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-3-previous-work)
  5. [Rules & Objectives](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-4-rules-objectives)
  2. [Collecting all Public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#2-collecting-all-public-amis)
  3. [Processing the Collected AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-processing-the-collected-amis)
  1. [Making sense of what we have](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-1-making-sense-of-what-we-have)
  2. [Filtering out AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-filtering-out-amis)
  1. [AMIs from Marketplace](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-1-amis-from-marketplace)
  2. [AMIs owned by AWS](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-3-amis-owned-by-aws)
  3. [AMIs with RootDeviceType set to “instance-store”](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-3-amis-with-rootdevicetype-set-to-instance-store)
  4. [Owners with more than 50 Public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-4-owners-with-more-than-50-public-amis)
  5. [Sanity Checks](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-5-sanity-checks)
  4. [Accessing the AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-accessing-the-amis)
  1. [Failed Options](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-1-failed-options)
  * [Option 1](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-1)
  * [Option 2](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-2)
  * [Option 3](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-3)
  2. [Working method](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-2-working-method)
  3. [Architecture for scale scanning](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-3-architecture-for-scale-scanning)
  4. [Final considerations](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-4-final-considerations)
  5. [Digging for secrets](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-digging-for-secrets)
  1. [Mounting](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-1-mounting)
  2. [Finding secrets](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-2-finding-secrets)
  3. [Looking through private Git repositories](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-3-looking-through-private-git-repositories)
  6. [Results](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-results)
  1. [AWS Keys](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-1-aws-keys)
  2. [Secrets extracted from Git repositories](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-2-secrets-extracted-from-git-repositories)
  3. [Secrets from config files](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-3-secrets-from-config-files)
  7. [Impact](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-impact)
  8. [Responsible disclosure](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-responsible-disclosure)
  1. [Owners of AWS access keys](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-1-owners-of-***REDACTED-AWS-KEY***s)
  * [Working with AWS’s security team](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-1-1-working-with-aws-s-security-team)
  2. [Other keys](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-2-other-keys)
  9. [Stories worth telling](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-stories-worth-telling)
  1. [GitLab Personal Access Token](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-1-gitlab-personal-access-token)
  2. [Stripe API key](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-2-stripe-api-key)
  3. [Sales meeting, but with a twist](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-3-sales-meeting-but-with-a-twist)
  4. [The amazing AWS Security Team](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#9-4-the-amazing-aws-security-team)
  10. [Future work & Ethical considerations](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#9-future-work-ethical-considerations)
  1. [Ethical considerations](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#9-1-ethical-considerations)
  2. [Future work](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#9-2-future-work)
  11. [Conclusions](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#conclusions)

## 1\. Introduction

### 1.1 Some words from AWS security team

Note that AWS-owned AMIs are not affected by this issue and no customer action is required for those AMIs.

Part of publishing AMIs is indeed publishing something public and customers should take care to inspect them prior to publishing so that they know what is in fact being published. As a best practice, AMI creators should not include credentials, including AWS account credentials, in published AMIs.

For more information about crafting secure, shareable AMIs, recommendations can be found here:

  * <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/building-shared-amis.html>
  * <https://docs.aws.amazon.com/marketplace/latest/userguide/best-practices-for-building-your-amis.html>
  * <https://docs.aws.amazon.com/marketplace/latest/userguide/product-submission.html>

We also recommend customers use AMIs owned and published by AWS, or by another Amazon verified provider. For more information about verified providers, review “Verified provider” in the User Guide for Linux Instances. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html#verified-ami-provider>

### 1.2 Research Idea – Origins

Some time ago I was doing a typical cloud security configuration review for a client. While checking for misconfigurations in the EC2 dashboard, I saw for the first time not one, but many public AMIs.

But what is an AMI? Well, AMI stands for Amazon Machine Image and if it’s the first time you hear about them that doesn’t mean you haven’t used one before. You see, every time you launch an EC2 instance, that instance is always based on an AMI.

And to put it simply, an AMI is like a preconfigured virtual machine. Imagine you want to start an instance that has a certain database technology already installed and ready to go. Chances are that someone already configured such an instance and then made that instance an AMI so that others can use it.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image.png?resize=840%2C460&ssl=1)EC2 Launch Instance – Dashboard select AMI

But most likely you used a common Amazon Linux AMI from the AWS Marketplace. These AMIs are from verified publishers. They are, in a sense, official AMIs. And then you have the Community AMIs, which are AMIs published by anyone and verified by none.

To come back to my story, this client had multiple public AMIs that anyone could have found and used to start an EC2 instance based on that image. Essentially, anyone on the internet could have gained access to whatever files, secrets, credentials, code the client configured at some point and published “accidentally” (we’ll talk later about those quotes).

When I asked the client if I can check what was inside the AMIs, they said no 😐. After finishing the engagement I was left with a question: Did they accidentally expose sensitive data all these years through these AMIs? And this gave birth to a second, bigger question: Are there other companies exposing sensitive data through public AMIs?

While I didn’t have the chance to get an answer for the first question, I knew I could answer the second one. So, with the help of my colleague Matei Josephs, we aimed to answer with this research if “**Are there any public AMIs with sensitive data out there?** “.

### 1.3 Relevant Details About AMIs

First off, AMIs are dependent on their region. An AMI made public (published) in eu-central-1 will not be available in us-west-2 or any other region for that matter. This means that you have to specify the proper region if you want to access a particular AMI.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-1.png?resize=840%2C548&ssl=1)Example AMI response from AWS API

The second thing is that AMIs are by default created as private and it’s actually hard to make it public. You have to disable a setting at the account level, wait 10 minutes, go to the AMI you want to make public and when you try to make it public you have to type “confirm” in a pop-up that tells you the implied security risks. That’s why I said the AMIs are published “accidentally” with quotes, because as far as I can tell, there is no accident in doing with; maybe just lack of awareness.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-2.png?resize=840%2C201&ssl=1)Deprecation details from <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html>

The third thing is that AMIs can be deprecated. Let’s look at the images above. Apart from the highlighted fields, we have on the last line a property called “DeprecationTime”. AMIs can become deprecated. As a user, you can deprecate your AMIs whenever you want. And if you don’t, AWS will automatically deprecate your image after two years from its creation. This behavior was introduced in 2021 and its result is that deprecated images will not be accessible from the web console anymore. However, you can still use and query deprecated AMIs. You just have to use the CLI for that.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-3.png?resize=840%2C211&ssl=1)CLI options for “ec2 describe-images” regarding deprecation

### 1.4 Previous Work

Dolev Farhi did something similar as us, but Dolev scanned AMIs from a single AWS region and only based on certain keywords: <https://blog.lethalbit.com/hunting-for-sensitive-data-in-public-amazon-images-ami/>

We wanted to scan all public AMIs, so our work completes Dolev’s by covering the other 26+ AWS regions and the AMIs from Dolev’s region that we’re left out

Ben Morris did a research close to what we are doing. He scanned public EBS volumes for secrets as he presented in his talk at DEF CON 27: <https://www.youtube.com/watch?v=HXM1rBk_wXs>

While in theory we are scanning the AMI’s volumes, in our case the EBS volume is not public by default just because the AMI is public. So there is very little overlap (we estimate under 5%) between his research and ours.

Having this said, we believe that our research gives a more complete view into this issue that was almost not explored from an offensive perspective at large scale.

### 1.5 Rules & Objectives

We set out some rules from the beginning. The most important one, act in an ethical manner. Practically, this research didn’t involve any hacking or breaking into systems. It only relied on data publicly available and set out by companies or individuals. However, we felt that acting ethically should be always on our mind.

We also established a few objectives:

  1. Dig for secrets in every public AMI across every AWS region
  2. Have Fun
  3. Responsible Disclosure

So we wanted to find out if there are secrets exposed in public AMIs by searching through all of them, have fun while doing it and responsible disclose to issue to the affected companies if it’s the case.

Let’s get into it!

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/pexels-photo-2252311-edited-1.jpeg?resize=575%2C431&ssl=1)Photo by Laura Stanley on [Pexels.com](https://www.pexels.com/photo/dog-lying-on-shore-during-day-2252311/)

## 2\. Collecting all Public AMIs

First off, we enabled all AWS regions inside our AWS account. This was an easy process that didn’t cost anything.

Now: the command for retrieving all public AMIs from a region is fairly simple:
  
  
  # this will work for most regions with a default page size of 1000
  aws ec2 describe-images --include-deprecated --region $region > $region.json
  
  # set a smaller page size if you get timeout errors
  aws ec2 describe-images --include-deprecated --region $region --page-size 200 > $region.json

We knew this would be a challenging research when we had to wait a few hours to get all the public AMIs. Collecting the AMIs from every AWS region resulted in 11 GB of data 😂

This was the point where we decided to give a name to the research and create a private repository. In Romanian we have this expression of “digging for something” when you search for something. And while our objective was to dig for secrets in every public AMI, it simply clicked for us. That’s how we got to the whole “CloudQuarry” and “digging” thing.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/ae95aede-cbb8-4c3d-b942-a1732094b40d.jpeg?resize=840%2C840&ssl=1)CloudQuarry image generated by DALL·E 3

We transformed the 11 GB into 750 MB of archives which we uploaded in our repository.

## 3\. Processing the Collected AMIs

### 3.1 Making sense of what we have

We got a total of 3.1 million public AMIs. This number represents all the public AMIs from 27 AWS region (now there are more regions in AWS) available in December 2023 (more on the new public AMIs from that date at the end of the article).

Here are the statistics per region, ordered by count, at the start of the research:
  
  
  us-east-1: 203,864
  us-west-2: 183,509
  eu-west-1: 171,196
  us-west-1: 170,634
  ap-southeast-1: 164,231
  ap-northeast-1: 163,020
  ap-southeast-2: 162,493
  eu-central-1: 161,535
  sa-east-1: 156,402
  us-east-2: 147,191
  ap-northeast-2: 142,417
  eu-west-2: 141,971
  ap-south-1: 141,404
  ca-central-1: 137,669
  eu-west-3: 131,319
  eu-north-1: 120,526
  ap-east-1: 104,742
  me-south-1: 100,369
  eu-south-1: 96,996
  af-south-1: 93,072
  ap-southeast-3: 61,353
  me-central-1: 44,236
  eu-central-2: 41,351
  eu-south-2: 40,912
  ap-south-2: 37,096
  ap-southeast-4: 34,652
  il-central-1: 19,072
  Total images: 3,173,232

Now we faced a new question: is there any point in scanning all 3.1 million AMIs? We decided to further analyze the data to answer this. So we ran some python scripts to check things like how many unique owners are and top 10 AWS accounts with AMIs from each region. You can find the stats in the next file:

[top-10-owners.txt](https://securitycafe.ro/wp-content/uploads/2024/04/top-10-owners.txt)

Just looking at the data above we can see that there are a few AWS accounts with tens of thousands of AMIs. We can do some google dorking on them to check who is the company behind them, but the idea is that most likely these big accounts are commercial publishers and if they are commercial publishers then the chances to have valid secrets in them are really low.

At this point we felt the need of a more easier way to analyze the data, so we moved it to MongoDB.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-4.png?resize=840%2C386&ssl=1)MongoDB Compass local instance

Using the Schema feature from MongoDB Compass we gained more insight into what was going on. For example, we saw that from a sample of 1000 random AMIs, 41% of them are owned by a single AWS account. That’s over 1 million AMIs if extrapolated.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-5.png?resize=840%2C298&ssl=1)MongoDB Compass Schema analysis

### 3.2 Filtering out AMIs

#### 3.2.1 AMIs from Marketplace

We decided that we can filter out AMIs based on some common sense conditions. The most obvious one was to filter out AMIs that are from the AWS Marketplace. The rationale behind this is that AMIs from marketplace are used on a daily basis by anyone. So, the chances to find valid secrets are small. Even more, these AMIs are from official and verified providers that are intentionally publish in the AWS Marketplace. We assume that they should be aware of what they publish and they most likely will not include sensitive information in their AMIs.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-6.png?resize=507%2C369&ssl=1)JSON Property for AMIs from AWS Marketplace

We saw that the AMIs published in AWS Marketplace have an additional property that is not present for the community AMIs: **ProductCodes**

To make our life easier, when we added the AMIs in MongoDB, we replaced the “ProductCodes” field with a custom property called “IsInMarketplace”.
  
  
  def initialize_collection(amis_collection):
  for region in regions:
  amis = get_amis_for_region(region)
  for ami in amis:
  ami['Region'] = region
  ami['IsInMarketplace'] = 'ProductCodes' in ami.keys()
  ami['IsRootInstanceCoreType'] = ami['RootDeviceType'] == 'instance-store'
  amis_collection.insert_one(ami)
  print(f"[x] Finished for region {region}")

Doing this, we managed to filter out 1.6 million AMIs, reducing the total number from 3.1 million to 1.5 million AMIs. In the next file is the new count for each region:

[amis-numbers-marketplace-filter.txt](https://securitycafe.ro/wp-content/uploads/2024/04/amis-numbers-marketplace-filter.txt)

Along the next chapters we’ll build a MongoDB query that will filter all the necessary AMIs. This is how it looks for now:
  
  
  {IsInMarketplace: false}

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-7.png?resize=840%2C184&ssl=1)MongoDB Compass filter AMIs from AWS Marketplace

#### 3.2.3 AMIs owned by AWS

Analyzing the fields available for the remaining AMIs, we noticed that there was only one value for the field **ImageOwnerAlias** , and that value was “amazon”.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-8.png?resize=381%2C219&ssl=1)AMI owned by AWS

So the AMIs owned by AWS can be identified through property with the value “amazon”. Well, we again assumed that there is no point in searching for secrets in AWS owned AMIs. In the end, they know better. While that might not be the case, we assumed the best and decided to filter them out.

MongoDB query filter:
  
  
  {IsInMarketplace:false, ImageOwnerAlias: {$not:{$eq:"amazon"}}}

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-9.png?resize=840%2C246&ssl=1)MongoDB Compass filter AMIs owned by AWS

Hey! Look at that! We got the number down to 1 million AMIs. While our objective was not to reduce the number of AMIs, but rather to construct a list of high potential targets, seeing a more feasible number of AMIs gives us the hope that we can scan all the AMIs worth scanning.

#### 3.2.3 AMIs with RootDeviceType set to “instance-store”

Doing some tests we noticed that we can’t start or access AMIs that have the property **RootDeviceType** set to “instance-store”. These types of AMIs have the next characteristic:

> Amazon instance store-backed AMI – The root device for an instance launched from the AMI is an instance store volume created from a template stored in Amazon S3.
> 
> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>

So we can’t access these AMIs without the source from the S3 bucket. We decided to not scan these AMIs since we don’t know where the root device is stored and since we won’t have access most likely to that root device.

Again, we did the same thing when adding the AMIs in MongoDB, we changed the “RootDeviceType” property with a new field called “IsRootInstanceCoreType”. Now that I look back, I can see that the name should have been “IsRootInstance**Store** Type”, but let’s leave it as it is.
  
  
  def initialize_collection(amis_collection):
  for region in regions:
  amis = get_amis_for_region(region)
  for ami in amis:
  ami['Region'] = region
  ami['IsInMarketplace'] = 'ProductCodes' in ami.keys()
  ami['IsRootInstanceCoreType'] = ami['RootDeviceType'] == 'instance-store'
  amis_collection.insert_one(ami)
  print(f"[x] Finished for region {region}")

MongoDB query filter:
  
  
  {IsInMarketplace:false, ImageOwnerAlias: {$not:{$eq:"amazon"}}, IsRootInstanceCoreType:false}

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-11.png?resize=840%2C247&ssl=1)MongoDB Compass filter AMIs with RootDeviceType set to “instance-store”

We only removed about 5k instances with this filter, but we managed to get below 1 million AMIs. The next filter however is the big game changer.

#### 3.2.4 Owners with more than 50 Public AMIs

Analyzing the remaining sample of AMIs, we noticed that we still have some AWS account with a large number of public AMIs.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-13.png?resize=840%2C347&ssl=1)MongoDB Compass analysis based on OwnerId

Checking the owners with the most AMIs we noticed that they are some kind of unofficial vendors, publishing new versions of their AMIs. Well, this is good, but how can we determine which account is some sort of vendor and which is not?

We were looking for a threshold. Something like, if a single AWS account owns more than X AMIs, then that AWS account is likely to be an unofficial vendor and we can exclude it. In the search of that threshold, we checked how many unique AWS accounts are out there with a maximum number of 25 public AMIs. Similarly, we did the same check for a maximum number of 20, 15, 10, 5 and 1. The next file contains the results:

[amis-per-aws-account.txt](https://securitycafe.ro/wp-content/uploads/2024/04/amis-per-aws-account.txt)

Looking at this data we saw that numbers between the checked thresholds are fairly close. We factored in another thing. We assumed that no one is crazy enough to have more than 2 public AMIs on each AWS region. And imagine this: an AWS account has more than 50 public AMIs unintentionally left out there with source code, secrets, keys and so on. It felt like simply too much.

So, we introduced what I felt to be the first trade-off. We set this threshold of maximum 50 public AMIs per AWS account. Even after almost half a year later, I still think this was a good call. Doing some scripting in Python we identified those accounts with more than 50 AMIs. You can find the list in the MangoDB filter query below:
  
  
  {
  IsInMarketplace: false,
  IsRootInstanceCoreType: false,
  ImageOwnerAlias: {$not:{$eq:"amazon"}},
  OwnerId: 
  {
  $nin: [
  "979382823631","125523088429","782774275127","085178109370","462397596885","504405067906","782442783595","575461648593","281784684473","126027368216","958347557273","531415883065","357466774442","118940168514","172840064832","364390758643","108329106114","161831738826","958145178466","258751437250","138312800438","939706979954","211372476111","992587258474","099720109477","281784684473","679593333241","953345546836","014677528312","531533671159","275272412307","150196106750","692314432491","297478128798","609069431582","659279834602","304251891748","074754820263","082051669340","083837402522","240152784131","012284807008","833371238208","781110569745","852100819133","666044672026","040921035827","641549025415","602111481490","470264848403","164326021446","263721492972","677635134310","604437731932","651188399649","117403053999","273419675927","909031101827","675738832863","973501904202","078680276960","101072000470","601427279990","847205733218","033737991781","867686887310","515116089304","253213882263","922711891673","107025636812","144433228153","361870911536","981484854994","981586224937","341718127296","012177264511","506463145083","343299325021","798920643433","672242615610","193273892879","088819544517","619681448102","955366579413","213396452403","833997227572","696905082017","481432522479","633059600857","298058684257","872251088935","558211695259","717539892973","761449685630","458419666758","117936542248","262744063927","156597721064","700366075446","228847291132","929637706107","375021575472","221210582303","221354433967","811078382625","604384805766","747514752573","268367799918","002243364032","903897969027","391477561959","634922670793","691173103445","121773538331","894535543691","167422901596","897883143566","808508158480","178480506716","961113262821","128329325849","649294524699","799597332240","857032533038","701511253276","902347396780","342470128466","063491364108","056126556840","823218754427","622992712626","776682305951","524466471676","522179138863","066803512886","332551323846","623002322076","005923036815","725085649209","159375186019","830106197091","055761336000","153434714329","805912557329","231994803134","785895325085","664284451649","643366669028","120340763379","860900021006","811682917860","030444862968","734147683238","314270375726","743288062907","411745053086","920152662742","113073460856","511242591283","158855661827","003483243915","107042026245","308029823110","222958650704","489483686436","275994140148","212021838531","879268495141","208491357083","666882590071","226465381217","062844181125","703926772882","940762080936","872909225683","085996170456","266183714499","023992783472","812481205477","644630763931","766915741798","922761411349","958621391921","471211731895","567502172578","517062167202","576481180806","422652172681","233757773908","753722448458","930457884660","220197662125","858280671036","413071817000","754685078599","260760892802","919814621061","370050660245","672550935748","988443417517","174203920225","959243851260","391847209875","654897662046","261542671292","514734236355","787223699828","079972220921","879742242852","455864098378","092722883498","187515304745","354643243794","020679151690","641886270455","367134611783","529661837159","769790836554","354613140921","398653132559","609594173164","679090434138","143320424681","887485515065","943353741583","745719312218","514117492693","072157914504","963121779227","657159205431","999867407951","160082703681","302634334388","153242070384","492681118881","646472328658","441566271543","223093067001","568608671756","811737349733","670387110090","614612213257","012067661104","183081753049","555854959998","372903911592","931685398798","711772050517","397995763618","626107101308","188439194153","328217207599","303519801974","297975325230","488931611485","013230744746","125035497591","331174399982","275898483189","732123782549","636156223522","210811600188","835705546860","902696655598","381009627173","887450378614","505803097751","121695370940","159737981378","465267886299","034389035875","055279482367","502976614458","851065383862","843529240033","481155165509","542040705575","009967377517","105532983076","077742499581","263245908434","887764444972","049929217248","705482507833","883755651572","036086565681","400392161012","674059360964","174003430611","108494951140","491925185505","178579023202","689494258501","966122790603","324146450368","648710915214","687241535879","042423532529","299934467172","772315742791","582244788873","084912087861","601277729239","210686502322","456531263183","142421590066","410186602215","253379484728","942344369036","090003032930","390302536420","694121914657","344758251446","733078701466","746013851261","273854932432","608014515287","900854079004","919239153674","388963328112","463018831373","760937637931","511311637224","897878824798","887664104594","687725076918","813909747961","141318035583","068287425771","317307795746","948542851936","105571261999","034360980390","001382923476","054713022081","861068367966","558986605633","541621974560","478299826944","873237481665","865636555390","154239132089","709601304699","579393713941","833372943033","625240141681","701759196663","699717368611","704708324783","130167558768","270051122755","415789037893","235279919161","893612263489","098706035825","560348900601","549196663111","635144173025","971246865984","764336703387","904411313395","801328867837","227120241369","371522382791","816268476753","247716482002","142548018081","817633883686","578985338881","649843420731","617935088040","328669466519","160390125595","320704736504","701208020788","995913728426","312594956781","022044324644","582547558294","155889952199","346947735772","428641199958","675552985074","849201093595","080433136561","511657745411","148102829632","044893506424","434481986642","838367653738","000692753149","216958472421","233975207881","007561666938","895523100917","466085125143","821543836110","763870024620","589768463761","131827586825","851601128636","322151761634","700650335418","572074891743","723754913286","119175775298","795746500882","917001008158","068169053218","792107900819","536652696790","976433692360","515798882395","483285841698","942504563685","965351925530","544319711298","600530653622","748115360335","940213080334","362695845571","686087431763","086951212264","688023202711","706635527432","728137396354","895557238572","496014204152","200193376361","089691119308","459220251735","166425443641","573932760021","605812595337","383156758163","890968705060","406659825668","710464970777","734555027572","072360076281","379101102735","400306079213","020014417079","800406105498","921547910285","057670693668","214575254960","643313122712","807659967283","793995986362","411009282317","055430919509","149754531711","766535289950","137677339600","282316784512","474125479812","519405898872","330183209093","262212597706","910732127950","143080556111","538276064493","915533145685","562637147889","840044800169","762429196748","867058893013","657871693752","174003592710","421085264799","181232990041","374168611083","540036508848","042001279082","855262394183","952013314444","666563790427","146628656107","161595045889","067063543704","101720206348","075585003325","185007729374","980678866538","867471893442","797456418907","903794441882"
  ]
  }
  }

Well, this filter brought us to the more realistic number of **27,858** AMIs.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-14.png?resize=840%2C256&ssl=1)MongoDB Compass filter owners with more than 50 public AMIs

So, we removed 488 AWS accounts and their associated public AMIs. This removed 970,481 AMIs. So, to put things in perspective, as a mean, each AWS account removed had about 2000 public AMIs.

Let’s do some sanity checks and complete our list of targets.

#### 3.2.5 Sanity Checks

We are almost ready. The last step we did when filtering out instances was to set some limits in terms of volumes number and volumes size.

Firstly, each AMI comes with one or more EBS Snapshots. These are basically the volumes (disks) associated with the AMI. And when we start an EC2 instance based, we essentially get a copy of the AMI’s volumes in our account.

When checking the remaining AMIs from MongoDB we noticed that a few AMIs had some extremely big volumes or a lot of volumes. This would have required a lot of scanning time, increased cost and overall a headache.

As an example, we encountered AMIs with 28 volumes or with volumes big as 20 TB of data. As my colleague Matei like to cite from the Zen of Python, special cases aren’t special enough to break the rules.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-15.png?resize=407%2C232&ssl=1)Example of AMI with a volumes of 20 TB of data

So, we checked some means and we decided to filter out any AMI that has more than 3 volumes or with volumes bigger than 200 GB.
  
  
  for ami in amis:
  bdm = ami['BlockDeviceMappings']
  
  ebs_items = [x['Ebs'] for x in bdm if 'Ebs' in x.keys()]
  ebs_items = [x for x in ebs_items if 'SnapshotId' in x.keys()]
  
  if len(ebs_items) > 3:
  bad_amis.append(ami)
  continue
  
  big_snapshots = [x for x in ebs_items if x['VolumeSize'] > 200]
  
  if len(big_snapshots) > 0:
  bad_amis.append(ami)

We didn’t know how to do this in MongoDB so we did some classic python scripting. After this final filtering we brought down the number of AMIs to **26,778**.

And with this we managed to construct a list of targets. We were ready to start looking on ways to access the AMIs’ contents ❤️

## 4\. Accessing the AMIs

For us it made sense to not look into ways of how to access the AMIs before we had a final number of AMIs. Mostly because based on how many AMIs there were, we had to prioritize either time, costs or scanning robustness.

With 26k AMIs, we knew we had to find an option that:

  * Must be time and cost efficient
  * Must be automated
  * Must be as reliable as possible

### 4.1 Failed Options

Here are some options that might work when checking manually certain AMIs, but we couldn’t use at scale.

#### Option 1

So the AMI has information about its EBS Snapshot, right? So, in theory you could copy directly the Snapshot in your account and do whatever you want with it.

![Diagram with first option of accessing AMIs](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-16.png?resize=840%2C639&ssl=1)Option 1 for accessing AMIs

The flow would be something like this: we copy the AMI’s snapshot in our account and then we download it. Once downloaded we can mount it and access the files within.

Well, the main problem with this is that we can’t copy the EBS Snapshot in most cases. And this is something weird. When you make the AMI public, you essentially give permission to anyone to start an EC2 instance based on that EBS Snapshot. However, you have to explicitly make the EBS Snapshot public in order for this copy snapshot operation to work. In our tests we rarely encountered AMIs with public EBS Snapshots.

#### Option 2

So we have to give up the option of copying the EBS Snapshot. Let’s try something else:

![Diagram with second option of accessing AMIs](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-17.png?resize=840%2C567&ssl=1)Option 2 for accessing AMIs

Let’s start an EC2 instance in our AWS account based on the target AMI. So far so good. Now for accessing the AMI’s contents we will make an EBS Snapshot of its volume and download it.

This actually works great and is very reliable. I actually recommend this option when you want to check a single AMI. AWS even has a public tool for downloading EBS Snapshots and it works fantastic! It’s called coldsnap: <https://github.com/awslabs/coldsnap>

The problem with this method is that downloading EBS snapshots take a lot of time and requires a significant storage space. Both drawbacks were too hard to fix for this method of accessing the AMI, so we had to look for something else.

#### Option 3

Ok, so starting an EC2 instance based on the target AMI seems like the right track, but we have to change the part with the download. Here comes our third option:

![Diagram with third option of accessing AMIs](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-18.png?resize=840%2C703&ssl=1)Option 3 for accessing AMIs

We wanted to start an EC2 instance based on the target AMI and then connect to the instance. We thought of using either SSH or native solutions like SSM Run Command or SSM Session Manager.

Unfortunately, none of them worked. For SSH I think AWS couldn’t add a new key for the local user. Whereas for SSM, I think the version of the SSM Agent was too outdated for most of the AMIs in order to work.

Nonetheless, from these 3 failed options we tested we arrived at the conclusion that we should do everything inside the AWS ecosystem for being the most time efficient and that we need to start an EC2 instance based on the target AMI if we want to access its contents.

### 4.2 Working method

We figured that if we can’t connect to the instance that’s based on the AMI, but we can start it, why not move the EBS volume to another EC2 instance. So what we did was:

  * We started a normal EC2 instance and configured it so that it has everything required for connecting to it. We called this the Secret Searcher instance.
  * Next, we start a new EC2 instance based on the target AMI
  * We stop the new EC2 instance, detach its volume and terminate the instance
  * Afterwards, we reattach the volume to the Secret Searcher instance
  * Here we mount the volume and, well…search it for secrets

![Secret Searcher method for accessing the AMI's contents](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/option-4.drawio.png?resize=431%2C386&ssl=1)Secret Searcher method for accessing the AMI’s contents

The only drawback for this method is that it’s not the cheapest, but that doesn’t mean that will be expensive. Other than this, it ticked all the boxes for us.

Method | Speed | Cost | Reliability | Can be automated  
---|---|---|---|---  
1 | Slow | Small | Not great | Yes  
2 | Slowest | Medium | Great | Yes  
3 | Fastest | Biggest | Worst | Yes  
**4** | **Fast** | **Medium-Big** | **Great** | **Yes**  
  
Doing some tests for a region with 30 public AMIs, we came to an initial estimation of $10k for this research 😆

However, after more tests we determined that the cost should not exceed $1.2k and it didn’t.

### 4.3 Architecture for scale scanning

The high level flow is like this:

  * We have a master EC2 instance that will run the main script for automating everything.
  * This instance will start and configure in a region the Secret Searcher instance and any other prerequisites
  * Then, will start spawning batches of multiple EC2 instances based on target AMIs
  * Once the instances are running, the master instance will stop them and detach their volume(s)
  * For each AMI, the volume(s) will be reattach to the Secret Searcher instance
  * In the meantime the EC2 instances without volume(s) will be terminated to cut costs
  * On the Secret Searcher instance the volume(s) will be mounted and searched for secrets (more about this on next chapter)
  * The collected data is uploaded to an S3 bucket for further analysis and processing
  * The volume(s) will be detached and deleted immediately after the upload to S3 finishes
  * The process continues until every AMI from the region is processed

![Architecture for scanning AMIs at scale](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-20.png?resize=840%2C569&ssl=1)Architecture for scanning AMIs at scale

This approached allowed us to scan multiple AWS regions in parallel and resulted in a shorter waiting time for the final results.

### 4.4 Final considerations

We had to decide on an instance type that would work for most the the AMIs. We picked “c5.large” because it’s somewhat in the middle of what can support and is an instance type available in every region. Doing some tests we noticed 3 aspects.

The first and most simple one was that in order to move the EBS Volume from the spawned EC2 instance to the Secret Searcher instance, both instance must be in the same availability zone. So we spawned all resources in the availability zone “<region>a” (e.g., eu-central-1a).

The second one: some older AMIs had the parameter **VirtualizationType** set to “paravirtual” (you can read about it [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html)), which is an older type of virtualization. For covering this scenario we had to use an instance type from a previous generation: **c3.large**. You can check compatibility for Paravirtual (PV) of most instance types [here](https://aws.amazon.com/amazon-linux-ami/instance-type-matrix/).

![Example of AMI with VirtualizationType set to "paravirtual"](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-21.png?resize=493%2C557&ssl=1)Example of AMI with VirtualizationType set to “paravirtual”

And the last thing is that we got a high percentage of errors with the next message:

  * […] when calling the RunInstances operation: Enhanced networking with the Elastic Network Adapter (ENA) is required for the ‘c5.large’ instancetype. Ensure that you are using an AMI that is enabled for ENA.

This seemed a blocker because we didn’t know how to fix it, but then we tried something. You see, we started all instances without a public IP. This not only reduced the costs, but it prevented any startup script or tool to call home, to its owner. Even more, I think this is what kept us under to radar from AWS themself and didn’t get us blocked.

![Meme about AWS usage](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/8mjiy8.jpg?resize=503%2C496&ssl=1)

Anyway, we tried to manually spawn an EC2 that had the ENA error, but with a public IP and magically the error disappeared. Also, when we spawned this instance manually we used the instance type “t2.medium”. Doing a little more digging, we saw this bullet point for C5 instance type:

  * Requires HVM AMIs that include drivers for ENA and NVMe

I’m not sure what it means, but my guess is that C5 instances require some prerequisites in order to have ENA enabled, whereas T2 instances don’t.
  
  
  try:
  instance_type = 'c5.large'
  if 'VirtualizationType' in ami_object and ami_object['VirtualizationType'] == 'paravirtual':
  instance_type = 'c3.large'
  elif is_ena:
  instance_type = 't2.medium'
  
  instance = None
  if is_ena == False:
  instance = ec2.run_instances(InstanceType=instance_type,
  Placement={'AvailabilityZone':f'{region}{availability_zone}'},
  NetworkInterfaces=[{'AssociatePublicIpAddress':False, 'DeviceIndex':0}],
  MaxCount=1, MinCount=1,
  ImageId=ami_object['ImageId'],
  TagSpecifications=[{'ResourceType': 'instance', 'Tags':tags}])
  else:
  instance = ec2.run_instances(InstanceType=instance_type,
  Placement={'AvailabilityZone':f'{region}{availability_zone}'},
  MaxCount=1, MinCount=1,
  ImageId=ami_object['ImageId'],
  TagSpecifications=[{'ResourceType': 'instance', 'Tags':tags}])
  
  instance_id = instance['Instances'][0]['InstanceId']
  print(f'[x] Instance {instance_id} started. Waiting to become running.')
  
  waiter = ec2.get_waiter('instance_running')
  waiter.wait(InstanceIds=[instance_id], WaiterConfig={'Delay': 5, 'MaxAttempts': 120})
  
  print(f"[x] Instance {instance_id} based on ami {ami_object['ImageId']} is ready.")
  
  return {"instanceId": instance_id, "ami": ami_object['ImageId']}
  except Exception as e:
  error = 'failed '
  if hasattr(e, 'message'):
  error = f'{error}  {e.message}'
  else:
  error = f'{error}  {e}'
  
  if '(ENA)' in error and is_ena == False:
  return start_instance_with_target_ami(ami_object, region, is_ena=True)
  else:

## 5\. Digging for secrets

To recap, we are now at the point where we have the AMI’s volume mounted and we need to search it. We decided to use SSM Run Command for running a remote script that will mount the volume, scan its contents and upload the results in an S3 Bucket.

![Diagram with execution flow for secret searching](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/flow-secret-searching.png?resize=515%2C412&ssl=1)Secret searching flow

### 5.1 Mounting

I think mounting was the biggest challenge in terms of automation. We had to identify the volume’s filesystem type, mount the right partition (if it was partitioned) and fix UUID collisions.

We looked for an existing tool to do all of this, but we couldn’t find anything. We ended up using udisksctl for mounting because it tries to detect the proper filesystem type (ext, xfs and so on).

Let’s take a look at the next image for discussing UUID collision and partitioning.

![root volume and attached volume with UUID collision](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-22.png?resize=840%2C159&ssl=1)UUID collision between root volume and attached volume

For an unknown reason, we encountered a lot of UUID collisions when attaching a new volume to the Secret Searcher instance. The issue with this is that you can’t mount a second volume with the same UUID as a mounted one. There are tools specific to the filesystem’s type to fix this: **xfs_admin** for xfs volumes and **tune2fs** for ext4 volumes.

And the last challenge was that most of the volumes had multiple partitions. In the image above we can see that the attached volume (xvdf) has 3 partitions. We had to identify the right one to mount and search. Now, you might say that the right one is the one with the biggest size.

Well, it’s not so easy to extract and compare this information using bash. Even more, there are volumes with multiple storage partitions and we didn’t want to take only the biggest partition in size.

To overcome this, we did something less elegant, but practical. We tried to mount and scan every partition no matter if its usage. And, well…it worked fine 💪

### 5.2 Finding secrets

We decided that there is too much work to write code to look for any possible secret and sensitive information, so we tried a few tools like [truffleh](https://github.com/trufflesecurity/trufflehog)[o](https://github.com/trufflesecurity/trufflehog)[g](https://github.com/trufflesecurity/trufflehog) and [linpeas](https://github.com/peass-ng/PEASS-ng/blob/master/linPEAS/README.md). The drawback was that a scan on a 8 GB AMI took around 10-15 minutes with trufflehog and 30 minutes with linpeas. Multiply that with 26,778 and you’ll never finish.

The solution? **find**!

![meme always had been](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/a.jpg?resize=840%2C472&ssl=1)

Yep, we decided to use **find**. And we did it like this: we made a small list of things we wanted to check and have fun with. The most important ones were AWS access keys from the .aws directory and potential private Git repositories. Next in line were SSH keys and typical web application configuration files like config.php, web.config, .env and so on.
  
  
  find $mount_point \( ! -path "$mount_point/Windows/*" -a ! -path "$mount_point/Program Files/*" -a ! -path "$mount_point/Program Files \(x86\)/*" \) -size -25M \
  \( -name ".aws" -o -name ".ssh" -o -name "credentials.xml" \
  -o -name "secrets.yml" -o -name "config.php" -o -name "_history" \
  -o -name "autologin.conf" -o -name "web.config" -o -name ".env" \
  -o -name ".git" \) -not -empty

However, we had this strong fear of missing out important things so we decided to do something complementary. Besides a few folders, we indexed the whole volume. We made a list of all the files, along with their full path, so that we can later analyze it in case needed. This way we won’t have to come back to scanning all the public AMIs, but rather check what AMIs contain the files of interest for us.

A redacted snippet for one AMI would look like this:
  
  
  /var/lib/cloud/instances/i-00000000000000000/sem/config_rsyslog
  /var/lib/cloud/instances/i-00000000000000000/sem/config_runcmd
  /var/lib/cloud/instances/i-00000000000000000/sem/config_scripts_per_instance
  /var/lib/cloud/instances/i-00000000000000000/sem/config_scripts_user
  /var/lib/cloud/instances/i-00000000000000000/sem/config_set_hostname
  /var/lib/cloud/instances/i-00000000000000000/sem/config_set_passwords
  /var/lib/cloud/instances/i-00000000000000000/sem/config_ssh
  /var/lib/cloud/instances/i-00000000000000000/sem/config_ssh_authkey_fingerprints
  /var/lib/cloud/instances/i-00000000000000000/sem/config_timezone
  /var/lib/cloud/instances/i-00000000000000000/sem/config_users_groups
  /var/lib/cloud/instances/i-00000000000000000/sem/config_write_files
  /var/lib/cloud/instances/i-00000000000000000/sem/config_write_metadata
  /var/lib/cloud/instances/i-00000000000000000/sem/config_yum_add_repo
  /var/lib/cloud/instances/i-00000000000000000/sem/config_yum_configure
  /var/lib/cloud/instances/i-00000000000000000/sem/consume_data
  /var/lib/cloud/instances/i-00000000000000000/user-data.txt.i
  /var/lib/cloud/instances/i-00000000000000000/vendor-data.txt
  /var/lib/cloud/instances/i-00000000000000000/vendor-data.txt.i
  /var/lib/cloud/instances/i-11111111111111111
  /var/lib/cloud/instances/i-11111111111111111/boot-finished
  /var/lib/cloud/instances/i-11111111111111111/datasource
  /var/lib/cloud/instances/i-11111111111111111/obj.pkl
  /var/lib/cloud/instances/i-11111111111111111/sem
  /var/lib/cloud/instances/i-11111111111111111/sem/config_keys_to_console
  /var/lib/cloud/instances/i-11111111111111111/sem/config_locale
  /var/lib/cloud/instances/i-11111111111111111/sem/config_mounts
  /var/lib/cloud/instances/i-11111111111111111/sem/config_package_update_upgrade_install
  /var/lib/cloud/instances/i-11111111111111111/sem/config_phone_home
  /var/lib/cloud/instances/i-11111111111111111/sem/config_power_state_change
  /var/lib/cloud/instances/i-11111111111111111/sem/config_puppet
  /var/lib/cloud/instances/i-11111111111111111/sem/config_resolv_conf
  /var/lib/cloud/instances/i-11111111111111111/sem/config_rsyslog
  /var/lib/cloud/instances/i-11111111111111111/sem/config_runcmd
  /var/lib/cloud/instances/i-11111111111111111/sem/config_scripts_per_instance
  /var/lib/cloud/instances/i-11111111111111111/sem/config_scripts_user
  /var/lib/cloud/instances/i-11111111111111111/sem/config_set_hostname
  /var/lib/cloud/instances/i-11111111111111111/sem/config_set_passwords
  /var/lib/cloud/instances/i-11111111111111111/sem/config_ssh
  /var/lib/cloud/instances/i-11111111111111111/sem/config_ssh_authkey_fingerprints
  /var/lib/cloud/instances/i-11111111111111111/sem/config_timezone
  /var/lib/cloud/instances/i-11111111111111111/sem/config_users_groups
  /var/lib/cloud/instances/i-11111111111111111/sem/config_write_files
  /var/lib/cloud/instances/i-11111111111111111/sem/config_write_metadata
  /var/lib/cloud/instances/i-11111111111111111/sem/config_yum_add_repo
  /var/lib/cloud/instances/i-11111111111111111/sem/config_yum_configure
  /var/lib/cloud/instances/i-11111111111111111/sem/consume_data
  /var/lib/cloud/instances/i-11111111111111111/user-data.txt.i
  /var/lib/cloud/instances/i-11111111111111111/vendor-data.txt
  /var/lib/cloud/instances/i-11111111111111111/vendor-data.txt.i

We think that our trade-off gives other researchers space to conduct their analysis on specific files that were not covered by us.

All data found was copied from the volume’s location to our user’s home folder and then uploaded in an S3 bucket for further analysis and validation. After the upload completed we deleted the copied files, unmounted the volume and continued.

One fun fact before moving forward: in our initial tests we got a few unknown causes that broke the Secret Searcher instance. It turned out that the .git folders had more than 8 GB of data and when we tried to copy them in our user’s home folder (in a volume of 8 GB), the instance crashed. Once we modified the configuration of the Secret Searcher to use 50 GB instead of 8 everything went well 😌

### 5.3 Looking through private Git repositories

We gathered thousands of repositories worth of over 400 GB of data. The idea with the repositories was that they might contain hard-coded credentials. This was especially and insight coming from Matei as I was very skeptical on this (spoiler: he was right).

We decided that for now there is no point in determining which repository is private and which one is public. We just wanted a way to scan them for secrets and for that we used [gitleaks](https://github.com/gitleaks/gitleaks).

As you might expect, we didn’t run gitleaks on the S3 bucket. We had to download everything on a physical hard drive.

![meme git secrets](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/3.jpg?resize=600%2C471&ssl=1)

Gitleaks proved to be a fantastic tool that checked for secrets across all commits. Of course, we also had a big number of false positives on some types of credentials, but we’ll talk more about them on the next chapter.

## 6\. Results

### 6.1 AWS Keys

This was our main focus during this research mostly because it can give access to an AWS environment starting from an AWS misconfiguration.

Throughout this piece of research, we obtained over 200 valid AWS credentials. These were obtained from 4 sources: /home/<user>/.aws/credentials, Git repositories, .env folders, /home/<user>/.aws/config. After concatenating the data from all the sources, we had to clean up and validate the data. So, we made sure to place the hundreds of potential AWS credentials in %UserProfile%/.aws/credentials, making sure that the profile names are numeric and sequential. Then, we ran the following batch command to test each set of credentials:
  
  
  for /L %i in (1, 1, <REPLACE WITH NUMBER OF PROFILES>) do ( echo %i & aws sts get-caller-identity --profile %i > %i.txt

Then, we ran the following batch script to check which profiles were valid:
  
  
  @echo off
  setlocal enabledelayedexpansion
  
  rem Loop through all files in the current directory
  for %%F in (*) do (
  rem Check if the file is not empty
  if %%~zF GTR 0 (
  rem Print the name of the non-empty file
  echo Non-empty file: %%F
  echo %%F >> non_empty.txt
  ) else (
  rem Delete the empty file
  del "%%F"
  echo Deleted empty file: %%F
  )
  )
  
  pause

Lastly, back on our Linux machine we transferred non_empty.txt and ran the following one-liner to only keep the valid credentials:
  
  
  for i in $(cat non_empty.txt | awk -F. '{print $1}');do grep "\[$i\]" clean_creds -A3;done > credentials

From the **.aws/credentials** and other configuration files we managed to get over 60 valid AWS credentials. This is actually us when we validated the first pair of access keys:

![gif meme pleasure](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/meme-p.gif?resize=258%2C172&ssl=1)

The way we validated them was with the command “aws sts get-caller-identity”. The crazy part is that among these 50 pair of access keys, about 10 were from the root user account. This meant that we got full control over more than 10 AWS accounts.

Well, this is not all. The Git repositories proved to be a gold mine of secrets. We managed to get over 100 valid AWS keys. Again, with about 10 of them being for the root user account.

We noticed that some of them were duplicates. So, after removing the duplicates our results looked like this:

  * 121 valid AWS access keys
  * 20 of them being from the root user account

![meme pikachu surprised](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/4.jpg?resize=500%2C500&ssl=1)

We’ll talk later more about impact, but for now we’d like to highlight that out of nothing we got, only from public resources, access into 120+ AWS accounts and full access into 20 of them.

### 6.2 Secrets extracted from Git repositories

Something we simply didn’t think of was that there were more repositories per AMI. For some reason I thought there will be only one. Running gitleaks on all of them took about 48 hours of continuous scanning. The results? Well…
  
  
  2077989 Generic API Key
  105322  AWS
  23738  Private Key
  22936  JSON Web Token
  3038  Telegram Bot API Token
  2382  GCP API key
  1075  Slack token
  1007  Slack Webhook
  937  Stripe
  213  Twitter API Key
  211  GitHub Personal Access Token
  209  Twitter Access Secret
  206  Twitter API Secret
  165  EasyPost API token
   148  SumoLogic Access ID
  134  Twilio API Key
  118  Algolia API Key
  105  SendGrid API token
  96  Facebook
  80  Okta Access Token
  70  EasyPost test API token
  56  SumoLogic Access Token
  55  GitHub OAuth Access Token
  42  Flutterwave Secret Key
  42  Flutterwave Encryption Key
  42  Finicity Public Key
  40  GitHub App Token
  20  GitHub Refresh Token
  15  HubSpot API Token
  14  Alibaba AccessKey ID
  12  Mailgun private API token
  12  Databricks API token
  9  Zendesk Secret Key
  7  Sentry Access Token
  6  LinkedIn Client ID
  6  Flickr Access Token
  4  LinkedIn Client secret
  4  Dropbox API secret
  3  Twitter Access Token
  3  Codecov Access Token
  3  Adobe Client Secret
  2  Microsoft Teams Webhook
  2  Mailgun public validation key
  2  Lob Publishable API Key
  2  Lob API Key
  2  Coinbase Access Token
  1  Shippo API token
  1  Pulumi API token
  1  Kucoin Secret Key
  1  Kucoin Access Token
  1  Intercom API Token
  1  GitLab Personal Access Token

Two challenges appeared now:

  1. We need to remove false positives
  2. We need to check if the secrets are valid

At the moment of writing this we validated only around half of the categories identified. The most relevant results:

  * 100+ valid sets of AWS access keys
  * 10+ valid Stripe live API keys
  * 1 valid set of Alibaba access keys
  * 10+ GitLab/GitHub tokens

For some secrets, like AWS keys, gitleaks extracted only the access key id and the commit id. We had to write a script for extracting the secret access key. While it appeared complicated at first, we used “git show <commit-id>:<file-path>” inside a python script and went actually really fine.
  
  
  def get_file_contents_from_commit(commit_and_file_path, repo_folder):
  try:
  result = subprocess.run(['git', 'show', f'{commit_and_file_path}'], capture_output=True, text=True, check=True, cwd=repo_folder, encoding='utf-8')
  return result.stdout
  except:
  return None

### 6.3 Secrets from config files

What else we got from the configuration files we scanned? Well, all kinds of things:

  * A lot of gmail credentials
  * AWS access keys
  * A lot of tokens from communication services 
  * Private SSH keys
  * DB connection strings
  * Keys for back-end APIs
  * Secrets for signing JWTs
  * Keys/tokens/secrets for various services

And just everything you can imagine and it can be found in the configuration file of a web application.

Truth to be told, except for AWS access keys, we didn’t investigate these files in details as it would have took too much time. The most interesting thing we took from this was that people are still hard-coding secrets in web application config files under the false sense of safety that the repository is private.

## 7\. Impact

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/05/8p1t6i.jpg?resize=500%2C686&ssl=1)

Here we’ll talk about the impact that a malicious actor might have caused with the collected secrets. Is hard to properly quantify this because, first, we didn’t finish processing the data, but second, we didn’t investigate the full extend of what we can do with the permissions from valid credentials.

So we had over 120 valid AWS access keys, 18 of them being from the root user. This means that we theoretically fully compromised 18 AWS accounts. But even here we don’t know if these accounts are holding the whole infrastructure of the company or it’s just a dev account.

Ok, but let’s assume the worst for a minute. Let’s assume that these accounts were production accounts. Well, you can imagine what would be like to have a foothold inside the cloud infrastructure of big companies that operate in domains like networking equipment, automation, fintech, health research, aerospace research, satellite navigation, universities, software outsourcing , telecommunication and more.

Imagine backdooring a fintech application that collaborates with multiple international banks. Or backdooring a network equipment. Maybe shutting down critical components for satellite navigation or espionage and sabotage on research facilities. And let’s not forget about stealing customer data and ransomware.

All this from the AWS accounts, but we got tons of other secrets, remember?

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/05/8p1vp1.jpg?resize=840%2C288&ssl=1)

We got a lot of SMTP credentials. Why bother hacking the company when you can send phishing emails using the official email address? But why bother sending phishing emails when you can generate password reset emails and read the email?

Next we have Git tokens/keys that give access to private repos. Now we’re talking about backdoor or supply chain attacks. We also have thousands of social media secrets. This can lead to defamation or account takeover. And with other keys from various pay-as-you-go services, it would be possible to inflict additional costs on the legitimate owners.

What about all the source code from thousands of private git repositories? Well, we can look into it and find zero days. For some repos we found the secret key for signing JWTs. Imagine how fun it would be to analyze the source code, sign admin tokens and use them on the production running application.

To top it all off, let’s not forget about the Stripe keys that summed up could have made us $40k richer.

We have to admit that it is a bit overwhelming and unexpected how much impact this research showed in the end.

## 8\. Responsible disclosure

We have a treasure of secrets and a potential impressive level of access. Now it’s time for the most important and boring part of the research: responsible disclosure.

### 8.1 Owners of AWS access keys

First off, AWS access keys. If you ever found a pair of AWS access keys, you might know that it’s not always straightforward to find who owns the AWS account and how can you contact them. We ended up using the a few CLI calls for trying to get the contact information:
  
  
  aws account get-contact-information
  aws account get-alternate-contact --alternate-contact-type SECURITY
  aws account get-alternate-contact --alternate-contact-type BILLING
  aws account get-alternate-contact --alternate-contact-type OPERATIONS

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-34.png?resize=625%2C256&ssl=1)Example response for contact information

![bernie meme](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/1.jpg?resize=500%2C500&ssl=1)

Well, that was easy, right? Not really 🥲. From the 120+ valid access keys, only about 5 had a valid contact email set. Most of them only had a website referred or even worse, were owned by individuals not companies.

At this point the situation is like this: we have about 5 AWS accounts with valid contact emails and about 70 AWS accounts with a website referred. For these 70+ accounts, we had to search their website and find a a contact email, which proved to be harder than one might imagine.

The rest of them didn’t provided enough information to be identifiable or the user’s access keys didn’t have permissions to make these API calls. And there is one additional aspect. I can very well write in my AWS account at the contact details that I’m Amazon/Microsoft/Google and nobody will stop me. We had to be careful how we disclose the issue to the presumed owner.

For the cases where contact details were not available, we went back to the ethical considerations and decided not to poke any further and to contact AWS directly. However, this area could be very fruitful for malicious actors. For instance, an attacker could easily target data in the S3 buckets associated with the account in ransomware attacks. 

Anyway, our initial disclosure email looked like this:
  
  
  Hello,
  
  Me and my colleague Matei Josephs are working on a cybersecurity research in the cloud area. During this research we identified that you are exposing the AWS credentials of the user <username> from AWS account 12345EXAMPLE among other things. We estimate that the risk of this issue is critical.
  
  What would be the appropriate communication channel for sharing more information about this security issue?
  
  Thank you,
  Eduard Agavriloae

We wanted companies to confirm that they own the mentioned resources before telling them the detailed issue.

After 90 days from the initial disclosure email sent to over 70 companies, we got about 5 responses. How many AWS access keys were still valid after all this time? Well, all of them except 10.

![meme bike falls](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/44.jpg?resize=500%2C680&ssl=1)

In the end we provided a partially redacted list of the remaining valid AWS access credentials directly to AWS in the hope that they will be able to contact the owners more easily than us.

#### 8.1.1 Working with AWS’s security team

This was our last stop before publishing the article. We wanted to reduce the impact of the affected AWS customers before going public. I have to say that before working with AWS’s changed the perspective we built about responsible disclosure. Their team was so open, curious and helpful that’s hard to describe.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/05/8p1jsy.jpg?resize=687%2C500&ssl=1)

After our notification, AWS quickly notified customers of the reported exposed AWS Keys. Then we set a meeting with them where we detailed our research, the results and exchanged ideas around it. Turns out that what we did not only was legal, but we didn’t even violate any Terms&Conditions. We’ll talk more about how this can be fixed from our point of view and what we discussed with AWS at the end of the article.

Making another check on the AWS keys after two weeks, now we had only 58 valid one. The notification from AWS certainly did more than we could, but the remaining number of valid keys is still high.

### 8.2 Other keys

When other keys were involved, it was actually easier to determine the owner. For example, for all the Stripe keys we found, we were able to access the owner’s invoices which allowed us to immediately determine the owner and a contact email.

Similar story with Git tokens. And similar story with the disclosure emails. Very low response rate and fix rate. For Stripe keys we contacted Stripe and ask for their help in fixing this.

![meme change my mind](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/1231.jpg?resize=577%2C432&ssl=1)

## 9\. Stories worth telling

### 9.1 GitLab Personal Access Token

A GitLab personal access token was found for a large FinTech provider. While we would rather not disclose the provider by name, here are some of their partners and clients:

![redacted image with clients and partners](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-24.png?resize=624%2C121&ssl=1)Redacted list of partners of FinTech company

The GitLab personal access token gave us at least read access to the private repositories of the company. This is the point where we stopped digging as we already knew that the impact was quite high and decided to report the issue as quickly as possible. We tried to get in touch with their displayed contacts, but we did not get any response.

This is when we decided to involve the Computer Emergency Response Team (CERT) for the country where the company was based. After follow-ups from the CERT, here is the response:

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-25.png?resize=585%2C144&ssl=1)

### 9.2 Stripe API key

Another interesting finding from a Git repository was having access to some Stripe API keys. Most of them were sk_test keys (meaning that they were test keys), however, some were sk_live keys. For those of you who don’t know, Stripe is a payment service provider like PayPal. Of course, having access to some live API keys, we decided to query the balance on each account. The following one stood out to us:

![Balance returned from Stripe API](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-27.png?resize=840%2C580&ssl=1)Balance returned from Stripe API

If you haven’t already noticed, the reason this one stood out was the 7-digit amount and the USD currency. $3,171,708 you may ask? Well, that’s what we hoped, but the Stripe API documentation brought us back down to earth.

![screenshot documentation stripe API balance](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-28.png?resize=626%2C154&ssl=1)Documentation snippet for balance endpoint

The amount indicated in the balance is in cents, so what we thought were $3,171,708, were actually $31,717.08. Not quite 3 million dollars, but still – a decent amount. After the first wave of disappointment, we approached them via the email indicated on their contact page. Fast-forward one week and we got no response. This is when we went back to our ethical considerations, or more precisely the following point within our ethical considerations: **do enough to prove impact**. And that is what we did. We generated a transaction and triggered a refund from the Stripe API. Then, we noticed that the transaction was indeed reverted.

![payment modal](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-29.png?resize=265%2C166&ssl=1)Payment form

![API call for reverting a transaction](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-30.png?resize=840%2C345&ssl=1)API call for reverting a transaction

![Transaction refund screenshot from revolut](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-31.png?resize=455%2C82&ssl=1)Transaction refund

Still, in order to reach the company, we found their CEO on LinkedIn, did some OSINT to find their email and contacted them making sure to include the potential for financial damage within the disclosure email. Next thing you know, we heard back from the CEO.

![email reply from CEO of affected company](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-32.png?resize=641%2C509&ssl=1)Reply from the CEO

We provided a detailed report, containing findings, impact and recommendations for remediation. Shortly, the CTO responded this time, thanking us for responsibly disclosing this issue.

![email reply after fix from CTO](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/image-33.png?resize=373%2C114&ssl=1)Response after fix from CTO

### 9.3 Sales meeting, but with a twist

For one small company with valid AWS keys out there we couldn’t find a contact email. The only contact form available was to set a sales meetings with them.

Well, that’s what we did. We scheduled a sales meeting for the next day and we actually presented them the issue in a meeting. They seemed a bit scared, but I guess anyone would be. In the end they thanked us for disclosing the issue with them and now I’m connected on LinkedIn with their CEO 😆

![meme epic handshake](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/04/8mxedi.jpg?resize=697%2C500&ssl=1)

We went to weird lengths to disclose to companies their exposed AWS access keys. For instance, we completed tens of contact forms with zero response back. For a medical institution we had to submit a report to an investigation board. An HR person closed our issue there without asking for more details. And for only one company we managed to report the issue on a bug bounty platform, but it was only a vulnerability disclosing program so our bounty for a P1 was $0 🥲

### 9.4 The amazing AWS Security Team

I am one of those people that sincerely cares about cybersecurity and maybe you are too. Well, that’s how the people from the AWS’s Security Team are. Of course, we discussed with only 3 of them, but their spirit towards cybersecurity was so well defined that it can’t be just them.

To put in perspective, AWS was not responsible with anything on this issue. They made the process of publishing AMIs so that’s impossible to do it without knowing what you’re doing. Having an AMI public is by no chance a simple mistake, no. It is very explicit. And even so, these people put in the effort, curiosity and time to help the clients with exposed AWS keys.

You might say that was in their interest, and yes, I believe that too, but it was visible that they were helping from a place of care, not a place of obligation. And trust me, I’m no big fan of corporation culture. These guys were what you can call good guys.

In a more objective perspective, they took our report seriously, they listened us, they scheduled a call to discuss more, they asked for further details and they helped the affected clients. Not at any point we were questioned, asked to not publish or threatened with anything. They even reviewed our blog post before publishing and gave a few suggestions about the message we’re about to send.

I honestly hope that every big provider of anything out there has a security team with a open culture towards researchers, improvement and helping as AWS does.

![](https://i0.wp.com/securitycafe.ro/wp-content/uploads/2024/05/8p1kp8.jpg?resize=612%2C408&ssl=1)

## 10\. Future work & Ethical considerations

### 10.1 Ethical considerations

When we began undertaking this research project, we set some ethical limits. We were sure that we will find some interesting data, so we decided from the start what we could and could not do with the data. Our general approach was to test whether the secrets are valid, do enough to prove impact, but not more than that.

At the time of writing this, we worked on this research for about 6 months. The limited number of responses to our responsible disclosure made us to wait a bit longer before publishing the research.

In the end we realized exactly what we advice against: security by obscurity is not security. Just as these companies made their AMIs public hoping that no one would find them, we started doing the same thing with this attack vector.

So we decided that the best option is to publish this research in the hope that defenders will catch wind of it before attackers manage to implement their scanning infrastructure.

### 10.2 Future work

First off, our colleague **Stefan Tita** just finished the same scanning process on **Azure** and now we are in the process on analyzing the data collected from there. So far it seems that the same issue is present there as well.

Second, there is still a lot to do with the collected data from AWS. Some directions we have in mind so far:

  * We extracted 20k+ JWTs. We want to check if there are any of them valid and if we can identity the web application that authenticates them
  * We could take a look at the source code of certain repositories in order to do some source code review, identify some cool vulnerabilities and get some CVEs
  * We found in the Git repositories multiple JWT signing keys. We would like to check if we can identify the web applications running that code and sign our own JWTs.
  * We still have a lot of secrets to validate
  * We want to do an analysis on the extracted file names (see [CloudQuarry Wordlists](https://github.com/MatJosephs/CloudQuarryWordlists))

In terms of what can be further done, we could adjust the script to run continuously and whenever a new public AMI is detected, to start the scanning process. We suspect that some companies are making AMIs public for only a short period of time. Well, that short period of time can be enough to get the data within.

While we look further into the data more ideas might come and new articles will be written. In the end we might extend to GCP as well, but until then there is still work to do.

## Conclusions

Usually I like to draw 2-3 ideas and keep the “Conclusions” chapter short, but on this research we have a bit more to say.

We recommended AWS to put some limitations or throttling in place when multiple community (especially deprecated) AMIs are spawned in a short period of time from a single AWS account. We didn’t get a certain response if this will be implemented. Since you can use multiple AWS accounts to split the load and once you compromise a new account, you can split the load further, maybe this is not something that can be fixed. Can you still replicate this research? Most likely yes, but be aware that AWS monitors the AMI usage. We might publish our repository in the future after we present the research at a few conferences, but we are not sure yet.

About what we noticed, companies are still relying on obscurity for covering their lack of security. Finding the AMI of a company among 3.1 million public ones might be hard, but when scanning every public AMI then the AMI surely won’t be missed. We’d like to mention that you can target specific companies and technologies by searching AMIs based on description, title or owner, so #bugbounty tip right there.

Going further with this, obscurity hides even more bad security practices. Hard-coding secrets in private repositories can put your company to their knees. As Matei likes to say it, what good to hide your secrets in private repositories if the repositories are put in public AMIs.

We saw big companies having this critical vulnerability in their environment. It seems that people are still not doing regular Cloud Security Configuration Review regularly or at all. Even more, they deploy vulnerable resources knowing very well or ignoring the security implications.

Looking even closer you can identify another bad security practice: not rotating secrets. We report this issue a lot in our day-to-day engagements and we sometimes get uninterested reactions. It’s exactly this kind of scenario that would prevent attackers from having access for years in your environment.

Small good practices add up and help you have a mature security posture. There is a CIS benchmark item that states that your AWS account should have contact information set. That’s a low risk finding at most, but look how much it would have helped companies in being contacted with a security incident.

Finally, after 6 months, 1200+ lines of code, 14+ days of scanning and a $500+ bill, we have this initial piece of article to share with everyone, but we believe that the full impact of this research is yet to be unfolded.

Thank for reading!

Eduard Agavriloae & Matei Josephs

### Share this:

  * [ Share on Facebook (Opens in new window) Facebook ](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/?share=facebook)
  * [ Share on X (Opens in new window) X ](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/?share=twitter)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/?share=reddit)
  * 

### Like this:

Like Loading…

### _Related_

[amis](https://securitycafe.ro/tag/amis/)[aws](https://securitycafe.ro/tag/aws/)[cloud](https://securitycafe.ro/tag/cloud/)[Cloud Security](https://securitycafe.ro/tag/cloud-security/)[cloudquarry](https://securitycafe.ro/tag/cloudquarry/)[public amis](https://securitycafe.ro/tag/public-amis/)[Research](https://securitycafe.ro/tag/research/)

## Post navigation

[Previous Post: CVE-2024-28344 & CVE-2024-28345 in Sipwise C5](https://securitycafe.ro/2024/03/21/cve-2024-28344-cve-2024-28345-in-sipwise-c5/)

[Next Post: Red Team Finds A Way – Exploiting The Human Factor](https://securitycafe.ro/2024/07/02/red-team-finds-a-way-exploiting-the-human-factor/)

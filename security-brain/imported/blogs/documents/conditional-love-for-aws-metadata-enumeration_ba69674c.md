---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-07_conditional-love-for-aws-metadata-enumeration.md
original_filename: 2024-02-07_conditional-love-for-aws-metadata-enumeration.md
title: Conditional Love for AWS Metadata Enumeration
category: documents
detected_topics:
- cloud-security
- idor
- access-control
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- cloud-security
- idor
- access-control
- xss
- command-injection
- rate-limit
language: en
raw_sha256: ba69674c23bdda828ea6eb69a5babd88730722176a6221bd7455f6af3e38f6fb
text_sha256: 55feb9035e2139f496f5f7847963062b08f286c041bc57bc7493d70ce16d976b
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Conditional Love for AWS Metadata Enumeration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-07_conditional-love-for-aws-metadata-enumeration.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, access-control, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `ba69674c23bdda828ea6eb69a5babd88730722176a6221bd7455f6af3e38f6fb`
- Text SHA256: `55feb9035e2139f496f5f7847963062b08f286c041bc57bc7493d70ce16d976b`


## Content

---
title: "Conditional Love for AWS Metadata Enumeration"
url: "https://blog.plerion.com/conditional-love-for-aws-metadata-enumeration/"
final_url: "https://www.plerion.com/blog/conditional-love-for-aws-metadata-enumeration"
authors: ["Daniel Grzelak (@dagrz)"]
bugs: ["AWS misconfiguration", "Cloud"]
publication_date: "2024-02-07"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 446
---

Did your parents ever tell you the one about the security researcher and the AWS policy condition engine? No? Weird. It’s okay, I’ll tell it to you now.

You see, when a security researcher (me) and the AWS policy engine love each other very very much, they start spending a lot of time together. They learn about each other and tell nerdy jokes. Eventually, when they hug really tight, a metadata enumeration abuse technique pops out. That’s not _exactly_ how it works, but it’s close enough.

The truth is someone else loved the AWS policy engine before I did. Maybe he would describe the process a little differently but in 2021 [Ben Bridts](https://twitter.com/benbridts) published [a spicy approach for extracting AWS account IDs from public S3 buckets](https://cloudar.be/awsblog/finding-the-account-id-of-any-public-s3-bucket/). It would be underselling it to say this post was inspired by his work. It certainly wouldn’t be possible without it. ❤️ Ben.

\---

Ben identified that S3 implemented a policy condition key called “[s3:ResourceAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-resource-account)” that restricts user, role, or application access to the Amazon S3 buckets owned by a specific AWS account ID. Expressed in nerd, the caller of the S3 API can make that call conditional on the account ID of the bucket they are trying to address.

That means it’s possible to write an IAM policy condition that says “Allow access to a bucket if the account it belong’s to is 133713371337”.
  
  
  1{
  2  "Version": "2012-10-17",
  3  "Statement": [
  4  {
  5  "Sid": "AllowResourceAccount",
  6  "Effect": "Allow",
  7  "Action": "s3:*",
  8  "Resource": "*",
  9  "Condition": {
  10  "StringEquals": {"s3:ResourceAccount": "133713371337"}
  11  }
  12  }
  13  ]
  14}

`‍`If a cheeky hacker attaches that policy to their own user:

`aws iam put-user-policy --user-name cheeky-user \  
--policy-name yikes \  
--policy-document file://./policy.json`

And they try to read from the “commoncrawl” public bucket, they will get an error:

`% aws s3api head-bucket --bucket commoncrawl  
  
An error occurred (403) when calling the HeadBucket operation: Forbidden`

But if they are really good at guessing 12 digit numbers and put “949746302274” in the policy instead of “133713371337”, the operation will succeed (no error, no output):

`% aws s3api head-bucket --bucket commoncrawl  
%`

An observant reader might point out that the attacker in this example should have instead bought a lottery ticket if they are going to be that lucky. They would need to repeat this trick on average 10^12/2 times testing account ID 000000000000 through to 999999999999, to find the correct ID.

That’s cool and all, but who has the time and money to make 10^12/2 AWS API calls? Not this security researcher! Luckily, Ben also saved us the agony of finger calluses from infinite backspace and numpad keypresses.

You see dear reader, the “s3:ResourceAccount” condition key can be used with any string operator including “StringLike”, not just “StringEquals”. Clever little hackers can use this to test conditions like does the account ID begins with “9”:

`"Condition": {  
"StringLike": {"s3:ResourceAccount": "9*"}  
}`

Or “95”

`"Condition": {  
"StringLike": {"s3:ResourceAccount": "95*"}  
}`

That means they can go through digit by digit, instead of needing to guess all the digits at once. If one digit succeeds, they move onto the next. The most they will have to press backspace and a digit is just 120 times. Thank you Ben.

This is where Ben’s story ends and ours begins.

We wanted to know, were there any other resources in the global namespace that could have their account IDs enumerated in this manner? Could a public Route53 zone or Cloudfront distribution be enumerated for example?

My favourite approach to finding security issues in AWS is [reading the docs](https://dagrz.com/writing/aws-security/getting-into-aws-security-research/#:~:text=Trawl%20AWS%20documentation) because AWS is very good at documenting everything, and I’m not smart enough to just figure it out on my own. It wasn’t surprising to find AWS has documented all the [service based condition keys](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) and with the magic of copy and paste, we [compiled them all](https://github.com/plerionhq/conditional-love/blob/main/service-condition-keys.txt). A few candidates popped up:

`kms:ResourceAliases  
ram:ResourceArn  
s3:ResourceAccount  
s3express:ResourceAccount`

Those didn’t seem that exciting. Was this the end of the love fest?

Yeh, nah. That’s Australian for “ease into it with a yeh first so the no is not as harsh”. At some point in history the accomodating folks at AWS realised the utility of this condition and [made it global](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceaccount) under the “aws” namespace. Except for a few specific exceptions “aws:ResourceAccount” can be applied to almost every AWS API. We are cooking with gas.

![](https://cdn.prod.website-files.com/663cfee0a192fe7e5bd05ee8/66954071e65f00790ee7acc8_resouceaccount-exceptions.webp)

I’ll save you from the boring painstaking part of trying to find resources and API calls that:

  * Allow cross-account or public access; and
  * Use a global namespace identifier (rather than an ARN that already has an account ID in it)

Our search was not exhaustive, but I am exhausted. We did find the following resources allowed account ID enumeration given just their public identifier:

  * [Data Exchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html) data sets – As AWS eloquently states, “AWS Data Exchange is a service that makes it easy for AWS customers to exchange data in the cloud”. There are even public data sets that can be bought and sold on the AWS Marketplace. Data assets are grouped into data sets, which are addressed with a 32 alphanumeric character identifier, e.g. “935c01c3a7f5e3499df7dff4dedeebae”. The “dataexchange:GetDataSet” operation is used to access a given dataset and is vulnerable to conditional love.
  * [Lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html) URL invocation – Lambda functions can be configured to be executable via a simple HTTPS endpoint. The idea is you send a web request without the extra mucking around with API Gateway. The URL includes a random 32 alphanumeric character identifier, e.g. “https://zowoqxdmbmrm6iudgpuo57p2ma0lxolt.lambda-url.us-east-1.on.aws/”. While it’s typical to make these endpoints completely public, it’s also possible to require authentication via the “AWS_IAM” mode. Public Lambda functions URLs do not process condition keys when invoked, however when in “AWS_IAM” mode policies are fully evaluated and therefore vulnerable to conditional love.
  * [API Gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html) invocation – Similarly to Lambda function URLs, API gateway invocation is vulnerable when in “AWS_IAM” mode. API gateway endpoints are shorter, e.g. “https://vafkcspga1.execute-api.us-east-1.amazonaws.com/”. They also differ in that execution happens under a separate service and action, “execute-api:Invoke”.

There’s no material difference to how this works for these services. Instead of using “s3:ResourceAccount” in the policy, use “aws:ResourceAccount”, and replace the action with the target service and API call.

`{  
"Version": "2012-10-17",  
"Statement": [  
{  
"Sid": "AllowResourceAccount",  
"Effect": "Allow",  
"Action": ["SERVICE_NAME:*"],  
"Resource": "*",  
"Condition": {  
"StringLike": {"aws:ResourceAccount": ["PARTIALSTRING*"]}  
}  
}  
]  
}`

The end.

Just kidding.

Turns out, if you keep reading the docs, you learn more interesting stuff. Like that there are global other condition keys that operate on the destination rather than the source.

`aws:ResourceOrgPaths  
aws:ResourceOrgID  
aws:ResourceTag/{tag-key}  
lambda:FunctionArn`

The answer is “Yes”. Yes you can apply the same technique to these conditions to enumerate your friend’s OrgID and tags values.

AWS explicitly states that confidential or otherwise sensitive data should never be put in tags.

![](https://cdn.prod.website-files.com/663cfee0a192fe7e5bd05ee8/66954071e64b9b30e21c68b4_no-sensitive-data-in-tags.png)

However, AWS users often aren’t aware of, or don’t implement this well-reasoned guidance. As a cloud security platform we at Plerion do encounter credentials and other secrets in tags more than we’d hope. We hope for _never_ but ¯\\_(ツ)_/¯ attackers don’t care about our hopes and dreams.

There’s another mitigating factor. You have to know / guess the tag key in order to enumerate a tag value. If an organisation has an esoteric tagging system, they are more protected through their excellent use of obscurity.

Unfortunately, there are a bunch of tag keys that are pretty common. CloudFormation [creates some tags automatically](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html):

`aws:cloudformation:logical-id  
aws:cloudformation:stack-id  
aws:cloudformation:stack-name`

AWS [publishes recommended tags](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-tags.html):

`AppName  
AppId  
EnvironmentType  
OwnerTeamEmail  
ComplianceFramework  
CostCenter  
Customer  
DataClassification  
HoursOfOperation  
OwnerTeam  
PatchGroup  
ProjectId  
SupportPriority`

What would you put in your hacker wordlist?

As your reward for diligently reading this blog post we’re also releasing [Conditional Love](https://github.com/plerionhq/conditional-love/), our AWS metadata enumeration tool.

Never again will you have to grind your fingertips to the bone as you manually attach and detach policies. Simply setup a role for testing with all the necessary permissions, install python, and get going. Here are some examples of what it can do:

Identify the value of the OwnerEmail tag of a role you can assume:

`% ./conditional-love.py --profile=<YOUR_CLI_PROFILE> \  
--role=<YOUR_ROLE_ARN_TO_ASSUME> \  
--action=sts:AssumeRole \  
--condition=aws:ResourceTag \  
--tag-key=OwnerEmail \  
--target=<TARGET_ROLE_ARN> \  
--alphabet=abcdefghijklmnopqrstuvwxyz.@  
Starting to be wrong. Please be patient...  
=>d  
=>da  
=>dag  
=>dagr  
=>dagrz  
=>dagrz@  
=>dagrz@p  
=>dagrz@pl  
=>dagrz@ple  
=>dagrz@pler  
=>dagrz@pleri  
=>dagrz@plerio  
=>dagrz@plerion  
=>dagrz@plerion.  
=>dagrz@plerion.c  
=>dagrz@plerion.co  
=>dagrz@plerion.com`

Identify the Organisation ID the ‘Commoncrawl’ S3 bucket belongs to:

`% ./conditional-love.py --profile=<YOUR_CLI_PROFILE> \  
--role=<YOUR_ROLE_ARN_TO_ASSUME> \  
--action=s3:HeadObject \  
--condition=aws:ResourceOrgID \  
--target=s3://commoncrawl/ \  
--alphabet=abcdefghijklmnopqrstuvwxyz-  
Starting to be wrong. Please be patient...  
=>o  
=>o-  
=>o-f  
=>o-fz  
=>o-fz?  
=>o-fz??  
=>o-fz???  
=>o-fz????  
=>o-fz?????  
=>o-fz?????o  
=>o-fz?????ot`

Identify the account ID that the Carvana ‘Car Sales for United States’ DataExchange dataset belongs to:

`% ./conditional-love.py --profile=<YOUR_CLI_PROFILE> \  
--role=<YOUR_ROLE_ARN_TO_ASSUME> \  
--action=dataexchange:GetDataSet \  
--condition=aws:ResourceAccount \  
--target=935c01c3a7f5e3499df7dff4dedeebae \  
--region=us-west-2  
Starting to be wrong. Please be patient...  
=>1  
=>10  
=>102  
=>102?  
=>102??  
=>102???  
=>102????  
=>102?????  
=>102??????  
=>102??????7  
=>102??????70  
=>102??????709`

At release Conditional Love supports the following actions:

`s3:HeadObject  
dataexchange:GetDataSet  
lambda:InvokeFunctionUrl  
execute-api:Invoke  
sts:AssumeRole  
sqs:ReceiveMessage`

And the following conditions:

`s3:ResourceAccount  
aws:ResourceAccount  
aws:ResourceOrgPaths  
aws:ResourceOrgID  
aws:ResourceTag  
lambda:FunctionArn`

Notice that not all target resource conditions start with “Resource”.

Adding more actions or conditions is trivial so check out the code if you are interested.

One question remains, what can AWS customers do to protect themselves from this kind of enumeration?

  * Do some basic threat modelling. Ask yourself, what could happen if all of our tags, account IDs and organisation IDs became public?
  * Assume everything in resource tags is public. Never put confidential information in tags and implement a cloud security a tool like Plerion to identify when that happens.
  * Where reasonable, publish resources like Images, lambda layers, applications, and integrations from separate purpose-built AWS accounts as source account IDs are also published as part of the process. Avoid doing so from production accounts.
  * Given that only principals that have access to a resource can enumerate metadata, AWS recommends customers ensure only authorized accounts are listed within their policies. This will prevent the ability of unauthorized accounts to perform actions on resources.

As this post goes to virtual print, I’m wondering to myself – is this technique more dangerous within a single account? If an attacker lands within a constrained context in an account, it’s reasonable to assume they’ll be able to map its tagging schema and list the resources they might have access to. Should there be any advantage to be gained from metadata enumeration, they’ll be in a perfect position to maximise it. Something to ponder.

A lot of time and love from the Plerion team went into making this happen. If you enjoyed this blog, please share it.

‍

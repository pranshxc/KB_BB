---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-22_aws-security-flaw-which-can-grant-admin-access.md
original_filename: 2018-05-22_aws-security-flaw-which-can-grant-admin-access.md
title: AWS Security Flaw which can grant admin access!
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 4e1bb742c1952db2c9b8e0b4922f7de37c41b09ecbadfabd4868e9c2c8e18a38
text_sha256: ebd90e8852fdea99abc45598a3f3f04fb73a38d8b8fdc2c10854c6b491b74922
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# AWS Security Flaw which can grant admin access!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-22_aws-security-flaw-which-can-grant-admin-access.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4e1bb742c1952db2c9b8e0b4922f7de37c41b09ecbadfabd4868e9c2c8e18a38`
- Text SHA256: `ebd90e8852fdea99abc45598a3f3f04fb73a38d8b8fdc2c10854c6b491b74922`


## Content

---
title: "AWS Security Flaw which can grant admin access!"
url: "https://medium.com/ymedialabs-innovation/an-aws-managed-policy-that-allowed-granting-root-admin-access-to-any-role-51b409ea7ff0"
authors: ["Sharath AV"]
programs: ["Amazon"]
bugs: ["Broken authorization"]
publication_date: "2018-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5872
scraped_via: "browseros"
---

# AWS Security Flaw which can grant admin access!

AWS Security Flaw which can grant admin access!
Sharath AV
Follow
5 min read
·
May 22, 2018

172

2

I recently discovered an AWS Managed Policy that potentially allowed granting admin access to self or any other IAM role. This blog-post describes my findings and my interactions with AWS Security team on the same.

For a particular project, we were using SSO for AWS Account login using Okta. In this, the permissions to users are given through IAM Roles. I was one of the users having been given limited access to AWS account through an IAM role. I accidentally discovered one day that I was able to put any inline policy to other IAM roles. Perplexed by this, I went to IAM console to check if I have admin access or any other policies attached related to AWS IAM. I noticed that none of the policies assigned to my role were related to IAM service and nor did I have admin access. But I could potentially grant admin privilege to any other IAM role.

For instance, I could add a new inline policy with the below JSON(which grants the role admin privileges):

{
“Version”: “2012–10–17”,
“Statement”: [{
“Effect”: “Allow”,
“Action”: “*”,
“Resource”: “*”
}]
}

After discovering this, I sent out a report of my findings to AWS security team on March 19th 2018. They then asked more details on which IAM role I am referring and to give detailed steps to reproduce the same. So I followed up with them to provide the requested details. Later, their security team member acknowledged about this issue by saying:

“I’ve reviewed this, and I’ve found out why you’re able to add an inline policy — the role you are using has the managed policy “AmazonElasticTranscoderFullAccess” attached. This grants (among other things) the “iam:PutRolePolicy” permission, which is what allows you to attach an inline policy to the role.
I’ve reached out to the Elastic Transcoder team to review if this is necessary, and we’ll take appropriate action as required.”

So, this AWS Managed IAM policy(AmazonElasticTranscoderFullAccess) potentially allowed it’s grantee to in turn grant admin access(or any other access) to any other roles. Though this policy wasn’t related to IAM, it allowed changing access to other IAM roles.

I hoped that they would take quick action on this issue, as this was a serious security flaw (allowing granting of admin access ). But I did not hear any updates from them for a long time. I wanted to make other AWS users aware of this, but that could have lead to misuse of the information, so I just posted vague information of it on /r/aws on reddit, from where I learnt about Responsible Disclosure. This post is my disclosure of my findings on the same having given 60 days of time for AWS team to address the issue. At the time of this posting, AWS team has deprecated the AmazonElasticTranscoderFullAccess policy that I had reported, and they have now created a new policy for replacement with the name AmazonElasticTranscoder_FullAccess (Notice the _ being added in the name), to which they want users to migrate to and circumvent this issue. The new policy does not have the iam:PutRolePolicy in its allowed actions as it was in the previous policy, so this issue should resolve the issue I had reported. However, the users who are still using the old managed policy(AmazonElasticTranscoderFullAccess) in their AWS Account should be aware of this vulnerability in the policy, and take necessary actions on the same.

Screenshots of deprecated policy:

Press enter or click to view image in full size

Here, you can see that the AmazonElasticTranscoderFullAccess policy grants iam:PutRolePolicy permission. And this policy is being deprecated by them ( notice the exclamation mark/icon in red).

For those interested to know more on my rest of the interaction/follow-ups with AWS security team, you can continue reading below:

Get Sharath AV’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I mailed them on April 3rd requesting details on any action being taken, their security team member responded with:

“My apologies for the delay in the response! I’ll check up on this and update you before the end of the week.”

Then on April 6th, their security team member wrote:

“The ETS team is in the processing of reviewing their managed policy to see how they can better scope the permissions to narrow down the granted access, and to ensure that scenarios like the one you reported are no longer possible. Once they have finalised a new policy, we’ll push out the update and it will be visible in the managed policies for the service.

Thank you again for your report!”

Then I told them that I would like to do a Responsible Disclosure on this issue, to which their security team member responded with:

“The service team proposed a change to correct the issue that you reported but as this is a complex issue we are carefully considering the side effects of that change.

If you would not mind, please send us a draft copy of your disclosure document so we can review it prior to publication. We will, of course, let you know when the fix is complete.”

I am posting this blog after I shared my draft of this blog post with them, and after they have sent out email notification to all users of the old policy to migrate to the new policy. Their email notification reads as below:

Subject: Managed Policy AmazonElasticTranscoderFullAccess Has Been Replaced [AWS Account: XXXXXXXXXXXX]

Hello,

Your AWS account has one or more IAM users or roles currently using the “AmazonElasticTranscoderFullAccess” managed policy.

We have released a new managed policy with improved access restrictions. Existing IAM users and roles can continue to use the previous policy without interruption, however new IAM users and roles will use the new replacement policy.

For any previous IAM users and roles using the original managed policy described above, we strongly encourage you to update those users and roles to use the new replacement policy called “AmazonElasticTranscoder_FullAccess” (note the underscore difference). This new managed policy has the improved access restrictions as mentioned.

Naturally, with improved access restrictions, the new policy does not include all the permissions that are included in the original policy. Before you migrate any user or role to the new replacement policy, we recommend you review their differences in the Policy section of AWS IAM console. If you require one or more of the removed permissions, please add them separately to any user or role.

If you require assistance or more information, please contact AWS Support: https://aws.amazon.com/support .

Sincerely,
Amazon Web Services

Edit: Updated blog contents to use only “admin” instead of “root/admin”, as admin is not same as root in AWS. Root has few privileges that admin users do not have.

Update: AWS security team sent the below items to me as a token of appreciation on this responsible disclosure:

Press enter or click to view image in full size

A water bottle, web cam cover, popsocket, and a lock sponge. I am not sure what to do with that sponge though :P

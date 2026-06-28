---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-07_spotted-how-we-discovered-privilege-escalation-missing-cloudtrail-data-and-a-rac.md
original_filename: 2023-06-07_spotted-how-we-discovered-privilege-escalation-missing-cloudtrail-data-and-a-rac.md
title: 'Spotted: How we discovered Privilege Escalation, missing CloudTrail data and
  a race condition in AWS Directory Service'
category: documents
detected_topics:
- access-control
- cloud-security
- sso
- command-injection
- race-condition
- api-security
tags:
- imported
- documents
- access-control
- cloud-security
- sso
- command-injection
- race-condition
- api-security
language: en
raw_sha256: ba1a9160cc138b11b6a8be50f8ca6e53db04732adcf7fdb1f185c6f178ef2b37
text_sha256: 07b8f94b6b5e18f467f5d38ac3b65c85cf20440f5da7cfbbaa44594747c01531
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Spotted: How we discovered Privilege Escalation, missing CloudTrail data and a race condition in AWS Directory Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-07_spotted-how-we-discovered-privilege-escalation-missing-cloudtrail-data-and-a-rac.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, sso, command-injection, race-condition, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `ba1a9160cc138b11b6a8be50f8ca6e53db04732adcf7fdb1f185c6f178ef2b37`
- Text SHA256: `07b8f94b6b5e18f467f5d38ac3b65c85cf20440f5da7cfbbaa44594747c01531`


## Content

---
title: "Spotted: How we discovered Privilege Escalation, missing CloudTrail data and a race condition in AWS Directory Service"
page_title: "Spotted: How we discovered Privilege Escalation, missing CloudTrail data and a race condition in AWS Directory Service | Cloudar"
url: "https://cloudar.be/awsblog/spotted-privilege-escalation-in-aws-directory-service/"
final_url: "https://cloudar.be/awsblog/spotted-privilege-escalation-in-aws-directory-service/"
authors: ["Ben Bridts (@benbridts)"]
programs: ["AWS"]
bugs: ["Cloud", "Privilege escalation", "Race condition"]
publication_date: "2023-06-07"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 1070
---

[ 07 Jun 2023](https://cloudar.be/2023/06/) ____[Ben Bridts](https://cloudar.be/author/bbridts/) __[Security& Compliance](https://cloudar.be/category/security-compliance/)

07/06/2023 Ben Bridts

It takes a village to spot a bug. Recently, Cloudar discovered a set of bugs in AWS Directory Service. One of them could be used for privilege escalation by an authenticated user with sufficient permissions. We reached out to AWS and they have remediated this issue and [published a security bulletin](https://aws.amazon.com/security/security-bulletins/AWS-2023-003/). No customer action is required

## **The findings**

When you configure an AWS service to use an IAM role on your behalf, [you need to have the iam:PassRole permission](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in addition to the permissions required to configure and/or use the service.

Due to the bug we reported, AWS Directory Service didn’t verify the presence of those permissions when [assigning users or groups to an existing IAM role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/assign_role.html). This allowed users with the ds:EnableRoleAccess permission to assign users to any role in their account that [has a trust relationship with AWS Directory service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html).

Additionally, we found some actions that were not logged to CloudTrail and a validation that’s only done client-side

## **The discovery**

Cloudar is an [AWS Managed Service Provider Partner](https://aws.amazon.com/partners/programs/msp/), and as such, we work together with our clients to configure their environments. One of our clients alerted us of a strange behavior in the AWS Console for AWS Directory Service, which prompted us to take a deeper look behind the scenes of how that service works.

### Step 1: Missing CloudTrail Data

We had configured AWS Directory Service for AWS Management Console access for our client, and it was working properly for them. However, when looking in the console, the feature appeared to be disabled.

![A screenshot of the AWS Console showing that the "AWS Management Console" feature of AWS Directory Service is disabled.](https://cloudar.be/wp-content/uploads/2023/05/Picture-1.png)

Usually, we would investigate CloudTrail logs to see what disabled this, but at the time, we didn’t see an entry in CloudTrail that showed the enabling or disabling of access. When we tested what happened when changing the status ourselves, we also did not see those actions recorded in CloudTrail.

We’ve reported this to AWS, and enabling or disabling console access does now create events in CloudTrail (note: **OMITTED** is part of the CloudTrail event):
  
  
  {
  […]
     "eventSource": "ds.amazonaws.com",
     "requestParameters": {
         "directoryId": "d-123456789a",
         "applicationId": "***OMITTED***",
         "serviceAccountUserName": "***OMITTED***",
         "serviceAccountPassword": "HIDDEN_DUE_TO_SECURITY_REASONS"
     },
     "responseElements": null,
     "readOnly": false,
     "eventType": "AwsApiCall",
     "managementEvent": true,
     "sessionCredentialFromConsole": "true"
  }
  
  
  {
  […]
     "eventSource": "ds.amazonaws.com",
     "eventName": "UnauthorizeApplication",
     "requestParameters": {
         "directoryId": "d-123456789a",
         "applicationId": "***OMITTED***"
     },
     "responseElements": null,
     "readOnly": false,
     "eventType": "AwsApiCall",
     "managementEvent": true,
     "sessionCredentialFromConsole": "true"
  }

### Step 2: Looking at what the console does

Instead of looking through CloudTrail logs, we opened the development console in our browser. There we saw that it was sending requests to an undocumented API when enabling console access. There is no public API for enabling console access or assigning user to roles within Directory Service, so this wasn’t unexpected.

What _was_ unexpected was that when enabling or disabling console access, there were two calls to the internal API. One to (un)authorize an application called “AWSManagementConsole” and one to (un)authorize an application called “Directory Service console”.

Assuming there was a consistency problem, we investigated what happened if we only unauthorized one of them by sending requests to the undocumented API from the command line. When we unauthorized the “AWSManagementConsole” and authorized “Directory Service console”, we were able to reproduce our customer’s issue where the console would show “disabled”, but the sign-in would still work.

By the time we sent our report to AWS, the double API call didn’t happen anymore (only “AWSManagementConsole” is used today), so this seemed to have been a temporary issue. We still reported this behavior, indicating that we could no longer reproduce.

### Step 3: Finding a race condition

Since this wasn’t an easy bug to uncover, we had to read a lot of documentation to deeply understand what Directory Service was doing. While doing that, we noted an interesting sentence: “[If any IAM roles have been assigned to users or groups in the directory, the Disable button may be unavailable](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_management_console_access.html#console_disable).”

The word “may” seemed very ambiguous, especially after finding an issue where a network disconnection could lead to an unexpected state. We looked a bit further and realized that the expected behavior is that you can’t disable the integration if you still have users and/or groups assigned to roles.

![A screenshot showing an error message when trying to disable console access while there are still users assigned](https://cloudar.be/wp-content/uploads/2023/05/cannot-disable.png)

However, that check is done completely in the browser, and appears to be based on the state when the tab was loaded. This means you can disable the console access while still having users and/or groups assigned. You could do this by calling the same (undocumented) API that the console uses, or in the browser by 1) opening the console while there are no assignments 2) using a second tab to assign users and/or groups to a role 3) using the first tab to disable console access.

![A screenshot showing how the "AWS Console Access" feature is disabled while there are still users assigned](https://cloudar.be/wp-content/uploads/2023/05/disabled-with-users.png)

We’ve reported this issue to AWS, but don’t consider it a vulnerability as the assignments are not usable if the Console access is disabled.

### Step 4: Privilege escalation

Having discovered two APIs that did some part of their logic client-side, and having experimented with the role-assignment, we looked at other validations that should happen when you assign a Role to a user in a directory. To assign a specific role to a user or group:

  * you should have ds:EnableRoleAccess permission for the Directory Service domain;
  * the role you want to pass should have a trust policy that allows use in AWS Directory Service;
  * the role should be in the same AWS account;
  * you should have iam:PassRole permissions on the role.

When we tested these checks, we noticed that we could assign a role (within the same account), even if we didn’t have the right iam:PassRole permission. In certain setups, this could mean privilege escalation.

  * Imagine you have two people, Alice and Bob, managing a domain, and each of them is responsible for assigning users to specific IAM roles. Alice assigns people to Role A and Bob assigns people to Role B. They could abuse the missing iam:PassRole check to assign people to a role they are not responsible for. For example, Alice assigns herself (or someone else) to Role B.
  * Another possible scenario would be when a user has the required permissions to create and manage a domain in AWS Directory Service, but no IAM permissions (e.g., with the PowerUserAccess managed policy). If there is already a role that has a trust relationship with AWS Directory Service, that user could create their own domain and assume that existing role.

This issue has been completely fixed.

## Recommended actions

Taking advantage of this vulnerability required a specific configuration and a high level of permissions within Directory Service. AWS customers who were relying on iam:PassRole permissions for access control before 2023-05-12 should review their directory for misconfiguration and their CloudTrail logs for unexpected AssumeRole calls.

## Timeline

2023-04-07: Issue found and reported to AWS.

2023-04-07: Investigation started by AWS.

2023-04-13: Issue confirmed by AWS, and development of a fix in progress.

2023-04-24: Development finished and deployment of the fix in progress.

2023-05-12: Fix deployed globally.

## Acknowledgements

We would like to thank the AWS teams involved, especially the Security team for their open communication and helpful responses. I’d also like to thank my coworkers for diving deep when they see unexpected things in the AWS console.

## Reach out to us

I talked on [June 12 at fwd:cloudsec about how this journey showed the universal benefits of security features](https://pretalx.com/fwd-cloudsec-2023/talk/7BXVWM/), and you can [watch that talk on youtube](https://www.youtube.com/watch?v=ey3dwohF6BY).

  * ###### SHARE

  *  __
  * __
  * __
  * __
  * __

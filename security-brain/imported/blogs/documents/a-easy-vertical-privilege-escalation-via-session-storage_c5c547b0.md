---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-16_a-easy-vertical-privilege-escalation-via-session-storage.md
original_filename: 2023-09-16_a-easy-vertical-privilege-escalation-via-session-storage.md
title: A Easy Vertical Privilege Escalation via Session Storage
category: documents
detected_topics:
- business-logic
- jwt
- access-control
- command-injection
- otp
tags:
- imported
- documents
- business-logic
- jwt
- access-control
- command-injection
- otp
language: en
raw_sha256: c5c547b0ccbbb9ddc56f8d1b04e427796f252507a24591277b85d35cac02843b
text_sha256: deefabb1e23b159d82fe9763b8d5cf1bd171580965a18111bcca49c12383dd1f
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# A Easy Vertical Privilege Escalation via Session Storage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-16_a-easy-vertical-privilege-escalation-via-session-storage.md
- Source Type: markdown
- Detected Topics: business-logic, jwt, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `c5c547b0ccbbb9ddc56f8d1b04e427796f252507a24591277b85d35cac02843b`
- Text SHA256: `deefabb1e23b159d82fe9763b8d5cf1bd171580965a18111bcca49c12383dd1f`


## Content

---
title: "A Easy Vertical Privilege Escalation via Session Storage"
url: "https://amjadali110.medium.com/a-easy-vertical-privilege-escalation-via-session-storage-cfa9f558c94"
authors: ["Amjad Ali"]
bugs: ["Privilege escalation"]
publication_date: "2023-09-16"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 774
scraped_via: "browseros"
---

# A Easy Vertical Privilege Escalation via Session Storage

A Easy Vertical Privilege Escalation via Session Storage
Amjad Ali
Follow
4 min read
·
Sep 15, 2023

128

2

Hey everyone 👋,

I hope all is well. After a gap of one month, I’m back with another write-up. If you missed my previous story, “A High-Impact Payment Bypass on a Government Website — A Tale of Business Logic Flaw Exploitation” you can catch up on it here:- https://amjadali110.medium.com/a-high-impact-payment-bypass-on-government-website-a-tale-of-business-logic-flaw-exploitation-b158feb7826a
In this write-up, I want to share the story of my recent discovery, Vertical Privilege Escalation via Session Storage, which I discovered on a private program and got 3($$$) digits bounty. So, without further more delay, let’s dive into the details.

Press enter or click to view image in full size

This was a CRM portal, and it had two different user roles: Normal User and Admin. As part of my testing, I logged in using a Normal User account to explore the functionalities of the web app. Normal Users had only limited resources and features access and couldn’t modify data within the portal. While surfing through the website, I checked the Local Storage and Session Storage. In the Session Storage, I saw the “userPermissionsList” object, which contains a JSON array of user permissions.

Press enter or click to view image in full size

So, I quickly logged in as an admin account. Admins had complete access to resources and features and could modify data within the portal. I also checked the Session Storage within the admin account and compared the admin and normal user “userPermissionsList” objects, which contained JSON arrays of user permissions.

The initial permissions for a normal user look like this:

[
  {"permissionId": 1, "permissionName": "CanGetApplicants"},
  {"permissionId": 5, "permissionName": "CanGetUsers"},
  {"permissionId": 8, "permissionName": "CanGetApplications"},
  {"permissionId": 9, "permissionName": "CanResendEmails"},
  {"permissionId": 18, "permissionName": "CanGetCustomers"},
  {"permissionId": 22, "permissionName": "CanGetUserActivity"}
]

The initial permissions for a admin look like this:

[
  {"permissionId": 1, "permissionName": "CanGetApplicants"},
  {"permissionId": 2, "permissionName": "CanCreateApplicants"},
  {"permissionId": 3, "permissionName": "CanUpdateApplicants"},
  {"permissionId": 4, "permissionName": "CanManageAccounts"},
  {"permissionId": 5, "permissionName": "CanGetUsers"},
  {"permissionId": 6, "permissionName": "CanCreateUsers"},
  {"permissionId": 7, "permissionName": "CanUpdateUsers"},
  {"permissionId": 8, "permissionName": "CanGetApplications"},
  {"permissionId": 9, "permissionName": "CanResendEmails"},
  {"permissionId": 10, "permissionName": "CanGetDocuments"},
  {"permissionId": 11, "permissionName": "CanUploadDocuments"},
  {"permissionId": 12, "permissionName": "CanCreateIndividualInvitations"},
  {"permissionId": 14, "permissionName": "CanQueryIndividualInvitations"},
  {"permissionId": 15, "permissionName": "CanGetBulkInvitations"},
  {"permissionId": 16, "permissionName": "CanUploadBulkInvitationsFile"},
  {"permissionId": 17, "permissionName": "CanUpdateFormStatus"},
  {"permissionId": 18, "permissionName": "CanGetCustomers"},
  {"permissionId": 19, "permissionName": "CanResendInvitations"},
  {"permissionId": 20, "permissionName": "CanResendEvaluations"},
  {"permissionId": 21, "permissionName": "CanResendManualReviews"},
  {"permissionId": 22, "permissionName": "CanGetUserActivity"},
  {"permissionId": 23, "permissionName": "CanGetDeliveredDocuments"},
  {"permissionId": 24, "permissionName": "CanGetBillingTables"},
  {"permissionId": 25, "permissionName": "CanGetBillingTableHistoricalRecords"},
  {"permissionId": 26, "permissionName": "CanGetBillingTableDraftUpdateRecords"},
  {"permissionId": 27, "permissionName": "CanGetFeedbacks"},
  {"permissionId": 28, "permissionName": "CanUpdateBillingTables"},
  {"permissionId": 29, "permissionName": "CanUpdateUserEmail"},
  {"permissionId": 30, "permissionName": "CanGetTemplates"},
  {"permissionId": 31, "permissionName": "CanResendApplicationEmail"},
  {"permissionId": 32, "permissionName": "CanDeleteUpcomingUpdates"},
  {"permissionId": 33, "permissionName": "CanCreatePolls"},
  {"permissionId": 34, "permissionName": "CanGetPolls"},
  {"permissionId": 35, "permissionName": "CanUpdatePolls"},
  {"permissionId": 36, "permissionName": "CanNotifyIndividualInvitations"},
  {"permissionId": 37, "permissionName": "CanSendInvitationEmail"}
]

Upon reviewing these “userPermissionsList” objects, I discerned a potential vulnerability. To test it, I returned to the Normal User account.

Understanding Local Storage and Session Storage

Before diving into the vulnerability exploitation, it’s essential to grasp the concept of Local Storage and Session Storage.

Get Amjad Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What is Local Storage & Session Storage?”

LocalStorage and SessionStorage are browser storage features introduced in HTML5. It allows saving data in key-value pairs in web browsers via JavaScript. Usually, most of the browsers support up to 5MB browser storage and will enable us to save more data efficiently.

Attempting to Exploit the Vulnerability

With the collected information, I proceeded to the Normal User account and navigated to the “Session Storage” section. Inside Session Storage, I located the “userPermissionsList” object, containing a JSON array of user permissions. I modified the Admin Account “userPermissionsList” object to Normal User in the Session Storage to gain admin-level access. After making these changes, I refreshed the page, and to my amazement, I gained unauthorized access to administrative-level resources and features, achieving an effortless Vertical Privilege Escalation.
I promptly reported this issue, and after two days, I received a response from the program managers, along with a three-digit bounty ($$$).

Press enter or click to view image in full size

It’s worth noting that many Bug Bounty Hunters overlook Local Storage and Session Storage. I strongly recommend always checking these storage mechanisms, as they may contain sensitive information such as JWT token, Email/Password, as well as PII etc.

I hope this write-up offers you valuable insights and aids you in your future endeavors. Thank you for taking the time to read about my experience. If you have any thoughts or questions, please feel free to share them in the comments section.

My Linkedin: https://www.linkedin.com/in/amjadali110/

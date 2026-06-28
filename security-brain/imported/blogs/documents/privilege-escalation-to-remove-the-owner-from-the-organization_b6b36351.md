---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-09_privilege-escalation-to-remove-the-owner-from-the-organization.md
original_filename: 2022-12-09_privilege-escalation-to-remove-the-owner-from-the-organization.md
title: Privilege Escalation to remove the owner from the organization
category: documents
detected_topics:
- access-control
- api-security
- sso
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- access-control
- api-security
- sso
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: b6b363516bc15aba31a9678588b7a43f5dfb61564e040aca1fc706c6aa0c6179
text_sha256: f6f6748b06050418294cb23960f1ed6a7388dd446b8b8cea65802da407940ef1
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation to remove the owner from the organization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-09_privilege-escalation-to-remove-the-owner-from-the-organization.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sso, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `b6b363516bc15aba31a9678588b7a43f5dfb61564e040aca1fc706c6aa0c6179`
- Text SHA256: `f6f6748b06050418294cb23960f1ed6a7388dd446b8b8cea65802da407940ef1`


## Content

---
title: "Privilege Escalation to remove the owner from the organization"
url: "https://medium.com/@kashyapherry147/privilege-escalation-to-remove-the-owner-from-the-organization-c029292a5d55"
authors: ["Hemant Kumar"]
bugs: ["Privilege escalation", "Mass assignment"]
publication_date: "2022-12-09"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1800
scraped_via: "browseros"
---

# Privilege Escalation to remove the owner from the organization

Privilege Escalation to remove the owner from the organization
HEMANT
Follow
4 min read
·
Dec 9, 2022

70

Hi Hackers,

Today, I am going to share one of my most interesting findings: a Privilege Escalation vulnerability that allowed an attacker to remove the owner of an organization and take control of the entire organization.

In this write-up, I’ll walk you through how I discovered the vulnerability, the impact it could have had, and the steps I took to validate and responsibly report it.

So, without wasting any more time, let’s get started.

I am not going to disclose the company’s name for privacy reasons, so let’s assume the target is:

https://organization.redacted.com

On November 19, 2022, I reported a Google Maps API key exposure issue to Redacted.com. Two days later, the security team triaged my report and assigned it a medium severity rating.

After seeing that my report had been accepted, I decided to spend more time hunting on the platform.

The application supported multiple user roles, including Owner and Administrator. To test the authorization model, I created two accounts:

Owner
Administrator

After analyzing the application, I noticed that administrators did not have permission to modify the organization’s settings. This made me curious about how the application enforced role-based access control.

I opened Burp Suite and began comparing requests made by both the Owner and Administrator accounts. While intercepting requests from the Owner account, I discovered a JSON parameter:

{
  "is_owner": true
}

This immediately caught my attention.

I started wondering whether it would be possible to elevate my privileges by manipulating this parameter.

To test the theory, I intercepted a request from the Administrator account and modified it to include the following data:

PUT /v1.2/organization/org-id/qid/[administrator-email-address] HTTP/2

Request body:

{
  "is_owner": true
}

After forwarding the request, the application accepted the change.

To my surprise, my Administrator account had now been promoted to an Owner account.

At this point, I had successfully identified a privilege escalation vulnerability. However, I wanted to understand the full impact of the issue.

I began investigating whether an Owner could remove another Owner from the organization. While testing with the Owner account, I intercepted a request responsible for removing users from the organization:

DELETE /v1.2/organization/org-id/user/owner-id HTTP/2

To perform this action, I first needed the target owner’s user ID.

Get HEMANT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After spending some time analyzing the application’s API endpoints, I discovered an endpoint that disclosed user information, including user IDs:

GET /v1.2/organization/6386d3e81dcec0115ea89f6d/user

With both the organization ID and the owner’s user ID available, I now had everything needed to test the impact of the privilege escalation vulnerability.

I intercepted another request in Burp Suite and modified it to target the owner’s account:

DELETE /v1.2/organization/org-id/user/owner-id

(Using the appropriate organization ID and owner ID.)

The request was successfully processed, demonstrating that a newly promoted Owner could remove the original Owner from the organization.

I sent the request and waited for the response.

And boom — I had successfully removed the original Owner from the organization.

At that point, my account remained the only Owner, effectively giving me complete control over the entire organization. This demonstrated the full impact of the vulnerability: an Administrator could escalate their privileges to become an Owner and then remove the legitimate Owner, resulting in a complete takeover of the organization.

This was a critical authorization flaw because it allowed an attacker to bypass the intended role hierarchy and gain full administrative control over an organization’s resources, settings, and users.

After validating the issue and documenting the impact, I responsibly reported the vulnerability to the company’s security team.

After validating the issue, I responsibly reported the vulnerability to the company.

Five days later, I received a response from the security team informing me that the report had been marked as a duplicate. To be honest, I was disappointed because the vulnerability had a significant impact.

What made it even more frustrating was that I later reported another privilege escalation vulnerability and a 2FA bypass issue, and both of those reports were also marked as duplicates.

At the time, I felt discouraged and questioned whether all the effort had been worth it. However, I eventually realized an important lesson:

If you’re a bug bounty hunter, duplicates are simply part of the journey.

Every duplicate report means that you were thinking in the right direction and finding real vulnerabilities. Sometimes another researcher just happens to get there first. What matters is continuing to learn, improve your methodology, and keep hunting.

Don’t let duplicates discourage you. Stay consistent, stay curious, and keep pushing forward. Your next report could be the one that makes all the hard work worthwhile.

Thanks for reading, amazing hackers!

Happy Hacking!

Instagram: https://www.instagram.com/cyber__hawk/

Linkedin: https://www.linkedin.com/in/hemant-714564199/

Twitter: https://twitter.com/Herry51130182

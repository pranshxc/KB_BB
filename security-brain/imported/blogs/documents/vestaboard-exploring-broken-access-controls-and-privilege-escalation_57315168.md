---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-06_vestaboard-exploring-broken-access-controls-and-privilege-escalation.md
original_filename: 2024-08-06_vestaboard-exploring-broken-access-controls-and-privilege-escalation.md
title: 'Vestaboard: Exploring Broken Access Controls and Privilege Escalation'
category: documents
detected_topics:
- access-control
- jwt
- sqli
- command-injection
- graphql
- api-security
tags:
- imported
- documents
- access-control
- jwt
- sqli
- command-injection
- graphql
- api-security
language: en
raw_sha256: 573151685438b5ff281860b30ff7e7d89f7fa2ee6ad10a5ba8fa61dd694c8588
text_sha256: f589d29c9c312ac8d19479dc2a53fab1be2169fc3cc4458b061729d36d20accf
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Vestaboard: Exploring Broken Access Controls and Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-06_vestaboard-exploring-broken-access-controls-and-privilege-escalation.md
- Source Type: markdown
- Detected Topics: access-control, jwt, sqli, command-injection, graphql, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `573151685438b5ff281860b30ff7e7d89f7fa2ee6ad10a5ba8fa61dd694c8588`
- Text SHA256: `f589d29c9c312ac8d19479dc2a53fab1be2169fc3cc4458b061729d36d20accf`


## Content

---
title: "Vestaboard: Exploring Broken Access Controls and Privilege Escalation"
page_title: "Vestaboard: Exploring Broken Access Controls and Privilege Escalation - Rhino Security Labs"
url: "https://rhinosecuritylabs.com/research/vestaboard-vulnerabilities/"
final_url: "https://rhinosecuritylabs.com/research/vestaboard-vulnerabilities/"
authors: ["Tyler Ramsbey (@Tyler_Ramsbey)"]
programs: ["Vestaboard"]
bugs: ["Broken Access Control", "Privilege escalation"]
publication_date: "2024-08-06"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 95
---

[ Strategic and Technical Blog ](https://rhinosecuritylabs.com/blog)

____

[Research](https://rhinosecuritylabs.com/research/)

![](https://rhinosecuritylabs.com/wp-content/uploads/2024/06/blank_vesta_resized-1140x400.png)

# Vestaboard: Exploring Broken Access Controls and Privilege Escalation

Tyler Ramsbey

## Overview of Vulnerabilities

During research on the Vestaboard web platform, the Rhino research team identified three instances of Broken Access Controls.

  1. Read-Access to other Vestaboards. 
  2. Ability to update names of other users. 
  3. Privilege escalation from Admin to Owner. 

Upon disclosure, Vestaboard responded promptly and fully remediated the identified vulnerabilities. 

## What is Vestaboard?

Vestaboard is a smart messaging display that allows users to send and display messages. Unlike traditional displays, Vestaboard combines physical and digital elements to create a unique visual experience. Users can send messages, create designs, display real-time information, and integrate with various applications. Vestaboard can be controlled from a mobile application or web interface–our research was performed on the web interface.

## 1\. Read-Access to other Vestaboards

Vestaboard provides the ability to share Vestaboard content with others. The generated URL allows anyone to access the Vestaboard content if they have the unique Board ID in this format: [https://web.vestaboard.com/simulator/[board-id](https://web.vestaboard.com/simulator/\[board-id)]. When a user logs into Vestaboard on the web interface, the Board ID is passed in the URL. Consequently, it’s possible to obtain the Board ID of other users by viewing the user’s browser history or finding it in various logs. Some boards can be discovered via this Google search: “site:[web.vestaboard.com/simulator](http://web.vestaboard.com/simulator)”. 

The image above shows the “share” button to generate the URL. 

With access to a Board ID, an unauthenticated attacker has persistent access to all content on the Vestaboard. Since Vestaboard can be integrated with company-specific channels (such as Slack channels) this could lead to sensitive information being leaked. 

The image above shows a password on the target Vestaboard being viewed by an unauthenticated attacker. 

## 2\. Ability to Update Names of Other Users

We discovered broken access control that allows attackers to update the first and last name of users in other tenants. By creating a free user account unrelated to the target and updating the account’s profile information, it sends a request to the /graphql endpoint. This request includes an input for the user’s ID and does not correlate the permissions between the authenticated JWT and user being targeted. If this ID is modified to target another user, the request is successful and the target user’s name is updated. 

Our attempts to increase the impact by updating the victim’s email or password were unsuccessful. Vestaboard requires re-authentication for updating the email/password for an account. This defense-in-depth practice prevented us from facilitating account takeover. 

The image above shows the attacker targeting another account by replacing the “id” parameter in the POST request.

This update affects the targeted user’s primary account so the change is reflected in every Vestaboard tenant they are in. 

The image above shows the successful name change of the victim. 

## 3\. Privilege Escalation from Admin to Owner

In the Vestaboard platform there are three different user roles:

  * **User:** Create, schedule, and edit messages. 
  * **Admin:** Set quiet hours, time zones, and manage users. 
  * **Owner:** Delete messages, delete the Vestaboard, manage billing, and transfer ownership. Vestaboard is designed to only allow one Owner per tenant. 

Since Admins have permission to manage users, they can modify roles to change a User to an Admin from the web interface. 

The image above shows the Admin’s ability to modify the User and Admin roles. 

The Admin cannot make another user the Owner since the Owner is an elevated role with greater access to the Vestaboard tenant. By changing the role of another user and capturing the request with Burp Suite, it’s possible to manually add the Owner role and elevate permissions of an account from Admin to Owner. The new Owner then has full tenant access. 

The image above shows us manually adding the “Owner” role in the request. 

## Conclusion

Vestaboard not only fixed the vulnerabilities we reported to them but also served as an example of how vendors should work with security researchers. We want to sincerely thank Vestaboard for their quick response to patch these instances of broken access control. 

As always, feel free to follow us on Twitter or LinkedIn and join our Discord server for more releases and blog posts. 

Twitter: [https://twitter.com/rhinosecurity](https://twitter.com/rhinosecurity)

LinkedIn: [https://www.linkedin.com/company/rhino-security-labs/](https://www.linkedin.com/company/rhino-security-labs/)

Discord: [https://discord.gg/TUuH26G5](https://discord.gg/TUuH26G5)

Researcher/Author: [https://youtube.com/@TylerRamsbey](https://youtube.com/@TylerRamsbey)

## Disclosure Timeline

**Date** | **Event**  
---|---  
11/15/2023 | Issues reported to Vestaboard  
11/15/2023 | Vestaboard acknowledged the vulnerability and began working on a fix  
12/06/2023 | Vestaboard releases patch to address the vulnerabilities  
08/06/2024 | Rhino published details on vulnerabilities  
  
## Related Resources

### Referral Beware, Your Rewards are Mine (Part 1)

[](https://rhinosecuritylabs.com/research/referral-beware-your-rewards-are-mine-part-1/)

### Multiple CVEs in Infoblox NetMRI: RCE, Auth Bypass, SQLi, and File Read Vulnerabilities 

[](https://rhinosecuritylabs.com/research/infoblox-multiple-cves/)

### CVE-2025-26147: Authenticated RCE In Denodo Scheduler 

[](https://rhinosecuritylabs.com/research/cve-2025-26147-authenticated-rce-in-denodo/)

## Interested in more information?

20603 

[ Contact Us Today  __ ](https://rhinosecuritylabs.com/contact/)

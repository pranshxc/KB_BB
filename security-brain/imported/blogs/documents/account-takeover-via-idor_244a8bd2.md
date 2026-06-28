---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-04_account-takeover-via-idor.md
original_filename: 2020-09-04_account-takeover-via-idor.md
title: Account Takeover via IDOR
category: documents
detected_topics:
- access-control
- idor
- command-injection
- supply-chain
tags:
- imported
- documents
- access-control
- idor
- command-injection
- supply-chain
language: en
raw_sha256: 244a8bd24ced48b0d9a03db98971937627730e0bbbbddce2ce36f4c8cf287e48
text_sha256: b9f755c2cb15e9a6062c800441651822b50fee079f9c9a1468e78aa37260804b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-04_account-takeover-via-idor.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `244a8bd24ced48b0d9a03db98971937627730e0bbbbddce2ce36f4c8cf287e48`
- Text SHA256: `b9f755c2cb15e9a6062c800441651822b50fee079f9c9a1468e78aa37260804b`


## Content

---
title: "Account Takeover via IDOR"
page_title: "Account Takeover via IDOR - Deteact - continuous information security services"
url: "https://blog.deteact.com/account-takeover-via-idor/"
final_url: "https://blog.deteact.com/account-takeover-via-idor/"
authors: ["Roma Ramazanoff (@r0hack)"]
bugs: ["IDOR", "Account takeover"]
bounty: "25,000"
publication_date: "2020-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4280
---

# Account Takeover via IDOR

[September 4, 2020September 11, 2020](https://blog.deteact.com/2020/09/04/) [r0hack](https://blog.deteact.com/author/r0hack/)

**Insecure Direct Object Reference (IDOR)** is a very common type of weakness in the application authorization logic. The potential damage from IDOR exploitation can be either minimal or critical. Let’s consider some cases when the presence of IDOR allowed to perform an attack with a high impact level – account takeover or project takeover.

![](https://blog.deteact.com/ru/wp-content/uploads/sites/2/2020/08/image5-1024x592.png)

Account takeover gives the attacker full or nearly full access to the victim’s account.

Project takeover gives the attacker access to a separate project created inside a user account. Often, the attack does not allow the full takeover of the account, but you can control some resources belonging to another user (for example, a project or an internal user created by the administrator). I have repeatedly encountered such vulnerabilities in Bug Bounty programs.

### **What is this IDOR?**

IDOR — is an Insecure Direct Object Reference. This flaw is often explained by the example of the helpdesk interface: by changing the ticket ID you can read the tickets of other users. But in fact, the IDOR is not limited to changing the numeric identifier to read the data, the result of an attack can lead to the data altering.

There are also cases where it is difficult to guess the ID, for example, it could be a hash or UUID, in this case, the risk is greatly reduced. But in my practice, it has almost always been possible to find ways to find out the ID of the victim.

I think that IDOR can be divided into sub-types by the type of resulting action:

  1. Data reading
  2. Data altering
  3. Privilege escalation (a special case of data change)
  4. Account takeover (private case of privilege escalation)

Consider an example of using IDOR to capture an account or project.

## **IDOR leads to Account TakeOver**

How can IDOR lead to the takeover of an account or any other entity that is created inside an account (most often it is an internal project)? For example, a user creates a manager or some project in their account, and control over these entities may be captured by an attacker.

It is not so easy to hack the main account or a user session, because the main account is usually not directly accessible to the attacker from their account. The main account takeover is often done via the entities of the account, for example, via a project or the manager (a lower privilege user connected to the project). Below are some specific cases from Bug Bounty.

### **IDOR when adding and deleting a project in a group**

There are projects with different subscription plans that can be purchased for a certain price. There is also a special Enterprise plan, which adjusts to the client depending on their needs. In one of the projects, when you connect the Enterprise plan, you can add usual projects to the group, and then they also get the Enterprise status.

IDOR was detected in two places at once: when you add a project to an Enterprise-group and when you delete it. When adding a project, everything was trivial: a POST request with JSON body was passed, which contained the project name that was open for everyone, so you could add someone else’s project to your group and get control over it:

POST /api/projects/victim/children HTTP/1.1 Host: victim.com {"subdomain":"victim1"}

1234 | POST /api/projects/victim/children HTTP/1.1Host: victim.com {"subdomain":"victim1"}  
---|---  
  
Another exploit was a little more tricky. The process of project deletion from a group was implemented logically incorrectly. When a project was deleted, a POST request with a complete description of the group was passed in a serialized form, but the ID of the project, whose deletion was requested, was omitted.

You could simply add or change the project ID in the JSON body and point it to someone else’s project.

The exploitation was complicated by the fact that the ID was a random value, which could not be guessed. But it was possible to find a way to find the project ID through the frontend: you could navigate to the project page (the projects had corresponding public pages) and find the ID in the HTML code:

![](https://blog.deteact.com/ru/wp-content/uploads/sites/2/2020/08/image.png)

Final request:

Host: victim.com Cookie: ... {"childrenProjects":&#91;"id_project1","id_project2","id_project_victim"]}

1234 | Host: victim.comCookie: ... {"childrenProjects":&#91;"id_project1","id_project2","id_project_victim"]}  
---|---  
  
### **IDOR in user reassignment**

This attack used 2 vulnerabilities at once, thanks to the chain a very high risk level was obtained. These are Improper Access Control and IDOR .

Due to incorrectly configured access, you could view other people’s projects and managers that were linked to these projects. This vulnerability already allowed to steal some confidential data.

But in the course of further study of the application, another drawback was found, which allowed connecting someone else’s manager to your account by their identifier (so it is IDOR), when updating the profile.

The manager’s ID could be recognized through previous vulnerability. By connecting someone else’s manager to his account, the attacker got privileges of this manager and got control over his project, the access allowed to view and edit data.

We are talking about a vulnerability described in the [Cross-organization data access in city-mobil.ru](https://hackerone.com/reports/863983) report. The vulnerability allowed access to data of more than 1 million drivers: passports, driver licenses. Also by capturing partner’s account, the attacker could change drivers’ data, which were registered with this partner (taxi company).

## Takeaways

More than $25,000 was paid for the vulnerabilities described above, and the potential damage from the cybercriminals’ actions could exceed this amount many times.

To avoid such losses, analyze the security of your projects in a timely manner. Contact us for [security assessment and penetration testing services](https://pentest.deteact.ru/).

[Bug Bounty](https://blog.deteact.com/category/research/bug-bounty/) [Research](https://blog.deteact.com/category/research/) [Uncategorized](https://blog.deteact.com/category/uncategorized/) [Web Security](https://blog.deteact.com/category/research/web/)

## Post navigation

[PREVIOUS POST Previous post: Defeating Google Closure Library Sanitizer](https://blog.deteact.com/google-closure-library-sanitizer-bypass/)

[NEXT POST Next post: We won The Standoff](https://blog.deteact.com/the-standoff-pwned/)

### Leave a Reply [Cancel reply](/account-takeover-via-idor/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Δ

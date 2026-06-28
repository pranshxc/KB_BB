---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-30_75k-google-cloud-platform-organization-issue.md
original_filename: 2019-01-30_75k-google-cloud-platform-organization-issue.md
title: $7.5k Google Cloud Platform organization issue
category: documents
detected_topics:
- cloud-security
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 14832d51765b2a3d30fd835ecae8b72887e2e4a196a8546044af5f50d458cd26
text_sha256: e9b904235d35d8864b0d4636c1ee80682b24f66176543a7e8a682c4b34d66399
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# $7.5k Google Cloud Platform organization issue

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-30_75k-google-cloud-platform-organization-issue.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `14832d51765b2a3d30fd835ecae8b72887e2e4a196a8546044af5f50d458cd26`
- Text SHA256: `e9b904235d35d8864b0d4636c1ee80682b24f66176543a7e8a682c4b34d66399`


## Content

---
title: "$7.5k Google Cloud Platform organization issue"
url: "https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html"
final_url: "https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html"
authors: ["Ezequiel Pereira (@epereiralopez)"]
programs: ["Google"]
bugs: ["Logic flaw"]
bounty: "7,500"
publication_date: "2019-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5439
---

###  $7.5k Google Cloud Platform organization issue 

on  [ January 30, 2019  ](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html "permanent link")

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[Google Cloud Platform (GCP)](https://cloud.google.com/) lets [G Suite](https://gsuite.google.com/) and [Cloud Identity](https://cloud.google.com/identity/) users create what are called "[Organizations](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)".  
  
GCP organizations can be used to easily manage resources (Such as projects, billing accounts, IAM roles, etc.) in one single place. Most resources cannot be detached from the organization they were created in, and even though they can be deleted, most of them can be restored within a month.  
Because of this, it is important that users pay attention to where they are putting their resources, for example: if for some reason they created a billing account on an organization they do not trust, they could end up being charged for the actions of someone else.  
  
But, how could they even get to create a resource in an organization?  
Well, they could either:  

  * Be part of the G Suite/Cloud Identity domain (i.e. An employee, or a student), and it wouldn't be anything unexpected.
  * Or the organization can be shared with them.

  
GCP organizations can be shared with any Google user through the [Cloud Identity & Access Management (IAM)](https://cloud.google.com/resource-manager/docs/access-control-org).  
So, if I shared it with several users, maybe one of them could accidentally create a resource in it, and I could manage that resource however I want.  
  
But, GCP organizations have names, their domains, so my organization was called "ezequiel.tech", wouldn't everyone realize they are creating resources in a weird organization they never saw before?  
Usually yes, but I found that for some reason this name could be changed through the (deprecated) [organizations.update method](https://cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/update) in the [Resource Manager](https://cloud.google.com/resource-manager/), even though the documentation said the "displayName" was read-only.  
  
With this, I could have my own organization and name it as another one and confuse users:  

  * I name my organization "<IMPORTANT-COMPANY>.com"
  * Share it with "domain:<IMPORTANT-COMPANY>.com" (Effectively sharing it with [every Google user with a @<IMPORTANT-COMPANY>.com account](https://cloud.google.com/iam/docs/overview#g_suite_domain))
  * Profit from unsuspecting users creating resources in my organization, specially billing accounts (Which can be closed, not deleted, and I can just re-open them and use them), or building projects that manage sensible information (For instance, a project that access other servers I previously had no credentials for)

  
There was another issue too, if I shared my GCP organization with a normal (@gmail.com) user, whenever they create a project the Google Cloud Console interface forced them to choose an organization, if mine was the only one they had access to, they would be forced to create a project in it (Note: The underlying API can create organization-less projects with no issue).  
I could have easily had called my organization "No organization" (There was no requirement for it to be a domain) and probably most users would have never realized what happened.  
For some reason this also removed the Google Cloud Platform free trial banner if the victim hadn't signed up to it already.  
  
Considering the simpleness of this attack (An attacker could just buy a $4 domain, and sign up for the 14-day free trial of G Suite and then create a GCP organization), and the effects this could have, I reported the issue to the [Google Vulnerability Rewards Program](https://g.co/vrp).  
  
They quickly fixed the causes of this issue, so now it is not possible to change the name of an organization, and when sharing it, users are not forced by the interface to create resources in the organization.  
  
Also, according to Google, this issue had an interesting effect if done against the "google.com" organization (They internally use "google.com" as a GCP organization for internal stuff), the fake organization would look more realistic than the real "google.com" organization, they even have a picture of how this looked like:  
  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDJQoP8kTg1wm1pjovB7qtVdte0mmLvwchnAl29xV2uQ33ql9HExDGfFdsL-hfoUdwLFARSHBOi2dU89xWBxg-Rs8T60BPKa0yCHymw768XLCvc6dRm4WUMhppjvYLWHvzUQG_wsKj2PH7/s320/download_20190129_160703.png)

_Picture the Google Security Team sent me: A fake organization is on top, the one below is the real one._

  
Obviously attacking the "google.com" organization could've had big effects, since confused Google employees using Google Cloud Platform could had created resources without realizing their mistake and do internal/confidential stuff (Although Google probably has lots of checks in order to avoid serious issues, and, after all, the platform if theirs).  
  
Because of all of this, on January 29th, 2019, I got a reward of 7500 dollars.  
  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLdgbxjdM9tIMBBS1MyvdQeO7FfllFxkslQjeBQ1pRSJdr-cZ6gHuqs8YLcD926LP_Fg9vRDHQ6lnvsNsdD8yHslpd1hGrJ3Sya1I_bIMYwRxFWfFnJbtnkic1J2nHM4Xd8qWOBzR-yEwm/s640/Screenshot_20190130_110549.png)

  

###  Timeline

  * Issue found and reported on November 29th, 2018
  * Issue quickly fixed
  * Reward decision delayed (Holidays)
  * Reward of $7500 issued on January 29th, 2019

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//2.bp.blogspot.com/_NkNHNz9XuD8/TIXE8gqAv1I/AAAAAAAAIrY/kp358NsJsjA/S45-s35/AAA%2BFBook%2BBsAs%2BGraciela%2By%2BGus_%2B022.jpg)

[Gustavo Ferrero](https://www.blogger.com/profile/14946577681148137866)[March 12, 2019 at 12:03:00 PM GMT-3](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html?showComment=1552403007578#c7176947084032543428)

Congrats Ezequiel! You did it again! Great job. More kudos must go to you once again! Standing ovation.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/7176947084032543428)

Replies

Reply

  2. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[June 21, 2019 at 4:23:00 PM GMT-3](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html?showComment=1561145005258#c9047800835945001217)

so guy, it's great, keep this.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/9047800835945001217)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Laura Bush](https://www.blogger.com/profile/14063697739786180181)[August 19, 2019 at 5:04:00 PM GMT-3](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html?showComment=1566245087392#c3103145364668388567)

This comment has been removed by a blog administrator.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/3103145364668388567)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/6070397520912981280?po=2848585614969085937&hl=en&saa=85391&origin=https://www.ezequiel.tech&skin=emporio)

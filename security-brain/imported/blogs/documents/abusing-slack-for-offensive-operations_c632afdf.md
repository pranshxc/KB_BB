---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-04_abusing-slack-for-offensive-operations.md
original_filename: 2020-03-04_abusing-slack-for-offensive-operations.md
title: Abusing Slack for Offensive Operations
category: documents
detected_topics:
- mfa
- supply-chain
- sso
- access-control
- sqli
- command-injection
tags:
- imported
- documents
- mfa
- supply-chain
- sso
- access-control
- sqli
- command-injection
language: en
raw_sha256: c632afdf9e2f9eb8b19718339f6edbfed621efa49ec03291d82b27343acdeefc
text_sha256: 25cc5cf6779977f8f38eac43fe01966fe7413bc336ba3d7a58293ab2cdba545c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Slack for Offensive Operations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-04_abusing-slack-for-offensive-operations.md
- Source Type: markdown
- Detected Topics: mfa, supply-chain, sso, access-control, sqli, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c632afdf9e2f9eb8b19718339f6edbfed621efa49ec03291d82b27343acdeefc`
- Text SHA256: `25cc5cf6779977f8f38eac43fe01966fe7413bc336ba3d7a58293ab2cdba545c`


## Content

---
title: "Abusing Slack for Offensive Operations"
page_title: "Abusing Slack for Offensive Operations - SpecterOps"
url: "https://posts.specterops.io/abusing-slack-for-offensive-operations-2343237b9282"
final_url: "https://specterops.io/blog/2020/03/04/abusing-slack-for-offensive-operations/"
authors: ["Cody Thomas (@its_a_feature_)"]
programs: ["Slack"]
bugs: ["Logic flaw"]
publication_date: "2020-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4734
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Abusing Slack for Offensive Operations

Author

[Cody Thomas](https://specterops.io/blog/author/codythomas/)

Read Time

9 mins

Published

Mar 4, 2020

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2020%2F03%2F04%2Fabusing-slack-for-offensive-operations%2F&title=Abusing+Slack+for+Offensive+Operations&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2020%2F03%2F04%2Fabusing-slack-for-offensive-operations%2F&text=Abusing+Slack+for+Offensive+Operations) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Abusing Slack for Offensive Operations&Body=https://specterops.io/blog/2020/03/04/abusing-slack-for-offensive-operations/) [ ](https://specterops.io/blog/category/research/feed/)

![](https://specterops.io/wp-content/uploads/sites/3/2025/04/eb9d00_1_zyuvUcE6_Y9KmIAuKtOd-Q.jpg)

### Background

With more than 10 million daily active users, Slack is one of the most widely adopted chat platforms in the industry. Throughout our operations, we’ve seen a large variety of organizations use it for several business critical functions such as:

  * Build alerting for CI/CD Pipelines
  * Changes to production code bases via Github
  * Password Reset requests to IT
  * Hunt/IR channels collaborating on active investigations
  * All-hands announcements
  * Project-specific collaboration
  * Helpdesk Troubleshooting

Slack also provides some security enhancements over the older-school style chat programs like IRC by providing integration into Active Directory Federated Services (ADFS), Multi-Factor Authentication (MFA), and logging. Despite Slack not having an on-premise solution, it’s widely accepted for many business use-cases. All of this together makes it a very enticing target for attackers as a real-time awareness mechanism over more traditional methods such as email collection.

When the Slack client is installed on a computer (macOS or Windows), it’s installed as a user level application. Slack stores all of its information inside its own application directories located at the following locations:

  * On Windows hosts, this data is stored in the user’s AppData folder:  _%AppData%\Roaming\Slack_
  * On macOS hosts, this data is stored in the user’s Application Support folder:  _~/Library/Application Support/Slack/_
  * ** Update** On some macOS hosts, this data is instead stored in: ~/Library/Containers/com.tinyspeck.slackmacgap/Data/Library/Application Support/Slack

All of the data is readable by the user that installed the Slack client and by the SYSTEM or root context. To prevent requiring the user to repeatedly sign into each Slack workspace, Slack leverages Cookies in a sqlite database. Because a single user can be signed into multiple Slack workspaces in a single Slack client, all of this information is stored in the same area.

### Offensive Guidance

[n0pe_sled](https://medium.com/u/28c3b11e433b?source=post_page---user_mention--2343237b9282---------------------------------------), [Lee Christensen](https://medium.com/u/91b45ba406ef?source=post_page---user_mention--2343237b9282---------------------------------------), and I have leveraged Slack on a bunch of engagements now, so we wanted to share how this works. From an offensive perspective, we want to do a few things in ascending order of desirability:

  * List out all of the Slack workspaces a user has registered in their Slack client (i.e. see which Slacks a user has viewable on the left-hand side of their application)
  * List out all of the files a user has downloaded through Slack
  * Log in as the user (if they know the user’s password for that specific workspace)
  * Log into a workspace as the user if they don’t know the password
  * Log into a workspace as the user if they don’t know the password and the user has MFA enabled

All of the following assumes you have access to a user’s computer in at least a medium integrity context or you have remote access to the file system so you can access the Slack folder. From here, a few specific files will help achieve most of these objectives.

### To list out the workspaces a user has registered in their Slack client:

_Slack/storage/slack-workspaces_ or  _Slack/storage/slack-teams_

  * This file contains a JSON dictionary of information about each team such as Team ID, username, user_id, team_name, team_url, and theme information

### To list out all the files a user has downloaded through Slack:

_Slack/storage/slack-downloads_

  * This file contains a JSON dictionary of information about each download such as team_id, file_id, url of file downloaded (with original file name), downloadState, local download path, and when the download started/finished.

### To log in as the user if you know the user’s password (and no MFA):

  * You can use the information from  _Slack/storage/slack-teams_ to get the team url and username for the specific Slack workspace, then use your password to log in via the web interface or from a new Slack client

This does cause a new login event though which can potentially trigger email notifications and logging warnings.

### To log in without knowing the password

All of the others are achieved at once through a combination of a few files and the lightest amount of work. Download the following two files (about 40KB in size):

  * _Slack/storage/slack-workspaces_
  * _Slack/Cookies_

Cookies is a sqlite database the Slack client uses to authenticate back to the Slack domain. These cookies don’t typically expire.

When programs need to store sensitive data on the file system, they can use built-in mechanisms to protect these files. In Windows, this is typically done with [DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107). The nice thing about DPAPI on Windows is that even if you can remotely access the files (such as mounting a share with another user’s credentials), you still typically need to be in the user’s context to decrypt the contents of the files. In macOS, this is typically done by storing credentials in the Keychain. The nice thing about storing credential material (like application specific keys) in the Keychain is that the attacker needs to know the user’s plaintext password or get the user to type in their password to successfully pull the key.

Chrome is a good example of this style of protection since it follows both of these processes. At least in macOS, this means that an attacker doesn’t  _just_ need access as the user account, but also needs to know the user’s plaintext password to decrypt the login Keychain to access the appropriate key. However, Slack stores all of this information in unencrypted files on disk, so all an attacker needs is read access to the two files mentioned above. This means that these files can be retrieved remotely as well and still leveraged for this technique.

Once you have both files, simply follow the next steps to impersonate their session:

  1. Install a new instance of slack (but don’t sign in to anything)
  2. Close Slack and replace the automatically created  _Slack/storage/slack-workspaces_ and  _Slack/Cookies_ files with the two you downloaded from the victim
  3. **UPDATE on 11/3/2020 thanks to [Justin Bui](https://twitter.com/slyd0g)** Check your new instance of Slack for a  _Slack/storage/root-state.json_ file. If it exists, delete that file.
  4. Start Slack

You will now be automatically logged into all of the Slack teams that have valid Cookies (even if they have MFA set up on the accounts). You won’t kick the user out of their current Slack instance, and you won’t trigger a new “logon” email or notification because the Cookies your malicious Slack instance uses are already validated. Below is an example walking through step-by-step to steal “Secret Alice”’s slack information, read her messages, and even post as her into the general channel.

Walkthrough of Slack impersonation

It’s important to remember that you are acting as this user in their Slack, so in order to remain stealthy you should try to avoid clicking their unread messages. Similarly, if you’re searching within their Slack for keywords related to your operations, they can see those searches as well, so be sure to clear them out as soon as you’re done with your search.

### Disclosure

We reached out to Slack about this issue and requested that they at least leverage the built in OS level functionality to encrypt or protect the information in any way, but we got the following response:

> After some discussion with our internal teams, we have ultimately chosen not to make a change here at this time. While we agree that encrypting these stored files is a good suggestion, an attacker would still likely need direct access to their victim’s computer in order to exploit them. Additionally, even  _without_ access to these files, there are quite a lot of attacks available to an attacker, should they manage to access an installed Slack instance on a victim’s computer. We appreciate the suggestion, and may look into implementing this in the future, but for the reasons mentioned, we will be closing this report as “Informative”, for now.

Hopefully this will be addressed in the future, but at the moment, even with the latest install of Slack, this is possible. While not groundbreaking, it’s important to know that this can bypass MFA and as far as we can tell, these Cookies never expire or rotate.

### Defensive Considerations

There are a few different potential solutions for defenders when trying to prevent or detect this offensive usage.

### Slack Logging

Slack does provide some insight into logins if you have Standard, Plus, or Enterprise Grid plans for the Owner or Admins to check on their members. If an individual user is worried, they can check their own access logs for  _any_ tier level (even free) and download them.

![](https://specterops.io/wp-content/uploads/sites/3/2025/04/40f4e2_1_nsWuYZxDklPAB7VC72WRwA.jpg)

Slack personal access logs

### [View Access Logs for your workspace](https://slack.com/help/articles/360002084807-View-Access-Logs-for-your-workspace?source=post_page-----2343237b9282---------------------------------------#view-access-logs-for-all-members)

### Access Logs are an easy way to check for any unusual or suspicious sign-in activity. On the Standard, Plus, and…

slack.com

### [View Access Logs for your account](https://slack.com/help/articles/360002084827-View-Access-Logs-for-your-account?source=post_page-----2343237b9282---------------------------------------)

### Worried someone else may have accessed your account? Or maybe you forgot to sign out of Slack while on a shared device…

slack.com

In Windows, system access control lists (SACLs) can be applied to the files mentioned in this post to generate events when processes other than Slack access the files.

### Active Directory Integration

We’ve only seen one instance where this technique was completely stopped — [ADFS integration](https://slack.com/help/articles/230902028-ADFS-single-sign-on) with Single-Sign-On (SSO). We were unable to fully track down if it was strictly ADFS with SSO or if there was another mechanism used in conjunction. However, when we encountered this situation, the Slack workspace in question required us to re-authenticate before logging in.

### Reporting Timeline

As committed as SpecterOps is to [transparency](https://posts.specterops.io/a-push-toward-transparency-c385a0dd1e34), we acknowledge the speed at which attackers adopt new offensive techniques once they are made public. This is why prior to publication of a new bug or offensive technique, we regularly inform the respective vendor of the issue, supply ample time to mitigate the issue, and notify select, trusted vendors in order to ensure that detections can be delivered to their customers as quickly as possible.

  * July 9th, 2019: Vulnerability reported to Slack via HackerOne
  * July 10th, 2019: Slack requested more information about the context around the vulnerability
  * July 12th, 2019: Slack looking into report
  * July 22nd, 2019: Slack closed the issue as “Informative”

Post Views: 3,060

[ Cody Thomas ](https://specterops.io/blog/author/codythomas/)

Senior Software Engineer 

Cody Thomas is a Senior Software Engineer at SpecterOps specializing in offensive software development where he is the original author and maintainer of the Mythic Command and Control framework. He was the course architect for Adversary Tactics: Mac Tradecraft and performed offensive macOS research.

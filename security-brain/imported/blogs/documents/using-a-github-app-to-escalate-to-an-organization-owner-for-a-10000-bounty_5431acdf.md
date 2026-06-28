---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-20_using-a-github-app-to-escalate-to-an-organization-owner-for-a-10000-bounty.md
original_filename: 2018-06-20_using-a-github-app-to-escalate-to-an-organization-owner-for-a-10000-bounty.md
title: Using a GitHub app to escalate to an organization owner for a $10,000 bounty
category: documents
detected_topics:
- access-control
- oauth
- idor
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- oauth
- idor
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 5431acdfa275c888a40a3cbf46fe62603014475b225a093abe4a75e67ebdd1d0
text_sha256: 6f23ec86f42386d576d48972486752b5770a61b6069f31b2f76181dccb0e95b3
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Using a GitHub app to escalate to an organization owner for a $10,000 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-20_using-a-github-app-to-escalate-to-an-organization-owner-for-a-10000-bounty.md
- Source Type: markdown
- Detected Topics: access-control, oauth, idor, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5431acdfa275c888a40a3cbf46fe62603014475b225a093abe4a75e67ebdd1d0`
- Text SHA256: `6f23ec86f42386d576d48972486752b5770a61b6069f31b2f76181dccb0e95b3`


## Content

---
title: "Using a GitHub app to escalate to an organization owner for a $10,000 bounty"
url: "https://medium.com/@cachemoney/using-a-github-app-to-escalate-to-an-organization-owner-for-a-10-000-bounty-4ec307168631"
authors: ["Tanner Emek (@itscachemoney)"]
programs: ["GitHub"]
bugs: ["Broken authorization", "IDOR"]
bounty: "10,000"
publication_date: "2018-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5832
scraped_via: "browseros"
---

# Using a GitHub app to escalate to an organization owner for a $10,000 bounty

Using a GitHub app to escalate to an organization owner for a $10,000 bounty
Tanner
Follow
5 min read
·
Jun 21, 2018

732

2

I had never participated in GitHub’s long running bounty program in the past, but the HackTheWorld promo of free private repositories for life piqued my interest. I’m going to walk through a simple yet high-impact privilege escalation I landed on while poking around. In this case, I was able to leverage a GitHub app to escalate from an organization member to an account owner.

Background

First, let’s go over the simple user roles of a GitHub organization. I added this section to demonstrate the capabilities of an owner account, and how there are measures put in place to minimize granting it.

Outside collaborator (for completeness) — A role where you’re technically not part of the organization, but just given access to specific repositories inside.
Member — The lowest role you can have inside of an organization. Depending on the organization settings, you may be limited to viewing or having “write” access on a subset of repositories. The highest level of access you can be given with this permission is a repository admin, which will allow changing most configuration settings for that specific repository.
Owner — The highest role you can have inside of an organization, which is basically the equivalent of a super admin. This role allows you to view and edit all organization data and repositories; but more critically, irreversibly delete the entire organization and its code.

Organizations are widely used throughout GitHub, and the common assumption is that their members don’t pose a threat when the proper access controls are in place (ex. not giving admin access to every repository). A common model is to put members into “teams”, and use those to facilitate access control across repositories. Using this model, organization owners can be limited to a very small subset of users, since team-based controls are sufficient to give extended access where needed.

Digging into GitHub apps

While going through the organization settings as an owner, I noticed a “Third-party access policy” switch. The purpose of this setting is to prevent members of your organization from giving repository access to untrusted 3rd parties via OAuth. Once enabled, a member must specifically request access from the OAuth permissions prompt, which then requires approval by an organization owner before it can access any organization data.

Playing around with those settings didn’t lead anywhere, and I couldn’t find a way to bypass the approval requirement.

The next thing I looked into was another kind of app, an integration. Integrations are similar to OAuth apps, except they act on behalf of the organization instead of the user. My thought process was to check if the “Third-party access policy” would apply to integrations as well, or if those would slip through. I navigated to the marketplace and went through the installation flow with a few apps. It was clear that as an organization member, you’re not given the option to install the integration. You can only install integrations into your own account, or for organizations of which you’re an owner. I later found the following note in the documentation.

Organization members can’t request a GitHub App installation.

The integration can only be installed into my account, or to an organization for which I have “owner” permissions.

While going through the installation flow, I noticed that after choosing a “Billing account” you’re brought to a screen that has a URL such as: https://github.com/apps/:app_name/installations/new/permissions?target_id=:id

Get Tanner’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The target_id is the organization_id, or the account_id where the app is to be installed. Naturally, as a member of another organization, I crossed my fingers and changed the target_id to that organization_id. Since my member account was a repository admin, I was prompted with the installation page. I was successfully able to install the app, but only to the one repository for which I had admin rights to. I double checked the installation by visiting the “Installed GitHub Apps” page from the organization owner account. Success!

Press enter or click to view image in full size
Integration successfully installed into the account that which I am a member.

At this point it was past 3am, and I knew I had found a valid issue since I circumvented the “Third-party access” restriction that was set. I went ahead and reported it to the GitHub program, with the intention of leaving comments in the report for any later findings.

Taking the elevator to the penthouse

The next day I wanted to see if I could take this any further. I created my own GitHub integration, and noticed the permissions that could be requested were extremely sensitive. Particularly the permission to have “write” access to all organization members and teams. Surely having the permission to install an integration into one repository won’t allow me to grant “write” access to all of the organization’s members, right? Incorrect. Since the intended design is such that only owners can install integrations, having the permission is binary. The scopes you can grant aren’t enforced, since you’re already considered to have the highest level of access.

Installing the app while requesting a boatload of permissions.

The next step was to see if the API worked as expected, and if I was actually able to use it without running into a permissions error down the line. I successfully messed around with a bunch of endpoints before landing on the holy grail. Add or update an organization membership with a role parameter. Using that endpoint, I was successfully able to invite another user into the organization as an account owner.

Press enter or click to view image in full size
Audit log entries for the underprivileged “OrgMember” account installing the integration — then using the API to invite “NewMember” as an owner.
Prevalence

I figured the good in this was that it was only able to be exploited by a repository admin. How many of those could you possibly have in your organization? After more investigation, I found that all organizations that allow members to create repositories are vulnerable. That’s because a member is automatically given admin rights to any repository they create; allowing them to exploit this by just creating a dummy repository to install the app into. This feature is enabled by default, and it’s common for organizations to leave it enabled since GitHub’s payment model is no longer repository bound, but based on the number of users.

Exploitation of this bug isn’t necessarily going to be through malicious insiders, but through attackers compromising member accounts. Let’s say an organization has 300 members in it; the surface area for an attacker to go after is no longer limited to the 3 or 4 organization owners, but any of its members.

As always, it’s been a pleasure working with the GitHub security team!

Timeline
Initial report: 11/11/17 @ 3:30 AM
Reporting the ability to escalate to organization owner: 11/11/17 @ 8:30 PM
GitHub team officially looking into the issue: 11/13/17 @ 5:30 AM
Bounty of $10,000 awarded and triaged: 11/14/17 @ 1:40 PM
Fix deployed to production: 11/15/17
Issue marked as resolved: 12/1/17

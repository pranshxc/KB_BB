---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_attacking-the-software-supply-chain-with-a-simple-rename.md
original_filename: 2022-10-26_attacking-the-software-supply-chain-with-a-simple-rename.md
title: Attacking The Software Supply Chain With A Simple Rename
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 44c7ff25dc6edaa90451bdc5e1aea67b7a50abaa4bd209e48b17f960dc8add0c
text_sha256: b00f5c22f438fa351986947c2234d6162cd8ca156392a6f59c6d9af83989fe02
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking The Software Supply Chain With A Simple Rename

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_attacking-the-software-supply-chain-with-a-simple-rename.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `44c7ff25dc6edaa90451bdc5e1aea67b7a50abaa4bd209e48b17f960dc8add0c`
- Text SHA256: `b00f5c22f438fa351986947c2234d6162cd8ca156392a6f59c6d9af83989fe02`


## Content

---
title: "Attacking The Software Supply Chain With A Simple Rename"
page_title: "Attacking the Software Supply Chain with a Simple Rename - Checkmarx.com"
url: "https://checkmarx.com/blog/attacking-the-software-supply-chain-with-a-simple-rename/"
final_url: "https://checkmarx.com/blog/attacking-the-software-supply-chain-with-a-simple-rename/"
authors: ["Aviad Gershon (@aviadgershon)", "Elad Rapoport (@eladrapoport)"]
programs: ["GitHub"]
bugs: ["Repojacking", "Supply chain attack"]
publication_date: "2022-10-26"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1987
---

If not explicitly tended, all renamed usernames on GitHub were vulnerable to this flaw, including over 10,000 packages on the Go, Swift, and Packagist package managers. This means that thousands of packages could have been hijacked immediately and start serving malicious code to millions of users.

**The vulnerability was fixed by GitHub following our report and is no longer exploitable.**

This isn’t the first vulnerability found in this mechanism; earlier this year, an attacker used a similar vulnerability to [hijack and poison popular PHP packages](https://medium.com/checkmarx-security/attacker-caught-hijacking-packages-using-multiple-techniques-to-steal-aws-credentials-d14e5b5c420e) with millions of downloads.

The mechanism that was found vulnerable, the “Popular repository namespace retirement”, remains an attractive attack point for supply chain attackers in the future. Therefore, we provide an [open-source tool](https://github.com/checkmarx/chainjacking) to identify and help mitigate this risk.

## GitHub Repository URL is Coupled to its Username

GitHub Repositories have a unique URL, it is nested under the user account which created the repository. Whenever someone would like to download (clone) the open-source repository, they use the full repository URL.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

## When GitHub Users Rename Their Username

We showed that GitHub repositories are coupled to usernames. What happens when users decide to rename their account? In that case, GitHub supports the rename and displays the following warning noting that all traffic for the old repository’s URL will be redirected to the new one.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

After accepting the warning and renaming the username, GitHub automatically sets up redirect rules from the old repository’s URLs to the new URLs. This is done to keep things operating for users unaware of this username change.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

## What is RepoJacking?

RepoJacking is a technique to hijack renamed repository URLs traffic and routing it to the attacker’s repository by exploiting a logical flaw that breaks the original redirect.

A GitHub repository is vulnerable to RepoJacking when its creator decided to rename his username while the old username is available for registration. We have shown the coupling in the repository URLs between the repository name and the creator username, and this means attackers can create a new GitHub account having the same combination to match the old repository URL used by existing users.

Whenever attackers do this, the default redirect is disabled, and all existing traffic is immediately routed to the attackers malicious GitHub repository.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

## GitHub Protection Against RepoJacking

To avoid this potentially harmful behavior, GitHub put in place the “[popular repository namespace retirement](https://github.blog/2018-04-18-new-tools-for-open-source-maintainers/#popular-repository-namespace-retirement)” protection measure: any repository with more than 100 clones at the time its user account is renamed is considered “retired” and cannot be used by others. 

To clarify: what is considered “retired’ is the namespace, meaning the combination of the username and the repository name. 

For example, let’s take the repository named “repo” of the username “account-takeover-victim.” 

This repository was recently cloned 100 times, which qualifies it for the popular repository namespace retirement. 

At this point, the account’s owner decides to rename the username to whichever name they choose. 

**The practical result of this is that the username “account-takeover-victim” can now be claimed by anyone.**

However, once the new owner of this username tries to open a new repository under the name “repo,” they will be blocked and get the following message: 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

## Bypassing GitHub Protection

In a previous blog, we described one technique for bypassing this protection. This was most likely the way it was done in the [CTX incident](https://checkmarx.com/blog/attacker-caught-hijacking-packages-using-multiple-techniques-to-steal-aws-credentials/). Shortly after that incident and the publicity it gained, GitHub patched this vulnerability.

Our group’s Chief Architect, Elad Rapoport, felt that there was more to this story, took another go, and found a new way to bypass the same protection. The new exploit was reported to the GitHub bug bounty program, which recently confirmed and patched the new vulnerability.

The current bypass abuses the “[Repository Transfer](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)” feature to achieve its goal in the following manner:

  1. **“victim/repo”** is a popular GitHub repository retired under the “[popular repository namespace retirement](https://github.blog/2018-04-18-new-tools-for-open-source-maintainers/#popular-repository-namespace-retirement)” protection.
  2. **“helper_account”** creates the **“repo”** repository
  3. **“helper_account”** transfer ownership of the **“repo”** repository to **“attacker_account.”**
  4. **“attacker_account”** rename its username to **“victim.”**
  5. The new **“victim”** account (previously **“attacker_account”**) accepts the ownership transfer

The namespace **“victim/repo”** is now in the attacker’s control

## Impact

As shown with the previous bypass of this protection measure, successful exploitation enables the takeover of popular code packages in several package managers, including “Packagist,” “Go,” “Swift,” and more. We have identified over 10,000 packages in those package managers using renamed usernames and are at risk of being vulnerable to this technique in case a new bypass is found.

In addition, exploiting this bypass can also result in a takeover of popular GitHub actions, which are also consumed by specifying a GitHub namespace. Poisoning a popular GitHub action could lead to major Supply Chain attacks with significant repercussions.

As mentioned, by now this vulnerability is fixed and no longer exploitable, which isn’t to say that another way to bypass this same protection won’t be found.

## Timeline

1 Nov 21 – We found a way to bypass the GitHub [namespace retirement](https://github.blog/2018-04-18-new-tools-for-open-source-maintainers/#popular-repository-namespace-retirement) feature

8 Nov 21 – We disclose the bypass findings to GitHub

8 Nov 21 – GitHub acknowledged the bypass and replied that they are working on a fix

24 Mar 22 – GitHub respond that they have fixed the bypass

11 May 22 – We discover that the bypass is still exploitable and reported to GitHub

23 May 22 – This attack was [found active against open-source attack](https://checkmarx.com/blog/attacker-caught-hijacking-packages-using-multiple-techniques-to-steal-aws-credentials/)

25 May 22 – This technique was published by a security researcher taking ownership of the attacks and was fixed shortly after by GitHub

13 June 22 – we found additional vulnerability to bypass GitHub [namespace retirement](https://github.blog/2018-04-18-new-tools-for-open-source-maintainers/#popular-repository-namespace-retirement) feature and reported to GitHub

19 Sep 22 – GitHub fixed the vulnerability, classifies it as “High” severity, and grants us a bug bounty

26 Oct 22 – Full disclosure

## Conclusion

Many GitHub users choose to use the “User rename” feature GitHub offers, among them, users that control popular repositories and packages. For that reason, the attempt to bypass the “Popular repository namespace retirement” remains an attractive attack point for supply chain attackers with the potential to cause substantial damages.

Moreover, it is interesting to notice that GitHub’s provided protection is activated based on internal metrics and gives the users no indication if a particular namespace is protected by it or not. This might leave some repositories and packages unknowingly at risk.

We recommend that customers avoid using retired namespaces to minimize the attack surface as other vulnerabilities in this mechanism may still exist.

We have released an [open-source tool](https://github.com/checkmarx/chainjacking) to identify those packages and suggest a safer way to consume them (using the new Package URL).

We want to thank GitHub for working with us and applying a fix to this vulnerability.

_**Working together to keep the open-source ecosystem safe.**_

Tags:

Application Security Testing

AppSec

Article

Developer

English

Open-Source Security

SSCS

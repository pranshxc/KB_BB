---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-10_messing-with-githubs-fork-collaboration-for-fun-and-profit.md
original_filename: 2021-03-10_messing-with-githubs-fork-collaboration-for-fun-and-profit.md
title: Messing with GitHub's fork collaboration for fun and profit
category: documents
detected_topics:
- access-control
- api-security
- command-injection
- automation-abuse
- graphql
tags:
- imported
- documents
- access-control
- api-security
- command-injection
- automation-abuse
- graphql
language: en
raw_sha256: f50f41778d79aef496bc87dceafd8ba09cb550b05180890ada519808c4c20464
text_sha256: 1cb055b6ec646e2f6a5d84df5f692266a9fc9c8e79738b7b47ecef53e155b2a4
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Messing with GitHub's fork collaboration for fun and profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-10_messing-with-githubs-fork-collaboration-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: access-control, api-security, command-injection, automation-abuse, graphql
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `f50f41778d79aef496bc87dceafd8ba09cb550b05180890ada519808c4c20464`
- Text SHA256: `1cb055b6ec646e2f6a5d84df5f692266a9fc9c8e79738b7b47ecef53e155b2a4`


## Content

---
title: "Messing with GitHub's fork collaboration for fun and profit"
page_title: "Messing with GitHub’s fork collaboration for fun and profit | Teddy Katz’s Blog"
url: "https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html"
final_url: "https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html"
authors: ["Teddy Katz (@not_aardvark)"]
programs: ["GitHub"]
bugs: ["Broken Access Control"]
bounty: "30,000"
publication_date: "2021-03-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3824
---

# Messing with GitHub's fork collaboration for fun and profit

Mar 10, 2021 

GitHub has a useful feature called [fork collaboration](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork). It works as follows:

  1. Suppose I want to make changes to an open-source project. First, I create a [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo), and commit the changes there.
  2. I create a pull request from a branch of my fork (the “head branch”) to the original project (the “base repository”).
  3. Sometimes, it’s useful for the maintainer of the project to edit my pull request directly. To allow this, I can turn on the “Allow edits from maintainers” checkbox, which **grants write access to the head branch** to the **maintainers of the base repository**.

![A screenshot of GitHub's form to create a new pull request. The proposed title for the pull request is "Update README.md". The proposed description is "foo bar baz". There is a checkbox at the bottom of the pull request labeled "Allow edits and access to secrets by maintainers", which is currently checked. The screenshot is annotated with a red arrow pointing to the checkbox.](/assets/img/fork-collaboration-checkbox.png)

I was curious about how this access grant worked, so tested a few things out, and found a few major security bugs along the way.

## Pull requests from other peoples’ branches

Interestingly, you don’t have to own a repository to create a pull request from it. As long as two repositories are in the same fork network, anyone can create a pull request from any branch in the network to any other branch. This makes a fork collaboration feature tricky to implement.

For example, what would be the expected behavior if I created a pull request _from_ a branch in someone else’s repository, _to_ my own repository, with fork collaboration enabled?

As a reminder, fork collaboration generally allows the maintainer of the _base_ repository to write to the _head_ branch. In this case, I’m the maintainer of the base repository, and the head branch belongs to someone else. So following the same logic, enabling fork collaboration would give me write access to someone else’s branch.

But that’s silly – I shouldn’t just be able to grant myself write access to someone else’s repository by creating a pull request. So I tried it out, and unsurprisingly, GitHub appears to protect against this. (I’m [not the first person](https://bounty.github.com/researchers/tunz.html#:~:text=Unauthorized%20branch%20access%20using%20fork%20collaboration) to think of this attack.) The fork collaboration checkbox didn’t even appear in the UI in this scenario, and I got an error when trying to create this pull request with the API (`"Fork collab can't be granted by someone without permission"`).

“Someone without permission” apparently means “someone without write access to the head branch”, which makes sense – I shouldn’t be able to grant anyone write access to the head branch unless I have write access to it in the first place.

### Turning on fork collaboration after-the-fact

However, after testing further I noticed that GitHub was only doing this validation when a user _created_ a pull request. When a user _edited_ an existing pull request with the [REST API](https://docs.github.com/en/rest/reference/pulls#update-a-pull-request), GitHub seemed to apply a looser set of validations. I tried out a modified version of the previous attack:

  1. Create a pull request from a branch of someone else’s repository to my repository, with fork collaboration _disabled_.
  2. Edit the pull request to enable fork collaboration, using the REST API.
  3. Obtain write access to someone else’s branch.

At first, steps 1 and 2 worked great, but step 3 didn’t work – I didn’t have write access to the victim’s branch, and I wasn’t sure why. I’d made some progress by enabling the fork collaboration checkbox, but I still wasn’t able to get write access to someone else’s repository.

### Doing the same thing over and over and expecting different results

A few days later, I came back to the issue and tried a third time. It turned out that I had just been choosing targets poorly – this modified attack did grant write access, but only if the victim repository was itself a _fork_ of another repository. In other words, an attacker could get write access to any public repository that displayed “forked from …” in the UI.1

So this was a fairly major issue. Although most projects don’t develop their code directly on forks, they frequently merge pull requests with code from forks. This issue would have allowed an attacker to arbitrarily tamper with random users’ forks of random repositories.

That said, the issue wasn’t quite as exploitable as I’d originally thought, given that it only granted access to fork repositories. In the next blogpost, I’ll discuss a different bug I found that would allow write access to arbitrary public repositories, including both forks and non-forks.

## Enabling fork collaboration on other peoples’ pull requests

Looking at fork collaboration again a few days later, I noticed another, smaller issue. When someone creates a pull request, the maintainers of the base repository can always edit certain metadata about the pull request (e.g. labels and open/closed state), regardless of whether they have write access to the head branch. But the state of the fork collaboration checkbox is itself a piece of metadata about the pull request. Could the maintainers of the base repository edit that too?

When I tried it out with the REST API, GitHub returned an error (`"Only the pull request author may change the maintainer_can_modify value"`). This makes sense – if the pull request author is the one with write access to the head branch, then they should be the one to decide whether to grant access to others.

But I found that when editing a pull request with the GraphQL API, GitHub applied yet another set of access controls – and this set didn’t include checking the author of the pull request. As a result, even if the author declined to grant access to their branch, a maintainer on the base repository could enable fork collaboration and get write access to the branch anyway, by editing the pull request to enable fork collaboration using the GraphQL API.

## Lots of code leads to lots of bugs

One surprising aspect of these bugs was the divergence in how access control worked across different APIs. It seems like there must be at least six endpoints separately implementing the same access controls for the fork collaboration checkbox:

  1. Creating a pull request with the web UI
  2. Editing a pull request with the web UI
  3. Creating a pull request with the REST API
  4. Editing a pull request with the REST API
  5. Creating a pull request with the GraphQL API
  6. Editing a pull request with the GraphQL API

As code changes over time in response to product requirements and security fixes, it’s not really surprising that endpoints would get out of sync with each other if six different implementations are being maintained at a time. Unfortunately, this seems like it would be a recipe for bugs and incomplete security fixes.

From what I’ve seen, GitHub does a great job of centralizing the more “fundamental” access control checks (such as restricting access to private repositories) without reimplementing the checks in every single endpoint. However, it seems like there’s still some room for improvement in the validity checks for features with more nuanced access controls, such as fork collaboration.

## Timeline

As always, the GitHub security team was a pleasure to work with.

  * **2016-09-07** Choongwoo Han discovered an [extremely similar issue](https://bounty.github.com/researchers/tunz.html#:~:text=Unauthorized%20branch%20access%20using%20fork%20collaboration) to the first one described in this blogpost, and reported it to GitHub. The issue was ostensibly fixed soon afterwards. I’m unsure whether the fix was incomplete at the time, or whether it regressed later.
  * **2021-01-22 05:29:45 UTC** I reported the first issue from this post (getting write access to arbitrary forks by creating pull requests from their branches) to GitHub’s bug bounty program via HackerOne.
  * **2021-01-22 18:28:42 UTC** Issue confirmed by GitHub security team
  * **2021-01-24 00:17:59 UTC** I reported the second issue from this post (enabling fork collaboration on other peoples’ pull requests) to GitHub via HackerOne.
  * **2021-01-25 17:36:56 UTC** Initial response from GitHub security team on the second issue, mentioning that the issue was being looked into
  * **2021-01-25 19:57:23 UTC** GitHub determined that the fix/root cause was the same for both issues. They expressed appreciation for filing the second issue as an additional testcase, but they decided to treat it as a duplicate for the purposes of a bug bounty.
  * **2021-01-27 19:51:30 UTC** Patch deployed on github.com, GitHub replied on HackerOne to double-check that the issue was resolved
  * **2021-01-28 01:18:32 UTC** I replied on HackerOne noting that the first issue was resolved, but the second issue still appeared to be exploitable.

At this point, GitHub’s claim that the fix was the same for both issues seemed kind of dubious, given that the first issue was fixed and the second wasn’t. To their credit, GitHub acknowledged the error and reversed that determination. (It seems like the root cause for the second issue was slightly different from what they originally suspected.).

  * **2021-01-28 17:22:02 UTC** GitHub reopened the second issue on HackerOne
  * **2021-01-28 22:44:10 UTC** Fix for the second issue deployed on github.com. GitHub replied on HackerOne to double-check that the second issue was resolved. As far as I can tell, the fix was complete this time.
  * **2021-03-02, around 20:45 UTC** GitHub Enterprise Server 3.0.1, 2.22.7, 2.21.15, and 2.20.24 were [released](https://docs.github.com/en/enterprise-server@3.0/admin/release-notes#3.0.1) with fixes for both issues, as [CVE-2021-22861](https://nvd.nist.gov/vuln/detail/CVE-2021-22861) and [CVE-2021-22863](https://nvd.nist.gov/vuln/detail/CVE-2021-22863) respectively.
  * **2021-03-02 22:29:32 UTC** GitHub awarded a $20000 bounty for the first issue
  * **2021-03-02 22:26:36 UTC** GitHub awarded a $10000 bounty for the second issue

* * *

  1. Apparently, this [would have granted write access to _any_ public repository until December 2020](https://github.blog/changelog/2021-03-02-rest-api-maintainer-fork-collaboration-access-changes/), but then something changed and narrowed the vulnerability to only include fork repositories. Based on [GitHub’s CVE description](https://nvd.nist.gov/vuln/detail/CVE-2021-22861) as well as the bounty amount, I suspect that GitHub Enterprise Server still had the older, more severe version of the vulnerability. I’m unsure about the specifics of what caused the behavior change in December, although I suspect it might have been a [bug](https://github.community/t/bug-pr-edit-permissions-not-working-on-fork-of-fork/152123). ↩

[](/2021/03/10/fork-collab-abuse.html)

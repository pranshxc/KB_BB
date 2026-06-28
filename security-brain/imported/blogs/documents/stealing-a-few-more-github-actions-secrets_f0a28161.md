---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-23_stealing-a-few-more-github-actions-secrets.md
original_filename: 2022-02-23_stealing-a-few-more-github-actions-secrets.md
title: Stealing a few more GitHub Actions secrets
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: f0a28161237ec75073c2d9a6f924cd36cdc8bd7f16f07bfad181c1e2ef558123
text_sha256: c0fc724cf81cd50ca6e8e79cfee782340711e20b5d4a703395d5633ff0a15ed5
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: true
---

# Stealing a few more GitHub Actions secrets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-23_stealing-a-few-more-github-actions-secrets.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: True
- Raw SHA256: `f0a28161237ec75073c2d9a6f924cd36cdc8bd7f16f07bfad181c1e2ef558123`
- Text SHA256: `c0fc724cf81cd50ca6e8e79cfee782340711e20b5d4a703395d5633ff0a15ed5`


## Content

---
title: "Stealing a few more GitHub Actions secrets"
page_title: "Stealing a few more GitHub Actions secrets | Teddy Katz’s Blog"
url: "https://blog.teddykatz.com/2022/02/23/ghosts-of-branches-past.html"
final_url: "https://blog.teddykatz.com/2022/02/23/ghosts-of-branches-past.html"
authors: ["Teddy Katz (@not_aardvark)"]
programs: ["GitHub"]
bugs: ["Logic flaw"]
bounty: "7,500"
publication_date: "2022-02-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2874
---

# Stealing a few more GitHub Actions secrets

Feb 23, 2022 

In a [previous blogpost](/2021/03/17/github-actions-write-access.html), I wrote about a security bug I found in GitHub, which would have allowed an attacker to get write access to almost any public repository. As a quick recap:

  * Each pull request on GitHub has a “base branch”, which is a git branch in the same repository as the pull request.
  * GitHub Actions sometimes executes code from the base branch of a pull request, giving the code access to the repository’s secrets. (Specifically, this happens if the base branch has a [`pull_request_target` workflow](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target).) This is generally safe, because anyone who might push to the base branch could already write to the repository directly.
  * Due to an oversight at the time, a user could set the “base branch” of their pull request to a _commit hash_ , rather than a real branch.
  * As a result, an attacker could create a pull request from a fork, and then change the “base branch” to a commit hash for a malicious commit on the attacker’s fork. Since commit hashes are shared among forks, GitHub Actions would execute code from the malicious commit, granting it access to the parent repository and its secrets.

This post describes a different security bug I found in GitHub, using a similar attack strategy. This post should be coherent on its own, but if you’re confused after reading it, you might find it useful to read [the previous post](/2021/03/17/github-actions-write-access.html), which goes into much more detail about the GitHub Actions security model.

## Git, GitHub, and weird branch names

Last summer, I took a look at how git and GitHub behave with _unusual branch names_.

In certain places, the git CLI allows the use of either a branch or a commit hash. For example, to switch to a branch called `my-branch`, one can use:
  
  
  $ git checkout my-branch
  

Similarly, to switch to a specific commit, one can use a commit hash as a command-line argument:
  
  
  $ git checkout ***REDACTED-SUSPECT-TOKEN***GitHub can be used in a similar way. For example, one can view the state of a repository at a particular branch at `github.com/someone/some-repo/tree/my-branch`, or the state at a particular commit hash at `github.com/someone/some-repo/tree/a047be85247755cdbe0acce6f1dafc8beb84f2ac`.

Of course, we can choose the names of our branches. What happens if we decide to create a branch called `a047be85247755cdbe0acce6f1dafc8beb84f2ac` (the same as the commit hash)?
  
  
  $ git branch ***REDACTED-SUSPECT-TOKEN***  $ git checkout ***REDACTED-SUSPECT-TOKEN***  warning: refname 'a047be85247755cdbe0acce6f1dafc8beb84f2ac' is ambiguous.
  ...
  
  $ git branch
  * ***REDACTED-SUSPECT-TOKEN***  main
  

Git allows the branch to be created, albeit with a [warning](https://stackoverflow.com/questions/20510749/git-clone-error-warning-refname-is-ambiguous-git-normally-never-creates-a-r). Then when using `checkout` and other commands, git interprets `a047be85247755cdbe0acce6f1dafc8beb84f2ac` as a branch rather than a commit hash.

On the other hand, GitHub rejects the branch completely:1
  
  
  $ git push
  remote: error: GH002: Sorry, branch or tag names consisting of 40 hex characters are not allowed.
  remote: error: Invalid branch or tag name "a047be85247755cdbe0acce6f1dafc8beb84f2ac"
  

That’s no fun. What if we name the branch after a shorthash of the commit, instead of the full hash?
  
  
  $ git branch a047be8
  $ git checkout a047be8
  $ # ...
  $ git push
  * [new branch]  a047be8 -> a047be8
  branch 'a047be8' set up to track 'a047be8'
  

GitHub accepts the push this time! We’ve successfully created an _ambiguous branch_.

## Shadowing shorthashes with branch names

To summarize the last section:

  * We have a commit in a GitHub repository, with a shorthash of `a047be8`.
  * We also pushed a branch named `a047be8` to the same repository.

At this point, when we go to `github.com/someone/some-repo/tree/a047be8`, GitHub chooses to show the files for the `a047be8` _branch_ , rather than showing files for the `a047be8` _commit_.2 I think this is a reasonable choice. If GitHub resolved `a047be8` as a commit shorthash, then there would be no way to refer to the branch with that name. As-is, resolving `a047be8` as a branch only causes problems if someone is using a shorthash in a URL and expecting it to resolve to a commit. But that use case is inadvisable anyway because it would [also fail if a shorthash collision occurs](/2019/11/12/github-actions-dos.html).

In other words, the branch `a047be8` is effectively “shadowing” the commit with the shorthash `a047be8`, preventing the commit from being referred to using that shorthash.

However, the commit still exists. If the branch `a047be8` is ever deleted, then the name `a047be8` will suddenly start getting resolved to the commit `a047be85247755cdbe0acce6f1dafc8beb84f2ac` again – even if someone had no idea that the commit existed, and was just trying to find the now-deleted branch. This edge case seemed like a good place to look for bugs.

## Ghost branches

At this point, I tried an experiment to see how well GitHub would handle deleted branches that matched commit shorthashes.

In the previous examples, we had a commit with a particular shorthash in a repository, and then we pushed a branch with a name matching the shorthash. Of course, we could also do things in reverse – if a branch already exists, we could sometimes push a commit with a shorthash that matches the branch name. So I did the following:

  1. First, I pushed a branch called `deadbeef` to a GitHub repository.
  2. Then I created a pull request from some other branch to `deadbeef`.
  3. Next, deleted the `deadbeef` branch, which caused the pull request to be automatically closed.
  4. Finally, I used my practical-joke project, [lucky-commit](https://github.com/not-an-aardvark/lucky-commit), to generate a new commit with the shorthash `deadbeef`. I pushed that commit to the GitHub repository as well.3

I was expecting that if anything went wrong, it would probably be in displaying the pull request diff. For example, I thought maybe the UI would start displaying a diff with the new `deadbeef` commit rather than the old `deadbeef` branch. But in reality, GitHub showed a historical diff with the now-deleted `deadbeef` branch, which is the correct behavior. (In hindsight, it makes sense that pull request diffs would only update when a pull request is open.)

I was about to give up and move onto something else when I noticed something strange: I was allowed to reopen the pull request in the GitHub UI.

![A screenshot of a GitHub pull request. The title of the pull request is 'Pull request with "deadbeef" as base branch'. The pull request is closed. Underneath the title, some text about the pull request is shown: "not-an-aardvark wants to merge 1 commit into deadbeef from not-an-aardvark-patch-10". The screenshot has been annotated to underline the word "deadbeef" in this text. Further down on the page, a historical timeline for this pull request is shown. The first timeline entry says, "not-an-aardvark deleted the branch 'deadbeef' one minute ago". The screenshot has been annotated to highlight this timeline event. Below it, another timeline event about the pull request is shown: "not-an-aardvark closed this 1 minute ago". At the bottom of the screenshot, there is a button labeled "Reopen pull request". This button appears to be clickable, and the screenshot is annotated with a red arrow pointing at the button.](/assets/img/reopenable-pull-request-with-deleted-base-branch.png)

This is kind of bizarre. Normally, for any open pull request, both the head and base branches of the pull request need to exist. As we saw earlier, if either branch is deleted, the pull request is immediately closed. But in this case, GitHub lets us reopen the pull request after deleting the base branch.

Why? Well, we’ve fooled GitHub into thinking that the base branch called `deadbeef` still exists – even though it doesn’t – because when GitHub attempts to find the code at the `deadbeef` branch, it hits the commit with the shorthash `deadbeef` rather than finding nothing. As a result, GitHub allows the pull request to be reopened.

## Return of the nonsensical pull requests

At this point, we have an open pull request where the base branch points to a commit with the shorthash `deadbeef`, rather than an actual branch.

This is almost identical to the scenario described in the [previous blogpost](/2021/03/17/github-actions-write-access.html) that was mentioned earlier, where a “nonsensical” pull request like this could be used to steal GitHub Actions secrets. The exploit path in that post was fixed in February 2021 by adding validation to the “edit base branch” endpoint – effectively preventing that endpoint from being used to create nonsensical pull requests. However, at the time, GitHub didn’t add checks for branch existence to the GitHub Actions backend. In other words, at that point GitHub Actions was still vulnerable to these nonsensical pull requests, but it was no longer believed to be possible to create one.

When I tried out using GitHub Actions using this new method of creating nonsensical pull requests, I found that it was still possible to steal secrets using `pull_request_target` Actions workflows.

## Putting things together

At this point, we have a workable attack scenario:

  1. Someone with write access to a repository unwittingly creates a branch called `deadbeef` (or `AAAAAAA`, or `12345`, or any other name that matches certain constraints4) as part of their normal development workflow.
  2. An attacker creates a pull request from a fork to the `deadbeef` branch, then immediately closes the pull request (e.g. with the pretense that it was created by mistake).
  3. Later on, someone deletes the `deadbeef` branch (say, after its changes are merged into `main`).
  4. The attacker pushes a malicious GitHub Actions workflow like [this one](https://gist.github.com/not-an-aardvark/357547edf338f8fa9920bbcd286e3a7b) to their fork, in a [specially-crafted](https://github.com/not-an-aardvark/lucky-commit) commit that has the shorthash `deadbeef`.
  5. The attacker reopens their pull request. This event causes GitHub to look for a `pull_request_target` Actions workflow at the base branch of the pull request, “`deadbeef`”.
  6. Since the `deadbeef` branch no longer exists, GitHub resolves `deadbeef` to the attacker’s commit, finds the malicious Actions workflow in that commit, and proceeds to give it the repository secrets, as well as a `GITHUB_TOKEN` granting the attacker write access to the repository.5

Note that this attack scenario requires significant user interaction (an attacker would need to wait for someone to push an unusually-named branch by chance), so it’s much less severe than the attack described in the [previous blogpost](/2021/03/17/github-actions-write-access.html).

After I reported this issue to GitHub, they added a fix to ensure that `pull_request_target` events can only trigger from branches and not stray commits, which prevents this attack from working. At the time of writing this, it’s still possible to reopen a pull request with a deleted base branch, if the base branch name matches a commit shorthash in the repository. I don’t think that has any security impact anymore, but it looks pretty funny.

## Timeline

  * **2021-09-05 10:04:36 UTC** I reported this issue to GitHub via HackerOne
  * **2021-09-08 12:10:03 UTC** Initial response from GitHub
  * **2021-09-10 22:24:12 UTC** Issue confirmed by GitHub
  * **Sometime between 2021-10-07 and 2021-10-13** Issue fixed on github.com
  * **2021-11-18** GitHub awarded a $7500 bug bounty

I donated the bounty for this report to the [GiveWell Maximum Impact Fund](https://www.givewell.org/maximum-impact-fund), and GitHub generously matched the donation.

* * *

  1. Why does GitHub disallow that push? I think the main reason is to preserve the integrity of permalinks and commit hash checkouts. For example, users often presume that the URL `github.com/someone/some-repo/blob/a047be85247755cdbe0acce6f1dafc8beb84f2ac/foo/bar.sh` will always resolve to an immutable version of the file `foo/bar.sh` at the given commit hash. But if someone successfully pushed a branch called `a047be85247755cdbe0acce6f1dafc8beb84f2ac`, then GitHub would start returning a different version of `foo/bar.sh` from the branch, rather than the original version from the commit. To avoid this, GitHub blocks branch names consisting of exactly 40 hex characters.

In 2019, I sent GitHub a report that this protection could be bypassed by creating a branch called `a047be85247755cdbe0acce6f1dafc8beb84f2ac/foo` and putting a file called `bar.sh` in the repository root. As a result of that issue, GitHub now also blocks branch names that start with 40 hex characters followed by a slash. ↩

  2. The git CLI does the same thing. It’s probably not a coincidence that the git CLI and GitHub have matching behavior here – they both seem to be using the result of [`git rev-parse`](https://git-scm.com/docs/git-rev-parse). ↩

  3. This marks the third time that my practical-joke project has been instrumental in finding a security bug. I’m not really sure what to make of that. Maybe I can classify all of my practical jokes as “security research” now.

(The first time was described [here](/2019/11/12/github-actions-dos.html). The second time was a low-severity issue that I didn’t bother to write a blogpost about.) ↩

  4. Specifically, the branch name needs be parseable by `git rev-parse` as a commit hash. This can either be a hex string such as `deadbeef`, or it can be a string in the [`git describe`](https://git-scm.com/docs/git-describe) format such as `anything-123-gdeadbeef`, which will still resolve to the `deadbeef` commit. ↩

  5. Since the last blogpost, GitHub has introduced a significant number of opt-in security features that would reduce the blast radius of this type of attack, such as [Actions environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment). ↩

[](/2022/02/23/ghosts-of-branches-past.html)

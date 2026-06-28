---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-12_how-i-accidentally-took-down-github-actions.md
original_filename: 2019-11-12_how-i-accidentally-took-down-github-actions.md
title: How I accidentally took down GitHub Actions
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 2f91386742edc667940b39da34fdc7884d697a85bd311bf8b9a981649a15aef2
text_sha256: 27c19209a274ff1524b1f893dfaff032cbbc926a02c78d4c5e65dd4de259a074
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I accidentally took down GitHub Actions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-12_how-i-accidentally-took-down-github-actions.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2f91386742edc667940b39da34fdc7884d697a85bd311bf8b9a981649a15aef2`
- Text SHA256: `27c19209a274ff1524b1f893dfaff032cbbc926a02c78d4c5e65dd4de259a074`


## Content

---
title: "How I accidentally took down GitHub Actions"
page_title: "How I accidentally took down GitHub Actions | Teddy Katz’s Blog"
url: "https://blog.teddykatz.com/2019/11/12/github-actions-dos.html"
final_url: "https://blog.teddykatz.com/2019/11/12/github-actions-dos.html"
authors: ["Teddy Katz (@not_aardvark)"]
programs: ["GitHub"]
bugs: ["DoS", "Commit Hash Collisions"]
bounty: "5,000"
publication_date: "2019-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4948
---

# How I accidentally took down GitHub Actions

Nov 12, 2019 

Last December, I was invited to a private bug bounty program to test a beta version of [GitHub Actions](https://github.com/features/actions). GitHub Actions is a workflow automation tool integrated with GitHub. One common use case of GitHub Actions is for CI builds – a project can fairly easily start up a Docker container every time they push a commit (e.g.), and run their project’s tests in the container.

At the time, I wasn’t too familiar with the details of how GitHub Actions worked, so I decided to just try it out and see what would happen.

I used GitHub’s configuration wizard to create a config file. First, it let me select from a list of triggers for the Action (“do something when a commit is pushed”, “do something when someone creates an issue”, etc). I selected “do something when a comment is added to an issue”.

Next, it gave a list of options for what should happen when the trigger activates, which mainly consisted of different cloud services/containers (“Run something on AWS”, “Run code in Docker”, etc.). I selected “Run code in Docker” and specified that the file `./foo.sh` in the repository should be executed.

The config wizard created the following file for me (comments added here for explanation):
  
  
  workflow "New workflow" {
  resolves = ["GitHub Action for Docker"]
  on = "issue_comment" # When someone leaves an issue comment in this repo,
  }
  
  action "GitHub Action for Docker" {
  uses = "actions/docker/cli@76ff57a" # Set up a Docker container,
  runs = "./foo.sh" # ...and run `foo.sh` in this repo.
  }
  

Sure enough, when I committed that file to the repository and added a comment to an issue, it started a build that executed `foo.sh` in a Docker container.

I was a bit confused about the `uses = "actions/docker/cli@76ff57a"` line in the config file, so I looked at the build log. Near the top of the log, I saw that the build had downloaded and unzipped a tarball from `https://api.github.com/repos/actions/docker/tarball/76ff57a`. Eventually, I figured out that:

  * `https://github.com/actions/docker` was a repository containing integration code for GitHub Actions in a directory called `cli`. (Unfortunately, it seems to have been deleted sometime in the last year.)
  * `76ff57a` was the most recent commit hash on master for the `actions/docker` repository. That commit hash was auto-inserted by the config wizard when I created the config file.

So the runner for GitHub Actions would see the string `actions/docker/cli@76ff57a` in the config file, and then parse out the individual components: it would clone the `actions/docker` repository at commit `76ff57a`, enter the `cli` directory, and execute some setup code located there.

The commit hash `76ff57a` got my attention, because it was an abbreviated commit _shorthash_ (only 7 hex characters) rather than a full commit hash (40 hex characters).

## Commit Hash Collisions

A _commit hash_ is a pseudorandom 40-character hex string that identifies a git commit. An example of a commit hash is `76ff57a6c3d817840574a98950b0c7bc4e8a13a8`.

Since a string that long can be unwieldy, git sometimes shows an _abbreviated_ commit hash (sometimes called a “shorthash”) consisting of the first seven characters of the full commit hash. This is why GitHub generated the string `76ff57a` in my config file.

Commit shorthashes have a major problem: As a repository accumulates a large number of commits, eventually it will contain two commit hashes that start with the same seven characters (and have the same shorthash). After this happens, tools that use shorthashes will start to break because the commit shorthash is ambiguous (it’s no longer a pointer to a single commit). Due to the [birthday problem](https://en.wikipedia.org/wiki/Birthday_problem), any repository that has at least 19291 commits is likely to have a pair of ambiguous commits somewhere. So if we waited for the `actions/docker` repo to have tens of thousands of commits, one of the shorthashes would eventually become ambiguous and break someone’s build.

## Commit Hash Collisions, Faster

I didn’t really feel like waiting for a low-activity repo to accumulate tens of thousands of commits. Luckily, we only have to wait that long if commit hashes are generated pseudorandomly. If we’re creating commits while _trying_ to generate collisions, then it’s a lot easier – we can just create a single commit, then keep amending the commit message locally until it creates a commit hash that we want.

By coincidence, I had created a [tool](https://github.com/not-an-aardvark/lucky-commit) a couple years earlier that does exactly this as a practical joke. So I cloned the `actions/docker` repo (which had `76ff57a6c3d817840574a98950b0c7bc4e8a13a8` as the latest commit), created a new commit with some changes, and ran the tool. Two minutes later, I had different commit (`76ff57aa21370794040cd0caafd84d8a7aa0927c`) that also had the shorthash `76ff57a`.

To get the collision to affect anything on GitHub, I needed to push it to the `actions/docker` repo. This posed a problem, because I didn’t have write access to the `actions/docker` repo. However, I realized I could get around that issue by forking the `actions/docker` repo and pushing a commit to my fork (since GitHub shares commits between forks and parent repositories).

## GitHub Actions vs. Commit Hash Collisions

So I created a fork and pushed my commit to it. I wasn’t quite sure what GitHub would do if someone tried to download `https://api.github.com/repos/actions/docker/tarball/76ff57a` when the hash `76ff57a` was ambiguous. My best guess was that it would just pick one of the commits (either the original commit from `actions/docker`, or my new duplicate commit).

Instead, that URL just started returning a 404 error, causing my Actions build (and also everyone else’s build that used the latest commit from `actions/docker`) to break.

So the good news was that I’d found a security issue which could allow any GitHub user to DoS GitHub Actions builds globally. The bad news was that I’d accidentally just DoSed a part of GitHub Actions globally.

I had considered that this might happen, so I was ready to delete my fork as soon as I pushed the commit. (I thought deleting the fork would remove the ambiguity and cause everyone’s builds to start working again.) Unfortunately, even after I deleted my fork, the tarball URL _still_ returned a 404, meaning that I’d accidentally broken everyone’s builds with no way to fix them. Oops.

(In hindsight, I should have been more careful here. I could have tested out the tarball behavior on a test repo before using `actions/docker`. Luckily, at this point GitHub Actions was still in very early beta, so I’m hoping not too many people were affected.)

Anyway, I pinged someone on GitHub’s security team about the issue. After a few minutes, they were able to get the outage fixed by running a pass of [git garbage collection](https://git-scm.com/docs/git-gc). The root cause was fixed a few weeks later by updating the config wizard to generate full 40-character commit hashes in config files.

## Takeaways on Commit Shorthashes

This issue has had an effect on how I use commit shorthashes to refer to commits generally, when accounting for the possibility that someone could maliciously generate shorthash collisions.

Shorthashes _can_ safely be used for:

  * Identifying commits now or in the very near future (e.g. asking someone to take a look at your commit in the next few minutes)
  * Displaying commit hashes to users, if the full commit hash is also included somewhere. (For example, it’s okay to show a shorthash as the visible text in a link, as long as the target URL of the link includes the full 40-character hash).

Shorthashes _should not_ be used to identify commits for any extended period of time. This includes:

  * Build scripts (use full 40-character hashes instead)
  * Links in documentation (you can still use shorthashes for display if the full hash is included in the link target)

Again, the risk is that if you include a shorthash in your build script, any random troll (or careless security researcher) could decide to break your build script by generating a different commit with the same shorthash, and pushing it to a fork.

This issue would be somewhat mitigated if commit hashes on GitHub weren’t shared with forks. (As such, the risk is smaller for private repositories.) However, even if that were the case, someone without write access could still subtly introduce a collision by getting a PR accepted, or a shorthash could become ambiguous by chance over time. Personally, I think it’s better to just always follow the advice above to avoid a potential headache later.

## Making every shorthash collide

Finally, I thought it would be funny to create a git branch that uses _every_ 7-character commit shorthash (so every other commit in that repository would be guaranteed to have a shorthash collision).

Surprisingly, this is feasible. There are 167 total 7-character commit shorthashes, so by the [coupon collector’s problem](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem), we would need to hash something like 28 ⋅ 167 ≈ 7.5 billion test commits. This would take about 90 minutes on my laptop. In terms of storage space, the smallest git commit is about 175 bytes before compression, so the repository would weigh in at around (175 bytes) ⋅ 167 ≈ 47 GB.

Unfortunately, 47 GB is more space than I have left on my hard drive, so I didn’t go through with this. However, 47 GB is within [GitHub’s 100GB hard limit on repo size](https://help.github.com/en/github/managing-large-files/what-is-my-disk-quota#file-and-repository-size-limitations). I can imagine an attack scenario where someone creates that branch once, and then just forks a bunch of popular repos and pushes the same branch to all of the forks, breaking all shortlinks in the documentation/build scripts of lots of repos at once. (Please don’t actually do this – it probably violates GitHub’s ToS, and it’s possible GitHub has some protection against it anyway.)

**Update, several years later:** I went ahead and implemented a [proof-of-concept for this idea](https://github.com/not-an-aardvark/every-git-commit-shorthash). In total it’s only 24GB, but pushing it to GitHub would probably be a tall order.

## Timeline

(Some of these times are approximate due to limited logs/information from a year later.)

  * **2018-12-19, around 22:00:00 UTC:** I pushed a new `76ff57a` commit to my fork of `actions/docker`, inadvertently causing builds to start breaking.
  * **(about a minute later):** I deleted my fork of `actions/docker` in an unsuccessful attempt to fix the broken builds.
  * **2018-12-19 22:09:33 UTC:** I pinged someone from GitHub’s security team in a Slack that had been set up for the private bounty program.
  * **2018-12-19 22:13:08 UTC:** Initial response from GitHub on Slack. A short discussion about the issue ensued.
  * **2018-12-19, around 22:45:00 UTC:** GitHub ran GC on the `actions/docker` repo, which cleaned up the commit from my fork and resolved the immediate outage.
  * **2018-12-19 22:53:46 UTC:** Follow-up report about the issue submitted on HackerOne
  * **2018-12-19 23:11:30 UTC:** Initial response from GitHub on HackerOne
  * **2019-01-04 00:20:13 UTC:** $5000 bounty awarded from GitHub on HackerOne. Root cause fix was WIP at this point.
  * **(Sometime in the following week):** GitHub Actions config wizard updated to include full 40-character commit hash in generated config files, rather than 7-character shorthash.

[](/2019/11/12/github-actions-dos.html)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-06_dependabot-confusion-gaining-access-to-private-github-repositories-using-dependa.md
original_filename: 2023-05-06_dependabot-confusion-gaining-access-to-private-github-repositories-using-dependa.md
title: 'Dependabot Confusion: Gaining Access to Private GitHub Repositories using
  Dependabot'
category: documents
detected_topics:
- supply-chain
- command-injection
- path-traversal
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- path-traversal
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 66079c5a8ad17c87292d90df58b8a87d9e80eb564d3ad15804e55322de156d44
text_sha256: 8d389e5cefa9f58082f300cb8515735558ecfc511d152b3f7a2320c642046160
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Dependabot Confusion: Gaining Access to Private GitHub Repositories using Dependabot

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-06_dependabot-confusion-gaining-access-to-private-github-repositories-using-dependa.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, path-traversal, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `66079c5a8ad17c87292d90df58b8a87d9e80eb564d3ad15804e55322de156d44`
- Text SHA256: `8d389e5cefa9f58082f300cb8515735558ecfc511d152b3f7a2320c642046160`


## Content

---
title: "Dependabot Confusion: Gaining Access to Private GitHub Repositories using Dependabot"
url: "https://giraffesecurity.dev/posts/dependabot-confusion/"
final_url: "https://giraffesecurity.dev/posts/dependabot-confusion/"
authors: ["Giraffe Security"]
programs: ["GitHub"]
bugs: ["Dependency confusion"]
bounty: "2,500"
publication_date: "2023-05-06"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1182
---

# [![](/images/logo.png) Giraffe Security](/)

## Dependabot Confusion: Gaining Access to Private GitHub Repositories using Dependabot

May 6, 2023

[Tweet](https://twitter.com/share?ref_src=twsrc%5Etfw) [Follow @giraffesecurity](https://twitter.com/giraffesecurity?ref_src=twsrc%5Etfw)

![A meme about Dependabot](meme.png)

Dependabot is one of the most widely deployed tools to improve software supply chain security. But like all other software, it is not immune to security vulnerabilities. By using it, users take on the risk that any vulnerabilities in Dependabot itself may lead to the compromise of the very supply chain they are trying to secure. This article is about a vulnerability in Dependabot that allowed arbitrary user to gain access to a subset of GitHub repositories that have Dependabot enabled.

## A Little-Known Feature

Let’s start the analysis by discussing one of the less-known features of Dependabot.

Imagine that it is 2019 and you are using React 16.8.5 in your project and you come across a bug. You file an issue about it in GitHub, and it gets fixed. To see the issue fixed in your application, you would normally have to wait until the next release which may be months away. Luckily you can pick up the latest changes of React by specifying it as a Git dependency and taking on the latest changes from master rather than pulling the latest release from NPM registry. To do this, you would change the version requirement in your package.json file from `^16.8.5` to `git+https://[[email protected]](/cdn-cgi/l/email-protection)/facebook/react#f00be84`.

Now, if the next version of React gets released, you can change the dependency’s source back to the NPM registry. This is where Dependabot comes in — it is capable of detecting cases where you have temporarily changed the dependency’s source to Git in order to make use of unreleased changes. If these changes get released, Dependabot automatically creates a pull request to change the dependency’s source back to NPM registry, so you do not have to. Pretty neat, right?

![Diff of a Dependabot pull request that changes the source of React back to NPM registry](react.png)

## Security Implications

When I first saw this feature in action, it immediately became a point of interest, as I saw a huge problem with it. This problem concerns Git dependencies that are not published to the public NPM registry.

Organizations often have private packages they do not publish to the public NPM registry. One, perhaps the most common approach to distribute private packages, is to set up a private registry where all the internal packages are published. However, setting up a private registry introduces overhead and complexity and thus may not be worth it. The simpler solution is to specify the packages as Git dependencies instead. For example, if I have an internal package `giraffe-utils` in a GitHub repository `giraffesecurity/giraffe-utils` that I want to use in another project, I can specify it in the package.json file like this:
  
  
  {
  "giraffe-utils": "git+ssh://[[email protected]](/cdn-cgi/l/email-protection):giraffesecurity/giraffe-utils#master"
  }
  

Coming back to the Dependabot Git dependency source conversion feature, the question is how Dependabot determines whether you temporarily used Git source for a package or if the package is a Git dependency because the author has intentionally not uploaded it to NPM?

Well, luckily the code of Dependabot is [open source](https://github.com/dependabot/dependabot-core), so I was able to analyze the source code myself and see exactly how it works. The answer was, surprisingly, that all Git dependencies may be updated to come from the public registry. This means that if a malicious adversary guesses the name of a private dependency, they can upload a package with the same name to the public NPM registry and make Dependabot change the dependency’s source to the public one. The adversary is of course welcome to put any code they want into the package.

## Crafting an Exploit

After I discovered this seemingly unsafe behavior, I proceeded with building a proof of concept exploit that would make Dependabot replace an internal Git dependency with a dependency from the public registry.

The only issue I had to overcome was the condition that the Git dependency’s source can be changed to registry only if the latest version of the package contains the currently specified Git commit somewhere in its Git history. Dependabot checks whether this condition is true by finding the tag for the latest version in the dependency’s Git repository and comparing it to the commit specified in package.json of the project where the dependency is used.

In the React example at the beginning of the article, Dependabot would find commit `f00be84` (the currently used version) and commit referenced by tag `v16.8.6` (the potential new version). If the commit `f00be84` is the parent of or the same commit as `v16.8.6`, then the dependency source is converted from Git to the public NPM registry.

What is interesting is that these checks are performed in the Git repository that is specified in the package.json file of the version in the NPM registry. So even if the dependency has a source `git+ssh://[[email protected]](/cdn-cgi/l/email-protection):giraffesecurity/giraffe-utils`, Dependabot looks up the commits in the Git repository that is specified in the package.json file of the public NPM package `giraffe-utils`. Since the attacker controls that package, they can set up a repository that always matches the required condition for the dependency source conversion.

To summarise, all that is required is uploading an NPM package to the public registry and setting up a Git repository with the necessary Git tags. In the example of `giraffe-utils` where the dependency initially has a source `git+ssh://[[email protected]](/cdn-cgi/l/email-protection):giraffesecurity/giraffe-utils#master`, creating repository with one commit on master branch and tagging it with tag v1.0.0 (the version uploaded to registry) is sufficient to make Dependabot change the dependency’s source.

![Diff of a Dependabot pull request that changes
the source of giraffe-utils from Git to NPM registry](giraffe-utils.png)

## Impact

I presented a vulnerability that tricks Dependabot into making pull requests that introduce arbitrary code to the repository. It affects GitHub repositories that satisfy the following requirements:

  1. Dependabot must be turned on.
  2. The repository must use NPM, Yarn, or Bundler (although not discussed in the article, Bundler had the same issue) for dependency management.
  3. There must be a Git dependency whose name has not been claimed in the public package repository.

If these requirements are fulfilled, the attacker has to guess the name of the Git dependency in order to mount a successful attack. This may be difficult, but is also not impossible. For front-end projects, the dependency names may be present in the code bundle that everyone, including the attacker, can access. I have also seen that some companies have source maps for their front-end projects publicly available, meaning that the attacker can easily discover names of private Git dependencies.

After an attacker has identified the Git dependency, they can upload a package with the dependency’s name to NPM public registry. Then, Dependabot makes a pull request to the repository to change the dependency’s source. Once opened, the pull request introducing the malicious dependency may be merged and deployed to end users. That could happen when the repository has a workflow for automatically merging and deploying Dependabot pull requests or when the reviewer does not recognize that the dependency’s source is inadvertently being changed.

Regardless of whether the pull request is merged, most repositories these days have a continuous integration pipeline that could be compromised if it runs code in the attacker’s package. One can use a `preinstall` script to execute arbitrary code during installation. The `preinstall` script could exfiltrate source code or secrets from the continuous integration environment. For example, if the CI process uploads assets to Amazon S3, the attacker could steal AWS credentials. An attacker can also access any resources that are behind a firewall but accessible from CI environments.

## Fix

To fix the issue, GitHub removed the Git dependency to NPM public registry source conversion functionality from Dependabot. They rewarded me a bounty of $2500 for finding the issue.

## Takeaways

For people and organizations that use Dependabot – if you have an auto-merge workflow for Dependabot, reconsider it. After going through most of Dependabot’s public source code, I can say that the codebase is huge, convoluted, and filled with all sorts of edge cases and exceptions. Dependabot may look like a straightforward feature to implement, but the reality is that it is not. It likely contains more security vulnerabilities similar to the one I just presented.

Additionally, ensure you and others in your organization actually review Dependabot pull requests rather than blindly approving them.

For people that make software, whatever your role — every feature needs to have some sort of security review. The issue I discovered was a very simple one that the Dependabot team could have caught early on.

If you have any comments regarding this article, feel free to reach out to us at [[email protected]](/cdn-cgi/l/email-protection#17707e657671717257707e657671717264727462657e636e39737261).

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-17_github-secrets-exposed-due-to-rce-in-formatter-action-from-pull_request_target-e.md
original_filename: 2020-12-17_github-secrets-exposed-due-to-rce-in-formatter-action-from-pull_request_target-e.md
title: Github Secrets exposed due to RCE in Formatter Action from pull_request_target
  event
category: documents
detected_topics:
- command-injection
- sso
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- sso
- otp
- automation-abuse
language: en
raw_sha256: 0d9c6db59581286b36f0510c344435485e3b08bb59c1c06efc8bead29188fd14
text_sha256: 205cf9c59813e72e68778711b3a22163946d925c669f9fd43ded00bcd90a6762
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Github Secrets exposed due to RCE in Formatter Action from pull_request_target event

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-17_github-secrets-exposed-due-to-rce-in-formatter-action-from-pull_request_target-e.md
- Source Type: markdown
- Detected Topics: command-injection, sso, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `0d9c6db59581286b36f0510c344435485e3b08bb59c1c06efc8bead29188fd14`
- Text SHA256: `205cf9c59813e72e68778711b3a22163946d925c669f9fd43ded00bcd90a6762`


## Content

---
title: "Github Secrets exposed due to RCE in Formatter Action from pull_request_target event"
page_title: "Github Secrets exposed due to RCE in Formatter Action from pull_request_target event | Anthony Weems"
url: "https://lf.lc/vrp/175896812/"
final_url: "https://amlw.dev/vrp/175896812/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["RCE"]
bounty: "500"
publication_date: "2020-12-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4063
---

#  Github Secrets exposed due to RCE in Formatter Action from pull_request_target event 

December 17, 2020

### Vulnerability Details#

The formatter action is triggered on `pull_request_target` events, which run with the context of the base repository and is therefore allowed to mount secrets. However, the formatter action specifically checks out the reference from the Pull Request (which is attacker controlled code). This breaks the security benefits of `pull_request_target` and exposes secrets to the attack code. This might be acceptable when the action does not allow for code exec. However, the formatter action later runs the command:
  
  
  mvn com.coveo:fmt-maven-plugin:format
  

Running `mvn` with an attacker-controlled pom.xml file can lead to remote code execution in the action.

Steps to replicate:

  1. Find a target repository with the formatter action. For example, <https://github.com/googleapis/java-core/blob/master/.github/workflows/formatting.yaml>.
  2. Fork the repository from a Github account without write access to the repo
  3. Inject malicious XML into the Maven pom.xml file a. For example, modify the pom.xml to include a malicious pluginRepository b. Create a backdoored version of `com.coveo:fmt-maven-plugin` and host this at your pluginRepository
  4. Commit this pom.xml file, push to a branch in your fork
  5. Create a PR against the main googleapis/java-core repo
  6. Observe the formatter action runs against the PR and executes the backdoored plugin

To demonstrate, I have created a copy of the googleapis/java-core repo (not a fork) and configured my own fake secret in this repo. I then created a fork of this repo in a separate account and executed the steps above. I have provided a screenshot of the resulting exploit shown in the Github action log. After performing the attack, I converted both repositories to private repos. I can grant access to the repository or provide my backdoored plugin at Google’s request.

**Initial pull request to repository:** ![Initial pull request to repository](/assets/vrp/175896812-pr.png)

**Backdoored pom.xml file to use custom Maven repository:** ![Backdoored pom.xml file to use custom Maven repository](/assets/vrp/175896812-backdoor-pom.png)

**Github action output showing ACCESS_TOKEN and malicious commits to master:** ![Github action output showing ACCESS_TOKEN and malicious commits to master](/assets/vrp/175896812-action-output.png)

**Malicious commit to master from attacker created action:** ![Malicious commit to master from attacker created action](/assets/vrp/175896812-malicious-commit.png)

As shown above, the attacker tigres-builder created a malicious commit on master in the victim repo (amlweems/java-core) by simply making a PR against the repo.

### Attack Scenario#

Any Github user can compromise a service account and push code to all googleapis repositories.

Any Github user can make a PR against repositories in the `googleapis` and execute arbitrary code in the context of a pull_request_target event. Since this event is trusted, Github mounts secrets (e.g. the Github token and, in this case, the `YOSHI_CODE_BOT_TOKEN` secret from the repo). As a result, the attacker gains access to both of these secrets and could push code to the target repository or compromise the <https://github.com/yoshi-code-bot> account. Based on commit history, this account appears to have write access to to most repositories in the `googleapis` organization.

### Timeline#

  * 2020-12-17: Issue reported to Google VRP
  * 2020-12-21: Issue triaged
  * 2020-12-23: Internal bug report filed
  * 2021-01-08: Issue fixed
  * 2021-02-25: VRP issued reward ($500)

#### Discussion on Impact#

VRP at _Jan 12, 2021 11:20AM_ :
  
  
  As a part of our Vulnerability Reward Program, we decided that it does not meet
  the bar for a financial reward, but we would like to acknowledge your
  contribution to Google security in our Hall of Fame:
  
  https://bughunter.withgoogle.com/rank/hm
  
  Rationale for this decision:
  
  YOSHI_CODE_BOT_TOKEN was the only secret exposed to pull_request_target and the
  associated yoshi-code-bot user has very limited permissions. It can create pull
  requests, but not push directly to any repository.
  

me at _Jan 12, 2021 11:28AM_ :
  
  
  Thanks for the reply!
  
  While the YOSHI_CODE_BOT_TOKEN is the only secret, the Github token is also
  exposed to any pull_request_target and it has write privileges to the
  repository (since pull_request_target is enabled). The runner automatically
  configures this token in the .git/config of the repo so that any git commands
  "just work" and I demonstrated this in the screenshots in my initial report.
  
  As a result, every repository with the formatter action could be modified by an
  attacker.
  

VRP at _Jan 14, 2021 05:36PM_ :
  
  
  Thanks I've updated the product team and they'll take another look
  

me at _Feb 9, 2021 02:04PM_ :
  
  
  Hey, just wanted to check in and see if there was a response here. If it's
  helpful, the screenshots in my original report show that it's possible to make
  a commit with just the GITHUB_TOKEN, which is what was exposed in the case of
  the googleapis repos.
  

VRP at _Feb 10, 2021 04:23PM_ :
  
  
  The product team has noted that this should be fixed.
  

me at _Feb 19, 2021 10:04AM_ :
  
  
  I've confirmed it is fixed. I'm asking that this be re-examined for impact and
  bounty. As per above, the previous rationale was:
  
  "YOSHI_CODE_BOT_TOKEN was the only secret exposed to pull_request_target and
  the associated yoshi-code-bot user has very limited permissions. It can create
  pull requests, but not push directly to any repository."
  
  However, this is not the full picture. The GITHUB_TOKEN was also exposed,
  giving the attacker write access to any affected repo (which included dozens of
  repos in the googleapis org).

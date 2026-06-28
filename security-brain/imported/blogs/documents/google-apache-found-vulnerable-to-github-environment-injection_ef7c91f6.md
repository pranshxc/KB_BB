---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-01_google-apache-found-vulnerable-to-github-environment-injection.md
original_filename: 2022-09-01_google-apache-found-vulnerable-to-github-environment-injection.md
title: Google & Apache Found Vulnerable to GitHub Environment Injection
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: ef7c91f68e665fd98c760d7ddae76d84710bed78a189bc636ccbc646b77027eb
text_sha256: ef0e273ef43f9c175c558049f6ad36813cb577e89988d965ad3a78bdb0e09777
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Google & Apache Found Vulnerable to GitHub Environment Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-01_google-apache-found-vulnerable-to-github-environment-injection.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `ef7c91f68e665fd98c760d7ddae76d84710bed78a189bc636ccbc646b77027eb`
- Text SHA256: `ef0e273ef43f9c175c558049f6ad36813cb577e89988d965ad3a78bdb0e09777`


## Content

---
title: "Google & Apache Found Vulnerable to GitHub Environment Injection"
url: "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability-0"
final_url: "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability-0"
authors: ["Noam Dotan"]
programs: ["Google", "Apache"]
bugs: ["Privilege escalation", "CI/CD"]
publication_date: "2022-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2227
---

**SHARE:** [](https://twitter.com/intent/tweet?text=https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability-0) [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability-0)

In this blog post, we'll discuss a new type of GitHub Actions workflow vulnerability we called "GitHub Environment Injection". We've found a couple of top-tier open-source organizations vulnerable to this attack: Google Firebase and Apache. Both Google and Apache acknowledged the issues we reported and fixed their workflows accordingly. Those organizations contained repositories that had workflows that download an untrusted artifact and dumped its content into a GitHub environment file. As we’ve seen previously, using untrusted data in a privileged context can open the door to CI/CD pipeline takeover risk and allow a malicious actor to take control of the pipeline.

In this write-up, we’ll cover the vulnerable Google Firebase workflows and how they can lead to a software supply chain attack. To keep this blog within a reasonable length and due to similarities between the cases, we won’t cover the Apache case, but you can find their fix [here](https://github.com/apache/camel/commit/1e64de78999396bc0b8603470df12440f126c1bb "https://github.com/apache/camel/commit/1e64de78999396bc0b8603470df12440f126c1bb").

This post is the 3rd in the series of _Vulnerable GitHub Actions Workflows_ , following:

  * [Part 1: Privilege Escalation Inside Your CI/CD Pipeline](https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability")

  * [Part 2: Actions That Open the Door to CI/CD Pipeline Attacks](https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks "https://www.legitsecurity.com/blog/github-actions-that-open-the-door-to-cicd-pipeline-attacks")

## **Google Firebase - The Vulnerable Workflows Found**

The following firebase repositories: <https://github.com/firebase/friendlyeats-web> & <https://github.com/firebase/codelab-friendlychat-android/> contain a workflow named “preview_deploy.yml” that deploys a preview version of the application to Firebase in order to test it before merging:

![GitHub Actions workflow example with artifact download](https://www.legitsecurity.com/hubfs/vulnerable_workflow-jpeg.jpeg)

The workflow works as follows:

  * It is triggered whenever a workflow named “Generate Preview” finishes

  * It downloads two artifacts (zip files) that were uploaded by the “Generate Preview” workflow: pr.zip and firebase-android.zip

  * It then reads the pull-request number from ‘pr.zip' and writes it into the ‘pr_number' environment variable

  * lastly, it unzips the firebase app and deploys it

## **What is $GITHUB_ENV?**

From GitHub documentation:

“You can make an environment variable available to any subsequent steps in a workflow job by defining or updating the environment variable and writing this to the `GITHUB_ENV` environment file.”

This is a special file that whenever input is redirected to it, the runner engine takes it and sets environment variables accordingly.

For example, in the above workflow, line 47 sets an environment variable named “pr_number” to the “NR” file content.

![](https://www.legitsecurity.com/hs-fs/hubfs/github_env_usage-jpeg.jpeg?width=526&name=github_env_usage-jpeg.jpeg)

## **Yet another case of a vulnerable GitHub-Actions workflow**

The workflow downloads artifacts that were uploaded by a pull request triggered workflow and writes its content into $GITHUB_ENV. Since anyone can create a pull request and upload artifacts for public repositories, an attacker can craft an artifact payload that would set arbitrary environment variables in the privileged context (for more information about workflow_run and how privilege escalation attacks can take place when it is used insecurely, take a look at [Part 1](https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability "https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability")).

For example, if the file in line 47 (“NR”) had the following content: “123\nTEST=BLA”, the command would translate to ![GitHub Action setting environment variables example](https://www.legitsecurity.com/hs-fs/hubfs/env_injection-jpeg.jpeg?width=488&name=env_injection-jpeg.jpeg)

resulting in two environment variables being set instead of only “pr_number” as the workflow author intended.

OK, so we can set environment variables as we wish. Now let’s leverage this to execute code in the privileged workflow.

Linux has many special environment variables that control how programs behave which we can modify to execute code. For example, we can use “LD_PRELOAD” to load some malicious binary that we add in the pull request, or alternatively, use the more convenient “NODE_OPTIONS”. The “NODE_OPTIONS” env is used to provide additional command line parameters to the node engine. For example, the below value will tell the node engine to print “123” at the beginning of every node program:

![Node Options with Experimental Modules and Loader Example](https://www.legitsecurity.com/hubfs/dummy_malicious-jpeg.jpeg)

With this information in our hands, let’s build the final exploitation workflow:

  1. Fork one of the vulnerable Firebase repositories

  2. Create the below workflow:

  3. ![GitHub Actions script with experimental loader setup](https://www.legitsecurity.com/hubfs/exploit-jpeg.jpeg)
  4. Create a pull request to the original repository

  5. **The “NODE_OPTION” payload would dump the process environment variables to the console with all the sensitive secrets and** keys

An adversary that wishes to initiate a supply chain attack could create a more sophisticated payload that would modify the repository build artifacts, releases, and tags, and in some cases, the main branch source code to deliver a poisoned version of this code.

## **Surprisingly, a variation of this vulnerability was previously discovered by Google**

Felix Wilhelm from Project Zero found [a similar issue](https://bugs.chromium.org/p/project-zero/issues/detail?id=2070&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids "https://bugs.chromium.org/p/project-zero/issues/detail?id=2070&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids") a couple of years ago. He discovered that GitHub Actions set-env mechanism is broken and makes thousands of workflows vulnerable. Back then, to set an environment variable while the workflow was executing, one had to log a specific character sequence to STDOUT which the Action runner would pick up and change the container environment accordingly

![GitHub Actions: Setting PR number in environment variable](https://www.legitsecurity.com/hs-fs/hubfs/old_set_env2-jpeg-1.jpeg?width=619&name=old_set_env2-jpeg-1.jpeg)

This implementation of workflow commands was fundamentally insecure since logging to STDOUT is a widespread practice, and attackers could inject a malicious payload that would trigger the set-env command quite easily. The ability to modify environment variables creates multiple paths to RCE with the most obvious payload is the one shown before:

![Node.js environment variable exploit demonstration](https://www.legitsecurity.com/hubfs/real_malicious-jpeg.jpeg)

To mitigate this risk, GitHub took the following actions:

  1. Deprecate the set-env command in favor of the file command: <https://github.blog/changelog/2020-10-01-github-actions-deprecating-set-env-and-add-path-commands/>, which makes it harder for attackers to modify environment variables, like in the line below: 

  1. ![Setting environment variable in GitHub Actions](https://www.legitsecurity.com/hs-fs/hubfs/basic_env-jpeg-1.jpeg?width=331&name=basic_env-jpeg-1.jpeg)
  2. Create a list of blocked environment variables that cannot be changed: 
  1. ![Blocked environment variable set attempt in code](https://www.legitsecurity.com/hs-fs/hubfs/block_list-jpeg.jpeg?width=633&name=block_list-jpeg.jpeg)

## **Different symptoms but same disease**

The problem with the new implementation is:

  1. Although the migration from STDOUT commands to file commands helped mitigate this risk, we did find quite a few repositories that write unsafe data to the environment file, such as the ones from Firebase described above. With control on the payload written to the env-file attackers can modify environment variables as they wish.

  2. GitHub didn’t migrate the blocklist code from the STDOUT commands to file commands <https://github.com/actions/runner/blob/main/src/Runner.Worker/FileCommandManager.cs> doesn’t contain the code listed above

So, once again, if an attacker manages to modify environment variables, the path to attacking the organization’s software supply chain is very short.

We reported these findings to GitHub, but unfortunately, they decided not to fix it, claiming they “consider users to be responsible for any vulnerabilities arising from these insecure Actions workflows. So it’s up to the repositories maintainers to make sure they are safe. Google Firebase and Apache aren’t the only cases we found. **Since using the**`GITHUB_ENV`**file is currently considered the safe way to change environment variables in GitHub Actions, many repositories are using workflows that write untrusted data into the environment file, leaving them exposed to** pipeline takeover risk.

## **What Can You Do to Protect Yourselves**

  * Never write untrusted input data to the environment file

  * Restrict the GitHub token permissions only to the required ones, this way, even if an attacker will succeed in compromising your workflow, they won’t be able to do much

  * Prefer using Actions output parameters instead of environment variables

  * If possible, check that the triggering workflow doesn’t belong to a forked repository, and if it does require human approval as explained in this blog post: [Using Environment Protection Rules to Secure Secrets When Building External Forks with pull_request_target](https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci "https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci")

## **Timeline**

  * April 5th: report the issue to Apache through ASF Security Team

  * April 5th (a few hours later): Apache fixed the issue

  * April 30th: reported issue to Google through their bug bounty program

  * May 2nd: received first response from Google

  * June 29th: Google fixed the issue and provided approval for the write-up ([b2f24955a5d6909706f7528bc5a6d7250f9373a5](https://github.com/firebase/codelab-friendlychat-android/commit/b2f24955a5d6909706f7528bc5a6d7250f9373a5 "https://github.com/firebase/codelab-friendlychat-android/commit/b2f24955a5d6909706f7528bc5a6d7250f9373a5") & [df65aefd24cf6f092a27a5576067ff9f29aa2ef1](https://github.com/firebase/friendlyeats-web/commit/df65aefd24cf6f092a27a5576067ff9f29aa2ef1 "https://github.com/firebase/friendlyeats-web/commit/df65aefd24cf6f092a27a5576067ff9f29aa2ef1"))

## **Legit Security Can Help You Prevent Software Supply Chain Attacks**

The Legit Security platform connects to your GitHub organization and detects vulnerable workflows such as this one in real-time and much more. If you are concerned about these vulnerabilities and others across your software supply chain, please contact us or [request a demo](https://info.legitsecurity.com/demo-of-the-legit-security-platform "https://info.legitsecurity.com/demo-of-the-legit-security-platform") on our [website](https://www.legitsecurity.com/ "https://www.legitsecurity.com/").

  
  
  
  
  
  
  
  
  

Need guidance on AppSec for AI-generated code?

Download our new whitepaper.

![Legit-AI-WP-SOCIAL-v3-1](https://www.legitsecurity.com/hubfs/Legit-AI-WP-SOCIAL-v3-1.png)

###

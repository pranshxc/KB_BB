---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-15_securing-developer-tools-git-integrations.md
original_filename: 2022-03-15_securing-developer-tools-git-integrations.md
title: 'Securing Developer Tools: Git Integrations'
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- access-control
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- access-control
- automation-abuse
- api-security
language: en
raw_sha256: 955ec439ebd845c332b73ecc010975f74c0e32d02bfadc54e45064646cda534f
text_sha256: 915fb271031af2b24f1e687b173fc0b6354a734e4ed8373e721c1627a3175824
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Developer Tools: Git Integrations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-15_securing-developer-tools-git-integrations.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, access-control, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `955ec439ebd845c332b73ecc010975f74c0e32d02bfadc54e45064646cda534f`
- Text SHA256: `915fb271031af2b24f1e687b173fc0b6354a734e4ed8373e721c1627a3175824`


## Content

---
title: "Securing Developer Tools: Git Integrations"
page_title: "Securing Developer Tools: Git Integrations | Sonar"
url: "https://blog.sonarsource.com/securing-developer-tools-git-integrations"
final_url: "https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/"
authors: ["Sonar (@SonarSource)"]
programs: ["Microsoft", "JetBrains", "GitHub"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-03-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2814
---

## TL;DR overview

  * Git integrations in developer tools create a security attack surface where malicious repository contents can exploit how tools invoke Git, leading to argument injection or hook execution vulnerabilities.
  * Specially crafted .gitconfig files, commit messages, or branch names can influence the behavior of tools that invoke Git without properly sanitizing the inputs passed to git commands.
  * Git hooks—scripts that Git executes automatically on specific events—can be used by attackers who can write to a repository's .git/hooks directory, executing arbitrary code on any system that clones or runs the affected repository.
  * Teams should restrict which Git repositories their CI/CD systems can access, disable unsafe hooks in untrusted repositories, and review all tool invocations of Git for argument injection risks.

Attacks against developers are increasing and in the past year, dozens have been documented. For instance, a threat actor [recently distributed a backdoored version of a .NET development tool](https://www.bleepingcomputer.com/news/security/trojanized-dnspy-app-drops-malware-cocktail-on-researchers-devs/) to deploy multiple malicious payloads, like a clipboard hijacker and a crypto miner. In another recent example, a [campaign attributed to a North Korean entity](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/) has set up social network profiles and websites to social engineer and infect prominent figures of the developer community with malicious Visual Studio projects or browser exploits 

Developers are an attractive target for cybercriminals, as they have access to the core intellectual property assets of a company: the source code. Compromising a single developer enables attackers to embed malicious code into a company's products. If that product is then used by other companies, the malware can spread to their systems in a so-called supply chain attack.

Our security researchers recently discovered vulnerabilities and unexpected behaviors in various tools used by developers, which could have helped threat actors to launch similar targeted attacks. After a first article covering package managers ([Securing Developer Tools: Package Managers](https://blog.sonarsource.com/securing-developer-tools-package-managers)), this second publication focuses on Git integrations in terminals and code editors. We show how simple actions like opening an archive in a terminal or in a code editor can let attackers compromise a system. We demonstrate this risk with the official Git terminal prompt and Microsoft’s Visual Studio Code, but this same scenario affects a broad range of products.

While some of these findings are already known to the maintainers of the impacted projects, we hope to raise awareness on these problems and help to reach a consensus on how these risks should be mitigated to make the developer ecosystem safer. A few weeks after starting the responsible disclosure of these findings, we were put in relation with Justin Steven, a security researcher investigating similar vulnerabilities. We coordinated the publications of the technical details: you can find Justin’s publication [on his blog](https://www.justinsteven.com/).

## How it can impact you

The vulnerabilities covered in this article all allow the execution of arbitrary commands upon access to a malicious folder planted on the victim’s system. This attack vector applies only to folders obtained through other means than Git, like other source control management tools or website downloads. Cloning a remote repository does not retrieve the files necessary to conduct this attack. 

For instance, a plausible attack scenario would be the following:

  * An attacker crafts a malicious Git repository with a local configuration file;
  * The attacker compresses these files in an archive and sends it to the victim, e.g. over email;
  * The victim opens it in a vulnerable application;
  * The victim's computer is now compromised by the attacker.

![Visualisation of a realistic attack scenario](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/e5a73f20-2e75-4f18-8235-b46efd86a3cf/body-716bca34-27a2-4035-9b42-fb51a9774d76_RD-127_support%25402x.png)

We demonstrated this risk in three code editors, leading to a bypass of the trusted workspace feature of the two first ones:

  * Microsoft Visual Studio Code < 1.63.1 (CVE-2021-43891)
  * JetBrains IDEs < 2021.3.1 (CVE-2022-24346)
  * GitHub Atom (not fixed)

We could also demonstrate it across a broad range of Git integrations for terminals, like the official Git implementation, Oh My Zsh or fish. After reaching out to the Git maintainers, it was concluded that there will always be potentially dangerous features in Git via this attack vector: the only solution is then to change user security expectations when using Git integrations.

We believe that this attack vector could also be used to compromise software working on user-supplied Git repositories. This is the original scenario pursued by Justin Steven in his research, leading to interesting vulnerabilities in security tools deliberately downloading remote Git configurations to the local system. 

## Technical Details

In this section, we come back to one of the Git features that we used to achieve the local execution of arbitrary commands upon access to a malicious folder.

### Root Cause: Git Local Configuration

Git supports configuration from three sources, each level superseding the previous one: system (e.g. `/etc/gitconfig`), global (e.g. `~/.gitconfig`) and later repository-local (e.g. `.git/config`). 

The [upstream documentation](https://git-scm.com/docs/git-config) describes the available configuration directives quite thoroughly. One of them, [core.fsmonitor](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsmonitor), caught our attention:

> _If set, the value of this variable is used as a command which will identify all files that may have changed since the requested date/time._

Most Git commands will invoke the command specified in `core.fsmonitor`, if set, as soon as they need to query information about files present in the local repository, among which are git status and git diff. 

To demonstrate this behavior without forcing you to read Git’s code, create an empty folder and then create both the file `.git/config` with a `core.fsmonitor` set:

Copy to clipboard
  
  
  $ git init
  $ echo 'fsmonitor = "id>/tmp/fsmonitor"' >> .git/config
  $ git status
  $ cat /tmp/fsmonitor
  uid=501(user) gid=[...]

Running git status in an untrusted folder has proved dangerous! Now, what could be running such commands automatically without the user’s knowledge?

### Example of affected Terminal Integration: Git Prompt

The root cause of this vulnerability is similar for most prompts and the majority are vulnerable by default. As soon as a Git command with support for the directive `core.fsmonitor` is invoked, the arbitrary command is executed. 

Let’s have a look at the upstream implementation of the Git shell integration in Git (`contrib/completion/git-prompt.sh`). The script exports a function named `__git_ps1` that is intended to be placed in the user's shell primary prompt (`$PS1`). It invokes git diff after detecting that it is in a work tree and the prompt configuration `GIT_PS1_SHOWDIRTYSTATE` is set:

**contrib/completion/git-prompt.sh**

Copy to clipboard
  
  
  __git_ps1 ()
  {
      # [...]
      elif [ "true" = "$inside_worktree" ]; then
      if [ -n "${GIT_PS1_SHOWDIRTYSTATE-}" ] &&
          [ "$(git config --bool bash.showDirtyState)" != "false" ]
      then
              git diff --no-ext-diff --quiet || w="*"            
              git diff --no-ext-diff --cached --quiet || i="+"
              if [ -z "$short_sha" ] && [ -z "$i" ]; then
                      i="#"
              fi
      fi

As a result, `git diff` triggers the `core.fsmonitor` directive and automatically executes a potentially malicious system command in the background.

#### Proof-of-Concept - cd considered harmful!

In the following video, we reproduced the scenario of an attack against a developer using `git-prompt.sh` with `GIT_PS1_SHOWDIRTYSTATE=1`. We could verify that other Git prompts, like Oh My Zsh or fish, are generally vulnerable by default, and the exploitation process steps are strictly similar. 

In our demo, a developer simply downloaded an archive from an untrusted source, extracted it, and entered the resulting directory with the shell. This harmless behavior results in the execution of an arbitrary system command placed by the attacker, in our case, opening a calculator:

#### How to protect yourself?

We are not aware of an easy way to mitigate this risk while using the official Git program. As soon as subcommands like git status are invoked in folders containing an untrusted Git repository, attackers will have ways to execute unintended commands.

We believe that it would be very hard to establish a list of “safe” configuration directives. Various other ways to force the hidden execution of commands with a local configuration would still exist. Instead, maintainers should not only try to override settings like `core.fsmonitor`, but rather disable Git integrations by default or at least those that run without the user’s prior consent. 

After reaching out to the Git maintainers, it was concluded that there will always be potentially dangerous features in Git via this attack vector: the only solution is then to change user security expectations when using Git integrations. **For now, our sole recommendation is to disable SCM prompts when dealing with untrusted data.**

Please follow the recommendations of the maintainers of your prompt to disable the Git integration, or set the following variable to temporarily disable it:

Copy to clipboard
  
  
  # If you are using bash, zsh
  PS1=\s-\v\$
  # If you are using fish
  function fish_prompt
  printf '%s' $PWD ' $ '
  end

It is interesting to note that alternative Git implementations (e.g. JGit) may not always implement support for features like `core.fsmonitor`. 

### Example of affected IDE: Visual Studio Code

Visual Studio Code, the open-source and cross-platform IDE developed by Microsoft, is now the most popular development editor per Stack Overflow's latest survey. Part of its success is its modularity and the broad range of external modules available in the official marketplace. 

Because of the risks associated with the execution of package managers and other various external commands, Visual Studio Code introduced a feature called  _Workspace Trust_. This is a mechanism by which extensions can change their behavior depending on the trust status of the current project, with the goal to prevent the execution of any risky operation on untrusted codebases. For instance, package management modules will not be executed as long as the current workspace is not trusted.

This feature doesn’t mean that malicious projects won’t be able to compromise the system, only that you have to manually mark it as trusted first. This behavior is clearly documented in the official documentation and the Workspace Trust prompt itself:

![Visual Studio Code Workspace Trust prompt](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/27e8674b-2b58-4033-a899-d2207e619e02/body-3923a198-551b-4e39-a121-e5479636a5e1_Screenshot%2B2022-03-04%2Bat%2B15.17.15.png)

The vulnerability we describe below can also be applied to other IDEs, like the JetBrains suite and GitHub Atom. Jetbrains introduced a feature named _Trusted Projects_ in 2021.3.1, while GitHub decided to accept this risk. 

In the following sections, we focus on Visual Studio Code and show how malicious folders could force the execution of arbitrary commands even in trusted workspaces.

#### The Git extension

Visual Studio Code is shipped with the Git extension enabled by default, and declares its features in `vscode/extensions/git/package.json`. Up until version 1.63.1, it explicitly stated that it runs in untrusted workspaces (e.g. the user is still looking at the  _Workspace Trust_ prompt, or marked the current folder as untrusted):

Copy to clipboard
  
  
   "capabilities": {
     "virtualWorkspaces": true,
     "untrustedWorkspaces": {
       "supported": true
     }

That means that features of this extension will be invoked as soon as a folder is opened before the  _Workspace Trust_ prompt is even displayed. We dynamically traced the invocations of external commands (e.g. here with Objective-See’s `ProcessMonitor`) and could confirm that Git is invoked several times before the prompt:

Copy to clipboard
  
  
  [...]
  {"event":"ES_EVENT_TYPE_NOTIFY_EXEC", "process":{"name":"git", "arguments":["/usr/local/bin/git","rev-parse","--show-toplevel"]}
  {"event":"ES_EVENT_TYPE_NOTIFY_EXEC", "process":{"name":"git", "arguments":["/usr/local/bin/git","rev-parse","--git-dir"]}
  {"event":"ES_EVENT_TYPE_NOTIFY_EXEC", "process":{"name":"git", "arguments":["/usr/local/bin/git","status","-z","-u"]}
  [...]

This is explained by the willingness to show meaningful information to users as soon as they open the editor, but that also means that the execution of `core.fsmonitor` happens immediately. 

#### Proof-of-Concept

In the following video, we reproduced the scenario of an attack against a developer. They downloaded an archive from an untrusted source, extracted it in a temporary folder, and chose to open it in Visual Studio Code. It results in the execution of an arbitrary command, here a calculator:

The same exploitation scenario can be applied to the JetBrains IDEs suite and GitHub Atom. The former did not have the Git plugin behind the project trust feature, while the latter deliberately does not have this feature at all.

#### How to protect yourself?

External invocations of Git being unsafe in untrusted folders, the Visual Studio Code maintainers decided to enable this extension only in trusted workspaces ([67d6356a](https://github.com/microsoft/vscode/commit/67d6356a25661ecd2bdaf13a3fc8c9d14ee5161f)). We think this is a great choice, as the  _Workspace Trust_ documentation is really clear about the inherent risks. Microsoft assigned CVE-2021-43891 to this vulnerability, as well as a consequent monetary bounty that we donated to charities. 

The patch is included starting from Visual Studio Code 1.63.2, and you likely already benefit from it if you did not disable automatic updates; if so, you should consider enabling it as similar vulnerabilities are fixed several times per year. JetBrains also took the same approach to mitigate this risk in the IntelliJ suite starting from 2021.3.1, and assigned CVE-2022-24346 to this behavior. 

Even if GitHub Atom chose not to fix this risk, [GitHub Desktop recently fixed a vulnerability using a very similar exploitation scenario found by Vladimir Metnew](https://github.com/Metnew/write-ups/tree/main/rce-github-desktop-2.9.3): by forcing users to download a file to their local filesystem upon access to a malicious web page, they could ask GitHub Desktop to use this archive as a Git repository and Git filters led to the execution of arbitrary commands on the user’s behalf. 

## Timeline

**Date**| **Action**  
---|---  
2021-08-30| We report this Visual Studio Code vulnerability to Microsoft.  
2021-09-01| We report the vulnerability in the IntelliJ IDEs to JetBrains. They let us know they are already aware of this risk.  
2021-09-02| We report the vulnerability in Atom to GitHub. The submission is closed as Informative, being outside of their threat model.  
2021-11-01| Microsoft releases Visual Studio Code 1.63.2, with the Git extension behind Workspace Trust.  
2021-12-29| JetBrains releases the version IntelliJ 2021.3.1 with broader support of Trusted Projects.  
  
## Summary

In this article, we presented how disparities between the Git threat model and its actual use could affect the security of developers' tools where it is integrated. We demonstrated an attack against the popular terminal integration Git Prompt and IDE Visual Studio Code whereas many other products were found to be vulnerable against the same attack.

Our research is far from comprehensive as other CVS tools and less popular code editors were omitted. We hope to raise awareness of this problem and help the various affected projects to reach a consensus on how these risks should be mitigated. Developer tools need to modernize their threat models to take such targeted attacks into account and better educate users about the inherent risks. 

As a general rule, it should be considered unsafe to open third-party source code in modern IDEs (but it’s still OK in nano!) or to navigate through it with a terminal with shell integrations. You should turn to disposable virtual machines for such tasks and always keep code editors up-to-date. Workspace Trust is a great feature, even though it can ultimately lead to a form of  _decision fatigue_. 

We would like to thank all the maintainers involved in the numerous bug reports and discussions, as well as Justin Steven for his precious help in the coordinated disclosure process and his review of this article.

## Related Blog Posts

  * [Securing Developer Tools: Package Managers](https://blog.sonarsource.com/securing-developer-tools-package-managers)
  * [Vulnerability Research Highlights 2021](https://blog.sonarsource.com/vulnerability-research-highlights-2021)
  * [Agent 008: Chaining Vulnerabilities to Compromise GoCD](https://blog.sonarsource.com/gocd-vulnerability-chain)
  * [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer)

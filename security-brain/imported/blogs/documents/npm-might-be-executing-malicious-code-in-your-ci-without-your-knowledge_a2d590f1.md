---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-03_npm-might-be-executing-malicious-code-in-your-ci-without-your-knowledge.md
original_filename: 2022-01-03_npm-might-be-executing-malicious-code-in-your-ci-without-your-knowledge.md
title: NPM might be executing malicious code in your CI without your knowledge
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: a2d590f1982e2f88c647f744b717717fdd1472861f490719466605b657622fca
text_sha256: 61a3053846ce75580cfaf78d692dad156df79ddcdb9fb2f8a58e9ed3d9bd43a3
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# NPM might be executing malicious code in your CI without your knowledge

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-03_npm-might-be-executing-malicious-code-in-your-ci-without-your-knowledge.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `a2d590f1982e2f88c647f744b717717fdd1472861f490719466605b657622fca`
- Text SHA256: `61a3053846ce75580cfaf78d692dad156df79ddcdb9fb2f8a58e9ed3d9bd43a3`


## Content

---
title: "NPM might be executing malicious code in your CI without your knowledge"
url: "https://medium.com/cider-sec/npm-might-be-executing-malicious-code-in-your-ci-without-your-knowledge-e5e45bab2fed"
authors: ["Rotem Bar (@rotembar)"]
programs: ["GitHub"]
bugs: ["RCE"]
publication_date: "2022-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3033
scraped_via: "browseros"
---

# NPM might be executing malicious code in your CI without your knowledge

NPM might be executing malicious code in your CI without your knowledge
Rotem Bar
Follow
5 min read
·
Jan 3, 2022

95

How to tell if you are using NPM safely within your CI

Press enter or click to view image in full size

The JavaScript ecosystem is highly reliant on dependencies. And all I wanted was a method to safely download my desired dependencies from the internet.

The industry standard for doing so in Javascript is “NPM” or “Node Package Manager”. As a developer, when installing node.js software, I usually run “npm install” to download all the necessary packages for the software to run correctly.

Running “npm install” does two things automatically:

It downloads required dependencies from the internet.
It runs all scripts necessary to properly build the software.

Both of these actions come with security risks. You can read about the risks associated with the first one in my article on dependency attacks, but this article is all about potential problems with the second — running external scripts.

In its first phase, NPM goes to the package repository and fetches the needed packages. To authenticate against this package repository, it usually uses secrets/credentials which are accessible to the NPM client when accessing the package repository.

When running the second phase, NPM executes scripts, but even though access to the package repository is no longer required, NPM still has access to the same credentials while doing so.

Why is this a problem?

When NPM installs and runs scripts, it does so for all of the package dependencies, their dependencies, and so on. Because the developer doesn’t control all the sub-dependencies and their scripts, unverified and potentially malicious scripts will gain automatic access to the credentials and secrets used in the first action stated above.

To mitigate this problem, NPM allows you to use the command “ignore scripts”, to disable all scripts associated with dependencies from running. But now we have a different problem: there are packages that need the ability to run scripts for purposes such as compiling, fetching resources, etc. These desired scripts can be executed separately, after the install phase. This would prevent the scripts from gaining access to secrets that are necessary only at the installation phase.

For example:

# Install phase with access to secrets
(
  NODE_AUTH_TOKEN=your-secret-token-here
  npm ci --ignore-scripts
)
# Build phase with no access to secrets
(
  npm rebuild
  npm run install --if-present
  npm run prepare --if-present
)

For more details about how to do this see this great article on a secure way to run NPM CI by Wild Wild Wolf.

However, this solution on its own is not enough

In my previous article about malicious code analysis, I described how security scanning tools can be affected by the environment they are running in. For example, when a scanner is executed inside a certain directory, it will begin by picking up any configuration files it needs from its current directory.

Get Rotem Bar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

These configuration files are supposed to tell the tools how to behave (e.g., to skip certain directories, skip checks, ..). Some, however, can also be used to instruct the tool to execute commands, thereby using the scanning tool itself to perform the unwanted actions it is meant to prevent.

The same method can be applied to NPM. By adding a .npmrc file to the intended repo, the developer can manipulate the configuration which is picked up by the “npm” command.

For example, in NPM version 6, adding the command
“onload-script=${PWD}/evil-script” to the .npmrc file will execute the script “evil-script” (also added to the repository by the malicious developer) even if NPM has been given the “ignore scripts” command. In version 6, this will happen when executing any npm command, including the security function “npm audit,” “npm ci — ignore-scripts” and any other command such as “npm whoami”.

A similar action can be taken in the later npm versions 7 and 8 by replacing the git command in .npmrc, adding the following line to the configuration file: “git=${PWD}/evil-script.sh”. In this case, this would only affect the “npm ci” and “npm i” functions, however, the scope of potential harm is exactly the same.

This means that any developer is able to execute code on almost any pipeline in your organization if it is using “npm”. Running a simple script to extract environment variables can seriously damage your environment. Therefore, obtaining developer permissions (whether by an attacker or a rogue developer looking to hack pipelines) can be used to cause real harm.

Disclosing the flaw to NPM:

I contacted NPM (GitHub) through their official bug bounty program and got the following response:

Essentially ignore-script is designed to prevent the execution of malicious pre/post-install scripts of packages defined inside dependencies. CI Triggered on a pull request is intended to execute any code pushed as part of PR, however, this class of issue is usually prevented by running CI jobs in an isolated environment which GitHub Actions and Travis CI employs.

I agree in principle that isolating CI Jobs and giving them minimal permissions is a wise preventative measure, but it can be very hard to implement in practice.

In my experience, I have seen many different CI/CD solutions — and have encountered many pipelines that still allow too much access to internal resources. While steps are being taken in the right direction, I still believe that the safest option would be a “defense in depth” approach. This means that we need to both isolate the environments of our CI/CD and adjust the tools we run to prevent unintended code execution.

To continue pursuing the subject, I have opened an issue to NPM which is still under triage:

https://github.com/npm/cli/issues/4101

What should I do?
Run CI/CD functions in isolated environments which contain the minimal needed permissions to both resources on the host as well as to external resources.
Execute NPM securely by separating the script execution from the install phase (See above).
Possible Workarounds for ensuring the trustworthiness of npm configurations
Remove project configuration file (from a cloned repository) before using npm.
Copy project configuration file from external trusted resources (not controlled by developers).
Implement measures to detect potentially malicious changes in configurations (such as in .npmrc files) before triggering the build process.

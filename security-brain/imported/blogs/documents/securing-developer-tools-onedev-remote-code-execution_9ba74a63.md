---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-20_securing-developer-tools-onedev-remote-code-execution.md
original_filename: 2022-09-20_securing-developer-tools-onedev-remote-code-execution.md
title: 'Securing Developer Tools: OneDev Remote Code Execution'
category: documents
detected_topics:
- command-injection
- supply-chain
- access-control
- ssrf
- xss
- otp
tags:
- imported
- documents
- command-injection
- supply-chain
- access-control
- ssrf
- xss
- otp
language: en
raw_sha256: 9ba74a6343dbbb7ca76bb003d2e9f9204d54ab0f3210e3f903c3c806d5143224
text_sha256: 61ad91abadf681666a810e3b110b78327f54719a55c206746feff690b59af6a9
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Developer Tools: OneDev Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-20_securing-developer-tools-onedev-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, access-control, ssrf, xss, otp
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `9ba74a6343dbbb7ca76bb003d2e9f9204d54ab0f3210e3f903c3c806d5143224`
- Text SHA256: `61ad91abadf681666a810e3b110b78327f54719a55c206746feff690b59af6a9`


## Content

---
title: "Securing Developer Tools: OneDev Remote Code Execution"
page_title: "Securing Developer Tools: OneDev Remote Code Execution | Sonar"
url: "https://blog.sonarsource.com/onedev-remote-code-execution/"
final_url: "https://www.sonarsource.com/blog/onedev-remote-code-execution/"
authors: ["Paul Gerste"]
programs: ["OneDev"]
bugs: ["RCE", "SSRF", "Broken Access Control", "Container escape"]
publication_date: "2022-09-20"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2144
---

## TL;DR overview

  * Sonar's research identified a remote code execution vulnerability in OneDev, a self-hosted DevOps platform, that allows an attacker to execute arbitrary code on the server hosting the OneDev instance.
  * The vulnerability stems from unsafe handling of user-controlled data in a server-side execution path, a class of flaw that static analysis can reliably detect when code is analyzed with interprocedural taint tracking.
  * Because OneDev manages code repositories and CI/CD pipelines, a successful compromise grants attackers access to source code, secrets, and build infrastructure—making the blast radius exceptionally large.
  * OneDev users should update to the patched version immediately; teams self-hosting any DevOps platform should regularly scan platform code with SonarQube and monitor for upstream security advisories.

OneDev is a self-hosted Git server that comes with a lot of development-oriented features such as CI/CD, code search, and static analysis integration. With almost 10,000 stars on GitHub, it is gaining popularity and becoming an open-source and low-maintenance alternative to GitHub, GitLab, and Bitbucket.

Source code becomes an increasingly important asset of most companies, making it crucial to protect it from being stolen or, even worse, altered by malicious actors. This is why we decided to look at the very services that are the most interesting targets of these threat actors: source code hosting platforms.

In this article, we describe the vulnerabilities we found in OneDev that could be used by attackers to take over vulnerable instances. We will first look at their impact, then dive into the technical details, and finally, we'll discuss how the maintainers fixed the issues and how you can prevent them in your own code.

## Impact

We discovered the following vulnerabilities in OneDev 7.2.9:

  * Web Hook Server-Side Request Forgery
  * Access Control Bypass leading to Remote Code Execution (CVE-2022-39205)
  * Docker Escape (CVE-2022-39206)
  * Persistent Cross-Site Scripting (CVE-2022-39207)
  * Git Repository Disclosure (CVE-2022-39208)

Some of them can be combined by attackers to execute arbitrary commands on vulnerable OneDev instances. This would allow them to steal or manipulate source code, build artifacts, and launch further attacks against internal infrastructure. Most of the vulnerabilities require authentication as a regular user, except for CVE-2022-39208 which can be exploited without any authentication at all. The following is an overview of how the vulnerabilities can be exploited:

![Vulnerability overview](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/249298b7-458f-4688-ac65-6334e13b245c/body-e7018079-7e77-4a6e-b0ba-6602af1c7425_OneDev-attack-diagram.png)

We strongly recommend updating to at least version 7.3.0 to benefit from the maintainer's fixes.

Since the OneDev maintainers are using the OneDev instance at [code.onedev.io](https://code.onedev.io) to develop the project, attackers could have hijacked the project's infrastructure to plant malicious code into OneDev itself. This would have allowed them to compromise users of OneDev without having to directly attack them. Such a software supply chain attack is very stealthy and has happened before, for example in the [Codecov](https://www.bleepingcomputer.com/news/security/hundreds-of-networks-reportedly-hacked-in-codecov-supply-chain-attack/) and [SolarWinds](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12) incidents, and could have also happened in the [open-source](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/) [world](https://blog.sonarsource.com/php-supply-chain-attack-on-pear/).

## Technical Details

In this section, we will look at the technical details of three vulnerabilities that can be combined into a chain. First, we will look at a Server-Side Request Forgery issue, then we will see how it can be used to achieve Remote Code Execution, and finally, we will show how attackers could have used a Docker misconfiguration to escape from a container to the host system.

### Server-Side Request Forgery

A common feature among source code hosting platforms is the ability to add webhooks that will be triggered by certain events. An example use case for this is to trigger a deployment on every push to a repository's main branch. This functionality requires the user to set a URL and an event type, telling the server to send an HTTP request to that URL when events of that type occur. The request usually contains the event data in its body. This is what the feature looks like for OneDev:

![Screenshot of OneDev's web hook page](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/987dc9b8-e499-4958-bc6d-aca670bedf6c/body-8b34b072-be3d-462d-84b6-5d5560434728_Screenshot%2B2022-09-19%2Bat%2B15.46.13.png)

In the case of OneDev, the target URL of a webhook is not restricted at all (besides having to be a syntactically valid URL). This allows users to force the server to make HTTP requests to internal targets, including the server itself, by setting the webhook URL to an internal IP address and triggering the defined event.

This is known as Server-Side Request Forgery (SSRF), which can be used to talk to internal systems and trigger further vulnerabilities in them. In this case, it is a limited SSRF: the user does not control the HTTP method or any HTTP headers, they only control some parts of the body, and they can't see the HTTP response. This limits the user-controlled inputs that can be passed to an internal server to the URL, i.e. its path and query parameters.

The OneDev maintainers did not request a CVE for this vulnerability because they see it as intended behavior. They expect OneDev setups to be so diverse that blocking certain IP ranges could lead to issues for some users. The next section will cover how it was possible to use this SSRF to reach an internal endpoint, bypass its protection, and execute arbitrary code on the server.

### Access Control Bypass leading to Remote Code Execution (CVE-2022-39205)

To validate push events, OneDev uses Git commands under the hood. This is implemented with a callback endpoint that will be called whenever a push event happens. This endpoint is only supposed to be called from localhost, so the following check was introduced:

Copy to clipboard
  
  
  protected void doPost(HttpServletRequest request, HttpServletResponse response) {
      String clientIp = request.getHeader("X-Forwarded-For");
      if (clientIp == null) clientIp = request.getRemoteAddr();
  
      if (!InetAddress.getByName(clientIp).isLoopbackAddress()) {
          response.sendError(HttpServletResponse.SC_FORBIDDEN,
                  "Git hook callbacks can only be accessed from localhost.");
          return;
      }
  // ...
  }

The endpoint checks if the client's IP address is the loopback address, e.g. `127.0.0.1`, but it blindly trusts the `X-Forwarded-For` header if present. This is unsafe, as it requires a proper reverse proxy to be deployed in front of the OneDev instance. Otherwise, attackers can spoof their IP address by simply setting that header.

In case there is a properly configured reverse proxy, this check can still be bypassed using the SSRF vulnerability described above. Since the server sends the webhook request to itself, the sender's IP address will always be the loopback address.

After that initial check, the callback endpoint will read some parameters from the request. This includes a project ID, a user ID, and commit hashes. These values are then used to check certain conditions based on the project's settings and the user's permissions. Finally, a Git command will be executed based on the previous checks. OneDev invokes this command in a safe way that prevents Command Injection and Argument Injection vulnerabilities.

However, the callback also takes environment variables from the request's query parameters. They are then passed to the Git command invocation, which is very unsafe because the behavior of programs can be influenced by specifying certain environment variables.

**Making Git write files**

Modern versions of Git support [setting any config value via environment variables](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGCOUNT), which would be enough to execute arbitrary commands. This can be achieved by setting the `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_*`, and `GIT_CONFIG_VALUE_*` variables. However, the Git version that was shipped in the default Docker container of OneDev was older, so this option was not feasible.

Another technique to control program behavior via environment variables is to use `LD_PRELOAD` which allows specifying a shared library that can override certain functions used by a binary. This would require first uploading such a shared library to the filesystem, making it also not feasible in this scenario without an additional vulnerability.

We noticed that OneDev uses Git hooks to validate some Git events and that the hooks were simple shell scripts. These files were also writable by the user that the OneDev server runs as, so it would be possible to overwrite them with malicious commands. We then checked the Git documentation for any environment variable that would enable writing to an arbitrary file. We found `GIT_TRACE_SETUP`, which is used to activate the output of verbose debugging information, either to `STDERR` or to a file that can be specified in the variable's value. Its output looks like this:

Copy to clipboard
  
  
  $ env GIT_TRACE_SETUP=/tmp/trace.txt git status
  On branch main
  No commits yet
  nothing to commit (create/copy files and use "git add" to track)
  $ cat /tmp/trace.txt
  15:40:18.109099 trace.c:311             setup: git_dir: .git
  15:40:18.109933 trace.c:312             setup: git_common_dir: .git
  15:40:18.109940 trace.c:313             setup: worktree: /tmp/git-trace
  15:40:18.109947 trace.c:314             setup: cwd: /tmp/git-trace
  15:40:18.109953 trace.c:315             setup: prefix: (null)

This approach looked promising, but it had some drawbacks: 

  * First, only some parts of the output can be controlled via other environment variables; 
  * Second, Git would only append to existing files, not overwrite them. This is especially problematic here, because the Git hook scripts all ended with a call to `exit` on their last line, ending the execution of the script regardless of what comes in the next lines; 
  * The last straw that remained here was that the scripts had no linebreak at the very end, which meant that we could execute commands in a subshell if we could inject them in the first line of the trace output.

**Controlling the output**

This first line contains the value of `git_dir` and it can be controlled via the `GIT_DIR` environment variable. It has to point to a valid Git directory, otherwise, the whole command will fail and no trace output will be written. It is also not possible to insert non-existing segments into the path because Linux will complain in that case. This means the attacker needs to create a folder with a subshell command in its name on the filesystem first, and then they can use a `GIT_DIR` path that includes this directory and then traverses back to a valid Git directory.

Since the attacker in our scenario already has access to a project on the OneDev server, they can do this by creating and pushing a new branch. Branches are stored in a Git repository as `.git/refs/heads/<branchname>`. Branch names can include slashes, so this can result in multiple nested directories, but the last "segment" of a Git branch name will always be a file that holds the branch's most recent commit hash. So to create a branch that suits the needs of the exploit, the attacker has to include at least one slash after the subshell command to make sure the command will be in a directory name, not in a file name.

Putting it all together, the attacker would create and push such a branch and then use `GIT_DIR` and `GIT_TRACE_SETUP` to append to a Git hook. This is what such a hook script will look like afterward:

Copy to clipboard
  
  
  [...]
  exit $returnCode15:50:06.391600 trace.c:311             setup: git_dir: .git/refs/heads/$(id>/tmp/pwned)/../../../../../
  15:50:06.393284 trace.c:312             setup: git_common_dir: .git/refs/heads/$(id>/tmp/pwned)/../../../../../
  15:50:06.393318 trace.c:313             setup: worktree: /private/tmp/git-trace
  15:50:06.393336 trace.c:314             setup: cwd: /private/tmp/git-trace
  15:50:06.393352 trace.c:315             setup: prefix: (null)

### Container Escape (CVE-2022-39206)

OneDev recommends starting the server with access to a Docker socket to enable its Docker-based CI/CD pipelines. If the OneDev server is hosted in a Docker container itself, this is recommended to be done by mounting the host's Docker socket into the OneDev container.

This is dangerous because it allows breaking out of the container and executing commands as root on the host system unless Docker runs in rootless mode. OneDev also mounts the host's Docker socket into certain CI/CD pipeline containers, making it even possible for users with the appropriate permissions to perform a Docker escape by simply defining a malicious CI configuration.

The following summarizes the whole exploit chain:

![Exploit overview](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/955908a1-e6eb-452f-a387-09a5a87552c8/body-f773fe17-0020-4f67-8f2f-cb673437b944_OneDev-exploit-diagram.png)

### Patch

The SSRF vulnerability has not been fixed because the OneDev team expects the environment that OneDev can be deployed in to have a big variety with no common denominator. According to them, it is impossible to have a one-fits-all blocklist for webhook URLs, so they did not implement one.

We think it would be a good middle ground to have an admin setting that can control such a blocklist and give it a default value that blocks requests to all local and private IP ranges. If you have code in your own code base that makes requests based on user-controlled values, make sure to properly validate each request. The most important thing here is to validate the protocol, hostname, and port. Modifying them can allow attackers to talk to internal services that are otherwise not exposed. Such services are usually less secured and attackers could make requests to them in order to hijack them. Keep in mind that the validation has to be done at the right moment to be effective, as explained in [our recent blog post about a similar issue in WordPress](https://blog.sonarsource.com/wordpress-core-unauthenticated-blind-ssrf/).

**Access Control Bypass**

For the Access Control Bypass vulnerability, the maintainers introduced a new system of authentication tokens that have to be sent with each request and are validated before any actions are performed. This is a very solid solution because even SSRF vulnerabilities can't be used to trigger the endpoint as the attacker would have to know a valid token first.

As a rule of thumb, never blindly trust HTTP headers like `X-Forwarded-For`, unless you made really sure that they cannot be set by an attacker. A good recommendation is to make trusting these headers opt-in instead of opt-out, reducing the likelihood of accidentally trusting them.

**Container Escape**

The Container Escape vulnerability was only possible because the host's Docker socket was exposed in environments where users with low privileges could use it. This is an unsafe pattern and should be avoided. Make sure that only trusted users (e.g. admins) can access the socket and that all parameters that are included in requests to it are properly validated. There are also third-party proxies, such as [docker-socket-proxy](https://github.com/Tecnativa/docker-socket-proxy), that can restrict the Docker interface to a safer subset of possible requests.

## Timeline

**Date**| **Action**  
---|---  
2022-05-30| We report all issues to the OneDev maintainers  
2022-05-30| The OneDev maintainers confirm the issues  
2022-05-31| The OneDev maintainers fix the issues (except the SSRF), release a new version (7.3.0) and rebuild the code.onedev.io instance from scratch to ensure that it is not backdoored  
2022-09-13| The CVE IDs are assigned  
  
## Summary

In this article, we presented several high-impact vulnerabilities we found in OneDev, an open-source Git server. The issues have a critical impact but require a low-privileged user account to be exploited. While this reduces the impact for many instances, it was possible for attackers to take over the infrastructure of the OneDev itself, which could have resulted in a widespread impact for many users of the project.

We discussed the technical details of the vulnerabilities and also explained how the maintainers chose to tackle them, as well as how you can prevent such issues in your code.

Finally, we want to give big kudos to the OneDev maintainers handling the disclosure of these vulnerabilities. They responded exceptionally fast and fixed the issues within a day, also rebuilding the project's infrastructure from scratch to get rid of potential backdoors that could have resulted from malicious actors abusing the issues described in this blog post.

## Related Blog Posts

  * [Agent 008: Chaining Vulnerabilities to Compromise GoCD](https://blog.sonarsource.com/gocd-vulnerability-chain/)
  * [WordPress Core - Unauthenticated Blind SSRF](https://blog.sonarsource.com/wordpress-core-unauthenticated-blind-ssrf/)
  * [Securing Developer Tools: Argument Injection in Visual Studio Code](https://blog.sonarsource.com/securing-developer-tools-argument-injection-in-vscode/)
  * [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/)

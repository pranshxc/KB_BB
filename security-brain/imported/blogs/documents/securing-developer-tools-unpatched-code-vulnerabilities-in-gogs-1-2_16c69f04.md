---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-02_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-12.md
original_filename: 2024-07-02_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-12.md
title: 'Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (1/2)'
category: documents
detected_topics:
- command-injection
- supply-chain
- ssrf
- access-control
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- ssrf
- access-control
- automation-abuse
- api-security
language: en
raw_sha256: 16c69f04efd21be6d72fb77188e81573c5c132b731eb523b364464070143c475
text_sha256: bc3382cd1af60e28f328ce28561a8be29728f16bc051aaf3075dc3b568fe03d4
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (1/2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-02_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-12.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, ssrf, access-control, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `16c69f04efd21be6d72fb77188e81573c5c132b731eb523b364464070143c475`
- Text SHA256: `bc3382cd1af60e28f328ce28561a8be29728f16bc051aaf3075dc3b568fe03d4`


## Content

---
title: "Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (1/2)"
page_title: "Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (1/2) | Sonar"
url: "https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-1/"
final_url: "https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-1/"
authors: ["Thomas Chauchefoin (@swapgs)", "Paul Gerste"]
programs: ["Gogs"]
bugs: ["Argument injection", "Security code review"]
publication_date: "2024-07-02"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 200
---

## TL;DR overview

  * Sonar's research uncovered multiple critical vulnerabilities in Gogs—a self-hosted Git service—that remain unpatched, including argument injection and SSRF flaws that allow authenticated or unauthenticated attackers to execute code on the Gogs server.
  * The unpatched status is notable: Sonar followed responsible disclosure procedures, but some findings were not addressed, leaving the Gogs user base exposed to exploitable attack chains.
  * Organizations self-hosting Gogs face significant risk: a compromised Git service gives attackers access to source code, deployment keys, and CI/CD pipeline configurations.
  * Teams running Gogs should evaluate migrating to actively maintained Git platforms; until then, restricting Gogs access to trusted internal networks and applying strict authentication controls reduces exposure.

Most companies today value their source code as an important asset and rely on cloud services like GitHub or operate their own source code hosting platform to manage this asset. One option for this is [Gogs](https://gogs.io/), an open-source solution for self-hosting source code.

With over 44,000 stars on GitHub, Gogs is among the most popular Go projects. Its Docker image has been downloaded over 90 million times, indicating that many developers use it. In light of our blog post series on securing developer tools, we investigated the code base of Gogs for security vulnerabilities.

We discovered **four unfixed vulnerabilities in Gogs** that allow attackers to compromise vulnerable instances, enabling them to steal source code, plant code backdoors, wipe all code, and more.

This blog post will first cover the impact of the vulnerabilities we found and reported. We will then discuss the technical details of one of those vulnerabilities. Finally, we will provide recommendations and patches for users to help them protect their Gogs installations. This blog post is the first in a series of two. Next week's article will cover more details on the remaining vulnerabilities.

## Impact

We found the following vulnerabilities and reported them to the maintainers of Gogs:

  1. Argument Injection in the built-in SSH server (CVE-2024-39930, CVSS 9.9 Critical)
  2. Argument Injection when tagging new releases (CVE-2024-39933, CVSS 7.7 High)
  3. Argument Injection during changes preview (CVE-2024-39932, CVSS 9.9 Critical)
  4. Deletion of internal files (CVE-2024-39931, CVSS 9.9 Critical)

Unfortunately, the maintainers did not implement fixes and stopped communicating with us at some point after initially accepting our report. All four vulnerabilities are still present in the latest release of Gogs (0.13.0) and the latest commit in the Gogs repository (`5bdf91e` at the time of writing). **To protect yourself, read our recommendation section below.**

Attackers can use vulnerabilities 1, 3, and 4 to execute arbitrary commands on the Gogs server. The commands will run under the same use that Gogs is running as (configured via `RUN_USER`). This allows them to read all source code on the instance, modify any code, delete all code, or attack internal hosts reachable from the Gogs server. Vulnerability 2 allows attackers to read arbitrary files from the Gogs server. These files include the source code stored on the Gogs instance and configuration secrets, likely allowing the attacker to impersonate other users and gain more privileges.

All four vulnerabilities require an attacker to be authenticated. You can find more details about the exploitability of vulnerability 1 in the _Exploit Requirements_ section below. A quick [Shodan search](https://www.shodan.io/search?query=http.component%3A%22Gogs%22) lists around 7300 open Gogs instances:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/30878b95-a949-4a1a-97a9-febf6039a666/shodan-gogs-report-card.png)

We did not confirm how many of these are exploitable, nor do we have any data on whether or not malicious actors are exploiting these vulnerabilities in the wild.

## Technical Details of CVE-2024-39930

Like many source code hosting platforms, Gogs allows users to push and pull Git repositories over SSH. For this, Gogs comes with a built-in SSH server that admins can activate. This built-in server uses the `golang.org/x/crypto/ssh` package under the hood, which does most of the heavy lifting, such as implementing the SSH protocol, handling authentication, etc.

Gogs adds code on top of that, which handles authorization and maps repos to their respective internal file path. This is done by executing a helper executable that is part of Gogs. To understand the vulnerability we found in the binding code between the SSH library and the helper executable, we will take a quick detour into the SSH protocol:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/789423bb-e9e8-4b89-92d7-737a9164d5ba/SSH%20Flow%20Example.png)

An SSH connection starts with a client establishing a TCP connection with the server (1). The client and server then perform a handshake (2) that includes authentication, usually using public key cryptography. After the handshake successfully finishes, the client opens a channel with the type `session` (3), and the server confirms (4). Inside this channel, the client can send requests consisting of a type and a payload. For example, a client would send a `shell` request (5) to establish a classic interactive SSH session.

For Git-over-SSH, the client uses `env` and `exec` requests. While the former is used to set environment variables like `GIT_PROTOCOL`, the latter is used to start a Git process on the server that the client can then directly talk to and exchange repository data. Gogs handles these requests in [internal/ssh/ssh.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/ssh/ssh.go#L57-L79):

Copy to clipboard
  
  
  switch req.Type {
  case "env":
      var env struct {
          Name  string
          Value string
      }
      if err := ssh.Unmarshal(req.Payload, &env); err != nil {
          log.Warn("SSH: Invalid env payload %q: %v", req.Payload, err)
          continue
      }
      // Sometimes the client could send malformed command (i.e. missing "="),
      // see https://discuss.gogs.io/t/ssh/3106.
      if env.Name == "" || env.Value == "" {
          log.Warn("SSH: Invalid env arguments: %+v", env)
          continue
      }
      _, stderr, err := com.ExecCmd("env", fmt.Sprintf("%s=%s", env.Name, env.Value))
      if err != nil {
          log.Error("env: %v - %s", err, stderr)
          return
      }
  case "exec":
      // ...
      return
  default:
  }

We can see that the handler parses the payload of an `env` request into a name and a value. It then checks that both are not empty strings and executes a command to set the respective environment variable. The command is in the form `env <name>=<value>`, where `<name>` and `<value>` are user-controlled. So, what is the vulnerability here?

The command is not executed in a shell context, and the arguments are passed as an array instead of constructing a complete command string. This correctly prevents Command Injection vulnerabilities, so sending a variable like `FOO=$(id > /tmp/pwned)` would **not** result in the execution of the `id` command here.

However, Command Injection vulnerabilities have a sneaky sibling: Argument Injections. In this case, the beginning of an argument to a command is user-controlled, so what happens when `env` is executed with an argument like `--foo=bar`?

Copy to clipboard
  
  
  $ env --foo=bar
  env: unrecognized option '--foo=bar'
  Try 'env --help' for more information.

The `--` prefix makes the `env` command use the provided argument as an option instead of a positional argument! Since options usually modify the behavior of a command, they can be helpful for attackers to make a command do unintended things. In the case of `env`, the help message does not look promising at first glance:

Copy to clipboard
  
  
  Usage: env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]
  Set each NAME to VALUE in the environment and run COMMAND.
  Mandatory arguments to long options are mandatory for short options too.
    -i, --ignore-environment  start with an empty environment
    -0, --null           end each output line with NUL, not newline
    -u, --unset=NAME     remove variable from the environment
    -C, --chdir=DIR      change working directory to DIR
    -S, --split-string=S  process and split S into separate arguments;
                          used to pass multiple arguments on shebang lines
    -v, --debug          print verbose information for each processing step
        --help     display this help and exit
        --version  output version information and exit
  A mere - implies -i.  If no COMMAND, print the resulting environment.

If the attacker could provide an additional **positional** argument, it would be executed as a command. However, the single argument passed to `env` will always contain an equals character (`=`) and never be considered as `COMMAND`. All the other options are not helpful for attackers since they don't allow for command execution, file writes, or something similarly interesting. Or are they?

At a second glance, the `--split-string` option seems interesting: "process and split S into separate arguments". Could this be used to control the positional `COMMAND` argument? Let's try it out with a command that should print `foo` to stdout:

Copy to clipboard
  
  
  $ env '--split-string=echo foo'
  foo

It worked! We can see what happens under the hood by adding the `-v` option for verbosity:

Copy to clipboard
  
  
  $ env -v '--split-string=echo foo'
  split -S:  ‘echo foo’
   into:    ‘echo’
       &    ‘foo’
  executing: echo
     arg[0]= ‘echo’
     arg[1]= ‘foo’
  foo

At first, `env` recognizes the `--split-string` option (with its short form `-S`) and explains that it splits the string `echo foo` into two separate arguments: `echo` and `foo`. It then continues processing the arguments and recognizes `echo` as the positional `COMMAND` argument it should execute. It further parses `foo` to be the first of the positional `ARGS` arguments and, therefore, sets it as the first argument for the `echo` command. Finally, `echo foo` is executed and prints `foo`.

This feature is Argument Injection heaven for attackers! By controlling a single options argument, arbitrary arguments can be passed to the command. Bringing this into the context of Gogs' SSH handler, it becomes clear that an attacker can execute any command on the Gogs server by connecting via SSH and sending an environment variable with the name `--split-string` and the desired command as the value.

### Exploit Requirements for CVE-2024-39930

The requirements for a successful attack depend on the exact Gogs setup. For all Gogs instances, the **built-in SSH server has to be enabled**. You can check this by visiting the admin panel's configuration page (at `/admin/config`) and checking in the "SSH configuration" section if SSH is enabled and the built-in server is activated:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/830c204a-9637-4eed-b2cb-95cb9d36d7f8/gogs-admin-config-ssh.png)

In addition, the **attacker needs a valid SSH private key** for the instance. If the Gogs instance has registration enabled, the attacker can simply create an account and register their SSH key. Otherwise, they would have to compromise another account or steal a user's SSH private key.

Finally, **successful exploitation depends on the server's version of the`env` binary**. Not all versions support the `--split-string` option required to abuse the Argument Injection vulnerability. In our tests, the `gogs/gogs` Docker image was not exploitable because it is based on Alpine Linux, which uses the BusyBox implementation of `env`.

Ubuntu and Debian use the GNU coreutils version of `env`, which supports the option and is therefore exploitable. You can test your Gogs server by checking if `env --help` lists `--split-string` as a valid option.

Gogs instances running on Windows are unexploitable, as no `env` command is available there.

## Recommendations: How to Protect Yourself

Unfortunately, the maintainers of Gogs stopped responding to our disclosure at some point after initially accepting our report. Therefore, all four of our reported vulnerabilities are unpatched in the latest version of Gogs. To help users protect themselves, we have curated a list of mitigations and additional recommendations.

### Immediate Mitigations

**Disable the built-in SSH server:** To prevent the exploitation of the Argument Injection vulnerability discussed in this blog post, we recommend turning off the built-in SSH server in your `app.ini`:

Copy to clipboard
  
  
  [server]
  START_SSH_SERVER = false

Alternatively, you can disable SSH entirely if you don't need it (Git operations will still work via HTTP):

Copy to clipboard
  
  
  [server]
  DISABLE_SSH = true

**Disable user registration:** While this will not prevent existing users from exploiting the vulnerabilities, it will protect you from the mass exploitation of malicious actors that scan the internet for vulnerable instances. To turn off the registration of new user accounts, set the following option in your `app.ini`:

Copy to clipboard
  
  
  [auth]
  DISABLE_REGISTRATION = true

### Patches

Since the Gogs maintainers did not fix the vulnerabilities, we created patches that should fix them. However, we did not extensively test if these patches break functionality somewhere, so we are providing them without any guarantees.

[`Gogs-security-fixes-by-Sonar.patch`](https://gist.githubusercontent.com/paul-gerste-sonarsource/207f5dc79f59bb256a0bfccda4e3e92b/raw/Gogs-security-fixes-by-Sonar.patch)

[  
  
](https://gist.githubusercontent.com/paul-gerste-sonarsource/207f5dc79f59bb256a0bfccda4e3e92b/raw/Gogs-security-fixes-by-Sonar.patch)**How to apply the patches:** To use a version of Gogs with the patches applied, you have to build it from the source. You can find their [extensive documentation here](https://gogs.io/docs/installation/install_from_source). In the "Compile Gogs" step, you will have to apply our patches before running the build command like this:

Copy to clipboard
  
  
  # Clone the repository to the "gogs" subdirectory
  git clone --depth 1 https://github.com/gogs/gogs.git gogs
  
  # Change working directory
  cd gogs
  
  {% mark green %}# Apply the patches
  git apply Gogs-security-fixes-by-Sonar.patch{% mark %}
  
  # Compile the main program, dependencies will be downloaded at this step
  go build -o gogs

Our patches are compatible with the latest version of Gogs available at the time of writing this blog post, which is at commit `5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf` (corresponding to version 0.13.0).

**How the patches work:** Our patches remove the SSH `env` handler because, due to a functional bug, it had no effect anyway. For the two additional Argument Injections, we add end-of-options arguments to separate the user-controlled arguments from the options. For the file delete vulnerability, we add code that verifies the user-controlled path before removing a file.

### Further Recommendations

**Switch to Gitea:** We recommend switching from Gogs to Gitea, which started as a fork of Gogs. It is more actively maintained, and the vulnerabilities we found in Gogs were not present in Gitea when we checked.

### Detecting Attacks

We don't have any data on whether or not malicious actors are exploiting these vulnerabilities in the wild. If you want to check if you have been attacked, we curated a list of indicators. These are non-exhaustive and provided on a best-effort basis.

**CVE-2024-39930 (Argument Injection in the built-in SSH server):** The exploitation of this vulnerability is more challenging to detect on the network level because the attacker payload is sent inside an encrypted SSH connection. On the OS level, you can check for invocations of the `env` command with an argument that starts with either `--split-string` or `-S` (the short form option).

**CVE-2024-39932 (Argument Injection during changes preview):** On the network level, the exploitation of this vulnerability will involve an HTTP request whose path starts with `/<user>/<repo>/_preview/<branch>/--` where `<user>`, `<repo>`, and `<branch>` depend on the repository used for the attack.

We did not find reliable ways to detect attacks for the remaining two vulnerabilities because attackers can easily obfuscate their exploit attempts through multiple indirections.

## Timeline

**Date**| **Action**  
---|---  
2023-04-20| We report all issues via email to the Gogs maintainers, including steps to reproduce, fix recommendations, and a 90-day disclosure deadline.  
2023-04-28| We ping the maintainers again to see if our report was received.  
2023-04-28| The Gogs maintainers confirm the acceptance of our report.  
2023-05-16| We ask the Gogs maintainers for updates.  
2023-05-18| The Gogs maintainers reply that there are no updates yet.  
2023-08-15| We inform the Gogs maintainers that the 90-day disclosure deadline has expired.  
2023-10-02| We ask the Gogs maintainers to open GitHub advisories so we can help contribute patches.  
2023-12-04| We ask the Gogs maintainers for updates.  
2023-12-05| The Gogs maintainers respond they will look into the report.  
2024-02-14| We ask the Gogs maintainers for updates.  
2024-06-03| We inform the Gogs maintainers of the upcoming blog posts.  
2024-07-02| We release this blog post.  
2024-07-04| MITRE publishes the CVE IDs CVE-2024-39930, CVE-2024-39931, CVE-2024-39932, and CVE-2024-39933.  
  
## Summary

This blog post introduced four unpatched vulnerabilities in Gogs, a popular open-source solution for hosting and managing source code. We explained the impact of these vulnerabilities in case attackers exploit them. We then discussed the technical details of one of the four vulnerabilities (CVE-2024-39930) and examined its exploit requirements.

We also covered the options to protect Gogs instances against these unfixed vulnerabilities. To help with that, we provided patches and added recommendations on how to mitigate attacks. Finally, we listed ways to detect attacks as they happen or based on existing logs.

Next week's blog post will conclude our two-part series on Gogs. It will discuss the remaining vulnerabilities in more detail, leaving users time to patch until then.

## Related Blog Posts

  * SourceForge: [Dangerous Import: SourceForge Patches Critical Code Vulnerability](https://www.sonarsource.com/blog/dangerous-import-sourceforge-patches-critical-code-vulnerability/)
  * Jenkins: [Excessive Expansion: Uncovering Critical Security Vulnerabilities in Jenkins](https://www.sonarsource.com/blog/excessive-expansion-uncovering-critical-security-vulnerabilities-in-jenkins/)
  * OneDev: [Securing Developer Tools: OneDev Remote Code Execution](https://www.sonarsource.com/blog/onedev-remote-code-execution/)
  * Visual Studio Code: [Visual Studio Code Security: Deep Dive into Your Favorite Editor](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/)
  * TeamCity: [Source Code at Risk: Critical Code Vulnerability in CI/CD Platform TeamCity](https://www.sonarsource.com/blog/teamcity-vulnerability/)

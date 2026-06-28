---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-06_bash-privileged-mode-vulnerabilities-in-parallels-desktop-and-cdpath-handling-in.md
original_filename: 2023-04-06_bash-privileged-mode-vulnerabilities-in-parallels-desktop-and-cdpath-handling-in.md
title: Bash Privileged-mode Vulnerabilities In Parallels Desktop And CDPATH Handling
  In MacOS
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: ab6bb20bbfe5533c31e15d683b4ce0f0508f8c7bc888fa0c72a66fe33011fabc
text_sha256: bc621db03b9d053e88fb5ab17657eac8437ac2526dd16c2d20c06ca3954b9aab
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Bash Privileged-mode Vulnerabilities In Parallels Desktop And CDPATH Handling In MacOS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-06_bash-privileged-mode-vulnerabilities-in-parallels-desktop-and-cdpath-handling-in.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ab6bb20bbfe5533c31e15d683b4ce0f0508f8c7bc888fa0c72a66fe33011fabc`
- Text SHA256: `bc621db03b9d053e88fb5ab17657eac8437ac2526dd16c2d20c06ca3954b9aab`


## Content

---
title: "Bash Privileged-mode Vulnerabilities In Parallels Desktop And CDPATH Handling In MacOS"
page_title: "Zero Day Initiative — Bash Privileged-Mode Vulnerabilities in Parallels Desktop and CDPATH Handling in MacOS"
url: "https://www.zerodayinitiative.com/blog/2023/4/5/bash-privileged-mode-vulnerabilities-in-parallels-desktop-and-cdpath-handling-in-macos"
final_url: "https://www.zerodayinitiative.com/blog/2023/4/5/bash-privileged-mode-vulnerabilities-in-parallels-desktop-and-cdpath-handling-in-macos"
authors: ["Reno Robert (@renorobertr)"]
programs: ["Parallels"]
bugs: ["MacOS", "Local Privilege Escalation"]
publication_date: "2023-04-06"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1295
---

# Blog

#  Bash Privileged-Mode Vulnerabilities in Parallels Desktop and CDPATH Handling in MacOS 

__ April 06, 2023

__ Reno Robert

In the last few years, we have seen multiple vulnerabilities in Parallels Desktop leading to virtual machine escapes. Interested readers can check our previous blog posts about vulnerabilities across interfaces such as [RDPMC hypercalls](https://www.zerodayinitiative.com/blog/2021/4/26/parallels-desktop-rdpmc-hypercall-interface-and-vulnerabilities), the Parallels [ToolGate,](https://www.zerodayinitiative.com/blog/2021/9/9/analysis-of-a-parallels-desktop-stack-clash-vulnerability-and-variant-hunting-using-binary-ninja) and the [VGA virtual device](https://www.zerodayinitiative.com/blog/2020/5/20/cve-2020-8871-privilege-escalation-in-parallels-desktop-via-vga-device). This post explores another set of issues we received last year - local privilege escalations through setuid root binaries.

Parallels Desktop has a couple of setuid binaries: `prl_update_helper` and `Parallels Service`. Both binaries run with root privileges and both invoke bash scripts to run commands with the privileges of root. For such use cases, bash specifically provides a [privileged mode](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) using the “-p” flag. Parallels Desktop prior to version 18.1.0 does not take advantage of bash privileged mode, nor does it filter untrusted environment variables. This leads to local privilege escalation.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/0919946b-b4ba-4cfb-b706-1b3bdbec3265/1.png)

In the case of Parallels Desktop, the setuid binaries use the setuid() system call to set the real user identifier to that of the effective user identifier. The problem with this implementation is that sensitive environment variables such as BASH_ENV, ENV, SHELLOPTS, BASHOPTS, CDPATH, GLOBIGNORE, and other shell functions are processed by bash. This is because bash is not aware of the setuid or setgid execution and trusts its environment. A local unprivileged user with control over environment variables can exploit this bug to execute code with the privileges of root.

**The Bash Privileged Mode**

Bash shell drops privileges when started with the effective user identifier not equal to that of the real user identifier. The effective user identifier is reset by setting it to the value of the real user identifier. The same is also applicable for group identifiers. In privileged mode, bash does not drop the effective privileges and ignores sensitive variables and shell functions from the environment. Here’s the relevant source code in bash that can be found in `shell.c` file:

The functions of interest here are `uidget` and `disable_priv_mode`. The `uidget` function sets `running_setuid` if bash is launched from a `setuid/setgid` process. Later in the code, if privileged mode is not specified, the `setuid` and `setgid` calls are used to drop privileges to that of the real identifiers:

Note that, since the Bourne shell `sh` is linked to bash in macOS, the Apple bash code for invoking `disable_priv_mode` is slightly different from that of the upstream version. Interested readers can search for the `__APPLE__` macro to narrow down changes made to the upstream version of bash by Apple.

The other functions of interest in the bash startup code are `run_startup_files` and `shell_initialize`, as they handle information passed through the untrusted environment variables. When privileged mode is not specified, these functions provide at least a couple of generic ways to exploit the vulnerability. To begin, the BASH_ENV is an environment variable specifying a path to a shell script that will be executed by bash during a non-interactive start-up. One can set up an arbitrary startup script to be executed by bash running without privileged mode. Shown below is the code snippet of `run_startup_files` in `shell.c`:

A second approach is by using bash [shell functions](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html). When commands are executed in bash without an absolute path, it is possible to hijack those commands by exporting shell functions having the same name as that of the command being executed. This is possible even when the PATH environment variable is set to trusted paths. The corresponding source code can be found across `shell.c` and `variables.c` files:

Knowing this, let’s take a look at some of the privileged mode bugs in Parallels Desktop and their exploitation. 

**CVE-2023-27322 - Local Privilege Escalation Through Parallels Service**

This bug was submitted by Grisha Levit and is also identified as [ZDI-23-216](https://www.zerodayinitiative.com/advisories/ZDI-23-216/). `Parallels Service` forks a child process and executes an embedded script using a non-interactive bash shell invoked as `/bin/bash -s`. The parent process writes the embedded script through a pipe to the child process running the bash shell. Before invoking the bash shell, Parallels Service calls `setuid(0)` to set the real user identifier to the effective user identifier (root). Here is the relevant code snippet from the executable in Parallels Desktop version 17.1.4:

The `execv` function is a wrapper around `execve`, which fetches the environment using [_NSGetEnviron()](https://www.gnu.org/software/gnulib/manual/html_node/environ.html) and passes it to `execve`. Therefore, the bash shell spawned as a child process has access to all the environment variables set by the user who launched `Parallels Service`, who may be an unprivileged user. Interestingly, the execution of an embedded shell script turned out to be not immediately vulnerable. This is because `Parallels Service` also has the `setgid` bit set and there is no corresponding call `setgid(getegid())` as there was for the uid. Because of this, the real group identifier is not equal to that of the effective group identifier when bash is invoked. In such cases, bash identifies this as `setgid` execution, drops group privileges, and does not trust the environment. However, any further subshell launched from this bash shell will also have all the environment variables as well as the privileges of the parent shell, which is running as root and has the group privileges set after the call to `disable_priv_mode`. Considering this, the next interesting target is the `watchdog` script invoked from the embedded script as seen below:

The `watchdog` script uses /bin/bash as [shebang](https://en.wikipedia.org/wiki/Shebang_\(Unix\)) and does not use privileged mode:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1dab36f2-819f-4ec8-b9c2-655e7b3b4e80/2.png)

In this instance, bash trusts the environment. Because of this, the watchdog script can be exploited to gain root either by using the `BASH_ENV` environment variable or by exporting shell functions. Here is an example of exploitation using `BASH_ENV`:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1378f429-8739-4020-88f2-11777f2062b0/3.png)

To exploit using shell functions, we must identify a command to hijack. The watchdog script uses the `echo` command for printing some debug messages:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/ad646b65-a9e3-4228-976d-401e2a268a46/4.png)

A shell function with the same name can be exported such that the malicious function is executed instead of the expected `echo` command. Note that exporting functions is a feature of bash. We must therefore use the bash shell to export the target function instead of using the default zsh shell in macOS.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/cd2e1341-b938-44fe-a813-1d9d9a4bc988/5.png)

This issue was fixed in Parallels Desktop 18.1.0 by adding the “-p” flag, indicating privileged mode, to the shebang interpreter directive:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1be189b1-8b30-43dd-a67f-0fbcfc0eb607/6.png)

**CVE-2023-27324 and CVE-2023-27325 - Local Privilege Escalation Through Parallels Updater**

The next two bugs were found in the Parallels Updater `prl_update_helper` binary. These bugs were submitted by the researcher known as kn32 and are also identified as [ZDI-23-218](https://www.zerodayinitiative.com/advisories/ZDI-23-218/) and [ZDI-23-219](https://www.zerodayinitiative.com/advisories/ZDI-23-219/). In the case of CVE-2023-27324, the `prl_update_helper` binary invokes a bash script named `inittool` without setting privileged mode:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/08f38ad8-d6f6-4ee0-bfdc-da1108c0f9d1/7.png)

Before invoking the `inittool` script, the real user identifier is set to that of the effective user identifier, which is root. This means bash will run as root and will trust its execution environment, which can lead to local privilege escalation. 

This vulnerability can be exploited by using the `BASH_ENV` environment variable or by exporting the shell function for the `dirname` command.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/a664e84f-4338-4705-8e7c-598c2dbca825/8.png)

The next bug (CVE-2023-27325) in the Parallels Updater affects the `inittool2` executable invoked from the `inittool` script. Like the `Parallels Service`, `inittool2` forks a child process and executes an embedded script using a non-interactive bash shell invoked as `/bin/bash -s`. Exploitation is similar to that of CVE-2023-27324. In this case, the `rm` command can be hijacked to execute arbitrary code as root. Below is the embedded script from Parallels Desktop version 17.1.4:

Both CVE-2023-27324 and CVE-2023-27325 were fixed in Parallels Desktop 18.1.0 by clearing the environment during the call to [posix_spawn](https://pubs.opengroup.org/onlinepubs/007904875/functions/posix_spawn.html). Instead of passing the `environ` array to the child process, the `envp` argument is now provided with a pointer to a NULL array during the call to `posix_spawn`. Below is the patch diff between 17.1.4 and 18.1.0:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/007125fd-81c0-4dfa-b60f-25de5f99cee4/Fig1.png)

_Figure 1 - Patch diff of prl_update_helper executable_

Additionally, the privileged mode flag “-p” is also added to the shebang interpreter directive of the `inittool` script as well as the embedded script within `inittool2`. Note that the shebang of the embedded script is ignored since it is explicitly run using the bash interpreter. 

**CDPATH Handling in MacOS**

During the analysis of these submissions, we also observed some differences in the way Apple bash handles “privileged mode” as compared to the upstream bash. Apple’s bash in macOS 13.0.1 is based on GNU Bash 3.2: 

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/fad996b8-d870-4ec6-9241-0a95f8c305c7/9.png)

The upstream bash in privileged mode ignores many variables such as SHELLOPTS, BASHOPTS, CDPATH, and GLOBIGNORE as mentioned below:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/3098e06c-a7ec-4cb2-81c6-1dd19b330638/Screen+Shot+2023-04-03+at+12.16.30+PM.png)

Based on the [CHANGES](https://github.com/bminor/bash/blob/fb0092fb0e7bb3121d3b18881f72177bcb765491/CHANGES), here is a timeline of various changes related to privileged mode. Parsing of SHELLOPTS was ignored starting from bash-2.02-alpha1 and therefore ignored in version 3.2 too.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/adfdd7de-1b69-4c87-b2b6-4636be40a485/Screen+Shot+2023-04-03+at+12.10.47+PM.png)

BASHOPTS was introduced at a later stage in bash-4.1-alpha and therefore not applicable to version 3.2.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/4917db97-7d32-4a6d-bace-734afe4bc1c0/Screen+Shot+2023-04-03+at+12.11.33+PM.png)

The CDPATH and GLOBIGNORE variables were ignored only since bash-4.0-beta and therefore still get processed in Apple’s bash, which is based on version 3.2.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/c35bcf28-96b9-4778-854f-c4e075e16e7f/Screen+Shot+2023-04-03+at+12.12.17+PM.png)

The CDPATH environment variable can be set to a colon-separated list of directories, which can then be used as a directory root by the built-in “cd” command instead of the current working directory (CWD). In the case of Apple’s bash, if a bash script executed through a setuid wrapper uses “cd [Absolute Path to Trusted Directory]” to change the CWD and further uses “cd subdirectory” to change the CWD, the later cd command with the relative path can be hijacked to a location controlled by an attacker by setting the CDPATH variable. Consider the sample code below:

Here is the outcome as tested in Ubuntu:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/d4041e3c-1f26-4115-aa85-4415e1fa12bc/10.png)

It is seen that the CDPATH environment variable is ignored in bash privileged mode (`-p`). While repeating the same in macOS, it is honored.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/2fd5d05c-9c68-40e8-ba6f-e14c52d0a3f0/11.png)

This can become problematic when a script is written assuming bash privileged mode behavior in macOS to be the same as that of the upstream version. You may note the duplicated `/tmp/secure` line. This is not a typo. It comes from the POSIX [standard](https://github.com/apple-oss-distributions/bash/blob/main/bash-3.2/builtins/cd.def#L242). If CDPATH is used for a directory change, the new directory path is echoed to stdout, which is the first line `/tmp/secure`. The second line comes from the `pwd` command. 

Here is the comparison of `builtins/cd.def` which handles CDPATH in Apple bash versus the upstream version:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/dc6d12d5-0a61-4652-ab2d-d96cb385d665/Fig2.png)

_Figure 2 - Missing privileged mode check when handling CDPATH_

Similarly, differences in GLOBIGNORE handling can be seen by diffing `variables.c` source file:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/99b7b679-5c52-4bce-8137-479677fa0354/Fig3.png)

_Figure 3 - Missing privileged mode check when handling GLOBIGNORE_

Since macOS Catalina, zsh is used as the default shell. The official announcement for the same can be found [here](https://support.apple.com/en-gb/HT208050). Bash is deprecated on macOS and likely exists only for backward compatibility. For any bash scripts executed through a setuid wrapper, one must ensure privileged mode “-p” is enabled. In addition to that, beware of the differences in privileged mode between Apple bash and the upstream version. This is specifically noticed in the handling of the CDPATH and GLOBIGNORE environment variables.

**Conclusion**

Parallels Desktop is a popular target for researchers. We’ve already published seven advisories in the product in 2023 to go along with the 10 we published in 2022. With Parallels Desktop being one of the major virtualization solutions used in macOS, it’s understandable why it can be an enticing target for threat actors. My research into Parallels continues, and I’ll blog about any significant findings in the future. Of course, if you find similar vulnerabilities, we’d be interested in seeing those as well.

Until then, you can follow me [@renorobertr](https://www.twitter.com/renorobertr) and follow the team on [Twitter](https://www.twitter.com/thezdi), [Mastodon](https://infosec.exchange/@thezdi), [LinkedIn](https://www.linkedin.com/company/zerodayinitiative), or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Parallels](/blog/tag/Parallels)
  * [Research](/blog/tag/Research)
  * [Bash](/blog/tag/Bash)

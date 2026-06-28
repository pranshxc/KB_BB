---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-28_empowering-weak-primitives-file-truncation-to-code-execution-with-git.md
original_filename: 2023-02-28_empowering-weak-primitives-file-truncation-to-code-execution-with-git.md
title: 'Empowering weak primitives: file truncation to code execution with Git'
category: documents
detected_topics:
- command-injection
- supply-chain
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- api-security
language: en
raw_sha256: 2f2fd6893c1b137ac92c941fa9613ebced58746da3e40e52e575c4861b0cd803
text_sha256: 257406fa9eab74520dffe38ee3a8eef529f2ee94efe20df0c084adbee0b0c4a3
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Empowering weak primitives: file truncation to code execution with Git

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-28_empowering-weak-primitives-file-truncation-to-code-execution-with-git.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `2f2fd6893c1b137ac92c941fa9613ebced58746da3e40e52e575c4861b0cd803`
- Text SHA256: `257406fa9eab74520dffe38ee3a8eef529f2ee94efe20df0c084adbee0b0c4a3`


## Content

---
title: "Empowering weak primitives: file truncation to code execution with Git"
page_title: "Empowering weak primitives: file truncation to code execution with Git | Sonar"
url: "https://www.sonarsource.com/blog/empowering-weak-primitives-file-truncation-to-code-execution-with-git/"
final_url: "https://www.sonarsource.com/blog/empowering-weak-primitives-file-truncation-to-code-execution-with-git/"
authors: ["Thomas Chauchefoin (@swapgs)"]
bugs: ["Argument injection", "RCE"]
publication_date: "2023-02-28"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1454
---

## TL;DR overview

  * A file truncation primitive in Git can be chained with other weaknesses to achieve arbitrary code execution, demonstrating how low-severity primitives become high-impact when combined.
  * The attack exploits Git's handling of file operations during certain commands, enabling attackers to overwrite or truncate security-relevant files on the host system.
  * This research highlights the importance of threat modeling primitive operations—not just end-to-end exploits—when auditing complex, widely trusted tools like version control systems.
  * The vulnerability underscores the need for static analysis of security-critical code paths, including those in developer toolchain software.

During recent security research, we came up with a fun "trick" that we later shared in a Capture the Flag challenge for the Hack.lu CTF and our Code Security Advent Calendar. We received good feedback and wanted to share the details with a broader audience. 

Let's say that you discovered a code vulnerability that allows you to truncate arbitrary files. It sounds like a pretty weak exploitation primitive, but if you are dealing with an application that involves operations on a Git repository under your control, you're in luck! 

## The vulnerable snippet

For our example, let's use the code snippet of [Day 16 of this year's Code Security Advent Calendar](https://www.sonarsource.com/knowledge/code-challenges/advent-calendar-2022/). It implements a service that allows cloning an arbitrary Git repository and later running `git blame` on specific files and lines.

**challenge.py**

Copy to clipboard
  
  
  def _git(cmd, args, cwd='/'):
  
     proc = run(['git', cmd, *args],
  
                stdout=PIPE,
  
                stderr=DEVNULL,
  
                cwd=cwd,
  
                timeout=5)
  
     return proc.stdout.decode().strip()
  
  @app.route('/blame', methods=['POST'])
  
  def blame():
  
     url = request.form.get('url',
  
                            'https://github.com/package-url/purl-spec.git')
  
     what = request.form.getlist('what[]')
  
     with TemporaryDirectory() as local:
  
         if not url.startswith(('https://', 'http://')):
  
             return make_response('Invalid url!', 403)
  
         _git('clone', ['--', url, local])
  
         res = []
  
         for i in what:
  
             file, lines = i.split(':')
  
             res.append(_git('blame', ['-L', lines, file], local))
  
         return make_response('\n'.join(res), 200)

This code suffers from an argument injection vulnerability when crafting the command line for `git blame`. Argument injections are widespread code vulnerabilities identified by our static analysis technology; you can find a scan report of the above snippet on [SonarQube Cloud](https://sonarcloud.io/project/security_hotspots?id=SonarSourceResearch_2022_calendar_16&hotspots=AYTElMvtSrpHxVfO0aem):

![Image of common arguments leading to unwanted behavior. ](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/edab3a68-8510-4d8a-9098-846528f4ea3d/Screenshot%202023-02-24%20at%2017.16.17.png)

Exploiting argument injection vulnerabilities depends heavily on the features offered by the invoked binary. 

For instance, if a hypothetic program supports the option `--output=foo` that writes the program output to the file `foo`, attackers who can inject this argument could create new files or overwrite existing ones. The attacker's goal is usually to gain the ability to execute arbitrary code on the server, and such primitives are very powerful but also quite rare.

## Finding an interesting argument

Let's get back to our code snippet, where we can add new arguments to the `git blame` invocation. 

After looking at the manual of `git-blame`, we couldn't find any "interesting" option to execute arbitrary code. Most arguments alter the behavior of the blame process or the way it renders its output. Most importantly, the manual does not document the presence of the option `--output`, which is usually present on other `git` sub-commands. 

It is then surprising to see this behavior when running `git blame --output=foo`; notice the presence of a new file named `foo`:

Copy to clipboard
  
  
  $ git blame --output=foo
  usage: git blame [<options>] [<rev-opts>] [<rev>] [--] <file>
  
  
  <rev-opts> are documented in git-rev-list(1)
  
  
  --incremental  show blame entries as we find them, incrementally
  [...]
  $ ls -alh
  total 0
  drwx------  4 thomas  staff  128B Dec 29 14:43 ./
  drwx------@ 191 thomas  staff  6.0K Dec 29 14:43 ../
  drwxr-xr-x  9 thomas  staff  288B Dec 29 14:43 .git/
  -rw-r--r--  1 thomas  staff  0B Dec 29 14:43 foo
  

Although the command failed, an empty file named `foo` was created. If a file with the same name already exists, the destination file is truncated!

Copy to clipboard
  
  
  $ date > foo
  $ cat foo
  Thu Dec 29 15:42:56 CET 2022
  $ git blame --output=foo
  usage: git blame [<options>] [<rev-opts>] [<rev>] [--] <file>
  
  
  <rev-opts> are documented in git-rev-list(1)
  
  
  --incremental  show blame entries as we find them, incrementally
  [...]
  $ ls -alh
  total 0
  drwx------  4 thomas  staff  128B Dec 29 14:43 ./
  drwx------@ 191 thomas  staff  6.0K Dec 29 14:47 ../
  drwxr-xr-x  9 thomas  staff  288B Dec 29 14:43 .git/
  -rw-r--r--  1 thomas  staff  0B Dec 29 14:48 foo

This option provides attackers with an arbitrary file truncation primitive. The command `git-blame` supports `--output` because its implementation uses other sub-commands that _do_ support `--output`: command-line arguments are parsed several times by these components.

## Putting the pieces together

As we demonstrated in [Securing Developer Tools: Git Integrations](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/), control over the Git options of a local repository is dangerous: several configuration directives allow specifying external commands to change Git's behavior. For instance, `core.fsmonitor` can point to a third-party program to replace Git's built-in filesystem monitor. This process happens during most operations, including `git blame`. 

We could leverage this technique if we find a way to force Git operations to ignore the local repository and use one in our control instead. As you may have already guessed, the file truncation primitive was proven to be useful here. 

We can trick Git into loading a configuration from an unintended location by corrupting a critical file like `.git/HEAD`. In such cases, Git starts looking for repositories in the current folder, which the attacker fully controls as it is the work tree with all the files of the cloned remote repository.

## Solving the challenge

To solve the challenge, we created [a Git repository](https://github.com/SonarSourceResearch/csac2022-git-blame) with the following structure:

  * `objects/`, `refs/`, `worktree/`: empty folders to comply with the expected structure of a Git repository
  * `HEAD`: non-empty file to fake a valid reference
  * `config`: malicious configuration based on what we described in [Securing Developer Tools: Git Integrations](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/) and [Justin Steven's advisory](https://github.com/justinsteven/advisories/blob/main/2022_git_buried_bare_repos_and_fsmonitor_various_abuses.md). Most importantly, it should contain:
  * `bare = false`: don't mark the current directory as bare 
  * `worktree = worktree`: the working tree directory under which checked-out are files
  * `fsmonitor = $(id>/pwned)#`: the custom filesystem monitor daemon to start at the next Git invocation; this is the attacker's payload

When the repository is imported for the first time, nothing happens because the local Git repository stored in `.git` is constructed during the `clone` operation: this repository is valid and ignores the bare repository we planted. 

Then, the argument injection is triggered to truncate `.git/HEAD`, corrupting the once-valid local repository. By invoking `git blame` a second time, `git` now uses the malicious bare repository and calls the custom filesystem monitor, effectively executing the attacker's payload. 

## Closing words

As we shared with our [series](https://www.sonarsource.com/blog/checkmk-rce-chain-1/) [of](https://www.sonarsource.com/blog/checkmk-rce-chain-2/) [publications](https://www.sonarsource.com/blog/checkmk-rce-chain-3/) on vulnerabilities in the IT monitoring software Checkmk, seemingly minor vulnerabilities can hide a critical impact. Our [Code Quality approach](https://www.sonarsource.com/solutions/clean-code/) helps you identify these security liabilities before they are deployed to production. 

We hope you enjoyed this article and learned something about argument injection bugs; we sure had fun! 

## Related Blog Posts

  * [Code Security Advent Calendar 2022](https://www.sonarsource.com/blog/code-security-advent-calendar-2022/)
  * [Securing Developer Tools: Git Integrations](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-2/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-3/)

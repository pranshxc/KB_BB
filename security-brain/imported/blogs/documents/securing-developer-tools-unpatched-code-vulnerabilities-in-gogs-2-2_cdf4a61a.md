---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-09_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-22.md
original_filename: 2024-07-09_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-22.md
title: 'Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (2/2)'
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
- mobile-security
language: en
raw_sha256: cdf4a61af2604e7e705fe9609c06347dca4d9de02e22a2239211b6f445b7d30f
text_sha256: 14203f4a1e6750f40910f1d1728b617e59eec87f2a028b7f96f71f71ea328fe9
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (2/2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-09_securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-22.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `cdf4a61af2604e7e705fe9609c06347dca4d9de02e22a2239211b6f445b7d30f`
- Text SHA256: `14203f4a1e6750f40910f1d1728b617e59eec87f2a028b7f96f71f71ea328fe9`


## Content

---
title: "Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (2/2)"
page_title: "Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (2/2) | Sonar"
url: "https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-2/"
final_url: "https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-2/"
authors: ["Thomas Chauchefoin (@swapgs)", "Paul Gerste"]
programs: ["Gogs"]
bugs: ["Path traversal", "Arbitrary file delete", "Argument injection", "Security code review"]
publication_date: "2024-07-09"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 179
---

## TL;DR overview

  * Part 2 of Sonar's Gogs research details additional unpatched vulnerabilities including remote code execution paths accessible to low-privileged or unauthenticated attackers via Git-related features in the Gogs web interface.
  * The continued unpatched status highlights the maintainer sustainability challenge in open source security: Gogs is widely used but has limited active maintainership, leaving disclosed CVEs open longer than responsible disclosure standards recommend.
  * The vulnerabilities compound the findings from Part 1: multiple overlapping attack surfaces in Gogs mean that even partial mitigations may not fully reduce risk, as alternative exploit paths remain available.
  * Organizations dependent on Gogs are advised to treat these findings as blocking and migrate to a maintained alternative (Gitea, GitLab CE, or Forgejo) rather than waiting for patches from an under-resourced project.

In [last week's blog post](https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-1/), we examined an unfixed vulnerability in Gogs, an open-source solution for self-hosting source code. The flaw is one of four vulnerabilities we discovered and reported to the maintainers. These issues allow attackers to compromise vulnerable instances, enabling them to steal source code, plant code backdoors, wipe all code, and more.

Gogs is a popular open-source project with over 44,000 stars on GitHub and 90 million downloads of its Docker image. We have previously investigated the security of other developer tools, so it was a natural fit to include Gogs in this research series and give its code base a look.

This blog post will first cover the impact of the vulnerabilities we found and reported. We will then discuss the technical details of two of those vulnerabilities. Finally, we will provide recommendations and patches for users to help them protect their Gogs installations.

## Impact

We found the following vulnerabilities and reported them to the maintainers of Gogs:

  1. Argument Injection in the built-in SSH server (CVE-2024-39930, CVSS 9.9 Critical)
  2. Deletion of internal files (CVE-2024-39931, CVSS 9.9 Critical)
  3. Argument Injection during changes preview (CVE-2024-39932, CVSS 9.9 Critical)
  4. Argument Injection when tagging new releases (CVE-2024-39933, CVSS 7.7 High)

Unfortunately, the maintainers did not implement fixes and stopped communicating with us at some point after initially accepting our report. All four vulnerabilities are still present in the latest release of Gogs (0.13.0) and the latest commit in the Gogs repository (`5bdf91e` at the time of writing). **To protect yourself, read our recommendation section below.**

Attackers can execute arbitrary commands on the Gogs server using the first three vulnerabilities. The commands will run under the same use that Gogs runs as (configured via `RUN_USER`). This allows them to read all source code on the instance, modify any code, delete all code, or attack internal hosts reachable from the Gogs server. Vulnerability 4 allows attackers to read arbitrary files from the Gogs server. These files include the source code stored on the Gogs instance and configuration secrets, likely allowing the attacker to impersonate other users and gain more privileges.

All four vulnerabilities require an attacker to be authenticated. You can find more details about the exploitability of CVE-2024-39930 in our previous blog post and details on CVE-2024-39931 and CVE-2024-39932 below. A quick [Shodan search](https://www.shodan.io/search?query=http.component%3A%22Gogs%22) now lists around open 7500 Gogs instances, about 200 more than last week:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c3d0c038-e25c-453b-bc66-486f8047a6d8/gogs-shodan-report-2.png)

We did not confirm how many of these are exploitable, nor do we have any data on whether or not malicious actors are exploiting these vulnerabilities in the wild.

## Technical Details

Last week, we looked at the details of [CVE-2024-39930](https://nvd.nist.gov/vuln/detail/CVE-2024-39930), an argument injection in Gogs' built-in SSH server. That vulnerability has a severe impact (Remote Code Execution), but Gogs' default configuration is not vulnerable. Today, we will dive into the details of [CVE-2024-39931](https://nvd.nist.gov/vuln/detail/CVE-2024-39931) and [CVE-2024-39932](https://nvd.nist.gov/vuln/detail/CVE-2024-39932), two of the remaining vulnerabilities we found and reported. They can be exploited by authenticated attackers in Gogs’ default configuration.

### Deletion of Internal Files (CVE-2024-39931)

We will start with CVE-2024-39931, a path traversal vulnerability that allows attackers to delete arbitrary files on the system. The vulnerability fittingly exists in the file deletion feature of the web UI. To delete a file from a repo, a user clicks the delete button and is presented with a confirmation page:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/b5c1afb5-c88a-48ea-ae0a-d26c609581f7/gogs-file-deletion.png)

When confirming the deletion, the frontend calls the API handler at `/user/repository/_delete/<filepath>`:

[internal/cmd/web.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/cmd/web.go#L554-L555):

Copy to clipboard
  
  
  m.Group("", func() {
    // [...]  
    m.Combo("/_delete/*").Get(repo.DeleteFile).
        Post(bindIgnErr(form.DeleteRepoFile{}), {% mark yellow %}repo.DeleteFilePost{% mark %})
    // [...]
  })

This handler is just a wrapper around `Repository.DeleteRepoFile`:

[internal/route/repo/editor.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/route/repo/editor.go#L332-L391):

Copy to clipboard
  
  
  func DeleteFilePost(c *context.Context, f form.DeleteRepoFile) {
  // [...]
  c.Repo.TreePath = pathutil.Clean(c.Repo.TreePath)
  c.Data["TreePath"] = c.Repo.TreePath
  // [...]
  if err := c.Repo.Repository.DeleteRepoFile(c.User, db.DeleteRepoFileOptions{
  LastCommitID: c.Repo.CommitID,
  OldBranch:    oldBranchName,
  NewBranch:    branchName,
  {% mark yellow %}TreePath:     c.Repo.TreePath{% mark %},
  Message:      message,
  }); 
    // [...]
  }

To effectively remove a file from a project, a temporary repository with a work tree is created from the project's bare repository. The file is removed, tracked in a commit, and pushed to the original bare repository:

[internal/database/repo_editor.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/database/repo_editor.go#L285-L341):

Copy to clipboard
  
  
  func (repo *Repository) DeleteRepoFile(doer *User, opts DeleteRepoFileOptions) (err error) {
  // [...]
  localPath := repo.LocalCopyPath()
  if err = os.Remove(path.Join(localPath, {% mark yellow %}opts.TreePath{% mark %})); err != nil {
  return fmt.Errorf("remove file %q: %v", opts.TreePath, err)
  }
  // [...]
  err = git.CreateCommit(
  localPath,
  &git.Signature{
  Name:  doer.DisplayName(),
  Email: doer.Email,
  When:  time.Now(),
  },
  opts.Message,
  )
  // [...]
  }

As we can see, `opts.TreePath` is not validated and can point to any location inside the repository. To understand how this file deletion can lead to arbitrary code execution, we must understand how Gogs and many other source code hosting solutions store Git data on the server.

Usually, when using Git, you have a folder structure like this:

Copy to clipboard
  
  
  repo/
  ├── .git/
  │   ├── HEAD
  │   ├── config
  │   └── …
  ├── go.mod
  ├── main.go
  └── …

The `.git` folder contains all the Git-related metadata. The rest of the files (outside the `.git` folder) are the actual contents of the repo, also called the "working tree". This representation is helpful for working on files directly, but it has some storage overhead: the `.git` folder contains all the data that exists in the working tree!

But there's a different representation: the "bare repo". It is just the content from within the `.git` folder but without the working tree:

Copy to clipboard
  
  
  repo/
  ├── HEAD
  ├── config
  └── …

This is what Gogs and many others use to store a repo on the server, as it saves disk space and is usually enough for the Git operations the server needs to perform. However, to delete a file from a repo, Gogs creates a local checkout of the bare repo with the standard, non-bare structure. But how does Git know if a repo is bare or not?

The answer is quite simple: Git will look for a `.git` directory in the current working directory. If it finds one, it will examine its files to see if it contains valid repository metadata. If it doesn't find a `.git` directory, it checks if the current working directory is a bare repo by examining the included files. If the current working directory is not a bare repo, it starts over in the parent directory of the current working directory, and so on. The following flow chart visualizes this simplified decision process:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6f6ca7b2-37f6-4044-9a4e-881d3ce4b88f/Git%20repo%20detection%20flow.png)

One of the metadata files that Git checks is `HEAD`. This file should contain the name of a valid reference that is the repo's current head. If there is no such file, or if it does not contain a valid reference, then Git assumes the directory to be invalid and moves on.

So what happens when an attacker uses the arbitrary file delete to remove `.git/HEAD` from the local checkout of a repo? The next time a git command is executed in that repo, the `.git` folder is no longer considered valid. So, as the next step, Git will check if the root directory of the repo is a valid bare repo.

Since users can fully control the folders and files within a repo, the attacker could prepare it to contain all metadata files that make Git think it's a bare repo. By achieving this, they can now control all the git configurations via the `config` file in the repo. They can for example use the [well-known `core.fsmonitor` setting](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/#root-cause-git-local-configuration) to specify a command executed for almost all the Git subcommands.

With this, attackers can execute arbitrary commands using just the file deletion primitive that CVE-2024-39931 gives them. However, this not only works with file deletions but also with [file _truncations_](https://www.sonarsource.com/blog/empowering-weak-primitives-file-truncation-to-code-execution-with-git/). Let's look at how attackers could also achieve code execution with CVE-2024-39932, an Argument Injection vulnerability in Gogs' preview functionality.

### Argument Injection During Changes Preview (CVE-2024-39932)

When changing a file from the web UI, Gogs allows the user to see a preview of the changes. This is implemented in the `/_preview/*` API handler:

[internal/cmd/web.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/cmd/web.go#L553):

Copy to clipboard
  
  
  m.Group("", func() {
      // [...]
      m.Post("/_preview/*", bindIgnErr(form.EditPreviewDiff{}), {% mark yellow %}repo.DiffPreviewPost{% mark %})
      // [...]
      c.Data["PageIsViewFiles"] = true
    })
  }, reqSignIn, context.RepoAssignment())

First, `DiffPreviewPost` gets a reference to the modified file in the Git repository and calls `Repository.GetDiffPreview`:

[internal/route/repo/editor.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/route/repo/editor.go#L294-L319):

Copy to clipboard
  
  
  func DiffPreviewPost(c *context.Context, f form.EditPreviewDiff) {
  {% mark yellow %}treePath := c.Repo.TreePath{% mark %}
  // [...]
  diff, err := c.Repo.Repository.GetDiffPreview(c.Repo.BranchName, {% mark yellow %}treePath{% mark %}, f.Content)
  // [...]
  }

After cloning the current repository to a temporary folder and discarding any changes, the new changes are applied to the file pointed by `treePath`. Then, `git diff` is called with `treePath` as an argument to compute the differences:

[internal/database/repo_editor.go](https://github.com/gogs/gogs/blob/5bdf91e73c7733d92e80f6ea9e3fbba60490c9cf/internal/database/repo_editor.go#L222-L267):

Copy to clipboard
  
  
  func (repo *Repository) GetDiffPreview(branch, treePath, content string) (diff *gitutil.Diff, err error) {
  // [...]
  localPath := repo.LocalCopyPath()
  // [...]
  cmd := exec.Command("git", "diff", {% mark yellow %}treePath{% mark %})
  cmd.Dir = localPath
  cmd.Stderr = os.Stderr
  // [...]
  }

Because attackers can control the `treePath` variable, the name of the file being modified, they can add extra arguments to the `git diff` invocation. Since the goal is to truncate a file, attackers can use the `--output=some/file/path` option.

By changing the positional argument to an option, the `git diff` command is missing the positional argument, causing it to error. However, the `--output` option is processed before bailing out, and the specified file is opened with the `O_TRUNC` flag, which truncates it to an empty file.

By truncating the `.git/HEAD` file of the repo, Git will consider the `.git` folder to be broken and use the repo as a bare repo instead. The attacker can then take the same steps as above to turn the control over this bare repo into code execution.

As we have seen, even vulnerabilities that seem less impactful, like arbitrary file deletions, can be turned into more impactful ones by abusing features and quirks of the tools used around them. This also shows once again that Git is not made to be used on untrusted inputs and that it takes a significant amount of work to secure its use in such scenarios.

## Recommendations: How to Protect Yourself

Unfortunately, the maintainers of Gogs stopped responding to our disclosure at some point after initially accepting our report. Therefore, all four of our reported vulnerabilities are unpatched in the latest version of Gogs. To help users protect themselves, we have curated a list of mitigations and additional recommendations.

### Immediate Mitigations

**Disable the built-in SSH server:** To prevent the exploitation of the Argument Injection vulnerability discussed in our previous blog post (CVE-2024-39930), we recommend turning off the built-in SSH server in your `app.ini`:

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

Since the Gogs maintainers did not fix the vulnerabilities, we created patches that should fix them. However, we have not extensively tested whether these patches break functionality somewhere, so we are providing them without any guarantees.

[Gogs-security-fixes-by-Sonar.patch  
  
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
2024-07-02| We release our first blog post.  
2024-07-04| MITRE publishes CVE-2024-39930, CVE-2024-39931, CVE-2024-39932, and CVE-2024-39933.  
2024-07-09| We release our second blog post.  
  
## Summary

This concludes our two-part series on Gogs, in which we discussed four critical vulnerabilities we found in its code base. We reported these vulnerabilities to the maintainers of Gogs, but unfortunately, they never implemented fixes based on our recommendations. Therefore, the latest version of Gogs is still vulnerable.

We released details about the vulnerabilities to help affected users protect themselves, along with patches and recommendations on hardening vulnerable instances. If you are running a Gogs instance, we urge you to apply our patches and check if you have been exploited.

The code vulnerabilities we found show once again that Git is not designed for use on untrusted user inputs and that it takes significant work to make its use secure in such scenarios. We also observe that Argument Injections are still more common than their sibling, Command Injections.

## Related Blog Posts

  * Part 1: [Securing Developer Tools: Unpatched Code Vulnerabilities in Gogs (1/2)](https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-1/)
  * [Empowering weak primitives: file truncation to code execution with Git ](https://www.sonarsource.com/blog/empowering-weak-primitives-file-truncation-to-code-execution-with-git/)
  * [Dangerous Import: SourceForge Patches Critical Code Vulnerability](https://www.sonarsource.com/blog/dangerous-import-sourceforge-patches-critical-code-vulnerability/)
  * [Excessive Expansion: Uncovering Critical Security Vulnerabilities in Jenkins](https://www.sonarsource.com/blog/excessive-expansion-uncovering-critical-security-vulnerabilities-in-jenkins/)
  * [Source Code at Risk: Critical Code Vulnerability in CI/CD Platform TeamCity](https://www.sonarsource.com/blog/teamcity-vulnerability/)

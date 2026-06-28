---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-14_visual-studio-code-security-markdown-vulnerabilities-in-third-party-extensions-2.md
original_filename: 2023-11-14_visual-studio-code-security-markdown-vulnerabilities-in-third-party-extensions-2.md
title: 'Visual Studio Code Security: Markdown Vulnerabilities in Third-Party Extensions
  (2/3)'
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 890320fd00dedbe316e1619bc7d68650db79536bca1024255fea3759b37652d4
text_sha256: 1a46355ad0fdafd8789967d848c35fe07672cce21c94b4fe3c89edbdce235ac0
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Visual Studio Code Security: Markdown Vulnerabilities in Third-Party Extensions (2/3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-14_visual-studio-code-security-markdown-vulnerabilities-in-third-party-extensions-2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `890320fd00dedbe316e1619bc7d68650db79536bca1024255fea3759b37652d4`
- Text SHA256: `1a46355ad0fdafd8789967d848c35fe07672cce21c94b4fe3c89edbdce235ac0`


## Content

---
title: "Visual Studio Code Security: Markdown Vulnerabilities in Third-Party Extensions (2/3)"
page_title: "Visual Studio Code Security: Markdown Vulnerabilities in Third-Party Extensions (2/3) | Sonar"
url: "https://www.sonarsource.com/blog/vscode-security-markdown-vulnerabilities-in-extensions/"
final_url: "https://www.sonarsource.com/blog/vscode-security-markdown-vulnerabilities-in-extensions/"
authors: ["Thomas Chauchefoin (@swapgs)", "Paul Gerste"]
programs: ["GitKraken", "Microsoft"]
bugs: ["RCE", "Arbitrary Code Execution", "Markdown injection", "Security code review"]
bounty: "100"
publication_date: "2023-11-14"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 680
---

## TL;DR overview

  * Sonar discovered security vulnerabilities in VS Code Markdown extensions that allow attackers to inject malicious code through crafted Markdown content rendered in the editor.
  * The vulnerabilities exploit the way Markdown extensions render HTML within VS Code's webview, bypassing Content Security Policy protections.
  * Opening a malicious Markdown file could lead to code execution within the VS Code process, making document-based attacks a viable threat vector.
  * Extension developers should sanitize all HTML output in webviews; VS Code users should keep extensions updated and exercise caution when opening Markdown files from untrusted sources.

[Last week's blog post](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/) summarized our DEF CON talk "Visual Studio Code Is Why I Have (Workspace) Trust Issues". We presented common attack surfaces of the popular code editor Visual Studio Code (VSCode) and showed examples for each of them, either found by us or by other researchers.

When looking at a vulnerability that used a special `command:` link to trigger certain actions, we were intrigued and investigated further. After not finding a vulnerability related to those links in VSCode itself, we turned to third-party extensions that have millions of users themselves.

In this blog post, we present code vulnerabilities we found in [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (27 million installs) and [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) (15 million installs). We will first give some background on VSCode internals, then explain the vulnerable portions of the code, and finally show how these issues can be prevented.

## Impact

We found and responsibly disclosed three vulnerabilities in the code of third-party VSCode extensions, two in _GitLens_ by GitKraken and one in _GitHub Pull Requests and Issues_ by GitHub:

  * GitLens: Git local configuration leading to Arbitrary Code Execution ([CVE-2023-46944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46944))
  * GitLens: Markdown Injection leading to Arbitrary Code Execution (CVE pending)
  * GitHub Pull Requests and Issues: Markdown injection leading to Remote Code Execution ([CVE-2023-36867](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36867))

All three vulnerabilities are fixed. The affected versions are _GitLens_ before version 14.0.0 and _GitHub Pull Requests and Issues_ before version 0.66.2. The latter one is pre-installed in GitHub Codespaces and on github.dev, GitHub's web version of VSCode.

Fortunately, VSCode updates extensions automatically by default, so most users are expected to be safe as of now. If in doubt, you can always double-check which version you use by going to the _Extensions_ tab in VSCode's sidebar, searching for the respective extension, and clicking on the entry to see the extension's details, including the version number.

All three vulnerabilities require some interaction from the victim of the attack. The first GitLens issue (CVE-2023-46944) requires the user to open a malicious folder in VSCode. The second GitLens issue requires the user to click on a certain UI element that appears when opening an untrusted repository in VSCode. The third issue requires the user to click on a certain UI element that is shown based on a malicious GitHub issue or pull request.

Both GitLens vulnerabilities can be exploited in untrusted workspaces, bypassing the [Workspace Trust security boundary](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/#workspace-trust) of VSCode. The third vulnerability can only be triggered in trusted workspaces, but since attackers can abuse it remotely to attack maintainers of open-source projects, the victims are likely to trust their own projects, allowing the attack to be successful.

## Technical Details

In 2021, we found a vulnerability in VSCode that is related to local Git configurations. You can read the details [in our blog post from back then](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/), but it boils down to the fact that running the `git` executable on untrusted repositories is inherently unsafe because repositories can have their own local configuration that will override the global or user config. Since there are quite some settings that allow to specify custom commands that should be run when certain events occur, it is pretty straightforward to turn this into arbitrary code execution.

The recommended fix is to avoid running `git` on untrusted repos, for example by disabling the entire Git integration in untrusted VSCode workspaces. VSCode implemented this fix for the built-in Git integration, but what about third-party extensions that also use Git?

### GitLens: Git Local Configuration Leads to Code Execution (CVE-2023-46944)

GitLens is an extension developed by GitKraken and has 27 million installs at the time of writing this article. It offers additional features on top of what the built-in Git support of VSCode can do and aims to ease the lives of developers.

We noticed that it would also run in untrusted workspaces, which is a sign to take a closer look at the extension's security. If it uses files or data from the untrusted workspace in a security-sensitive way then attackers could use it to bypass the Workspace Trust boundary.

After observing that GitLens indeed runs `git` commands in the directory of the workspace, we tried our original payload that also worked for VSCode in 2021. As you can see, history repeats itself:

This would allow attackers to execute arbitrary code on the victim's system once a malicious repo is opened in VSCode. After this quick finding, we thought about other VSCode research we've seen in the past and how it could be applicable to third-party extensions such as GitLens.

### GitLens: Markdown Injection Leads to Arbitrary Code Execution

In our previous blog post, we covered several attack surfaces of VSCode, including Cross-Site Scripting (XSS). One example of an XSS vulnerability in VSCode was [CVE-2022-41034](https://github.com/google/security-research/security/advisories/GHSA-pw56-c55x-cm9m), discovered by [Thomas Shadwell](https://twitter.com/zemnmez).

The initial entry point was to include arbitrary HTML in Markdown cells of Jupyter Notebooks. But to go from there to full-blown code execution, he took a different path than other researchers before him. While others would use the usual web attacks of finding and exploiting cross-origin messaging handlers to hijack more privileged origins, he found a way to go straight for code execution.

His magic ingredient was auto-clicking a `command:` link. These links are used throughout VSCode to let the user trigger actions with a click. There are hundreds of these commands, and they can trigger all kinds of actions, from toggling UI elements to starting a debugging session. Even third-party extensions can register new actions that can then be triggered by the user or by other extensions.

After reading Thomas' work, we realized that a big portion of VSCode's UI is just based on Markdown. As an example, an extension can show a custom popup when the user hovers over a piece of code by listening for such an event and supplying a Markdown string with the information that should be shown:

Copy to clipboard
  
  
  vscode.languages.registerHoverProvider('javascript', {
    provideHover(document, position, token) {
      return {
        contents: [new vscode.MarkdownString('# Hover **Content**')]
      };
    }
  });

This is exactly what GitLens does to show detailed information about a Git commit. When a user hovers over the inline blame information that GitLens adds to the currently focused line of code, a popup appears. It lists details such as the commit's author, the commit message, and a per-line diff of the changes:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5bdeab1b-379a-4d7e-87e5-15574825dd65/gitlens-hover-popup.png)

Let's take a look at the code that creates this view:

[src/hovers/hovers.ts](https://github.com/gitkraken/vscode-gitlens/blob/9fdb50644b99ebbead2ac66b5a3f51b7d185a1c4/src/hovers/hovers.ts%20#L23-L141):

Copy to clipboard
  
  
  function changesMessage(/* ... */) /* ... */ {
    // ...
    current = `[$(git-commit) ${commit.shortSha}](${ShowQuickCommitCommand.getMarkdownCommandArgs(commit.sha)} "Show Commit")`;
    // ...
    message = `${diff}\n---\n\nChanges${previous ?? ' added in '}${current} &nbsp;&nbsp;|&nbsp;&nbsp; ${message}`;
    const markdown = new MarkdownString(message, true);
    // ...
    return markdown;
  }

As we can see, GitLens creates a Markdown string by interpolating information from Git into a Markdown template. GitLens also uses `command:` links, for example, to give the user the ability to open a diff of the whole file. To allow the use of `command:` links, GitLens sets the `isTrusted` property of the resulting Markdown string to `true`:

[src/hovers/hovers.ts](https://github.com/gitkraken/vscode-gitlens/blob/9fdb50644b99ebbead2ac66b5a3f51b7d185a1c4/src/hovers/hovers.ts#L137-L140):

Copy to clipboard
  
  
  const markdown = new MarkdownString(message, true);
  markdown.supportHtml = true;
  markdown.isTrusted = true;
  return markdown;

This is required because VSCode sanitizes Markdown strings during rendering and will discard `command:` links from non-trusted strings. But since it is set to true here, attackers could try to somehow insert malicious command links that could trigger unsafe actions.

Looking at how the line diff is generated, we can see that the previous and the current content of the line of code is interpolated into a Markdown code block:

[src/hovers/hovers.ts](https://github.com/gitkraken/vscode-gitlens/blob/9fdb50644b99ebbead2ac66b5a3f51b7d185a1c4/src/hovers/hovers.ts#L283-L291):

Copy to clipboard
  
  
  function getDiffFromHunkLine(hunkLine) {
    // ...
    return `\`\`\`diff${
        hunkLine.previous == null ? '' : `\n- ${hunkLine.previous.line.trim()}`
      }${
        hunkLine.current == null ? '' : `\n+ ${hunkLine.current.line.trim()}`
      }\n\`\`\``;
  }

There is no Markdown sanitization happening, but the content is inside a code block that does not allow usage of other Markdown until the code block is closed. All that is needed to escape the code block is to insert a closing code fence consisting of three backticks ('''``). The closing code fence is required to be at the beginning of a line and the user-controlled content is prefixed with either a plus or a minus sign to make it valid diff syntax. But GitLens only shows the diff for a single line, so how can the three backticks be at the beginning of a line?

Looking at how the Markdown parser determines the start of a line, we can observe that it recognizes the line feed character (`\n`), the carriage return character (`\r`), and the combination of both (`\r\n`) as the separator of two lines. However, GitLens only recognizes the line feed character (`\n`) to be a line separator:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/73832a56-f89e-4f37-8061-2035b8d20a72/gitlens-newline-parser-diff.png)

This creates a parsing difference that attackers can abuse to inject Markdown. By placing a `\r` character into a line, they can make GitLens include it in the line diff string. When the Markdown renderer of VSCode encounters the `\r`, it will treat it as a line separator, putting the following three backticks in a new line. This will end the code block and allow the attacker to include arbitrary Markdown:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c8bfaea8-ead2-477f-9a10-4bdf1dee6ce3/gitlens-newline-parser-diff-2.png)

The attacker can now add arbitrary Markdown to the hover popup. To show that this is security-sensitive, the attacker can insert a Markdown link that points to a `command:` URL and triggers a VSCode action when clicked.

In the original research that inspired us to dig more into this type of bug, the researcher used the command that opens a new terminal inside VSCode. It is possible to specify the executable and arguments that will be run in the terminal, but this command is only available in trusted workspaces. Since our scenario tries to bypass Workspace Trust, it has to be usable in untrusted workspaces.

Looking through the long list of available commands, we found it to be possible to trigger the installation of an arbitrary extension from the VSCode marketplace using the `workbench.extensions.installExtension` command. It takes the extension's ID in a query parameter and will then install and activate the extension.

The VSCode marketplace is available to everyone and publishing extensions is very easy. There is no manual review process, so new extensions can be installed by anyone within minutes after the extension is published.

This allows attackers to publish a malicious extension and then use the install command to run the install and run the malicious extension on the victim's machine. We created a [dummy extension](https://marketplace.visualstudio.com/items?itemName=pspaul.pop-a-calc) to show the successful execution of arbitrary commands by popping a calculator:

After finding this vulnerability, we continued to look through VSCode's marketplace to find more extensions that use attacker-controlled data unsafely when building Markdown UI elements.

### GitHub Pull Requests and Issues: Markdown Injection Leads to Code Execution (CVE-2023-36867)

This extension, made by GitHub, allows its users to manage issues and pull requests of their projects directly from their IDE. This includes viewing the description of those, which are typically use Markdown for rich-text features:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/8c4d8fd2-04c4-496b-bae1-6cfb9105c22c/github-issue-example.png)

To avoid Markdown injection, the GitHub extension first renders the raw description to text:

[src/issues/util.ts](https://github.com/microsoft/vscode-pull-request-github/blob/v0.66.0/src/issues/util.ts#L225-L227):

Copy to clipboard
  
  
  let body = marked.parse(issue.body, {
      renderer: new PlainTextRenderer(),
  });

This consumes the special Markdown character sequences and only outputs the actual content. But there is an issue with this: if the actual content still contains Markdown sequences, they will then be rendered by VSCode!

A simple example of this is a code block. As we already learned previously, the text between code fences is treated as raw text. All special Markdown characters and sequences are put into the output verbatim.

Attackers can abuse this by creating a GitHub issue that contains a Markdown code block, that in turn contains a Markdown link with a `command:` URL:

Copy to clipboard
  
  
  '''plain
  # [Click here](command:workbench.extensions.installExtension?["pspaul.pop-a-calc",{"donotSync":true}])
  '''

On GitHub's web interface, such a description would be rendered as follows:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/8e97440f-b0c0-4907-8821-4807ab04810c/github-issue-markdown.png)

However, the GitHub Pull Requests and Issues extension consumes the surrounding code fence during the plaintext rendering pass and causes the Markdown link to be rendered:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5d1fa16f-fedb-4b50-9e11-19566e7e2cb3/github-malicious-popup.png)

When the victim views the issue using the VSCode extension and clicks on the link, the attacker-controlled extension will be installed and run. The impact of this vulnerability can be considered Remote Code Execution because attackers can create a GitHub issue or PR to target the maintainers of the project without requiring the victim to download and open malicious files.

### Patch

#### GitLens

When we reported the two issues to GitLens, they were already aware of the Git local config issue and were already planning to disable the Git integration for untrusted workspaces. This also prevents the second issue from being exploitable, since no attacker-controlled commit information will be shown in the UI when the integration is turned off.

As we mentioned earlier, not executing any Git commands in untrusted repos is the safest approach. Git has a lot of complexity, so trying to prevent just the exploitable behaviors is bound to fail. Additionally, Git is still being developed, so new features would have to be considered as soon as they are released.

#### GitHub Pull Requests and Issues 

GitHub fixed the vulnerability in their extension by not setting the `isTrusted` property on their created Markdown strings:

Copy to clipboard
  
  
    const markdown: vscode.MarkdownString = new vscode.MarkdownString(undefined, true);
  - markdown.isTrusted = true;

This is of course the safest option but it also prevents the developers from using `command:` links. If you really need to use them in your Markdown, you can set the `isTrusted` property to a list of allowed commands. This will prevent attackers from using arbitrary commands in case they find a way to inject Markdown. You can find more information on this in the [VSCode docs](https://code.visualstudio.com/api/references/vscode-api#MarkdownString).

To avoid the underlying Markdown injection, make sure to always validate, sanitize, or escape data before using it to construct Markdown. A good way to do this in VSCode is to use the [`MarkdownString` class](https://code.visualstudio.com/api/references/vscode-api#MarkdownString) that features the `appendText` function that properly escapes raw text before appending it.

## Timeline

### GitLens

**Date**| **Action**  
---|---  
2023-06-07| We report the two vulnerabilities to GitLens  
2023-06-07| We get an automated acceptance response from GitLens  
2023-06-15| GitLens releases version 14.0.0 that prevents the vulnerable behavior in untrusted workspaces  
2023-07-13| We notice the GitLens release and ask for CVEs and an update from GitLens  
2023-07-13| We get another automated acceptance response from GitLens  
2023-07-15| We get a ticket reference from GitLens, stating they are looking into it  
2023-09-01| GitLens awards us with a $100 bug bounty for the Markdown issue  
2023-11-03| CVE-2023-46944 is assigned by MITRE  
  
### GitHub Pull Requests and Issues

**Date**| **Action**  
---|---  
2023-06-12| We report the vulnerability in GitHub Pull Requests and Issues to Microsoft  
2023-06-16| Microsoft confirms the issue  
2023-07-11| CVE-2023-36867 is assigned by Microsoft  
2023-07-14| Microsoft releases a fix in version 0.66.2 of GitHub Pull Requests and Issues  
  
## Summary

In this article, we took a look at the security of some third-party Visual Studio Code extensions. We saw three vulnerabilities in extensions with millions of installs, all of which have interesting attack vectors that require user interaction to be exploited. We also learned how Markdown is used to create many parts of VSCode's UI, and what risks this has.

Next week, we will finish our series on Visual Studio Code with some new vulnerabilities in VSCode itself. Stay tuned!

## Related Blog Posts

  * [Visual Studio Code Security: Deep Dive into Your Favorite Editor (1/3)](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/)
  * [Securing Developer Tools: Argument Injection in Visual Studio Code](https://www.sonarsource.com/blog/securing-developer-tools-argument-injection-in-vscode/)
  * [Securing Developer Tools: Package Managers](https://www.sonarsource.com/blog/securing-developer-tools-package-managers/)
  * [Securing Developer Tools: Git Integrations](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/)
  * [Securing Developer Tools: OneDev Remote Code Execution](https://www.sonarsource.com/blog/onedev-remote-code-execution/)

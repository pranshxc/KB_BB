---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-21_visual-studio-code-security-finding-new-vulnerabilities-in-the-npm-integration-3.md
original_filename: 2023-11-21_visual-studio-code-security-finding-new-vulnerabilities-in-the-npm-integration-3.md
title: 'Visual Studio Code Security: Finding New Vulnerabilities in the NPM Integration
  (3/3)'
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 34a21bf0b4e7dae97534e6790f9551b6160ffd7c64dc1bfdd3d3df9a306fb2db
text_sha256: fff5cc28fa1e540dc260eefb95f88998d9a7f672bd125cdcb79f8d0ddb55503e
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Visual Studio Code Security: Finding New Vulnerabilities in the NPM Integration (3/3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-21_visual-studio-code-security-finding-new-vulnerabilities-in-the-npm-integration-3.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `34a21bf0b4e7dae97534e6790f9551b6160ffd7c64dc1bfdd3d3df9a306fb2db`
- Text SHA256: `fff5cc28fa1e540dc260eefb95f88998d9a7f672bd125cdcb79f8d0ddb55503e`


## Content

---
title: "Visual Studio Code Security: Finding New Vulnerabilities in the NPM Integration (3/3)"
page_title: "Visual Studio Code Security: Finding New Vulnerabilities in the NPM Integration (3/3) | Sonar"
url: "https://www.sonarsource.com/blog/vscode-security-finding-new-vulnerabilities-npm-integration/"
final_url: "https://www.sonarsource.com/blog/vscode-security-finding-new-vulnerabilities-npm-integration/"
authors: ["Thomas Chauchefoin (@swapgs)", "Paul Gerste"]
programs: ["Microsoft (VS Code)"]
bugs: ["RCE", "Argument injection", "Security code review"]
publication_date: "2023-11-21"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 669
---

## TL;DR overview

  * Sonar researchers found vulnerabilities in VS Code's npm integration that could allow attackers to execute arbitrary commands through crafted package metadata.
  * The flaws exploit the way VS Code processes npm package information, turning a routine development workflow into a potential command injection vector.
  * These findings highlight the security risk of tightly integrating package managers with development tools without proper input sanitization.
  * The vulnerabilities were responsibly disclosed and patched by Microsoft; developers should ensure their VS Code installation is updated to the latest version.

Welcome back to our series on the security of Visual Studio Code! We strongly encourage you reading first [Visual Studio Code Security: Deep Dive into Your Favorite Editor (1/3)](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/) to refresh your memory on the most common types of vulnerabilities in Visual Studio Code as it will come in very handy today.

This time, we dive into two new vulnerabilities in the built-in integration of the JavaScript package manager, NPM. They can be exploited even when Visual Studio Code is configured to not trust the current folder, effectively circumventing the Workspace Trust security feature.

**We recommend all Visual Studio Code users to upgrade to Visual Studio Code 1.82.1 or above to benefit from protection against these vulnerabilities.**

## It all starts with a meeting…

There's a fun anecdote behind these discoveries. While rehearsing [our DEF CON talk on this topic](https://www.youtube.com/watch?v=sdiHfVhPso4), we paused on this slide that shows a command injection vulnerability (CVE-2020-16881) found by David Dworken in the NPM integration:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4a693c2e-e974-4e14-9f2f-3a02b0910f05/3%20-%20NPM%20Slide%201.png)

To address this issue, Microsoft started to validate the contents of the variable `pack` with a regular expression to limit the presence of malicious characters. This patch was quickly bypassed by Justin Steven with CVE-2020-17023:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/99024083-e676-4204-9c0c-f755be712016/3%20-%20NPM%20Slide%202.png)

The researcher also contributed a patch that addresses the issue in a way that CVE-2020-16881 should have been addressed in the first place—more information on this can be found in the original ticket [#107951](https://github.com/microsoft/vscode/issues/107951).

Two vulnerabilities on a single feature are not uncommon, but from our experience, we also know that developers addressing command injection vulnerabilities often leave an argument injection vulnerability at the same location. Could this be the case here?

Even if there is a vulnerability, this may be a risk accepted by the threat model of the software. Before jumping to any conclusion, we first have to understand how this extension works. 

## Let's get more familiar with the NPM integration!

Looking into the NPM integration, we can quickly notice that this is a built-in extension that is enabled by default. In its manifest, it declares that it can run even in untrusted workspaces and triggers when the current directory contains a file named `package.json`:

Copy to clipboard
  
  
  {
  "name": "npm",
  "publisher": "vscode",
  // [...]
  "activationEvents": [
  "onTaskType:npm",
  "onLanguage:json",
  "workspaceContains:package.json"
  ],
  "capabilities": {
  "virtualWorkspaces": {
  "supported": "limited",
  "description": "%virtualWorkspaces%"
  },
  "untrustedWorkspaces": {
  "supported": "limited",
  "description": "%workspaceTrust%"
  }
  },
  // [...]
  }

While the support of `untrustedWorkspaces.supported` is set to `limited`, the module does not really differentiate trusted and unsupported workspaces—it does not use `workspace.isTrusted` or similar features.

We have then the trail of a potential argument injection in a module that's enabled by default, which runs in unstrusted Visual Studio Code workspaces. Let's now confirm if this is a valid finding!

## CVE-2023-36742, Part 1: Argument Injection

The function depicted in the slides above is `npmView()`. When a `package.json` file is open, one of the functionalities of this module is to show information on the name of the dependency when hovered by the user's cursor.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4ef4933c-b750-4bb6-8aaa-8a21a9c0ee36/3%20-%20Integration.png)

Its full implementation is as follows, where `pack` is the variable that contains the name of the hovered dependency:

Copy to clipboard
  
  
  import * as cp from 'child_process';
  // [...]
  private npmView(npmCommandPath: string, pack: string, resource: Uri | undefined): Promise<ViewPackageInfo | undefined> {
  return new Promise((resolve, _reject) => {
  const args = ['view', '--json', pack, 'description', 'dist-tags.latest', 'homepage', 'version', 'time'];
  const cwd = resource && resource.scheme === 'file' ? dirname(resource.fsPath) : undefined;
  cp.execFile(npmCommandPath, args, { cwd }, (error, stdout) => {
  // [...]
  });
  });
  }

This allows an attacker to add arbitrary arguments to the invocation of NPM, but what could be done with it?

### Exploitation

Though this seemed like a powerful primitive in the first place, practical exploitation is unlikely. The most interesting idea was to use NPM's option to change its global configuration, `--globalconfig`. It would result in the following command-line, effectively loading an arbitrary configuration from a local file named `description` that would also be part of the malicious project:

Copy to clipboard
  
  
  npm view --json --globalconfig description dist-tags.latest homepage version time

But after some research, there's no "dangerous" configuration direction in the latest version version of npm. There was one, `onload-script` that pointed to a JavaScript module to execute before `npm view`, and it was removed in npm v7—[for security reasons](https://github.com/npm/feedback/discussions/71)!

However, we found that Ubuntu 20.04.6 TLS, which is still supported, embarks NPM 6.14.4 that would still process `onload-script`.

Because `onload-script` is relative to Node's library paths, like `/usr/share/npm/node_modules`, this requires an absolute path to the script to execute. On Linux systems, this can be solved by using `/proc/self/cwd/` that points to the current folder, but this is not as trivial on all systems.

It may not reflect the constraints of more recent versions of NPM and other platforms, but it still shows that in some cases it could be leveraged to execute arbitrary commands on behalf of the user in untrusted workspaces.

We've added this vector to our [Argument Injection Vectors](https://sonarsource.github.io/argument-injection-vectors/) project, including a mention of this caveat. Let us know if you find other interesting ones for `npm`!

## CVE-2023-36742, Part 2: NPM Local Configuration File

Since the command `npm` is executed, would it also happen to trust files from the local directory? That's one of the principal sources of security issues in Visual Studio Code we documented in [Visual Studio Code Security: Deep Dive into Your Favorite Editor (1/3)](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/). This can be confirmed either by using dynamic tools—here `strace` to identify filesystem accesses—or… [by reading the documentation](https://docs.npmjs.com/cli/v10/using-npm/config#npmrc-files):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/704b5d80-ec71-4b8e-bd67-3ff35c26ecd6/3%20-%20NPM%20Docs%201.png)

Notice the first line: per-project configuration files are supported. That means that this same call to `npm view` will attempt to read the configuration from the current folder. This basically has the same power as [CVE-2023-36742, Part 1: Argument Injection](https://docs.google.com/document/d/1CGcH_jnN8dmj67SO9WUBS_802rV4zEcWrddBAenDxD8/edit#heading=h.rlewi78vy0tu): with full control over the configuration of NPM, attackers could execute arbitrary commands on the victim's system in some cases.

## How did Microsoft address these vulnerabilities?

Date| Action  
---|---  
Aug 8, 2023| We reported the two issues to Microsoft through their MSRC platform.  
Aug 21, 2023| Microsoft confirmed the issues.  
September 9, 2023| Microsoft closed the first issue as a duplicate of the second issue.  
Sept 12, 2023| Visual Studio Code 1.82.1 is released, fixing CVE-2023-36742.  
  
On September 8, Microsoft developers Martin Aeschlimann and Christof Marti pushed a patch addressing the argument injection and mitigating the risks around the use of local configuration files by NPM in [`e7b3397`](https://github.com/microsoft/vscode/commit/e7b339721792056cee11c11afc69df71a0a85d59). Despite distinct root causes and requirements, Microsoft assigned [CVE-2023-36742](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36742) to both reports, arguing they were both fixed in a single commit.

First, they chose to tighten the validation of package names based on a similar implementation as the package `validate-npm-package-name`:

Copy to clipboard
  
  
  --- a/extensions/npm/src/features/packageJSONContribution.ts
  +++ b/extensions/npm/src/features/packageJSONContribution.ts
  @@ -252,11 +252,12 @@ export class PackageJSONContribution implements IJSONContribution {
  }
  
  private isValidNPMName(name: string): boolean {
  -		// following rules from https://github.com/npm/validate-npm-package-name
  -		if (!name || name.length > 214 || name.match(/^[_.]/)) {
  +		// following rules from https://github.com/npm/validate-npm-package-name,
  +		// leading slash added as additional security measure
  +		if (!name || name.length > 214 || name.match(/^[-_.\s]/)) {
  return false;
  }
  -		const match = name.match(/^(?:@([^/]+?)[/])?([^/]+?)$/);
  +		const match = name.match(/^(?:@([^/~\s)('!*]+?)[/])?([^/~)('!*\s]+?)$/);
  if (match) {
  const scope = match[1];
  if (scope && encodeURIComponent(scope) !== scope) {

While this method tries to mimic the behavior of this package, they have small implementation differences. For example, `validate-npm-package-name` agrees that `--help` is a valid package name, while `isValidNPMName()` disagrees.

Then, they introduced the end-of-options POSIX argument to separate options from positional arguments, making it impossible to inject new arguments in the call to `npm view`:

Copy to clipboard
  
  
  --- a/extensions/npm/src/features/packageJSONContribution.ts
  +++ b/extensions/npm/src/features/packageJSONContribution.ts
  @@ -284,7 +285,7 @@ export class PackageJSONContribution implements IJSONContribution {
  
  private npmView(npmCommandPath: string, pack: string, resource: Uri | undefined): Promise<ViewPackageInfo | undefined> {
  return new Promise((resolve, _reject) => {
  -  const args = ['view', '--json', pack, 'description', 'dist-tags.latest', 'homepage', 'version', 'time'];
  +  const args = ['view', '--json', '--', pack, 'description', 'dist-tags.latest', 'homepage', 'version', 'time'];
  const cwd = resource && resource.scheme === 'file' ? dirname(resource.fsPath) : undefined;
  cp.execFile(npmCommandPath, args, { cwd }, (error, stdout) => {
  if (!error) {

Interestingly, the `npm` binary will still load potentially malicious configuration files, but the extension will only be enabled in trusted workspaces—the vulnerability is still here, only now it's behind the Workspace Trust prompt: 

Copy to clipboard
  
  
  --- a/extensions/npm/src/npmMain.ts
  +++ b/extensions/npm/src/npmMain.ts
  @@ -97,7 +97,7 @@ export async function activate(context: vscode.ExtensionContext): Promise<void>
  }
  
  async function getNPMCommandPath(): Promise<string | undefined> {
  -	if (canRunNpmInCurrentWorkspace()) {
  +	if (vscode.workspace.isTrusted && canRunNpmInCurrentWorkspace()) {
  try {
  return await which(process.platform === 'win32' ? 'npm.cmd' : 'npm');
  } catch (e) {

## Reflexions around these patches

Retrospectively, these patches could be made simpler to address all historical issues and our new findings. This is a common pattern we often see when disclosing vulnerabilities to big code bases, where security patches often only try to address singular issues. Over time, it complexifies the code and makes later security reviews harder. It becomes also harder for future developers to work on this feature.

At Sonar, we believe that code quality and security are intimately linked—so much so that they are pillars of what we call Code Quality. It is important to make such code Intentional (clear, logical, etc.) and Adaptable, to ensure its Maintainability and Security. 

In practice, with the patches above, the code stays in a state in which future developers have to grasp and understand all previous decisions to work on it efficiently. They are likely to introduce new or re-introduce old defects, bugs, or vulnerabilities.

## Reflexions around Workspace Trust

Overall, we still think that Workspace Trust is a great feature, a net benefit for developer's security, and we came to slightly nuance our position on this over the last months. 

We're not surprised to find several bypasses around it—security features like this are primarily here to raise the bar for attackers and not fix all holes systematically—but we worry about how easy it became for Microsoft to sweep these issues under the "Workspace Trust" rug. 

If a component becomes the source of many vulnerabilities, it is often put behind Workspace Trust rather than trying to find a way to keep the same set of features more safely. For instance, in the case of the NPM vulnerabilities we just covered, other ways to fetch packages' information exist without relying on an external command call, and using them would have addressed our two findings as well.

Hence, we think that users will be more prone to trust third-party workspaces, so they can fully benefit from basic integrations like Git and NPM. 

The experience of security-conscious users could also be greatly improved by allowing them to not trust any project by default. This systematic prompt is likely to create a form of alert fatigue if you are dealing with many projects and are prompted every time. A similar feature request already exists on GitHub, under [#126311](https://github.com/microsoft/vscode/issues/126311). 

Finally, one can note that such built-in extensions, enabled by default, are also excluded from monetary rewards of the Microsoft Bounty Program. Third-party security researchers are thus less incentivized to look for Workspace Trust bypasses and make this security feature stronger.

## Summary

In this publication, we came back to two vulnerabilities in Visual Studio Code, both related to the NPM integration.

Stepping back from this research, we can also notice how close these bugs are to previous ones we found in the Git integration, CVE-2021-43891, and CVE-2022-30129. They have exactly the same root cause and impact, but only in another component. In this case, NPM security hardening paid off and prevented broader exploitation of the issues introduced by Visual Studio Code.

Another general takeaway from this research is that CVEs tend to point to fragile code. It may sound obvious but it's very common for developers and security practitioners to think that previous vulnerabilities on an attack surface mean that many people already reviewed this code and found anything that is to be found. Reality is more complex than that, and previous CVEs should never stop you from doing code reviews. Justin Steven has been fairly successful with this technique!

Speaking as Visual Studio Code enthusiasts ourselves, we still think that Workspace Trust is a powerful security feature, but it shouldn't be considered enough when dealing with potentially malicious material or when having high security requirements.

We would like to thank all Microsoft employees involved in the disclosure process, from MSRC triagers to Visual Studio Code developers, for their help in addressing our findings.

This post concludes our series on the security of Visual Studio Code, and our research on this topic. We've had fun doing it and sharing our findings with a broader audience. Stay tuned for new vulnerabilities!

## Related Blog Posts

  * [Visual Studio Code Security: Deep Dive into Your Favorite Editor (1/3)](https://www.sonarsource.com/blog/visual-studio-code-security-deep-dive-into-your-favorite-editor/)
  * [Visual Studio Code Security: Markdown Vulnerabilities in Third-Party Extensions (2/3)](https://www.sonarsource.com/blog/vscode-security-markdown-vulnerabilities-in-extensions/)
  * [Securing Developer Tools: Argument Injection in Visual Studio Code](https://www.sonarsource.com/blog/securing-developer-tools-argument-injection-in-vscode/)
  * [Securing Developer Tools: Git Integrations](https://www.sonarsource.com/blog/securing-developer-tools-git-integrations/)

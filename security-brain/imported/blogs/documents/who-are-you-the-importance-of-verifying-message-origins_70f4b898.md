---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-29_who-are-you-the-importance-of-verifying-message-origins.md
original_filename: 2024-01-29_who-are-you-the-importance-of-verifying-message-origins.md
title: Who are you? The Importance of Verifying Message Origins
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
- file-upload
- path-traversal
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
- file-upload
- path-traversal
- automation-abuse
language: en
raw_sha256: 70f4b898df201458496326d61c905b695a8c18816746b0b0b2b886cb6c18ed3d
text_sha256: 1beb54b3867dcd5f76b6748fc5ba695f27f64624f85b77fc34e771f1a6b1052b
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Who are you? The Importance of Verifying Message Origins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-29_who-are-you-the-importance-of-verifying-message-origins.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain, file-upload, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `70f4b898df201458496326d61c905b695a8c18816746b0b0b2b886cb6c18ed3d`
- Text SHA256: `1beb54b3867dcd5f76b6748fc5ba695f27f64624f85b77fc34e771f1a6b1052b`


## Content

---
title: "Who are you? The Importance of Verifying Message Origins"
page_title: "Who are you? The Importance of Verifying Message Origins | Sonar"
url: "https://www.sonarsource.com/blog/who-are-you-the-importance-of-verifying-message-origins/"
final_url: "https://www.sonarsource.com/blog/who-are-you-the-importance-of-verifying-message-origins/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Squidex"]
bugs: ["XSS", "postMessage", "Arbitrary file write", "RCE", "Security code review"]
publication_date: "2024-01-29"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 486
---

## TL;DR overview

  * Verifying message origins is a fundamental security practice that ensures incoming data actually comes from a trusted source before the application acts on it.
  * Failing to verify message authenticity enables attackers to forge requests, impersonate trusted services, and bypass authentication—common root causes in microservice and API vulnerability chains.
  * HMAC signatures and cryptographic verification of message payloads provide reliable origin authentication without requiring full TLS mutual authentication.
  * SonarQube's security analysis detects patterns where applications trust incoming data without verifying its source, flagging potential authentication bypass vulnerabilities.

In our continuous effort to help secure open-source projects and improve our Code Quality solution, we regularly scan open-source projects via [SonarQube Cloud](https://sonarcloud.io/) and evaluate the findings. When scanning the popular C# Content Management System [Squidex](https://squidex.io/), we were faced with the following finding reported by SonarQube Cloud:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/dcd38d16-1d2d-497a-abb4-7166ddc1f2e6/squidex1.png)

[**View this issue on SonarQube Cloud**](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=SonarSourceResearch_squidex-blogpost&open=AY01pLgzMIviG0DPCru_)

SonarQube Cloud detected that this event listener does not verify the event’s origin. This doesn’t feel like a big deal, does it?

As we will see in this blog post, it is a big deal and allows attackers to **fully take over a vulnerable Squidex instance** by tricking a user into clicking on a malicious link. The blog post will detail how attackers can leverage this seemingly minor issue of a missing origin check to achieve code execution and explain how you can discover similar issues in your own code.

## Impact

**Squidex version 7.8.2** and below is prone to **Cross-Site Scripting (XSS)** vulnerability via event listener ([CVE-2023-46252](https://nvd.nist.gov/vuln/detail/CVE-2023-46252)). Attackers can combine this vulnerability with an authenticated **Arbitrary File Write** ([CVE-2023-46253](https://nvd.nist.gov/vuln/detail/CVE-2023-46253)) to gain remote code execution (RCE) on a Squidex instance:

Both vulnerabilities were fixed with [Squidex version 7.9.0](https://github.com/Squidex/squidex/releases/tag/7.9.0).

## Technical Details

In this section, we describe the technical details of both of these vulnerabilities.

### XSS due to Missing Origin Check (CVE-2023-46252)

Before we dive into the technical details of this vulnerability, let’s see how we were able to discover it within seconds. On SonarQube Cloud, an application can quickly be analyzed by adding the corresponding GitHub repository. For public repositories, this is even free, regardless of their size or language. Once the repository is added, SonarQube Cloud starts to analyze the code and we can inspect the findings a few seconds later:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/55536616-9575-4867-b882-e9b75e75ed72/squidex-sonarcloud.gif)

Let’s have a look at the reported `eventListener` function, which is registered in the `SquidexFormField` pseudo-class:

Copy to clipboard
  
  
  function SquidexFormField() {
  // ...
  function eventListener(event) {
  if (event.source !== window) {
  var type = event.data.type;
  console.log('Received Message: ' + type);
  if (type === ...) {
  // ...

Although the event listener checks the source of the event (`event.source`), it is indeed missing a check of its origin (`event.origin`). Because of this as well as the lack of [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) and [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy), a malicious website can include the Squidex website in an iframe and use the [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) method to trigger the execution of the event listener in the context of the included Squidex website:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c37c9e4d-3dc1-4b01-9da8-8f141b0b133c/squidex-postmessage.png)

Looking at the different `type` values attackers can submit this way, the `valueChanged` type caught our attention. When the `SquidexFormField` receives a message with this type, the `value` property is updated and the function `raiseValueChanged` is called:

Copy to clipboard
  
  
  } else if (type === 'valueChanged') {
  value = event.data.value;
  raiseValueChanged();
  }

The `raiseValueChanged` function invokes the `valueHandler` callback, which can be registered via the `onValueChanged` function:

Copy to clipboard
  
  
  /**
  * Register an function that is called whenever the value of the field has changed.
  *
  * @param {function} callback: The callback to invoke. Argument 1: Field value (any).
  */
  onValueChanged: function (callback) {
  if (!isFunction(callback)) {
  return;
  }
  valueHandler = callback;
  raiseValueChanged();
  },

The `SquidexFormField` class is for example used in the [editor-editorjs.html](https://github.com/Squidex/squidex/blob/7.8.2/backend/src/Squidex/wwwroot/scripts/editor-editorjs.html) file, which can be accessed via the public `wwwroot` folder. It uses the `onValueChanged` method to register a callback function, which passes the value provided from the message event to the `editor.render` function:

Copy to clipboard
  
  
  <!DOCTYPE html>
  <html>
  ...
  <script>
  var field = new SquidexFormField();
  var editor = new EditorJS({
  ...
  onReady: function () {
  field.onValueChanged(function (value) {
  if (value) {
  editor.render(value);
  }
  });
  ...
  </script>
  </body>
  </html>

The `editor.render` function used here is part of the [editorjs npm package](https://www.npmjs.com/package/@editorjs/editorjs). Passing an attacker-controlled value to this function introduces a Cross-Site Scripting (XSS) vulnerability. Since the registered message event listener in [`editor-sdk.js`](https://github.com/Squidex/squidex/blob/7.8.2/backend/src/Squidex/wwwroot/scripts/editor-sdk.js) does not verify the origin of the received message, attackers can include the [`editor-editorjs.html`](https://github.com/Squidex/squidex/blob/7.8.2/backend/src/Squidex/wwwroot/scripts/editor-editorjs.html) page in an iframe and send a message to it in order to trigger the execution of arbitrary JavaScript code. This did not only affect self-hosted Squidex instances but also [Squidex Cloud](https://cloud.squidex.io/):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/436ae6a0-4dfd-4b64-9ffa-6c1a83014986/squidex-xss.png)

When determining the impact of this vulnerability, we identified a second vulnerability. This vulnerability is an authenticated file write, which attackers can combine with the XSS vulnerability to execute arbitrary code.

### Arbitrary File Write (CVE-2023-46253)

Squidex allows users with the `squidex.admin.restore` permission to create and restore backups. Part of these backups are uploaded assets. For each asset, the backup zip archive contains a `.asset` file with the actual content of the asset as well as a related `AssetCreatedEventV2` event, which is stored in a JSON file (`4.json`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ddd184b8-91cd-4aae-858d-7f440ae4b2e4/squidex-shell1.png)

Amongst other things, the JSON file contains the event type (`AssetCreatedEventV2`), the ID of the asset (`46c05041-9588-4179-b5eb-ddfcd9463e1e`), its original filename (`test.txt`), and its file version (`0`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/bcccaff6-ea57-4507-ae77-23488f095b6f/squidex-shell2.png)

When a backup with this event is restored, the corresponding asset needs to be re-created. This is done by:

  * determining the name of the `.asset` file in the zip archive,
  * reading its content, and
  * storing the content in the filestore (by default [`FolderAssetStore`](https://github.com/Squidex/libs/blob/main/assets/Squidex.Assets/FolderAssetStore.cs)).

However, the filename used to store the content in the filestore is populated with the ID of the asset. Since this asset ID is taken from the provided JSON file, attackers can set this to an arbitrary value when restoring a backup. This allows attackers to insert a path traversal sequence (`../`) and write the `.asset` file from the backup zip archive to an arbitrary location on the file system.

The by-default appended file version, which is not a `string` but a `long`, would usually restrict the name of the written file. However, attackers can overcome this by setting the `fileVersion` to `-1`, which makes the application omit the file version:

Copy to clipboard
  
  
  private string GetFileName(DomainId appId, DomainId id, long fileVersion = -1, string? suffix = null)
  {
  var sb = new StringBuilder(20);
  // id contains the ID of the asset to restore
  sb.Append(id);
  
  // only append file version if it's greater or equal to 0:
  if (fileVersion >= 0)
  {
  sb.Append('_');
  sb.Append(fileVersion);
  }
  // ...
  return sb.ToString();
  }

Thus attackers can fully control the name and the content of the file written. This ability can be turned into arbitrary code execution by, for example, overwriting the `dotnet-gcdump.dll` file and triggering `gcdump` via the `/api/diagnostics/gcdump` endpoint.

In summary, the seemingly minor issue of a missing origin check can be leveraged by attackers to craft a malicious link, which triggers an XSS attack to gain remote code execution via this additional arbitrary file write vulnerability.

### Patch

The XSS vulnerability (CVE-2023-46252) was fixed by adding the missing origin verification. Since there are valid use cases for certain origins to send messages to a Squidex website, a [dynamic configuration was introduced](https://github.com/Squidex/squidex/commit/9b7d5dce1faf07306e6202ac6df0642eac55acbc):

Copy to clipboard
  
  
  function eventListener(event) {
  if (acceptedOrigins && acceptedOrigins.indexOf(event.origin) < 0) {
  console.log('Origin not accepted: ' + event.origin);
  return;
  }

The arbitrary file write vulnerability (CVE-2023-46253) was fixed by preventing a path traversal attack. [An additional check was added](https://github.com/Squidex/libs/commit/51a1288ae69866546917874d35b227aefd6f7eab#diff-c48d916133cc8d128092281acc53cb9bf5b060a43ecb056b25d4f7cfde906137) to the `FilePathHelper` class, which ensures that files are only created within the intended destination folder:

Copy to clipboard
  
  
  public static class FilePathHelper
  {
  public static string EnsureThatPathIsChildOf(string path, string folder)
  {
  if (path.Contains("../", StringComparison.Ordinal) || path.Contains("..\\", StringComparison.Ordinal))
  {
  throw new InvalidOperationException("Names cannot point to parent directories.");
  }
  
  if (string.IsNullOrWhiteSpace(folder))
  {
  folder = "./";
  }
  
  var absolutePath = Path.GetFullPath(path);
  var absoluteFolder = Path.GetFullPath(folder);
  
  if (!absolutePath.StartsWith(absoluteFolder, StringComparison.Ordinal))
  {
  throw new InvalidOperationException("Names cannot point to parent directories.");
  }
  
  return path;
  }
  }

## Timeline

**Date**| **Action**  
---|---  
2023-10-11| We report all issues to the maintainers.  
2023-10-26| We ask the maintainers for an update.  
2023-10-26| The maintainers confirm the issues.  
2023-10-27| We help the maintainers to fix both issues.  
2023-11-08| The maintainers release the patched version 7.9.0.  
  
## Summary

In this blog post, we outlined the importance of verifying an event’s origin. We have seen how the absence of a check like this can quickly result in a severe impact. For Squidex, attackers could leverage the missing check to craft a malicious link, which triggers an XSS attack to gain remote code execution via an additional arbitrary file write vulnerability.

From a developer’s point of view, a check like this can be easily forgotten because it needs to be consistently applied to all event listeners throughout the whole code base. That’s where our SAST-based Code Quality solution provides irreplaceable benefits. By leveraging the analysis power of [SonarQube Server](https://www.sonarsource.com/products/sonarqube/) or [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) you can ensure that your code stays consistent, intentional, adaptable, and responsible. You don’t even want to introduce issues in the first place? With [SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/) you can follow a [Clean as You Code](https://www.sonarsource.com/solutions/our-unique-approach/) approach right from your IDE of choice.

At last, we would like to thank the Squidex maintainers for confirming our findings and working together with us on a patch to fix these. Thank you!

## Related Blog Posts

  * [pfSense Security: Sensing Code Vulnerabilities with SonarQube Cloud](https://www.sonarsource.com/blog/pfsense-vulnerabilities-sonarcloud/)
  * [Unzipping Dangers: OpenRefine Zip Slip Vulnerability](https://www.sonarsource.com/blog/openrefine-zip-slip/)
  * [Pimcore: One click, two security vulnerabilities](https://www.sonarsource.com/blog/pimcore-one-click-two-security-vulnerabilities/)
  * [OpenEMR - Remote Code Execution in your Healthcare System](https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/)

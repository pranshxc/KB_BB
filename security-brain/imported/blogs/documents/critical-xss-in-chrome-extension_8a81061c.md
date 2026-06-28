---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-17_critical-xss-in-chrome-extension.md
original_filename: 2022-01-17_critical-xss-in-chrome-extension.md
title: Critical XSS in chrome extension
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 8a81061c4718a8950b5167b68d740f935b9a84dd11ca1b726138002c840055fa
text_sha256: 31b7921dcafa4d90f2692c577b95cd0c9b4bafca750db02ea1ca190feed595bc
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Critical XSS in chrome extension

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-17_critical-xss-in-chrome-extension.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `8a81061c4718a8950b5167b68d740f935b9a84dd11ca1b726138002c840055fa`
- Text SHA256: `31b7921dcafa4d90f2692c577b95cd0c9b4bafca750db02ea1ca190feed595bc`


## Content

---
title: "Critical XSS in chrome extension"
url: "https://medium.com/@p3rr0x22/critical-xss-in-chrome-extension-b55757a2074"
authors: ["p3rr0 (@Hperalta89)"]
bugs: ["XSS", "postMessage"]
bounty: "1,500"
publication_date: "2022-01-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3002
scraped_via: "browseros"
---

# Critical XSS in chrome extension

Critical XSS in chrome extension
p3rr0
Follow
4 min read
·
Jan 18, 2022

56

Chrome extensions have a feature to inject content scripts containing JavaScript code in a web page. By using the standard Document Object Model (DOM), they are able to read details of the web pages the browser visits, make changes to them, and pass information to their parent extension.

Injected scripts code lives in an isolated world which is a private execution environment that isn’t accessible to the page or other extensions. A practical consequence of this isolation is that JavaScript variables in an extension’s content scripts are not visible to the host page or other extensions’ content scripts.

Extension scripts and context can be seen in chrome developer tools. In console tab there is an option in the upper left to select context, opening it will show a dropdown with the word extension if any is loaded. In the tab sources there is another menu to check content scripts code.

Now extensions can inject scripts on every url or specific ones, this is defined via regex patterns in the file manifest.json located in the extension installation folder at C:\Users\[login_name]\AppData\Local\Google\Chrome\User Data\Default\Extensions\[extension_id]\manifest.json

{
 "name": "My extension",
 ...
 "content_scripts": [
  {
  "matches": ["https://*.nytimes.com/*"],
  "css": ["my-styles.css"],
  "js": ["content-script.js"]
  }
 ],
 ...
}

Since content scripts run in the context of a web page and not the extension, they often need some way of communicating with the rest of the extension or the background extension document. For example, an RSS reader extension might use content scripts to detect the presence of an RSS feed on a page, then notify the background page in order to display a page action icon for that page.

For further information this is from the official google documentation

https://developer.chrome.com/docs/extensions/mv3/content_scripts/

https://developer.chrome.com/docs/extensions/mv3/messaging/

Get p3rr0’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In this case the chrome extension was used to inject content in google slides, by looking at manifest.json it was noted that content scripts where only injected in specific domains, the one related to the extension domain and in docs.google.com

https://*.redacted.com/

https://docs.google.com/

After finding the specific urls we can look at the code being injected which is also inside the extension installation folder. Since the extension needed to communicate with the extension’s background document to perform different actions it was required to set a communication channel between the extension’s isolated world and the extension’s background document. In order to do this one of the content scripts injected a postMessage listener in the main document, which would handle the messages and pass them to the background document.

Due to the nature of postMessage, a listener will receive messages from any website if no previous checks are defined when the listener function is written, official documentation can be checked for additional information about postMessage.

https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage

In this case any website could communicate with this listener and access the extension’s internal API because no checks were in place, one of the internal methods parsed the content of the message and used it’s value as the argument of window.open({message_content}).

Calling window.open() with a javascript: url is the same as typing it in the url address bar, which results in the code being executed in the context of the current domain.

The vulnerable listener allowed to perform an XSS attack via postMessage, but the severity is raised due to the changed scope in the CVSS calculator because the affected component is the chrome extension, but the impacted component in this case was docs.google.com which is external to the extension owner, since the scope is changed the other vectors are usually set to high because it would be required to determine the impact of the attack in an asset not owed by the affected company.

In this case the exploit scenario was that having the chrome extension installed automatically made your browser vulnerable to XSS in docs.google.com because any website could open a new tab at https://docs.google.com to send the crafted message, access the internal method and call window.open() with arbitrary content. The following code was used as PoC for the report.

nw = window.open('https://docs.google.com/;
nw.postMessage({url:"javascript:alert(1)"},'*')

When chrome extension are in scope vulnerable message listeners aren’t the only way to escalate severity, if a XSS is found in a domain related to the extension check in manifest.json if it allows for external connection or messaging, this will increase attack surface and open more ways to get scope to changed when setting metrics in CVSS , easily increasing severity to high or critical.

https://twitter.com/Hperalta89

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-18_personal-access-token-disclosure-in-asana-desktop-application.md
original_filename: 2022-06-18_personal-access-token-disclosure-in-asana-desktop-application.md
title: Personal Access Token Disclosure in Asana Desktop Application
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- mfa
- otp
- automation-abuse
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- mfa
- otp
- automation-abuse
language: en
raw_sha256: 9e11bc6da5033d2b462941e22bca446f6863c421d977991f65111afff648bd6c
text_sha256: 38209915f7850748e27cfcaddada509b1a0fc5bd870843b86a2ab6cb869b11ff
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Personal Access Token Disclosure in Asana Desktop Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-18_personal-access-token-disclosure-in-asana-desktop-application.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `9e11bc6da5033d2b462941e22bca446f6863c421d977991f65111afff648bd6c`
- Text SHA256: `38209915f7850748e27cfcaddada509b1a0fc5bd870843b86a2ab6cb869b11ff`


## Content

---
title: "Personal Access Token Disclosure in Asana Desktop Application"
page_title: "(Web-)Insecurity Blog | Personal Access Token Disclosure in Asana Desktop Application"
url: "https://security.lauritz-holtmann.de/advisories/asana-desktop-credential-disclosure/"
final_url: "https://security.lauritz-holtmann.de/advisories/asana-desktop-credential-disclosure/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["Asana"]
bugs: ["Information disclosure", "Hardcoded credentials"]
bounty: "6,100"
publication_date: "2022-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2536
---

ADVISORIES June 18, 2022 5 min read 908 words

This post gives an insight into a sensitive data exposure vulnerability in [_Asana for Mac_](https://asana.com/download) that was rated as [_P1_](https://bugcrowd.com/disclosures/caf10f76-f1fb-4dea-8434-9ed2c56a40bb/asana-desktop-application-includes-personal-access-token) and was awarded a bounty.

This was the very first report of that kind for me. Still, I think this type of deployment and build chain issue is more common than one may think.

The issue was reported to _Asana_ via their [Bugcrowd program](https://bugcrowd.com/asana) on June 16th and addressed within a few hours. In fact, the initial triage by Bugcrowd was lightning fast so that the leaked secret could be revoked within hours after it was reported.

* * *

## Table of Contents

  1. Approaching Electron-based applications
  2. Disclosure of Secrets
  3. Proving Impact
  4. Responsible Disclosure Timeline
  5. Learnings for Application Developers
  6. Learnings for Security Researchers

* * *

## Approaching Electron-based applications

Asana’s desktop application is based on [_Electron_](https://www.electronjs.org/), a framework to build “ _native applications_ ” based on websites using web technologies such as HTML, Javascript and CSS.

Electron applications are packed using the [_asar_](https://github.com/electron/asar) (_Electron Archive_) format. The `asar` command-line utility can be used to _extract_ files from a packed _asar_ bundle.

Therefore, we need to install `asar` first, before we can start our actual analysis:
  
  
  $ npm install -g asar
  

Afterward, we obtain the subject of our analysis from `https://desktop-downloads.asana.com/darwin_universal/prod/latest/Asana.dmg`:
  
  
  $ cd /tmp
  $ wget https://desktop-downloads.asana.com/darwin_universal/prod/latest/Asana.dmg
  

On macOS, the disk image (_*.dmg_ file) can be mounted using the `open` command. Afterward, we can copy the application itself (`Asana.app`) to an arbitrary destination:
  
  
  $ open Asana.dmg
  $ cp -r /Volumes/Asana/Asana.app /tmp/Asana.app
  

Running the `file` command reveals that the copied `Asana.app` is actually a folder. Using the `asar extract` command, we can aim to extract the actual “ _web application_ ” sources from the wrapper bundle:
  
  
  $ file /tmp/Asana.app
  /tmp/Asana.app: directory
  $ asar extract /tmp/Asana.app/Contents/Resources/app.asar /tmp/sources
  

The sources can then be opened in a text editor or IDE of your choice: ![VS Code - Asana Sources](/images/advisories/asana-sources.png)

* * *

## Disclosure of Secrets

After browsing a bit around and trying to get a first impression of the folder structure and bundled contents, I almost could not believe my eyes. Within a folder named `release_notes_bot`, there was a file named `.env` that immediately aroused my interest. And indeed, the contents looked a bit _odd_ :
  
  
  $ cat /tmp/sourcecode/release_notes_bot/.env 
  DESKTOP_RELEASE_NOTES_PERSONAL_ACCESS_TOKEN='0/a7f89e98g007e0s07da763a'
  

As the variable name indicates, the value appears to be a [_Personal Access Token_](https://developers.asana.com/docs/personal-access-token) (the above example uses the default one from the documentation 😉). Hardcoding or bundling secrets is definitely a bad practice. The Asana documentation advises, for good reasons:

> Remember to keep your tokens secret; treat them just like passwords! They act on your behalf when interacting with the API. Don’t hardcode them into your programs. Instead, opt to use them as environment variables.

**But** : The token could for instance be bound to a limited service account without access to anything from interest, or be invalid anyway.

* * *

## Proving Impact

Thus, to determine whether the obtained token inherits sensitive privileges, we need to consult the [_API documentation_](https://developers.asana.com/docs), again. This almost immediately nudges us to the following request:
  
  
  GET /api/1.0/users/me HTTP/1.1
  Host: app.asana.com
  Authorization: Bearer [PERSONAL-ACCESS-TOKEN]
  

If we send this request with the obtained token, we receive something like this in response:
  
  
  HTTP/1.1 200 OK
  Content-Type: application/json; charset=UTF-8
  [...]
  
  {
  "data":{
  "gid":"[REDACTED]",
  "email":"[john.smith]@asana.com",
  "name":"[john.smith]@asana.com",
  "photo":{
  "image_21x21":"https://s3.amazonaws.com/profile_photos/[REDACTED].png",
  [...]
  },"resource_type":"user",
  "workspaces":[{
  "gid":"[REDACTED]",
  "name":"[REDACTED]",
  "resource_type":"workspace"
  },{
  "gid":"[REDACTED]",
  "name":"Asana, Inc",
  "resource_type":"workspace"
  }]
  }
  }
  

**Bingo!** The token is _valid_ , _bound to a real user account_ (not just a limited service account), and _has access to multiple workspaces_.  
One of these workspaces appears to be the internal Asana workspace for their employees. 😮

To finally prove the impact, after consulting the documentation again, I obtained the limited outputs of the request to `https://app.asana.com/api/1.0/projects?limit=10&workspace=[REDACTED]` which included the names of some internal Asana projects, and then filed the report at _Bugcrowd_.

* * *

### Responsible Disclosure Timeline

  * **16th June 2022** : [LH] Initial Report via Bugcrowd: <https://bugcrowd.com/disclosures/caf10f76-f1fb-4dea-8434-9ed2c56a40bb/asana-desktop-application-includes-personal-access-token>
  * **16th June 2022** : [Bugcrowd] Report passes triage and is marked as **P3**.
  * **17th June 2022** : [Asana] Asana notifies that the report is fixed, the severity is elevated to **P1** and a _$6,100_ bounty is awarded.

* * *

### Learnings for Application Developers

Make sure that development artifacts do not make their way to production builds. Build processes are often fragile chains of multiple tools - regularly evaluate if each component really acts as expected.

More generally, handle sensitive secrets like _personal access tokens_ or API tokens with care. Limit their scope to their intended use case and regularly rotate and revoke your secrets to limit the impact of leakage.

* * *

### Learnings for Security Researchers

Many bug bounty programs include native applications such as Android, iOS, or desktop apps. For Asana, there was even a [promotion](https://bugcrowd.com/asana/updates/9a868fec-2ca7-49d4-b102-4897a96908e9) for their desktop application. Still, this relatively trivial to identify issue made its way to production - I have to admit that I do not know how long the build process was broken, though.

This leads me to the conclusion, that probably fewer researchers spend time looking at these native assets. Thus, do not fear native applications. Give them a shot, you do not have much to lose 🙂

* * *

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_) or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 🙂

If there is any interest in more educational posts, I could go for a post explaining how to debug _Electron_ applications using _Chrome_ with a hands-on example. In case you are interested, ping me on Twitter or [LinkedIn](https://www.linkedin.com/in/lauritz-holtmann/).

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fadvisories%2Fasana-desktop-credential-disclosure%2F&via=_lauritz_). 🤓

* * *

### Sources

  * [How to get the source code of any electron application](https://medium.com/how-to-electron/how-to-get-source-code-of-any-electron-application-cbb5c7726c37)
  * [Github: asar](https://github.com/electron/asar)
  * [Asana API documentation](https://developers.asana.com/docs)

  * [Asana](/tags/asana)
  * [Hardcoded Credentials](/tags/hardcoded-credentials)
  * [Sensitive Data Exposure](/tags/sensitive-data-exposure)
  * [Electron](/tags/electron)

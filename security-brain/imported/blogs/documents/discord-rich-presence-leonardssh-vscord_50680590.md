---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-23_discord-rich-presence-leonardsshvscord.md
original_filename: 2023-04-23_discord-rich-presence-leonardsshvscord.md
title: Discord Rich Presence LeonardSSH.vscord
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 50680590176bcbe9e01126eda4a044dc133f3f69fb49ad62db653b89c615dbfe
text_sha256: 2cca98645366bca48727bbbf16587ed92dfcf79700bac6aeee0548b2e7e6623e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Discord Rich Presence LeonardSSH.vscord

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-23_discord-rich-presence-leonardsshvscord.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `50680590176bcbe9e01126eda4a044dc133f3f69fb49ad62db653b89c615dbfe`
- Text SHA256: `2cca98645366bca48727bbbf16587ed92dfcf79700bac6aeee0548b2e7e6623e`


## Content

---
title: "Discord Rich Presence LeonardSSH.vscord"
page_title: "advisories/vscode-extension/Discord-Rich-Presence-LeonardSSH.vscord.md at main · Sudistark/advisories · GitHub"
url: "https://github.com/Sudistark/advisories/blob/main/vscode-extension/Discord-Rich-Presence-LeonardSSH.vscord.md"
final_url: "https://github.com/Sudistark/advisories/blob/main/vscode-extension/Discord-Rich-Presence-LeonardSSH.vscord.md"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["vscord"]
bugs: ["Information disclosure"]
publication_date: "2023-04-23"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1229
---

My friends are always active on Discord and they tend use extensions which integerates with Dicord Rich Presence to have some cool status on their Discord profile.

A common example would be this extension which are available for Vscode:

<https://marketplace.visualstudio.com/items?itemName=LeonardSSH.vscord> ( 250,319 installs ) <https://marketplace.visualstudio.com/items?itemName=icrawl.discord-vscode> ( 1,329,713 installs )

From the number of installs you can see such extensions are really very popuplar. You can find similar extension for other applications also like Spotify,Valorant,Genshin Impact,etc

To start using this extension you just need to install it in Vscode and make sure you are using Discord Desktop app,the communication b/w this extension and Discord app happens through websocket. Once the extension is installed just start working on you repository.

Here's how it appears on the Discord UI (both vscode extension have the same view as you can see in this screenshot): [![image](https://user-images.githubusercontent.com/31372554/233820334-462e19c2-2660-4ef6-913d-d0f4e6376899.png)](https://user-images.githubusercontent.com/31372554/233820334-462e19c2-2660-4ef6-913d-d0f4e6376899.png)

If you click on the _View Repository_ button, this popup will appear:

[![image](https://user-images.githubusercontent.com/31372554/233820391-ca93d949-364c-4956-aca7-cc492251634b.png)](https://user-images.githubusercontent.com/31372554/233820391-ca93d949-364c-4956-aca7-cc492251634b.png)

If you proceed to click on _Yep!_ , it will open the repository url in your browser.

* * *

From my understanding the `{git_url}` placeholder value is taken from the .git/config file
  
  
  [core]
  repositoryformatversion = 0
  filemode = false
  bare = false
  logallrefupdates = true
  ignorecase = true
  [remote "origin"]
  url = https://github.com/Sudistark/test-discord-vscode
  fetch = +refs/heads/*:refs/remotes/origin/*
  [branch "master"]
  remote = origin
  merge = refs/heads/master
  

Whatever is in the url is used, passed to Discord and is viewable to other Discord users also upon clicking on the _View Repository_ button.

Most users would be signed in to their GitHub acc in vscode, so there is no requirement for a GitHub personal access token.

But suppose you are not logged in so upon trying to clone a private repo or making commits would ask you for GitHub credentials

A prompt like this appear: [![chrome_qxNwX7MrYQ](https://user-images.githubusercontent.com/31372554/233851141-99ae2082-2fdf-48a7-bd25-a5625d79beb7.png)](https://user-images.githubusercontent.com/31372554/233851141-99ae2082-2fdf-48a7-bd25-a5625d79beb7.png)

username is your GitHub username and for password you need to use your GitHub personal access token. This username password will stored in .git/config file like this:
  
  
  [core]
  repositoryformatversion = 0
  filemode = false
  bare = false
  logallrefupdates = true
  ignorecase = true
  [remote "origin"]
  url = https://sudistark:ghp_xxxxxxxxxxxxxxx@github.com/Sudistark/test-discord-vscode
  fetch = +refs/heads/*:refs/remotes/origin/*
  [branch "master"]
  remote = origin
  merge = refs/heads/master
  

Noticed the `@` part before github.com contains your credentials.

[![image](https://user-images.githubusercontent.com/31372554/233851285-6a946116-e23e-470b-895c-4979072199ba.png)](https://user-images.githubusercontent.com/31372554/233851285-6a946116-e23e-470b-895c-4979072199ba.png)

* * *

The extension had no checks for git_url , even when the url contained the credentials it was pass as it is to Discord due to which any other Discord user would've have got the user's GitHub personal access token by copying the Repository url.

Browsers hides the credentials part ,for example if you were to visit this url suppose in Google Chrome :

<https://sudistark:ghp_xxxxxxxx@github.com/sudistark/private-repo>

In the address bar it would have appear like this instead: <https://github.com/sudistark/private-repo>

It was visible like this only (the credentials part was hidden ) even in Discord when you clicked on the _View Repository_ button.

As the credentials part was hidden all along in Discord and even when you clicked on _View Repository_ button, nobody would have been able to figured it out that there's a bug which is exposing the user's GitHub Personal access token to the public.

Someone would have been only able to identify this bug when he opens your discord profile, clicks on the _View Repository_ button then again clicks on the _Yep_ button confirming to open it in browser and then copies the url from the browser address bar.

* * *

I found this bug totally by mistake, I was just causally checking what my developer friend was doing, so I copied the repo url and pasted in our Discord chat and there I saw a GitHub token.

I had no fucking idea from where that token came from, at first I had doubt that this token is mine but when I checked it with one of the api calls. I saw my friend's username there in the response which confirmed that it was his token.

In the past I have copied my friend's repo url many times but never saw the GitHub token before so I asked him about it to identify the cause of this bug, he told me that he cloned the repo from his another acc using the GitHub token this time.

After trying the same thing I was able to reproduce this behaviour.

* * *

I quickly forwarded the details to the Project Maintainer , which were very swift in responding and addressing the issue: [leonardssh/vscord#209](https://github.com/leonardssh/vscord/issues/209)

A special shoutouts to @leonardssh and @xhayper, I really love when secuirty reports are handle like this. @xhayper noticed that another extension which had the same function was also vulnerable so he came out with a fix for it also, tryly awesome work.

The fix was pretty simple: <https://github.com/leonardssh/vscord/commit/a1a1d51ae4415584ab2c6d6fe9a7ac5a0cdd85d8>
  
  
  import stripCredential from "./helpers/stripCredential";
  
  
  public get gitRemoteUrl(): gitUrlParse.GitUrl | undefined {
  const v = stripCredential(this._remote?.fetchUrl ?? this._remote?.pushUrl ?? "");
  this.debug(`gitRemoteUrl(): Url: ${v ?? ""}`);
  if (!v) return;
  
  return gitUrlParse(v);
  }

<https://github.com/leonardssh/vscord/blob/a1a1d51ae4415584ab2c6d6fe9a7ac5a0cdd85d8/src/helpers/stripCredential.ts>
  
  
  import { URL } from "node:url";
  
  export default function (uri: string): string {
  try {
  const url = new URL(uri);
  url.username = "";
  url.password = "";
  return url.toString();
  } catch (ignored) {
  return uri;
  }
  }

Now the credential part is removed from the url before it is passed to Discord.

* * *

If you are interested in reproducing the bug, then just downgrade your extension it should be below 5.1.8

**Steps to reproduce**

  1. Make sure you aren't signed in to your Github acc in Vscode (instead we will rely upon the Username/Password based authentication for github )

  2. Create any private repository in your github acc

  3. Then clone it in your pc in vscode window (as we are not authenticated a prompt like this will appear) [![chrome_qxNwX7MrYQ](https://user-images.githubusercontent.com/31372554/233614351-27c74855-ca99-4ec7-a20f-7cd7a82acb0c.png)](https://user-images.githubusercontent.com/31372554/233614351-27c74855-ca99-4ec7-a20f-7cd7a82acb0c.png)

  4. Fill in the username and your github personal token as your password

<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>

  5. Now start editing any file in that repo and check discord
  6. Click on the View Repository button
  7. Click on Yep to open the url in browser
  8. From the Browser address bar , copy the url there you will notice that you have got your github token also.

You can verify your token from here
  
  
  curl -s -u "user:ghp_************" https://api.github.com/user

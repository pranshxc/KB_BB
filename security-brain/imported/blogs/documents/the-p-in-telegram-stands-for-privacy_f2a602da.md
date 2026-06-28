---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-11_the-p-in-telegram-stands-for-privacy.md
original_filename: 2021-02-11_the-p-in-telegram-stands-for-privacy.md
title: The 'P' in Telegram stands for Privacy
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: f2a602da9dc700415a1f4630125d778daef33acd348596822649015b4a222048
text_sha256: 3d62516a425c9e9210fa564adebf745f2b97a0d9ead7a415f36610b5d42c9e37
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# The 'P' in Telegram stands for Privacy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-11_the-p-in-telegram-stands-for-privacy.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f2a602da9dc700415a1f4630125d778daef33acd348596822649015b4a222048`
- Text SHA256: `3d62516a425c9e9210fa564adebf745f2b97a0d9ead7a415f36610b5d42c9e37`


## Content

---
title: "The 'P' in Telegram stands for Privacy"
page_title: "The 'P' in Telegram stands for Privacy ~ inputzero"
url: "https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html"
final_url: "https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html"
authors: ["Dhiraj (@RandomDhiraj)"]
programs: ["Telegram"]
bugs: ["Privacy issue"]
bounty: "3,000"
publication_date: "2021-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3919
---

#  [The "P" in Telegram stands for Privacy](https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html)

Written by [Dhiraj](https://www.blogger.com/profile/17432054824339572035 "author profile") on [12:49](https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html "permanent link") in [Privacy](https://www.inputzero.io/search/label/Privacy), [Telegram](https://www.inputzero.io/search/label/Telegram) with [ No comments ](https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html#comment-form) [ ![](https://img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=7052034537728065557&postID=5173062149660468180&from=pencil "Edit Post")

**Summary:** While understanding the implementation of various security and privacy measures in telegram, I identified that telegram fails again in terms of handling the users data. My initial study started with understanding how self-destructing messages work in the secret chats option, telegram says that "_The clock starts ticking the moment the message is displayed on the recipient's screen (gets two check marks). As soon as the time runs out, the message disappears from both devices._ "  

Telegram which has 500 million active users suffers from a logical bug exists in telegram for macOS (7.3 (211334) Stable) which stores the local copy of received message (audio/video) on a custom path even after those messages are deleted/disappeared from the secret chat.  
  

**Technical analysis:** Open telegram for macOS, send a recorded audio/video message in normal chat, the application leaks the sandbox path where the recorded message is stored in ".mp4" file.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipiQ9WjD6f0k03Din0jStvZq6bZPqkqvXAcAAj7ZzBvUjkQnbnzwQDgCiYQl7KF3H_jAtFOk42y2hTwlw48HW19t_JzV27FEnvxMzehdu7W6eiKbs14To-GdeW_L6xPYrPwNZM8c_AAxk/s16000/Telegram_Info_Leak.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipiQ9WjD6f0k03Din0jStvZq6bZPqkqvXAcAAj7ZzBvUjkQnbnzwQDgCiYQl7KF3H_jAtFOk42y2hTwlw48HW19t_JzV27FEnvxMzehdu7W6eiKbs14To-GdeW_L6xPYrPwNZM8c_AAxk/s2560/Telegram_Info_Leak.gif)

In my case the path was (/var/folders/x7/khjtxvbn0lzgjyy9xzc18z100000gn/T/). While performing the same task under secret chat option the MediaResourceData(path://) URI was not leaked but the recorded audio/video message still gets stored on the above path.  

  

  
  
In the video proof-of-concept the user receives a self-destructed message in the secret chat option, which gets stored even after the message is self-destructed.

**Bonus:** The above mentioned version of telegram for macOS stores local passcode in plain text, below is the video proof-of-concept.

  

Both the vulnerabilities was patched in version [7.4 (212543) Stable](https://macos.telegram.org/#v7-4-2021-01-29) and 3000 EURO bounty was awarded. In past I've identified multiple vulnerabilities under Telegram you can read them [here](https://www.inputzero.io/). Later today Fri 12 Feb 12:15 PM, CVE-2021-27204 & CVE-2021-27205 was assigned. What next?  

> Use Signal
> 
> — Elon Musk (@elonmusk) [January 7, 2021](https://twitter.com/elonmusk/status/1347165127036977153?ref_src=twsrc%5Etfw)

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html&t=The "P" in Telegram stands for Privacy "Share this on Facebook")[__](https://twitter.com/home?status=The "P" in Telegram stands for Privacy -- https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html "Tweet This!")[__](https://plus.google.com/share?url=https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=https://www.inputzero.io/2020/12/telegram-privacy-fails-again.html&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipiQ9WjD6f0k03Din0jStvZq6bZPqkqvXAcAAj7ZzBvUjkQnbnzwQDgCiYQl7KF3H_jAtFOk42y2hTwlw48HW19t_JzV27FEnvxMzehdu7W6eiKbs14To-GdeW_L6xPYrPwNZM8c_AAxk/s16000/Telegram_Info_Leak.gif&description=The "P" in Telegram stands for Privacy "Share on Pinterest")

[Email This](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=5173062149660468180&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=5173062149660468180&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=5173062149660468180&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=5173062149660468180&target=facebook "Share to Facebook")

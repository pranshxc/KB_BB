---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-09_telegram-addresses-another-privacy-issue.md
original_filename: 2019-09-09_telegram-addresses-another-privacy-issue.md
title: Telegram addresses another privacy issue
category: documents
detected_topics:
- mobile-security
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- business-logic
- api-security
language: en
raw_sha256: bff28acf435ea2874811c02b6ea39ba7a2c4c73aebfb01fdcc48b9553b340fb5
text_sha256: 4516ed874ae9b74e4d6582baf4c61c621d8f29be165fa25aa1f72adacd579a1e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Telegram addresses another privacy issue

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-09_telegram-addresses-another-privacy-issue.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `bff28acf435ea2874811c02b6ea39ba7a2c4c73aebfb01fdcc48b9553b340fb5`
- Text SHA256: `4516ed874ae9b74e4d6582baf4c61c621d8f29be165fa25aa1f72adacd579a1e`


## Content

---
title: "Telegram addresses another privacy issue"
page_title: "Telegram addresses another privacy issue ~ inputzero"
url: "https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html"
final_url: "https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html"
authors: ["Dhiraj (@RandomDhiraj)"]
programs: ["Telegram"]
bugs: ["Logic flaw", "Privacy issue"]
bounty: "2,500"
publication_date: "2019-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5040
---

#  [Telegram addresses another privacy issue](https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html)

Written by [Dhiraj](https://www.blogger.com/profile/17432054824339572035 "author profile") on [07:44](https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html "permanent link") in [Privacy](https://www.inputzero.io/search/label/Privacy), [Telegram](https://www.inputzero.io/search/label/Telegram) with [ No comments ](https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html#comment-form) [ ![](https://img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=7052034537728065557&postID=3378319109619527956&from=pencil "Edit Post")

**Summary:** This is not a security vulnerability its a privacy issue. As I understand Telegram a messaging app focuses on privacy which has over 10,00,00,000+ downloads in Playstore. In this case, we are abusing a well-known feature of deleting messages, which allows users to delete messages sent by mistake or genuinely to any recipient. It was observed that once the message (image) is sent to the recipient, it still remains in the internal storage of the user which is located at `/**Telegram/Telegram Images/`** path.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTtMHZRFAWwLLqOl5FmmqyLQJeAfubqDpUxqcHQaQZrVul2RaInfrYtqMJ4VjOeRIGDJ1acPMKCLhBV5NvwGD4TMpX1XTZF6E6buGO7Y_91lUAzq7cTvBOfG4ztjH_tpumtUDbqMBRrHM/s200/Dhiraj_Mishra.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTtMHZRFAWwLLqOl5FmmqyLQJeAfubqDpUxqcHQaQZrVul2RaInfrYtqMJ4VjOeRIGDJ1acPMKCLhBV5NvwGD4TMpX1XTZF6E6buGO7Y_91lUAzq7cTvBOfG4ztjH_tpumtUDbqMBRrHM/s1600/Dhiraj_Mishra.gif)

**Technical analysis:** I found this bug when I was researching about Telegram and MTProto protocol. To demonstrate this bug let's assume two people here, Bob and Alice.  
  
Assume a scenario where Bob sends a message which is a confidential image and was mistakenly sent to Alice, Bob proceeds to utilize a feature of Telegram known as "**Also delete for Alice** " which would essentially delete the message for Alice. Apparently, this feature does not work as intended, as Alice would still be able to see the image stored under `**/Telegram/Telegram Images/`** folder, concluding that the feature only deletes the image from the chat window.  
  
The highlighted issue is valid when we talk about Telegram "supergroups" as well, assume a case wherein you're a part of a group with 2,000,00 members and you accidentally share a media file not meant to be shared in that particular group and proceed to delete, by checking "delete for all members" present in the group. You're relying on a functionality that is broken since your file would still be present in storage for all users.  
Aside from this, I found that since Telegram takes `read/write/modify` permission of the USB storage which technically means the confidential photo should have been deleted from Alice's device or storage.  
**  
****Comparison:** A compete, app for Telegram which is WhatsApp also has the same feature to "**Delete for everyone** ". If you perform the following steps mentioned above in WhatsApp it deletes the confidential photo from Alice's `**/Whatsapp/Whatsapp Media/Whatsapp Images/** ` folder and maintains the privacy however Telegram fails. WhatsApp takes the same permission when it comes to storage which is `read/write/modify`.  
  
This issue could have a bigger impact and I am not sure how far this was in place; the word privacy of Telegram fails here again, and users trust against the Telegram is at risk.  
  
**Video PoC:**  
  
  
**  
****Affected version:** I have tried this with the latest stable version (5.10.0 (1684)) of Telegram for Android. I haven't tried this with Telegram for iOS and Telegram for Windows but assuming this issue **would** exist on other these platforms.  
  
**Responsible disclosure:** I submitted this to Telegram sec-team via security[at]telegram[dot]org and a fix was pushed in the latest version of Telegram 5.11. Also €2,500 was awarded by Telegram.  

  

**Other Workaround:** The alternative solution would be to utilize the feature of "**New Secret Chat** " in Telegram where no such traces are left.  
  
**References:** Picture used above credit and source[[1]](https://telegram.org/img/tl_card_store.gif). Download the PDF version of this article[[2](https://github.com/RootUp/PersonalStuff/blob/master/Telegram_Privacy.pdf)]. Later [CVE-2019-16248](https://nvd.nist.gov/vuln/detail/CVE-2019-16248) was assigned to this issue.

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html&t=Telegram addresses another privacy issue "Share this on Facebook")[__](https://twitter.com/home?status=Telegram addresses another privacy issue -- https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html "Tweet This!")[__](https://plus.google.com/share?url=https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=https://www.inputzero.io/2019/09/telegram-privacy-fails-again.html&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTtMHZRFAWwLLqOl5FmmqyLQJeAfubqDpUxqcHQaQZrVul2RaInfrYtqMJ4VjOeRIGDJ1acPMKCLhBV5NvwGD4TMpX1XTZF6E6buGO7Y_91lUAzq7cTvBOfG4ztjH_tpumtUDbqMBRrHM/s200/Dhiraj_Mishra.gif&description=Telegram addresses another privacy issue "Share on Pinterest")

[Email This](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=3378319109619527956&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=3378319109619527956&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=3378319109619527956&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=7052034537728065557&postID=3378319109619527956&target=facebook "Share to Facebook")

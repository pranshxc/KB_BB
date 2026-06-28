---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-11_xss-on-google-custom-search-engine.md
original_filename: 2019-07-11_xss-on-google-custom-search-engine.md
title: XSS on Google Custom Search Engine
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: f607997bc31a30285a2e31267406a3ff1bbe6e7fb033c20d8ffce505d9d691f6
text_sha256: a359c56e1d5e29da7c29fb24906baf3b11fa4a15ec5fdfb50ecce6c6bd2ab1bf
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# XSS on Google Custom Search Engine

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-11_xss-on-google-custom-search-engine.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f607997bc31a30285a2e31267406a3ff1bbe6e7fb033c20d8ffce505d9d691f6`
- Text SHA256: `a359c56e1d5e29da7c29fb24906baf3b11fa4a15ec5fdfb50ecce6c6bd2ab1bf`


## Content

---
title: "XSS on Google Custom Search Engine"
page_title: "XSS on Google Custom Search Engine – The Security Experts"
url: "https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/"
final_url: "https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/"
authors: ["KL Sreeram (@kl_sree)"]
programs: ["Google"]
bugs: ["XSS"]
publication_date: "2019-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5156
---

# [XSS on Google Custom Search Engine](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/)

![](https://thesecurityexperts.files.wordpress.com/2019/07/screenshot-from-2019-07-11-19-07-38.png?w=820&h=504&crop=1)

Product Affected: [https://cse.google.com](https://cse.google.com/)

Vulnerability: XSS (Stored with user interaction)

Every bug that ever reported have some realized or unrealized inspirations. It can be a person, bounty, write-up or anything. In my case the inspiration was [Google Vulnerability Research Grant](https://www.google.com/about/appsecurity/research-grants/) that was rewarded to me prior to [BountyCon](https://www.facebook.com/notes/facebook-bug-bounty/bountycon-2019-is-a-wrap/2568024086545135/) 2019\. I started looking for subdomain and landed in [https://cse.google.com](https://cse.google.com/).

Google CSE (Custom Search Engine) gives you ability to create your own custom search engine for your website. Once you have created the custom search engine, you can view it with the following link. <https://cse.google.com/cse?cx>=<YOUR_ID>. It also allows you to add your own promotion URL to your custom search engine (<https://cse.google.com/cse/search/promotions?cx>=<YOUR_ID> ).

![Screenshot from 2019-07-11 19-07-38](https://thesecurityexperts.wordpress.com/wp-content/uploads/2019/07/screenshot-from-2019-07-11-19-07-38.png?w=736)

When the user search the promotion triggering keywords the ad URL will appear in top of search, just like Google. Now all you have to do now is add the most classic “javascript:alert(0)” to the promotion URL. Luckily it didn’t get filtered. So once you search the keyword and click on the promotion URL the alert will popup.

![Screenshot from 2019-07-11 19-24-25](https://thesecurityexperts.wordpress.com/wp-content/uploads/2019/07/screenshot-from-2019-07-11-19-24-25.png?w=358&h=213)

Still complicated to exploit,as user want to enter the promotion triggering query manually. So did a bit of parameter guessing and it worked . <https://cse.google.com/cse?cx>=<YOUR_ID>?q=triggeringkeyword will automatically search the payload for you. Now all you have to do is, send the URL to the victim and he have to click on the promotion. TAAATAAAhh! XSS firesss! Couldn’t make URI based XSS wite-up any longer.. 🙂

Thanks,

[Sreeram](https://twitter.com/kl_sree)

Wait..Here is the GIF you were searching for..

![giphy](https://thesecurityexperts.wordpress.com/wp-content/uploads/2019/07/giphy.gif?w=567&h=307)

### Share this:

  * [ Share on X (Opens in new window) X ](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://0.gravatar.com/avatar/32dcb6585fa857f70a0fb3dad5be471439889652438e9036ea43ff96a3a998d4?s=90&d=identicon&r=G)

##  Published by Sree Ram KL

[ View all posts by Sree Ram KL ](https://thesecurityexperts.wordpress.com/author/sreeramkl/)

__July 11, 2019

__[Uncategorized](https://thesecurityexperts.wordpress.com/category/uncategorized/)

## Post navigation

[Journey through Google referer leakage bugs.](https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/)

##  One thought on “XSS on Google Custom Search Engine” 

## Add yours

  1. ![unicc dumps's avatar](https://2.gravatar.com/avatar/be74456fddf6894317669f7f85ade2476ee41700511537cc733547dc6d65b312?s=80&d=identicon&r=G) **[unicc dumps](https://unicc.bz/register.php)** says:

[July 17, 2019 at 11:11 am](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/#comment-247)

Ιt’s awesome to ppaу a quick visit this site and reaɗing the views  
of all friends on the topic of hіѕ article, while I am also eager of gettikng knowledge.

[Like](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/?like_comment=247&_wpnonce=56b47266ad)Like

[Reply](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/?replytocom=247#respond)

### Leave a comment [Cancel reply](/2019/07/11/xss-on-google-custom-search-engine/#respond)

Δ

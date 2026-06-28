---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-18_bypassing-authentication-using-javascript-debugger.md
original_filename: 2018-09-18_bypassing-authentication-using-javascript-debugger.md
title: Bypassing Authentication Using Javascript Debugger.
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: 3892adf9ef71146c22b46dd3c7c920d2b520ed32a03b1f112319922f10dd16d0
text_sha256: e8323360ee22b1633ff9a1228ce959a11f60bc03db68d5a589eb00a72630a77e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Authentication Using Javascript Debugger.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-18_bypassing-authentication-using-javascript-debugger.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `3892adf9ef71146c22b46dd3c7c920d2b520ed32a03b1f112319922f10dd16d0`
- Text SHA256: `e8323360ee22b1633ff9a1228ce959a11f60bc03db68d5a589eb00a72630a77e`


## Content

---
title: "Bypassing Authentication Using Javascript Debugger."
page_title: "Bypassing Authentication Using Javascript Debugger. | Mohit Dabas's Blog"
url: "https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/"
final_url: "https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/"
authors: ["Mohit Dabas (@mohitdabas08)"]
bugs: ["Authentication bypass"]
publication_date: "2018-09-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5691
---

![](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-04-59-pm.png?w=620)

# Bypassing Authentication Using Javascript Debugger.

So I was checking a website and tried to test it for flaws just a general thing nothing new. I targeted the login mechanism. I saw while clicking on it. It was generating javascript events.

![Screen Shot 2018-09-18 at 3.47.17 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-3-47-17-pm.png?w=620)

![Screen Shot 2018-09-18 at 3.49.12 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-3-49-12-pm.png?w=620)

so the hunt began for this function. i saw every .js files . you know where I found it **js//facebook.js** lol

![Screen Shot 2018-09-18 at 4.02.18 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-02-18-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.02.38 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-02-38-pm.png?w=620)

Here is the function related to authentication ……

![Screen Shot 2018-09-18 at 4.02.52 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-02-52-pm.png?w=620)

**Putting a breakpoint on data variable****comparison.**

![Screen Shot 2018-09-18 at 4.04.16 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-04-16-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.04.46 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-04-46-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.04.59 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-04-59-pm.png?w=620)

Modifying the data value in the console.

![Screen Shot 2018-09-18 at 4.05.15 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-05-15-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.05.32 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-05-32-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.06.09 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-06-09-pm.png?w=620)

Voila, more information!!!!!!!

![Screen Shot 2018-09-18 at 4.19.19 PM](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-19-19-pm.png?w=620)

![Screen Shot 2018-09-18 at 4.19.32 PM.png](https://mohitdabas.wordpress.com/wp-content/uploads/2018/09/screen-shot-2018-09-18-at-4-19-32-pm.png?w=620)

### Share this:

  * [ Share on X (Opens in new window) X ](https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/?share=facebook)
  * 

Like Loading...

### _Related_

Posted in [Exploits](https://mohitdabas.wordpress.com/category/exploits/) and tagged [debugging](https://mohitdabas.wordpress.com/tag/debugging/), [Exploits](https://mohitdabas.wordpress.com/tag/exploits/), [mohit-dabas-blog](https://mohitdabas.wordpress.com/tag/mohit-dabas-blog/) on [September 18, 2018](https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/ "10:52 am") by [mohitdabas](https://mohitdabas.wordpress.com/author/mohitdabas/ "View all posts by mohitdabas"). [4 Comments](https://mohitdabas.wordpress.com/2018/09/18/bypassing-authentication-using-javascript-debugger/#comments)

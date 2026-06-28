---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-14_xssing-google-code-in-thanks-to-improperly-escaped-json-data.md
original_filename: 2018-12-14_xssing-google-code-in-thanks-to-improperly-escaped-json-data.md
title: XSSing Google Code-in thanks to improperly escaped JSON data
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
raw_sha256: 109f96b3874760d395f0bbc3e77e22fd03fc4ed7ef52a939b7930bc77220164e
text_sha256: 79d50b9d2e1567616b37b4c133270fee044b7034b2189384acb235bdb1ffb408
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSSing Google Code-in thanks to improperly escaped JSON data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-14_xssing-google-code-in-thanks-to-improperly-escaped-json-data.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `109f96b3874760d395f0bbc3e77e22fd03fc4ed7ef52a939b7930bc77220164e`
- Text SHA256: `79d50b9d2e1567616b37b4c133270fee044b7034b2189384acb235bdb1ffb408`


## Content

---
title: "XSSing Google Code-in thanks to improperly escaped JSON data"
page_title: "XSSing Google Code-in thanks to improperly escaped JSON data - Web Security Blog"
url: "https://websecblog.com/vulns/google-code-in-xss/"
final_url: "https://websecblog.com/vulns/google-code-in-xss/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["XSS"]
publication_date: "2018-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5523
---

# XSSing Google Code-in thanks to improperly escaped JSON data

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[December 14, 2018February 16, 2022](https://websecblog.com/vulns/google-code-in-xss/)

[Google Code-in](https://codein.withgoogle.com/) is an online programming competition for students hosted by Google that takes place every year.

When I was signing up for a second time, I put a payload into all the text fields. I didn’t expect anything to happen, but when I clicked the submit button, all the payloads were executed. And the payloads continued executing on every page I visited. This alone didn’t mean much as it would only classify as a self-XSS but meant that this didn’t have to be the only place the payload was improperly shown on the page. I submitted this bug to the support email and also to Google VRP in case it turns out to be a real issue.

In Google Code-in you can submit tasks for review and also can add comments to them. And as usual, I put the payload in the comment. Surprisingly, when I added the comment, the payload worked once again. And it stayed there even after I reloaded the page. I sent an update to Google and they fixed it the following day.

## The Payload

Now let’s take a look at what happened with the payload.

They used `script` elements with type `application/json` generated on the backend to pass user data to the client-side.
  
  
  <script type="application/json">
  {"someData": true, "text": "hello world", "user": 123}
  </script>

In the comment and other fields I used a simple payload like this:
  
  
  "'><script src=x></script>{{1-1}}

When a new comment is sent, it’s also added to the JSON object which holds the comments of a task as well as some other data.  
So when the comment was added, the JSON would look something like this:
  
  
  <script type="application/json">
  {
  "someData": true,
  "comments": [{
  "id": 123,
  "text": "\"'><script src=x></script>{{1-1}}"
  }]
  }
  </script>

As you can see, the double quote is escaped correctly and it’s a perfectly valid JSON.  
Except… they forgot to escape one important thing.

## Parsing Context

As written in the HTML4 [documentation](https://www.w3.org/TR/html4/types.html#h-6.2):

> The first occurrence of the character sequence “</” (end-tag open delimiter) is treated as terminating the end of the element’s content. In valid documents, this would be the end tag for the element.

This means as soon as the HTML parser sees `</script>`, it assumes it is the end of that element.

[![Google Code-in XSS](https://websecblog.com/wp-content/uploads/2018/12/gci_bug_source_code_edited.png)](https://websecblog.com/wp-content/uploads/2018/12/gci_bug_source_code_edited.png)

We get even more info [in the appendix of the documentation](https://www.w3.org/TR/html4/appendix/notes.html#h-B.3.2.1):

> When script or style data is the content of an element ([SCRIPT](https://www.w3.org/TR/html4/interact/scripts.html#edef-SCRIPT) and [STYLE](https://www.w3.org/TR/html4/present/styles.html#edef-STYLE)), the data begins immediately after the element start tag and ends at the first ETAGO (“</”) delimiter followed by a name start character ([a-zA-Z]); note that this may not be the element’s end tag. Authors should therefore escape “</” within the content.

How to prevent this from happening, from the chapter [_Restrictions for contents of script elements_](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements):

> The easiest and safest way to avoid the rather strange restrictions described in this section is to always escape “`<!--`” as “`<\!--`“, “`<script`” as “`<\script`“, and “`</script`” as “`<\/script`” when these sequences appear in literals in scripts (e.g. in strings, regular expressions, or comments), and to avoid writing code that uses such constructs in expressions. Doing so avoids the pitfalls that the restrictions in this section are prone to triggering: namely, that, for historical reasons, parsing of script blocks in HTML is a strange and exotic practice that acts unintuitively in the face of these sequences.

This still wouldn’t be enough to get a working XSS on the page ([in modern browsers](https://caniuse.com/#feat=contentsecuritypolicy)) since they have a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) set up. I wrote about bypassing CSP in a separate [article](https://websecblog.com/vulns/google-csp-evaluator/). In a nutshell, CSP allows you to whitelist allowed sources of scripts, styles, and other resources to mitigate XSS attacks. This means a `<script>` element just like that wouldn’t be able to get through CSP and therefore wouldn’t be executed.

Fortunately, Google Code-in uses AngularJS on its frontend. This means CSP can be easily bypassed. Expressions such as `{{1-1}}` get easily evaluated (see [Angular XSS on McDonalds.com](https://websecblog.com/vulns/angular-xss-vulnerability-on-mcdonalds-com/)). Since AngularJS 1.6, Google [removed the expression sandbox](https://blog.angularjs.org/2016/09/angular-16-expression-sandbox-removal.html) completely, which means we can access the document with no problem just like this:
  
  
  {{constructor.constructor('alert("xss")')()}}

Now we have a working payload that gets executed every time someone (in this case mentors or site admins) opens the comments page.

* * *

Timeline|  
---|---  
2018-10-30| Vulnerability reported  
2018-10-31| Fixed (by the dev team)  
2018-11-01| Closed  
2018-11-21| Reopened and accepted  
2018-11-21| Priority changed to P2  
2018-12-11| Reward issued  
2018-12-12| Marked as fixed  
  
Written by [Thomas Orlita](https://thomasorlita.com/)

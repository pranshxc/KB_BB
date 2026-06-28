---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-06_a-web-security-story-from-2008-silently-securing-jsonparse.md
original_filename: 2023-04-06_a-web-security-story-from-2008-silently-securing-jsonparse.md
title: 'A web security story from 2008: silently securing JSON.parse'
category: documents
detected_topics:
- xss
- command-injection
- mfa
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- otp
- automation-abuse
- api-security
language: en
raw_sha256: d4b157f3deb3de273a922842539d09bf73a6a70bc27debce485aeb829cedbfda
text_sha256: da9a2897d5f5fe7761f40d8c2ef7d564a82c6b84756eb954292680206afda31b
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# A web security story from 2008: silently securing JSON.parse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-06_a-web-security-story-from-2008-silently-securing-jsonparse.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `d4b157f3deb3de273a922842539d09bf73a6a70bc27debce485aeb829cedbfda`
- Text SHA256: `da9a2897d5f5fe7761f40d8c2ef7d564a82c6b84756eb954292680206afda31b`


## Content

---
title: "A web security story from 2008: silently securing JSON.parse"
page_title: "A web security story from 2008: silently securing JSON.parse - DEV Community"
url: "https://dev.to/mikesamuel/2008-silently-securing-jsonparse-5cbb"
final_url: "https://dev.to/mikesamuel/2008-silently-securing-jsonparse-5cbb"
authors: ["Mike Samuel (@mvsamuel)"]
programs: ["JSON.parse"]
bugs: ["Parsing issue", "XSS", "Arbitrary Code Execution"]
publication_date: "2023-04-06"
added_date: "2023-04-07"
source: "pentester.land/writeups.json"
original_index: 1291
---

[![Mike Samuel](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F157271%2Fa0ec88ed-18c5-410f-899a-992cfd45d14b.jpeg)](/mikesamuel)

[Mike Samuel](/mikesamuel)

Posted on Apr 6, 2023 • Edited on Jan 23

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

#  A web security story from 2008: silently securing JSON.parse 

[#cybersecurity](/t/cybersecurity) [#javascript](/t/javascript) [#security](/t/security) [#webdev](/t/webdev)

My 8 year old is doing a report for school on cyber security so I thought I'd dig up an old report for a break-the-web level security vulnerability that we silently fixed and which, as far as I know, has never been disclosed.

Back in 2008, _JSON.parse_ was not part of the JavaScript language. It was a separate library downloaded from json.org that [used JavaScript `eval` to unpack data](https://github.com/douglascrockford/JSON-js/blob/8da84c40419b33609cc1d0100395dca01a33b503/json2.js#L547-L552).  

  
  
  // In the third stage we use the eval function to compile the text into a
  // JavaScript structure. The "{" operator is subject to a syntactic ambiguity
  // in JavaScript: it can begin a block or an object literal. We wrap the text
  // in parens to eliminate the ambiguity.
  
  j = eval("(" + text + ")");
  

That code from a modern version of `json2.js` wraps the JSON source text in parentheses, because `{}` is a statement block in JavaScript but `({})` is an object constructor.

But a side-effect of using `eval` is that, if the source text is something like `doVeryBadThings()` then the JavaScript engine will happily do those very bad things, a classic [arbitrary code execution vulnerability](https://en.wikipedia.org/wiki/Arbitrary_code_execution).

> In computer security, arbitrary code execution (ACE) is an attacker's ability to run any commands or code of the attacker's choice on a target machine or in a target process.

Luckily, `json2.js` did a bunch of regular expression checks to make sure that `text` contained valid JSON, allowing commands that construct a value but not more powerful commands.

Unluckily, JSON is not a _subset_ of JavaScript in the semantic sense. There are important differences.

To understand those differences, let's begin at the end with [a change to the JavaScript language definition](http://archives.ecma-international.org/2008/TC39/tc39-2008-055.pdf) that I argued for based on this research.

[![Screenshot of draft EcmaScript 3.1 specification quoted below](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi0ss4ch4yzc02x091ks7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi0ss4ch4yzc02x091ks7.png)

Here's the changed specification text. It mirrors some explanatory text from Unicode §6.2.

> **7.1 Unicode Format-Control Characters**  
>  The Unicode format-control characters (i.e., the characters in category “Cf” in the Unicode Character Database such as LEFT-TO-RIGHT MARK or RIGHT-TO-LEFT MARK) are control codes used to control the formatting of a range of text in the absence of higher-level protocols for this (such as mark-up languages).  
>  It is useful to allow these in source text to facilitate editing and display.  
>  The format control characters maybe used in identifiers, within comments, and within string literals and regular expression literals.

And to the right of that is some deleted specification text.

> 7/2/2008 **Deleted** : anywhere in the source text of an ECMAScript program. These characters are removed from the source text before applying the lexical grammar. Since these characters are removed before processing string and regular expression literals, one must use a Unicode escape sequence (see 7.6) to include a Unicode format-control character inside a string or regular expression literal

JavaScript allows these control flow characters, known as _[Cf]_ , in identifiers because they're important for proper presentation of identifiers, especially those in cursive writing systems like عنصر in the Perso-Arabic alphabet. But they're a bit of a blind spot for many developers.

They were "removed from the source text **before** applying the lexical grammar." That means before the JavaScript parser has broken the source code into tokens, so

  * before it pairs quotation marks (`"`) that start and end quoted string values, and
  * before it pairs delimiters like `/*` and `*/` or groups sequences like `//` and `+=` that have no analogue in JSON.

JSON's specification does not have an equivalent clause. json.org simply says:

> A string is a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes.

I realized that, by putting a _[Cf]_ character between a backslash and a quote character I could get JavaScript's `eval` to find a different end of string than the JSON grammar would as expressed in the regular expressions that vet the JSON text. And that would allow me to sneak code into a JSON string that `eval` would execute.

I sent an email to the JSON maintainer, Douglas Crockford, with a [proof of concept](https://www.malwarebytes.com/glossary/proof-of-concept):

[![Email to Douglas Crockford dated Mar 14 2008 / transcript below](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl8bctk6aj5lrjt2a9h1b.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl8bctk6aj5lrjt2a9h1b.png)

Transcript:

> From Mike Samuel  
>  to Douglas, Kevin
> 
> On firefox 2, the below alerts "hello world" after "created string about to parse" using a version of <http://www.JSON.org/json2.js> downloaded earlier today.  
> 
  
  
  <html>
  <head>
  <script src=json2.js></script>
  </head>
  <body onload="
  var s = '&quot;\\\u200D\\&quot;, alert(\'hello world\') //&quot;\n';
  alert('created string about to parse');
  JSON.parse(s);
  ">
  
  </body>
  </html>
  

> From Douglas Crockford  
>  to me
> 
> I don't understand what is happening here.  
>  Can you please explain the attack to me?

I didn't do a good job explaining it the first time though, but here is my second attempt:

[![Email quoted below](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F32bwx0o4rr2xo66m1bip.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F32bwx0o4rr2xo66m1bip.png)

The proof of concept was, where `|` stands in for Unicode's _zero-width joiner_ character (U+200D):  

  
  
  "\|\", alert('hello world') //"
  

So a valid JSON parser would see just a single quoted string that contained two escaped characters, one of which was an escaped quote. And the regular expressions that json2.js used to approximate had the same interpretation.

So json2.js's security checks let that string through to JavaScript's `eval`.

But JavaScript's tokenizer saw something different because the control character is stripped out **before tokenization** :  

  
  
  "\\", alert('hello world') //"
  

There, the two backslashes (which previously had a _[Cf]_ character between them) combine to form one escaped backslash.  
The previously escaped double quote now ends the string. As the email explains (with bullets added for clarity):

> Firefox sees ...
> 
>  1. a string literal containing only a backslash followed by
>  2. a comma followed by
>  3. a call to `alert` followed by
>  4. a line comment.
> 

(That line comment hides the final double quote, so that `eval` doesn't stop with a syntax error.)

Douglas realized he needed to change the regular expression used by json2.js.

[![Email quoted below](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhkse1lkcd92q64oir8an.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhkse1lkcd92q64oir8an.png)

> So I think I have to do the same search for restricted characters that I do for ADsafe:
>  
>  
>  cx = /[\u0000-\u001f\u007f-\u009f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/,
>  
> 
> Bother.

(Bother, indeed.)

But then he realized that we didn't want attackers to be able to [reverse engineer the vulnerability](https://www.theregister.com/2005/07/01/reverse_engineering_patches/) from that targeted change, so he unilaterally changed the definition of JSON on the fly.

> If I put `cx` in json.js and announce them[sic] problem, it will be giving a pretty clear signal to the miscreants about how to exploit but. But if instead, the fix is that I replace the regexp
>  
>  
>  /\\./
>  
> 
> with one that only matches `\` followed by a printable ASCII character, then the the text will be rejected. My fix will be less informative.

So that's how an arbitrary code execution that affected almost all of the JavaScript code using JSON in 2008 was silently closed with, afaik, no-one the wiser.

##  Top comments (1)

Subscribe

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[ Create template ](/settings/response-templates)

Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](/404.html)

[ ![kurtextrem profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F50805%2F30253821-2be4-48e7-94e8-d15737c4bc40.jpg) ](https://dev.to/kurtextrem)

[ Jacob "kurtextrem" Groß  ](https://dev.to/kurtextrem)

Jacob "kurtextrem" Groß 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F50805%2F30253821-2be4-48e7-94e8-d15737c4bc40.jpg) Jacob "kurtextrem" Groß  ](/kurtextrem)

Follow

  * Location 

Munich, Germany 

  * Joined 

Dec 24, 2017

• [ Apr 10 '23  ](https://dev.to/mikesamuel/2008-silently-securing-jsonparse-5cbb#comment-261b8)

  * [Copy link](https://dev.to/mikesamuel/2008-silently-securing-jsonparse-5cbb#comment-261b8)
  *  * Hide 
  *  *  * 

Now if that isn't a story to tell your kids about - I don't know what is.

2 likes Like  Reply

[Code of Conduct](/code-of-conduct) • [Report abuse](/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink. 

Hide child comments as well

Confirm 

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)

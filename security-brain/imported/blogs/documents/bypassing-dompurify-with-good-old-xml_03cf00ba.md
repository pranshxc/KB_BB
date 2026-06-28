---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-01_bypassing-dompurify-with-good-old-xml.md
original_filename: 2024-04-01_bypassing-dompurify-with-good-old-xml.md
title: Bypassing DOMPurify with good old XML
category: documents
detected_topics:
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 03cf00bac4f824a34af362690abf810aa8ed86c7332543eb58a82085aba42ab5
text_sha256: 1f6586faa50a8bf2c92a0c2a57389f98172117eb62fa686777c9c2b55fc90531
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing DOMPurify with good old XML

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-01_bypassing-dompurify-with-good-old-xml.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `03cf00bac4f824a34af362690abf810aa8ed86c7332543eb58a82085aba42ab5`
- Text SHA256: `1f6586faa50a8bf2c92a0c2a57389f98172117eb62fa686777c9c2b55fc90531`


## Content

---
title: "Bypassing DOMPurify with good old XML"
page_title: "Bypassing DOMPurify with good old XML - GMO Flatt Security Research"
url: "https://flatt.tech/research/posts/bypassing-dompurify-with-good-old-xml/"
final_url: "https://flatt.tech/research/posts/bypassing-dompurify-with-good-old-xml/"
authors: ["RyotaK (@ryotkak)"]
programs: ["DOMPurify"]
bugs: ["WAF bypass", "XSS"]
publication_date: "2024-04-01"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 357
---

# Bypassing DOMPurify with good old XML

#####  Posted on April 1, 2024 • 6 minutes • 1164 words 

Table of contents

  * Introduction
  * HTML != XML
  * Taking a look at the patch
  * Confusing nodeName
  * Bypassing DOMPurify with Processing Instructions again
  * Hunting for the another bypass
  * About us

## Introduction

Hello, I’m RyotaK ( [@ryotkak](https://twitter.com/ryotkak) ), a security engineer at Flatt Security Inc.

Recently, [@slonser_](https://twitter.com/slonser_) found [a bypass](https://blog.slonser.info/posts/dompurify-node-type-confusion/) in the DOMPurify when it’s used to sanitize XML documents. After taking a look at the patch, I found two more bypasses of XML/HTML confusion, so I’m documenting it here.

## HTML != XML

As [@slonser_](https://twitter.com/slonser_) wrote in his post, HTML and XML have a bit different parsing rules.  
For example, the following text is parsed as a single node in the XML parser, but the HTML parser recognizes the `h1` tag.
  
  
  <?xml-stylesheet ><h1>Hello</h1> ?>
  

This is because XML defines the structure of Processing Instructions as the following:

<https://www.w3.org/TR/xml/#sec-pi>
  
  
  '<?' PITarget (S (Char* - (Char* '?>' Char*)))? '?>'
  

However, HTML enters the bogus comment state when it encounters `<?`:

<https://html.spec.whatwg.org/#tag-open-state>
  
  
  U+003F QUESTION MARK (?)
  This is an unexpected-question-mark-instead-of-tag-name parse error. Create a comment token whose data is the empty string. Reconsume in the bogus comment state.
  

Because the bogus comment state uses `>` instead of `?>` for the end token, there is a mismatch between how the HTML parser and XML parser parse the Processing Instructions.

<https://html.spec.whatwg.org/#bogus-comment-state>
  
  
  U+003E GREATER-THAN SIGN (>)
  Switch to the data state. Emit the current comment token.
  

Due to this difference, injecting the Processing Instructions allows the sanitizer bypass if the sanitized XML document is later used in the HTML document.  
And as DOMPurify didn’t scan for the Processing Instructions, [@slonser_](https://twitter.com/slonser_) managed to bypass the sanitizer by inserting the following payload:
  
  
  <?xml-stylesheet > <img src=x onerror="alert('DOMPurify bypassed!!!')"> ?>
  

## Taking a look at the patch

To process the Processing Instructions properly, DOMPurify applied the following patch:
  
  
  diff --git a/src/purify.js b/src/purify.js
  index 4594ba09..5b7bc2aa 100644
  --- a/src/purify.js
  +++ b/src/purify.js
  @@ -909,7 +909,10 @@ function createDOMPurify(window = getGlobal()) {
  root.ownerDocument || root,
  root,
  // eslint-disable-next-line no-bitwise
  -  NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_COMMENT | NodeFilter.SHOW_TEXT,
  +  NodeFilter.SHOW_ELEMENT |
  +  NodeFilter.SHOW_COMMENT |
  +  NodeFilter.SHOW_TEXT |
  +  NodeFilter.SHOW_PROCESSING_INSTRUCTION,
  null
  );
  };
  

As the `NodeFilter.SHOW_PROCESSING_INSTRUCTION` option is specified, DOMPurify is now properly scanning the Processing Instruction and removing it if it’s not allowed. So, what could be wrong with this patch?

## Confusing nodeName

It turns out, that the Processing Instruction returns the value specified in the `<?tag` as the `nodeName`.

<https://dom.spec.whatwg.org/#dom-node-nodename>
  
  
  The nodeName getter steps are to return the first matching statement, switching on the interface this implements:
  [...]
  ProcessingInstruction
  Its target.
  

For example, `tag` will be returned when accessing the `nodeName` property of Processing Instruction that can be represented as `<?tag ?>`.

Because DOMPurify highly depends on the `nodeName` of nodes to determine whether the node is allowed, this causes confusion when sanitizing the node:

[src/purify.js line 992-1013](https://github.com/cure53/DOMPurify/blob/fcb9dbd9a935d91e1a087b5ee721da1c6b008790/src/purify.js#L992-L1013)
  
  
  /* Now let's check the element's type and name */
  const tagName = transformCaseFunc(currentNode.nodeName);
  [...]
  /* Remove element if anything forbids its presence */
  if (!ALLOWED_TAGS[tagName] || FORBID_TAGS[tagName]) {
  

## Bypassing DOMPurify with Processing Instructions again

We can use the arbitrary nodeName with Processing Instructions, so what we have to do is create Processing Instructions with an allowed tag name.

For example, the following Processing Instructions bypass the DOMPurify when sanitized as the XML document:
  
  
  <?img a ?>
  

As we saw earlier, HTML and XML have inconsistent parsing for the Processing Instructions.

So, by using the following XML, we can bypass the DOMPurify and execute `alert(1)` if it’s later used in the HTML document:
  
  
  <?img ><img src onerror=alert(1)>?>
  

You can confirm it by using the following script with DOMPurify 3.0.10:
  
  
  document.documentElement.innerHTML = DOMPurify.sanitize("<?img ><img src onerror=alert(1)>?>", {PARSER_MEDIA_TYPE: "application/xhtml+xml"})
  

## Hunting for the another bypass

To prevent the issue mentioned above, the following patch is applied to remove all Processing Instructions.
  
  
  diff --git a/src/purify.js b/src/purify.js
  index 061ba1a8..1d984685 100644
  --- a/src/purify.js
  +++ b/src/purify.js
  @@ -1009,6 +1009,12 @@ function createDOMPurify(window = getGlobal()) {
  return true;
  }
  
  +  /* Remove any ocurrence of processing instructions */
  +  if (currentNode.nodeType === 7) {
  +  _forceRemove(currentNode);
  +  return true;
  +  }
  +
  /* Remove element if anything forbids its presence */
  if (!ALLOWED_TAGS[tagName] || FORBID_TAGS[tagName]) {
  /* Check if we have a custom element to handle */
  

As it completely removes Processing Instructions, it’s no longer possible to use the parser inconsistency of the Processing Instructions.

But, are there any other inconsistent parsing?

After reading the specification of XML, I noticed that there is an interesting section:

<https://www.w3.org/TR/xml/#sec-cdata-sect>
  
  
  CDATA sections may occur anywhere character data may occur; they are used to escape blocks of text containing characters that would otherwise be recognized as markup. CDATA sections begin with the string " <![CDATA[ " and end with the string " ]]> "
  

Luckily for me, the CDATA section has a separate NodeFilter option, which wasn’t enabled on DOMPurify.

<https://dom.spec.whatwg.org/#callbackdef-nodefilter>
  
  
  const unsigned long SHOW_CDATA_SECTION = 0x8;
  

So, what I had to do was find the inconsistency between XML and HTML parsers.

At first glance, the HTML parser seems to be parsing a CDATA section in a way compatible with XML:

<https://html.spec.whatwg.org/#cdata-sections>
  
  
  CDATA sections must consist of the following components, in this order:
  1. The string "<![CDATA[".
  2. Optionally, text, with the additional restriction that the text must not contain the string "]]>".
  3. The string "]]>".
  

However, upon further investigation, it turns out HTML only supports the CDATA section inside the SVG and MathML namespace, and not in the HTML namespace.

<https://html.spec.whatwg.org/#markup-declaration-open-state>
  
  
  The string "[CDATA[" (the five uppercase letters "CDATA" with a U+005B LEFT SQUARE BRACKET character before and after)
  Consume those characters. If there is an adjusted current node and it is not an element in the HTML namespace, then switch to the CDATA section state. Otherwise, this is a cdata-in-html-content parse error. Create a comment token whose data is the "[CDATA[" string. Switch to the bogus comment state.
  

If the CDATA section appears in the HTML namespace, it switches to the bogus comment state, which uses `>` instead of `]]>` for the end token.

<https://html.spec.whatwg.org/#bogus-comment-state>
  
  
  U+003E GREATER-THAN SIGN (>)
  Switch to the data state. Emit the current comment token.
  

So, similar to the Processing Instructions, the following XML creates the `h1` tag when parsed with an HTML parser:
  
  
  <![CDATA[ ><h1>Hello</h1> ]]>
  

As with the Processing Instructions, this inconsistency allows the DOMPurify bypass with the following payload:
  
  
  <![CDATA[ ><img src onerror=alert(1)> ]]>
  

You can confirm it by using the following script with DOMPurify 3.0.11:
  
  
  document.documentElement.innerHTML = DOMPurify.sanitize("<![CDATA[ ><img src onerror=alert(1)> ]]>", {PARSER_MEDIA_TYPE: "application/xhtml+xml"})
  

To fix this inconsistency, DOMPurify applied the following patch:
  
  
  diff --git a/src/purify.js b/src/purify.js
  index 1d984685..72c925a0 100644
  --- a/src/purify.js
  +++ b/src/purify.js
  @@ -913,7 +913,8 @@ function createDOMPurify(window = getGlobal()) {
  NodeFilter.SHOW_ELEMENT |
  NodeFilter.SHOW_COMMENT |
  NodeFilter.SHOW_TEXT |
  -  NodeFilter.SHOW_PROCESSING_INSTRUCTION,
  +  NodeFilter.SHOW_PROCESSING_INSTRUCTION |
  +  NodeFilter.SHOW_CDATA_SECTION,
  null
  );
  };
  

Since the CDATA section has `#cdata-section` as the `nodeName`, this patch can’t be bypassed in the way that I did for the Processing Instructions, unless `#cdata-section` is explicitly allowed.

<https://dom.spec.whatwg.org/#dom-node-nodename>
  
  
  The nodeName getter steps are to return the first matching statement, switching on the interface this implements:
  [...]
  CDATASection
  "#cdata-section".
  

## About us

Flatt Security Inc. provides security assessment services. We are willing to have offers from overseas. If you have any questions, please contact us at <https://flatt.tech/en/> .

Thank you for reading this article.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-21_xss-in-hidden-input-field.md
original_filename: 2022-02-21_xss-in-hidden-input-field.md
title: XSS in hidden input field
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
raw_sha256: 6786c642b9ac5dff12b60b97fdc94d16470443ea4fb0363a66c5466a33fa17de
text_sha256: 1a6e5d6ed75ca132937ccc589304dcc22349cf4b1fdd5fb5c24188cef1cb6f9c
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in hidden input field

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-21_xss-in-hidden-input-field.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `6786c642b9ac5dff12b60b97fdc94d16470443ea4fb0363a66c5466a33fa17de`
- Text SHA256: `1a6e5d6ed75ca132937ccc589304dcc22349cf4b1fdd5fb5c24188cef1cb6f9c`


## Content

---
title: "XSS in hidden input field"
url: "https://f4t7.medium.com/xss-in-hidden-input-field-1b98a5fece26"
authors: ["Faizan Elahi"]
bugs: ["XSS"]
publication_date: "2022-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2882
scraped_via: "browseros"
---

# XSS in hidden input field

1

·

Faizan Elahi
 highlighted

1

·

Faizan Elahi
 highlighted

XSS in hidden input field
Faizan Elahi
Follow
3 min read
·
Feb 21, 2022

141

5

Press enter or click to view image in full size

Hello again! I’m faizan and today I’m writing about an XSS I found in an input field which was hidden from the page using Content division element. If you know what an XSS is, you may skip to the methodology.

What is an XSS?
An XSS (Cross Site Scripting) is a type of Vulnerability where an attacker can inject their own javascript code, making the application think its their own written code and ultimately using it for malicious purposes such as: Stealing their session cookies, credentials, Credit card information, and much more.

What does it mean by Stored XSS?
When the attacker is capable of permanently storing his/her malicious payload/javascript code inside the application server.

Methodology:

Before we dive in. let’s discuss how an input field is hidden from the web page.
There are various ways to hide an input field, from which the two are:

Using type=”hidden” attribute inside an <input> tag.
Putting the <input> tag inside another element and setting its style to display:none

The type=”hidden” can be bypassed if the value is being reflected before the attribute is called inside an <input> tag. i.e.
<input name=”xyz” value=”somevalue” type=”hidden”>

Which can be bypassed by inserting another type attribute as type=”text” i.e.
<input name=”xyz” value=”somevalue” type=”text” type=”hidden”>

This will override the hidden field and you are good to go :)

In my case the <input> tag was inside the <div> element like:

Get Faizan Elahi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<div style=”display:none”>
<input type=”text” value=”somevalue”>
</div>

As the input field was hidden I could not use onmouseover or similar attributes as the input field was not visible.

So I tried the universal attribute which is autofocus which focuses on the input field automatically, then by using onfocus=”alert(document.cookie)”
would do the job. After inserting the payload, It looked something like:

<div style=”display:none”>
<input type=”text” value=”somevalue” autofocus onfocus=”alert(document.cookie)”>
</div>

It was so Happy. I sent the request and opened the browser but there was no luck!

As the <input> tag was hidden it could not be autofocused!

How did I perform the XSS?

After playing around multiple attributes, I came across an attribute called pattern. This attribute is used to compare value and pattern it is same as an if condition, if pattern matches and is valid do something else if invalid do something else. After providing the payload the response looked like this:

<div style=”display:none”>
<input type=”text” value=”somevalue” pattern=”somethingelse” oninvalid=”alert(document.cookie)”>
</div>

I sent the request again and opened the browser, the pop up appeared on the screen!

developers wondering how I got inside 😂

If you know have any other ideas or question leave a comment below!
-Faizan

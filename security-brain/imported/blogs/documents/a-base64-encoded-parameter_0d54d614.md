---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-19_a-base64-encoded-parameter.md
original_filename: 2019-05-19_a-base64-encoded-parameter.md
title: A base64 encoded parameter.
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
raw_sha256: 0d54d614a89c0a01bb8e21a784cb10b34114e10a4cc70bd3e12e8da5003aef4d
text_sha256: 02d85bea5b343da3fdb480475667c62639dafe8688c3c6f34f2cd23d43ed7186
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A base64 encoded parameter.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-19_a-base64-encoded-parameter.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0d54d614a89c0a01bb8e21a784cb10b34114e10a4cc70bd3e12e8da5003aef4d`
- Text SHA256: `02d85bea5b343da3fdb480475667c62639dafe8688c3c6f34f2cd23d43ed7186`


## Content

---
title: "A base64 encoded parameter."
page_title: "A $75 Base64 encoded parameter.. This article is about a parameter which… | by Navneet | Medium"
url: "https://medium.com/@navne3t/a-base64-encoded-parameter-c6fb6b177d68"
authors: ["Navneet (@na5n33t)"]
bugs: ["HTML injection"]
bounty: "75"
publication_date: "2019-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5256
scraped_via: "browseros"
---

# A base64 encoded parameter.

A $75 Base64 encoded parameter.
Navneet
Follow
2 min read
·
May 20, 2019

42

This article is about a parameter which was taking the values not as simple text or HTML code but as encoded base64 string/text. The article below tells what was the bug and how it was submitted ?

It was a first/index page of a Subdomain of a public program ,which was a login page. I was uninterested to look for anything and about to close the page but somehow unintentionally entered the admin/admin in the login page and an error comes up above the login form which says wrong credentials, but the thing that catch my eye was the parameter that comes up at the address bar “errLogin” and the value of the parameter was not simple/plain text.

The link was like

https://www.SomeWebsite.com/? errLogin=[Some_base64_encoded_String]

So, I thought let’s try to enter plain text into parameter , as I entered plain text, some gibberish text gets reflected above the login form where error message was shown.

Now, I thought it can be a XSS bug but the payload was again reflected as gibberish text. Then somehow it came to my mind to decode it as base64.So, I copied the encoded text and try to decode it using some base64decoder website and it shows simple html code like this

<b>Error:</b>Wrong credentials

Now , I wrote simple html code and encoded into base64 then enter it as a value of that parameter and yay! it’s reflected at above the login page where the error message was shown.

I thought this is now can be reflected XSS but I was not able to pop-up the alert box because of filter website have.I tried a lot of payloads but unable to pop up the alert box .

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I don’t want to submit the report without showing any effect. So, I submitted with this below PoC as HTML injection

<a href=’https://www.google.com’ > Register! </a>

the whole link looks like

https://www.SomeWebsite.com/?errLogin=[base64_encoded_injected_HTML]
Submitted Impact:

When user visit above link , and click on the register , he/she will be visited to Google.

Point to note:

If some gibberish text reflects as a result of input in some parameter try to encode it into base64 and try ,may be it works.

Bounty:

This was accepted as valid bug and $75 was rewarded in return and also they said if you are able to submit this as XSS then we can pay you more.

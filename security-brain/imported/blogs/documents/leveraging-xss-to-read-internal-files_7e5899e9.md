---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-09_leveraging-xss-to-read-internal-files.md
original_filename: 2020-10-09_leveraging-xss-to-read-internal-files.md
title: Leveraging XSS to Read Internal Files
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- business-logic
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- business-logic
- mobile-security
language: en
raw_sha256: 7e5899e9fac85c2fb4c0c02c929e41d554030491570762bbc2a158940f8ddc62
text_sha256: 4d5049d208c106e84f0e482156f3135f988fb88cbe25bf9e52472cd839185384
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Leveraging XSS to Read Internal Files

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-09_leveraging-xss-to-read-internal-files.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `7e5899e9fac85c2fb4c0c02c929e41d554030491570762bbc2a158940f8ddc62`
- Text SHA256: `4d5049d208c106e84f0e482156f3135f988fb88cbe25bf9e52472cd839185384`


## Content

---
title: "Leveraging XSS to Read Internal Files"
url: "https://blog.dixitaditya.com/leveraging-xss-to-read-internal-files/"
final_url: "https://blog.dixitaditya.com/xss-to-read-internal-files"
authors: ["Aditya Dixit (@zombie007o)"]
bugs: ["XSS", "LFI"]
publication_date: "2020-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4204
---

# Leveraging XSS to Read Internal Files

UpdatedFebruary 3, 2022

•2 min read•[ __View as Markdown](/xss-to-read-internal-files.md)

![Leveraging XSS to Read Internal Files](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1643881960154%2FnXX8btyTT.png&w=3840&q=75)

[ A](https://hashnode.com/@adityadixit)

[Aditya Dixit](https://hashnode.com/@adityadixit)

[ __](https://twitter.com/zombie007o)[__](https://www.linkedin.com/in/ad17ya/)

I'm leading the Research at Credshields, and Pentest teams at Cobalt Labs and HackerOne. I occasionally blog about my findings and adventures in pentesting.

On this page

BackgroundThe XSS =&gt; LFI

Everybody is familiar with what an XSS is so fast-forwarding it a bit, this is a write-up on how I managed to get an XSS in a PDF generator on an Android application that allowed me to read local files on the system.

## Background

A little background on the target -  
This was a Healthcare related app/pentest which had an android application that they pre-installed in their Android tablets and locked them so filesystem access or any app access was impossible.

It installed a custom launcher that prevented users to change screens or access anything inside, just like the ones you see on a displayed Mobile phone in a mall.

So finding a Local File Read was definitely a critical one because it bypassed the business logic of the application and allowed the attacker to access internal data.

* * *

## The XSS => LFI

Finding Cross-Site scripting in a mobile or any application is not uncommon. These kinds of issues are widespread but the one I got was inside a PDF-generated output.

The application allowed me to edit any patient's records and get a printout of their details. This also allowed me to save the output as a PDF file.

So I tried to enter a normal HTML payload to see if it gets rendered in the generated PDF output.

> `<h1>test</h1>test2`

And I wasn't surprised to see it getting executed.

The next approach which I had seen in some blogs is to check if reading Local files was possible because all of this was happening locally.  
This is the payload that I tried
  
  
  <script>
  x=new XMLHttpRequest;
  x.onload=function(){
  document.write(this.responseText)
  };
  x.open("GET","file:///etc/passwd");
  x.send();
  </script>
  

But for some reason, it didn't work and kept on loading the same page.

Then I tried another payload using `<img>` tags.
  
  
  <img src="xasdasdasd" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>
  

which did not work as well and the app crashed. Maybe it was because of `onerror` or `img`.

So instead of using all the complex payloads, I tried a simple one, i.e.,

![xss](https://imgur.com/TwkRoyL.png)
  
  
  <script>document.write('<iframe src=file:///etc/passwd></iframe>');</scrip>
  

and got an awesome file read in the generated PDF file shown below.

![lfi](https://imgur.com/D2UvZWN.png)

This bypassed the launcher which was prohibiting users to access the system and allowed them to read internal files.

* * *

> _References:_
> 
>  * _<https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/server-side-xss-dynamic-pdf>_
>  * _<https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html>_
> 

[#tutorial](/tag/tutorial)[#security](/tag/security)[#hacking](/tag/hacking)[#android](/tag/android)

 __64K views

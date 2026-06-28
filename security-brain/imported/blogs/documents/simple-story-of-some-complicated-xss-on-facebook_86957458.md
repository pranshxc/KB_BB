---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-21_simple-story-of-some-complicated-xss-on-facebook.md
original_filename: 2020-06-21_simple-story-of-some-complicated-xss-on-facebook.md
title: Simple story of some complicated XSS on Facebook
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- file-upload
- path-traversal
- automation-abuse
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- file-upload
- path-traversal
- automation-abuse
language: en
raw_sha256: 869574587c9551bca2d8411823f1f2976e9124a0474b75e04718debadcb63ff5
text_sha256: 48a37047f8c3c68cc5a9e1f83474ed22bf01a82c20845c8559d726c5b37b387f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Simple story of some complicated XSS on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-21_simple-story-of-some-complicated-xss-on-facebook.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, file-upload, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `869574587c9551bca2d8411823f1f2976e9124a0474b75e04718debadcb63ff5`
- Text SHA256: `48a37047f8c3c68cc5a9e1f83474ed22bf01a82c20845c8559d726c5b37b387f`


## Content

---
title: "Simple story of some complicated XSS on Facebook"
url: "https://medium.com/@win3zz/simple-story-of-some-complicated-xss-on-facebook-8a9c0d80969d"
authors: ["Bipin Jitiya (@win3zz)"]
programs: ["Meta / Facebook"]
bugs: ["Reflected XSS"]
publication_date: "2020-06-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4480
scraped_via: "browseros"
---

# Simple story of some complicated XSS on Facebook

Simple story of some complicated XSS on Facebook
How did I found multiple reflected cross-site scripting (rXSS) vulnerabilities on Facebook
Bipin Jitiya
6 min read
·
Jun 21, 2020

--

2

Hello, World! ❤️

Welcome to my another blog post. I hope you all are doing well and safe. This post is about the reflected cross-site scripting (rXSS) vulnerabilities I found on Facebook. I suggest you read my previous article before reading this one, which is how I found several SSRFs on Facebook server where a vulnerable third-party business intelligence portal (MicroStrategy Web SDK) was deployed. If you read that article first, then, it will be easier to understand.

This post is about some complex rXSS I found on Facebook that was a little difficult to detect and exploit. As already discussed in my previous article, the MicroStrategy Web SDK was hosted on Facebook’s production server. I was looking for file upload functionality, so that I could upload a web shell to the server.

Press enter or click to view image in full size

By enumerating pre-built tasks, I found that the uploadFile task was registered and accessible.

Press enter or click to view image in full size

There was not much documentation available on the MicroStrategy website about this task. So I decided to manually review the source code for this task. I had already downloaded the MicroStrategy Web SDK on my local system, I started looking for the Java class for the uploadFile task.

Press enter or click to view image in full size

I decompiled each jar file of the SDK using the jd-gui tool, and started looking for “com.microstrategy.web.tasks.UploadFileTask” class. I found, the WebTasks.jar file had a class “com.microstrategy.web.tasks.UploadFileTask”.

Press enter or click to view image in full size

I observed that, it supports file upload and its processing functionality. First it will check the fileFieldName URL parameter which should match with the actual filename (which we want to upload). It will then check the file extension, if it happened to be an Excel file (xlsx and xls) it will call the function parseUploadedExcelFile and for other files it will process the file using the parseUploadedFile function.

Press enter or click to view image in full size

parseUploadedExcelFile function first checks for a valid session, so I was unable to upload any Excel file, but parseUploadedFile function did not check for a valid session.

Press enter or click to view image in full size

It did not actually store the uploaded file on the server, instead uploadFile task was used to process the uploaded file from the HTML form and return the contents of the file to client. It was not possible to upload the web shell because it did not store it on the server.

I observed that UploadFileTask class processes data from the uploaded file and renders it without output encoding. This can lead to arbitrary JavaScript code execution under the context of m-nexus.thefacebook.com.

Press enter or click to view image in full size

It was confirmed that reflected cross-site scripting vulnerability exists, but the question was how to exploit it? 🤔
I quickly created a web-page to exploit this XSS.

Press enter or click to view image in full size

Unfortunately I was unable to exploit this because I (as an attacker) cannot control the contents of the file. 😕

Press enter or click to view image in full size

After doing a little research on this, it was confirmed that form based file uploads do not allow attacker to specify file contents.

Press enter or click to view image in full size
https://tools.ietf.org/html/rfc1867

The real challenge comes here. 😨

After many trial and error I created a small HTML + JavaScript code from which I can send a file through a typical POST form and trigger a cross site scripting vulnerability. 😎

Press enter or click to view image in full size

All I need to do is host this file on my server and send its link to the victim, when s/he clicks on the link it will trigger a XSS popup with the domain name.

Press enter or click to view image in full size

Observe HTTP response of vulnerable URL in burp suite proxy tool. HTML/JavaScript code reflect without output encoding

Press enter or click to view image in full size

XSS attacks can allow malicious user to execute scripts on client’s machine which could gather information about the system and send that information to a malicious third-party.

An XSS attack can have potentially serious consequences. An attacker can trick a user to do unintended tasks by manipulating application DOM. After reporting this issue on Facebook, they gave me a very good reward.

Press enter or click to view image in full size
Next story ⏭️

This story is related to the blind SSRF vulnerability that I discussed in my earlier post. As you know I found a wikiScrapper task by enumerating pre-built tasks which used for scraping Wikipedia content. It has a searchString parameter that takes a keyword and extracts/scrape data from Wikipedia.

Press enter or click to view image in full size

I observed that if we provide a string that starts with http:// OR https://, then it extracts data from that website (arbitrary website). It did not encode the data when rendering web content, this determined that the searchString parameter was vulnerable to reflected cross site scripting.

To scrape any web page hosted on an arbitrary domain, there are certain conditions that must be met. The first condition is that it should be an HTML page with all required tags like HTML, BODY and H1. Second, it must contain a table and the table tag must contain at least one wikitable class.

To exploit this, all I had to do was to host a special web-page that met all the above conditions and then pass its link to searchString parameter. I quickly created an HTML code (has XSS payload) and hosted it on HTML Pasta (it allows you to anonymously host your HTML for free)

Press enter or click to view image in full size

Now open this specially created link in the browser and observe XSS pop up with the domain name.

Press enter or click to view image in full size
https://m-nexus.thefacebook.com/servlet/taskProc?taskId=wikiScrapper&taskEnv=html&taskContentType=json&searchString=https://{PASTE_LINK_HERE}&shouldSuggest=false&publicDataSuggestionURL=&publicDataSearchURL=&publicDataPageURL=

Observe HTTP response of vulnerable URL in burp suite proxy tool. HTML/JavaScript code reflect without output encoding.

Press enter or click to view image in full size

After reporting this issue on Facebook they gave me a very good reward.

Conclusion

Similarly I reported 3 more rXSS on Facebook. I received a five-digit bounty for all this XSS. All issues have now been fixed. The m-nexus.thefacebook.com domain is no longer publicly accessible.

I hope you enjoyed the article. Pardon me for my mistakes.
Thanks for reading. Keep learning.
Stay safe and healthy 😇

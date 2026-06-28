---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-10_xss-html-injection-and-file-upload-bypass-in-huawei-subdomain.md
original_filename: 2022-04-10_xss-html-injection-and-file-upload-bypass-in-huawei-subdomain.md
title: XSS | HTML Injection and File Upload Bypass in HUAWEI Subdomain
category: documents
detected_topics:
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- command-injection
- file-upload
language: en
raw_sha256: 36b894f399931169104b57c67fab54eff4be01b5859cefeea0db8bad663142ff
text_sha256: 4ccfbee1c62e0f8981f4c09df1a6fa06ab287348e14c543a829ce1e1ec6eab67
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# XSS | HTML Injection and File Upload Bypass in HUAWEI Subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-10_xss-html-injection-and-file-upload-bypass-in-huawei-subdomain.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `36b894f399931169104b57c67fab54eff4be01b5859cefeea0db8bad663142ff`
- Text SHA256: `4ccfbee1c62e0f8981f4c09df1a6fa06ab287348e14c543a829ce1e1ec6eab67`


## Content

---
title: "XSS | HTML Injection and File Upload Bypass in HUAWEI Subdomain"
url: "https://medium.com/@Bishoo97x/xss-html-injection-and-file-upload-bypass-in-huawei-subdomain-64966ba4f4ac"
authors: ["Ahmed Hassan"]
programs: ["Huawei"]
bugs: ["XSS", "HTML injection"]
publication_date: "2022-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2731
scraped_via: "browseros"
---

# XSS | HTML Injection and File Upload Bypass in HUAWEI Subdomain

XSS | HTML Injection and File Upload Bypass in HUAWEI Subdomain
Ahmed Hassan (Bishoo97x)
Follow
3 min read
·
Apr 11, 2022

81

2

Hi all :) I hope you are all good :)

I started to enumerate all Subdomains of Huawei. But after searching a lot i did not find any low hanging fruits.

But thats no Problem i searched and came across a specific subdomain which is for example redacted.com. After inspecting the Website i could create an Account on this Subdomain. Here i got the Possibility to upload an Avatar or a Profile Picture to complete the Setup of my Account.

So i starting testing File Upload Bypass and uploaded a svg.html File which was including a XSS Cross Site Scripting Payload in case it got accepted.

Get Ahmed Hassan (Bishoo97x)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And suddenly the File was accepted and the File was uploaded and saved on the web server successfully. After that i also tried HTML Code which was able to run and be saved on the Webserver.

Press enter or click to view image in full size

After that i tried to find the Path of the Avatar so i can open it and see if the XSS Payload can run or not. I did this by inspecting the Code in the Document Object Model of Firefox. Lets see if the Javascript Code will run or will be blocked.

Press enter or click to view image in full size

As we can see i could find the exact Path from the Firefox DOM. After that i opend this Path in a new Tab so lets be happy and see the best Output ever on this Day :)

And here we go we got the XSS Output by first of all uploading a svg.html File which includes a Javascript Code.

After this i tried other Files like HTML Injection and PHP Code Files and all of them worked and run too.

Press enter or click to view image in full size

At the End i submitted these Vulnerabilities to Huawei and they accepted all of them and sent me 3 Acknoledgments :). I hope you enjoyed the Writeup and hope to see you reading my next Writeup. :)

Press enter or click to view image in full size

Stay safe and have a nice day :) Bye

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-04_rce-on-starbucks-singapore-and-more-for-5600.md
original_filename: 2021-04-04_rce-on-starbucks-singapore-and-more-for-5600.md
title: RCE on Starbucks Singapore and more for $5600
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
- idor
- file-upload
- rate-limit
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
- idor
- file-upload
- rate-limit
language: en
raw_sha256: 681efb9e07bbb120d01007e795ad3f58be6248ffb982ee3948afc9cf5b1a4a1e
text_sha256: 9204d493a39ed627bcb115c565a3a6642bbe1a3e451f4bf4786c70752dd678b8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# RCE on Starbucks Singapore and more for $5600

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-04_rce-on-starbucks-singapore-and-more-for-5600.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security, idor, file-upload, rate-limit
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `681efb9e07bbb120d01007e795ad3f58be6248ffb982ee3948afc9cf5b1a4a1e`
- Text SHA256: `9204d493a39ed627bcb115c565a3a6642bbe1a3e451f4bf4786c70752dd678b8`


## Content

---
title: "RCE on Starbucks Singapore and more for $5600"
page_title: "RCE on Starbucks Singapore and more for $5600 - Kamil Onur Özkaleli as ko2sec"
url: "http://www.kamilonurozkaleli.com/posts/rce-on-starbucks-singapore-and-more/"
final_url: "http://www.kamilonurozkaleli.com/posts/rce-on-starbucks-singapore-and-more/"
authors: ["Kamil Onur Özkaleli (@ko2sec)"]
programs: ["Starbucks"]
bugs: ["RCE", "Unrestricted file upload"]
bounty: "5,600"
publication_date: "2021-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3765
---

# [Kamil Onur Özkaleli as ko2sec](http://www.kamilonurozkaleli.com/)

## This blog is mostly about security writeups and research articles.

[__](https://github.com/ko2sec "Github")[__](https://twitter.com/ko2sec "Twitter")[__](https://linkedin.com/kamilonurozkaleli "LinkedIn")

  * [Home](/)
  * [All posts](/posts)
  * [Tags](/tags)

# RCE on Starbucks Singapore and more for $5600

Posted at — Apr 3, 2021

### **Recon**

After I found a [critical vulnerability](http://www.kamilonurozkaleli.com/posts/starbucks-singapore-account-takeover/) in Starbucks Singapore web application, I wanted to dig a little deeper and began to examine the **com.starbucks.singapore** Android app. Unfortunately, I did not find any weaknesses in the mobile application and I decided to focus on the [application server](https://mobile.starbucks.com.sg) on which the application interacts. The mobile application was interacting mostly to a REST API on the server, but I noticed that in some operations it is talking to an endpoint with the extension “.aspx”. I did not find any weaknesses in the endpoints here and tried to find more endpoints by directory scanning. I did not find any weaknesses in the endpoints I discovered and took a few weeks off.

### **Recon Harder**

After a few weeks of break, I decided to research IIS vulnerabilities, as I know that the application server is running on IIS. While researching, I came across the [Hacking IIS](https://www.youtube.com/watch?v=HrJW6Y9kHC4) video of [shubs](https://twitter.com/infosec_au). I thank him for reminding me the [IIS Tilde Enumeration Scanner](https://github.com/irsdl/iis-shortname-scanner/tree/master/) by [Soroush Dalili](https://twitter.com/irsdl) in this video, which I knew before but didn’t come to mind during my exploration. I started exploring more endpoints using this tool that automates the vulnerability and caught my attention some “.ashx” endpoints in the “/api” directory.
  
  
  1
  2
  3
  4
  

| 
  
  
  DOWNLO~1.ASH
  EMAIL-~1.ASH
  IMAGEU~1.ASH
  MAILIN~1.ASH
  
  
---|---  
  
The IIS Tilde Enumeration Scanner tool exploits a vulnerability, which Microsoft describes as a feature, discovers the first 6 characters of a file’s name and the first 3 characters of its extension. Based on this information, I tried to find all the file names and quickly found some of them.
  
  
  1
  2
  

| 
  
  
  download.ashx
  email-bounce.ashx
  
  
---|---  
  
Unfortunately I couldn’t use these endpoints for any purpose and focused on the **IMAGEU ~ 1.ASH** endpoint. What did the letter U mean, I wonder if it could be **upload**? I started scanning with the ffuf tool in the form of “imageuploadFUZZ.ashx” and discovered that this endpoint is **imageuploadhandler.ashx**. Looking at the name of the endpoint, it is understood that it is used to upload image files. But there are a few problems here. Is this endpoint accessible to unauthorized users? What is the accepted format of this endpoint while sending a request? Can I upload any files other than image files? If I can upload a file, what is the full path to acces it? Will I be able to run the file?

### **Exploitation**

To find the answers to these questions, I sent random GET/POST requests to this endpoint, but the only response I got was 200 OK nothing more. I did not get any error codes or error/success messages. I wasn’t sure if this endpoint was working. At this point let’s think from the perspective of a developer, you have an endpoint that you use to upload files, how do you send requests to this endpoint from the frontend? Either from within an HTML form or via javascript with an XMLHttpRequest. I started exploring javascript files and found a file named [ajaxfileupload.js](https://mobile.starbucks.com.sg/include/js/ajaxfileupload.js).

![Scheme-1, js file is appending an HTML upload form into page.](/images/starbucks-2-1.png)

As you can see here, the file to be uploaded is sent as “multipart/form-data”. With some extra [research](https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean/28380690#28380690), I found proper upload request format.

![Scheme-2, generic “multipart/form-data” upload request.](/images/starbucks-2-2.png)

At this point, I tried to upload a file with “.aspx” extension containing only text and it was successfully uploaded. Endpoint was converting the filename to UUID format, which would also return the uuid+extension in response. The uploaded file could be found in the “/api” directory.

![Scheme-3, successful upload request and response.](/images/starbucks-2-3.png)

![Scheme-4, browsing uploaded file.](/images/starbucks-2-4.png)

I immediately reported the vulnerability to Starbucks via Hackerone and asked permission to try remote code execution. After getting permission from triager, I uploaded a simple script and ran the “whoami” command and added the output to the report.

![Scheme-3, successfully executed remote code.](/images/starbucks-2-5.png)

### **Impact**

Did you notice something interesting? **whoami** command returns **iis apppool\cards.starbucks.com.hk** , HK is for Hong Kong but we are in Singapore domain. So it was an indicator that I should also check if Hong Kong zone is using same application.

My concerns turned out to be true, Starbucks Hong Kong application server has the same endpoint and the same vulnerability. Then I tried to find other zones using the same application, and I found out that the Starbucks mobile application servers belonging to

  * Singapore
  * Hong Kong
  * Vietnam
  * Thailand
  * Malaysia
  * Cambodia

in total had the same vulnerability and I added them to the report but vulnerabilities belonging to other zones were not rewarded, as only Singapore applications were within the scope.

A malicious person could use this vulnerability to seize the entire server, databases, user information, application source code. He/She could make apps inaccessible or manipulate them however he/she wanted. Considering that the payment systems of mobile applications in Starbucks stores are also located on these servers, much more critical damages could be incurred.

Nov 6th 2020 - Report submitted  
Nov 6th 2020 - Triaged  
Nov 14th 2020 - Rewarded $4200 bounty for 9.1 CVSS score  
Nov 24th 2020 - Rewarded $1400 bounty for increasing CVSS score to 9.8

You can find Hackerone report [here](https://hackerone.com/reports/1027822).  
If you liked this article you can follow me on [Twitter](https://www.twitter.com/ko2sec).

  * [bug bounty](/tags/bug-bounty)
  * [starbucks](/tags/starbucks)

kamilonurozkaleli.com © all rights reserved. | [Ezhil theme](https://github.com/vividvilla/ezhil) | Built with [Hugo](https://gohugo.io)

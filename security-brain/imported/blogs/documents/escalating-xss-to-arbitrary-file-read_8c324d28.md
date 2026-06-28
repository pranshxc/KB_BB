---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-27_escalating-xss-to-arbitrary-file-read.md
original_filename: 2021-06-27_escalating-xss-to-arbitrary-file-read.md
title: Escalating XSS to Arbitrary File Read
category: documents
detected_topics:
- xss
- idor
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: 8c324d2832336549627e69a6f7c95f7edf0365139b0ef758622cb436a0b16eba
text_sha256: 57bb58b2f07b8670a47fb0c9b57ec3cad65f4a6682dce40a50948f6dbc13b315
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating XSS to Arbitrary File Read

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-27_escalating-xss-to-arbitrary-file-read.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `8c324d2832336549627e69a6f7c95f7edf0365139b0ef758622cb436a0b16eba`
- Text SHA256: `57bb58b2f07b8670a47fb0c9b57ec3cad65f4a6682dce40a50948f6dbc13b315`


## Content

---
title: "Escalating XSS to Arbitrary File Read"
page_title: "Escalating XSS to Arbitrary File Read - Pethuraj's Blog"
url: "https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/"
final_url: "https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/"
authors: ["Pethuraj (@Pethuraj)"]
bugs: ["XSS", "LFI"]
publication_date: "2021-06-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3540
---

![Escalating Reflected XSS to Arbitrary File Read \(1\)](https://www.pethuraj.com/blog/wp-content/uploads/2021/06/Escalating-Reflected-XSS-to-Arbitrary-File-Read-1.png)

[Arbitrary File Read](https://www.pethuraj.com/blog/category/arbitrary-file-read/), [XSS](https://www.pethuraj.com/blog/category/xss/)

# Escalating XSS to Arbitrary File Read

[27/06/202118/07/2021](https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/) by [admin](https://www.pethuraj.com/blog/author/admin/)

Hello guys!!  
I am back again with an interesting writeup! This is one of my oldest writeup.  
It is all about how I was able to escalate the XSS vulnerability to read internal files.

I’m not sharing the website details due to confidentiality of the program.

So just like this is a normal web application and it’s functionality is to generate dynamic pages.

Mostly if we find reflected xss vulnerability we all aim to make it stored xss to make severe impact.

This is a web application which lets users to generate dynamic pages and to create and maintain websites. After analysing the website I tried to break it.

Since this is a web application generator page, it have lot of input fields which is stored on to the server. After analysing the application I observed there may be possibility to read internal files.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/06/XSS-payload-1024x285.png)

I tried with XSS payload on one of the text field and found script tags were blocked.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/06/XSS-Blocked-1024x384.png)

So I tried to bypass the xss filter and it was quite easy in this case with appending the Null byte character(%00). And I found it was DOM based XSS vulnerability.

Here’s the blog that helped me to achieve this vulnerability – [_Server Side XSS Vulnerability to Read Internal Files_](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/server-side-xss-dynamic-pdf) and [Local File Read via XSS](https://blog.noob.ninja/local-file-read-via-xss-in-dynamically-generated-pdf/)

I tried with many payloads but no luck then I modified the payload as per the behaviour of the application.

**Payload:**
  
  
  <script%00>
  x=new XMLHttpRequest;
  x.onload=function(){document.write(this.responseText)};
  x.open("GET","file:///etc/passwd");x.send();
  </script%00> 
  
  
  
  

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/06/XSS-to-File-Read-Payload-1024x298.png)

Finally this payload worked and I was able to read the internal files on the pop up and web page as well.

The web page was broken and I was able to read the contents of **etc/passwd** file which is impactful and found to be high severity.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/06/Arbitrary-File-Read-via-XSS-1024x286.png)

For reporting this High severity vulnerability, I was awarded with a bounty [💰](https://emojipedia.org/money-bag/)

**Get in touch with me –**

<https://twitter.com/Pethuraj>  
<https://www.linkedin.com/in/pethu/>

Share on Social Media

[x](https://x.com/share?url=https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/&text=Escalating+XSS+to+Arbitrary+File+Read)[facebook](https://www.facebook.com/sharer.php?u=https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/)[linkedin](https://www.linkedin.com/shareArticle?url=https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/&title=Escalating+XSS+to+Arbitrary+File+Read)[email](mailto:?subject=Escalating+XSS+to+Arbitrary+File+Read&body=https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/)[whatsapp](https://api.whatsapp.com/send?text=Escalating+XSS+to+Arbitrary+File+Read%20https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/)

## Post navigation

[Edmodo Bug Bounty Writeup](https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/)

[United Nations IDOR Vulnerability Writeup](https://www.pethuraj.com/blog/united-nations-bugbounty-writeup/)

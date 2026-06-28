---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-30_remote-code-execution-in-tgz-file-upload.md
original_filename: 2022-01-30_remote-code-execution-in-tgz-file-upload.md
title: Remote Code Execution in .tgz File Upload
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 6470e17d648003afc297bf9beb52be89d1ead0f350a60aad03479c21e51bf51c
text_sha256: 2317a9bfc7d74839959133c6c39ac92611e98ae6d095993aca6d9e5cfb62ea9a
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code Execution in .tgz File Upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-30_remote-code-execution-in-tgz-file-upload.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6470e17d648003afc297bf9beb52be89d1ead0f350a60aad03479c21e51bf51c`
- Text SHA256: `2317a9bfc7d74839959133c6c39ac92611e98ae6d095993aca6d9e5cfb62ea9a`


## Content

---
title: "Remote Code Execution in .tgz File Upload"
page_title: "Remote Code Execution in .tgz File Upload — Machevalia"
url: "https://machevalia.blog/blog/remote-code-execution-in-tgz-file-upload"
final_url: "https://machevalia.blog/blog/remote-code-execution-in-tgz-file-upload"
authors: ["Nick Berrie (@machevalia)"]
bugs: ["RCE", "Unrestricted file upload"]
bounty: "3,100"
publication_date: "2022-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2961
---

# Remote Code Execution in .tgz File Upload

[Bug Bounty](/blog/category/Bug+Bounty)[Write Ups](/blog/category/Write+Ups)

Jan 30

Written By [](/blog?author=63a1076f081fe62c6e3ae37b)

## Insecure Parsing of .tgz Archive Leads to Remote Code Execution

In this write-up, I will be detailing my first remote code execution "RCE" of the year. Often when RCE occurs after a file upload it is due to either 1. a lack of filtering in the file types that can be uploaded or an 2. error in that filtering process for the web form where the file is being uploaded. Many web applications filter file uploads by extension and by MIME-type, often seen in web forms as "content-type". For instance, I have bypassed file upload filters in the past by appending ";.php" to the expected file extension and by changing the content type to the expected file type such as from "_application/x-php_ " to "_image/jpeg_ ". 

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae462/1671497590656/Example_PHP_wAlteredMIME-1.png?format=original)

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae465/1671497590666/Extension_Change_Example-2.png?format=original)

Examples of altered MIME types and appending file extensions

For this specific RCE, the server expected a .tgz file. 

I attempted a few of my favorite file extension and MIME type changes without success. What stuck out to me was how long it took to get the error back in these initial test cases. The server was not doing a simple check on extensions or MIME type and I guessed that since it was expecting a .tgz archive it was unpacking the archive and looking in it before throwing the error. After coming up with this hypothesis I created a .tgz archive with a PHP web shell inside of it. Same result - no dice. This is when I decided to look into exactly what this target expected me to be uploading. The application on the server was expecting a .tgz archive with specifically formated information on atoms and molecules in formats I had never heard of. No worries, I didn't need to become a molecular engineer to find someone else's properly formated archive and take it for my own use. (That's the nice thing about most Universities and many research laboratories - they share everything).

With properly formatted files within a .tgz archive in hand. I unzipped the archive, added a web shell to the archive, repacked it, and then sent it off to the server. This time the archive got unpacked and I could see the files I uploaded in my job's folder with the exception of my web shell...hmm it must have dropped any files it didn't need for processing within the application. Back to the drawing board, I unpacked the archive once more, replaced one of the expected files with a web shell with the same name but the .php file extension. This time the sever threw the upload error again after a short wait. 💡 As Emeril would say, "BAMMMM". I now knew what the application was filtering on - it expected 4 specifically named files in the archive along with specific extensions. Time to put it all together.

![Emeril GIFs - Get the best GIF on GIPHY](https://media0.giphy.com/media/o9ggk5IMcYlKE/giphy.gif)

Knowing that the application expected files with certain names and extensions and that it would drop any additional files somewhere along the way I combined techniques and did this: I unpacked the archive again, added a PHP web shell that was named as expected, and included two extensions. _As an example, I would have changed "FileName123.pdf" to "FileName123.pdf.php"_ The application's logic would hopefully see the first extension and expected name and approve the file for processing while the server would ignore the first extension and only pay attention to my .php extension. It worked - the application accepted my archive, processed the job, and posted my web shell to a job folder that I had access to. At this point, I ran some simple commands to prove access then removed the web shell. 

Unfortunately, there weren't any screenshots I could include that would provide a visual aid to this process since all of my payload changes were occurring within a .tgz archive and the resulting images on the server would reveal too much about the target which cannot be disclosed. So, I do apologize for a lack of imagery but hopefully, my detailed write-up helps you understand how I worked through the problem in front of me to get a nice payout and help the target secure their environment.

The target has since patched this vulnerability by restricting access to the resulting jobs folder and files within. While this does prevent an attacker from accessing the malicious file, it does not help with the filtering logic or prevent an attacker from uploading malicious content to be parsed. It may still be possible to get some sort of malicious action to occur on the server should the application parsing the uploaded files be vulnerable to something. I always recommend that organizations correct the logic in their application if possible over a compensating control. Overall, I was awarded $3100 for this vulnerability. 

[Bug Bounty](/blog/tag/Bug+Bounty)[Write-up](/blog/tag/Write-up)

[ ](/blog?author=63a1076f081fe62c6e3ae37b)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-27_traversing-the-path-to-rce.md
original_filename: 2018-08-27_traversing-the-path-to-rce.md
title: Traversing the Path to RCE
category: documents
detected_topics:
- command-injection
- path-traversal
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- mobile-security
language: en
raw_sha256: 7c9323f5236df375aac16f5c4fc097f06291ed6b574e45163c6f7bd51d774c79
text_sha256: 42e660689ca95cd602fd3716d3e452cb73f663fd583b8990ccd37c15cfda13c6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Traversing the Path to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-27_traversing-the-path-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `7c9323f5236df375aac16f5c4fc097f06291ed6b574e45163c6f7bd51d774c79`
- Text SHA256: `42e660689ca95cd602fd3716d3e452cb73f663fd583b8990ccd37c15cfda13c6`


## Content

---
title: "Traversing the Path to RCE"
page_title: "Traversing the Path to RCE – ∞ Security Blog"
url: "https://blog.hawkeyesecurity.com/2018/08/27/traversing-the-path-to-rce/"
final_url: "https://blog.hawkeyesecurity.com/2018/08/27/traversing-the-path-to-rce/"
authors: ["hawkinsecurity"]
bugs: ["Path traversal", "RCE"]
publication_date: "2018-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5737
---

Posted on [August 27, 2018August 27, 2018](https://blog.hawkeyesecurity.com/2018/08/27/traversing-the-path-to-rce/) by [tghawkins](https://blog.hawkeyesecurity.com/author/tghawkins/)

This post will detail the steps I took to find a path traversal vulnerability, and how I paired the vulnerability with the logic of the application to achieve Remote Code Execution through a shell upload.

I found this while testing a mobile application that has a feature allowing users to upload and encrypt documents to a cloud server, then decrypt the files when the user wants to view their uploaded files. When uploading a file and intercepting the traffic in burpsuite, I saw that the server first checks if the file exists with a given image name.

![1-CheckIfFileExists](https://blog.hawkeyesecurity.com/wp-content/uploads/2018/08/1-checkiffileexists.png?w=1000)

Then after it verifies that the image does not already exist, the server then encrypts the file, and uploads it in the following request, changing the value of the “method” parameter to “writeFile”.

![2-CreateEncryptedFile.png](https://blog.hawkeyesecurity.com/wp-content/uploads/2018/08/2-createencryptedfile.png?w=1000)

Then to read the file, the server just changes the method parameter to “readFile”, specifying the document’s name in the path parameter. The output is the content of the encrypted file.

![3-Display:Read Encrypted File.png](https://blog.hawkeyesecurity.com/wp-content/uploads/2018/08/3-displayread-encrypted-file.png?w=1000)

Since I saw that I could read files using this request, I immediately tried to traverse the “path” parameter in order to read system files. This was the result of traversing for the etc/passwd file.

![4-PathTraversal.png](https://blog.hawkeyesecurity.com/wp-content/uploads/2018/08/4-pathtraversal.png?w=1000)

So now that I could read system files, I also noticed (but did not attempt) that I could also override these files just by changing the “method” parameter value to “writeFile”. I wanted to escalate this to remote code execution, so I tried uploading a php shell to the web root, in the /api/ directory with the following request:

![5-ShellUploadToWebRoot.png](https://blog.hawkeyesecurity.com/wp-content/uploads/2018/08/5-shelluploadtowebroot1.png?w=1000)

As you can see, I’ve traversed the path to upload the shell “da.php” into the “/api/” directory, where the value of the “contents” parameter is the php shell code. Navigating the the url /api/da.php?cmd=id, you can see that the shell upload was successful, and outputs the results from executing the unix “id” command.

The mobile application is listed as in-scope for a private hackerone program, however after reporting this and waiting 3 weeks for a response, they told me that the mobile application itself is in-scope, but not the endpoints that the app communicates with, as it is hosted by the third party developer of the app. Even though it has an impact on all users that upload documents through their app, they still refused to take responsibility for it and changed the scope afterwards to reflect this. Overall a pretty disappointing experience, but still one I can learn from, and hopefully others can too.

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.hawkeyesecurity.com/2018/08/27/traversing-the-path-to-rce/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.hawkeyesecurity.com/2018/08/27/traversing-the-path-to-rce/?share=facebook)
  * 

Like Loading...

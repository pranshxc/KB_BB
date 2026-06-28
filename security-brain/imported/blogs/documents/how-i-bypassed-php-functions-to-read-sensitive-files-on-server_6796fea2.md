---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-04_how-i-bypassed-php-functions-to-read-sensitive-files-on-server.md
original_filename: 2022-02-04_how-i-bypassed-php-functions-to-read-sensitive-files-on-server.md
title: How I bypassed PHP functions to read sensitive files on server
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 6796fea27921e27d0cf7d33a188db8905046e36abf528f2676e3d39eb9c1dc06
text_sha256: 8c7a14c3e5a0c7d7d1cf06da15565c02f435e752f6a66ea0d928d9affa985874
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed PHP functions to read sensitive files on server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-04_how-i-bypassed-php-functions-to-read-sensitive-files-on-server.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6796fea27921e27d0cf7d33a188db8905046e36abf528f2676e3d39eb9c1dc06`
- Text SHA256: `8c7a14c3e5a0c7d7d1cf06da15565c02f435e752f6a66ea0d928d9affa985874`


## Content

---
title: "How I bypassed PHP functions to read sensitive files on server"
page_title: "How I bypassed PHP functions to read sensitive files on server – Kailash"
url: "https://kailashbohara.com.np/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/"
final_url: "https://kailashbohara.com.np/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/"
authors: ["Kailash (@corrupted_brain)"]
bugs: ["Components with known vulnerabilities", "RCE"]
publication_date: "2022-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2938
---

# [How I bypassed PHP functions to read sensitive files on server](https://corrupted-brain.github.io/blog/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/ "How I bypassed PHP functions to read sensitive files on server")

During the penetration testing of a target, the [nuclei](https://github.com/projectdiscovery/nuclei) results show that the website of an organization is vulnerable to code execution vulnerability i.e [CVE-2017-9841](https://blog.ovhcloud.com/cve-2017-9841-what-is-it-and-how-do-we-protect-our-customers/). The CVE-2017-9841 vulnerability lets a user run PHP code on vulnerable websites remotely, by exploiting a breach in PHPUnit lets us run desirable PHP codes and read sensitive files.

After checking all the things, I verified the existence of vulnerability making the proper request in Burp suite, and confirmed by running of the PHP function, `getcwd()` that returns the current working directory.![php getcwd\(\) function](/images/posts/rce1.png) Now there won’t be any problem running system commands by using the `shell_exec()` function in PHP. This function executes user-supplied commands and returns output as a string. I did this by simply listing all the home directories/files of the current user.![](/images/posts/rce2.png) Finally, reading the config file was just easy as reading this post. ![](/images/posts/rce3.png) I stopped over here and thought of reporting this issue to the organization but because of the tight schedule of my daily life I was unable to report the issue for 4-5 days. After a few days I thought of reporting the issue but wanted to confirm whether the vulnerability still exists or not. **But to my surprise 😕 It wasn’t working as before** 😂. ![](/images/posts/rce4.png) As per my guess within 4-5 days, the administrator might have checked the logs or might be aware of the exploit that I tried and made fixation to it. Hence, the execution of `shell_exec()` function was forbidden. However, few other functions could still be executed except shell_exec(). From the image below I confirmed that the execution was forbidden by applying some filter in the phpinfo file.![](/images/posts/rce5.png) Along with shell_exec(), other functions like `show_source()`, `system()`,`shell_exec()`, `exec()`,`popen()` and `proc_open()` which can be used to read/write files were also disabled. After this I started looking for other possible ways to read the files again, and found we can use the [`glob()`](https://www.php.net/manual/en/function.glob.php) method to return an array of filenames and directories. I used following snippet of code locally and confirmed it returns the array of files and directories.
  
  
  <?php
  print_r(glob("*"));
  ?>
  

Eventually, I was able to list the files again as shown below, and now all that’s left is to find a way to read those listed files.![](/images/posts/rce6.png) At the end, I figured out that I had to combine multiple functions together to read files.
  
  
  <?php $a = '../../../../../../../public_html/application/config/database.php';
  $b = explode(',',file_get_contents($a));
  print_r($b); ?>
  

In the above code,

  * $a variable is used to set target file which we are going to read. The target file was found using _print_r(glob())_
  * In the $b variable, we used explode function to return array of strings. _file_get_contents()_ reads contents of database.php from public_html/application/config/database.php and contents array is returned.
  * Finally, printed contents of $b variable using _print_r()_ or _var_dump()_ can also be used. ![](/images/posts/rce7.png)

* * *

#### Share on

  * [__Twitter](https://twitter.com/intent/tweet?text=How I bypassed PHP functions to read sensitive files on server https://corrupted-brain.github.io/blog/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/ "Share on Twitter")
  * [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://corrupted-brain.github.io/blog/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/ "Share on Facebook")
  * [__Google+](https://plus.google.com/share?url=https://corrupted-brain.github.io/blog/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/ "Share on Google Plus")
  * [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://corrupted-brain.github.io/blog/blog/2022/02/04/bypassing-PHP-functions-to-read-system-file-copy/&title=How I bypassed PHP functions to read sensitive files on server&summary=Bypassing file read restriction on an application to achieve Remote Code Execution.&source=https://corrupted-brain.github.io/blog "Share on LinkedIn")

**How I bypassed PHP functions to read sensitive files on server** was published on February 04, 2022.

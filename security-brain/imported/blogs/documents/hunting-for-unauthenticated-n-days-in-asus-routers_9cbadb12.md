---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-30_hunting-for-unauthenticated-n-days-in-asus-routers.md
original_filename: 2024-01-30_hunting-for-unauthenticated-n-days-in-asus-routers.md
title: Hunting for Unauthenticated n-days in Asus Routers
category: documents
detected_topics:
- sso
- command-injection
- csrf
- api-security
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- csrf
- api-security
- supply-chain
language: en
raw_sha256: 9cbadb1244841d74a42ccf7c00721ba827b912c97d244ce039d10a3aee3df660
text_sha256: af208d9750d8eb128b56168a6aa0152226b35548a4af9a693ef34934a0760308
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting for Unauthenticated n-days in Asus Routers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-30_hunting-for-unauthenticated-n-days-in-asus-routers.md
- Source Type: markdown
- Detected Topics: sso, command-injection, csrf, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `9cbadb1244841d74a42ccf7c00721ba827b912c97d244ce039d10a3aee3df660`
- Text SHA256: `af208d9750d8eb128b56168a6aa0152226b35548a4af9a693ef34934a0760308`


## Content

---
title: "Hunting for Unauthenticated n-days in Asus Routers"
page_title: "Shielder - Hunting for <del>Un</del>authenticated n-days in Asus Routers"
url: "https://www.shielder.com/blog/2024/01/hunting-for-~~un~~authenticated-n-days-in-asus-routers/"
final_url: "https://www.shielder.com/blog/2024/01/hunting-for-~~un~~authenticated-n-days-in-asus-routers/"
authors: ["TheZero (@Th3Zer0)", "suidpit (@suidpit)"]
programs: ["Asus"]
bugs: ["RCE", "Format string vulnerability", "Reverse engineering", "Patch diffing"]
publication_date: "2024-01-30"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 483
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/blog/2024/01/hunting-for-~~un~~authenticated-n-days-in-asus-routers/ "ENG") [ITA](https://www.shielder.com/it/blog/2024/01/hunting-for-~~un~~authenticated-n-days-in-asus-routers/ "ITA")

# Hunting for ~~Un~~ authenticated n-days in Asus Routers

## TL;DR

After reading online the details of a few published critical CVEs affecting ASUS routers, we decided to analyze the vulnerable firmware and possibly write an n-day exploit. While we identified the vulnerable piece of code and successfully wrote an exploit to gain RCE, we also discovered that in real-world devices, the _“Unauthenticated Remote”_ property of the reported vulnerability doesn’t hold true, depending on the current configuration of the device.

## Intro

Last year was a great year for IoT and router security. A lot of devices got pwned and a lot of CVEs were released. Since [@suidpit](https://twitter.com/suidpit) and [I](https://github.com/TheZ3ro) love doing research by reversing IoT stuff, and most of those CVEs didn’t have much public details or Proof-of-Concepts yet, we got the chance to apply the [CVE North Stars](https://cve-north-stars.github.io/) approach by [clearbluejar](https://github.com/clearbluejar).

In particular, we selected the following CVEs affecting various Asus SOHO routers:

  * [CVE-2023-39238](https://nvd.nist.gov/vuln/detail/CVE-2023-39238)
  * [CVE-2023-39239](https://nvd.nist.gov/vuln/detail/CVE-2023-39239)
  * [CVE-2023-39240](https://nvd.nist.gov/vuln/detail/CVE-2023-39240)

The claims in the CVEs descriptions were pretty bold, but we recalled some CVEs published months before on the same devices (eg. [CVE-2023-35086](https://nvd.nist.gov/vuln/detail/CVE-2023-35086)) that described other format string in the same exact scenario:

> “An unauthenticated remote attacker can exploit this vulnerability without privilege to perform remote arbitrary code execution”

 _Take**careful** note of those claims cause they will be the base of all our assumptions from now on!_

From the details of the CVEs we can already infer some interesting information, such as the affected devices and versions. The following firmware versions contain patches for each device:

  * Asus RT-AX55: 3.0.0.4.386_51948 or later
  * Asus RT-AX56U_V2: 3.0.0.4.386_51948 or later
  * Asus RT-AC86U: 3.0.0.4.386_51915 or later

Also, we can learn that the vulnerability is supposedly a **format string** , and that the affected modules are `set_iperf3_cli.cgi`, `set_iperf3_srv.cgi`, and `apply.cgi`.

Since we didn’t have any experience with Asus devices, we started by downloading the vulnerable and fixed firmware versions from the vendor’s website.

## Patch Diffing with BinDiff

Once we got hold of the firmware, we proceeded by extracting them using [Unblob](https://github.com/onekey-sec/unblob).

By doing a quick `find`/`ripgrep` search we figured out that the affected modules are not CGI files as one would expect, but they are compiled functions handled inside the `/usr/sbin/httpd` binary.

We then loaded the new and the old httpd binary inside of Ghidra, analyzed them and exported the relevant information with BinDiff’s [BinExport](https://github.com/google/binexport/) to perform a patch diff.

> A patch diff compares a vulnerable version of a binary with a patched one. The intent is to highlight the changes, helping to discover new, missing, and interesting functionality across various versions of a binary.

Patch diffing the `httpd` binary highlights some changes, but none turned out to be interesting to our purpose. In particular, if we take a look at the handlers of the vulnerable CGI modules, we can see that they were not changed at all.

![](/img/blog/asus-bindiff1.png)![](/img/blog/asus-decompiled1.png)

Interestingly, all of them shared a common pattern. The input of the `notify_rc` function was not fixed and was instead coming from the user-controlled JSON request. :money_with_wings:

The `notify_rc` function is defined in `/usr/lib/libshared.so`: this explains why diffing the `httpd` binary was ineffective.

Diffing `libshared.so` resulted in a nice discovery: in the first few lines of the `notify_rc` function, a call to a new function named `validate_rc_service` was added. At this point we were pretty much confident that this function was the one responsible to patch the format string vulnerability.

![](/img/blog/asus-bindiff2.png)![](/img/blog/asus-validaterc1.png)![](/img/blog/asus-validaterc2.png)

The `validate_rc_service` function performs a syntax check on the `rc_service` JSON field. The Ghidra decompiled code is not trivial to read: basically, the function returns **1** if the `rc_service` string contains only alphanumeric, whitespace, or the `_` and `;` characters, while returns **0** otherwise.

Apparently, in our vulnerable firmware, we can exploit the format string vulnerability by controlling what ends up inside the `rc_service` field. We didn’t have a device to confirm this yet, but we didn’t want to spend time and money in case this was a dead-end. Let’s emulate!

## Enter the Dragon, Emulating with Qiling

If you know us, we bet you know that we love [Qiling](https://github.com/qilingframework/qiling/), so our first thought was “What if we try to emulate the firmware with Qiling and reproduce the vulnerability there?”.

Starting from a Qiling skeleton project, sadly `httpd` crashes and reports various errors.

In particular, the Asus devices use an NVRAM peripheral to store many configurations. The folks at [firmadyne](https://github.com/firmadyne/libnvram) developed a library to emulate this behavior, but we couldn’t make it work so we decided to re-implement it inside of our Qiling script.

The script creates a structure in the **heap** and then hijacks all the functions used by `httpd` to read/write the NVRAM redirecting the to the heap structure.

After that we only had to fix some minor syscalls’ implementation and hooks, and _voilà_! We could load the emulated router web interface from our browsers.

![](/img/blog/asus-qiling-emulation.png)

In the meantime we reversed the `do_set_iperf3_srv_cgi`/`do_set_iperf3_cli_cgi` functions to understand what kind of input should we send along the format string.

Turns out the following JSON is all you need to exploit the `set_iperf3_srv.cgi` endpoint:
  
  
  1
  2
  3
  4
  

| 
  
  
  {
  'iperf3_svr_port': '8888',
  'rc_service': '%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p'
  }
  
  
---|---  
  
And we were welcomed with this output in the Qiling console:

![](/img/blog/asus-qiling-formatstring.png)

At this point, the format string vulnerability was confirmed, and we knew how to trigger it via firmware emulation with Qiling. Moreover, we knew that the fix introduced a call to `validate_rc_message` in the `notify_rc` function exported by the `libshared.so` shared library. With the goal of writing a working n-day for a real device, we purchased one of the target devices (**Asus RT-AX55**), and started analyzing the vulnerability to understand the root cause and how to control it.

## Root Cause Analysis

Since the fix was added to the `notify_rc` function, we started by reverse engineering the assembly of that function in the old, vulnerable version. Here follows a snippet of pseudocode from that function:
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  

| 
  
  
  int notify_rc(char *message)
  
  {
  // ...
  pid = getpid();
  psname(pid,proc_name,0x10);
  pid = getpid();
  cprintf("<rc_service> [i:%s] %d:notify_rc %s\n",proc_name,pid,message);
  pid = getpid();
  logmessage_normal("rc_service","%s %d:notify_rc %s",proc_name,pid,message);
  // ...
  }
  
  
---|---  
  
The function seems responsible for logging messages coming from various places through a single, centralized output sink.

The `logmessage_normal` function is part of the same library and its code is quite simple to reverse engineer:
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  

| 
  
  
  void logmessage_normal(char *logname, char *fmt, ...)
  
  {
  char buf [512];
  va_list args;
  va_start(args, fmt);
  
  vsnprintf(buf,0x200,fmt_string,args);
  openlog(logname,0,0);
  syslog(0,buf); // buf can be controlled by the user!
  
  closelog();
  va_end(args);
  return;
  }
  
  
---|---  
  
While Ghidra seems unable to recognize ✨automagically✨ the variable arguments list, the function is a wrapper around `syslog`, and it takes care of opening the chosen log, sending the message and finally closing it.

The vulnerability lies in this function, precisely in the usage of the `syslog` function with a string that can be controller by the attacker. To understand why, let us inspect the signature of it from the libc manual:

`void syslog(int priority, const char *format, ...);`

According to its signature, `syslog` expects a list of arguments that resembles those of the `*printf` family. A quick search shows that, in fact, the function is a known sink for format string vulnerabilities.

## Exploitation - Living Off The ~~Land~~ Process

Format string vulnerabilities are quite useful for attackers, and they usually provide arbitrary read/write primitives. In this scenario, since the output is logged to a system log that is only visible to administrators, we assume an unauthenticated remote attacker should not be able to read the log, thus losing the “read” primitive of the exploit.

ASLR is enabled on the router’s OS, and the mitigation implemented at compile-time for the binary are printed below:
  
  
  Arch:  arm-32-little
  RELRO:  Partial RELRO
  Stack:  No canary found
  NX:  NX enabled
  PIE:  No PIE (0x10000)
  

According to this scenario, a typical way of developing an exploit would consist in finding a good target for a _GOT Overwrite_ , trying to find a function that accepts input controlled by the user and hijacking it to `system`.

Nevertheless, in pure _Living Off The Land_ fashion, we spent some time looking for another approach that wouldn’t corrupt the process internals and would instead leverage the logic already implemented in the binary to obtain something good (namely, a shell).

One of the first things to look for in the binary was a place where the `system` function was called, hoping to find good injection points to direct our powerful write primitive.

Among the multiple results of this search, one snippet of code looked worth more investigation:
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  

| 
  
  
  void sys_script(char *script)
  {
  int cmp;
  char *pcVar1;
  char buf [64];
  char *cmd;
  undefined4 local_10c;
  
  snprintf(buf,0x40,"/tmp/%s",script);
  cmp = strcmp(script,"syscmd.sh");
  if (cmp == 0) {
  if (SystemCmd[0] != '\0') {
  snprintf((char *)&cmd,256,
  "%s > /tmp/syscmd.log 2>&1 && echo \'XU6J03M6\' >> /tmp/syscmd.log &\n",SystemCmd);
  system((char *)&cmd);
  strlcpy(SystemCmd,&DAT_0007e451,0x80);
  return;
  }
  f_write_string("/tmp/syscmd.log",&DAT_0007e451,0);
  return;
  }
  // ...
  }
  
  
---|---  
  
Let’s briefly comment this code to understand the important points:

  * `SystemCmd` is a global variable which holds a string.
  * `sys_script`, when invoked with the `syscmd.s` argument, will pass whatever command is present in `SystemCmd` to the `system` function, and then it will zero out the global variable again.

This seems a good target for the exploit, provided we can, as attackers:

  1. Overwrite the `SystemCmd` content.
  2. Trigger the `sys_script("syscmd.sh")` function.

Point 1 is granted by the format string vulnerability: since the binary is not position-independent, the address of the `SystemCmd` global variable is hardcoded in the binary, so we do not need leaks to write to it. In our vulnerable firmware, the offset for the `SystemCmd` global var is `0x0f3ecc`.

Regarding point 2, some endpoints in the web UI are used to legitimately execute commands through the `sys_script` function. Those endpoints will call the following function named `ej_dump` whenever a GET request is performed:
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  

| 
  
  
  int ej_dump(int eid,FILE *wp,int argc,char **argv)
  
  {
  // ...
  ret = ejArgs(argc,argv,"%s %s",&file,&script);
  if (ret < 2) {
  fputs("Insufficient args\n",wp);
  return -1;
  }
  ret = strcmp(script,"syscmd.sh");
  if (ret == 0) {
  sys_script(script);
  }
  // ...
  }
  
  
---|---  
  
So once the `SystemCmd` global variable is overwritten, simply visiting `Main_Analysis_Content.asp` or `Main_Netstat_Content.asp` will trigger our exploit.

## A Shell for Your Thoughts

We will spare you a [format string exploitation 101](https://owasp.org/www-community/attacks/Format_string_attack), just remember that with `%n` you can write the number of characters written so far at the address pointed by its offset.

It turned out we had a few constraints, some of them typical of format string exploits, while others specific to our scenario.

The _first_ problem is that the payload must be sent inside a JSON object, so **we need to avoid “breaking” the JSON body** , otherwise the parser will raise an error. Luckily, we can use a combination of raw bytes inserted into the body (accepted by the parser), double-encoding (`%25` instead of `%` to inject the format specifiers) and UTF-encode the nullbyte terminating the address (`\u0000`).

The _second_ one is that, after being decoded, our payload is stored in a C string so **null-bytes will terminate** it early. This means we can only have one null-byte and it must be at the end of our format string.

The _third_ one is that there is a **limit on the length** of the format string. We can overcome this by writing few bytes at a time with the `%hn` format.

The _fourth_ one (yes, more problems) is that in the format string there is a **variable number of characters before our input** , so this will mess with the number of characters that `%hn` will count and subsequently write at our target address. This is because the `logmessage_normal` function is called with the process name (either `httpd` or `httpsd`) and the pid (from 1 to 5 characters) as arguments.

Finally, we had our payload ready, everything was polished out perfectly, time to perform the exploit and gain a shell on our device…

![](/img/blog/asus-auth-response.png)

Wait, WAT???

## To Be or Not To Be Authenticated

Sending our payload without any cookie results into a redirect to the login page!

At this point we were completely in shock. The CVEs report “an **unauthenticated remote attacker** ” and our exploit against the Qiling emulator was working fine without any authentication. What went wrong?

While emulating with Qiling before purchasing the real device, we downloaded a dump of the NVRAM state from the internet. If the `httpd` process loaded keys that were not present in the dump, we automatically set them to empty strings and some were manually adjusted in case of explicit crash/Segfault.

It turns out that an important key named `x_Setting` determines **if the router is configured or not**. Based on this, access to most of the CGI endpoints is enabled or disabled. The NVRAM state we used in Qiling contained the `x_Setting` key set to **0** , while our real world device (regularly configured) had it set to **1**.

But **wait** , _there is more!_

We researched on the previously reported format string CVEs affecting the other endpoints, to test them against our setup. We found exploits online setting the _Referer_ and _Origin_ headers to the target host, while others work by sending plain GET requests instead of POST ones with a JSON body. Finally, to reproduce as accurately as possible their setup we even emulated other devices’ firmware (eg. the _Asus RT-AX86U_ one).

**None of them worked** against an environment that had `x_Setting=1` in the NVRAM.

And you know what? If the router is not configured, the WAN interface is not exposed remotely, making it unaccessible for attackers.

## Conclusions

This research left a bitter taste in our mouths.

At this point the chances are:

  1. There is an extra authentication bypass vulnerability that is still not fixed 👀 and thus it does not appear in the diffs.
  2. The “unauthenticated remote attacker” mentioned in the CVEs refer to a **CSRF-like scenario**.
  3. All the previous researchers found the vulnerabilities by emulating the firmware without taking in consideration the NVRAM content.

Anyway, we are publishing our PoC exploit code and the Qiling emulator script in our [poc repository on GitHub](https://github.com/ShielderSec/poc/tree/main/CVE-2023-39238).

![](/img/blog/asus-fmt-exploit.png)

If you know about an (un)fixed authentication-bypass (😉) in Asus devices drop us a message on [X (formerly Twitter)](https://x.com/ShielderSec) or [BlueSky](https://bsky.app/profile/shielder.com). We would also love to hear a comment from Asus and/or from the researchers that reported the CVEs about their reasoning and considerations.

## Pitch 🗣

Are you developing embedded / IoT systems? Take security seriously! We can help you doing [full-stack security testing](https://www.shielder.com/services/iot-security/) from glitching your Secure Boot checks up to gaining code execution on your MQTT server. [Get in touch](https://www.shielder.com/contacts/) with us to learn more.

__ 12 min

Date

30 January 2024

 __[RCE](/tags/rce "RCE") [NDay](/tags/nday "NDay") [CVE](/tags/cve "CVE") [Exploit](/tags/exploit "Exploit") [Writeup](/tags/writeup "Writeup")

Author

[thezero](/authors/thezero "thezero")

[ __](https://github.com/TheZ3ro "thezero GitHub profile")

Security Researcher and Senior Penetration Tester at Shielder.  
In the office I’m the one with the soldering iron.

Author

[suidpit](/authors/suidpit "suidpit")

[ __](https://twitter.com/suidpit "suidpit Twitter profile")[__](https://github.com/suidpit "suidpit GitHub profile")

Security Researcher and Penetration Tester at Shielder. Human, Chaotic Good. Disciple of Bushido & Disney.

Previous post

[CVE-2023-33466 - Exploiting Healthcare Servers with Polyglot Files](https://www.shielder.com/blog/2023/10/cve-2023-33466-exploiting-healthcare-servers-with-polyglot-files/ "CVE-2023-33466 - Exploiting Healthcare Servers with Polyglot Files")

Next post

[Bref Security Audit](https://www.shielder.com/blog/2024/03/bref-security-audit/ "Bref Security Audit")

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")

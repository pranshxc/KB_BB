---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-09_the-silent-spy-among-us-modern-attacks-against-smart-intercoms.md
original_filename: 2023-03-09_the-silent-spy-among-us-modern-attacks-against-smart-intercoms.md
title: 'The Silent Spy Among Us: Modern Attacks Against Smart Intercoms'
category: documents
detected_topics:
- command-injection
- access-control
- mobile-security
- sso
- file-upload
- mfa
tags:
- imported
- documents
- command-injection
- access-control
- mobile-security
- sso
- file-upload
- mfa
language: en
raw_sha256: 89d77fdac2e7f4d28bfa00b8fdf8b00a306139d9673ccf554e394d8b2f833f68
text_sha256: f3a49e9f7fa58d35343f21bdd4f4e2576aec7326d5776d70126629ab4e58c82d
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# The Silent Spy Among Us: Modern Attacks Against Smart Intercoms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-09_the-silent-spy-among-us-modern-attacks-against-smart-intercoms.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, mobile-security, sso, file-upload, mfa
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `89d77fdac2e7f4d28bfa00b8fdf8b00a306139d9673ccf554e394d8b2f833f68`
- Text SHA256: `f3a49e9f7fa58d35343f21bdd4f4e2576aec7326d5776d70126629ab4e58c82d`


## Content

---
title: "The Silent Spy Among Us: Modern Attacks Against Smart Intercoms"
page_title: "The Silent Spy Among Us: Smart Intercom Attacks | Claroty"
url: "https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms"
final_url: "https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms"
authors: ["Claroty's Team82 (@Claroty)"]
programs: ["Akuvox"]
bugs: ["IoT", "OS command injection", "Missing authentication", "MiTM", "SIP"]
publication_date: "2023-03-09"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1404
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# The Silent Spy Among Us: Smart Intercom Attacks

Vera Mens 

/ March 9th, 2023

![The Silent Spy Among Us: Smart Intercom Attacks](/img/asset/YXNzZXRzL2ltYWdlNDctMTY3ODI5ODY3OC5wbmc/image47-1678298678.png?fm=webp&fit=crop&w=800&h=450&s=2d3611cb29026cd377a950296a6d852b)

**UPDATE, March 13:**

Akuvox has reached out to Team82 informing us that it has confirmed the 13 vulnerabilities we uncovered in the E11 smart intercom, and said it will update firmware for these devices before March 20. 

In a statement to customers and partners emailed to Team82, Akuvox said:

“We noticed a recent research report about Akuvox E11 vulnerabilities from Claroty and relevant media coverages. Once we confirmed the existence of the vulnerabilities, we have given the top priority to patch the vulnerabilities. An updated firmware will be released before March 20, 2023 and be available on the Akuvox Knowledge Base.

“Additionally, Akuvox strictly complies with the laws and regulations in all countries and regions where we operate and is committed to continuously enhancing product security to meet the most stringent requirements and to best protect the users of our products.”

\--

What started out as a journey to learn more about a new smart intercom inside the Claroty offices turned into an expansive Team82 research project that uncovered 13 vulnerabilities in the popular Akuvox E11. The vulnerabilities could allow attackers to execute code remotely in order to activate and control the device’s camera and microphone, steal video and images, or gain a network foothold. 

### Table of Contents

  1. Vulnerabilities and their main attack vectors

  2. Our Research Journey

  3. Explore the Firmware

  4. Akuvox Web Server Emulation

  5. Vulnerability Research: Local Environment

  6. Unprotected Routes

  7. Command Injection for Easy Pwn

  8. Vulnerability Research: Cloud Environment

  9. SIP and Cross-Account Abuse

  10. Mitigations

  11. CVEs

#### Vulnerabilities and their main attack vectors:

  1. Remote code execution within the local area network

  2. Remote activation of the device’s camera and microphone and transmission of data back to the attacker

  3. Access to an external, insecure FTP server and the download of stored images and data

The vulnerabilities remain unpatched after many unsuccessful attempts to contact and coordinate the disclosure with the Chinese vendor, a global leader in SIP-based smart intercoms. Our efforts to reach Akuvox began in January 2022, and along the way several support tickets were opened by Team82 and immediately closed by the vendor before our account was ultimately blocked on Jan. 27, 2022. 

We involved the CERT Coordination Center (CERT/CC), which also made multiple attempts to contact the vendor to no avail. After months of failed attempts, we disclosed our findings to CISA in December; CISA also had no success in working with Akuvox, and today published an [advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-23-068-01) describing 13 vulnerabilities found by Team82. The implications of those flaws range from missing authentication, hard-coded encryption keys, missing or improper authorization, and the exposure of sensitive information to unauthorized users. 

## Our Research Journey

### Open Sesame

Last year, as Claroty’s business grew, so did the number of its employees. Very soon our startup-size offices were too small and we had to move to others. When we arrived at our shiny new offices, something new greeted us at the door: an Akuvox E11 smart intercom.

A new door phone is not very exciting for most people, but we are security researchers; we see a camera attached to an ethernet cable and our heart pumps faster.

Our first notion in poking around this new connected device was to figure out if this could make our team’s life simpler. For example, having our research space near the closest office entrance meant that we’d spend a lot of time getting up from our desk letting people in if the receptionist wasn’t around—not fun. 

We decided to look for an API that we could use to open the door; given this is a smart intercom, there must be one. Fortunately, we didn’t have to dig too deeply; it was right in the documentation:

![Unlock Door Instructions](/img/asset/YXNzZXRzL2ltYWdlMjIucG5n/image22.png?fm=webp&fit=crop&s=96c42d7094a7a25805930b90b7d8eec2) __ An API that allows users to remotely unlock doors secured by Akuvox E11 devices.

So we could use an API that takes credentials for authentication and an action which in our case would be to open the door: [http://IP/fcgi/do?action=OpenDoor&UserName=XXX&Password=***REDACTED*** there, we were able to write a simple Slack bot using this API and never have to get up out of our chairs again.

![Clarobot Interface](/img/asset/YXNzZXRzL2ltYWdlNDcucG5n/image47.png?fm=webp&fit=crop&s=bfa1cb360047cf2e4fac2ca3422dd8e4) __ A view of the Slack bot written by Team82 using the Akuvox API. 

Naturally, our curiosity wasn’t satisfied, and we wanted answers to more questions, such as: Are all Akuvox API calls protected by a username and password? What other actions can be performed?

To find out, and rather than brick a production device and anger our IT department, we bought our own device.

![Akuvox Intercom eBay](/img/asset/YXNzZXRzL2ltYWdlMjQucG5n/image24.png?fm=webp&fit=crop&s=54ba020555f85b8f504cb04e848acd07) __ Team82 purchased an Akuvox E11 to conduct its research. 

### Explore the Firmware

While we waited for the physical device to arrive, we were able to download the firmware online:

![Akuvox Firmware](/img/asset/YXNzZXRzL2ltYWdlNDAucG5n/image40.png?fm=webp&fit=crop&s=a7ac6a0de8c7da6b26827c37a4762f7b) __

We discovered the firmware was not encrypted, which meant we could export it with the binwalk utility:

![binwalk E11 firmware](/img/asset/YXNzZXRzL2ltYWdlNTAucG5n/image50.png?fm=webp&fit=crop&s=3c8b245643ed588c35748a57fc1e6565) __

Let’s extract it and see what we could find:

![firmware](/img/asset/YXNzZXRzL2ltYWdlNi0xNjc4Mjk1OTA2LnBuZw/image6-1678295906.png?fm=webp&fit=crop&s=2a81cc42a57ca3709f98c834abdce5e6) __ ![squashfs root](/img/asset/YXNzZXRzL2ltYWdlMi0xNjc4Mjk1OTIzLnBuZw/image2-1678295923.png?fm=webp&fit=crop&s=0ccd9a44289df48859f7728d64ab10ba) __

First, was a [squash-fs](https://en.wikipedia.org/wiki/SquashFS) partition with Linux-like directory structure, which simplified our ability to emulate and review the firmware. 

Our next step was to find its main services. The best candidate was the local web server, which would allow us to discover where configurations reside (because we could follow where they are saved), and what actions can be performed on the device.

Usually, the web server is brought up right at initialization making it straightforward to find the configuration and implementation file’s location. Therefore, we looked at the init script directory and searched for interesting scripts and binary executions. Finally, we found in script `init.sh` a `lighttpd` web server initialization process and were able to continue our journey.

![lighttpd web server](/img/asset/YXNzZXRzL2ltYWdlMzQucG5n/image34.png?fm=webp&fit=crop&s=a9d55943d4563ffdaca403d271ab1e3c) __

The web server configuration resides in : `/app/config/web/lighttpd.conf`

By digging more into the configuration files, we learn that the web server uses the [FCGI](https://en.wikipedia.org/wiki/FastCGI) module and the pages are served by `/app/bin/fcgiserver.fcgi`. The implementation of the main functionalities resides in `/app/lib/libservlets.so`.

### Akuvox Web Server Emulation

Since we hadn’t received the physical device yet, but had the binaries of the web server, why not just run and execute them? Akuvox devices, like many other embedded devices, run on ARM-based CPUs. Therefore, we need to use a Raspberry Pi or similar device to run the binaries within the Akuvox firmware. Luckily for us, we always have a couple Raspberry Pis lying around.

![Akuvox Web Server Simulation](/img/asset/YXNzZXRzL2ltYWdlMjcucG5n/image27.png?fm=webp&fit=crop&s=0b1931660c89e0a07f37eff754fc3889) __ A Raspberry Pi used to emulate the Akuvox E11 web server.

Since the web server uses absolute paths for file access, we wouldn’t be able to run the binaries inside the RPi root file system; all of its paths would be relative to the RPi file system. This was solved by using [chroot](https://man7.org/linux/man-pages/man2/chroot.2.html) on the “/” directory of the Akuvox firmware; once inside the chrooted file system, all paths would be relative to the firmware’s file system.

The procedure of chrooting to another file system is always similar, and goes something like this:

`> mkdir $SQUASH_FS/system $SQUASH_FS/proc $SQUASH_FS/dev $SQUASH_FS/tmp`

`> sudo mount -t proc /proc $SQUASH_FS/proc/`

`> sudo mount --rbind /dev $SQUASH_FS/dev/`

`> echo 'export SHELL=/system/bin/sh' >> ./system/etc/mkshrc`

`> sudo chroot . /system/bin/sh`

Now that we were within the Akuvox’s file system, we could bring up the web server:

`> /app/bin/lighttpd -D -f /app/config/web/lighttpd.conf -m /app/lib`

![chrooted filesystem](/img/asset/YXNzZXRzL2ltYWdlMzkucG5n/image39.png?fm=webp&fit=crop&s=dadd4179ff494dbc579144c3f9c33857) __

From there, we were able to browse <http://IP_OF_RPI> and access an Akuvox web interface:

![Akuvox Login](/img/asset/YXNzZXRzL2ltYWdlMTQtMTY3ODI5NjM0MS5wbmc/image14-1678296341.png?fm=webp&fit=crop&s=3cda913fb22c5826756caf39805a60d6) __ The Akuvox web interface. 

## Vulnerability Research: Local Environment

### Starting with the Web

The default password for the local web interface is admin/admin (noted in the intercom’s documentation). Our goal was then to explore the web server and find interesting and unprotected routes. 

![Akuvox Settings](/img/asset/YXNzZXRzL2ltYWdlMS0xNjc4Mjk2Mzk5LnBuZw/image1-1678296399.png?fm=webp&fit=crop&s=de14e28288487e86c0c1dc7cfb755ea4) __

After some poking of the main binary, we found an unprotected route. ([CVE-2023-0354](https://claroty.com/team82/disclosure-dashboard/cve-2023-0354)):

`http://IP/fcgi/do?id=6&id=2&Operation=GetDivContent&DivName=[REDACTED]`

UI screen:

![Akuvox UI Screen](/img/asset/YXNzZXRzL2ltYWdlNDgucG5n/image48.png?fm=webp&fit=crop&s=3bc6cd38133bddfd470f1d288670f8fd) __ ![Akuvox Other Settings](/img/asset/YXNzZXRzL2ltYWdlMjMucG5n/image23.png?fm=webp&fit=crop&s=9e2c1aea7784fe1812bd42010e9039dd) __

This route is used to extract the device configuration, which includes information about the device, and credentials for various services embedded in the configuration:

![Akuvox Cloud Token](/img/asset/YXNzZXRzL2ltYWdlMjEucG5n/image21.png?fm=webp&fit=crop&s=5ffe8f991d06bec90f93beef227f9019) __

The passwords however are encrypted (but not the cloud token):

![Web Login Akuvox](/img/asset/YXNzZXRzL2ltYWdlMTMtMTY3ODI5NjYyMC5wbmc/image13-1678296620.png?fm=webp&fit=crop&s=81a394e2a47362c7e65f192d3010fd4a) __

Let’s see how the encryption is implemented and whether the development team made mistakes that could help us decrypt the passwords:

![ptr to enrypted](/img/asset/YXNzZXRzL2ltYWdlMjgucG5n/image28.png?fm=webp&fit=crop&s=14fe4a78c828616c10ce84cece51c33f) __ libcfg.so: AesAndBase64Encrypt used to encrypt password with a hardcoded key.

We found the password to decrypt the firmware embedded within. 

Despite the function name (aes_decrypt), the encryption is not the AES you are familiar with, but a proprietary cipher ([CVE-2023-0353](https://claroty.com/team82/disclosure-dashboard/cve-2023-0353)). Since the decryption code resides on the firmware, we can use it to decrypt the credentials. (Fraunhofer, a German research organization, reported the issue before this research. Refer [here](https://www.sit.fraunhofer.de/fileadmin/dokumente/CVE/Advisory_Akuvox_R50P.pdf?_=1563787897) for more information.)

Let’s decrypt the password used for web login:

![root snippet](/img/asset/YXNzZXRzL2ltYWdlNDUucG5n/image45.png?fm=webp&fit=crop&s=0968f9610db7cef15de56bf02b3af72a) __

The credentials are admin/admin (as we expected in our newly chrooted environment). That is a cool finding because it means that we have a web authentication bypass for every network accessible device. Using [Censys](https://search.censys.io/) we found about 5,000 of these devices exposed to the internet:

![Censys Host Settings](/img/asset/YXNzZXRzL2ltYWdlMTkucG5n/image19.png?fm=webp&fit=crop&s=79323357747a4a675661ec8be9c51bb1) __

### Unprotected Routes

Another interesting route is the following one, which we redacted:

`http://IP/fcgi/do?id=8&Operation=GetDivContent&DivName=[REDACTED1]`

`http://IP/fcgi/do?id=8&Operation=GetDivContent&DivName=[REDACTED2]`

![PCAP Settings](/img/asset/YXNzZXRzL2ltYWdlOS0xNjc4Mjk2NzgzLnBuZw/image9-1678296783.png?fm=webp&fit=crop&s=ea9afd025a6a6c2700957d2773a193a7) __

Those routes enable network sniffing on the device, and do not require authentication. This is bad by itself, but is even worse since most of the communication to and from the device is not encrypted or properly encrypted, meaning that passwords for services, images and logs are communicated in plain text.

![PCAP](/img/asset/YXNzZXRzL2ltYWdlNDQucG5n/image44.png?fm=webp&fit=crop&s=a7565780235e47a871621d155f96a672) __

Conveniently enough, the generated configuration and PCAP files can be downloaded without authentication as well.

`http://IP/[REDACTED]/config.tgz`

`http://IP/[REDACTED]/phone.pcap`

This information allowed us to capture network activity from the device, see all communication with the cloud, and with local parties. This also allows us to capture SIP calls as well. By decoding the packets, we will be able to recreate the video and the voice that was communicated.

### Command Injection for Easy Pwn

Gaining a web authentication bypass is interesting, but we are researchers. We see a box with ethernet cable attached to it, and we want to run code on it. Therefore, we looked for a vulnerability that allowed us to execute code from the web interface.

Now with the authentication bypass, we have a new broad attack surface available to us and we can explore the routes that do require authentication.

After reviewing most of the route’s implementation, we found a command injection vulnerability ([CVE-2023-0351](https://claroty.com/team82/disclosure-dashboard/cve-2023-0351)) that in the “call log” page:

  
[http://IP/fcgi/do?id=5&id=1:](http://IP/fcgi/do?id=5&id=1)

![AKuvox interface](/img/asset/YXNzZXRzL2ltYWdlMTgucG5n/image18.png?fm=webp&fit=crop&s=aca53ec712a859a53b9af47bfe5b8a8b) __

The actual vulnerability resides in `libservlets.so` library, `CPhoneBookModel::SetContDataByString` function:

![Path not sanitized snippet](/img/asset/YXNzZXRzL2ltYWdlNDMucG5n/image43.png?fm=webp&fit=crop&s=726e46f97017a2fee846cd30aa9b4dc2) __ libservlets.so: command injection in SetContDataByString that parses input data from the user when contact is added to the contact list.

The `system` function executes the following: 

`system("busybox mv /app/resources/www/htdocs/download/FILE_NAME.jpg /mnt/sdcard/profiles/FILE_NAME.jpg")`

The `FILE_NAME` is the filename of the profile picture provided by the user. You cannot see it in the UI because this functionality is hidden, but see it when we look at the implementation.

By reviewing the code, we see that the `FILE_NAME` is not sanitized, so in theory we can pass any string we want and it will be concatenated to the rest of the command to be executed.

There are some limitations:

  1. `FILE_NAME/COMMAND` cannot include backslashes or spaces: This is a no-brainer. We will UTF-8 encode the backslash and execute the command with the [command expansion](https://linuxhint.com/bash_command_expansion/) notation to avoid use of the spaces. Another note, we need somehow to review the output, so we will redirect the output of the command we want to execute to the `“/tmp/download”`; folder which can be accessed from the web at `http://IP/download/FILE.`For example, the command : `id > /tmp/download/id_result `will become: `$(id>$({echo,'\x2f'tmp'\x2f'download'\x2f'id_result}))`

  2. `FILE_NAME/COMMAND.jpg` file must exist in `/app/resources/www/htdocs/download`:

![Access Snippet](/img/asset/YXNzZXRzL2ltYWdlMzcucG5n/image37.png?fm=webp&fit=crop&s=2d69c397d7bc661c3aa45102342ddc32) __

Let's find a place in which we can upload a file to `/app/resources/www/htdocs/download`. 

Luckily we have found an option to upload a JPG file to `ContactProfile` module:

![Post Data](/img/asset/YXNzZXRzL2ltYWdlNDYucG5n/image46.png?fm=webp&fit=crop&s=4efffa9e64e0c9072da4b94885ea3688) __

Fortunately for us, the file upload functionality does not sanitize the filename and it uploaded to `/app/resources/www/htdocs/download`

![Download Snippet](/img/asset/YXNzZXRzL2ltYWdlMy0xNjc4Mjk3MzgyLnBuZw/image3-1678297382.png?fm=webp&fit=crop&s=794865aa893516b59f26f6e9dbc1ae04) __

Now that the file exists, we can issue the request with the command injection:

![Request Snippet](/img/asset/YXNzZXRzL2ltYWdlMTAtMTY3ODI5NzQxMS5wbmc/image10-1678297411.png?fm=webp&fit=crop&s=4c14c97aa30f0bb7532c419b8d7a4997) __

Let's wrapt it all in some Python script:

![POC Git](/img/asset/YXNzZXRzL2ltYWdlMjYucG5n/image26.png?fm=webp&fit=crop&s=93cb8867d29e7487004a7e8e8bc70bf8) __

We can now run an arbitrary code execution on all accessible devices.

### More Unprotected Routes

As a bonus, we have discovered another (well-documented) web interface that shows camera footage in real time—no authentication mechanism is implemented for this interface ([CVE-2023-0349](https://claroty.com/team82/disclosure-dashboard/cve-2023-0349)):

`http://IP:8080/video.cgi`

`http://IP:8080/jpeg.cgi`

`http://IP:8080/picture.cgi`

![Camera Sample](/img/asset/YXNzZXRzL2ltYWdlNS0xNjc4Mjk3NTEyLnBuZw/image5-1678297512.png?fm=webp&fit=crop&s=a35ddbcbff270ab7c7b7aeb2a1910562) __ Team82's personal helper showcasing our just-arrived Akuvox device. ![Live stream Akuvox](/img/asset/YXNzZXRzL2ltYWdlMTcucG5n/image17.png?fm=webp&fit=crop&s=998d0568ea71e1819fc86be42dab395b) __ A snippet from Akuvox documentation demonstrating the live stream feature.

This means that anyone with network access (public or LAN) to the device can use this route to see the real time video captured by the intercom. In sensitive areas such as a healthcare facility, this would be a privacy issue that would violate patient privacy regulations, for example. 

### Discovery Services

Once our Akuvox device arrived, it was time to explore its architecture:

![Interface Checklist](/img/asset/YXNzZXRzL2ltYWdlNy0xNjc4Mjk5MDA0LnBuZw/image7-1678299004.png?fm=webp&fit=crop&s=4cbfbb553a775b190c7db7bab1f9d5d5) __

We’ve already described our findings about the local web configuration server and web interface, now we need to look at its IP Scanner discovery tool.

![IP Scanner Firmware](/img/asset/YXNzZXRzL2ltYWdlMzgucG5n/image38.png?fm=webp&fit=crop&s=99ed98bf36afc9a6f548d2672d68cae8) __

IP scanner is a Windows-based application. The download is available [here](https://knowledge.akuvox.com/). Its purpose is to search the local network for Akuvox devices:

![IP scanner Multicast Request](/img/asset/YXNzZXRzL2ltYWdlNDEucG5n/image41.png?fm=webp&fit=crop&s=cad9e11965642dc5ca870a65940c5597) __

By looking at Wireshark output, we can see that this is not a familiar discovery protocol. In addition, it looks like the payload is encrypted. To understand the protocol structure and how it is encrypted, we must look into either the Windows application or the binary that responds to the protocol at the device itself. We’ve chosen the latter.

First, lets see the encryption implementation:

![MAC & Hard Coded Password](/img/asset/YXNzZXRzL2ltYWdlMjAucG5n/image20.png?fm=webp&fit=crop&s=a46906e3a25f7f3aa26161bcd155d840) __

Once again, we see hard-coded passwords to decrypt the packet data. This time however, a typical AES is used:

![Empty IV](/img/asset/YXNzZXRzL2ltYWdlMzEucG5n/image31.png?fm=webp&fit=crop&s=33e355424962b7d2c400c0fd5d16e62a) __

So we have everything to decrypt the packet contents. Let’s do it:

![FW version](/img/asset/YXNzZXRzL2ltYWdlMTYucG5n/image16.png?fm=webp&fit=crop&s=592acd77922ccff3ddc4149008422d49) __

This is an xml-formatted message. From its structure, it looks like multiple message types exist. Let’s continue with reviewing the binary to see if there are more interesting message types.

Look at this one:

![Command message fail](/img/asset/YXNzZXRzL2ltYWdlMzYucG5n/image36.png?fm=webp&fit=crop&s=747c00d0c184a2b13391c7102fc91864) __

Can it be? A message used for command execution? Without authentication?

We have the code that parses the message, so we can construct it! This is what we came up with:

![Code snippet CliCommand](/img/asset/YXNzZXRzL2ltYWdlOC0xNjc4Mjk3OTQzLnBuZw/image8-1678297943.png?fm=webp&fit=crop&s=726f666d8d7b5086f39d407e068bfa47) __

So we wrote a quick PoC script to send our command via the proprietary protocol.

![POC git](/img/asset/YXNzZXRzL2ltYWdlMjYtMTY3ODI5Nzk4NS5wbmc/image26-1678297985.png?fm=webp&fit=crop&s=ce632c611317da03d6b803df8f130204) __

It works! We have an arbitrary command execution on every device within the local network. Cool.

Let’s move to the cloud. 

## Vulnerability Research: Cloud Environment

#### Pictures and Cloud: What Could Go Wrong?

[SmartPlus](https://play.google.com/store/apps/details?id=com.akuvox.mobile.smartplus&hl=en&gl=US&pli=1), a mobile application, allows a user to control the intercom remotely.

![SmartPlus Interface](/img/asset/YXNzZXRzL2ltYWdlNC0xNjc4Mjk4MDUwLnBuZw/image4-1678298050.png?fm=webp&fit=crop&s=47d5834e9f1fad1fc77ce4d3be9a0c71) __

Another feature is the activities screen:

![Door Logs Acuvox](/img/asset/YXNzZXRzL2ltYWdlMTItMTY3ODI5ODA4MC5wbmc/image12-1678298080.png?fm=webp&fit=crop&s=38d889bcb204e02d402e094d84d426c3) __

We can view all the interesting "activities" within the app through this feature. If enabled, movement near the intercom's camera can be considered activity. As soon as someone walks past the intercom, the device takes a picture and uploads it to a remote address. That’s how we can see all the activities in the app. Of course, our lab intercom isn't connected to a real door and the individuals are my stuffed animals.

Where do those pictures come from and where are they stored?

Remember, there exists a functionality to sniff the traffic on the intercom. By turning it on, we can see what happens when a picture is taken:

![FTP Akuvox](/img/asset/YXNzZXRzL2ltYWdlMzAucG5n/image30.png?fm=webp&fit=crop&s=617234e2e4477ce5dbcd748659704eeb) __

  
Ok, so this is bad…

Every time a door is opened on any Akuvox (door phone) in the world, an image is sent to the company’s FTP server. A single user, “akuvox,” is used and thus, a single password for authentication. In addition, it is stored on the root directory of the server. What is more, the name of the image includes the MAC address which is a device identifier.

Ok maybe it is not that bad. Can we list the directory?

![List Root Directory](/img/asset/YXNzZXRzL2ltYWdlNDkucG5n/image49.png?fm=webp&fit=crop&s=e914b421d112760cf1e6a10d79a7cfbb) __

We can, meaning that an attacker can access the FTP server from any FTP client and see the names of the images that are uploaded, and therefore can download the specific images from the server by name.

## SIP and Cross-Account Abuse

Using the FTP vulnerability, we can see pictures from arbitrary devices, but is it possible to trigger this functionality and turn on specific cameras? Remember, although we have an arbitrary code execution allowing us to take pictures from internet-exposed devices and devices on the local network, what about the devices behind NAT?

The best place to look for the possibility of turning on a specific camera was the Session Initiation Protocol (SIP). SIP is a communication protocol used for real-time communication sessions between two or more participants over IP networks. SIP controls multimedia communication sessions such as voice and video calls, instant messaging, and online games.

SIP is also an open standard protocol and is widely used for voice over IP (VoIP) applications. It operates on a request-response model and is based on a client-server architecture. SIP clients can initiate communication sessions by sending SIP requests to a SIP server, which will then forward the requests to the appropriate destination.

SIP establishes multimedia sessions involving multiple participants through the use of SIP proxies and SIP servers, which manage communication and routing of data between the participants.

This is roughly how it works:

[ ![B2BUA](/img/asset/YXNzZXRzL2ltYWdlMzIucG5n/image32.png?fm=webp&fit=crop&s=132262e4fdd1c703ee7ae4b1ba955f6c) __ Source: Wikipedia ](https://commons.wikimedia.org/wiki/File:SIP-B2BUA-call-flow.png)

One person calls another and they can exchange over IP both voice and video. In the context of the Akuvox E11, and administrator can make a call to an intercom he owns with the mobile app:

![Video to Voice Connection](/img/asset/YXNzZXRzL2ltYWdlMTEtMTY3ODI5ODMxNi5wbmc/image11-1678298316.png?fm=webp&fit=crop&s=15725e406c0125f45a0b34e6bab9c215) __ ![RTP Stream](/img/asset/YXNzZXRzL2ltYWdlMTUtMTY3ODI5ODM0MS5wbmc/image15-1678298341.png?fm=webp&fit=crop&s=5de6734a2fa9536e981494664a0894ee) __

We wanted to know what happens, however, if they call another Akuvox intercom that is not associated with their account?

![SIP call](/img/asset/YXNzZXRzL2ltYWdlMjUucG5n/image25.png?fm=webp&fit=crop&s=1eb4ce6d55ea4e11ad32196cf152c732) __

We tested this using the intercom at our lab and another one at the office entrance. Each intercom is associated with different accounts and different parties. We were, in fact, able to activate the camera and microphone by making a SIP call from the lab’s account to the intercom at the door. 

  
The issue stems from a missing authorization check. The platform does not verify that the caller is the owner of the edge device and therefore, it’s possible to call using SIP to any intercom and as a consequence to get the video and audio feed ([CVE-2023-0348](https://claroty.com/team82/disclosure-dashboard/cve-2023-0348)). This is a similar class of bug as a 2019 [Apple FaceTime vulnerability](https://9to5mac.com/2019/01/28/facetime-bug-hear-audio/) that allowed users to hear audio from the iPhone they were calling before the FaceTime call was accepted.

![SIP account](/img/asset/YXNzZXRzL2ltYWdlMjkucG5n/image29.png?fm=webp&fit=crop&s=d6a70313d17d6dd15e3623deeecdfaee) __

This is where we stopped our research and decided to disclose the vulnerabilities. Unfortunately, the coordination between Team82 and Akuvox did not go as planned, as you can see by the timeline below.

![Task checklist](/img/asset/YXNzZXRzL2ltYWdlMzMtMTY3ODI5ODQ4Ny5wbmc/image33-1678298487.png?fm=webp&fit=crop&s=773d4b015d975627f709d523a97759be) __

Akuvox Disclosure Timeline

  * **Jan. 23, 2022:** Initial disclosure efforts begin; Akuvox has not published a secure email address or product security webpage.

  * **Jan. 24, 2022:** Email sent to support@akuvox.com asking for contact details to disclose vulnerabilities.

  * **Jan. 24, 2022:** Support ticket number #10125 opened

  * **Jan. 25, 2022:** Our support ticket #10125 was closed without explanation

  * **Jan. 26, 2022:** We sent another email to support@akuvox.com and explained we are not seeking a bug bounty, but simply are trying to responsibly disclose vulnerabilities. We also added a high-level description of the vulnerabilities and asked for details on how best we should report to Akuvox.

  * **Jan. 26, 2022:** Another support ticket was opened

  * **Jan. 27, 2022:** The new support ticket was closed again without explanation. In addition, Akuvox blocked our account and we were prevented from opening new tickets.

  * **Jan. 27, 2022:** We submitted a report through CERT/CC

  * **Feb. 8, 2022:** CERT/CC told us they were attempting to contact the vendor

  * **Feb. 22, 2022:** CERT/CC told us multiple attempts to contact the vendor were made without response.

  * **March 3, 2022:** A detailed email was sent to Akuvox explaining we tried to contact them multiple times and elaborated our intent. No response.

  * **March 22, 2022:** CERT/CC recommended we try to contact an email address associated with the FCC ID (/FCC-ID/2AHCR-VPR49G/). We emailed this address and got no response.

  * **Dec. 5, 2022:** The case was transferred to ICS-CERT. They also tried to contact Akuvox with no success.

  * **March. 3, 2022:** ICS-CERT and CERT/CC confirm they made multiple attempts to contact the vendor, but received no response.

  * **March 9, 2023:** public disclosure.

_Note: It seems that Akuvox fixed the FTP server permissions issue. They disabled the ability to list its content so malicious actors could not enumerate files anymore._

## Mitigations

Despite Akuvox’s failure to acknowledge the numerous disclosure attempts made by Team82 and others, we still recommend a number of mitigation measures. 

First would be to ensure an organization’s Akuvox device is not exposed to the internet in order to shut off the current remote attack vector available to threat actors. Administrators would, however, likely lose their ability to remotely interact with the device over the SmartPlus mobile app. 

Within the local area network, organizations are advised to segment and isolate the Akuvox device from the rest of the enterprise network. This prevents any lateral movement an attacker with access to the device might gain. Not only should the device reside on its own network segment, but communication to this segment should be limited to a minimal list of endpoints. Furthermore, only ports needed to configure the device should be opened; we also recommend disabling UDP port 8500 for incoming traffic, as the device’s discovery protocol is not needed. 

Finally, we recommend changing the default password protecting the web interface. Right now the password is weak and included in the documentation to the device, which is publicly available. 

## CVEs

[CVE-2023-0355](https://claroty.com/team82/disclosure-dashboard/cve-2023-0355)

CWE-321: Use of hard-coded cryptographic key 

CVSS v3: 6.5

[CVE-2023-0354](https://claroty.com/team82/disclosure-dashboard/cve-2023-0354)

CWE-306: Missing authentication for critical function

CVSS v3: 9.1

[CVE-2023-0353](https://claroty.com/team82/disclosure-dashboard/cve-2023-0353)

CWE-257: Storing passwords in a recoverable format

CVSS v3: 7.2

[CVE-2023-0352](https://claroty.com/team82/disclosure-dashboard/cve-2023-0352)

CWE-640: Weak password recovery mechanism for forgotten password

CVSS v3: 9.1

[CVE-2023-0351](https://claroty.com/team82/disclosure-dashboard/cve-2023-0351)

CWE-94: Command injection 

CVSS v3: 8.8

[CVE-2023-0350](https://claroty.com/team82/disclosure-dashboard/cve-2023-0350)

CWE-646: Reliance on file name or extension of externally-supplied file 

CVSS v3: 6.5

[CVE-2023-0349](https://claroty.com/team82/disclosure-dashboard/cve-2023-0349)

CWE-862: Missing authorization

CVSS v3: 7.5

[CVE-2023-0348](https://claroty.com/team82/disclosure-dashboard/cve-2023-0348)

CWE-284: Improper access control 

CVSS v3: 7.5

[CVE-2023-0347](https://claroty.com/team82/disclosure-dashboard/cve-2023-0347)

CWE-200: Exposure of sensitive information to an unauthorized actor 

CVSS v3: 7.5

[CVE-2023-0346](https://claroty.com/team82/disclosure-dashboard/cve-2023-0346)

CWE-287: Improper authentication 

CVSS v3: 7.5

[CVE-2023-0345](https://claroty.com/team82/disclosure-dashboard/cve-2023-0345)

CWE-798: Use of hard-coded credentials 

CVSS v3: 9.8

[CVE-2023-0344](https://claroty.com/team82/disclosure-dashboard/cve-2023-0344)

CWE-912: Hidden functionality 

CVSS v3: 9.1

[CVE-2023-0343](https://claroty.com/team82/disclosure-dashboard/cve-2023-0343)

CWE-329: Generation of predictable initialization vector (IV) with cipher block chaining (CBC) mode 

CVSS v3: 6.5

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ Twitter ](https://twitter.com/intent/post?text=The Silent Spy Among Us: Smart Intercom Attacks&url=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ ](mailto:?subject=The Silent Spy Among Us: Smart Intercom Attacks&body=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ Twitter ](https://twitter.com/intent/post?text=The Silent Spy Among Us: Smart Intercom Attacks&url=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) [ __ ](mailto:?subject=The Silent Spy Among Us: Smart Intercom Attacks&body=https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms)

Recent Vulnerability Disclosures

  * ##### [CVE-2026-28256 A Use of Hard-coded, Security-relevant Constants vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28256)
  * ##### [CVE-2026-28255 A Use of Hard-coded Credentials vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 6.8 ](/team82/disclosure-dashboard/cve-2026-28255)
  * ##### [CVE-2026-28254 A Missing Authorization vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to access sensitive information through unprotected APIs. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28254)
  * ##### [CVE-2026-28253 A Memory Allocation with Excessive Size Value vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to cause a denial-of-service condition. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 7.5 ](/team82/disclosure-dashboard/cve-2026-28253)
  * ##### [CVE-2026-28252 A Use of a Broken or Risky Cryptographic Algorithm vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to bypass authentication and gain root-level access to the device. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 8.1 ](/team82/disclosure-dashboard/cve-2026-28252)

Solutions

  * [Claroty xDome Platform](/platform)
  * [Industrial Cybersecurity](/industrial-cybersecurity)
  * [Healthcare Cybersecurity](/healthcare-cybersecurity)
  * [Commercial Cybersecurity](/commercial-cybersecurity)
  * [Public Sector Cybersecurity](/public-sector-cybersecurity)

Threat Research

  * [Team82 Home](/team82)
  * [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard)
  * [Research](/team82/research)
  * [PGP Key](/team82/pgp-key)

Partners

  * [Partners](/partners)
  * [Technology Alliance Partners](/partners/technology-alliances)
  * [Channel Partners](/partners/channel-partners)
  * [Become a Partner](https://portal.claroty.com/#/page/partner-reg)
  * [Partner Login](https://portal.claroty.com/#/page/login)

Resources

  * [Resource Library](/resources)
  * [Blog](/blog)
  * [White Papers](/resources/white-papers)
  * [Reports](/resources/reports)
  * [Case Studies](/resources/case-studies)
  * [Datasheets](/resources/datasheets)
  * [Integration Briefs](/resources/integration-briefs)
  * [Videos](https://www.youtube.com/@claroty20)
  * [Claroty Nexus](https://nexusconnect.io)

Company

  * [About Us](/company)
  * [Careers](/careers)
  * [Leadership](/leadership)
  * [Newsroom](/newsroom)
  * [xCel Enablement & Training](/xcel-enablement-and-training)
  * [Trust Center](/trust)
  * [Customer Experience](/customer-experience)
  * [Events](/event-listing)
  * [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies)
  * [Contact Us](/contact-us)

[ ![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) ](/)

© 2026 Claroty. All rights reserved.

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

[Terms & Conditions](/terms-conditions) / [Privacy Policy](/privacy-policy)

__ Close Modal ![Unlock Door Instructions](/img/asset/YXNzZXRzL2ltYWdlMjIucG5n/image22.png?fm=webp&fit=crop&s=96c42d7094a7a25805930b90b7d8eec2)

__ Close Modal ![Clarobot Interface](/img/asset/YXNzZXRzL2ltYWdlNDcucG5n/image47.png?fm=webp&fit=crop&s=bfa1cb360047cf2e4fac2ca3422dd8e4)

__ Close Modal ![Akuvox Intercom eBay](/img/asset/YXNzZXRzL2ltYWdlMjQucG5n/image24.png?fm=webp&fit=crop&s=54ba020555f85b8f504cb04e848acd07)

__ Close Modal ![Akuvox Firmware](/img/asset/YXNzZXRzL2ltYWdlNDAucG5n/image40.png?fm=webp&fit=crop&s=a7ac6a0de8c7da6b26827c37a4762f7b)

__ Close Modal ![binwalk E11 firmware](/img/asset/YXNzZXRzL2ltYWdlNTAucG5n/image50.png?fm=webp&fit=crop&s=3c8b245643ed588c35748a57fc1e6565)

__ Close Modal ![firmware](/img/asset/YXNzZXRzL2ltYWdlNi0xNjc4Mjk1OTA2LnBuZw/image6-1678295906.png?fm=webp&fit=crop&s=2a81cc42a57ca3709f98c834abdce5e6)

__ Close Modal ![squashfs root](/img/asset/YXNzZXRzL2ltYWdlMi0xNjc4Mjk1OTIzLnBuZw/image2-1678295923.png?fm=webp&fit=crop&s=0ccd9a44289df48859f7728d64ab10ba)

__ Close Modal ![lighttpd web server](/img/asset/YXNzZXRzL2ltYWdlMzQucG5n/image34.png?fm=webp&fit=crop&s=a9d55943d4563ffdaca403d271ab1e3c)

__ Close Modal ![Akuvox Web Server Simulation](/img/asset/YXNzZXRzL2ltYWdlMjcucG5n/image27.png?fm=webp&fit=crop&s=0b1931660c89e0a07f37eff754fc3889)

__ Close Modal ![chrooted filesystem](/img/asset/YXNzZXRzL2ltYWdlMzkucG5n/image39.png?fm=webp&fit=crop&s=dadd4179ff494dbc579144c3f9c33857)

__ Close Modal ![Akuvox Login](/img/asset/YXNzZXRzL2ltYWdlMTQtMTY3ODI5NjM0MS5wbmc/image14-1678296341.png?fm=webp&fit=crop&s=3cda913fb22c5826756caf39805a60d6)

__ Close Modal ![Akuvox Settings](/img/asset/YXNzZXRzL2ltYWdlMS0xNjc4Mjk2Mzk5LnBuZw/image1-1678296399.png?fm=webp&fit=crop&s=de14e28288487e86c0c1dc7cfb755ea4)

__ Close Modal ![Akuvox UI Screen](/img/asset/YXNzZXRzL2ltYWdlNDgucG5n/image48.png?fm=webp&fit=crop&s=3bc6cd38133bddfd470f1d288670f8fd)

__ Close Modal ![Akuvox Other Settings](/img/asset/YXNzZXRzL2ltYWdlMjMucG5n/image23.png?fm=webp&fit=crop&s=9e2c1aea7784fe1812bd42010e9039dd)

__ Close Modal ![Akuvox Cloud Token](/img/asset/YXNzZXRzL2ltYWdlMjEucG5n/image21.png?fm=webp&fit=crop&s=5ffe8f991d06bec90f93beef227f9019)

__ Close Modal ![Web Login Akuvox](/img/asset/YXNzZXRzL2ltYWdlMTMtMTY3ODI5NjYyMC5wbmc/image13-1678296620.png?fm=webp&fit=crop&s=81a394e2a47362c7e65f192d3010fd4a)

__ Close Modal ![ptr to enrypted](/img/asset/YXNzZXRzL2ltYWdlMjgucG5n/image28.png?fm=webp&fit=crop&s=14fe4a78c828616c10ce84cece51c33f)

__ Close Modal ![root snippet](/img/asset/YXNzZXRzL2ltYWdlNDUucG5n/image45.png?fm=webp&fit=crop&s=0968f9610db7cef15de56bf02b3af72a)

__ Close Modal ![Censys Host Settings](/img/asset/YXNzZXRzL2ltYWdlMTkucG5n/image19.png?fm=webp&fit=crop&s=79323357747a4a675661ec8be9c51bb1)

__ Close Modal ![PCAP Settings](/img/asset/YXNzZXRzL2ltYWdlOS0xNjc4Mjk2NzgzLnBuZw/image9-1678296783.png?fm=webp&fit=crop&s=ea9afd025a6a6c2700957d2773a193a7)

__ Close Modal ![PCAP](/img/asset/YXNzZXRzL2ltYWdlNDQucG5n/image44.png?fm=webp&fit=crop&s=a7565780235e47a871621d155f96a672)

__ Close Modal ![AKuvox interface](/img/asset/YXNzZXRzL2ltYWdlMTgucG5n/image18.png?fm=webp&fit=crop&s=aca53ec712a859a53b9af47bfe5b8a8b)

__ Close Modal ![Path not sanitized snippet](/img/asset/YXNzZXRzL2ltYWdlNDMucG5n/image43.png?fm=webp&fit=crop&s=726e46f97017a2fee846cd30aa9b4dc2)

__ Close Modal ![Access Snippet](/img/asset/YXNzZXRzL2ltYWdlMzcucG5n/image37.png?fm=webp&fit=crop&s=2d69c397d7bc661c3aa45102342ddc32)

__ Close Modal ![Post Data](/img/asset/YXNzZXRzL2ltYWdlNDYucG5n/image46.png?fm=webp&fit=crop&s=4efffa9e64e0c9072da4b94885ea3688)

__ Close Modal ![Download Snippet](/img/asset/YXNzZXRzL2ltYWdlMy0xNjc4Mjk3MzgyLnBuZw/image3-1678297382.png?fm=webp&fit=crop&s=794865aa893516b59f26f6e9dbc1ae04)

__ Close Modal ![Request Snippet](/img/asset/YXNzZXRzL2ltYWdlMTAtMTY3ODI5NzQxMS5wbmc/image10-1678297411.png?fm=webp&fit=crop&s=4c14c97aa30f0bb7532c419b8d7a4997)

__ Close Modal ![POC Git](/img/asset/YXNzZXRzL2ltYWdlMjYucG5n/image26.png?fm=webp&fit=crop&s=93cb8867d29e7487004a7e8e8bc70bf8)

__ Close Modal ![Camera Sample](/img/asset/YXNzZXRzL2ltYWdlNS0xNjc4Mjk3NTEyLnBuZw/image5-1678297512.png?fm=webp&fit=crop&s=a35ddbcbff270ab7c7b7aeb2a1910562)

__ Close Modal ![Live stream Akuvox](/img/asset/YXNzZXRzL2ltYWdlMTcucG5n/image17.png?fm=webp&fit=crop&s=998d0568ea71e1819fc86be42dab395b)

__ Close Modal ![Interface Checklist](/img/asset/YXNzZXRzL2ltYWdlNy0xNjc4Mjk5MDA0LnBuZw/image7-1678299004.png?fm=webp&fit=crop&s=4cbfbb553a775b190c7db7bab1f9d5d5)

__ Close Modal ![IP Scanner Firmware](/img/asset/YXNzZXRzL2ltYWdlMzgucG5n/image38.png?fm=webp&fit=crop&s=99ed98bf36afc9a6f548d2672d68cae8)

__ Close Modal ![IP scanner Multicast Request](/img/asset/YXNzZXRzL2ltYWdlNDEucG5n/image41.png?fm=webp&fit=crop&s=cad9e11965642dc5ca870a65940c5597)

__ Close Modal ![MAC & Hard Coded Password](/img/asset/YXNzZXRzL2ltYWdlMjAucG5n/image20.png?fm=webp&fit=crop&s=a46906e3a25f7f3aa26161bcd155d840)

__ Close Modal ![Empty IV](/img/asset/YXNzZXRzL2ltYWdlMzEucG5n/image31.png?fm=webp&fit=crop&s=33e355424962b7d2c400c0fd5d16e62a)

__ Close Modal ![FW version](/img/asset/YXNzZXRzL2ltYWdlMTYucG5n/image16.png?fm=webp&fit=crop&s=592acd77922ccff3ddc4149008422d49)

__ Close Modal ![Command message fail](/img/asset/YXNzZXRzL2ltYWdlMzYucG5n/image36.png?fm=webp&fit=crop&s=747c00d0c184a2b13391c7102fc91864)

__ Close Modal ![Code snippet CliCommand](/img/asset/YXNzZXRzL2ltYWdlOC0xNjc4Mjk3OTQzLnBuZw/image8-1678297943.png?fm=webp&fit=crop&s=726f666d8d7b5086f39d407e068bfa47)

__ Close Modal ![POC git](/img/asset/YXNzZXRzL2ltYWdlMjYtMTY3ODI5Nzk4NS5wbmc/image26-1678297985.png?fm=webp&fit=crop&s=ce632c611317da03d6b803df8f130204)

__ Close Modal ![SmartPlus Interface](/img/asset/YXNzZXRzL2ltYWdlNC0xNjc4Mjk4MDUwLnBuZw/image4-1678298050.png?fm=webp&fit=crop&s=47d5834e9f1fad1fc77ce4d3be9a0c71)

__ Close Modal ![Door Logs Acuvox](/img/asset/YXNzZXRzL2ltYWdlMTItMTY3ODI5ODA4MC5wbmc/image12-1678298080.png?fm=webp&fit=crop&s=38d889bcb204e02d402e094d84d426c3)

__ Close Modal ![FTP Akuvox](/img/asset/YXNzZXRzL2ltYWdlMzAucG5n/image30.png?fm=webp&fit=crop&s=617234e2e4477ce5dbcd748659704eeb)

__ Close Modal ![List Root Directory](/img/asset/YXNzZXRzL2ltYWdlNDkucG5n/image49.png?fm=webp&fit=crop&s=e914b421d112760cf1e6a10d79a7cfbb)

__ Close Modal ![B2BUA](/img/asset/YXNzZXRzL2ltYWdlMzIucG5n/image32.png?fm=webp&fit=crop&s=132262e4fdd1c703ee7ae4b1ba955f6c)

__ Close Modal ![Video to Voice Connection](/img/asset/YXNzZXRzL2ltYWdlMTEtMTY3ODI5ODMxNi5wbmc/image11-1678298316.png?fm=webp&fit=crop&s=15725e406c0125f45a0b34e6bab9c215)

__ Close Modal ![RTP Stream](/img/asset/YXNzZXRzL2ltYWdlMTUtMTY3ODI5ODM0MS5wbmc/image15-1678298341.png?fm=webp&fit=crop&s=5de6734a2fa9536e981494664a0894ee)

__ Close Modal ![SIP call](/img/asset/YXNzZXRzL2ltYWdlMjUucG5n/image25.png?fm=webp&fit=crop&s=1eb4ce6d55ea4e11ad32196cf152c732)

__ Close Modal ![SIP account](/img/asset/YXNzZXRzL2ltYWdlMjkucG5n/image29.png?fm=webp&fit=crop&s=d6a70313d17d6dd15e3623deeecdfaee)

__ Close Modal ![Task checklist](/img/asset/YXNzZXRzL2ltYWdlMzMtMTY3ODI5ODQ4Ny5wbmc/image33-1678298487.png?fm=webp&fit=crop&s=773d4b015d975627f709d523a97759be)

![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) __ Close Menu

  * [Platform](/platform) __

[The Claroty Platform](/platform) [Claroty CPS Protection Program](/cps-protection-program) [Claire, the AI Security Agent](/claire) [Asset Inventory](/platform/asset-inventory) [Exposure Management](/platform/exposure-management) [Network Protection](/platform/network-protection) [Secure Access](/platform/secure-access) [Threat Detection](/platform/threat-detection) [Operational Efficiency](/platform/operational-efficiency) [Integrations](/platform/integrations)

  * [Industries]() __

[Industrial Home](/industrial-cybersecurity) [Industrial Verticals](/industrial-cybersecurity/verticals) [Healthcare Home](/healthcare-cybersecurity) [Commercial Home](/commercial-cybersecurity) [Commercial Verticals](/commercial-cybersecurity/verticals)

  * [Public Sector](/public-sector-cybersecurity) __

[Public Sector Home](/public-sector-cybersecurity) [Federal Government Home](/public-sector-cybersecurity/us-government-cybersecurity) [SLED Home](/public-sector-cybersecurity/sled-government-cybersecurity)

  * [Customers](/customer-experience) __

[Customer Experience](/customer-experience) [Case Studies](/resources/case-studies) [xCel Enablement & Training for Customers](/xcel-enablement-and-training-for-customers)

  * [Partners](/partners) __

[Partners](/partners) [Technology Alliance Partners](/partners/technology-alliances) [Channel Partners](/partners/channel-partners) [Partner Login](https://portal.claroty.com/#/page/login)

  * [Threat Research](/team82) __

[Team82 Home](/team82) [Threat Intelligence](/threat-intelligence) [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard) [Research](/team82/research) [Talks](/team82/talks) [PGP Key](/team82/pgp-key)

  * [Resources](/resources) __

[Blog](/blog) [Reports](/resources/reports) [White Papers](/resources/white-papers) [Datasheets & Solution Overviews](/resources/datasheets) [Integration Briefs](/resources/integration-briefs) [Case Studies](/resources/case-studies) [On-Demand Webinars](/resources/webinars) [Visit our Nexus Website](https://nexusconnect.io)

  * [Company](/company) __

[About Us](/company) [Careers](/careers) [Leadership](/leadership) [Newsroom](/newsroom) [xCel Enablement & Training](/xcel-enablement-and-training) [Trust Center](/trust) [Events](/event-listing) [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies) [Contact Us](/contact-us)

  * [__Search](/search)

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

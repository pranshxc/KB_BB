---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-15_triple-threat-breaking-teltonika-routers-three-ways.md
original_filename: 2023-05-15_triple-threat-breaking-teltonika-routers-three-ways.md
title: 'Triple Threat: Breaking Teltonika Routers Three Ways'
category: documents
detected_topics:
- command-injection
- ssrf
- xss
- cloud-security
- supply-chain
- mfa
tags:
- imported
- documents
- command-injection
- ssrf
- xss
- cloud-security
- supply-chain
- mfa
language: en
raw_sha256: 2c024102953b8efe07ee6ebdc7df574f6a8220134b14e76af570913ea81db8bd
text_sha256: 42b214a3a0d3ce9c476397904103e7679647683621ca3c95a8ae5aaf0072001f
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Triple Threat: Breaking Teltonika Routers Three Ways

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-15_triple-threat-breaking-teltonika-routers-three-ways.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, xss, cloud-security, supply-chain, mfa
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `2c024102953b8efe07ee6ebdc7df574f6a8220134b14e76af570913ea81db8bd`
- Text SHA256: `42b214a3a0d3ce9c476397904103e7679647683621ca3c95a8ae5aaf0072001f`


## Content

---
title: "Triple Threat: Breaking Teltonika Routers Three Ways"
page_title: "Triple Threat: Breaking Teltonika Routers Three Ways | Claroty"
url: "https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways"
final_url: "https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways"
authors: ["Roni Gavrilov", "Noam Moshe"]
programs: ["Teltonika"]
bugs: ["IoT", "RCE", "OS command injection", "SSRF", "XSS"]
publication_date: "2023-05-15"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1154
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# Triple Threat: Breaking Teltonika Routers Three Ways

Noam Moshe, 

Roni Gavrilov-OTORIO 

/ May 15th, 2023

![Triple Threat: Breaking Teltonika Routers Three Ways](/img/asset/YXNzZXRzL3RlbHRvbmlrYS1kaWFncmFtLSgxKS5wbmc/teltonika-diagram-%281%29.png?fm=webp&fit=crop&w=800&h=450&s=e179218bf5182be1f50b474d33b6adc3)

## Executive Summary

  * Comprehensive research was conducted on Teltonika Networks’ IIoT products, with a focus on industrial cellular devices widely used in various industries, specifically, the Teltonika Remote Management System, and RUT model routers. 

  * This research is the result of a collaboration with [OTORIO](https://www.otorio.com/blog/teltonkia-cloud-takeover-vulnerability-exposed/), joining forces for disclosure and resolving major issues in the affected product lines. 

  * The research uncovered eight vulnerabilities, affecting thousands of internet-connected devices worldwide.

  * Multiple attack vectors were identified during the research, including the exploitation of internet-exposed services, cloud account takeover, and cloud infrastructure vulnerabilities.

  * An attacker successfully exploiting these industrial routers and IoT devices can cause a number of impacts on compromised devices and networks, including monitoring network traffic and stealing sensitive data, hijacking internet connections and accessing internal services. 

  * Teltonika Networks mitigated the vulnerabilities in coordination with CISA, which published an [advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-23-131-08) Thursday; CISA's advisory assesses one of the vulnerabilities a CVSS v3 score of 10. 

  * We would like to thank Teltonika Networks for fixing all the reported issues and coordinating closely with us.

## Table of Contents

>  1. Understanding Teltonika Cloud-Based IoT Routers
> 
>  2. Device Identification and Pairing Mechanism
> 
>  3. Compromised Attack Vectors
> 
>  4. Takeover: Unregistered device
> 
>  5. Takeover: Registered device over LAN/WAN
> 
>  6. Information Oracle Vulnerability
> 
>  7. Takeover: Through account takeover
> 
>  8. Abusing User-controlled Subdomains
> 
>  9. Accessing Internal Cloud
> 
>  10. Summary
> 
> 

## Understanding Teltonika Cloud-Based IoT Routers

[Teltonika Networks](https://teltonika-networks.com/) specializes in manufacturing and developing networking devices, including routers, modems and industrial networking equipment. 

The [Teltonika Remote Management System](https://rms.teltonika-networks.com/) (RMS) product is a cloud-based or on-premises platform that enables users to monitor and manage their connected devices from anywhere. The RMS platform provides real-time monitoring and control, making it easier for organizations to track the status and performance of their devices and network. The platform also offers advanced features such as device management, software and firmware updates, GPS tracking, and data visualization. The RMS platform is designed to be scalable and secure, ensuring that businesses of all sizes can benefit from the platform's capabilities.

![Breaking Teltonika Routers Three Ways](/img/asset/YXNzZXRzLzExLmpwZw/11.jpg?fm=webp&fit=crop&s=33283da7e9ec9d129e23619c3f9af73b) __ Teltonika’s RMS platform, enabling remote management of network devices.

Teltonika offers a wide range of network solutions and devices, however we’ve looked at the RUT241 and RUT955 devices in particular. These devices are part of the company’s industrial cellular routers product line and offer 4G LTE, WiFi, and Ethernet communication designed specifically for industrial environments and commercial applications. The RUT241 and RUT955 routers are equipped with advanced network routing and firewall capabilities, various VPN protocols, allowing users to securely connect to their private networks. These routers are also easy to configure and manage, making them suitable for use by businesses of all sizes.

[ ![Teltonika's RUT241 4G router](/img/asset/YXNzZXRzL2ZyLmpwZw/fr.jpg?fm=webp&fit=crop&s=e967f025ef7d1ca7e82639d53db11880) __ Teltonika's RUT241 4G router.  ](https://teltonika-networks.com/products/routers/rut241)

While hundreds of thousands of Teltonika devices are deployed worldwide, a search on internet-scanning engines such as Shodan and Censys also reveals thousands of internet-facing devices, with their management ports externally exposed to the internet.

[ ![Search results for Teltonika devices](/img/asset/YXNzZXRzLzIuanBn/2.jpg?fm=webp&fit=crop&s=02eeba0020ded572b302d9fd2c3abd9f) __ Search results for Teltonika devices using the internet search-engine censys.io.  ](http://censys.io)

## Teltonika Device Identification and Pairing Mechanism

When examining the device identification process in Teltonika’s RMS platform, we noticed that the only two identifiers needed in order to claim and interact with a device are a device serial number (SN) and MAC address. These two identifiers are labeled on the back of every device, and should ensure that only users with physical access to the device can claim it.

![RUT950](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9sYWJlbC5wbmc/teltonika_label.png?fm=webp&fit=crop&s=741abb335627abb0a75aff5d7558ce81) __ A Teltonika RUT router label showing the device’s MAC address and serial number.

Since we did not have our device at that time, we could not progress without research as any vector we wanted to explore required us knowing these two identifiers. Luckily for us, one of the industry trends lately is people uploading an unboxing/tutorial video to YouTube, explaining how to set up the device. In many cases, since users film their device, they are also leaking the device’s secret at the same time, images below.

![RUT950](/img/asset/YXNzZXRzLzMuanBn/3.jpg?fm=webp&fit=crop&s=ee60f78c4dc35afe26190619b59d3932) __ ![RUT950 Unboxing](/img/asset/YXNzZXRzLzQuanBn/4.jpg?fm=webp&fit=crop&s=d5641ac2787b98c056c93ce8ffefb56b) __ ![RUT Unboxing 2](/img/asset/YXNzZXRzLzUuanBn/5.jpg?fm=webp&fit=crop&s=b584bdf06110acdc909397e7efa89309) __

Using these two identifiers, users are able to claim their devices and take control over them. Then, the device authenticates to the cloud using the same identifiers.

![Adding a new PMS Device](/img/asset/YXNzZXRzLzYuanBn/6.jpg?fm=webp&fit=crop&s=ddfbf71cd08837e77d9c87cfdfd76b82) __ The UI used by users to claim their devices, claiming devices by their serial number and MAC address.

## Attack Vectors Used to Compromise Teltonika IIoT

In our mutual research, we have focused on three threat scenarios in which remote attackers are able to compromise the Teltonika cloud-management solution and take full control over unregistered and registered devices. We’ve used different techniques and methods including direct exploitation as well as remote and cloud capabilities to manipulate remote users into compromising their accounts and devices. When exploited, these vulnerabilities could allow attackers full control over Teltonika 4G routers. Attackers could use it as a pivot point to companies’ internal networks, giving access to internal IoT and industrial devices that were never meant to be exposed, putting them at risk.

### Takeover: Unregistered device over the cloud ([CVE-2023-2586](/team82/disclosure-dashboard/cve-2023-2586))

Teltonika RMS cloud-based management platform is vulnerable to an unauthorized attacker registering previously unregistered devices on the RMS, but only if the router’s RMS management feature, which is enabled by default, has not been disabled. This could enable the attacker to perform different operations from the cloud on an unsuspecting user's routers, including remote code execution with root privileges (using the Task Manager feature on RMS).

Attackers can collect the identifiers used for registration in different ways, for example by using shodan.io, register the device to their account and then compromise it. In order to demonstrate how easy it is, we’ve written a python script leveraging the shodan API for discovering Teltonika routers MAC address and serial number. Querying SNMP service of internet exposed devices, we queried the relevant OIDs, providing us with the secret identifiers required for registration. Using this method, we were able to discover hundreds of MAC and serial number pairs.

![Collecting identifiers for registration](/img/asset/YXNzZXRzLzcuanBn/7.jpg?fm=webp&fit=crop&s=83ebac5c9a580da78e7fe601b53053d4) __ Collecting identifiers for registration using shodan.io.

Using the collected identifiers, an attacker could register these devices to his cloud account, if they were not previously registered to any account. Since not all people necessarily use Teltonika RMS to manage their devices, we discovered that many devices are actually connected to the internet but not claimed on Teltonika’s cloud.

After a device is paired to the attacker's cloud account, the Task Manager feature in the cloud platform could allow the attacker to create a task and execute commands on the remote device.

![RMS Task manager feature](/img/asset/YXNzZXRzLzguanBn/8.jpg?fm=webp&fit=crop&s=2a652a0061ec0e8b19e25ef1fa9ef0e3) __ A reverse shell task created using the RMS Task manager feature.

In the example above, we created a reverse shell task using the Task Manager. Running this task on the registered router will result in remote code execution (RCE) with root privileges.

![Remote code execution on RUT955](/img/asset/YXNzZXRzLzkuanBn/9.jpg?fm=webp&fit=crop&s=88b042eeb60bd7bb03b94fcbbbc075f6) __ Remote code execution on RUT955 obtained by using the Task Manager feature. 

### Takeover: Registered device over LAN/WAN

Our next goal in this research project was to understand how devices connect to the cloud, identify themselves, and create a secure communication channel.

![Registered device over LAN/WAN Tavekover](/img/asset/YXNzZXRzLzEwMC5qcGc/100.jpg?fm=webp&fit=crop&s=e7cec96fafb70821820503eb7d3c000f) __

In order to do so, we downloaded, extracted, and reverse engineered the device’s firmware, which is available for [download on Teltonika’s website](https://wiki.teltonika-networks.com/view/RUT240_Firmware_Downloads).

![Teltonika RUT240 router firmware](/img/asset/YXNzZXRzLzExLTE2ODQ5Mjg4OTQuanBn/11-1684928894.jpg?fm=webp&fit=crop&s=3c885241298b70ba4952d36f9597a4bd) __ Teltonika RUT240 router firmware available for download.

The firmware file is a big binary blob, however it contains a SquashFS filesystem inside, along with a kernel image. It is very common for vendors to ship a filesystem in their firmware, including all the files necessary for an upgrade.

![Inside Teltonika’s RUT240 firmware](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9pbnNpZGUtZmlybXdhcmUucG5n/teltonika_inside-firmware.png?fm=webp&fit=crop&s=4116eaa444bc6cbf48c0b03fc786b3fe) __ Inside Teltonika’s RUT240 firmware.

When examining the filesystem inside the firmware upgrade, we discovered some interesting configuration files, setting up configurations for an MQTT broker.

![/etc/config/rms_mqtt](/img/asset/YXNzZXRzLzEzLTE2ODQ5Mjg5NDUuanBn/13-1684928945.jpg?fm=webp&fit=crop&s=e12facba5119741e3c13dbeaf898d583) __ /etc/config/rms_mqtt : a configuration file for the device’s MQTT connection.

MQTT is a pub-sub protocol aimed at allowing remote communication in the form of messages. As part of the MQTT protocol, two different kinds of entities reside: a client which could send and receive messages, and a broker which distributes received messages and routes them to the appropriate clients.

In order to distribute the messages to the correct clients, the broker holds a list of topics - different channels which publishers could send messages to - and in order for a client to receive messages, they need to subscribe to a certain topic. Whenever a message is sent to a specific topic, the broker distributes it to all the users who have subscribed to this topic.

MQTT supports a wide variety of security mechanisms, including encryption, client username/password authentication and even certificate-based authentication. Inside the configuration file we discovered, we saw mentions of certificates and keys that could be used to establish the MQTT connection. There was no actual client certificate and key embedded inside the firmware itself, which meant devices must receive said certificates as part of the cloud connection process.

In order to obtain a device’s certificate and connect to the MQTT broker, we reversed engineered the main binary handling cloud communication: `rms_mqtt`. This binary handles two main things:

  * **Cloud Communication Handshake:** the device connects to the Teltonika RMS cloud server, informing it that the device is online and ready to be managed by the cloud.

  * **MQTT Communication:** the device connects to Teltonika’s MQTT broker and registers to multiple topics in order to send status reports and receive commands from the cloud. During this communication, the device authenticates to the MQTT broker using its private key and certificate.

We discovered that during the initial cloud handshake, devices identify themselves to the cloud and request a private key and certificate for MQTT communication. This is done by sending the device information, including its model, firmware version but most importantly the device’s serial number and MAC address to the cloud.

![MQTT certificate](/img/asset/YXNzZXRzLzE0LmpwZw/14.jpg?fm=webp&fit=crop&s=dc03d24ffc46640e884fa648e109b533) __ A JSON sent by the device in order to identify itself to the cloud and receive an MQTT certificate.

By leaking a device serial number and MAC address, it is possible for attackers to authenticate to Teltonika’s RMS platform and receive a device certificate. Then, using said certificate, it is possible for the attackers to connect to Teltonika’s MQTT broker and communicate on behalf of the device, impersonating it.

This form of device identification and authentication is not secure, since it relies on two inherently weak identifiers: serial number and MAC address. 

The serial number part of the authentication is a sequential number following a certain prefix, and is easily guessable because it consists only of numbers in specific ranges instead of being completely random. Examples:

`1112XXXXX`

`1123XXXXX`

When looking at the MAC part of the authentication, it is flawed as well. Like most other devices, the MAC address of Teltonika devices is composed of two different parts: three bytes of the organizationally unique identifier (OUI) and three unique bytes of the specific device.

An example MAC address could look like this, where the blue part is the manufacturer prefix part of the MAC, and the green part is the device suffix part of the MAC:

`00:1E:42:11:22:33`

This MAC composition means that the number of possible MAC addresses for each device is at most 8*3=24 bits (224=16,777,216), which is a relatively small number and is easily guessable by attackers.

While this identification method is definitely not secure, it is still not easy to exploit it in a real-life scenario, because it will require too much time to brute force all possible serial number and MAC combinations. Using this weak identification alone, an attacker would need to execute [`Number_of_Possible_SNs`] * [`Number_of_Possible_MACs`] requests, or `~100,000 * 2 ^ 24` requests in order to gain control over all cloud-connected devices, or `~100,000` requests in order to claim one device in particular.

In order to make this vulnerability ([CVE-2023-32347](https://claroty.com/team82/disclosure-dashboard/cve-2023-32347)) even more easily exploitable, we discovered another vulnerability that allowed us to leak all used serial numbers and MAC addresses, drastically reducing the range of our brute force attack.

  

## Finding all Registered Devices Using Cloud Oracles

As part of our research on the RMS platform, we discovered a feature in the platform that allows users to enumerate the serial numbers and MAC address of all cloud-connected devices. This type of vulnerability is called an information oracle, because it could be used to identify and distinguish between used and unused serial numbers and MACs.

This vulnerability ([CVE-2023-32346](/team82/disclosure-dashboard/cve-2023-32346)) lies in the device claiming feature, accessible from this API route: `/api/devices/import`, allowing users to claim their devices. Using this route, users can try and claim devices from their serial number and MAC address. However, we noticed that only three options exist:

  1. The serial number is already in use

  2. The MAC is already in use

  3. The device is successfully claimed

![Claiming process error](/img/asset/YXNzZXRzLzE1LmpwZw/15.jpg?fm=webp&fit=crop&s=46f8ed74d5759309a895c00787bce586) __ An error returned from the claiming process, telling us that the serial number we guessed is used already in the RMS platform.

Abusing this oracle, we can easily create a list of all the serial numbers and MAC addresses of cloud-connected devices. This is made even more trivial when we notice that this feature accepts a CSV list of devices, meaning we could check multiple serial numbers and MACs in one request.

![Request checking serial numbers](/img/asset/YXNzZXRzLzE2LmpwZw/16.jpg?fm=webp&fit=crop&s=3f88a3cd06feaf26334a13aaff0acd78) __ A request checking multiple serial numbers and MACs.

By abusing the CSV import feature, it is possible for attackers to retrieve a full list of all used serial numbers and MAC addresses in the RMS platform, which reduces the range of brute force necessary to find every one to `[Number_of_Actual_Devices] ^ 2`. Then, by performing this brute force computation, attackers can identify and impersonate every device on the platform.

After gaining the ability to impersonate devices, we explored what new attack surface was exposed. One feature that caught our interest was the ability to access the device management ports over Teltonika’s cloud, allowing users to access their device’s SSH service and web server. During usage of this feature, the device’s password is passed directly to the device, in order to authenticate the user. By impersonating the device, we managed to leak this password, and gain the credential for the device.

![Teltonika’s WebUI Login Request](/img/asset/YXNzZXRzLzE3LmpwZw/17.jpg?fm=webp&fit=crop&s=673902ec22ae1999303b2686afdaaaac) __ A login request over Teltonika’s WebUI.

This, in combination with the thousands of devices that are internet-facing led us to seek out vulnerabilities in the device management web server. That’s where we discovered a few remote code execution vulnerabilities that could allow attackers to take over Teltonika 4G routers.

This vulnerability ([CVE-2023-32349](/team82/disclosure-dashboard/cve-2023-32349)) stems from the tcpdump utility, allowing users to download a PCAP of filtered traffic from their devices.

![tcpdump functionality of RUT241 devices](/img/asset/YXNzZXRzLzE4LmpwZw/18.jpg?fm=webp&fit=crop&s=4392b5388f909622878aab90517da4e4) __ The tcpdump functionality of RUT241 devices, allowing users to save traffic from their devices.

In order to save the traffic, Teltonika uses the tcpdump binary. Users can also filter the traffic, only saving traffic coming from a specific interface, host etc. These filters will then be reflected in an OS command executing tcpdump.

![Teltonika TCPDump utility](/img/asset/YXNzZXRzLzE5LmpwZw/19.jpg?fm=webp&fit=crop&s=9a53ce26a9058a19b5a2732951e55396) __ The tcpdump command is being executed by the Teltonika TCPDump utility.

When it comes to filter validation, Teltonika actually validates each parameter, not allowing users to supply malicious parameters thus blocking an attempt for an OS command injection.

However, when we look where these variables are stored, we notice that it comes from the UCI configuration tool, used by Teltonika devices to store and change system configurations. Behind the scenes, this is mapped to a config file containing these variables.

![/etc/config/system configuration file](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb25maWcxLnBuZw/teltonika_config1.png?fm=webp&fit=crop&s=0d9e0cdf00b5d530bf07ba4d3f6b01b3) __ The /etc/config/system configuration file, containing the parameters passed to the tcpdump binary.

However, one feature that is exposed to authenticated users is the `UBUS JSONRPC`, which gives access to users to the `UBUS` utility. By using this API, which is accessible through the `/UBUS` API route, it is possible for users to interact with the UCI configuration utility, allowing users to both get and set configuration parameters.

![/UBUS api route](/img/asset/YXNzZXRzL3RlbHRvbmlrYV91YnVzLXBheWxvYWQucG5n/teltonika_ubus-payload.png?fm=webp&fit=crop&s=4bacbf7c253bf649fe712458b0393c29) __ A payload sent to the /UBUS api route, requesting the UCI config for the widget.

Through this `UBUS` interface, it is possible for users to alter configurations in the system. Abusing this, we can alter the configuration for one of the parameters passed to the TCPDump utility, and then save the configuration. Then, when we invoke the TPCDump utility, it will use our parameters and will execute arbitrary code.

![Configuration of the tcp_mount parameter](/img/asset/YXNzZXRzL3RlbHRvbmlrYS1jb25maWcyMi5wbmc/teltonika-config22.png?fm=webp&fit=crop&s=6bf53664e1dc363377b30968cc8f2c6d) __ A request setting the configuration of the tcp_mount parameter to a malicious OS command.

Then we commit the changes to the configurations:

![Teltonika Config](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb25maWctbWFsaWNpb3VzLTE2ODM5MDUzMDIucG5n/teltonika_config-malicious-1683905302.png?fm=webp&fit=crop&s=6f2ecf9d6a054c74f4a7bfcce0346714) __

Then, whenever we use the TCPDump utility, our malicious payload will be executed.

![malicious payload being executed](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9tYWwtcGF5LWV4ZWMucG5n/teltonika_mal-pay-exec.png?fm=webp&fit=crop&s=a2507ec988cb701b49d0dad70065a631) __ Our malicious payload being executed, resulting in us being able to execute OS commands in the root permissions.

### Registered device(s) takeover through account takeover ([CVE-2023-2587](https://claroty.com/team82/disclosure-dashboard/cve-2023-2587))

The first step in the attack process involves an attacker obtaining a valid MAC-serial pairing of any Teltonika router registered to a cloud account. Once an attacker has this information, the attacker can impersonate the device and make the RMS cloud platform think they are the actual router. As a result, all the information that is supposed to be sent to the router will be sent to the attacker instead. 

Attackers with a MAC-serial of a registered device can send a specially crafted JSON message with an HTML object in the `fw_version` field to trigger the vulnerability.

![HTML object in the fw_version field](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9odG1sLW9iamVjdC5wbmc/teltonika_html-object.png?fm=webp&fit=crop&s=43421c0312ef53f96dbcb41760892212) __ HTML object in the fw_version field.

By sending this JSON message, the attacker will trigger a stored-cross-site scripting (XSS) vulnerability under the “DEVICE FIRMWARE” window in the middle of the main RMS page for this router administrator (the victim). The vulnerable place is when the victim moves the mouse over the “malicious” `fw_version` that we inject. As it can see in the image above.  
  
For demonstration, we inject an HTML object with the tag <u> (underline). Another example would be the HTML `<embed>` tag to load an arbitrary web page; by moving the mouse over the “malicious” `fw_version` the web page will be loaded.

![fw_version field will trigger the XSS](/img/asset/YXNzZXRzLzI2LmpwZw/26.jpg?fm=webp&fit=crop&s=562f9bcf3919e7866b8d203c9b8d2808) __ Mouse over the fw_version field will trigger the XSS.

This XSS could be leveraged by a malicious actor in order to leak cookies, resulting in account takeover. But, as some limitations in the XSS made it a bit more difficult, we’ve chained it with the next vulnerability, which led to easier and reliable exploitation of account takeover.

## Abusing User-controlled Subdomains in teltonika-networks.com ([CVE-2023-2588](https://claroty.com/team82/disclosure-dashboard/cve-2023-2588))

The “Device CLI/Device WEB” feature in the RMS, allows users to access managed device’s local ssh/web management services over the RMS cloud proxy. Requesting for a web proxy to our device, will result in a url in the RMS cloud subdomain leading to our device local web interface:

![Accessing router local web service over the cloud](/img/asset/YXNzZXRzL3RlbHRvbmlrYS1yb3V0ZXItd2ViLnBuZw/teltonika-router-web.png?fm=webp&fit=crop&s=843cff66f87520faebee898f2effa817) __ Accessing router local web service over the cloud.

This URL can be shared with others and requires no RMS-level authentication. Since we are in control of our local device, we are also in control of the web pages that are served over this URL.

For example, we can redirect the traffic internally to our own web server instead of the local web service:

![Legitimate RMS subdomain redirect to malicious web page](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9yZWRpcmVjdC5wbmc/teltonika_redirect.png?fm=webp&fit=crop&s=92f874984ba46f17d663491b3a8f48d8) __ Legitimate RMS subdomain redirect to malicious web page.

As the defined web policies in the domain (such as Content Security Policy) are also open, at this phase we are able to execute JavaScript code in the context of the connected client. In the image below we can see that RMS define whitelist with two sources: 

  1. `rms.teltonika-networks.com `

  2. `*.rms.teltonika-networks.com`

![Content-security-policy RMS subdomain](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb250ZW50LXBvbGljeS5wbmc/teltonika_content-policy.png?fm=webp&fit=crop&s=c91d3eba75ccf20ac463f0233286e75f) __ Content-security-policy allows loading content from RMS subdomain

The second source (*.rms.teltonika-networks.com) includes the Device WEB feature (remote proxy over the RMS).

Leveraging this issue, we managed to write a web page that will be loaded automatically when accessing the url, automatically leaking the user’s RMS cloud cookies or executing action on behalf of it, on this example, remote code execution on all managed devices in the account:

![Exploit page](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9leHBsb2l0LXBhZ2UucG5n/teltonika_exploit-page.png?fm=webp&fit=crop&s=10aeae483edf3b0b2c5717b56ab92f08) __ Exploit page: Creates a reverse shell and executes it on all routers.

While this malicious page can be embedded on any website online or sent as part of a phishing campaign, using the stored-XSS vulnerability in the fw_version field, an attacker can target specific users, using the HTML <embed> tag to load the exploit page as part of their management panel. 

Once the victim moves the mouse over this area, the exploit.html web page will be loaded, creating a reverse shell on all managed routers under this RMS user.

![exploit.html web page](/img/asset/YXNzZXRzLzMxLmpwZw/31.jpg?fm=webp&fit=crop&s=d2cdf4695e80609d40f8b22a2d4f38bc) __

## Accessing Internal Cloud Infrastructure ([CVE-2023-32348](https://claroty.com/team82/disclosure-dashboard/cve-2023-32348))

Another vulnerability ([CVE-2023-32348](/team82/disclosure-dashboard/cve-2023-32348)), enabled us to make requests from the RMS infrastructure. This meant we were able to access everything the RMS can access, including internal API, other infrastructure etc. By exploiting this vulnerability, it is possible for attackers to access internal infrastructure used by Teltonika.

This vulnerability stems from the [Device VPN Hub feature of the RMS platform](https://wiki.teltonika-networks.com/view/RMS_VPN_Hubs), a shared VPN hub allowing cross-device communication. This feature allows users to set up a private VPN connection over Teltonika’s infrastructure to create some kind of a local network over the cloud between Teltonika routers and remote devices.

![RMS VPN feature](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9ybXMtdnBuLnBuZw/teltonika_rms-vpn.png?fm=webp&fit=crop&s=621ae2e85208942e8e9db73405c8cd34) __ The RMS VPN feature, allowing users to set up a VPN network for their devices.

Behind the scenes, this feature uses an OpenVPN server and client in order to connect the devices to the Device VPN Hub. When users connect their devices to a specific VPN hub, RMS downloads to the device an OpenVPN configuration, including private keys and certificates, and then it executes OpenVPN client in order to connect the device to the Hub.

![OpenVPN configuration](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9vcGVudnBuLnBuZw/teltonika_openvpn.png?fm=webp&fit=crop&s=64ac18b0c56034d1f9c13fc2fd90355f) __ OpenVPN configuration used by the device to connect to the VPN hub.

Then, the OpenVPN client on the device opens and creates a new virtual interface for the VPN tunnel. Finally, it can communicate with all devices connected to this VPN, over the new interface.

However, we discovered that the OpenVPN server hosted by Teltonika allows devices to route through it. This means that if we implicitly try to connect to a remote server, routing through the OpenVPN server, the OpenVPN server will route our request to the destination. This enables us to scan and access everything the OpenVPN server itself is accessible to, including internal backend services, other infrastructure and even the cloud infrastructure itself.

For example, by routing through the OpenVPN server, we were able to access both the AWS infrastructure and exfiltrate sensitive identification tokens, and internal Teltonika services.

![Teltonika VPN hubs managent](/img/asset/YXNzZXRzLzM0LmpwZw/34.jpg?fm=webp&fit=crop&s=ea8313fb764beae8aca36bd2c5cff04e) __ An internal service used by Teltonika to manage their VPN hubs. ![Amazon AWS meta-data service request](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9hd3MucG5n/teltonika_aws.png?fm=webp&fit=crop&s=87c0c8995e82d3caf53396c112a4cc69) __ A request to Amazon AWS meta-data service, providing information about the internal AWS network only accessible to servers from the internal networks.

By abusing this arbitrary routing vulnerability, attackers could be able to access Teltonika’s internal services, including the Amazon AWS Metadata service, and may leak sensitive information.

Generally speaking, this type of cloud-based server-side request forgery (SSRF) vulnerability could be dangerous, because it exposes the cloud infrastructure to attacks and could allow attackers to compromise the entire cloud. However, in this case we could not leverage this attack further.

## Summary

The evolution of industry 4.0 demands high connectivity of devices wherever they are located. The use of 4/5G routers to enable such connectivity has been and will always be one of the foundations that enable the hyper transformation and drives this connectivity. 

In IoT, the challenge starts with the need to scale up; most solutions need to support a huge fleet of 4G routers, enabling sys-admins to configure, monitor, and maintain all of their devices. This is where cloud management platforms are introduced, allowing sys-admins control over their devices remotely, through the internet. 

However, with the move to smart cloud-controlled devices comes risk, as vulnerabilities in the cloud platform could introduce new attack vectors to companies, putting at risk their remote site and vulnerable IoT/IIoT networks.

In order to explore this new threat landscape, Claroty’s Team82 and OTORIO collaborated to research and uncover critical vulnerabilities in one of the most popular 4G router solutions, Teltonika Networks Throughout our research, we explored attack surfaces in 4G routers’ cloud management platforms, and discovered three unique attack vectors that could allow attackers to remotely take control over devices and gain access to companies’ internal IIoT/IoT networks. 

All discovered vulnerabilities were disclosed to Teltonika, which addressed and provided security fixes to them all. 

## Acknowledgement

 _We wish to acknowledge and thank Teltonika Networks for its cooperation and coordination throughout this disclosure._

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ Twitter ](https://twitter.com/intent/post?text=Triple Threat: Breaking Teltonika Routers Three Ways&url=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ ](mailto:?subject=Triple Threat: Breaking Teltonika Routers Three Ways&body=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ Twitter ](https://twitter.com/intent/post?text=Triple Threat: Breaking Teltonika Routers Three Ways&url=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) [ __ ](mailto:?subject=Triple Threat: Breaking Teltonika Routers Three Ways&body=https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways)

Related Vulnerability Disclosures

  * ##### [CVE-2023-32346 CWE-204: Observable Response Discrepancy Teltonika’s Remote Management System versions prior to 4.10.0 contain a function that allows users to claim their devices. This function returns information based on whether the serial number of a device has already been claimed, the MAC address of a device has already been claimed, or whether the attempt to claim a device was successful. An attacker could exploit this to create a list of the serial numbers and MAC addresses of all devices cloud-connected to the Remote Management System. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 5.3 ](/team82/disclosure-dashboard/cve-2023-32346)
  * ##### [CVE-2023-32347 CWE-287: Improper Authentication Teltonika’s Remote Management System versions prior to 4.10.0 use device serial numbers and MAC addresses to identify devices from the user perspective for device claiming and from the device perspective for authentication. If an attacker obtained the serial number and MAC address of a device, they could authenticate as that device and steal communication credentials of the device. This could allow an attacker to enable arbitrary command execution as root by utilizing management options within the newly registered devices. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 8.1 ](/team82/disclosure-dashboard/cve-2023-32347)
  * ##### [CVE-2023-32348 CWE-918: Server-Side Request Forgery Teltonika’s Remote Management System versions prior to 4.10.0 contain a virtual private network (VPN) hub feature for cross-device communication that uses OpenVPN. It connects new devices in a manner that allows the new device to communicate with all Teltonika devices connected to the VPN. The OpenVPN server also allows users to route through it. An attacker could route a connection to a remote server through the OpenVPN server, enabling them to scan and access data from other Teltonika devices connected to the VPN. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 9.3 ](/team82/disclosure-dashboard/cve-2023-32348)
  * ##### [CVE-2023-32349 CWE-15: External Control of System or Configuration Setting Versions 00.07.00 through 00.07.03.4 of Teltonika’s RUT router firmware contain a packet dump utility that contains proper validation for filter parameters. However, variables for validation checks are stored in an external configuration file. An authenticated attacker could use an exposed UCI configuration utility to change these variables and enable malicious parameters in the dump utility, which could result in arbitrary code execution. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 8.0 ](/team82/disclosure-dashboard/cve-2023-32349)
  * ##### [CVE-2023-32350 CWE-78: Improper Neutralization of Special Elements used in an OS Command (OS Command Injection) Versions 00.07.00 through 00.07.03 of Teltonika’s RUT router firmware contain an operating system (OS) command injection vulnerability in a Lua service. An attacker could exploit a parameter in the vulnerable function that calls a user-provided package name by instead providing a package with a malicious name that contains an OS command injection payload. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 8.8 ](/team82/disclosure-dashboard/cve-2023-32350)
  * ##### [CVE-2023-2586 CWE-287: Improper Authentication Teltonika’s Remote Management System versions 4.14.0 is vulnerable to an unauthorized attacker registering previously unregistered devices through the RMS platform. If the user has not disabled the "RMS management feature" enabled by default, then an attacker could register that device to themselves. This could enable the attacker to perform different operations on the user's devices, including remote code execution with 'root' privileges (using the 'Task Manager' feature on RMS). [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 9.0 ](/team82/disclosure-dashboard/cve-2023-2586)
  * ##### [CVE-2023-2587 CWE-79: Improper Neutralization of Input During Web Page Generation (Cross-Site Scripting) Teltonika’s Remote Management System versions prior to 4.10.0 contain a cross-site scripting (XSS) vulnerability in the main page of the web interface. An attacker with the MAC address and serial number of a connected device could send a maliciously crafted JSON file with an HTML object to trigger the vulnerability. This could allow the attacker to execute scripts in the account context and obtain remote code execution on managed devices. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 7.5 ](/team82/disclosure-dashboard/cve-2023-2587)
  * ##### [CVE-2023-2588 CWE-830: Inclusion of Web Functionality from an Untrusted Source Teltonika’s Remote Management System versions prior to 4.10.0 have a feature allowing users to access managed devices’ local secure shell (SSH)/web management services over the cloud proxy. A user can request a web proxy and obtain a URL in the Remote Management System cloud subdomain. This URL could be shared with others without Remote Management System authentication . An attacker could exploit this vulnerability to create a malicious webpage that uses a trusted and certified domain. An attacker could initiate a reverse shell when a victim connects to the malicious webpage, achieving remote code execution on the victim device. [Read more: “Triple Threat: Breaking Teltonika Routers Three Ways”](https://claroty.com/team82/research/triple-threat-breaking-teltonika-routers-three-ways) CVSS v3: 8.8 ](/team82/disclosure-dashboard/cve-2023-2588)

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

__ Close Modal ![Breaking Teltonika Routers Three Ways](/img/asset/YXNzZXRzLzExLmpwZw/11.jpg?fm=webp&fit=crop&s=33283da7e9ec9d129e23619c3f9af73b)

__ Close Modal ![Teltonika's RUT241 4G router](/img/asset/YXNzZXRzL2ZyLmpwZw/fr.jpg?fm=webp&fit=crop&s=e967f025ef7d1ca7e82639d53db11880)

__ Close Modal ![Search results for Teltonika devices](/img/asset/YXNzZXRzLzIuanBn/2.jpg?fm=webp&fit=crop&s=02eeba0020ded572b302d9fd2c3abd9f)

__ Close Modal ![RUT950](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9sYWJlbC5wbmc/teltonika_label.png?fm=webp&fit=crop&s=741abb335627abb0a75aff5d7558ce81)

__ Close Modal ![RUT950](/img/asset/YXNzZXRzLzMuanBn/3.jpg?fm=webp&fit=crop&s=ee60f78c4dc35afe26190619b59d3932)

__ Close Modal ![RUT950 Unboxing](/img/asset/YXNzZXRzLzQuanBn/4.jpg?fm=webp&fit=crop&s=d5641ac2787b98c056c93ce8ffefb56b)

__ Close Modal ![RUT Unboxing 2](/img/asset/YXNzZXRzLzUuanBn/5.jpg?fm=webp&fit=crop&s=b584bdf06110acdc909397e7efa89309)

__ Close Modal ![Adding a new PMS Device](/img/asset/YXNzZXRzLzYuanBn/6.jpg?fm=webp&fit=crop&s=ddfbf71cd08837e77d9c87cfdfd76b82)

__ Close Modal ![Collecting identifiers for registration](/img/asset/YXNzZXRzLzcuanBn/7.jpg?fm=webp&fit=crop&s=83ebac5c9a580da78e7fe601b53053d4)

__ Close Modal ![RMS Task manager feature](/img/asset/YXNzZXRzLzguanBn/8.jpg?fm=webp&fit=crop&s=2a652a0061ec0e8b19e25ef1fa9ef0e3)

__ Close Modal ![Remote code execution on RUT955](/img/asset/YXNzZXRzLzkuanBn/9.jpg?fm=webp&fit=crop&s=88b042eeb60bd7bb03b94fcbbbc075f6)

__ Close Modal ![Registered device over LAN/WAN Tavekover](/img/asset/YXNzZXRzLzEwMC5qcGc/100.jpg?fm=webp&fit=crop&s=e7cec96fafb70821820503eb7d3c000f)

__ Close Modal ![Teltonika RUT240 router firmware](/img/asset/YXNzZXRzLzExLTE2ODQ5Mjg4OTQuanBn/11-1684928894.jpg?fm=webp&fit=crop&s=3c885241298b70ba4952d36f9597a4bd)

__ Close Modal ![Inside Teltonika’s RUT240 firmware](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9pbnNpZGUtZmlybXdhcmUucG5n/teltonika_inside-firmware.png?fm=webp&fit=crop&s=4116eaa444bc6cbf48c0b03fc786b3fe)

__ Close Modal ![/etc/config/rms_mqtt](/img/asset/YXNzZXRzLzEzLTE2ODQ5Mjg5NDUuanBn/13-1684928945.jpg?fm=webp&fit=crop&s=e12facba5119741e3c13dbeaf898d583)

__ Close Modal ![MQTT certificate](/img/asset/YXNzZXRzLzE0LmpwZw/14.jpg?fm=webp&fit=crop&s=dc03d24ffc46640e884fa648e109b533)

__ Close Modal ![Claiming process error](/img/asset/YXNzZXRzLzE1LmpwZw/15.jpg?fm=webp&fit=crop&s=46f8ed74d5759309a895c00787bce586)

__ Close Modal ![Request checking serial numbers](/img/asset/YXNzZXRzLzE2LmpwZw/16.jpg?fm=webp&fit=crop&s=3f88a3cd06feaf26334a13aaff0acd78)

__ Close Modal ![Teltonika’s WebUI Login Request](/img/asset/YXNzZXRzLzE3LmpwZw/17.jpg?fm=webp&fit=crop&s=673902ec22ae1999303b2686afdaaaac)

__ Close Modal ![tcpdump functionality of RUT241 devices](/img/asset/YXNzZXRzLzE4LmpwZw/18.jpg?fm=webp&fit=crop&s=4392b5388f909622878aab90517da4e4)

__ Close Modal ![Teltonika TCPDump utility](/img/asset/YXNzZXRzLzE5LmpwZw/19.jpg?fm=webp&fit=crop&s=9a53ce26a9058a19b5a2732951e55396)

__ Close Modal ![/etc/config/system configuration file](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb25maWcxLnBuZw/teltonika_config1.png?fm=webp&fit=crop&s=0d9e0cdf00b5d530bf07ba4d3f6b01b3)

__ Close Modal ![/UBUS api route](/img/asset/YXNzZXRzL3RlbHRvbmlrYV91YnVzLXBheWxvYWQucG5n/teltonika_ubus-payload.png?fm=webp&fit=crop&s=4bacbf7c253bf649fe712458b0393c29)

__ Close Modal ![Configuration of the tcp_mount parameter](/img/asset/YXNzZXRzL3RlbHRvbmlrYS1jb25maWcyMi5wbmc/teltonika-config22.png?fm=webp&fit=crop&s=6bf53664e1dc363377b30968cc8f2c6d)

__ Close Modal ![Teltonika Config](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb25maWctbWFsaWNpb3VzLTE2ODM5MDUzMDIucG5n/teltonika_config-malicious-1683905302.png?fm=webp&fit=crop&s=6f2ecf9d6a054c74f4a7bfcce0346714)

__ Close Modal ![malicious payload being executed](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9tYWwtcGF5LWV4ZWMucG5n/teltonika_mal-pay-exec.png?fm=webp&fit=crop&s=a2507ec988cb701b49d0dad70065a631)

__ Close Modal ![HTML object in the fw_version field](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9odG1sLW9iamVjdC5wbmc/teltonika_html-object.png?fm=webp&fit=crop&s=43421c0312ef53f96dbcb41760892212)

__ Close Modal ![fw_version field will trigger the XSS](/img/asset/YXNzZXRzLzI2LmpwZw/26.jpg?fm=webp&fit=crop&s=562f9bcf3919e7866b8d203c9b8d2808)

__ Close Modal ![Accessing router local web service over the cloud](/img/asset/YXNzZXRzL3RlbHRvbmlrYS1yb3V0ZXItd2ViLnBuZw/teltonika-router-web.png?fm=webp&fit=crop&s=843cff66f87520faebee898f2effa817)

__ Close Modal ![Legitimate RMS subdomain redirect to malicious web page](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9yZWRpcmVjdC5wbmc/teltonika_redirect.png?fm=webp&fit=crop&s=92f874984ba46f17d663491b3a8f48d8)

__ Close Modal ![Content-security-policy RMS subdomain](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9jb250ZW50LXBvbGljeS5wbmc/teltonika_content-policy.png?fm=webp&fit=crop&s=c91d3eba75ccf20ac463f0233286e75f)

__ Close Modal ![Exploit page](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9leHBsb2l0LXBhZ2UucG5n/teltonika_exploit-page.png?fm=webp&fit=crop&s=10aeae483edf3b0b2c5717b56ab92f08)

__ Close Modal ![exploit.html web page](/img/asset/YXNzZXRzLzMxLmpwZw/31.jpg?fm=webp&fit=crop&s=d2cdf4695e80609d40f8b22a2d4f38bc)

__ Close Modal ![RMS VPN feature](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9ybXMtdnBuLnBuZw/teltonika_rms-vpn.png?fm=webp&fit=crop&s=621ae2e85208942e8e9db73405c8cd34)

__ Close Modal ![OpenVPN configuration](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9vcGVudnBuLnBuZw/teltonika_openvpn.png?fm=webp&fit=crop&s=64ac18b0c56034d1f9c13fc2fd90355f)

__ Close Modal ![Teltonika VPN hubs managent](/img/asset/YXNzZXRzLzM0LmpwZw/34.jpg?fm=webp&fit=crop&s=ea8313fb764beae8aca36bd2c5cff04e)

__ Close Modal ![Amazon AWS meta-data service request](/img/asset/YXNzZXRzL3RlbHRvbmlrYV9hd3MucG5n/teltonika_aws.png?fm=webp&fit=crop&s=87c0c8995e82d3caf53396c112a4cc69)

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

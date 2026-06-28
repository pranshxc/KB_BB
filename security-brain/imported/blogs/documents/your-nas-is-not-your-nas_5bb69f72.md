---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-28_your-nas-is-not-your-nas.md
original_filename: 2022-03-28_your-nas-is-not-your-nas.md
title: Your NAS is not your NAS !
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- supply-chain
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- supply-chain
language: en
raw_sha256: 5bb69f72c42c207b15e0f7ddb9a9d1142abc26404cb860ab37bcfb68b8e6a7c7
text_sha256: 317c82e5079a1d6c07759ce14bcfdf90e3dfacab3a6a389971470febc5bf38fa
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Your NAS is not your NAS !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-28_your-nas-is-not-your-nas.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `5bb69f72c42c207b15e0f7ddb9a9d1142abc26404cb860ab37bcfb68b8e6a7c7`
- Text SHA256: `317c82e5079a1d6c07759ce14bcfdf90e3dfacab3a6a389971470febc5bf38fa`


## Content

---
title: "Your NAS is not your NAS !"
page_title: "Your NAS is not your NAS ! | DEVCORE"
url: "https://devco.re/blog/2022/03/28/your-NAS-is-not-your-NAS-en/"
final_url: "https://devco.re/blog/2022/03/28/your-NAS-is-not-your-NAS-en/"
authors: ["Angelboy (@scwuaptx)"]
programs: ["Synology"]
bugs: ["RCE", "Memory corruption", "Buffer Overflow"]
publication_date: "2022-03-28"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 2776
---

[Tech Editorials](/en/blog/category/Tech Editorials) [#RCE](/en/blog/tag/RCE/) [#NAS](/en/blog/tag/NAS/) [#IoT](/en/blog/tag/IoT/) [#Pwn2Own](/en/blog/tag/Pwn2Own/)

#  Your NAS is not your NAS ! 

[ __ ](/en/blog/author/angelboy) [Angelboy](/en/blog/author/angelboy) 2022-03-28

![](https://devco.re/assets/img/blog/20220328/cover.png)

* * *

[English Version](/blog/2022/03/28/your-NAS-is-not-your-NAS-en/) [中文版本](/blog/2022/03/28/your-NAS-is-not-your-NAS/)

Two years ago, we found a [critical vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-21-492/), CVE-2021-31439, on Synology NAS. This vulnerability can let an unauthorized attacker gain code execution on remote Synology DiskStation NAS server. We used this vulnerability to exploit Synology DS418play NAS in Pwn2Own Tokyo 2020. After that, we found the vulnerability is not only exists on Synology but also on most NAS vendors. Following we will describe the details and how we exploit it.

This research is also presented at [HITCON 2021](https://hitcon.org/2021/en). You can check the slides [here](https://hitcon.org/2021/agenda/03f06675-261d-4c97-b524-33ef9cc6ccb2/%E4%BD%A0%E7%9A%84%20NAS%20%E4%B8%8D%E6%98%AF%E4%BD%A0%E7%9A%84%20NAS%20!.pdf).

## Network Attached Storage

In the early days, NAS was generally used to separate the server and data and also used for backup. It was mainly used to allow users to directly access data and share files on the Internet. In modern times, NAS provides not only file sharing but also various services. In this era of Internet of Things, there will be more people combining NAS and home assistants to make life more convenient.

![](/assets/img/blog/20220328/1.png)

## Motivation

### Why do we want to research NAS?

#### Red Team

While we were doing red team assessment, we found that NAS generally appeared in the corporate intranet, or sometimes even exposed to the external network. They usually stored a lot of corporate confidential information on the NAS. Therefore, NAS gradually attracted our attention, and its Strategic Value has been much higher than before.

#### Ransomware

NAS has become more and more popular in recent years. More and more people store important data on NAS. It makes NAS a target of ransomware. At the beginning of last year, NAS vulnerabilities led to outbreak of locker event. We hope to reduce the recurrence of similar things, thereby increasing the priority of NAS research to improve NAS security.

#### Pwn2Own Mobile 2020

The last reason is that NAS has become one of the main targets of Pwn2Own Mobile since 2020. We also wanted to try to join Pwn2Pwn event, so we decided to make NAS as the primary goal of the research at that time. Because of Synology is the most popular device in Taiwan, we decided start from it.

## Recon

### Environment

  * DS918+
  * DSM 6.2.3-25426

Our test environment is Synology DS918+. It very similar as DS418 play(target of Pwn2Own Tokyo 2020). In order to better meet the environment that we usually encounter and the requirements in Pwn2Own, it will be in the state of all default settings.

### Attack surface

![](/assets/img/blog/20220328/2.png)

First of all, we can use netstat to find which port is open. We can see that in the default environment, many services are opened, such as smb/nginx/afpd.

![](/assets/img/blog/20220328/3.png)

In UDP, it has minissdpd/findhost/snmpd, etc., most of protocols help to find devices.

We selected a few services for preliminary analysis.

#### DSM Web interface

The first one is the DSM Web interface. This part is probably the one that most people analyze and it has obvious entry points. Many years ago, there were many command injection vulnerabilities, but after that Synology set strict specifications. There are almost no similar problems nowadays.

#### SMB

The SMB protocol in Synology is based on [Samba](https://www.samba.org/). Due to the large number of user, many researcher are doing code review on it. Therefore, there are many vulnerabilities found in Samba every year. The most famous vulnerability recently is [SambaCry](https://www.samba.org/samba/security/CVE-2017-7494.html). But because more people are reviewing, it is relatively safer than other services.

#### iSCSI Manager

It mainly helps users manage and monitor iSCSI services and it is developed by Synology itself. There are a lot of vulnerabilities in iSCSI recently. Maybe it will be a good target. If there is no other attack surface, we might analyze it first.

#### Netatalk

The last one is Netatalk, which is known as afp protocol. Netatalk in Synology is based on [Netatak](http://netatalk.sourceforge.net/) 3.1.8. The most critical vulnerability recently is CVE-2018-1160. For this vulnerability, please refer to [Exploiting an 18 Year Old Bug](https://medium.com/tenable-techblog/exploiting-an-18-year-old-bug-b47afe54172). Compared with other services, Netatalk has very few vulnerabilities in the past. It is less noticed, and it has not been updated and maintained for a long time.

After overall analysis, we believe that Netatalk is the most vulnerable point in Synology. We finally decided to analyze it first. In fact, there are other services and attack surfaces, but we didn’t spend much time on other service. We will only focus on Netatalk in this article.

## Netatalk

Apple Filing Protocol (AFP) is a file transfer protocol similar to SMB. It is used to transfer and share files on MAC. Because Apple itself is not open-sourced, in order to utilize AFP on Unix-like systems, Netatalk is created. Netatalk is a freely-available Open Source AFP fileserver. Almost every NAS uses it to make file sharing on MAC more convenient.

### Netatalk in Synology

The netatalk in Synology is enabled by default. The version is modified from netatalk 3.1.8, and it tracks security updates regularly. Once installed, you can use the AFP protocol to share files with Synology NAS. It also enables protections such as ASLR, NX and StackGuard.

![](/assets/img/blog/20220328/4.png)

#### DSI

Before we look into the detail of the vulnerability we need to talk about Data Stream Interface (DSI). The DSI is a session layer format used to carry AFP traffic over TCP. While server and client communicate through the AFP, a DSI header is in front of each packet.

DSI Packet Header :

![](/assets/img/blog/20220328/5.png)

The content of the DSI packet is shown as the figure above. It contains metadata and payload, which generally follows the DSI header and payload format.

AFP over DSI :

![](/assets/img/blog/20220328/6.png)

The communication of the AFP protocol is shown above. The client first gets the server information to determine available authentication methods, the version used, and so on. Then it opens a new session and to execute AFP commands. Without authentication, we can only do related operations such as login and logout. Once the client is verified, we can do file operations like SMB.

In Netatalk implementation, `dsi_block` will be used as the packet structure.

dsi_block :

![](/assets/img/blog/20220328/7.png)

  * dsi_flag means that the packet is a request or reply
  * dsi_command indicates what our request does 
  * DSICloseSession
  * DSICommand
  * DSIGetStatus
  * DSIOpenSession
  * dsi_code 
  * Error code
  * For reply
  * dsi_doff 
  * DSI data offset
  * Using in DSIWrite
  * dsi_len 
  * The Length of Payload

DSI : A descriptor of dsi stream

![](/assets/img/blog/20220328/8.png)

In Netatalk, most of the information are stored in a structure called DSI for subsequent operations after parsing the packet and configuration files, such as `server_quantum` and payload content.

![](/assets/img/blog/20220328/9.png)

The payload of the packet is stored in the `command` buffer in the DSI structure. The buffer size is `server_quantum`, and the value is specified in the afp configuration file `afp.conf`.

![](/assets/img/blog/20220328/10.png)

If not specified, it uses the default size(0x100000).

With a preliminary understanding, let’s talk about this vulnerability.

### Vulnerability

![](/assets/img/blog/20220328/11.png)

The vulnerability we found occurs while receiving the payload. It can be triggered without authentication. The vulnerable function is `dsi_stream_receive`.

![](/assets/img/blog/20220328/12.png)

It’s the function that parses the information from received packet and puts it into the DSI structure. When it receives the packet data, it first determine how much data to read into the command buffer according to the `dsi_len` in the dsi header. At the beginning, the size of `dsi_cmdlen` is verified.

![](/assets/img/blog/20220328/13.png)

However, as shown in the picture above, if `dsi_doff` is provided by user, `dsi_doff` is used as the length. There is no verification here.

![](/assets/img/blog/20220328/14.png)

The default length of `dsi->commands` is 0x100000(`dsi->server_quantum`), which is a fixed length allocated in `dsi_init`, so as long as `dsi->header.dsi_doff` is larger than `dsi->server_quantum`, heap overflow occurs.

### Exploitation

In DSM 6.2.3, `dsi->commands` buffer is allocated by malloc at libc 2.20. When it allocates more than 0x20000, malloc calls mmap to allocate memory. The memory layout of afpd after `dsi_init` is as below.

![](/assets/img/blog/20220328/15.png)

At the below of `dsi->commands` is Thread Local Storage, which is used to store thread local variables of the main thread.

![](/assets/img/blog/20220328/16.png)

Because of this memory layout, we can use the vulnerability to overwrite the data on Thread Local Storage. What variables to be overwritten in the Thread Local Storage?

#### Thread-local Storage

Thread-local Storage (TLS) is used to store the local variables of the thread. Each thread have its own TLS, which allocated when the Thread is created. It will be released when thread is destroyed. We can use heap overflow vulnerabilities to overwrite most of the variables stored in TLS.

#### Target in TLS

In fact, there are many variables that can control RIP on TLS. Here are a few more common ones.

  * `main_arena`
  * We can forge main_arena to achieve arbitrary writing, but it’s more complicated
  * `pointer_guard`
  * We can modify the pointer guard to change the function pointer, but it requires a leak.
  * `tls_dtor_list`
  * It’s more suitable for our current situation

#### Overwrite `tls_dtor_list`

We can use the [technique](https://googleprojectzero.blogspot.com/2014/08/the-poisoned-nul-byte-2014-edition.html) used by project zero in 2014 to overwrite the `tls_dtor_list` in the `Thread Local Storage`, and then control the RIP in exit().
  
  
  struct dtor_list
  {
  dtor_func func;
  void *obj;
  struct link_map *map;
  struct dtor_list *next;
  }
  

`tls_dtor_list` is a singly linked list of `dtor_list` objects. It is mainly a destructor for thread local storage. In the end of the thread execution, it calls destructor function pointer in the linked list. We can overwrite `tls_dtor_list` with `dtor_list` we forged.

![](/assets/img/blog/20220328/17.png)

When the process exits, it calls `call_tls_dtors()`. This function takes the object in `tls_dtor_list` and calls each destructor. At this time, if we can control `tls_dtor_list`, it calls the function we specified.

![](/assets/img/blog/20220328/18.png)

However, in the new version of glibc, the function of `dtor_list` is protected by pointer guard. So we need to know the value of pointer guard before we overwrite it. The pointer guard is initialized at the beginning of the program and is an unpredictable random number. If we don’t have information leakage, it’s hard to know the value.

But in fact pointer guard would also be placed in `Thread Local Storage`.

![](/assets/img/blog/20220328/19.png)

In the `Thread Local Storage`, there is a `tcbhead_t` structure below the `tls_dtor_list`, which is the thread descriptor of main thread.

`tcbhead_t` structure is used to store various information about the thread such as the `stack_guard` and `pointer_guard` used by the thread. In x86-64 Linux system, the fs register always points to the `tcbhead_t` of the current thread, so the program access thread local storage by using fs register. The memory layout of `Thread local storage` is shown as below.

![](/assets/img/blog/20220328/20.png)

We can use the vulnerability to overwrite not only `tls_dtor_list` but also pointer guard in the `tcbhead_t`. In this way, we can overwrite it with `NULL` to solve the pointer guard problem mentioned earlier.

![](/assets/img/blog/20220328/21.png)

But another problem appears, after we overwrite pointer guard, stack guard will also be overwritten.

![](/assets/img/blog/20220328/22.png)

Before netatalk receives data, it first puts the original stack guard on the stack, and then invoke recv() to receive data to `dsi->command`. At this time, the buffer overflow occurs and cause stack guard and pointer guard to be overwritten. After this, netatalk returns to normal execution flow. It takes the stack guard from the stack and compare it with the stack guard in `Thread Local Storage`. However, it has been overwritten by us, the comparison here fails, causing abort to terminate the program.

#### Bypass stack guard

![](/assets/img/blog/20220328/23.png)

In the netatalk(afpd) architecture, each connection forks a new process to handle the user’s request, so the memory address and stack guard of each connection are the same as the parent process. Because of this behavior, we can use brute-force bytes one by one to leak stack guard.

#### Brute-force stack guard

We can use the overflow vulnerability to overwrite only the last byte of stack guard on `Thread Local Storage` with different value in each different connection. Once the value is different from the original value, the service disconnects. Therefore, we can use the behavior to validate whether the value we overwritten is the same as stack guard. After the lowest byte is determined, we can continue to add another byte, and so on.

![](/assets/img/blog/20220328/24.png)

In the above figure, we assume that the stack guard is `0xdeadbeeffacebc00`. Due to the stack guard feature in Linux, the lowest byte must be 0. Let’s start with the second byte. We can overwrite with 0x00 to see if the connection is disconnected first. If it is disconnected, it means the value we overwrote is wrong. Next, we will test other values to see if the connection is disconnected. And so on, until there is no disconnection, we can find the correct value of section bytes. Then we can try to overwrite third byte, fourth byte and so on. After the stack guard is overwritten with 8 bytes and the connection is not disconnected, we can successfully bypass the stack guard.

After we leak the stack guard, we can actually control RIP successfully. Next, we need to forge the structure `_dtor_list` to control RIP.

#### Construct the `_dtor_list` to control RIP

In DSM 6.2.3-25426, Because it does not enable PIE, we can forge `_dtor_list` on the data section of afpd.

![](/assets/img/blog/20220328/25.png)

Luckily, when netatalk use `dhx2 login` authentication, it will copy the username we provided to the data section of afpd. We can use the feature to construct `_dtor_list` on the known address.

![](/assets/img/blog/20220328/26.png)

After everything is constructed, we can trigger the normal function `DSICloseSession` to control the RIP.

#### `tls_dtor_list` in Synology

![](/assets/img/blog/20220328/27.png)

But in the glibc-2.20 in DSM 6.2.3-25426, it will invoke `__tls_get_addr` to get the variable `tls_dtor_list`. The function will take the variable from `tcb->div`. We also need to construct it on a known address.

The final structure we forged is as follows

![](/assets/img/blog/20220328/28.png)

Finally, we control RIP to invoke execl() in afpd to get the reverse shell.

### Remark

In general Netatalk, PIE protection is enabled by default. It is difficult to construct `_dtor_list` in a known address. In fact, you can also leak libc address using a similar method. It is still exploitable.

This vulnerability not only affects Synology, but also affects some devices use Netatalk.

### Other vendor

We tested several vendors using Netatalk and found that most device have similar problems, some are unexploitable but some are exploitable. We have tested QNAP and Asustor here, and both have successfully obtained the shell.

#### QNAP

  * We tested on TS451 
  * QTS 4.5.4.1741
  * Not enable by default
  * Protection 
  * **No Stack Guard**
  * No PIE
  * Built-in system function

![](/assets/img/blog/20220328/29.png) ![](/assets/img/blog/20220328/30.png)

#### Asustor

  * We tested on AS5202T 
  * ADM 3.5.7.RJR1
  * Not enable by default
  * Protection 
  * **No Stack Guard**
  * No PIE
  * Built-in system function

![](/assets/img/blog/20220328/31.png)

It is worth mentioning that both QNAP and Asustor NAS does not enabled stack guard, and you can get the reverse shell without brute-force.

When Synology has not yet patched this vulnerability, it can be exploited as long as the default is installed. **No authentication is required**.

Although QNAP and Asustor are not enabled by default, many users who use Macs still turn it on for convenience. Actually, Netatalk will be used almost in NAS. Most NAS will have an impact, as long as they enable Netatalk, an attacker can use this vulnerability to take over most of the NAS.

**Your NAS is not your NAS !**

![](/assets/img/blog/20220328/32.png)

In fact, many people open Netatalk on the external network. There are 130,000 machines on shodan alone, most of which are Synology.

## Mitigation

### Update

At present, the above three have been patched, please update to the latest version.

  * Synology 
  * https://www.synology.com/zh-hk/security/advisory/Synology_SA_20_26
  * QNAP 
  * https://www.qnap.com/en/security-advisory/qsa-21-50
  * Asustor 
  * https://www.asustor.com/service/release_notes#ADM%203.5.7.RKU2

This vulnerability is also fixed in the recently released [Netatalk 3.1.13](https://netatalk.sourceforge.io/3.1/ReleaseNotes3.1.13.html). If you use a version before Netatalk 3.1.13, you also need to update to the latest version.

### Disable AFP

  * It’s best to disable it directly. The project is rarely maintained, and the risk of continuing to use it is extremely high.
  * SMB is **relatively safe**
  * If you want to use similar feature, it is recommended to use SMB. It is relatively safe, but it can only be said to be relatively safe.
  * It is recommended that all related services should be opened in the intranet.

## Summary

We have successfully found a serious vulnerability in the NAS, and successfully wrote a proof-of-concept, which proved that it can be exploited on many NAS such as Synology, QNAP and Asustor.

We also think that Netatalk is a new generation of backdoor in NAS!

In the future, We hope that NAS vendor who use third-party can re-examine the security issues caused by them. It is strongly recommended that NAS vendor can review it by themselves and pay attention to whether other vendor have also fixed the vulnerabilities in the same third-party. It is possible that it will also be affected.

The users who want to use NAS can also pay more attention to not opening the NAS on the external network and unused services should be disabled as much as possible to reduce the attack surface.

## To be continue

In fact, we have not only found one vulnerability, we have also found that there are still many problems. In next part, we will publish more research after most vendor fix it.

Please look forward to Part II.

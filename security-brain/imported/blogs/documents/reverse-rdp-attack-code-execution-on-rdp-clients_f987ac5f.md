---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-05_reverse-rdp-attack-code-execution-on-rdp-clients.md
original_filename: 2019-02-05_reverse-rdp-attack-code-execution-on-rdp-clients.md
title: 'Reverse RDP Attack: Code Execution on RDP Clients'
category: documents
detected_topics:
- cloud-security
- command-injection
- mobile-security
- sso
- path-traversal
- automation-abuse
tags:
- imported
- documents
- cloud-security
- command-injection
- mobile-security
- sso
- path-traversal
- automation-abuse
language: en
raw_sha256: f987ac5f8a0bd6703d2a24d6ebf83777f0de5875a32c6cbf734ef6878a21486d
text_sha256: f9ce4ebda062e692ced4d378d67373f9028c01d5b5a870628367c59fee465f0f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Reverse RDP Attack: Code Execution on RDP Clients

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-05_reverse-rdp-attack-code-execution-on-rdp-clients.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, mobile-security, sso, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `f987ac5f8a0bd6703d2a24d6ebf83777f0de5875a32c6cbf734ef6878a21486d`
- Text SHA256: `f9ce4ebda062e692ced4d378d67373f9028c01d5b5a870628367c59fee465f0f`


## Content

---
title: "Reverse RDP Attack: Code Execution on RDP Clients"
page_title: "Reverse RDP Attack: Code Execution on RDP Clients - Check Point Research"
url: "https://research.checkpoint.com/reverse-rdp-attack-code-execution-on-rdp-clients/"
final_url: "https://research.checkpoint.com/2019/reverse-rdp-attack-code-execution-on-rdp-clients/"
authors: ["Eyal Itkin"]
programs: ["Microsoft"]
bugs: ["Path traversal"]
publication_date: "2019-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5434
---

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [CONTACT US](https://research.checkpoint.com/contact/)
  * [DISCLOSURE POLICY](https://research.checkpoint.com/disclosure-policy/)
  * [CHECKPOINT.COM](https://www.checkpoint.com/)
  * [UNDER ATTACK?](https://www.checkpoint.com/about-us/contact-incident-response/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [Latest Publications](https://research.checkpoint.com/latest-publications/)
  * [CPR Podcast Channel](https://research.checkpoint.com/cpr-podcast-channel/)
  * [AI Research](https://research.checkpoint.com/ai-research/)
  * [Web 3.0 Security](https://research.checkpoint.com/category/web3/)
  * [Intelligence Reports](https://research.checkpoint.com/intelligence-reports/)
  * Resources
  * [ThreatCloud AI](https://www.checkpoint.com/ai/)
  * [Threat Intelligence & Research](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero Day Protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Sandblast File Analysis](http://threatemulation.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [SUBSCRIBE](https://research.checkpoint.com/subscription/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

SUBSCRIBE

## CATEGORIES

  * [ AI Research 16 ](https://research.checkpoint.com/category/ai-research/)
  * [ Android Malware 23 ](https://research.checkpoint.com/category/android-malware/)
  * [ Artificial Intelligence 5 ](https://research.checkpoint.com/category/artificial-intelligence-2/)
  * [ ChatGPT 3 ](https://research.checkpoint.com/category/chatgpt/)
  * [ Check Point Research Publications 460 ](https://research.checkpoint.com/category/threat-research/)
  * [ Cloud Security 1 ](https://research.checkpoint.com/category/cloud-security/)
  * [ CPRadio 44 ](https://research.checkpoint.com/category/cpradio/)
  * [ Crypto 2 ](https://research.checkpoint.com/category/crypto/)
  * [ Data & Threat Intelligence 2 ](https://research.checkpoint.com/category/data-threat-intelligence/)
  * [ Data Analysis 0 ](https://research.checkpoint.com/category/data-analysis/)
  * [ Demos 22 ](https://research.checkpoint.com/category/demos/)
  * [ Global Cyber Attack Reports 412 ](https://research.checkpoint.com/category/threat-intelligence-reports/)
  * [ How To Guides 13 ](https://research.checkpoint.com/category/how-to-guides/)
  * [ Ransomware 5 ](https://research.checkpoint.com/category/ransomware/)
  * [ Russo-Ukrainian War 1 ](https://research.checkpoint.com/category/russo-ukrainian-war/)
  * [ Security Report 1 ](https://research.checkpoint.com/category/security-report/)
  * [ Threat and data analysis 0 ](https://research.checkpoint.com/category/threat-and-data-analysis/)
  * [ Threat Research 175 ](https://research.checkpoint.com/category/threat-research-2/)
  * [ Web 3.0 Security 11 ](https://research.checkpoint.com/category/web3/)
  * [ Wipers 0 ](https://research.checkpoint.com/category/wipers/)

![](https://research.checkpoint.com/wp-content/uploads/2019/01/RDP_blog_1021x580.jpg)

# Reverse RDP Attack: Code Execution on RDP Clients

February 5, 2019 

[](https://www.linkedin.com/shareArticle?mini=true&url=https://research.checkpoint.com/2019/reverse-rdp-attack-code-execution-on-rdp-clients/ -  https://research.checkpoint.com/?p=20554;source=LinkedIn "Share on LinkedIn!") [](http://www.facebook.com/sharer.php?u=https://research.checkpoint.com/2019/reverse-rdp-attack-code-execution-on-rdp-clients/ - https://research.checkpoint.com/?p=20554  "Share on Facebook!") [](http://twitter.com/home/?status=Reverse RDP Attack: Code Execution on RDP Clients - https://research.checkpoint.com/?p=20554 via @kenmata  "Tweet this!")

https://research.checkpoint.com/2019/reverse-rdp-attack-code-execution-on-rdp-clients/

**Research by:** Eyal Itkin

**Overview**  
Used by thousands of IT professionals and security researchers worldwide, the Remote Desktop Protocol (RDP) is usually considered a safe and trustworthy application to connect to remote computers. Whether it is used to help those working remotely or to work in a safe VM environment, RDP clients are an invaluable tool.

However, Check Point Research recently discovered multiple critical vulnerabilities in the commonly used Remote Desktop Protocol (RDP) that would allow a malicious actor to reverse the usual direction of communication and infect the IT professional or security researcher’s computer. Such an infection could then allow for an intrusion into the IT network as a whole.  
16 major vulnerabilities and a total of 25 security vulnerabilities were found overall. The full list can be found in Appendix A & B.

_**7th of August 2019 – New developments in the research:**_

_After the initial publication of our research, our researchers found new implications for the Reverse RDP Attack that also impact Microsoft’s Hyper-V product. Due to these new developments, Microsoft updated their response and issued the vulnerability an official CVE:[CVE-2019-0887](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0887). Full details can be found in the newly published [blog post](https://research.checkpoint.com/reverse-rdp-the-hyper-v-connection)._

**Introduction**  
The Remote Desktop Protocol (RDP), also known as “mstsc” after the Microsoft built-in RDP client, is commonly used by technical users and IT staff to connect to / work on a remote computer. RDP is a proprietary protocol developed by Microsoft and is usually used when a user wants to connect to a remote Windows machine. There are also some popular open-source clients for the RDP protocol that are used mainly by Linux and Mac users.

RDP offers many complex features, such as: compressed video streaming, clipboard sharing, and several encryption layers. We therefore decided to look for vulnerabilities in the protocol and its popular implementations.

In a normal scenario, you use an RDP client, and connect to a remote RDP server that is installed on the remote computer. After a successful connection, you now have access to and control of the remote computer, according to the permissions of your user. But if the scenario could be put in reverse? We wanted to investigate if the RDP server can attack and gain control over the computer of the connected RDP client.

[![](/wp-content/uploads/2019/01/fig-1.png)](/wp-content/uploads/2019/01/fig-1.png)

**Figure 1:** Attack scenario for the RDP protocol

There are several common scenarios in which an attacker can gain elevated network permissions by deploying such an attack, thus advancing his lateral movement inside an organization:

  1. Attacking an IT member that connects to an infected work station inside the corporate network, thus gaining higher permission levels and greater access to the network systems.
  2. Attacking a malware researcher that connects to a remote sandboxed virtual machine that contains a tested malware. This allows the malware to escape the sandbox and infiltrate the corporate network.

Now that we decided on our attack vector, it is time to introduce our targets, the most commonly used RDP clients:

  * mstsc.exe – Microsoft’s built-in RDP client.
  * [FreeRDP](http://www.freerdp.com/) – The most popular and mature open-source RDP client on Github.
  * [rdesktop](https://www.rdesktop.org/) – Older open-source RDP client, comes by default in Kali-linux distros.

**Fun fact:** As “rdesktop” is the built-in client in Kali-linux, a Linux distro used by red teams for penetration testing, we thought of a 3rd (though probably not practical) attack scenario: Blue teams can install organizational honeypots and attack red teams that try to connect to them through the RDP protocol.

**Open-Source RDP clients**

As is usually the case, we decided to start looking for vulnerabilities in the open source clients. It seems that it will only make sense to start reverse engineer Microsoft’s client after we will have a firm understanding of the protocol. In addition, if we find common vulnerabilities in the two open sourced clients, we could check if they also apply to Microsoft’s client. In a recon check it looked like “rdesktop” is smaller than “FreeRDP” (has fewer lines of code), and so we selected it as our first target.

**Note:** We decided to perform an old-fashioned manual code audit instead of using any fuzzing technique. The main reasons for this decision were the overhead of writing a dedicated fuzzer for the complex RDP protocol, together with the fact that using AFL for a protocol with several compression and encryption layers didn’t look like a good idea.

### **rdesktop  
****Tested version:** v1.8.3

After a short period, it looked like the decision to manually search for vulnerabilities paid off. We soon found several vulnerable patterns in the code, making it easier to “feel” the code, and pinpoint the locations of possible vulnerabilities.

We found 11 vulnerabilities with a major security impact, and 19 vulnerabilities overall in the library. For the full list of CVEs for “rdesktop”, see Appendix A.

**Note:** An additional recon showed that the [xrdp](http://www.xrdp.org/) open-source RDP server is based on the code of “rdesktop”. Based on our findings, it appears that similar vulnerabilities can be found in “xrdp” as well.

Instead of a technical analysis of all of the CVEs, we will focus on two common vulnerable code patterns that we found.

**Remote Code Executions – CVEs 2018-20179 – 2018-20181**

Throughout the code of the client, there is an assumption that the server sent enough bytes to the client to process. One example for this assumption can be found in the following code snippet in Figure 2:

[![](/wp-content/uploads/2019/01/fig-2.png)](/wp-content/uploads/2019/01/fig-2.png)

**Figure 2:** Parsing 2 fields from stream “s” without first checking its size

As we can see, the fields “length” and “flags” are parsed from the stream “s”, without checking that “s” indeed contains the required 8 bytes for this parsing operation. While this usually only leads to an Out-Of-Bounds read, we can combine this vulnerability with an additional vulnerability in several of the inner channels and achieve a much more severe effect.

There are three logical channels that share a common vulnerability:

  * lspci
  * rdpsnddbg – yes, this debug channel is always active
  * seamless

The vulnerability itself can be seen in Figure 3:

[![](/wp-content/uploads/2019/01/fig-3.png)](/wp-content/uploads/2019/01/fig-3.png)

**Figure 3** : Integer-Underflow when calculating the remaining “pkglen”

By reading too much data from the stream, i.e. sending a chopped packet to the client, the invariant that “s->p <= s->end” breaks. This leads to an Integer-Underflow when calculating “pkglen”, and to an additional Integer-Overflow when allocating “xmalloc(pkglen + 1)” bytes for our buffer, as can be seen in my comment above the call to “xmalloc”.

Together with the proprietary implementation of “STRNCPY”, seen in Figure 4, we can trigger a massive heap-based buffer overflow when copying data to the tiny allocated heap buffer.

[![](/wp-content/uploads/2019/01/fig-4.png)](/wp-content/uploads/2019/01/fig-4.png)

**Figure 4:** proprietary implementation of the “strncpy” function

By chaining together these two vulnerabilities, found in three different logical channels, we now have three **remote code execution** vulnerabilities.

**CVE 2018-8795 – Remote Code Execution**

Another classic vulnerability is an Integer-Overflow when processing the received bitmap (screen content) updates, as can be seen in Figure 5:

[![](/wp-content/uploads/2019/01/fig-5.png)](/wp-content/uploads/2019/01/fig-5.png)

**Figure 5:** Integer-Overflow when processing bitmap updates

Although “width” and “height” are only 16 bits each, by multiplying them together with “Bpp” (bits-per-pixel), we can trigger an Integer-Overflow. Later on, the bitmap decompression will process our input and break on any decompression error, giving us a controllable heap-based buffer-overflow.

**Note:** This tricky calculation can be found in several places throughout the code of “rdesktop”, so we marked it as a potential vulnerability to check for in “FreeRDP”.

### **FreeRDP  
****Tested version:** 2.0.0-rc3

After finding multiple vulnerabilities in “rdesktop”, we approached “FreeRDP” with some trepidation; perhaps only “rdesktop” had vulnerabilities when implementing RDP? We still can’t be sure that every implementation of the protocol will be vulnerable.

And indeed, at first glance, the code seemed much better: there are minimal size checks before parsing data from the received packet, and the code “feels” more mature. It is going to be a challenge. However, after a deeper examination, we started to find cracks in the code, and eventually we found critical vulnerabilities in this client as well.

We found 5 vulnerabilities with major security impact, and 6 vulnerabilities overall in the library. For the full list of CVEs for “FreeRDP”, see Appendix B.

**Note:** An additional recon showed that the RDP client [NeutrinoRDP](https://github.com/neutrinolabs/NeutrinoRDP) is a fork of an older version (1.0.1) of “FreeRDP” and therefore probably suffers from the same vulnerabilities.

At the end of our research, we developed a PoC exploit for CVE 2018-8786, as can be seen in this video:

**CVE 2018-8787 – Same Integer-Overflow**

As we saw earlier in “rdesktop”, calculating the dimensions of a received bitmap update is susceptible to Integer-Overflows. And indeed, “FreeRDP” shares the same vulnerability:

[![](/wp-content/uploads/2019/01/fig-6.png)](/wp-content/uploads/2019/01/fig-6.png)

**Figure 6:** Same Integer-Overflow when processing bitmap updates

**Remote Code Execution – CVE 2018-8786**

[![](/wp-content/uploads/2019/01/fig-7.png)](/wp-content/uploads/2019/01/fig-7.png)

**Figure 7:** Integer-Truncation when processing bitmap updates

As can be seen in Figure 7, there is an Integer-Truncation when trying to calculate the required capacity for the bitmap updates array. Later on, rectangle structs will be parsed from our packet and into the memory of the too-small allocated buffer.

This specific vulnerability is followed by a controlled amount (“bitmapUpdate->number”) of heap allocations (with a controlled size) when the rectangles are parsed and stored to the array, granting the attacker a great heap-shaping primitive. The downside of this vulnerability is that most of the rectangle fields are only 16 bits wide, and are upcasted to 32 bits to be stored in the array. Despite this, we managed to exploit this CVE in our PoC. Even this partially controlled heap-based buffer-overflow is enough for a **remote code execution**.

### **Mstsc.exe – Microsoft’s RDP client  
****Tested version:** Build 18252.rs_prerelease.180928-1410

After we finished checking the open source implementations, we felt that we had a pretty good understanding of the protocol and can now start to reverse engineer Microsoft’s RDP client. But first thing first, we need to find which binaries contain the logic we want to examine. The *.dll files and *.exe files we chose to focus on:

  * rdpbase.dll – Protocol layer for the RDP client.
  * rdpserverbase.dll – Protocol layer for the RDP server.
  * rdpcore.dll / rdpcorets.dll – Core logic for the RDP engine.
  * rdpclip.exe – An .exe we found and that we will introduce later on.
  * mstscax.dll – Mostly the same RDP logic, used by mstsc.exe.

**Testing prior vulnerabilities**

We started by testing our PoCs for the vulnerabilities in the open-source clients. Unfortunately, all of them caused the client to close itself cleanly, without any crash. Having no more excuses, we opened IDA and started to track the flow of the messages. Soon enough, we realized that Microsoft’s implementation is much better than the implementations we tested previously. Actually, it seems like Microsoft’s code is better by several orders of magnitude, as it contains:

  * Several optimization layers for efficient network streaming of the received video.
  * Robust input checks.
  * Robust decompression checks, to guarantee that no byte will be written past the destination buffer.
  * Additional supported clipboard features.
  * …

Needless to say, there were checks for Integer-Overflows when processing bitmap updates.

### 

**Wait a minute, they share a clipboard?**

When we checked “rdesktop” and “FreeRDP”, we found several vulnerabilities in the clipboard sharing channel (every logical data layer is called a channel). However, at the time, we didn’t pay much attention to it because they only shared two formats: raw text and Unicode text. This time it seems that Microsoft supports several more shared data formats, as the switch table we saw was much bigger than before.

After reading more about the different formats in [MSDN](https://docs.microsoft.com/en-us/windows/desktop/shell/clipboard#cf_hdrop), one format immediately attracted our attention: “CF_HDROP”. This format seems responsible for “Drag & Drop” (hence the name H**DROP**), and in our case, the “Copy & Paste” feature. It’s possible to simply copy a group of files from the first computer, and paste them in the second computer. For example, a malware researcher might want to copy the output log of his script from the remote VM to his desktop.

It was roughly at this point, while I was trying to figure out the flow of the data, Omer ([@GullOmer](https://twitter.com/gullomer?lang=en)) asked me if and where [PathCanonicalizeA](https://docs.microsoft.com/en-us/windows/desktop/api/shlwapi/nf-shlwapi-pathcanonicalizea) _is called_. If the client fails to properly canonicalize and sanitize the file paths it receives, it could be vulnerable to a path-traversal attack, allowing the server to drop arbitrary files in arbitrary paths on the client’s computer, a very strong attack primitive. After failing to find imports for the canonicalization function, we dug in deeper, trying to figure out the overall architecture for this data flow.

Figure 8 summarizes our findings:

[![](/wp-content/uploads/2019/01/fig-8-1024x229.png)](/wp-content/uploads/2019/01/fig-8.png)

**Figure 8:** Architecture of the clipboard sharing in Microsoft’s RDP

This is where rdpclip.exe comes into play. It turns out that the server accesses the clipboard through a broker, and that is rdpclip.exe. In fact, rdpclip.exe is just a normal process (we can kill / spawn it ourselves) that talks to the RDP service using a dedicated virtual channel API.

At this stage, we installed [ClipSpy](https://www.codeproject.com/Articles/168/ClipSpy), and started to dynamically debug the clipboard’s data handling that is done inside rdpclip.exe.

These are our conclusions regarding the data flow in an ordinary “Copy & Paste” operation in which a file is copied from the server to the client:

  1. On the server, the “copy” operation creates a clipboard data of the format “CF_HDROP”.
  2. When the “paste” is performed in the client’s computer, a chain of events is triggered.
  3. The rdpclip.exe process on the server is asked for the clipboard’s content, and converts it to a FileGroupDescriptor (Fgd) clipboard format.
  4. The metadata of the files is added to the descriptor one at a time, using the HdropToFgdConverter::AddItemToFgd() function.
  5. After it is finished, the Fgd blob is sent to the RDP service on the server.
  6. The server simply wraps it and sends it to the client.
  7. The client unwraps it and stores it in its own clipboard.
  8. A “paste” event is sent to the process of the focused window (for example, explorer.exe).
  9. This process handles the event and reads the data from the clipboard.
  10. The content of the files is received over the RDP connection itself.

**Path Traversal over the shared RDP clipboard**

If we look back on the steps performed on the received clipboard data, we notice that the client doesn’t verify the received Fgd blob that came from the RDP server. And indeed, if we modify the server to include a path traversal path of the form: ..\canary1.txt, ClipSpy shows us (see Figure 9) that it was stored “as is” on the client’s clipboard:

[![](/wp-content/uploads/2019/01/fig-9.png)](/wp-content/uploads/2019/01/fig-9.png)

**Figure 9:** Fgd with a path-traversal was stored on the client’s clipboard

In Figure 10, we can see how explorer.exe treats a path traversal of ..\filename.txt:

[![](/wp-content/uploads/2019/01/fig-10.png)](/wp-content/uploads/2019/01/fig-10.png)

**Figure 10:** Fgd with a path-traversal as explorer.exe handles it

Just to make sure, after the “paste” in folder “Inner”, the file is stored to “Base” instead:

[![](/wp-content/uploads/2019/01/fig-11.png)](/wp-content/uploads/2019/01/fig-11.png)

**Figure 11:** Folders after a successful path traversal attack

And that’s practically it.

If a client uses the “Copy & Paste” feature over an RDP connection, a malicious RDP server can transparently drop arbitrary files to arbitrary file locations on the client’s computer, limited only by the permissions of the client. For example, we can drop malicious scripts to the client’s “Startup” folder, and after a reboot they will be executed on his computer, giving us full control.

**Note:** In our exploit, we simply killed rdpclip.exe, and spawned our own process to perform the path traversal attack by adding additional malicious file to every “Copy & Paste” operation. The attack was performed with “user” permissions, and does not require the attacker to have “system” or any other elevated permission.

Here is a video of our PoC exploit:

**Taking it one step further**

Every time a clipboard is updated on either side of the RDP connection, a [CLIPRDR_FORMAT_LIST](https://msdn.microsoft.com/en-us/library/cc241105.aspx) message is sent to the other side, to notify it about the new clipboard formats that are now available. We can think of it as a complete sync between the clipboards of both parties (except for a small set of formats that are treated differently by the RDP connection itself). This means that our malicious server is notified whenever the client copies something to his “local” clipboard, and it can now query the values and read them. In addition, the server can notify the client about a clipboard “update” **without the need for a “copy” operation** **inside the RDP window** , thus completely controlling the client’s clipboard without being noticed.

**Scenario #1:**

A malicious RDP server can eavesdrop on the client’s clipboard – this is a feature, not a bug. For example, the client locally copies an admin password, and now the server has it too.

**Scenario #2:**

A malicious RDP server can modify any clipboard content used by the client, even if the client does **not** issue a “copy” operation inside the RDP window. If you click “paste” when an RDP connection is open, you are vulnerable to this kind of attack. For example, if you copy a file on your computer, the server can modify your (executable?) file / piggy-back your copy to add additional files / path-traversal files using the previously shown PoC.

We were able to successfully test this attack scenario using [NCC’s .NET deserialization](https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2018/december/beware-of-deserialisation-in-.net-methods-and-classes-code-execution-via-paste/) PoC:

  1. The server executes their PoC, and positions in the clipboard a .NET content that will pop a calculator (using the “System.String” format).
  2. When the client clicks “paste” inside the PowerShell program, the deserialization occurs and a calc is popped.

**Note:** The content of the synced clipboard is subject to [Delayed Rendering](https://msdn.microsoft.com/en-us/library/cc241081.aspx). This means that the clipboard’s content is sent over the RDP connection only after a program actively asks for it, usually by clicking “paste”. Until then, the clipboard only holds the list of formats that are available, without holding the content itself.

**Disclosure Timeline**

  * 16 October 2018 – Vulnerability was disclosed to Microsoft.
  * 22 October 2018 – Vulnerabilities were disclosed to FreeRDP.
  * 22 October 2018 – FreeRDP replied and started working on a patch.
  * 28 October 2018 – Vulnerabilities were disclosed to rdesktop.
  * 5 November 2018 – FreeRDP sent us the patches and asked for us to verify them.
  * 18 November 2018 – We verified the patches of FreeRDP, and gave them a “green light” to continue.
  * 20 November 2018 – FreeRDP committed the patches to their Github as part of 2.0.0-rc4.
  * 17 December 2018 – Microsoft acknowledged our findings. For more information, see **Microsoft’s Response**.
  * 19 December 2018 – rdesktop sent us the patches and asked us to verify them.
  * 19 December 2018 – We verified the patches of rdesktop, and gave them a “green light” to continue.
  * 16 January 2019 – rdesktop committed the patches to their Github as part of v1.8.4.

**Microsoft’s Response**

During the responsible disclosure process, we sent the details of the path traversal in mstsc.exe to Microsoft.

This is Microsoft’s official response:

“Thank you for your submission. We determined your finding is valid but does not meet our bar for servicing. For more information, please see the Microsoft Security Servicing Criteria for Windows (https://aka.ms/windowscriteria).”

As a result, this path traversal has no CVE-ID, and there is no patch to address it.

**Conclusion**

During our research, we found numerous critical vulnerabilities in the tested RDP clients. Although the code quality of the different clients varies, as can be seen by the distribution of the vulnerabilities we found, we argue that the remote desktop protocol is complicated, and is prone to vulnerabilities. As we demonstrated in our PoCs for both Microsoft’s client and one of the open-sourced clients, a malicious RDP server can leverage the vulnerabilities in the RDP clients to achieve remote code execution over the client’s computer.

As RDP is regularly used by IT staff and technical workers to connect to remote computers, we highly recommend that everyone patch their RDP clients. In addition, due to the nature of the clipboard findings we showed in Microsoft’s RDP client, we recommend users to disable the clipboard sharing channel (on by default) when connecting to a remote machine.

**Recommendation for Protection**

Check Point recommends the following steps in order to protect against this attack:

  1. Check Point Research worked closely with FreeRDP, rdesktop and Microsoft to mitigate these vulnerabilities.  
If you are using rdesktop or FreeRDP, update to the latest version which includes the relevant patches.
  2. When using Microsoft RDP client (MSTSC), we strongly recommend disabling bi-directional clipboard sharing over RDP.
  3. Apply security measures to both the clients and the servers involved in the RDP communication.  
Check Point provides various security layers that may be used for protection such as [IPS](https://www.checkpoint.com/products/ips-software-blade/), [SandBlast Agent](https://www.checkpoint.com/products/advanced-endpoint-protection/), [Threat Emulation](https://www.checkpoint.com/products/threat-emulation-sandboxing/) and ANTEX.
  4. Users should avoid using RDP to connect to remote servers that have not implemented sufficient security measures.
  5. Check Point’s [IPS blade](https://www.checkpoint.com/products/ips-software-blade/) provides protections against these threats: 
  1. “FreeRDP Remote Code Execution (CVE-2018-8786)”

**Appendix A – CVEs found in rdesktop:**

  * [CVE 2018-8791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8791): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function rdpdr_process() that results in an information leak.
  * [CVE 2018-8792](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8792): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function cssp_read_tsrequest() that results in a Denial of Service (segfault).
  * [CVE 2018-8793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8793): rdesktop versions up to and including v1.8.3 contain a Heap-Based Buffer Overflow in function cssp_read_tsrequest() that results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8794](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8794): rdesktop versions up to and including v1.8.3 contain an Integer Overflow that leads to an Out-Of-Bounds Write in function process_bitmap_updates() and results in a memory corruption and possibly even a remote code execution.
  * [CVE 2018-8795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8795): rdesktop versions up to and including v1.8.3 contain an Integer Overflow that leads to a Heap-Based Buffer Overflow in function process_bitmap_updates() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8796): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function process_bitmap_updates() that results in a Denial of Service (segfault).
  * [CVE 2018-8797](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8797): rdesktop versions up to and including v1.8.3 contain a Heap-Based Buffer Overflow in function process_plane() that results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8798): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function rdpsnd_process_ping() that results in an information leak.
  * [CVE 2018-8799](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8799): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function process_secondary_order() that results in a Denial of Service (segfault).
  * [CVE 2018-8800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8800): rdesktop versions up to and including v1.8.3 contain a Heap-Based Buffer Overflow in function ui_clip_handle_data() that results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-20174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20174): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function ui_clip_handle_data() that results in an information leak.
  * [CVE 2018-20175](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20175): rdesktop versions up to and including v1.8.3 contains several Integer Signedness errors that leads to Out-Of-Bounds Reads in file mcs.c and result in a Denial of Service (segfault).
  * [CVE 2018-20176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20176): rdesktop versions up to and including v1.8.3 contains several Out-Of-Bounds Reads in file secure.c that result in a Denial of Service (segfault).
  * [CVE 2018-20177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20177): rdesktop versions up to and including v1.8.3 contain an Integer Overflow that leads to a Heap-Based Buffer Overflow in function rdp_in_unistr() and results in a memory corruption and possibly even a remote code execution.
  * [CVE 2018-20178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20178): rdesktop versions up to and including v1.8.3 contain an Out-Of-Bounds Read in function process_demand_active() that results in a Denial of Service (segfault).
  * [CVE 2018-20179](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20179): rdesktop versions up to and including v1.8.3 contain an Integer Underflow that leads to a Heap-Based Buffer Overflow in function lspci_process() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-20180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20180): rdesktop versions up to and including v1.8.3 contain an Integer Underflow that leads to a Heap-Based Buffer Overflow in function rdpsnddbg_process() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-20181](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20181): rdesktop versions up to and including v1.8.3 contain an Integer Underflow that leads to a Heap-Based Buffer Overflow in function seamless_process() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-20182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20182): rdesktop versions up to and including v1.8.3 contain a Buffer Overflow over the global variables in function seamless_process_line() that results in a memory corruption and probably even a remote code execution.

**Appendix B – CVEs found in FreeRDP:**

  * [CVE 2018-8784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8784): FreeRDP prior to version 2.0.0-rc4 contains a Heap-Based Buffer Overflow in function zgfx_decompress_segment() that results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8785](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8785): FreeRDP prior to version 2.0.0-rc4 contains a Heap-Based Buffer Overflow in function zgfx_decompress() that results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8786): FreeRDP prior to version 2.0.0-rc4 contains an Integer Truncation that leads to a Heap-Based Buffer Overflow in function update_read_bitmap_update() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8787): FreeRDP prior to version 2.0.0-rc4 contains an Integer Overflow that leads to a Heap-Based Buffer Overflow in function gdi_Bitmap_Decompress() and results in a memory corruption and probably even a remote code execution.
  * [CVE 2018-8788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8788): FreeRDP prior to version 2.0.0-rc4 contains an Out-Of-Bounds Write of up to 4 bytes in function nsc_rle_decode() that results in a memory corruption and possibly even a remote code execution.
  * [CVE 2018-8789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8789): FreeRDP prior to version 2.0.0-rc4 contains several Out-Of-Bounds Reads in the NTLM Authentication module that results in a Denial of Service (segfault).

![](https://research.checkpoint.com/wp-content/uploads/2022/10/back_arrow.svg) GO UP 

[BACK TO ALL POSTS](/latest-publications/)

## POPULAR POSTS

[ ![](https://research.checkpoint.com/wp-content/uploads/2023/01/AI-1059x529-copy.jpg) ](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OPWNAI : Cybercriminals Starting to Use ChatGPT](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2019/01/Fortnite_1021x580.jpg) ](https://research.checkpoint.com/2019/hacking-fortnite/)

  * Check Point Research Publications
  * Threat Research

[Hacking Fortnite Accounts](https://research.checkpoint.com/2019/hacking-fortnite/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2022/12/OpenAIchatGPT_header.jpg) ](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OpwnAI: AI That Can Save the Day or HACK it Away](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

### BLOGS AND PUBLICATIONS

[ ![](https://research.checkpoint.com/wp-content/uploads/2020/02/CheckPointResearchTurkishRat_blog_header.jpg) ](https://research.checkpoint.com/2020/the-turkish-rat-distributes-evolved-adwind-in-a-massive-ongoing-phishing-campaign/)

  * Check Point Research Publications
  * Global Cyber Attack Reports
  * Threat Research

February 17, 2020

### “The Turkish Rat” Evolved Adwind in a Massive Ongoing Phishing Campaign

[ ![](https://research.checkpoint.com/wp-content/uploads/2017/08/WannaCry-Post-No-Image-1021x450.jpg) ](https://research.checkpoint.com/2017/the-next-wannacry-vulnerability-is-here/)

  * Check Point Research Publications

August 11, 2017

### “The Next WannaCry” Vulnerability is Here

[ ![](https://research.checkpoint.com/wp-content/uploads/2026/03/Handala-void-1-scaled.png) ](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)

  * Check Point Research Publications

March 12, 2026

### “Handala Hack” – Unveiling Group’s Modus Operandi

[![](https://research.checkpoint.com/wp-content/uploads/2022/12/CheckPointResearchLogo_white-1-e1671590634727.png)](https://research.checkpoint.com)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

  * Publications
  * [Global cyber attack reports](/category/threat-intelligence-reports/)
  * [Research publications](/category/threat-research/)
  * [IPS advisories](https://advisories.checkpoint.com/advisories/)
  * [Check point blog](https://blog.checkpoint.com/)
  * [Demos](/category/demos/)
  * Tools
  * [Sandblast file analysis](http://threatemulation.checkpoint.com/)
  * [ThreatCloud](https://www.checkpoint.com/infinity/threatcloud/)
  * [Threat Intelligence](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero day protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Live threat map](https://threatmap.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [Contact Us](https://research.checkpoint.com/contact/)

### Let’s get in touch

Subscribe for cpr blogs, news and more

[Subscribe Now](/subscription/)

© 1994-2026 Check Point Software Technologies LTD. All rights reserved.

Property of [CheckPoint.com](https://www.checkpoint.com/)

[Privacy Policy](/privacy-policy/)

![](https://research.checkpoint.com/wp-content/uploads/2022/10/popup-side-image.jpg)

## SUBSCRIBE TO CYBER INTELLIGENCE REPORTS

First Name

Last Name

Country—Please choose an option—ChinaIndiaUnited StatesIndonesiaBrazilPakistanNigeriaBangladeshRussiaJapanMexicoPhilippinesVietnamEthiopiaEgyptGermanyIranTurkeyDemocratic Republic of the CongoThailandFranceUnited KingdomItalyBurmaSouth AfricaSouth KoreaColombiaSpainUkraineTanzaniaKenyaArgentinaAlgeriaPolandSudanUgandaCanadaIraqMoroccoPeruUzbekistanSaudi ArabiaMalaysiaVenezuelaNepalAfghanistanYemenNorth KoreaGhanaMozambiqueTaiwanAustraliaIvory CoastSyriaMadagascarAngolaCameroonSri LankaRomaniaBurkina FasoNigerKazakhstanNetherlandsChileMalawiEcuadorGuatemalaMaliCambodiaSenegalZambiaZimbabweChadSouth SudanBelgiumCubaTunisiaGuineaGreecePortugalRwandaCzech RepublicSomaliaHaitiBeninBurundiBoliviaHungarySwedenBelarusDominican RepublicAzerbaijanHondurasAustriaUnited Arab EmiratesIsraelSwitzerlandTajikistanBulgariaHong Kong (China)SerbiaPapua New GuineaParaguayLaosJordanEl SalvadorEritreaLibyaTogoSierra LeoneNicaraguaKyrgyzstanDenmarkFinlandSlov***REDACTED-AWS-KEY***istanNorwayLebanonCosta RicaCentral African RepublicIrelandGeorgiaNew ZealandRepublic of the CongoPalestineLiberiaCroatiaOmanBosnia and HerzegovinaPuerto RicoKuwaitMoldovMauritaniaPanamaUruguayArmeniaLithuaniaAlbaniaMongoliaJamaicaNamibiaLesothoQatarMacedoniaSloveniaBotswanaLatviaGambiaKosovoGuinea-BissauGabonEquatorial GuineaTrinidad and TobagoEstoniaMauritiusSwazilandBahrainTimor-LesteDjiboutiCyprusFijiReunion (France)GuyanaComorosBhutanMontenegroMacau (China)Solomon IslandsWestern SaharaLuxembourgSurinameCape VerdeMaltaGuadeloupe (France)Martinique (France)BruneiBahamasIcelandMaldivesBelizeBarbadosFrench Polynesia (France)VanuatuNew Caledonia (France)French Guiana (France)Mayotte (France)SamoaSao Tom and PrincipeSaint LuciaGuam (USA)Curacao (Netherlands)Saint Vincent and the GrenadinesKiribatiUnited States Virgin Islands (USA)GrenadaTongaAruba (Netherlands)Federated States of MicronesiaJersey (UK)SeychellesAntigua and BarbudaIsle of Man (UK)AndorraDominicaBermuda (UK)Guernsey (UK)Greenland (Denmark)Marshall IslandsAmerican Samoa (USA)Cayman Islands (UK)Saint Kitts and NevisNorthern Mariana Islands (USA)Faroe Islands (Denmark)Sint Maarten (Netherlands)Saint Martin (France)LiechtensteinMonacoSan MarinoTurks and Caicos Islands (UK)Gibraltar (UK)British Virgin Islands (UK)Aland Islands (Finland)Caribbean Netherlands (Netherlands)PalauCook Islands (NZ)Anguilla (UK)Wallis and Futuna (France)TuvaluNauruSaint Barthelemy (France)Saint Pierre and Miquelon (France)Montserrat (UK)Saint Helena, Ascension and Tristan da Cunha (UK)Svalbard and Jan Mayen (Norway)Falkland Islands (UK)Norfolk Island (Australia)Christmas Island (Australia)Niue (NZ)Tokelau (NZ)Vatican CityCocos (Keeling) Islands (Australia)Pitcairn Islands (UK)

Email

## We value your privacy!

BFSI uses cookies on this site. We use cookies to enable faster and easier experience for you. By continuing to visit this website you agree to our use of cookies.

ACCEPT

REJECT

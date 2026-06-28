---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-08_go-blue-a-protection-plan-for-credentials-in-chromium-based-browsers.md
original_filename: 2022-06-08_go-blue-a-protection-plan-for-credentials-in-chromium-based-browsers.md
title: Go BLUE! A Protection Plan for Credentials in Chromium-based Browsers
category: documents
detected_topics:
- automation-abuse
- supply-chain
- command-injection
- path-traversal
- mfa
- otp
tags:
- imported
- documents
- automation-abuse
- supply-chain
- command-injection
- path-traversal
- mfa
- otp
language: en
raw_sha256: 1edc192e500200cfe70af4c8f6d9398a01a17818a7b943e63dbe722b19b9062f
text_sha256: ef292f30b1ddb256cb51e93faf64a7f4b32e138882cae81f90577fcc423a4d96
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Go BLUE! A Protection Plan for Credentials in Chromium-based Browsers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-08_go-blue-a-protection-plan-for-credentials-in-chromium-based-browsers.md
- Source Type: markdown
- Detected Topics: automation-abuse, supply-chain, command-injection, path-traversal, mfa, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `1edc192e500200cfe70af4c8f6d9398a01a17818a7b943e63dbe722b19b9062f`
- Text SHA256: `ef292f30b1ddb256cb51e93faf64a7f4b32e138882cae81f90577fcc423a4d96`


## Content

---
title: "Go BLUE! A Protection Plan for Credentials in Chromium-based Browsers"
url: "https://www.cyberark.com/resources/threat-research-blog/go-blue-a-protection-plan-for-credentials-in-chromium-based-browsers"
final_url: "https://www.cyberark.com/resources/threat-research-blog/go-blue-a-protection-plan-for-credentials-in-chromium-based-browsers"
authors: ["Zeev Ben Porat"]
programs: ["Google (Chromium)"]
bugs: ["Browser hacking"]
publication_date: "2022-06-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2577
---

# Go BLUE! A Protection Plan for Credentials in Chromium-based Browsers

June 8, 2022 Zeev Ben Porat

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fgo-blue-a-protection-plan-for-credentials-in-chromium-based-browsers)
  * [Twitter](https://twitter.com/share?text=Go%20BLUE%21%20A%20Protection%20Plan%20for%20Credentials%20in%20Chromium-based%20Browsers&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fgo-blue-a-protection-plan-for-credentials-in-chromium-based-browsers&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#e3dc90968189868097dea08c8d97868d97c6d1d385918c8ec6d1d38e9ac6d1d3ab9681c6d1d2c5828e93d8818c879adea08b868088c6d1d38c9697c6d1d3948b8297c6d1d490c6d1d38b829393868d8a8d84c6d1d38297c6d1d3a09a818691a29188c6d1d2c6d3a2c6d3a2a48cc6d1d3a1afb6a6c6d1d2c6d1d3a2c6d1d3b3918c978680978a8c8dc6d1d3b38f828dc6d1d3858c91c6d1d3a0918687868d978a828f90c6d1d38a8dc6d1d3a08b918c8e8a968ece8182908687c6d1d3a1918c9490869190c6d3a2aa8dc6d1d38e9ac6d1d3939186958a8c9690c6d1d3818f8c84c6d1d3938c9097c6d1d3c6d1db8b869186c6d1dac6d1a0c6d1d3aac6d1d387869080918a818687c6d1d382c6d1d39786808b8d8a929686c6d1d3978cc6d1d3869b9791828097c6d1d390868d908a978a9586c6d1d387829782c6d1d3c6d1db93829090948c918790c6d1a0c6d1d3808c8c888a8690c6d1dac6d1d3878a918680978f9ac6d1d385918c8ec6d1d3978b86c6d1d38e868e8c919ac6d1d38c85c6d1d382c6d1d3a08b918c8e8a968ece8182908687c6d1d381918c94908691c6a6d1c6dbd3c6dada90c6d1d3c6d6a1a0a1a1c6d6a7c6d1d393918c80869090cdc6d1d3a48c8c848f86c6a6d1c6dbd3c6dada90c6d1d3918690938c8d9086c6d1d3978ccdcdcdc6d3a2c6d3a28b97979390c6d0a2c6d1a5c6d1a5949494cd809a818691829188cd808c8ec6d1a59186908c9691808690c6d1a5978b91868297ce918690868291808bce818f8c84c6d1a5848cce818f9686ce82ce93918c978680978a8c8dce938f828dce858c91ce80918687868d978a828f90ce8a8dce808b918c8e8a968ece8182908687ce81918c9490869190)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fgo-blue-a-protection-plan-for-credentials-in-chromium-based-browsers&title=Go%20BLUE%21%20A%20Protection%20Plan%20for%20Credentials%20in%20Chromium-based%20Browsers&summary=In%20my%20previous%20blog%20post%20%28here%29%2C%20I%20described%20a%20technique%20to%20extract%20sensitive%20data%20%28passwords%2C%20cookies%29%20directly%20from%20the%20memory%20of%20a%20Chromium-based%20browser%E2%80%99s%20%5BCBB%5D%20process.%20Google%E2%80%99s%20response%20to...)

![](https://www.cyberark.com/wp-content/uploads/2022/05/Blue-1-header-image.png)

In my previous blog post ([here](https://www.cyberark.com/resources/threat-research-blog/extracting-clear-text-credentials-directly-from-chromium-s-memory)), I described a technique to extract sensitive data (passwords, cookies) directly from the memory of a Chromium-based browser’s [CBB] process. Google’s response to the responsible disclosure was discouraging, stating “Won’t Fix” since “there is no way for Chrome (or **any** application) to defend against a malicious user who has managed to log into your device as you” ([here](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/security/faq.md#why-arent-physically_local-attacks-in-chromes-threat-model)).

When I showed this work to some of the experienced security researchers on my team, the general reaction was that it is not very interesting, since there are other known methods to get the same information. Naturally, I was disappointed, but to be completely frank – I was also frustrated! We work in a cybersecurity company, and we all embrace the “assume breach” paradigm. I felt our job was to identify malicious attack vectors and block them before the bad guys do, and a cry was welling up inside me:

Wake up! We are the defense team! **GO BLUE**!

Hence this blog, in which I try to map the known attack vectors on sensitive data in Chromium-based browsers, propose mitigations for these attack vectors, and demonstrate how some of these mitigations already work in at least one security application (CyberArk Endpoint Privilege Manager).

### TL;DR

  * Sensitive information (passwords, session-cookies, etc.) is processed and stored by browsers. This information is a prime target of malicious credential stealers.
  * Weaknesses in the protection of this information in Chromium-based browsers have been known for many years, and attack tools have been published that demonstrate how the information can be stolen.
  * In response to our reported vulnerabilities, Chromium.org indicates that it will not fix the product to protect against attacks carried out by a program running locally on the endpoint.
  * The major attack vectors on this sensitive data are identified and mapped.
  * A comprehensive Kernel level protection plan is proposed.
  * Current implementation of major portions of the protection plan in CyberArk Endpoint Privilege Manager is demonstrated.

### Background

Vulnerabilities in web applications have been known for quite a while. A good [blog post](https://resources.infosecinstitute.com/topic/browser-based-vulnerabilities-in-web-applications/) on this subject was published by Satyam Singh in March 2015. Among other issues, he reports that passwords are stored as clear text in the browser’s memory and suggests a possible mitigation (salted hashing).

This report, like many others, has been mostly neglected. I did not see any web applications that adopted the salted hashing mitigation or anything similar. There are several known attack techniques/tools that bypass many of the popular endpoint protection products (AVs, EDRs). It is important to note that many of these published tools do not need admin privileges.

In this blog post, I propose a plan to protect sensitive data in CBBs (most of it also applicable to other browser types, I believe). The proposed mitigations (blocking actions) are all done in a kernel-mode filter driver[s]. They are meant to block (or make the attack much harder for) both standard and elevated processes (but not kernel-mode code).

### Where Are the “Secrets?”

Sensitive data is stored and processed by CBBs in different locations/process routes. To provide comprehensive protection for this data, one needs to address all of the following locations/processes:

  1. Files on disk
  2. Browser’s VM
  3. Keyed-in data (from Keyboard)
  4. SSL-encrypted messages on their way to the web
  5. Information delivered by the browser (if you ask nicely)

### “Tora! Tora! Tora!” – Main Attack Vectors

There is a multitude of tools and malicious products that “steal” browsers’ “secrets.” In this section, I summarize the underlying techniques (aka “attack vectors”) with a small set of actual samples.

**A) Decrypt encoded “secret” values stored in files on disk ([MITRE T1555/003](https://attack.mitre.org/techniques/T1555/003/))**  
This is a very common technique that is widely used by credential stealers. Sensitive information is stored by Chromium in disk files using DPAPI encryption. There are published tools that show how to decrypt these values if you run as the original user.

Sample published tool: **LaZagne**([MITRE S0349](https://attack.mitre.org/software/S0349/)) [GitHub [here](https://github.com/AzizKpln/Lazagne-Reverse-Engineering)] **  
** Sample Credential Stealer: **Redline** [Analysis by Cyberint [here](https://cyberint.com/blog/research/redline-stealer/)]

**B) Extract “secrets” stored in clear-text format from browser’s Virtual Memory ([MITRE T1555/003](https://attack.mitre.org/techniques/T1555/003/))**

As mentioned above, it has been known for a long time that sensitive information is stored in browsers’ Virtual Memory in clear-text format. We shall consider (in the mitigation section below) three different methods to get the memory data:

a) Access browser from an external process:  
`**hProcess** = OpenProcess(PROCESS_VM_READ, FALSE, <browser process pid>) ;  
ReadProcessMemory(**hProcess** , …);`

b) Create a browser process:  
`CreateProcess (0, <browser Activation Command>,…, pStartupInfo, **hProcess**);  
ReadProcessMemory(**hProcess** , …);`

c) Activate a dump utility to dump the memory of the browser process

Sample published tool: **mimikittenz**[GitHub [here](https://github.com/orlyjamie/mimikittenz)] **  
** Sample published tool: my previous blog [[here](https://www.cyberark.com/resources/threat-research-blog/extracting-clear-text-credentials-directly-from-chromium-s-memory)]

**C) Ask the browser nicely (use command line arguments) ([MITRE T1539](https://attack.mitre.org/techniques/T1539/))**

A hacker known as “Alex” (@mangopdf) published in 2018 a method to activate the browser with a command line parameter (- -remote-debugging-port) that lets you ask the browser “nicely” to give you all its cookies (via a TCP “remote debugging port”).

Sample published tool: **cookie_crimes**[GitHub [here](https://github.com/defaultnamehere/cookie_crimes). “Alex”’s Blog [here](https://mango.pdf.zone/stealing-chrome-cookies-without-a-password)]  
A useful implementation**: WhiteChocolateMacademiaNut** [GitHub [here](https://github.com/slyd0g/WhiteChocolateMacademiaNut)]

**D) Code injection into the browser process ([MITRE T1185](https://attack.mitre.org/techniques/T1185/))**

Obviously, code injected into the browser process can implement attacks “A” and “B” above. Additional attacks that can be implemented include:

– Logging input characters (to capture passwords)  
– Hooking the SSL encryption function (to capture clear-text passwords, cookies and more)  
– Hooking other functions to bypass protection mechanisms

Sample exploiter: **Cobalt Strike** ([MITRE S0154](https://attack.mitre.org/software/S0154/))  
Sample exploiter: **chaes**[[MITRE S0631](https://attack.mitre.org/software/S0631/)]

A Cybereason report [[here](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)] on **chaes** states that “browser hooking is the hallmark feature of most financial malware.”

**E) Keylogging ([MITRE T1056](https://attack.mitre.org/techniques/T1056/001/))**

Keylogging can be used to capture “secrets” such as passwords. We shall focus for now only on user-mode standard process attacks.

Sample tool: **Basic-Windows-keylogger** (GitHub [here](https://github.com/ghostlulzhacks/Basic-Windows-keylogger), blog [here](https://medium.com/@ghostlulzhacks/malware-basic-windows-key-logger-746cc09e66aa))  
Sample Credential Stealer: **AppleSeed** ([MITRE S0622](https://attack.mitre.org/software/S0622/)) used by [**Kimsuky**](https://attack.mitre.org/groups/G0094) ([MITRE G0094](https://attack.mitre.org/groups/G0094/))

**F) Adversary in the middle ([MITRE T1539](https://attack.mitre.org/techniques/T1539/), [MITRE T1557](https://attack.mitre.org/techniques/T1557/)) **

An AiTM attack on the connection between the browser and the server of a web application can capture clear-text passwords and cookies (with “tokens”) if the communication is not secured (HTTP and not HTTPS). This issue is out of the scope of this blog and is included in this list of attack vectors on browsers for the sake of completeness.

Sample Open source framework: **Evilginx 2** (GitHub [here](https://github.com/kgretzky/evilginx2), Blog by Kuba [Gretzky](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/) [here](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/))  
Sample exploiter: [**Kimsuky**](https://attack.mitre.org/groups/G0094) ([MITRE G0094](https://attack.mitre.org/groups/G0094/)) (using a modified version of PHProxy)

### Detailed Mitigation Considerations

OK, it’s time to consider the mitigations for the attacks identified above. All mitigations will rely on kernel mode driver callbacks. In the following discussion, we shall refer to the Chrome browser (chrome.exe), but the same logic applies to other Chromium-based browsers (e.g., msedge.exe).

**A) Protecting sensitive browser files**

Rule:**Block unauthorized processes from accessing sensitive browser files**.

A) _Q: What should be protected?_

Consider “Login Data,” which holds encrypted passwords. It is usually found in the folders:  
C:\Users\<Windows user>\AppData\Local\Google\Chrome\User Data\<Default | Gmail user>  
(where Gmail user is a profile name, not the actual Gmail user name).

However, Chromium started (a short while ago) to create a snapshot of the files in this folder whenever a major upgrade is performed. Therefore, it will also be found in folders such as  
\SnapShots\91.0.4472.164\<Default | Gmail user> located in the original “User Data” folder.

So, a good definition of the “Login Data” files that should be protected is:

“?:\Users\\*\AppData\Local\Google\Chrome\User Data\\*\Login Data”

_Q: Which operations should be protected?___

– Direct READ access (e.g., copy operation)

– File or path rename operation (which might take the file out of the scope defined above)

– Zipping or archiving by any standard program (for example, tar.exe should not be authorized to access this file)

**B) Protecting browser’s VM**

Rule:**Block unauthorized processes from accessing browser’s memory**.

_Q: Wh_ _at_ _is the browser process that we are going to protect (and trust)?__  
_  
Clearly, the Chrome process to be protected (and trusted, e.g.: to access “Login Data”) will be a binary that is signed by Google. Obviously, we do not want to apply our protection to everything signed by Google, as it might create many false positive cases, so we should also verify it is actually the Chrome application.

Intuitively, we might rely on the binary name being chrome.exe or, more strictly, on the full path name “%SYSTEMDRIVE%:\Program Files\Google\Chrome\Application\chrome.exe.” This would be a mistake because a standard attacker can run Chrome from a different folder and under a different name. Try the following cmd.exe batch with a parameter [%1] that defines your attack folder (while Chrome is not already active):

_Code Snippet #1: Running Chrome from an unprotected folder and with a different name_

`  
cd %1  
xcopy /S "c:\Program Files\Google\Chrome" *  
cd Application  
ren chrome.exe newChrome.exe  
newChrome.exe  
`

You will see that a fully functional browser is running, where the binary file name of all the browser’s processes is newChrome.exe.

The solution is to look for a property of the binary file that is included in the signature. A good candidate here is the OriginalFileName property, which is chrome.exe.

So, the processes we want to protect (and trust) are:

**processes signed by Google****with OriginalFileName = “chrome.exe”**

Note that if the attacker modifies OriginalFileName to be newChrome.exe, the binary is no longer signed. Therefore, we will not trust it (e.g., it will not be allowed to access login data or other critical files and will not be a fully functional browser).

_Q: How to block access of unauthorized processes to the browser’s memory?__  
_  
– Remove from OpenProcess the **PROCESS_VM_READ** access right (if it is requested)  
– Prevent unauthorized processes from creating a browser process  
– Prevent all potential ways of dumping the memory of the browser process

_Explanation:_ This means that binaries signed by a trusted vendor (e.g., Microsoft) that can perform a memory dump should not be authorized to OpenProcess (**PROCESS_VM_READ**) the browser. Examples: rundll32, Taskmgr.exe. Might need to examine all LOLbins.

**C) Prevent usage of “dangerous” command line arguments**

Rule: **Block unauthorized processes from creating a browser with “dangerous” command line arguments**

This might seem redundant because in the previous section, we listed the requirement to “prevent unauthorized processes from creating a browser process” but note that “unauthorized processes” may be different in these two cases. For example, we may allow cmd.exe to create a new instance of the browser, but not with the “dangerous” command line arguments.

In fact, the default here should be **not to authorize** any process to create a browser with the “dangerous” command line arguments, and to let the user authorize specific processes (applications) to a minimized set of endpoints.

**“- -remote-debugging-port”**

As discussed above, creating a browser with this command line argument allows another process to control the operation of the browser via a TCP connection over the specified port. This control includes options to retrieve sensitive data, including all the cookies.

This option is part of Chromium’s DevTools and is usually used for testing web applications. An example of an open-source application using this feature is “ChromeDriver” by Chromium.org. This application is defined [here](https://chromedriver.chromium.org/) as a “tool for automated testing of web apps across many browsers.” The usage of such an application should be allowed specifically by the user.

If the use of this option is widespread (many endpoints) and continuous, it might be a good idea to implement the following protection scheme (using an NDIS kernel driver):

– Track **all** browser debugging ports that are currently open.  
– Allow only specific applications (e.g.: ChromeDriver.exe) to connect to these ports.

**“- -remote-debugging-pipe”**

This option is not currently active (as far as I know), but it might be a good idea to be prepared and treat it in the same way “- -remote-debugging-port” is treated.

**short format = verbose format**

Apparently, in Chrome, short-formatted command line arguments have the same text as the verbose version.

“-remote-debugging-port” has the same effect as “- -remote-debugging-port.”  
Make sure the rule[s] you define cover both versions.

**“- -headless”**

This command line argument is commonly used together with “–remote-debugging-port.” One legitimate use of this mode of working (browser has no user interface) is to perform “web scraping” (web crawlers). I do not know how common this command line argument is in legitimate use, but I do know that malwares use it to achieve “legitimate” communications to their control. So, it might be a good idea to make a separate rule to prohibit usage of this command line argument. If it appears without “–remote-debugging-port” it should be blocked. As usual, the user may authorize specific applications.

**D) Prevent code injection into the browser process**

This is a very complex protection task, and “holes” in the protection I propose here will probably be discovered (I’ll be grateful if you let me know!), but I shall not cowardly (😃) avoid my duty to protect (and help others protect).

Rule: **For unauthorized processes OpenProcess-ing a browser process, remove all “dangerous” access rights**

“Dangerous” access rights allow code injection. My list of dangerous access rights includes:  
**PROCESS_CREATE_THREAD****  
****PROCESS_DUP_HANDLE****  
****PROCESS_SUSPEND_RESUME****  
****PROCESS_VM_OPERATION****  
****PROCESS_VM_READ****  
****PROCESS_VM_WRITE****  
****ACCESS_SYSTEM_SECURITY****  
****WRITE_DAC****  
****WRITE_OWNER****  
**  
Rule: **For unauthorized processes OpenThread-ing a browser process’ thread, remove all “dangerous” access rights**

“Dangerous” access rights allow code injection. My list of dangerous access rights includes:  
**THREAD_IMPERSONATE****  
****THREAD_SET_CONTEXT****  
****THREAD_SET_INFORMATION****  
****THREAD_SET_LIMITED_INFORMATION****  
****THREAD_SET_THREAD_TOKEN****  
****THREAD_SUSPEND_RESUME****  
****ACCESS_SYSTEM_SECURITY****  
****WRITE_DAC****  
****WRITE_OWNER****  
****  
** The list of authorized processes should be very short, but must include the parent of the browser process.

Rule: **Prevent browser process from loading unsigned (untrusted) DLL**

DLL injection, DLL hijacking, DLL side-loading and Windows hooks are all techniques that can be used to inject a malicious DLL into a process.

Since Chrome.exe can be activated from an unsafe location (as shown above), a standard program can modify any of the DLLs in the current version folder  
(e.g.: “C:\Program Files\Google\Chrome\Application\97.0.4692.71\chrome_elf.dll”)  
and it will be successfully loaded into the valid browser process.

This rule will block such an attack as well as any other malicious DLL loading (provided, of course, the attacker cannot create a version of a loaded DLL that is signed by an authorized vendor).

**E) Keylogging protection**  
Keylogging is a broad general issue that is not specific to browsers, and there are various commercial anti-keylogging products available.

In my next blog post, I will describe a standard (non-elevated) user-mode keylogging technique and suggest a method to detect if such a keylogging attack is active. Additionally, I will show a method to obstruct this attack during the keying-in of sensitive fields (e.g., password) in the browser.

It is interesting to note that this attack was seen for the first time in the wild (as far as I know) when used recently by the North Korea-based cyberespionage group [**Kimsuky**](https://attack.mitre.org/groups/G0094) ([MITRE G0094](https://attack.mitre.org/groups/G0094/)).

### Mitigations Summary

  * Deny any access of unauthorized processes to sensitive files  
(CreateFile, MoveFile)
  * Deny any access of unauthorized processes to browser’s VM  
(OpenProcess, OpenThread)
  * Prevent unauthorized processes from creating the browser  
(CreateProcess)
  * Block suspicious command line options when browser is created  
(CreateProcess-command line)
  * Prevent browser process from loading unsigned (untrusted) DLL  
(LoadLibrary)

### Mitigation Demos

The following demos show how some of the mitigations discussed above operate in the CyberArk Endpoint Privilege Manager.

All of the videos work according to the following general plan:

  * Turn relevant Endpoint Privilege Manager protection policy OFF
  * Successfully execute attack[s]
  * Roll back the results of the attack
  * Turn the relevant Endpoint Privilege Manager protection policy ON
  * Repeat the same attacks and observe that they are blocked
  * Show blocking events recorded in the Endpoint Privilege Manager server

### Demo#1 – Protecting sensitive files

![](https://fast.wistia.com/embed/medias/ktsxf3dkzx/swatch)

### Demo#2 – Protecting browser memory

![](https://fast.wistia.com/embed/medias/20o5et6e0z/swatch)

![](https://fast.wistia.com/embed/medias/cwmj5ncw8m/swatch)

![](https://fast.wistia.com/embed/medias/0nr9mss41p/swatch)

### Demo#3 – Asking nicely

![](https://fast.wistia.com/embed/medias/cdx6i19opq/swatch)

### Demo#4 – Code Injection

![](https://fast.wistia.com/embed/medias/7soisl8bs2/swatch)

### Summary

If the proposed protection plan is implemented fully and accurately (mainly in the identification and protection of trusted/authorized processes), I believe that it may:

  * Block the vast majority of current credential stealers’ attacks on protected browsers.
  * Make it very difficult for a standard user-mode process to steal credentials from protected browsers.
  * Make it difficult for elevated user-mode processes to steal credentials from protected browsers (by forcing them to make “noisy,” illegitimate actions that will probably be detected/blocked by other security mechanisms).
  * Provide a wide range of protection against other types of attacks on web applications (e.g., by preventing browser hooking, [which] is the hallmark feature of most financial malware).

It will **not** :

  * Protect against kernel-mode (rootkit)

Let us make the attackers sweat.

GO BLUE!

_Author note: Thank you to Anatoly Kardash a Senior Director on CyberArk’s R &D team for his support on this research._

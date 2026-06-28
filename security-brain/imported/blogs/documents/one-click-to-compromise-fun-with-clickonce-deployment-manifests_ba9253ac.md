---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-30_one-click-to-compromise-fun-with-clickonce-deployment-manifests.md
original_filename: 2020-07-30_one-click-to-compromise-fun-with-clickonce-deployment-manifests.md
title: One Click to Compromise -- Fun With ClickOnce Deployment Manifests
category: documents
detected_topics:
- cloud-security
- sso
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: ba9253ac5769f13bd7cc9d81d5f7dc5c858ef6b66a80d9751cab5228bafb1a16
text_sha256: 6e31cdba6ffe68150d8f064fa973f321a2faa2953e55ae1b981147bc0e7ccb2f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# One Click to Compromise -- Fun With ClickOnce Deployment Manifests

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-30_one-click-to-compromise-fun-with-clickonce-deployment-manifests.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `ba9253ac5769f13bd7cc9d81d5f7dc5c858ef6b66a80d9751cab5228bafb1a16`
- Text SHA256: `6e31cdba6ffe68150d8f064fa973f321a2faa2953e55ae1b981147bc0e7ccb2f`


## Content

---
title: "One Click to Compromise -- Fun With ClickOnce Deployment Manifests"
url: "http://blog.redxorblue.com/2020/07/one-click-to-compromise-fun-with.html"
final_url: "https://blog.redxorblue.com/2020/07/one-click-to-compromise-fun-with.html"
authors: ["Dave Cossa (@G0ldenGunSec)"]
programs: ["Microsoft"]
bugs: ["NTLMv2 hash disclosure", "One-click execution of arbitrary .Net assemblies", "Windows"]
publication_date: "2020-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4370
---

###  One Click to Compromise -- Fun With ClickOnce Deployment Manifests 

\-  [ July 30, 2020  ](https://blog.redxorblue.com/2020/07/one-click-to-compromise-fun-with.html "permanent link")

**Note:**

I submitted a report to MSRC regarding the hash-disclosure vulnerability associated with ClickOnce deployment manifests. After review I got a response back earlier in July where it was noted that the vulnerability did not meet the bar for immediate servicing and was given the green light to disclose.

**  
**

**Edit 9/22:**

MS has remediated the NTLM-disclosure part of this issue as of KB4576630 <https://support.microsoft.com/en-us/help/4576630/kb4576630> However, this method will still work as a delivery mechanism for stage-0 payloads.

**TL;DR**

ClickOnce Deployment Manifests are a relatively unknown way to both get an initial payload into an environment as well as remotely retrieve NTLM challenge-response hashes over HTTP. Hash retrieval occurs on initial file open (before any warnings pop) meaning that even if the user opts to close out on the warning, we still have a hash we can attempt to crack. 

IE also has some interesting interactions with these files and will automatically execute a manifest upon browsing to it – even on an internet-zoned site. This means that on a hyperlink click we’ll be getting an NTLMv2 remotely over HTTP at a minimum (if the remote user is configured with IE as their default browser) and can get a shell with one more click. This also gives us several different options for execution, as the deployment manifest can be sent directly as an attachment, embedded into an HTML and hosted, or hosted on a webserver and linked directly to via hyperlink. For the POC|GTFO crowd, here’s demos of two different methods that could be used:

**Run via IE + hyperlink click:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvBlEkGtO4XgXlKO41FNvBd3ZyIP2o3l9eSir8fq_e5h_YdA2fMx4-AC7e6lKkqbDlLmTb71ro9CPS0FtZPrxr-shtiKtd7xNN146klFBWY_tOP0BrhGn2evpQF1d99vYq48KAkG4FUFA/w976-h549/testManifestIE.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvBlEkGtO4XgXlKO41FNvBd3ZyIP2o3l9eSir8fq_e5h_YdA2fMx4-AC7e6lKkqbDlLmTb71ro9CPS0FtZPrxr-shtiKtd7xNN146klFBWY_tOP0BrhGn2evpQF1d99vYq48KAkG4FUFA/s800/testManifestIE.gif)

**  
**

**Run via web delivery:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLn8IE3GXz1x1bjBNvQJ_CtWTxgm3Eg2Zr0R3BcYYsjYiXAyCXCka5ahVYKHUv69eSncY5GMolHha1RgPfABeWuhQqDrXsTGMZAiLQ5dgn0mDxzbqsxfeuLYGSPT3NjtXZiH5bRfkADYY/w781-h439/testManifest.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLn8IE3GXz1x1bjBNvQJ_CtWTxgm3Eg2Zr0R3BcYYsjYiXAyCXCka5ahVYKHUv69eSncY5GMolHha1RgPfABeWuhQqDrXsTGMZAiLQ5dgn0mDxzbqsxfeuLYGSPT3NjtXZiH5bRfkADYY/s800/testManifest.gif)

**Background and ClickOnce Execution Process**

A few months ago I was on an assessment for a client that had done a pretty solid job of locking down the ‘standard’ types of payloads we would use to try and get an initial foothold in their environment (HTA’s, all types of WScript payloads, macros / DDE, etc.). In my efforts to find payloads that would get us execution on their systems, I happened to stumble across the “.application” file extension, which after a quick google search got me to a Microsoft article on deploying applications to systems over a corporate network with ClickOnce Deployment Manifests. This seemed like an interesting lead, so I spent a bit of time digging into them further, and ended up finding quite a bit more good info about them.

ClickOnce was designed to be used as a deployment technology in enterprise environments and allows for the creation of self-updating C# or C++ applications that can be installed and ran with minimal user interaction (<https://docs.microsoft.com/en-us/visualstudio/deployment/clickonce-security-and-deployment?view=vs-2019>). The deployment process consists of several steps and various manifest files, which are really just XML's. First, a deployment manifest (.application) file is somehow executed by the end-user (file click, browse via IE, etc.). Upon this first open of the deployment manifest, Windows loads the ClickOnce runtime (dfsvc.exe), which parses this initial file and handles all additional calls out to grab other required files. Applications spawned via ClickOnce deployment are children of the ClickOnce process: 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsSyPvDKQL9AfQVMxeSAREvusr_inV25VN6M6aX_SA_hrhL0ZQ-46iJ7xzDu7uBocyYdu4X4BS5U2SKU7XAlxFbW89gSWaXFV3UoploHksRsxxrfrQq2eDp6wVZy0G_igR0HYFI7TnvQM/d/19.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsSyPvDKQL9AfQVMxeSAREvusr_inV25VN6M6aX_SA_hrhL0ZQ-46iJ7xzDu7uBocyYdu4X4BS5U2SKU7XAlxFbW89gSWaXFV3UoploHksRsxxrfrQq2eDp6wVZy0G_igR0HYFI7TnvQM/s728/19.png)

The first file dfsvc pulls in is the remotely hosted version of the same deployment manifest that it is currently parsing, which is done in order to determine if updates to the deployment have occurred and need to be processed. The version numbers are compared, and if the most current version is not installed, dfsvc will use the relative pathname of the application manifest (relative to the included path to the deployment manifest) to next request this second manifest file:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5idGzs5gzJL8JYbMfRLoTng4V5GyGQTNsRAONuF3tBkauEu4yfeg5U_gAYsX7Sy4Wcwf0EWWGV4wIEKS39g1jPcNa6uZhkWpoTgi0O3S05UM9AKys6n7WIw1Df1rWwbVSkzHl668gbDo/d/24.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5idGzs5gzJL8JYbMfRLoTng4V5GyGQTNsRAONuF3tBkauEu4yfeg5U_gAYsX7Sy4Wcwf0EWWGV4wIEKS39g1jPcNa6uZhkWpoTgi0O3S05UM9AKys6n7WIw1Df1rWwbVSkzHl668gbDo/s862/24.png)  

This second file (application manifest / .manifest) is then parsed by the runtime. It contains more configuration options than the initial manifest, as well as relative paths to the files that need to be deployed to the remote system. The entire deployment process took me a bit of time to get my head around, but it can be summed up with the following example:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd1hC8biHMgEKqkF9UQdBGivf1nGfaf0kiXE0ly6bccwDuiwhgDEipGYwCIk1QZ2ediWZ7TaJeSslK8x5gM-Olw89w1FGeQnIbLB3a16eURbcgy91kdytrYjFFxQus0OWICtqHW7yxyis/d/25.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd1hC8biHMgEKqkF9UQdBGivf1nGfaf0kiXE0ly6bccwDuiwhgDEipGYwCIk1QZ2ediWZ7TaJeSslK8x5gM-Olw89w1FGeQnIbLB3a16eURbcgy91kdytrYjFFxQus0OWICtqHW7yxyis/s556/25.png)

1. Initial call to the server to grab the deployment manifest, this is what kicks off the ClickOnce runtime on the remote system

2. The now-running ClickOnce runtime connects back to our system, requesting a server-side copy of the deployment manifest its currently running to check for version updates. It determines that although there are no deltas, there is no local installation of this manifest on the remote host, so it proceeds to request the application manifest.

3. The runtime next requests the application manifest, which contains paths to the files to be installed on the remote system.

4. In our simple example, the only file in our deployment is a shellcode injector, which is requested by the remote system, downloaded, and ran, prompting the user if they want to execute or not.

**Testing and Use Cases**

After getting a better idea of the above process, I set about creating a super simple deployment manifest to test the functionality out; using the guide here was quite helpful: <https://docs.microsoft.com/en-us/visualstudio/deployment/walkthrough-manually-deploying-a-clickonce-application?view=vs-2019>. I uploaded the generated files to an Apache server on an AWS box, and found that I was successfully able to execute the .Net assembly I had included in the project after clicking through a security warning. Having success here, my next thought immediately went to authentication – since we’re forcing a remote system to connect to a server of our choosing, I was curious if it would actually go through and complete an NTLM authentication. I quickly fired up Responder on the remote system, attempted to re-download the manifest, and saw the following immediately upon opening the file, even before accepting the execution warning: 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4c3mfT4nzGBhiYxKjgObjJddeS-aYFLQrw-Zar-dnbbQoh6TNxWmrNoFJ5g-7VlOBemsrXCU2W_nHhLuRUjirEzM8svgAyCUu8cW5u-CKkIf9CYJ3BOiSGJq39d5GZaN02dCBgqs2D4g/d/20.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4c3mfT4nzGBhiYxKjgObjJddeS-aYFLQrw-Zar-dnbbQoh6TNxWmrNoFJ5g-7VlOBemsrXCU2W_nHhLuRUjirEzM8svgAyCUu8cW5u-CKkIf9CYJ3BOiSGJq39d5GZaN02dCBgqs2D4g/s505/20.png)

At this point I was most definitely interested and started doing a bit more research to see if anyone had done anything from a payload perspective with these before. I found a page on LOLBAS which referenced a talk that @SubTee gave that had a slide on them from back in 2015, but outside of that there really wasn’t much (<https://lolbas-project.github.io/lolbas/Binaries/Dfsvc/>). However, I’m still always amazed at how bad I am at googling things, so if there is more info out there on this type of payload, my bad.

Edit: yep, I'm still bad at googling stuff. [@0xF4B0](https://twitter.com/0xF4B0) gave a talk on ClickOnce last year at BlackHat, his talk + whitepaper cover some different use-cases and setup methods for deployment manifests. I would highly recommend giving it a read: <https://www.blackhat.com/us-19/briefings/schedule/index.html#clickonce-and-youre-in---when-appref-ms-abuse-is-operating-as-intended-15375>

To ensure this wasn’t just something tied to the systems I was testing with being on the same local network, I next created a new manifest that pointed to an externally-facing IP, and re-sent the application manifest file to myself across two different email providers. Upon receiving the attachment and opening I was greeted with a very standard ‘open-save-cancel’ dialog box, and upon clicking it I once again immediately got an NTLMv2 challenge-response hash back on my remote system.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmTYeWtScSfaawE3Fbbu2mfYra2rpeu0RRCcqLPtuRffdm443kGRCgK_yB-nBjo6elVh_y1Cv776sQJw4dtyYiwM-FJA-fF5vQLVPS99Phl7v2k4EEdUu_PcZ9CE2JJGY1Zbnl3tIdTMY/d/16.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmTYeWtScSfaawE3Fbbu2mfYra2rpeu0RRCcqLPtuRffdm443kGRCgK_yB-nBjo6elVh_y1Cv776sQJw4dtyYiwM-FJA-fF5vQLVPS99Phl7v2k4EEdUu_PcZ9CE2JJGY1Zbnl3tIdTMY/s960/16.png)

If I wanted to continue past just getting a hash here, in order to get to the point I would actually be able to execute code on the remote system, one additional warning message must be clicked through as well:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0ZjlSCZrz7CmIOw_nVGS6lWSUX6SkRgXMNRFRhs0nlcYB4_aZPWpZUtZ5_G76QODFacvw5fd9-K4X2IbVKVuWXWQvOOBhkBfwq6PQoY8WPoM1WAb-7MWeEisKYh1WVy1_XFDIJgil0b8/d/10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0ZjlSCZrz7CmIOw_nVGS6lWSUX6SkRgXMNRFRhs0nlcYB4_aZPWpZUtZ5_G76QODFacvw5fd9-K4X2IbVKVuWXWQvOOBhkBfwq6PQoY8WPoM1WAb-7MWeEisKYh1WVy1_XFDIJgil0b8/s590/10.png)

Note: having a valid code signing cert makes this error look less scary 

When the assembly is ran, it is downloaded to disk (located in the \Users\\*user*\AppData\Local\ Apps\2.0\\*randomChars* folder). For that reason I would recommend keeping your stage-0 pretty small & keeping shellcode or anything risky in additional files downloaded as a part of your manifest that are referenced from your assembly, no differently than keeping any other initial payload sent via macro / attachment / web delivery compact. I would probably also migrate off any processes ran out of here immediately and then remove the folder structure unless you want to use it in the future as a persistence mechanism. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTtf0eqNCa_Ez1fazCXiXYmsu4943HNhpAP375pETbQiuK3VB8YOESqEb2whkt_LdPYffgCAFlZu-XUm1kL2cMgBovoGw1vRK2DZLArHCsVFXvpVXxUP47dWk5tzNED29I2xEInvLexB4/d/11.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTtf0eqNCa_Ez1fazCXiXYmsu4943HNhpAP375pETbQiuK3VB8YOESqEb2whkt_LdPYffgCAFlZu-XUm1kL2cMgBovoGw1vRK2DZLArHCsVFXvpVXxUP47dWk5tzNED29I2xEInvLexB4/s461/11.png)

While it’s great and all that we can execute basically any .net code we want this way, what I found most interesting about this filetype was the ‘no warning’ remote hash disclosure over HTTP. This grants us the ability to still get ‘some’ value out of a click, even if actual execution fails or is cancelled by the user. However, there really wasn’t a great solution that I was able to find that handled both delivery of multiple files, as well as collection of hashes. 

After a weekend of messing around with a variety of types of webservers and the impacket libraries, I finally settled on modifying some of the functionality that already existed within the Responder project (<https://github.com/lgandx/responder>) to allow for both hash retrieval and file delivery. I’ve got more details on these changes down in the ‘Building ClickOnce Deployment Manifests’ section below, but really what I put together was really intended only as a PoC and not something that I recommend copying without some pretty substantial improvements. 

With this setup in place, I tossed the initial application manifest payload (.application) into an html, which my hybrid Responder / web server hosted as well. Testing this whole execution chain yielded the following from a server-side perspective:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKNoGFaVyOYUuFM_dGV2Aebr1rU2SXrq1MZPBVI6-If9qtuW8z8kSGWEU1keM4MTzkBHL9r2pncuc1VR7S67si-mw21io8vuSt2Uthr6aQ9R8XVkeG8K0d9wgkqhx0bQsnADvcBWSMJyg/d/21.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKNoGFaVyOYUuFM_dGV2Aebr1rU2SXrq1MZPBVI6-If9qtuW8z8kSGWEU1keM4MTzkBHL9r2pncuc1VR7S67si-mw21io8vuSt2Uthr6aQ9R8XVkeG8K0d9wgkqhx0bQsnADvcBWSMJyg/s736/21.png)

Up until this point I had been testing my payloads almost exclusively by tossing a deployment manifest onto the desktop of one of my VM’s and then double-clicking it for the initial execution vector. This worked well from a speed-of-testing perspective, but wasn’t a great representation of a ‘realistic’ attack vector (psshhh…). As I started working through various deployment methods I turned off my Responder server and was once again testing with a default Apache setup. During this time I found that if I navigated directly to my web-hosted deployment manifest using IE it would automatically execute, without even prompting me with an open/save dialog. This behavior was quite interesting, and after comparing some traffic captures in Wireshark I made some additional changes to my HTTP server that allowed for NTLM capture remotely over HTTP while also delivering a payload transparently, allowing us to get down to a true ‘One Click’ deployment:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPRR7hQLBVSKbnloitJVzjYtsAO2Ti_wrTimoKYf7bp8d02EtvOxsuUYqVBiNnK9_4DjFLKOob5snFcoRoqU9gVVWTlX7Mp_WspULyx2BPeyQboLu6TL-NKPA8YrtZgxlKkorybdLUxl4/d/26.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPRR7hQLBVSKbnloitJVzjYtsAO2Ti_wrTimoKYf7bp8d02EtvOxsuUYqVBiNnK9_4DjFLKOob5snFcoRoqU9gVVWTlX7Mp_WspULyx2BPeyQboLu6TL-NKPA8YrtZgxlKkorybdLUxl4/s1047/26.png)

As I kept digging into why the ClickOnce runtime was being automatically loaded by IE, I found that this was actually the expected / default behavior when opening manifest deployment files:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivif6BEXDYvczo0_U3GWmXnbrMGZTs_86_5x1HKJtGfY9UUbfAt5cFw-Jktkn69hgzAqiQiddebgQIsz7iT77kxmZf3qr8qGCS3PqCJLXlDxTkesiGYkApJz_F4Oo4e2HaFKV-PGwBOD8/d/27.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivif6BEXDYvczo0_U3GWmXnbrMGZTs_86_5x1HKJtGfY9UUbfAt5cFw-Jktkn69hgzAqiQiddebgQIsz7iT77kxmZf3qr8qGCS3PqCJLXlDxTkesiGYkApJz_F4Oo4e2HaFKV-PGwBOD8/s768/27.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Nzzkt7qMfWsBHVha8swd93WoofNAd4Dv6tFWJRdFBycXFZXr2QEDUFlgcWy6hSC_SSjX5e7HmCeUrhmKr3_rAOmeW-biMJahg-ArWplllLsO5dagoEOMm3vy5J5g6UeqMEWYRIiyLBA/d/28.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Nzzkt7qMfWsBHVha8swd93WoofNAd4Dv6tFWJRdFBycXFZXr2QEDUFlgcWy6hSC_SSjX5e7HmCeUrhmKr3_rAOmeW-biMJahg-ArWplllLsO5dagoEOMm3vy5J5g6UeqMEWYRIiyLBA/s753/28.png)

At this point I spent more time looking at some of the specific features of different configuration options within the manifests themselves, but from an actual delivery perspective there wasn’t really anything new beyond this. Below, I’ve included some of the other unique features of the manifests that have potential applications, as well as a step-by-step on creating deployment manifests if you’re interested in trying out:

  

**.Deploy Extension**

Some organizations may have perimeter controls in place blocking inbound downloads of .exe / .dll files from unstrusted sources. ClickOnce manifests give us a way to get around some of these by including the following option in the deployment options tab of the deployment manifest build process:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj91GmJGz9AtIfkdIDh3qUvp29L_GfN1Ol57LakePMSKg1iXdmZ-7I6S_NFnng-LDo4_h2SONiusEJOOgmKyYFFlPNghVkbGi2LIzUQaBYZgH4sId4hiZ4DlK0XhKlYuBnqotAWRkShhXI/d/34.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj91GmJGz9AtIfkdIDh3qUvp29L_GfN1Ol57LakePMSKg1iXdmZ-7I6S_NFnng-LDo4_h2SONiusEJOOgmKyYFFlPNghVkbGi2LIzUQaBYZgH4sId4hiZ4DlK0XhKlYuBnqotAWRkShhXI/s410/34.png)

With this option checked you would just need to toss on an extra ‘.deploy’ to the end of every file you’re deploying (ex. shellcodeInjector.exe.deploy). The ClickOnce runtime will download the .deploy files over the wire, and then strip off the extra extension on the remote system before saving and running.

**Usage as a Persistence Mechanism**

The last cool thing I found about manifests is their potential usage as a persistence mechanism. After initial install of a manifest, further runs of the already-installed manifest no longer prompt the user with a security warning, because no new files are downloaded if the ClickOnce runtime performs its version check and finds no updates on the server-side manifest. Paired with the previously noted Internet Explorer interactions, this can allow for a shell callback by simply running IE and pointing it to an externally hosted .application file:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSiSYpC6CLN6yqek9lf15bMyd2PMoxX3QaevztKrWUqnGX1Ijsp5hqa5_9m_U1aiVoJRTtkKFUD42DogzINNoNKojUPMj8meZEDy188xnQKKEIDwgX031G6NWUA4tqIfKdKcWXE-wBsXk/d/33.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSiSYpC6CLN6yqek9lf15bMyd2PMoxX3QaevztKrWUqnGX1Ijsp5hqa5_9m_U1aiVoJRTtkKFUD42DogzINNoNKojUPMj8meZEDy188xnQKKEIDwgX031G6NWUA4tqIfKdKcWXE-wBsXk/s393/33.png)

While at the end of the day there is still a .exe on disk that’s being called by this, and you could just as easily set up a persistence mechanism to call it directly, this was a bit interesting to me as it allows us to set up a mechanism that instead calls IE and gives the remotely hosted manifest as an arg.

**Building ClickOnce Deployment Manifests**

Requirements: Visual Studio (I’m using VS 2019 in this example)

Note: This walkthrough uses a tool installed with Visual Studio called MAGE, but everything covered here can also be done through Visual Studio directly as well.

Pre-step: In your project in Visual Studio, ensure you go into the 'Application' tab of the project properties, and under the "Manifest" drop-down, select "Create application without a manifest". If this is not selected you will not be able to deploy your application using ClickOnce and the below steps.

To start, open up the developer command prompt for VS 2019\. From here type in ‘mage’. This loads the Manifest Generation and Editing tool GUI (MAGE) 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYgE7oNxGt7qL81U8pErXc9OHeR55mw08U-fr9UOV25NJmAnwLScOTyEG0KJWqVHJswKel8pXlnnnC7ReTl-c8sQkMqYDyjBfsQSljlgtUEPMcUurkuBm9abTtp4N0JrHMRTARrYnPIMo/d/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYgE7oNxGt7qL81U8pErXc9OHeR55mw08U-fr9UOV25NJmAnwLScOTyEG0KJWqVHJswKel8pXlnnnC7ReTl-c8sQkMqYDyjBfsQSljlgtUEPMcUurkuBm9abTtp4N0JrHMRTARrYnPIMo/s910/1.png)

We’ll be working backwards here, first creating an application manifest (the second stage in the delivery chain) before creating our initial deployment manifest. To create this manifest, click the left-most button directly under the file menu. After creating the application manifest, begin to configure it by selecting the appropriate processor architecture for your assembly and giving your manifest a name + version.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihjjwyHUKLRRpcM3Uh3-Ga3ne7ecCQQqAAREcKT1RotSKde-ksPG05YiDdxdy_xnhhqYlLxxKWAvbXpIQXfHx_8LsuG8NgeIBlVAm1JkAKYqm3Ux849eBiCbH9DDwN-s_jz8nW5LWDsGM/d/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihjjwyHUKLRRpcM3Uh3-Ga3ne7ecCQQqAAREcKT1RotSKde-ksPG05YiDdxdy_xnhhqYlLxxKWAvbXpIQXfHx_8LsuG8NgeIBlVAm1JkAKYqm3Ux849eBiCbH9DDwN-s_jz8nW5LWDsGM/s838/2.png)

On the files menu on the left-hand side, select a folder containing an assembly that is to be configured as a ClickOnce application. This can be any type of assembly with a valid entry point, and can be a single file or multiple files of various types (ex. a .exe and a .txt file containing the shellcode to execute, etc.). This can allow you to do some pretty neat stuff, for example to evade detections I built a payload that had functions in different files and referenced base64-encoded shellcode I had stored as a string in a text document that was also downloaded by the manifest.

If you don’t have a specific folder set up for this deployment manifest yet, I would do so now in order to keep track of the variety of files you’ll be creating. I recommend creating a subfolder for your application manifest in this new folder, as when linking it to your deployment manifest, MAGE will always take the current folder the application manifest is in as a part of the file path (more on this later).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMph9L97GI-xE7j03PFq5Udi9ov6ykqUHTVMi6HRurZh-dt6bednxRhfPU0uqhI5g0d7LcrwDxPhxl7tDC1OYqgW1NwsPIOgJYX4BbV_AG5HASZUX0QR3A9bG-pSHqUSmY5qb3IKgaMNw/d/3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMph9L97GI-xE7j03PFq5Udi9ov6ykqUHTVMi6HRurZh-dt6bednxRhfPU0uqhI5g0d7LcrwDxPhxl7tDC1OYqgW1NwsPIOgJYX4BbV_AG5HASZUX0QR3A9bG-pSHqUSmY5qb3IKgaMNw/s837/3.png)

Everything else should be good to leave at default values. When done, save the application manifest. Either sign the code with a valid code signing cert or have MAGE create a key to sign it with

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMQ-NfaNaX1JmkNCBU5_8OMDPnYtChxLZjEdW4TBaldZ2-8_qH4zgL7jzJwn3mbo2Amjt6nyEJUx61T-cd3e4KMfP7KReNpAZ0gYC7oxf9pFlXFph2o_ZlGldHt6eaCImxo-Ywvcdmxmk/d/4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMQ-NfaNaX1JmkNCBU5_8OMDPnYtChxLZjEdW4TBaldZ2-8_qH4zgL7jzJwn3mbo2Amjt6nyEJUx61T-cd3e4KMfP7KReNpAZ0gYC7oxf9pFlXFph2o_ZlGldHt6eaCImxo-Ywvcdmxmk/s521/4.png)

Once the application manifest has been created and saved, move on to creating a deployment manifest by clicking the ‘Create a new deployment manifest’ button immediately next to the one that was clicked to create the application manifest. Configure this in the same manner, changing the name and processor architecture.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_kFeTpAH5PYVbzEdZqz0xuOSEk8CVlAzSuAuLOLzcxa9DaAe5cZjiMEbn1mObTFR-Jz_CvoyZGiDijC4V3JjYezQ1FPdLUuornlhQvPKOF-L0CA6DojQ601PXVat3uTlsA1qfccjpz0c/d/5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_kFeTpAH5PYVbzEdZqz0xuOSEk8CVlAzSuAuLOLzcxa9DaAe5cZjiMEbn1mObTFR-Jz_CvoyZGiDijC4V3JjYezQ1FPdLUuornlhQvPKOF-L0CA6DojQ601PXVat3uTlsA1qfccjpz0c/s839/5.png)

Set a publisher and product in the Description tab (these can be anything), and then in the Deployment Options tab select ‘online only’ for application type, and check the ‘include start location’ box, which allows you to enter the address you’ll be hosting your deployment manifest on:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAamgw5iQ7CIk8b1qxSW7wGGC80lxb020cJqnovZzjc6ACTE0ArtINls5gE4ukqrgvwWWKW0t3D_zPNhu6UsBLiSOmUPQRHpWLqe6lvaEa1rIRjF8L3YsMrABJkrdf7iB6e5O5tQqBvU8/d/7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAamgw5iQ7CIk8b1qxSW7wGGC80lxb020cJqnovZzjc6ACTE0ArtINls5gE4ukqrgvwWWKW0t3D_zPNhu6UsBLiSOmUPQRHpWLqe6lvaEa1rIRjF8L3YsMrABJkrdf7iB6e5O5tQqBvU8/s838/7.png)

Finally, in the ‘Application Reference’ tab, select the application manifest that you just created. This will link the application manifest to the deployment manifest. Remember that paths between the two files are relative, so if your application manifest is in a folder called “1.0.0.0” as in the example below, this folder hierarchy needs to be replicated (or simulated) server-side when deploying (see example below). When selecting the application manifest, MAGE will always include the name of the current folder it’s located in but will not take any portion of the path beyond that.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpkNQkpNykHIK4zsosMAnlZtUbV48c_gXzLt8uCol-U3TUrISDKi5PUrfm5hOdonzpNLrfpoR75-qUrifPv3p3QjBuyheu0q43NS8BZ1aviQucPvwgW-qz3DLGGRY6ZM5Ymn2aUD9QuKM/d/8.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpkNQkpNykHIK4zsosMAnlZtUbV48c_gXzLt8uCol-U3TUrISDKi5PUrfm5hOdonzpNLrfpoR75-qUrifPv3p3QjBuyheu0q43NS8BZ1aviQucPvwgW-qz3DLGGRY6ZM5Ymn2aUD9QuKM/s833/8.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNf8YCSjnZrv1cyf5rMm3z28UYRyR5bOnsyB4Qm-B68d2q31UPegOIPVynZQ1EG4YLkS2dOumaYUD8XT15N_BWDk9Uz2RGjMX2xH5zr2uhWdB-YOq2m2qsNaDgclvtNNAchGljcAaZS58/d/29.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNf8YCSjnZrv1cyf5rMm3z28UYRyR5bOnsyB4Qm-B68d2q31UPegOIPVynZQ1EG4YLkS2dOumaYUD8XT15N_BWDk9Uz2RGjMX2xH5zr2uhWdB-YOq2m2qsNaDgclvtNNAchGljcAaZS58/s518/29.png)

Once this is done, simply sign and save it– using your previously generated cert / valid code signing cert.

At this point, you should now have both a completed application manifest and deployment manifest. Upload them to the web / file server you indicated when building the deployment manifest, and you should be good to start delivering. 

On the webserver side of things, it really depends what your end goal is – hash interception, payload delivery, or both. If you’re looking to do both, I _really_ suggest doing something more scalable than what I threw together, but if you’re looking to test on your own network, here are roughly the changes I made to responder:

Most of the changes were made to the PacketSequence function in the HTTP.py library, and primarily consisted of adding some additional rules to return files based on name. Some of these (.application, .exe, optional .html) are done pre-NTLM auth, with the manifest being done after NTLM auth in order to allow us to grab the hash. And yep my search terms are hardcoded values and are really janky :) 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdoUsopee4YSfOdKL7qDrOjdS3U4XS_wjxIkBq4dbjRqkg-UcbUr8e6su1W9CV5tc4zqsMOU4yy658RnA0V_Pe7yvi4aQiKJRYLOdnKe_GLh4W_5GEkJqvVoEjolhn6z0Mdi3fwQ4nPZ4/d/31.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdoUsopee4YSfOdKL7qDrOjdS3U4XS_wjxIkBq4dbjRqkg-UcbUr8e6su1W9CV5tc4zqsMOU4yy658RnA0V_Pe7yvi4aQiKJRYLOdnKe_GLh4W_5GEkJqvVoEjolhn6z0Mdi3fwQ4nPZ4/s1028/31.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0KCbDd7LcYIhPU1sgcy3AgxsUVV2PDYjVetpWitotVwg72M2C8y9eF7W9bIizauV8gEEV8TZxWWTXAYzhkBZGixzXcNrU4-NT3s3YBtn8tbm3SFv-sme-qdTbDsXZNMcQEk4-EfjhYg/d/30.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0KCbDd7LcYIhPU1sgcy3AgxsUVV2PDYjVetpWitotVwg72M2C8y9eF7W9bIizauV8gEEV8TZxWWTXAYzhkBZGixzXcNrU4-NT3s3YBtn8tbm3SFv-sme-qdTbDsXZNMcQEk4-EfjhYg/s908/30.png)

On top of these changes, I modified the ServeExeFile and ServeHtmlFile classes in packets.py to remove unnecessary headers that broke things (X-CCC and X-CID) and changed the html mimetype to “application/x-ms-application”. Finally, I updated the conf file to include the following settings:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk2kzGIvYQzqkGiy88i1ksbgtcno2jMxPGJbFfYAQFfR4GCpDmojMcoLXrV6r03jyMviGY-wnMNt6if2IRFZnAl_AXR-5YvevxSIlBVHOdEnD_ib_kP3b5F3LsRacshj7we4p23G_kp0o/d/32.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk2kzGIvYQzqkGiy88i1ksbgtcno2jMxPGJbFfYAQFfR4GCpDmojMcoLXrV6r03jyMviGY-wnMNt6if2IRFZnAl_AXR-5YvevxSIlBVHOdEnD_ib_kP3b5F3LsRacshj7we4p23G_kp0o/s571/32.png)

Note that the .html serving thing is completely optional, this was just done so that I could host a web page that contained an embedded deployment manifest file in it.

**Random Other Stuff**

· There are some other options within the manifest that you can manually modify that can allow you to attempt to install / run as an admin. I tried messing around with these but all my attempts ended in execution failures. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhajj5kG4nUjN2uDxf2Wapna0-QBIyQHzwoxaNtCLjnZ_KG5ngufBn7_31b9qRXhchG4wlNHN7B96KEIl0vU_fqeivOLTHjkmPHxG0yL2D7CjYSfO2yX2tEbignc2yP1VEZs6IpcbGDT5o/d/35.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhajj5kG4nUjN2uDxf2Wapna0-QBIyQHzwoxaNtCLjnZ_KG5ngufBn7_31b9qRXhchG4wlNHN7B96KEIl0vU_fqeivOLTHjkmPHxG0yL2D7CjYSfO2yX2tEbignc2yP1VEZs6IpcbGDT5o/s674/35.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBiemMN8sg4XDrvKYgw6F-hp2c1uPWtBhj9E86Yjalls17ehtFhWwcPcQXFb-2nQXAbY_vhy5KvbfVL3qCO-NcOkFbX5afmlp8OLhmQB25fPLzWsFAugUsmrDDBEzVp8shu5GHgjvLazE/d/23.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBiemMN8sg4XDrvKYgw6F-hp2c1uPWtBhj9E86Yjalls17ehtFhWwcPcQXFb-2nQXAbY_vhy5KvbfVL3qCO-NcOkFbX5afmlp8OLhmQB25fPLzWsFAugUsmrDDBEzVp8shu5GHgjvLazE/s1087/23.png)

I’ve had varying degrees of luck sending the .application as a direct attachment. I’ve had pretty good luck getting it past corporate mail filters into inboxes, but the default O365 outlook filter appears to block it as untrusted, so YMMV.

· The documentation for these files is super disjointed and kind of all over the place. I’m pretty confident that this is only scratching the surface of what can be done through these files, but still figured it was decent enough to warrant a blog post. Hopefully it gives some inspiration to go find some additional functionality within this framework.

**Defenses:**

· Disallow .application and .deploy files at the perimeter

· AppLocker blocks ClickOnce assemblies in its default config as files are ran out of Appdata/Local, AWL can work as a solution.

· Disable the ClickOnce trust prompt via registry key as outlined here (change default behavior for the internet zone): <https://docs.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2019> Note, this only partially mitigates the risk – the ability to run the manifest is disabled, but hash retrieval is still possible:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGzdHS45eLJKnOEq5iQOvi6TRfEhzhCjPiNC29MAX3RZj0YbNnPVw5xpJ_Tz7CCSwoayrFJa0aWdzNaroFZSaaT-6pfolefGCXI2ae-HQ39yYxV_oOVn2HSfUkxzegZqXUlR4EIcBigZE/d/36.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGzdHS45eLJKnOEq5iQOvi6TRfEhzhCjPiNC29MAX3RZj0YbNnPVw5xpJ_Tz7CCSwoayrFJa0aWdzNaroFZSaaT-6pfolefGCXI2ae-HQ39yYxV_oOVn2HSfUkxzegZqXUlR4EIcBigZE/s1099/36.png)

  

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8176792450471116129?po=3857097445581235629&hl=en&saa=85391&origin=https://blog.redxorblue.com&skin=contempo)

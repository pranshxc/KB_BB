---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-23_shambles-the-next-generation-iot-reverse-engineering-tool-to-discover-0-day-vuln.md
original_filename: 2023-08-23_shambles-the-next-generation-iot-reverse-engineering-tool-to-discover-0-day-vuln.md
title: 'Shambles: The Next-Generation IoT Reverse Engineering Tool to Discover 0-Day
  Vulnerabilities'
category: documents
detected_topics:
- command-injection
- sso
- automation-abuse
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- sso
- automation-abuse
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: dae15d1f3e1b6e7603031de2f04605c79774646e74f4a377135ae040f4f102f9
text_sha256: ac1bef5c8c0b2bf7ce4b574b5692fd6323688ab34c5db8b6005df8fb680e057c
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Shambles: The Next-Generation IoT Reverse Engineering Tool to Discover 0-Day Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-23_shambles-the-next-generation-iot-reverse-engineering-tool-to-discover-0-day-vuln.md
- Source Type: markdown
- Detected Topics: command-injection, sso, automation-abuse, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `dae15d1f3e1b6e7603031de2f04605c79774646e74f4a377135ae040f4f102f9`
- Text SHA256: `ac1bef5c8c0b2bf7ce4b574b5692fd6323688ab34c5db8b6005df8fb680e057c`


## Content

---
title: "Shambles: The Next-Generation IoT Reverse Engineering Tool to Discover 0-Day Vulnerabilities"
url: "https://boschko.ca/shambles/"
final_url: "https://boschko.ca/shambles/"
authors: ["Olivier Laflamme (@olivier_boschko)"]
bugs: ["IoT", "Buffer Overflow", "Command injection", "Reverse engineering"]
publication_date: "2023-08-23"
added_date: "2023-08-25"
source: "pentester.land/writeups.json"
original_index: 838
---

[Reverse Engineering](/tag/reverse-engineering/)

# Shambles: The Next-Generation IoT Reverse Engineering Tool to Discover 0-Day Vulnerabilities

Simplifying the discovery of IoT/ICS 0-days. Revolutionizing embedded systems reverse engineering in a tool for everyone. 

  * [ ![Olivier Laflamme](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/size/w100/2021/09/119486535_632169284368147_173960549788702982_n-1.jpg) ](/author/olivier/)

#### [Olivier Laflamme](/author/olivier/)

23 Aug 2023 • 22 min read

Share

Reverse engineering has always held an aura of mystery making it an intimidating field to venture into. The act of uncovering hidden vulnerabilities in embedded systems, particularly 0-day vulnerabilities, is often regarded as a luxury and privileged pursuit. [Shambles](https://www.liansecurity.com/?ref=boschko.ca#/main/product/info?productId=2) aims to transform this experience by making embedded systems reverse engineering child's play.

Shambles aims to empower individuals to **quickly** and **easily** uncover vulnerabilities in IoT/ICS products. It streamlines and enhances the discovery and validation of 0-day vulnerabilities in embedded systems, eliminating the need for users to possess expert-level knowledge or extensive reverse engineering experience.

* * *

Fundamentally, Shambles stands as an advanced integrated toolkit used for dissecting the binary code of embedded systems. Thereby, Shambles is a comprehensive suite of in-house applications which provide functionalities, spanning from unpacking, decompiling, and disassembling to generating static pseudocode vulnerability, to a fully-fledged firmware emulation kernel, a debugger, and much more. All these diverse capabilities seamlessly converge within a unified tool. Consequently, the resultant culmination, Shambles, emerges as an all-encompassing and holistic solution for reversing and discovering vulnerabilities in embedded systems. 

* * *

For context, as of August 2023, I discovered `107` 0-day vulnerabilities in less than `200 hours` and wrote working RCE POCs for `49` of them. At the time of publishing this number will likely be in the hundreds. About `~30%` have been reported to vendors - so there's still plenty to find/report! These are vulnerabilities in IoT devices, mainly routers, cameras, and firewalls of big brands we all know and love. The majority of these flaws were Command Injections, BOF/DOS, and bypassing CVEs vendor patches; which are vulnerabilities Shambles excels at identifying 😊.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-146.png)

At the time of writing, the easiest way to get early access to Shambles is by joining our [Discord](https://discord.gg/wxJMRm8Hyg?ref=boschko.ca) ([https://discord.gg/wxJMRm8Hyg](https://discord.gg/wxJMRm8Hyg?ref=boschko.ca)) and reading the `**_faq-readme_**` section. To stay up to date with releases and developments follow [H4k](https://twitter.com/h4kb4n?ref=boschko.ca) and [Boschko](https://twitter.com/olivier_boschko?ref=boschko.ca) on Twitter. 

* * *

As a disclaimer, it's important to mention that I maintain an informal affiliation and relationship with Lian Security, the company behind Shambles. This connection can be best described as a healthy blend of friendship and business partnership. Our mutual goal is to pave the way for a future where Shambles becomes accessible to a broader audience. We strive to redefine the landscape of reverse engineering by concentrating on simplifying the process of discovering vulnerabilities.

I hold a deep passion for the success of Shambles. My sincere hope is that the IoT/RE community recognizes its value, embraces its potential, and utilizes it to discover and responsibly disclose zero-day vulnerabilities, thus contributing to making the internet safer. Observing Shambles flourish within this community would bring immense gratification. I wholeheartedly believe that Shambles possesses enormous potential to empower both new and experienced researchers and enthusiasts, enabling them to delve into the domain of embedded systems, bolster online security, and create a positive impact on the cybersecurity landscape.

* * *

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-21.png)

Let's talk about the company behind Shambles. It has been developed by a skilled team of 12 engineers at [Lian Security](https://liansecurity.com/?ref=boschko.ca#/main/home) for well over two years now. They're responsible for software such as [SHAMBLES](https://liansecurity.com/?ref=boschko.ca#/main/product/info?productId=2), [INCINERATOR](https://liansecurity.com/?ref=boschko.ca#/main/product/info?productId=1), and [FLEGIAS](https://liansecurity.com/?ref=boschko.ca#/main/product/info?productId=4) covering everything from software to hardware, basic operations and maintenance, product UI design, and so on.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-14.png)

Kindly note, and be mindful that that Lian Security is a [company based in China](https://www.beianx.cn/info/452506275655749?ref=boschko.ca), along with everything that entails. The people behind their products are talented security professionals just like the rest of us. Most of them have worked at F100 and extremely respected information security and research companies. I personally believe it would be a shame to deprive ourselves of their talent, research, hard work, and dedication to a framework based off of regional biases. 

The team plans to make public, and open source some seriously fantastic research. Such as [Implementation of obfuscation detection by Text Classification](https://www.liansecurity.com/?ref=boschko.ca#/main/news/FzJZjIkBUQjGUXE2xvvb/detail), and [NAND memory dump analysis](https://www.liansecurity.com/?ref=boschko.ca#/main/news/GTL0j4kBUQjGUXE26fsx/detail). 

* * *

Let's get started! I'll be showcasing most of the features that Shambles has to offer and how I personally use them to uncover vulnerabilities in a sequential fashion. There are a lot of features that I won't be delving into. However, if you want to see more Lian Security has a really great blog on how to [reproduce CVE-2019-10999 in Shambles](https://liansecurity.com/?ref=boschko.ca#/main/news/YZUl6YMBu1ziL48C64o3/detail). 

Shambles is available on `Windows`, `MacOS`, and `Linux` systems and supports the following firmware architectures `MIPS/ARM/PPC/RISC-V` with plans to integrate `intel x86` in future releases. There are ways for large organizations to obtain Shambles on-premise, and Lain Security is also exploring the possibility, and is open to the idea of selling bulk API calls to companies and vendors 😊. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/3ko49u--1-.jpg)

Under the hood, the reverse-engineering core of Shambles is the [Reactor](https://www.liansecurity.com/?ref=boschko.ca#/main/feature/reverse/engine) engine which is used to decompile the instruction sets of `MIPS/ARM/PPC/RISC-V` processors and `Android` APKs. `Electron` is used for the frontend, `Java` is used for the kernel portion, and `GO` is used for the backend and API server. 

There are two ways to get Firmware analyzed. The first is through the Shambles desktop interface and the second is via their [cloud web-based portal](https://shambles.cloud/?ref=boschko.ca#/login). The latter allows you to upload the firmware and have it statically analyzed through the portal below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-23.png)

Personally, I upload the majority of my firmware through this cloud portal. Once the firmware is uploaded, and analyzed you'll obtain general information and the sum of static analysis findings. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-80.png)

Before we go any further you might be seeing the number of potential vulnerabilities observed and be like

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-122.png)

To be honest so did I at first. After using Shambles you'll come to realize that its fidelity is **extremely** high. Most of these BOFs have to be chained with other primitives and oftentimes you won't have control over the registers. Nevertheless, don't dismiss the number presented by the analysis it's genuinely quite accurate and precise. The thing to remember is that the primary difference between Shambles and tools like IDA PRO, for example, lies in its efficiency in vulnerability excavation and reducing unnecessary manual review. 

Another feature I quickly want to shine some light on is the cloud report generator. I think having the ability to download such a report provides great value to vendors. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/resized.png)

The report gives you a good overview of binaries that might need some cleaning up and refactoring. It also includes any known CVEs the binaries you're using may have. Overall, not a bad thing to have and be aware of if you're a vendor.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/imgonline-com-ua-twotoone-up14Yy46qmdyI46o.jpg)

I find myself mainly using the desktop client on Windows. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-44.png)

Once this firmware is uploaded through the cloud app it can be retrieved in the desktop application `Browser All` view as seen below. It goes without saying that you only have visibility to the firmware your `userID` uploads. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-25.png)

In the future, for an added layer of security, Lian Security will implement a two-way certificate validation feature for public cloud users. This will ensure that the files uploaded and generated by the users can only be accessed by the users themselves, and they can use their own certificates to encrypt their account directories. Even though their current implementation is quite safe.

In the desktop application, `Clone to Local` does exactly what you think it does. Once a firmware is cloned it can be opened with Shambles. Here is the second place where you can upload firmware to get analyzed which gets uploaded to Shambles Cloud, and unpacked, analyzed, fuzzed, etc. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-27.png)

Once the firmware has been cloned locally, double-click it in the `Local Firmware List` to obtain the view below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-1.png)

There is a lot of information in the `Firmware Info` tab. We won't go into every single feature but the `File Password` feature I think it's nice. Shambles identifies instances of hard-coded credentials in the application firmware. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-77.png)

You do have the ability to crack these passwords using Shambles Cloud, but you might be better off doing this locally. Lastly, `Key Information` is always interesting. Private keys and certificates could give you further insight into whatever you're reversing. And if you have the physical machine open up some MITM avenues. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-81.png)

On the right-hand side, you'll have the following `Vulnerability` and `Virtual Machine` tabs.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image.png)

These are the suspected vulnerabilities that were picked up by analysis.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-127.png)

High, Medium, and Low are simply statically derived metrics based off of some fidelity metrics. I personally find most of my command injections in the `Low Vulnerability` section. This is something I've showcased in the past and you often see me look into this section during my [live streams](https://www.twitch.tv/olivier_boschko?ref=boschko.ca), so don't disregard low and medium severity. It's not an impact qualifier. 

Expanding any of these high, medium, or low tabs will provide you with the binary of interest and the number of detections/alerts they generate. When I say alert think of it as a "suspicion of a vulnerability". 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-132.png)

If we click on `/sbin/ncc2` which has ~244 alerts, or potential vulnerabilities. By expanding the drop downs we can get a quick view of where it believes the issues are. This is great for quickly parsing and identifying a funky `%s`, `strcpy`, `memset`, etc. I personally use it to prioritize functions I find interesting.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-131.png)

What's fun with Shambles is that it provides you with the pointer to the function that the static analysis or triggered on. As seen below Shambles believes there's a potential BOF in the `sub_49f280` function because of the following operation `strcpy(&var118, get_entry_value_by_name(p1, p2, "nextPage"))` which makes a lot of sense if the buffer for `var118` is tiny and we can pass input through a `nextPage` parameter. Personally, this allows me to quickly weed out what are and quickly actionable vulnerable functions, and which aren't. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/04/image.png)

You can simply double-click it to be brought to its disassembled view.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-124.png)

The color coding used is defined in the picture below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/imgonline-com-ua-twotoone-MXykBQpMYc.jpg)

By going to the ASM view of the function and hitting `TAB` we can obtain the pseudocode, which feels a lot like it and looks much nicer than IDA/Ghidra. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-61.png)

As mentioned previously, I won't be able to show every Shambles feature I find amazing. But I do want to shine some light on their being a really well-built search tool (`Alt+T` to spawn) Using it is a huge time-save and is one of the best I've used.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-13.png)

Through the search, you're provided with the ASM view. But there's also the strings view, import view (functions imported by the analyzed binary), export view (program's entry point for execution), segment view (segments present in the binary), and hex view. 

So let's have a look at whether or not Shambled found a valid vulnerability. 

The `nextPage` parameter does in fact appear to be vulnerable to a buffer overflow when the string returned by `get_entry_value_by_name(p1, p2, "nextPage")` is longer than `260 bytes`. `strcpy` might write past the end of the `var118` buffer, causing a buffer overflow. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-45.png)

To prove a point, we are also going to look at a command injection that was discovered in the `Low Vulnerability` section. There is actually also a buffer overflow in this function. Oftentimes when you have a BOF you also have a command injection. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-133.png)

This is a bit of a longer function, all you need to know is that the function takes in 3 parameters.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-135.png)

The function then calls `get_entry_value_by_name` three times, passing `p0`, `p1`, `p2` as `ddnsHostName`, `ddnsUsername`, and `ddnsPassword` respectively. This is going to be the input we control and pass to the `ddns_check.c` endpoint via the `doCheck` parameter. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-134.png)

after assigning some values to some variables and doing some checks the code then calls `__system` function with a formatted command string. This function under the hood executes a system command of `/bin/sh` onto the `noip2` binary seen below.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-73.png)

Our provided input will be "injected" into the `%s` format string since it is intended for our passing string argument that represents a command to be executed. This looks extremely promising. 

For context, these two vulnerabilities took approximately 5-7 minutes each to identify, locate, and make sense of through Shambles. How can we make this process even faster? The answer is with Artificial Intelligence! 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-149.png)

As of `Version 1.2.2` Lain Security added the AI Assistant to Shambles! Before if the pseudocode was confusing you'd copy everything into ChatGPT and ask it to make sense of it for you. Or you'd spend 15 minutes slowly working through functions. Shambles AI assistant is there to help make your life easy. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-7.png)

Located right under the Virtual Machine side panel, let's see what the AI Assistant says about our buffer overflow in the `sub_49f280` function. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-81.png)

Its analysis is quite spot on. And I'm sure we all can see the value in such a feature. In many ways, it's a better description and analysis than I gave you guys previously regarding `sub_49f280`. There are a lot more ideas and exploit paths to validate. And for those of us who do this late at night with a few 青岛啤酒 beers in our system, the Detailed Interpreter makes life so much better with easy-to-follow pseudocode commenting as seen below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-8.png)

Now that we have two potential vulnerabilities, we want to validate their legitimacy. Normally this is where you'd pull out your janky unmaintained Ubuntu 18.04 with a shaky [FirmAE](https://github.com/pr0v3rbs/FirmAE?ref=boschko.ca) or [QEMU](https://www.qemu.org/?ref=boschko.ca) environment and hope nothing breaks. With Shambles there's no need to stress or worry! We're able to emulate our firmware and validate our vulnerabilities by using the Shambles built-in dynamic emulator! 

In the official documentation, it's often referred to as `dynamic simulation mode` but we'll call it setting up the Virtual Machine (VM) mode which will contain all the application functions in static analysis. Shambles VM mode is a built-in operating environment that provides and enables the firmware to run dynamically. You can perform operations such as debugging, hooking, monitoring, and editing the firmware.

To be able to access and create a VM you must click on the dropdown arrow as seen below to switch from `Blue -> Green`, green being the VM mode a state achieved after synchronizing the interfaces.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-32.png)

To enter the synchronization interface click `Sync Emulator` seen below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-40.png)

When the firmware synchronization is complete, you can see that the color of the firmware name in the Mode switch changes (turns green).

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-42.png)

After entering Dynamic simulation a.k.a VM mode for this firmware you'll be able to create a virtual machine for it. As seen in the steps below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-82.png)

If you've ever emulated firmware you'll know you often have to make modifications to `rCS`, `init.d`, or `httpd.conf`. In Shambles, you will typically have to change the hardcoded boot IP to `0.0.0.0` for the emulation to work properly. At times you'll also have to kill the webservers (`httpd`, `jhttpd`, `bao`, etc.,) pid and restart it manually from within the SSH console which we will soon see. Here is a [good Shambles article with commonly seen emulation debugging](https://liansecurity.feishu.cn/docs/doccnoReH3epH8X3fdXJlFlxMLe?ref=boschko.ca) (to easily translate, append `.translate.goog` after TLD (`.com`) of the page). 

If we have to make changes to the files of the Virtual Machine we'd have to do it through the static terminal as seen below. This can only be accessed in VM mode. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-48.png)![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-49.png)

Once all the changes have been made, refresh the filesystem, and start the virtual machine. For this firmware, no modifications needed to be made for it to be emulated properly. We can go ahead and start the machine by clicking the play button.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-50.png)

Once we start the VM, a new panel will open containing verbose error messages, the boot processes, general tasking, logging, and output from the device's usage. After running this for a few seconds, we will want to see if the router started properly. We'll be able to see all of this by starting an SSH shell inside of Shambles to the emulated firmware by clicking the button seen below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-52.png)

This will be a live interactive shell spawned from the emulated firmware as a mount flash from which an SSH will spawn. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-53.png)

Now we have an SSH shell on the running firmware being emulated we can check to see if the proper daemons have started and make sure the required processes are working fine. As seen below the router is up and running without any hiccups.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-69.png)

Our goal now is to validate our vulnerability with a tool such as [Caido](https://caido.io/?ref=boschko.ca) or [Burp Suite](https://portswigger.net/burp?ref=boschko.ca). To do so we'll want to access the router through our browser. To achieve this we'll have to set up port forwarding. Here is a diagram of how the routing needs to flow.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/Blank-diagram.png)

As seen above port forwarding is not complicated. The virtual machine runs on a cloud host, so it is necessary to forward the network of the virtual machine first, and then establish a connection with the user's local machine. We will only want to forward port `80` for our router. So we will add a forward rule as seen below.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-57.png)

Here we are mapping port `80` which is webserver port inside of the VM to port `10040` in the `Setting` panel. We then need to head over to the `Local Forward` panel.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-58.png)

Then all we have to do is start the forward.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-59.png)

Voila! We've successfully emulated the firmware and can start interacting through the UI. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-61.png)

Now that everything is running smoothly we'll focus back on validating our two suspected vulnerabilities. We'll start off with the stack-based buffer overflow. Again we are sending a `canclePing` action to `ping.ccp` with a `nextPing` value greater than `260` characters long.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-144.png)

Sending such a request crashes the application. If you try to send the request again you won't be able to since the initial BOF crashed the server which is basically an unauthenticated DOS BOF. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-143.png)

We can see from the main VM panel the system killed the `ping` process causing the router to DOS due to it segfaulting as a result of our POST request of `canclePing` with malicious `nextPage` input. We can see from the image below that the stack is overwritten with `0x41` which is hexadecimal for `A`. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-67.png)

This BOF brakes the application completely so all we have to do is reboot the VM to get it working again. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-151.png)

I won't be covering this bug via the Shambles debugger. However, I can say I have absolutely no complaints about it. It does everything a debugger needs to do and more. 

Now let's go ahead and validate the command injection vulnerability. We're invoking everything through the `doCheck` function where our vulnerable input parameters are `ddnsHostName` and `ddnsUsername` and our malicious input is going to be `;/bin/ps>/www/BlogDemoCommandInjection_Hostname.txt;` and `;/bin/ps>/www/BlogDemoCommandInjection_Username.txt;` respectively using `;` as a command delimiter to escape the binary that's being run by `/bin/sh` which is `noip2`.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-138.png)

Once our POST request is sent to the application, we can use Shambles SSH shell to validate that these files were created and contain `4316` bytes, the output of the `ps` command. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-139.png)

Moreover, we can see from the VM console log it's complaining that certain arguments weren't found. This is really useful for times when you're debugging or trying to get the proper syntax or escape for command injection.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-142.png)![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/05/image-137.png)

Since we wrote the file to the webroot we're able to view our file in the browser as well. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-69.png)

Another class of vulnerability I've enjoyed discovering with Shambles is what I'd call "patch bypasses". I think it's more widely known as "patch diffing"; the process of cross-comparing the vulnerable and fixed versions of a product. 

Exploiting old 0-day security patches is a great opportunity to learn and understand how vendors go about remediating vulnerability classes. I've come to realize that their implementations/fixes are often rushed and quite flawed. Typically, you would use awesome tools like [BinDiff](https://www.zynamics.com/bindiff.html?ref=boschko.ca) to accomplish this, however, Shambles offers a similar solution built in that I quite enjoy using. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/7ubv1i.jpg)

To use this feature you must upload both firmware versions, the patched and the vulnerable one.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-76.png)

Once loaded into Shambles you'll have an expanded `Firmware Info` now containing a `Similar Graph` section as seen below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-77.png)

You can have as many nodes as you have cloned instances of the modified firmware. Once you hit `Compare` you'll be presented with the following view. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-73.png)

You can expand whatever package or binary you want to get additional information on. This includes but is not limited to functions that have changed as seen in the view below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-74.png)

You can step into any of these and see the assembly changes.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-76.png)

Therefore it goes without saying, you can hit `TAB` to obtain pseudocode to start understanding the patch. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/03/image-75.png)

This might not look powerful. However, once you start hunting for authentication bypass and start referring to old 0-day bypass you'll come to fully appreciate and use this functionality. For a dynamic demonstration of this feature check out [H4kb4n](https://twitter.com/h4kb4n?ref=boschko.ca)'s tweet 😃

> A dynamic demonstration would be better! Demonstration of shambles bindiff feature.[#shambles](https://twitter.com/hashtag/shambles?src=hash&ref_src=twsrc%5Etfw&ref=boschko.ca) [#liansecurity](https://twitter.com/hashtag/liansecurity?src=hash&ref_src=twsrc%5Etfw&ref=boschko.ca) [#reverseengineering](https://twitter.com/hashtag/reverseengineering?src=hash&ref_src=twsrc%5Etfw&ref=boschko.ca) [pic.twitter.com/bEf5pRWj1i](https://t.co/bEf5pRWj1i?ref=boschko.ca)
> 
> — h4k (@h4kb4n) [August 6, 2023](https://twitter.com/h4kb4n/status/1688232137294827520?ref_src=twsrc%5Etfw&ref=boschko.ca)

A great way to enhance Shambles is through custom detection. Shambles has an engine called BinQL which allows you to create detection rules to further assist you in vulnerability discovery.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-74.png)

BinQL findings are appended to the `ELF Vulnerability Info` findings which are potential vulnerabilities initially identified through Shambles basic vulnerability detection functions. As the name could have implied, you might think that it's an adaptation of [CodeQL](https://codeql.github.com/?ref=boschko.ca) spun around for binary file retrieval. However, it isn't, BinQL is a custom truly proprietary innovation. BinQL is fully cloud-base. Therefore, once your uploaded firmware finished unpacking, BinQL can automatically carry out its detection processes. Custom detections can be formulated through the `Plugin` menu seen below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-2.png)

The reason you would use BinQL is because different vendors and firmware use different functions which can be vulnerable and not completely natively ingested by Shambles. Such as `do_system`, `__system`, `exec_cste`, etc., As mentioned, there are numerous input and output functions some unique to certain firmware, it is impractical for Shambles to natively identify and collect them all, as different devices may use different ones. 

In other words, BinQL allows users to define templates for input and output functions which helps Shambles perform more customized checks and validations.

High level; BinQL works by reverse engineering the data flow at the Intermediate Representation (IR) level. By simulating its execution, the engine assesses if the user's input can modify the stack content, execute system commands, or perform file read/write operations. Obtaining user input is typically achieved by detecting common user input functions, such as `fgets`, `get_value`, etc., Moreover, to determine if modifications to the stack are possible, Shambles look for functions like `strcpy`, `memcpy`, etc., which are defined in binql as output functions. 

Once you open the binary of interest, select `Plugin -> Vulnerability -> Analysis` the following web page will spawn. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/07/image-67.png)

Here is where you can enter your BinQL detection rules. These are rules you'd customize for the current binary. Once your rules are generated, click `Submit` and your rules will submit to the cloud detection server where the status will display the status of cloud detection and cannot be resubmitted while running. 

Here's how the detection rules work.

Name | Type | Description  
---|---|---  
name | String | Name of the function protocol  
retValue | int | Type of the return value  
Possible values:  
-1: IGNORE, current value type can be ignored  
0: OP_PRINTF_FORMAT, current value type is output format  
1: OP_IN, current value type is tainted input  
2: OP_OUT, current value is tainted output  
3: OP_SCANF_FORMAT, current value type is input format  
4: BUFFER_LENGTH, current value type is buffer-related length  
paramList | List | Types of all parameters. Possible values are the same as above  
matchString | String | String used for matching  
matchType | int | Matching method  
Possible values:  
0: equals  
1: contains  
2: startsWith  
3: endsWith  
4: regex  
functionType | int | Type of the current function  
Possible values:  
0: The current function serves as an input source  
1: The current function can execute commands  
2: The current function may cause buffer overflow  
3: The current function is related to file access  
  
We've previously identified that `get_entry_value_by_name` can lead to a stack based buffer overflow. Ultimately it has the chance of passing user-provided input which may get pushed to the stack. We're looking to identify instances like these. 
  
  
  v1 = get_entry_value_by_name(p1, p2, "fromLan");
  v41 = get_entry_value_by_name(p1, p2, "ddnsPassword");
  v61 = get_entry_value_by_name(v1, v3, "WlanValue");

To accomplish this we must first understand what `get_entry_value_by_name(p1, p2, p3);` means. So that we can assign the proper BinQL retValues which is extremely important. So, `get_entry_value_by_name` is defined in `libleopard.so` and named `get_entry_by_name`. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-4.png)

`get_entry_by_name` finds the position of the `p3` in the `p1`, this is not a stack overflow itself, but when the return value is used, there possibility that it will be pushed to a variable with an overflowable stack base. So the return value which is from the first parameters is referred to as `tainted output`. The first parameter of this function will be referred to as `tainted input`. The function `get_entry_value_by_name` is a function produces input that can lead to a stack overflow. So it is an `input function`. Therefore the BinQL configuration would be the following.
  
  
  [{
  "name":"get_entry_value_by_name",
  "retValue":2,
  "paramList":[1, 4, -1],
  "matchString":"get_entry_value_by_name",
  "matchType":0,
  "functionType":0
  }]

Therefore, our query to further identify interesting `get_entry_value_by_name` in the `ncc2` binary will be with the query below. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-3.png)

Once the `Server status` is finished shambles `ELF Vulnerability Info` panel will have the updated BinQL queried content.

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-5.png)

To better help you understand BinQL we've provided a few examples as it can be a little confusing to first-time users. First, let's look at an example of marking `tainted output`.

`int * web_get(int *a1, int *key, int a3, int a4, int a5);`

The function `web_get` is used to read parameters from the HTTP protocol. The first parameter is a pointer to all data, and the second parameter is the key of the data to be read. The return value is the required `tainted output` value. The matching method is `web_get`. Therefore our BinQL config will be in the following JSON format.
  
  
  [{
  "name":"web_get",
  "retValue":2,
  "paramList":[-1,-1,-1,-1,-1],
  "matchString":"web_get",
  "matchType":3,
  "functionType":2
  }]

Now lets look at an example of marking `tainted input`.

`FILE * popen(const char *command, const char *type);`

The function `popen` can execute commands. The first parameter is the `tainted input` parameter, and the other parameters can be ignored. The matching method is `popen`. 
  
  
  [{
  "name":"popen",
  "retValue":-1,
  "paramList":[1,-1],
  "matchString":"popen",
  "matchType":3,
  "functionType":2
  }]

Lastly let's look at an example of marking `tainted output`, `tainted input`, and `length`.

`char *strncpy(char *dest, char *src, int n);`

The function `strncpy` can cause buffer overflow if used improperly. The first parameter is `tainted output`, the second parameter is `tainted input`, and the third parameter is the `length to be copied`. The matching method is `strncpy`.
  
  
  [{
  "name":"strncpy",
  "retValue":-1,
  "paramList":[2,1,4],
  "matchString":"strncpy",
  "matchType":3,
  "functionType":2
  }]

After using BinQL, depending on the function protocol you've generated detection rules for you can expect to see a drastic increase in identified vulnerabilities. 

![](https://storage.ghost.io/c/29/6a/296af8dc-aee9-49ab-b451-8f11e2049940/content/images/2023/08/image-8.png)

* * *

That's it for now 🎉 you've made it to the end! There's _A LOT_ of features and amazing quality-of-life hacks that I didn't cover. Make sure to join the Lian Security [Discord](https://discord.gg/aUH9Yphtb5?ref=boschko.ca) to obtain early access to Shambles! If you want to see Shambles in action go watch me on [Twitch](https://www.twitch.tv/olivier_boschko?ref=boschko.ca)! 

## ******Summary:******

I hope you liked the blog post. Check out [https://liansecurity.com/](https://liansecurity.com/?ref=boschko.ca) and all their products & offerings their engineers are genuinely top shelf. 

Expect a lot more Shambles in future blog posts. Again I can't stress enough how massive of a time-save Shambles has been. The finalized pricing model will soon be official and stable. If you have questions or want to learn more about the tool send us a message on [Discord](https://discord.gg/wxJMRm8Hyg?ref=boschko.ca) or to me directly on [Twitter](https://twitter.com/olivier_boschko?ref=boschko.ca) and I'll pass on your questions or concerns. 

Follow me on [Twitter](https://twitter.com/olivier_boschko?ref=boschko.ca) I sometimes post interesting stuff there too. 

****Thank you for reading!****

* * *

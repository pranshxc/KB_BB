---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-06_our-experiences-participating-in-microsofts-azure-sphere-bounty-program.md
original_filename: 2020-10-06_our-experiences-participating-in-microsofts-azure-sphere-bounty-program.md
title: Our Experiences Participating in Microsoft’s Azure Sphere Bounty Program
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 9d29818c57746e0c120166414d303e24cfa23c8170376b98179a7673d8d88082
text_sha256: cc9d9c3d166da32dc024bfb8c2fb9b461165d4bc550fea7f745fb524ae46ec63
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Our Experiences Participating in Microsoft’s Azure Sphere Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-06_our-experiences-participating-in-microsofts-azure-sphere-bounty-program.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `9d29818c57746e0c120166414d303e24cfa23c8170376b98179a7673d8d88082`
- Text SHA256: `cc9d9c3d166da32dc024bfb8c2fb9b461165d4bc550fea7f745fb524ae46ec63`


## Content

---
title: "Our Experiences Participating in Microsoft’s Azure Sphere Bounty Program"
url: "https://www.mcafee.com/blogs/other-blogs/mcafee-labs/our-experiences-participating-in-microsofts-azure-sphere-bounty-program/"
authors: ["McAfee Advanced Threat Research (ATR)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation", "RCE", "Security Feature bypass"]
bounty: "160,000"
publication_date: "2020-10-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4216
scraped_via: "browseros"
---

# Our Experiences Participating in Microsoft’s Azure Sphere Bounty Program

Our Experiences Participating in Microsoft’s Azure Sphere Bounty Program
Philippe Laulheret

OCT 06, 2020

4 MIN READ

From June to August, part of the McAfee Advanced Threat Research (ATR) team participated in Microsoft’s Azure Sphere Research Challenge.  Our research resulted in reporting multiple vulnerabilities classified by Microsoft as “important” or “critical” in the platform that, to date, have qualified for over $160,000 USD in bounty awards scheduled to be contributed to the ACLU ($100,000), St. Jude’s Children’s Research Hospital ($50,000) and PDX Hackerspace (approximately $20,000). With these contributions, we hope to support and give back both to our local hacker community that has really stepped up to help during the COVID crisis, and also recognize, at a larger scale, the importance to protect and further civil liberties and the wellbeing of those most in need.  

This blog post is a high–level overview of the program, why we choose to take part in it, and a brief description of our findings. A detailed technical walkthrough of our findings can be found here.  

Additionally, Microsoft has released two summary blogs detailing the Azure Sphere Bounty Program as a whole, including McAfee’s efforts and findings. They can be found here:

MSRC Blog

Azure Sphere Core Team Blog

What is Azure Sphere and the Azure Sphere Research Challenge? 

In late May Microsoft started a new bug bounty program for its Azure Sphere platform. Azure Sphere is a hardened IoT device with a secure communication link to the cloud that has been in development for the last few years and reached general availability in early 2020. Microsoft designed and built it from scratch to ensure every aspect of it is as secure as possible, per their security model. To put the theory to test, Microsoft invited a few select partners and hackers to try their best to defeat its security measures.  

The Azure sphere team came up with multiple scenarios that would test the security model of the device and qualify for an increased payout from the regular Azure Bug Bounty program. These scenarios range from the ability to bypass certain security measures, to executing code in the hardware enabled secure core of the device.  

Research scenarios specific to the Azure Sphere Research Challenge 

Why did ATR get involved with the program? 

There are multiple reasons why we were keen to participate in this program. First, as security researchers, the Azure Sphere platform is an exciting new research target that has been built from the ground up with security in mind. It showcases what might become of the IoT space in the next few years as legacy platforms are slowly phased out. Being at the forefront of what is being done in the IoT space ensures our research remains current and we are ready to tackle future new challenges. Second, by finding critical bugs in this new platform we help make it more secure and offer our support to make the IoT space increasingly resistant to cyber threats. Finally, as this is a bug bounty program, we decided from the start that we would donate any award we received to charity, thus using our skills to contribute to the social good of our local communities and support causes that transcend the technology sector.   

Findings 

We’ve reported multiple bugs to Microsoft as a result of our research that were rated Important or Critical: 

Important – Security Feature bypass ($3,300): The inclusion of symlink in application package allows for referencing files outside of the application package mount point. 
Critical – RCE ($48,000): The inclusion of a “character device” in an application package allows for direct interaction with a part of the flash memory, eventually leading to the modification of critical system files and further exploitation. 
Important – EoP ($11,000): Multiple bugs in how uid_map files are processed, allowing for elevation of privilege to the sys user.  
Important – Eop ($11,000): A user with sys privileges can trick Application Manager into unmounting “azcore” and mount a rogue binary in its stead. Triggering a core dump of a running process will then execute the rogue binary with full capabilities & root privileges due to improper handling of permissions in the LSM. 
Critical – EoP ($48,000): Further problems in the privilege dropping of “azcore” leads to the complete bypass of Azure Sphere capability restrictions 
Critical – EoP ($48,000): Due to improper certificate management, it is possible to re-claim a device on the Azure Sphere pre-prod server and obtain a valid capability file that works in the prod environment. This capability file can be used to re-enable application development mode on a finalized device (claimed by a third party). The deployment of the capability file requires physical access to a device.  
Conclusion 

This research was an exciting opportunity to look at a new platform with very little prior research, while still being in the familiar territory of an ARM device running a hardened Linux operating-system.  

Through the bugs we found we were able to get a full chain exploit from a locked device to having root access. However, the Azure Sphere platform has many more security features such as remote attestation, and a hardware enabled secure core that is still holding strong.  

Finally, we want to thank Microsoft for the opportunity of participating in this exciting program, and the bounty awards.  

Introducing McAfee+

Identity theft protection and privacy for your digital life

Download McAfee+ Now

Stay Updated

Follow us to stay updated on all things McAfee and on top of the latest consumer and mobile security threats.

Philippe Laulheret

Philippe Laulheret is a Senior Security Researcher on the McAfee Enterprise's Advanced Threat Research team. With a focus on Reverse Engineering and Vulnerability Research, Philippe uses his background in Embedded...

More from McAfee Labs
Previous
Think Before You Click: EPI PDF’s Hidden Extras
Authored by: Anuradha & Prabudh PDF converting software can be super helpful. Whether you’re turning a Word...

AUG 04, 2025   |   7 MIN READ

Android Malware Targets Indian Banking Users to Steal Financial Info and Mine Crypto
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new Android malware campaign targeting Hindi-speaking users,...

AUG 04, 2025   |   8 MIN READ

Fake Android Money Transfer App Targeting Bengali-Speaking Users
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new and active Android malware campaign targeting...

JUL 14, 2025   |   8 MIN READ

Stolen with a Click: The Booming Business of PayPal Scams
In today’s digital age, online payment platforms like PayPal have become essential tools for our everyday transactions....

APR 11, 2025   |   4 MIN READ

Game Over: WeedHack – The Rise of Minecraft Malware-as-a-Service Campaigns
If you or your child plays Minecraft, here's what you need to know about a large-scale malware campaign McAfee Labs...

JUN 02, 2026   |   3 MIN READ

Sinkholing CountLoader: Insights into Its Recent Campaign
Authored by Harshil Patel and Sakshi Jaiswal  McAfee Labs has recently uncovered a large scale CountLoader campaign that uses multiple layers of...

MAY 13, 2026   |   10 MIN READ

Why Hackers Are Collecting Data They Can’t Read Yet. And How to Stay Safe
Hackers are collecting encrypted data today to decrypt later using quantum computing. Learn what “Harvest Now, Decrypt Later” means and...

APR 21, 2026   |   6 MIN READ

Operation NoVoice: Rootkit Tells No Tales
Authored By: Ahmad Zubair Zahid  McAfee’s mobile research team identified and investigated an Android rootkit campaign tracked as Operation Novoice....

MAR 31, 2026   |   15 MIN READ

AI Wrote This Malware: Dissecting the Insides of a Vibe-Coded Malware Campaign
McAfee Labs analyzes a malware campaign using AI-assisted code and fake software downloads. Learn how 440+ malicious ZIP files spread...

MAR 18, 2026   |   15 MIN READ

Learn to Identify and Avoid Malicious Browser Extensions
In this guide, you will learn about the advantages and security risks of browser extensions, the role...

NOV 20, 2025   |   13 MIN READ

Astaroth: Banking Trojan Abusing GitHub for Resilience
by Harshil Patel and Prabudh Chakravorty *EDITOR’S NOTE: Special thank you to the GitHub team for working...

OCT 10, 2025   |   8 MIN READ

Android Malware Promises Energy Subsidy to Steal Financial Data
Authored by ZePeng Chen Recently, we identified an active Android phishing campaign targeting Indian users. The attackers...

AUG 18, 2025   |   9 MIN READ

Think Before You Click: EPI PDF’s Hidden Extras
Authored by: Anuradha & Prabudh PDF converting software can be super helpful. Whether you’re turning a Word...

AUG 04, 2025   |   7 MIN READ

Android Malware Targets Indian Banking Users to Steal Financial Info and Mine Crypto
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new Android malware campaign targeting Hindi-speaking users,...

AUG 04, 2025   |   8 MIN READ

Fake Android Money Transfer App Targeting Bengali-Speaking Users
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new and active Android malware campaign targeting...

JUL 14, 2025   |   8 MIN READ

Stolen with a Click: The Booming Business of PayPal Scams
In today’s digital age, online payment platforms like PayPal have become essential tools for our everyday transactions....

APR 11, 2025   |   4 MIN READ

Game Over: WeedHack – The Rise of Minecraft Malware-as-a-Service Campaigns
If you or your child plays Minecraft, here's what you need to know about a large-scale malware campaign McAfee Labs...

JUN 02, 2026   |   3 MIN READ

Sinkholing CountLoader: Insights into Its Recent Campaign
Authored by Harshil Patel and Sakshi Jaiswal  McAfee Labs has recently uncovered a large scale CountLoader campaign that uses multiple layers of...

MAY 13, 2026   |   10 MIN READ

Why Hackers Are Collecting Data They Can’t Read Yet. And How to Stay Safe
Hackers are collecting encrypted data today to decrypt later using quantum computing. Learn what “Harvest Now, Decrypt Later” means and...

APR 21, 2026   |   6 MIN READ

Operation NoVoice: Rootkit Tells No Tales
Authored By: Ahmad Zubair Zahid  McAfee’s mobile research team identified and investigated an Android rootkit campaign tracked as Operation Novoice....

MAR 31, 2026   |   15 MIN READ

AI Wrote This Malware: Dissecting the Insides of a Vibe-Coded Malware Campaign
McAfee Labs analyzes a malware campaign using AI-assisted code and fake software downloads. Learn how 440+ malicious ZIP files spread...

MAR 18, 2026   |   15 MIN READ

Learn to Identify and Avoid Malicious Browser Extensions
In this guide, you will learn about the advantages and security risks of browser extensions, the role...

NOV 20, 2025   |   13 MIN READ

Astaroth: Banking Trojan Abusing GitHub for Resilience
by Harshil Patel and Prabudh Chakravorty *EDITOR’S NOTE: Special thank you to the GitHub team for working...

OCT 10, 2025   |   8 MIN READ

Android Malware Promises Energy Subsidy to Steal Financial Data
Authored by ZePeng Chen Recently, we identified an active Android phishing campaign targeting Indian users. The attackers...

AUG 18, 2025   |   9 MIN READ

Think Before You Click: EPI PDF’s Hidden Extras
Authored by: Anuradha & Prabudh PDF converting software can be super helpful. Whether you’re turning a Word...

AUG 04, 2025   |   7 MIN READ

Android Malware Targets Indian Banking Users to Steal Financial Info and Mine Crypto
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new Android malware campaign targeting Hindi-speaking users,...

AUG 04, 2025   |   8 MIN READ

Fake Android Money Transfer App Targeting Bengali-Speaking Users
Authored by Dexter Shin McAfee’s Mobile Research Team discovered a new and active Android malware campaign targeting...

JUL 14, 2025   |   8 MIN READ

Stolen with a Click: The Booming Business of PayPal Scams
In today’s digital age, online payment platforms like PayPal have become essential tools for our everyday transactions....

APR 11, 2025   |   4 MIN READ

Next
1
2
3

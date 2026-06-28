---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-13_patch-diffing-progress-moveit-transfer.md
original_filename: 2023-06-13_patch-diffing-progress-moveit-transfer.md
title: Patch Diffing Progress MOVEIt Transfer
category: documents
detected_topics:
- ssrf
- command-injection
- sqli
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- sqli
- automation-abuse
- api-security
language: en
raw_sha256: d14654de48d56c2b9ee7c94be5540ec838ec3cb82b2b60fa5a314c9b7c8aba03
text_sha256: 587db1b22d6e0ff27cf99284a87b71d5ad924dbfb9c592a9498f8af01070bf7a
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Patch Diffing Progress MOVEIt Transfer

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-13_patch-diffing-progress-moveit-transfer.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, sqli, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `d14654de48d56c2b9ee7c94be5540ec838ec3cb82b2b60fa5a314c9b7c8aba03`
- Text SHA256: `587db1b22d6e0ff27cf99284a87b71d5ad924dbfb9c592a9498f8af01070bf7a`


## Content

---
title: "Patch Diffing Progress MOVEIt Transfer"
page_title: "Patch Diffing Progress MOVEIt Transfer RCE (CVE-2023-34362)"
url: "https://blog.assetnote.io/2023/06/07/moveit-transfer-patch-diff-adventure/"
final_url: "https://www.assetnote.io/resources/research/patch-diffing-progress-moveit-transfer-rce-cve-2023-34362"
authors: ["Dylan Pindur"]
programs: ["Progress (MOVEit Transfer)"]
bugs: ["RCE", "SQL injection", "Security code review"]
publication_date: "2023-06-13"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1051
---

[Research Notes](/resources/research)

Security Research

June 7, 2023

# Patch Diffing Progress MOVEIt Transfer RCE (CVE-2023-34362)

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

In the last few days, threat actors have been exploiting a critical pre-authentication vulnerability within Progress MOVEIt Transfer. There have been several great blog posts covering the incident response, forensic artifacts, and detection engineering efforts when it comes to preventing compromise. [[1]](https://www.huntress.com/blog/moveit-transfer-critical-vulnerability-rapid-response) [[2]](https://www.trustedsec.com/blog/critical-vulnerability-in-progress-moveit-transfer-technical-analysis-and-recommendations/) [[3]](https://www.rapid7.com/blog/post/2023/06/01/rapid7-observed-exploitation-of-critical-moveit-transfer-vulnerability/).

Assetnote was successful at determining the full exploit chain for this vulnerability, including the SQL injection and the remote code execution attack vector. This exploit chain has been reproduced by our security research team and checks have been available and running on all customers. When critical vulnerabilities are exploited in the wild, our team works diligently in reverse engineering the exploit payloads and providing assurance to our customers on whether or not they are truly vulnerable via our [Attack Surface Management platform](https://assetnote.io/).

You can watch our RCE proof of concept video below:

This blog post will go into some detail about how to get an environment set up to reverse engineer this issue. At a later date, we will be disclosing the proof of concept and steps taken to reproduce the vulnerability.

Given that this vulnerability is still being actively exploited, no proof of concept will be published until a public proof of concept becomes available, or 30 days from now, after organisations have had time to patch their instances or remove them from the external internet.

When reverse engineering patches, the first step is to confirm that you are able to download and install two adjacent versions of the software (unpatched & patched) so that we can perform patch diffing. For a lot of researchers, this can often be the blocker before they have even gotten to the meatier parts of this process.

We were able to achieve this by first signing up for a trial for Progress MOVEIt Transfer and instantly obtaining a serial key and a download for the latest version of the software (<span class="code_single-line">2023.0.1</span>). This is a good start, but how are we going to get the unpatched version?

Doing some searches on Google, we came across the link <span class="code_single-line">https://cdn.ipswitch.com/ft/MOVEit/Transfer/2022/2022.1.1/MOVEit-Transfer-2022.1.1-FullInstall.exe</span>. We knew that <span class="code_single-line">2023.0.0</span> was vulnerable, and with a bit of wrangling, we were able to download this version through the following URL - <span class="code_single-line">https://cdn.ipswitch.com/ft/MOVEit/Transfer/2023/2023.0/MOVEit-Transfer-2023.0.0-FullInstall.exe</span>.

Installing this software has some challenges. We need a valid serial key to install the software, which thankfully we obtained through requesting a free trial. That serial key however, in order to use it for the older build, we have to go through the steps of the “Offline Activation” which generates a <span class="code_single-line">license.txt</span> which you can feed back into the installer.

After installing both versions of the software, we zipped up the <span class="code_single-line">C:\MOVEitTransfer\</span> for each respective version and ran it through [DiffMerge](https://formulae.brew.sh/cask/diffmerge) to see what had changed. We had to remove <span class="code_single-line">.dll</span> files from the exclusion list inside DiffMerge’s settings so that we could determine exactly which files to take a closer look at.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37d3a6b1a22f9672a9928_difftool.png)

We are aware that the exploitation logs for this vulnerability include requests to <span class="code_single-line">MOVEitISAPI.dll</span>, but this is not something we can decompile with ILSpy. It is a native binary that we will have to use Ghidra to reverse engineer. Before we get to that point, we decided to focus on what could be decompiled to see if there were any clues as to how this vulnerability is exploited.

Looking at the DLL files inside the <span class="code_single-line">wwwroot/bin</span> folder, we can see that there are a number of files that have changed. The next step is to decompile these DLL files using [ILSpy](https://github.com/icsharpcode/ILSpy) and compare the source code again using DiffMerge.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37d390685e1145d4a1416_ilspy.png)

After decompiling these files and comparing the patched and unpatched versions with DiffMerge, we noticed this specific code had been removed from the patched version:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37d398b4e924fc90109a1_patch-diff-1.jpeg)

Seeing this, we quickly realised the impact of this code, allowing you to set session variables arbitrarily based on the header input from a request. This seemed like a real lead towards discovering the root cause of this vulnerability.

We spent some time tracing the code and understanding how this function was called in the first place. Our investigation led us to <span class="code_single-line">machine2.aspx</span>, which seemingly can only be called via the internal network. Looking at the blog post from [Huntress Labs](https://www.huntress.com/blog/moveit-transfer-critical-vulnerability-rapid-response) and speaking with [wvu](https://twitter.com/wvuuuuuuuuuuuuu) on Twitter, we realised that the way <span class="code_single-line">machine2.aspx</span> was called was via an SSRF through <span class="code_single-line">MOVEitISAPI.dll?action=m2</span>.

For us to investigate this further, we needed to install the software and get a dynamic debugging environment set up. This is quite simple given that the MOVEit Transfer installer works out of the box without too much fiddling. It installs the software, as well as a MySQL database by default. Remember to save all of the credentials you have set locally.

Confirm that you can login to the MOVEit Transfer web application on localhost, and once that’s done, download a copy of [Jetbrains Rider](https://www.jetbrains.com/rider/) in order to set up a debugging environment. We prefer using Rider when doing dynamic debugging as it automatically attaches to the process running the web application and dynamically decompiles all of the loaded assemblies.

You can achieve this by clicking the “Attach to Process” button when starting up Rider, and selecting the W3WP process that runs the moveitdmz application:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37d3ae02bf014fb1fd3b7_rider.png)

After attaching to the process, on the left hand side you will see all of the assemblies are decompiled magically by Rider. You can pick the assembly you’re interested in, for our case, <span class="code_single-line">midmz</span> -> <span class="code_single-line">MOVEit.DMZ.WebApp</span> -> <span class="code_single-line">SILMachine2</span> -> Set a breakpoint in the <span class="code_single-line">Machine2Main</span> function:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37d396ac5fe81a538eb1a_rider2.png)

At this point, we are able to debug the application and confirm that we are able to hit <span class="code_single-line">machine2.aspx</span> via the SSRF located at <span class="code_single-line">MOVEitISAPI.dll?action=m2</span>.

While there are several more steps necessary for exploitation, we plan on releasing these details after organizations have had time to patch their instances.

We will update this blog post in 30 days time with the full details of the exploit chain.

Written by:

Dylan Pindur

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

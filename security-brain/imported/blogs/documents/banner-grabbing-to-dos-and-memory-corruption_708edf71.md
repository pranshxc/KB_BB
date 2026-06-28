---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-16_banner-grabbing-to-dos-and-memory-corruption.md
original_filename: 2019-04-16_banner-grabbing-to-dos-and-memory-corruption.md
title: Banner Grabbing to DoS and Memory Corruption
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 708edf712db4913af6f359fae2b2046c45f1b494ad7ee579464dee00c4185c8e
text_sha256: cf29ece4b2023e8d5d912748d2ad6c9c393d103b65ac52fbdba0fb35a85af4a1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Banner Grabbing to DoS and Memory Corruption

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-16_banner-grabbing-to-dos-and-memory-corruption.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `708edf712db4913af6f359fae2b2046c45f1b494ad7ee579464dee00c4185c8e`
- Text SHA256: `cf29ece4b2023e8d5d912748d2ad6c9c393d103b65ac52fbdba0fb35a85af4a1`


## Content

---
title: "Banner Grabbing to DoS and Memory Corruption"
url: "https://medium.com/bugbountywriteup/banner-grabbing-to-dos-and-memory-corruption-2442b1c25bbb"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["DoS", "Information disclosure"]
publication_date: "2019-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5305
scraped_via: "browseros"
---

# Banner Grabbing to DoS and Memory Corruption

Banner Grabbing to DoS and Memory Corruption
Daniel "V" Morais
Follow
5 min read
·
Apr 16, 2019

194

Hello friends,

Sorry for my absence, I’ve been working hard these days but here I am, making my contribution to our community. Today’s topic is about a flaw that I encountered in a company I ran the Pentest privately, where I found an IIS server among its various * .subdomains.com. This specific one had two CVE’s.

What I found interesting to share was that at the beginning of my bug bounty journey, I used to report low ‘hanging fruits’ without even trying to exploit them, e.g, banner grabbing.

Press enter or click to view image in full size

As you can see in the image above, often the banner grabbing itself will be considered low impact and your report will most likely be closed as informative. As time goes by, you get more knowledge, your methodology changes, and you start to improve the way you look at your target, having said that, let’s start:

Banner grabbing and bug bounty

Banner grabbing is a process to collect details regarding any remote PC on a network and the services running on its open ports. An attacker can make use of banner grabbing in order to discover network hosts and running services with their versions on their open ports and moreover operating systems so that he can exploit it.

To make a significant impact on that, check the list of active hosts with the banner displayed, write them down, and start looking for the vulns of the versions. Something simple, but little practiced by beginners, who usually report the low impact vuln without wanting to deepen it enough to become critical.

From banner grabbing to DoS and memory corruption

I will show you the step by step that I made to transform a banner grabbing in DoS and memory corruption, using only the exploits spread on the internet. The company (which did not allow to be identified then let’s call redacted) had several subdomains, and many of them with their banner exposed, including on ports like ssh, ftp, but my focus will be on port 80 (http), where they did use of a internal ticket system.

Discovery:

I used the following nmap command to check for banners that could help me in the next approach of the target

nmap -Pn -p 80, 443 -sV — script=banner -iL all_subdomains.txt

Press enter or click to view image in full size

For users who do not want to use nmap, this check could be done by CURL:

curl -s -I 192.168.0.100 | grep -e “Server: “

Press enter or click to view image in full size

The redacted company allowed DoS in its scope, since I was working locally for it, it was easy to get in touch with the infrastructure team to report on some critical flaw in that regard. Keeping in mind the IIS servers, in a quick search I found exploits to perform DoS on microsoft servers (MS15–034) to not be extensive, you can read more about the vuln here.

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Detecting the vulnerability:

The vulnerability can be triggered by specifying the Range header in an HTTP request. A vulnerable install will respond with an HTTP 416 Requested Range Not Satisfiable error.

Press enter or click to view image in full size

Am I really getting this error? Great!

Following the tutorial of the link above, I had just to specify the valid file and the byte range of 100 and as a result it lead me to a blue screen, it means … DoS!

Press enter or click to view image in full size

Remember, when dealing with DoS in a bounty bug, check if this type of vuln is allowed, if it’s not and still you find it relevant, communicate the team properly, what I did above was accompanied by the responsible team from the company.

Sometimes the same version may have more than one critical vulnerability, which was the case with this IIS server, had previously read that it was possible to run memory dump, let’s see how the result was:

Wait, Memory dump?

Anything that lets you corrupt the memory on a server has the potential of a remote code execution. At least, it lets you crash processes or the operating system. We have a metasploit module for this IIS vuln (always check there using search options)

Setting metasploit module

Press enter or click to view image in full size

Response:

The screen is beautiful but … no “critical” data at the time I performed the dump, regardless of that, the vulnerability was successfully confirmed, which was enough :)

Metasploit memory dump module for IIS link here.

Takeaways:

As you have been able to observe, I have tried to focus more on the beginner community, showing how to look in a different way for those low impact vulns that are very common to find. I hope I have contributed in a way, just as I learn from all of you. Happy Hacking!

Hope you liked it, now I have a twitter so we can share knowledge there also.

Find me here.

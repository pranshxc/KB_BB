---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-22_ssti-in-google-maps.md
original_filename: 2020-12-22_ssti-in-google-maps.md
title: SSTI in Google Maps
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: ba02702dbb967a5d877046a16e917be9217aa78b313fc4fe21488402f45cab83
text_sha256: d791cf66a63e6bb7dc7c6ac716ec4c47e1bedd338a11531d2099bccdf2cdc268
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# SSTI in Google Maps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-22_ssti-in-google-maps.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `ba02702dbb967a5d877046a16e917be9217aa78b313fc4fe21488402f45cab83`
- Text SHA256: `d791cf66a63e6bb7dc7c6ac716ec4c47e1bedd338a11531d2099bccdf2cdc268`


## Content

---
title: "SSTI in Google Maps"
url: "https://www.ehpus.com/post/ssti-in-google-maps"
final_url: "https://www.ehpus.com/post/ssti-in-google-maps"
authors: ["s1r1us (@s1r1u5_)"]
programs: ["Google"]
bugs: ["SSTI"]
publication_date: "2020-12-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4055
---

# SSTI in Google Maps

  * zohar shachar
  * Dec 22, 2020
  * 3 min read

A while back I was researching Google Maps ‘timeline’ feature, and specifically the capability to add your own ‘places’. I was trying to replicate [_a previous XSS I found_](https://www.ehpus.com/post/xss-fix-bypass-10000-bounty-in-google-maps) in the ‘export as KML’ feature, and thought the custom place ‘name’ could be a good spot to place my payload. As I was poking around, suddenly something caught my eye - one of the ‘places’ I entered was displayed incorrectly. I couldn’t remember what ‘name’ I entered, but I was sure it was not what was displayed:

  

[![](https://static.wixstatic.com/media/5527e6_5dedff1196d344cb860dd088b1eccc36~mv2.jpg/v1/fill/w_124,h_109,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_5dedff1196d344cb860dd088b1eccc36~mv2.jpg)](https://static.wixstatic.com/media/5527e6_06042d14274643499f2bfc8045733997~mv2.png)

  

What? **_Placeholder_**? What’s going on here?

  

**Initial discovery**

I set about trying to reproduce the result above. I initially thought that, perhaps, I entered something along the lines of “ _aaaaaaa}_ ” (notice the curly brackets), and somehow these curly brackets ‘closed’ the input, allowing me to ‘inject’ free chars, and then something got broken. 

Following this line of thought, I tried inputting the payload “ _aaa{}_ ”. I didn’t get the result I was looking for, but instead something else happened - Suddenly, the GUI ‘hang’ and I could not continue working without a hard refresh. Reviewing the network requests, I finally found that the response for the “ _aaa{}_ ” payload was a ‘500 error’ from the server that subsequently caused something to break on the client side. 

Further testing showed that any payload into the ‘place’ name that contains a curly bracket will cause the server to fail.

  

Encouraged by these initial results, I kept attempting more & more payloads, until I finally was able to reproduce the 'placeholder' issue by entering a payload of the form “ _xxxxxx’_ ” (i.e. any char ending with a single quote). 

  

So now I had two working ‘payloads’ that break _something_ , one error recoverable and one not, which led me to two conclusions:

  1. The server is using the client-provided ‘place name’ while generating the client side page, using some sort of template. 

  2. The input validation is lacking, and the client can interfere with the template structure.

  

In other words - we had here a clear case of server-side-template-injection! 

I continued to poke around until I managed to build a payload that injects ‘harmless’ content without breaking the template, of the form “ _ANYTEXT}=2 {ANYTEXT}ANYTEXT{ANYTEXT'_ ”

The results can be seen here:

  

[![](https://static.wixstatic.com/media/5527e6_06042d14274643499f2bfc8045733997~mv2.png/v1/fill/w_62,h_59,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_06042d14274643499f2bfc8045733997~mv2.png)](https://static.wixstatic.com/media/5527e6_06042d14274643499f2bfc8045733997~mv2.png)

  

**Is it exploitable?**

As exciting all of this research was, I still could not really point to an actual risk. [_Encouraged by amazing research_](https://portswigger.net/research/server-side-template-injection) on SSTI vulnerabilities I wanted to do something scary, to reference environment variables, to read sensitive data, even to run server side code… but I managed to do absolutely nothing. Not knowing which template engine I was working with, I had very little knowledge on how to move forward with this research.

  

Google has this awesome policy of rewarding the researcher for maximum potential damage, even if it was not demonstrated (you can read about it in the [_FAQ section of their policy_](https://www.google.com/about/appsecurity/reward-program/#faq)) and so I decided to report this ‘as is’ and hope for the best. 

  

Days after my initial report, I received a response that made me feel both confident and unconfident at the same time:

  

[![](https://static.wixstatic.com/media/5527e6_6daf4f5399d44132ac9e84fb53fe1f20~mv2.png/v1/fill/w_49,h_7,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_6daf4f5399d44132ac9e84fb53fe1f20~mv2.png)](https://static.wixstatic.com/media/5527e6_6daf4f5399d44132ac9e84fb53fe1f20~mv2.png)

So, the positive side was that Google’s team was able to reproduce this, identified this indeed as SSTI, and even were kind enough to clue me in into what template is used. 

  

The not-so-positive side was that Google’s team was clearly struggling to exploit this just as I was, and while I could excuse my own difficulties to my general blindness of the system internals, if Google’s engineers could not find a way to abuse this then it might not be possible to do. 

  

Indeed, I spent a lot of time trying to research the referenced template engine. I even recruited one of my most skillful colleagues to the challenge. Nonetheless, I just couldn’t make this happen. What I had here was a SSTI with no real harm. 

I’ve reported my failure back to Google, which replied with similar conclusions:

[![](https://static.wixstatic.com/media/5527e6_5baa86dbc5064bb7b93a741a89d5919b~mv2.png/v1/fill/w_49,h_10,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_5baa86dbc5064bb7b93a741a89d5919b~mv2.png)](https://static.wixstatic.com/media/5527e6_5baa86dbc5064bb7b93a741a89d5919b~mv2.png)

Inevitably, my ‘bug’ was no more:

![](https://static.wixstatic.com/media/5527e6_028069da6b6b44c0a6c84108bbf6efed~mv2.png/v1/fill/w_102,h_23,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_028069da6b6b44c0a6c84108bbf6efed~mv2.png)

  

**Final thoughts**

While I was for sure disappointed with the end result, that is the lifecycle of bug bounty - not all paths end in bounties. Nonetheless I enjoyed this research a lot, and was on the edge of my seat throughout - which at the end is why I do security research to begin with. Hope you enjoyed this as I did :)

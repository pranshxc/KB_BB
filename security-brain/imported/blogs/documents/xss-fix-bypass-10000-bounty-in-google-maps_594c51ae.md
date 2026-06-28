---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-07_xss-fix-bypass-10000-bounty-in-google-maps.md
original_filename: 2020-09-07_xss-fix-bypass-10000-bounty-in-google-maps.md
title: 'XSS->Fix->Bypass: 10000$ bounty in Google Maps'
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 594c51ae4d1a5c351f51779a95de8572ba63dc792a84d93e9b826784f5cca274
text_sha256: 2b85b064354d27bb544b4550983f1a7cc2e8f4f5d2381078c52f290ef3875358
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# XSS->Fix->Bypass: 10000$ bounty in Google Maps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-07_xss-fix-bypass-10000-bounty-in-google-maps.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `594c51ae4d1a5c351f51779a95de8572ba63dc792a84d93e9b826784f5cca274`
- Text SHA256: `2b85b064354d27bb544b4550983f1a7cc2e8f4f5d2381078c52f290ef3875358`


## Content

---
title: "XSS->Fix->Bypass: 10000$ bounty in Google Maps"
url: "https://www.ehpus.com/post/xss-fix-bypass-10000-bounty-in-google-maps"
final_url: "https://www.ehpus.com/post/xss-fix-bypass-10000-bounty-in-google-maps"
authors: ["Zohar Shachar"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "10,000"
publication_date: "2020-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4273
---

# XSS->Fix->Bypass: 10000$ bounty in Google Maps

  * zohar shachar
  * Sep 7, 2020
  * 3 min read

Ah, this moment of thrill every Google bug hunter knows, when you see a new ‘buganizer’ email landing in your inbox. Did they accept my new bug submission? Or perhaps the panel decided on a bounty amount for the previous one? Or maybe [_a new awesome grant_](https://security.googleblog.com/2020/04/research-grants-to-support-google-vrp_20.html)?

But then, you open the mail and see the demoralizing ‘fixed’ status updated. I mean, yeah, sure, it’s great that bugs are fixed, and security gaps are closed. But if we're being totally honest, this ‘fixed’ status is sort of ‘the end of the road’, the ‘final nail in the coffin’ for the particular research, and in many cases it’s hard and sad to let your precious bug go.

  

Well, scratch that! It was about a year ago when I was traveling for work, when I was sitting in the hotel room in a foreign country with nothing to do and nowhere to go and a new ‘fixed’ status update landed in my mailbox, regarding an XSS I found in Google Maps. Something in the boredom of this particular moment led me to overcome my initial mindset of ‘this is Google, they know how to fix an XSS’, and actually try and validate the fix. Within 10 minutes of that, I had a bypass in hand, and a few days later a double bounty in my account. [_Yalla_](https://www.urbandictionary.com/define.php?term=yalla) , to the bug! 

  

**Google Maps ‘export as KML’**

One of the many features offered by Google Maps is creating your own map. You can play with this feature by going [_here_](https://www.google.com/maps/d/). Once you're done building your map you can export it in several formats, one of which is [_KML_](https://developers.google.com/kml) (An ‘XML-Like’ file format with few extra features). Let’s create a sample map named ‘blabla<script>alert(1)</script>’, export it as ‘KML’ and review the server’s response:

[![](https://static.wixstatic.com/media/5527e6_dcbb75c6a8964eeda9c8054345bc0f65~mv2.png/v1/fill/w_49,h_19,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_dcbb75c6a8964eeda9c8054345bc0f65~mv2.png)](https://static.wixstatic.com/media/5527e6_dcbb75c6a8964eeda9c8054345bc0f65~mv2.png)

Interesting! We can see we receive an XML response (with some KML tags inside), and that our map name (probably as it contains special chars such as ‘<’) is contained within a [_CDATA_](https://en.wikipedia.org/wiki/CDATA) tag, which means our code will not be rendered by the browser. But wait. How do you ‘close’ a CDATA tag?

  

**First XSS: Escape CDATA for SVG payload**

I found that by adding special chars, you can ‘close’ the CDATA tag. Specifically, by adding ‘]]>’ at the beginning of your payload (I.e. as the beginning of the ‘map name’), you can escape from the CDATA and add arbitrary XML content (which will be rendered as XML) - leading immediately to XSS (for example with a simple [_SVG XSS_](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#user-content-xss-in-svg) payload). Here is the complete reproducing steps I send to Google (note: there is a missing ‘>’ in my description in step 3, which I corrected in a second email):

[![](https://static.wixstatic.com/media/5527e6_62da2116329840f98b6abeff2011a6ee~mv2.png/v1/fill/w_49,h_15,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_62da2116329840f98b6abeff2011a6ee~mv2.png)](https://static.wixstatic.com/media/5527e6_62da2116329840f98b6abeff2011a6ee~mv2.png)

Unfortunately I do not have an image of the result.. so you’d just have to trust me that at the time (prior to the fix), the above led to XSS.

Shortly after the submission, I received my ‘Nice catch’ from Google, and shortly after that - a 5000$ bounty.

[![](https://static.wixstatic.com/media/5527e6_e460d17449a149569ee49b2e0cd1308d~mv2.png/v1/fill/w_49,h_10,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_e460d17449a149569ee49b2e0cd1308d~mv2.png)](https://static.wixstatic.com/media/5527e6_e460d17449a149569ee49b2e0cd1308d~mv2.png)

**Second XSS: Bypass fix and Escape CDATA again**

So, as mentioned above I was sitting in some hotel room when this landed in my mailbox:

[![](https://static.wixstatic.com/media/5527e6_bf32d2aa25de46188eb356a2c5c1048e~mv2.png/v1/fill/w_49,h_8,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_bf32d2aa25de46188eb356a2c5c1048e~mv2.png)](https://static.wixstatic.com/media/5527e6_bf32d2aa25de46188eb356a2c5c1048e~mv2.png)

I wanted to see what was done. I launched up Google maps again, entered the same payload as before, and checked the response. What I saw was... Confusing. From what I could see, what was done in order to meet the closing of the CDATA tag was simply to add another CDATA tag:

  * ‘**< script>**’ will become ‘**<![CDATA[<script>]]>**’ (just like before) 

  * ‘**]] ><script>**’ will become ‘**<![CDATA[<![CDATA[<script>]]>]]>**’

Guess you see where this is going. Two ‘CDATA’ open tags? No problem, just used two ‘CDATA’ closing tags!

![](https://static.wixstatic.com/media/5527e6_ee6e056d100b4cd7b7e062b10e9f3d53~mv2.png/v1/fill/w_49,h_14,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_ee6e056d100b4cd7b7e062b10e9f3d53~mv2.png)

I was genuinely surprised the bypass was so simple. I reported it so quickly (literally 10 minutes between checking my mailbox and reporting a bypass), that right after sending this mail I started doubting myself. I was sure I missed something (maybe some other fix I didn’t notice, maybe some obvious reason why this doesn't work), I just couldn’t figure it out.

  

But I didn’t have much time for self doubt. Less than two hours after my bypass email my was sent a reassuring response arrived:

[![](https://static.wixstatic.com/media/5527e6_a77659a88e2a439fb05be4f6a84de9c3~mv2.png/v1/fill/w_49,h_17,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_a77659a88e2a439fb05be4f6a84de9c3~mv2.png)](https://static.wixstatic.com/media/5527e6_a77659a88e2a439fb05be4f6a84de9c3~mv2.png)

Few days later, I was rewarded another 5000$ bounty. Sweet :)

  

**Final thoughts**

Just a few weeks ago, I was able to re-exploit my [_SMTP Injection bug_](https://www.ehpus.com/post/smtp-injection-in-gsuite) after it was marked as fixed and I doubled my bounty there as well.

Ever since this Google-maps fix bypass incident I started to always re-validate fixes, even for simple things, and it has been paying off. I full heartedly encourage you to do the same. 

****

Timeline:

  * 04/23/2019 XSS reported to Google.

  * 04/27/2019 bug accepted ('nice catch!').

  * 05/07/2019 reward (5000$) issued.

  * 06/07/2019 Issue reported as fixed. 

  * 06/07/2019 Fix bypass reported.

  * 06/07/2019 Bypass confirmed, issue reopened.

  * 06/18/2019 second reward (5000$) issued.

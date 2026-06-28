---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-15_is-mime-sniffing-xss-a-real-thing-the-story-of-weird-google-bug-bounties.md
original_filename: 2019-05-15_is-mime-sniffing-xss-a-real-thing-the-story-of-weird-google-bug-bounties.md
title: Is MIME Sniffing XSS a real thing? [The story of weird Google bug bounties]
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
raw_sha256: d6386c11bd6fd8ed15fec5c51bea3f787c2f3f6e79d83fed612fbaf45c05af76
text_sha256: 540fee84813824ede8bdce39550f1d542da83e96a5049c088c731b3ca6e10110
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Is MIME Sniffing XSS a real thing? [The story of weird Google bug bounties]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-15_is-mime-sniffing-xss-a-real-thing-the-story-of-weird-google-bug-bounties.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `d6386c11bd6fd8ed15fec5c51bea3f787c2f3f6e79d83fed612fbaf45c05af76`
- Text SHA256: `540fee84813824ede8bdce39550f1d542da83e96a5049c088c731b3ca6e10110`


## Content

---
title: "Is MIME Sniffing XSS a real thing? [The story of weird Google bug bounties]"
page_title: "Exploring MIME Sniffing XSS: A Tale of Google Bug Bounties"
url: "https://www.komodosec.com/post/mime-sniffing-xss"
final_url: "https://www.komodosec.com/post/mime-sniffing-xss"
authors: ["Komodo Security"]
programs: ["Google"]
bugs: ["Stored XSS", "MIME sniffing"]
publication_date: "2019-05-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5263
---

# Is MIME Sniffing XSS a real thing? [The story of weird Google bug bounties]

  * Komodo Research
  * May 15, 2019
  * 5 min read

Updated: Sep 23, 2025

![Is MIME Sniffing XSS a real thing](https://static.wixstatic.com/media/d383fe_3af6fa57f48b4d92860859c876ac8051~mv2.jpg/v1/fill/w_144,h_75,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d383fe_3af6fa57f48b4d92860859c876ac8051~mv2.jpg)

  

Let’s start at the end. This one got me seriously confused. It all started a few months ago when a colleague was hacking away at some Google website. After some poking around, he detected a persistent XSS vulnerability – the attacker’s payload is stored on the server side and returned to the user without encoding. There was only one catch – The Content-Type of the server response was set to ‘multipart/form-data’ meaning that the browser will not evaluate the HTML and will not execute the JavaScript. 

  

\- _“I Think I’ll report it,”_ my colleague said, “ _Maybe it can be exploited with mime-sniffing._ ”

\- _“Good luck,”_ I responded, with a mocking tone. _“You know as well as I that mime-sniffing is dead”_.

\- _“we’ll see”_ , he said _“I have nothing to loss by reporting”_

  

Soon after my Colleague was rewarded by Google with few thousand dollars for this issue. Within few days he detected yet another instance of mime-sniffing-dependent-XSS, and was rewarded with few thousand dollars more. 

  

\- _“What the hell?”_ I asked him. 

\- _“I’m not sure myself”,_ he replied, “ _But if they pay me the bounties I’m not arguing. Besides, maybe they know something we don’t._ ” 

  

This raised a question in my mind: what is mime sniffing and how do mime sniffing vulnerabilities play a role in XSS exploits?

  

OK, I thought, homework time!

  

**MIME sniffing in a nut shell**

Generally speaking, browsers look at the Content-Type header in the HTTP response for an indication of how the response should be interpreted. Typically, if the application wants the browser to render HTML content, the HTTP response should include the ‘text/html’ content-type. Similarly, ‘image/jpeg’ content-type should be used for images, etc. 

‘Typically’ is the crucial word in that sentence, as different browsers tend to have different approaches for evaluating content-types especially when unknown content-types are used (‘unknown’ in the sense that the specific browser does not have clear instructions on how to evaluate it). In such a case, the browser may try to perform mime-sniffing, i.e. try to ‘understand’ from the content itself how it should be interpreted. 

  

Such mime sniffing vulnerabilities can allow attackers to execute unexpected code or scripts, making it an important consideration even in modern browsers.

  

In the context of XSS, if the content ‘resembles’ HTML, the browser _might_ understand it as HTML even if the content-type is not set to ‘text/html’. Understanding what is mime type sniffing is key to grasping why certain XSS issues only trigger under specific conditions, especially with content types like ‘multipart/form-data’ or unknown MIME types.

  

Confused? You’re not alone.

  

When exactly will the browser attempt such a ‘self-understanding’ approach? It depends on the browser, of course, but generally it’s quite a rare thing and mostly applicable to old browsers ([How old? IE 4 old](http://www.h-online.com/security/features/Risky-MIME-sniffing-in-Internet-Explorer-746229.html)). To make the attack even less plausible, a specific header (‘X-Content-Type-Options: nosniff’) can be set by the server to indicate to the browser that it _should not_ perform mime-sniffing. This capability has been supported by most major browsers ([with the exception of Safari](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options)) for quite some time ([even in IE 8](https://blogs.msdn.microsoft.com/ie/2008/09/02/ie8-security-part-vi-beta-2-update/)). 

  

**Missing ‘XCTO header’? Nope**

Back to the XSS in Google. My colleague considered his mime-sniffing XSS to be a ‘slightly more real’ XSS (i.e. has chances to be exploited in the real world), as the server response he received lacked the ‘X-Content-Type-Options: nosniff’ header, which means that the browser _might_ perform MIME-Sniffing in some cases. 

  

Without proper headers, mime confusion attacks exploit the browser’s attempt at mime type sniffing, demonstrating that even minor oversights can create exploitable mime sniffing vulnerabilities.

  

While I was not entirely convinced (neither of us were able to create a POC that actually works), I could sort-of accept that Google holds itself to the highest security posture, thus accepting the lack of header as an issue. That is until I found my own XSS. 

  

**The most confusing Google response of all time**

  

A few weeks later, I found my own instance of persistent XSS with non-HTML content type. In my case, the ‘X-Content-Type-Options: nosniff’ _was_ set. Nonetheless, not wanting to miss out on all this bounty goodness, I submitted it as a bug. This triggered the most confusing Google response I could think of.

Originally, the bug was rejected, as I could not provide a POC. This was the result I expected. Later, though, this happened: 

  

[![The most confusing Google response of all time](https://static.wixstatic.com/media/3184af_5a07ce9bb15943b087d2eaeb64b26a19~mv2.png/v1/fill/w_49,h_27,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3184af_5a07ce9bb15943b087d2eaeb64b26a19~mv2.png)](https://static.wixstatic.com/media/3184af_5a07ce9bb15943b087d2eaeb64b26a19~mv2.png)

  

Without any new data from me, Google switched from ‘intended behavior,’ to ‘new,’ to ‘accepted’ just to realize a week later that they were already following this as a bug. 

Apparently, I’m not the only one to be confused about mime-sniffing. I decided to tackle the issue once and for all and asked Google about it. That was **very** helpful: 

  

[![mime sniffing xss](https://static.wixstatic.com/media/3184af_6b0f6c0f5f1a44e197a989a57c63c3b5~mv2.png/v1/fill/w_49,h_27,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3184af_6b0f6c0f5f1a44e197a989a57c63c3b5~mv2.png)](https://static.wixstatic.com/media/3184af_6b0f6c0f5f1a44e197a989a57c63c3b5~mv2.png)

Problem solved indeed. 

  

At this point I felt that more data is needed (and let’s be honest, more bounties too). So, I decided to invest some time in detecting more such instances and in reporting everything I find. 

  

**Bounties, bounties, bounties**

In the following months I’ve detected and reported several more instances, each with slightly different characteristics, including a ‘ZIP’ document response (content-disposition set to ‘attachment’), ‘plain/text’ content type, ‘CSV’ content type, and even ‘Custom’ content-type. Without fail, all of the bugs I’ve reported were accepted (expect those deemed as duplicates), though several required some ‘convincing’: 

  

  

[![mime sniffing xss](https://static.wixstatic.com/media/3184af_b2e4ca06b90a4dbabd984496c40d95d8~mv2.png/v1/fill/w_88,h_52,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3184af_b2e4ca06b90a4dbabd984496c40d95d8~mv2.png)](https://static.wixstatic.com/media/3184af_b2e4ca06b90a4dbabd984496c40d95d8~mv2.png)

  

Ah ha! ‘Weird stuff!’ That explains everything. I can now use Google tricks against them:

  

  

[![mime sniffing](https://static.wixstatic.com/media/3184af_8b71ab4281a84f54bad74d41c6a33dab~mv2.png/v1/fill/w_49,h_36,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3184af_8b71ab4281a84f54bad74d41c6a33dab~mv2.png)](https://static.wixstatic.com/media/3184af_8b71ab4281a84f54bad74d41c6a33dab~mv2.png)

After that last email, the bug was accepted (and I was rewarded).

  

**Final thoughts**

Personally, my thoughts after this research remained similar to those I had before – while I accept that it is a theoretical risk, an XSS that requires mime-sniffing just doesn’t cut it for me. And I’m not alone – as shown above, at least some Google security engineers don’t really see the risk either. 

  

With that being said, studying what is mime sniffing, mime sniffing vulnerabilities, and mime confusion attacks provides valuable insights into securing applications against subtle XSS threats.

  

With that being said, I have huge respect for Google here for making the decision to treat such XSS as a real risk. Their decision to put their users’ security as first priority and fighting such esoteric vulnerabilities (even at the cost of paying good bounty money) can only be appreciated and I wish other organizations of such caliber would take security half as seriously as Google does. 

  

Founded by leading consulting experts with decades of experience, the KomodoSec team includes seasoned security specialists with worldwide information security experience and military intelligence experts. We deliver regulator-grade, intelligence-led red team tests on live production that cover critical or important functions, include key third parties, follow the EU TLPT RTS and TIBER-EU guidance end-to-end, and produce the exact artifacts supervisors expect for validation and attestation.

  * [Application Security](https://www.komodosec.com/blog/categories/application-security)
  * [Bug-Bounty](https://www.komodosec.com/blog/categories/bug-bounty)

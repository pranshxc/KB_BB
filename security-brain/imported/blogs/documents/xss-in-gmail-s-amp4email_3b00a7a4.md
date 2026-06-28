---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-02_xss-in-gmails-amp4email.md
original_filename: 2022-08-02_xss-in-gmails-amp4email.md
title: XSS in Gmail's Amp4Email
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
raw_sha256: 3b00a7a45d52dbd7b714a840e3e2a7c81dad9663f0107b60e904a3bfb5f8cc8f
text_sha256: 7eaf220d6fd1aa39ed814ce3a14f69bf68e28a32c66350da779925752b20ea53
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Gmail's Amp4Email

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-02_xss-in-gmails-amp4email.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `3b00a7a45d52dbd7b714a840e3e2a7c81dad9663f0107b60e904a3bfb5f8cc8f`
- Text SHA256: `7eaf220d6fd1aa39ed814ce3a14f69bf68e28a32c66350da779925752b20ea53`


## Content

---
title: "XSS in Gmail's Amp4Email"
url: "https://www.adico.me/post/xss-in-gmail-s-amp4email"
final_url: "https://www.adico.me/post/xss-in-gmail-s-amp4email"
authors: ["Adi 'Adico' Cohen (@wir3less2)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "5,000"
publication_date: "2022-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2369
---

# XSS in Gmail's Amp4Email

  * Adi "Adico" Cohen
  * Aug 2, 2022
  * 5 min read

### Background

  

AMP is most commonly used as a framework to develop fast-loading content on the web.

One of AMP's projects, AMP4Email has been adopted in recent years by many of the leading mail services as a way to provide Dynamic Emails (essentially a subset of regular HTML with a few default components to handle things like layouts, templates, forms, and such).

  

When I first heard about this feature a few years ago, my initial reaction (like many of you I’m sure) was “This can’t be secured! How did they prevent XSS?” and Boy was I wrong!

  

Gmail has a great setup where you could easily write and validate your AMP Emails through their Playground website. And even send it to your mailbox to see how it renders in Gmail, Perfect for security research :)

  

After spending a few days playing around in that sandbox I had about 5 different vectors that resulted in either broken HTML (that could potentially be exploited with some extra work) or just complete XSS vectors. Sounds pretty easy right? Or so I thought.

  

When I attempted to send any of those vectors to Gmail, I quickly discovered there’s either a second filter in play, or a completely different version of AMP with additional security validations.

  

In this post, I’ll walk through how I managed to get one of those initial vectors to bypass that extra layer and arrive at my inbox.

  

![](https://static.wixstatic.com/media/d12c69_80b85b3b23fa4ab0945e0f6242e12228~mv2.jpg/v1/fill/w_147,h_43,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_80b85b3b23fa4ab0945e0f6242e12228~mv2.jpg)

![](https://static.wixstatic.com/media/d12c69_b988e0c6f18f488a9313d02fef236667~mv2.jpg/v1/fill/w_115,h_20,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_b988e0c6f18f488a9313d02fef236667~mv2.jpg)

  

### Methodology

  

I found out over the years that the easiest way to circumvent an XSS filter is by tricking it into a different rendering context than what the browser will actually use to render a given piece of code.

For this to work, I need to be able to write a payload that contains more than one rendering context. Plain HTML is given as the first context. But additional ones can be achieved through many means (Templates, SVG, Math, CSS, etc…)

  

In the scope of AMP4Email however, most of those are forbidden and one of my only real options is Stylesheets, so I’ve decided to focus my research around that.

  

### Initial Vector

  

For my attack to work, I needed to find a discrepancy between how the filter renders a stylesheet and how the browser does. 

  

This means either tricking the filter into believing a _fake style tag_ (either opening or closing) is real and should be treated as such, when in reality the browser will ignore it. Or the exact opposite, treat a real tag as being fake and ignore it.

  

As I mentioned above, I already had a vector that successfully triggered an XSS in the AMP playground but was not able to bypass Gmail’s filter. 

  

Here it is:

  

  
  
  <style amp-custom>body{color:red}</styleX>
  <meta name="</style><img src='x'onerror=alert(1)">

  

The reason this vector works is that AMP is being slightly too _greedy_ , and leaves the CSS context as soon as it encounters the string “</style” even if it doesn’t have a closing bracket “>” or at least a whitespace after it.

I assume this was in place to mitigate other attacks. But I was able to use this to trick the filter into believing we’re back in HTML context, while the browser obviously ignores </styleX> entirely and stays well within the realm of CSS.

  

Next, I take advantage of this rendering context mismatch to position the XSS in a way that looks safe to the filter. I chose the name attribute of a <meta> tag but any safe attribute would work here.

But when the browser (which still renders CSS at this point) encounters this tag, it counts it as malformed CSS, terminates the stylesheet at the real </style> tag and renders the <img> tag with its onerror attribute, triggering the XSS.

If you try sending this payload to Gmail however, the entire document fails to load. (which is what happens when the filter encounters a significant validation error)

  

### Some (More) Research

  

At this point, I thought I could still sneak this payload by Gmail and to start off, I tried sending a few “harmless” payloads to get a sense of what restrictions are in place before I try anything too malicious.

  

This included tests such as:

  

  
  
  <style>div{font-family:'aa/*f<br> ff*/'}</style>
  <style>div{font-family:'aa/*f</xxx> ff*/'}</style>
  <style>div{font-family:'aa/*f</style> ff*/'}</style>

  

I quickly found out that while AMP allows any value to be present inside this string-comment hybrid, Gmail does not. 

  

Everything worked well with the first two payloads, they arrived at my inbox with only a minor change, they were **escaped**.

  

  
  
  <style>div{font-family:'aa/*f</xxx> ff*/'}</style> 

Transformed into 
  
  
  <style>div{font-family:'aa/*f\00003c/xxx\00003e ff*/'}</style>

  

And since I can't terminate a tag without HTML entities(‘<’ , ‘>’) What looked like a promising vector in AMP, seemed way less interesting after Gmail ran its magic on it.

  

I spent some more time trying to put HTML entities in different locations of the CSS statement until I reached the holy grail, which is non-other than my beloved CSS Selector!

  

If we send the following payload to Gmail

  

  
  
  <style amp-custom>[id='a<br>aa'],body{font-family:'aaaa'}</style>  

  

we get back the exact same thing, no escaping or other mutations take place

  

![](https://static.wixstatic.com/media/d12c69_b00c6fcb17094dfab257d96f523c2dc0~mv2.png/v1/fill/w_86,h_4,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_b00c6fcb17094dfab257d96f523c2dc0~mv2.png)

  

Great, I thought, so all I need now is to copy in my </styleX><meta…> payload and be done, right?

  

I wrote it down in the AMP playground editor only to immediately receive an error.

![](https://static.wixstatic.com/media/d12c69_23a2c0330e9e4446a66286e3a923033b~mv2.png/v1/fill/w_49,h_5,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_23a2c0330e9e4446a66286e3a923033b~mv2.png)

  

Damn, so I can’t “fake” closing the tag in the middle of a selector because AMP detects it as malformed CSS. 

  

At this point, I still thought I could jiggle the payload a little and make it work so I tried to find the cutoff of where AMP errors out.

And just as expected, it happens after encountering “</style” 

  

I decided to delete the “e” and send “</styl>” to see how Gmail handles this case.

And this might not surprise you at this point, but Gmail did not appreciate my attempt

![](https://static.wixstatic.com/media/d12c69_718253bd61ff4e1388eeb026349e387a~mv2.png/v1/fill/w_66,h_4,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_718253bd61ff4e1388eeb026349e387a~mv2.png)

  

So now I know that Gmail has an even stricter filter and just deletes the payload as soon as anything resembling a closing </style> tag is encountered. Great. Thanks Google.

  

### The Payload

  

Before I completely gave up on this direction, I had one last idea left I wanted to try.

Since every other CSS Context encoded my HTML Entities besides Selectors, what would happen if I send an Encoded Selector to Gmail? Will it get decoded for me?

  

I started out again with the safest payload I could come up with, just to ensure that If it does get filtered it will be because of the encoding and nothing else.

  

So I sent the following snippet: 
  
  
  <style amp-custom>[id='a<b\000072> aa'],body{font-family:'aaaa'}</style>

And Yes! It worked! Gmail actually decoded the \000072 into the letter ‘r’

  

![](https://static.wixstatic.com/media/d12c69_4e696f1cb40a43e6bceea2bd028c0982~mv2.png/v1/fill/w_59,h_4,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_4e696f1cb40a43e6bceea2bd028c0982~mv2.png)

  

Now for the real test. Can I use this to inject a closing style tag? 

  

  
  
  <style amp-custom>[id='a</st\000079le> aa'],body{font-family:'aaaa'}</style>

  

Comes out as:

![](https://static.wixstatic.com/media/d12c69_6037df547fa64884801a68d1f58273a3~mv2.png/v1/fill/w_46,h_5,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_6037df547fa64884801a68d1f58273a3~mv2.png)

  

I sure can!

  

At this point I could completely ditch the <meta> tag, it’s not needed because AMP rightfully doesn’t treat </st\000079le> as anything it should worry about. And this only mutates to a usable payload after Gmail’s extra filter is executed.

  

To tie everything together, I came up with the following final payload that injects an <img> tag, but at this point, any HTML could be used:

  

  
  
  <style amp-custom>[id='</st\000079le></head><body>
  <img src=https://bla.com/xx.jpg onerror=a=1>']{color:blue}</style>

  

I could immediately see this worked when I opened the email and noticed the broken image.

  

![](https://static.wixstatic.com/media/d12c69_d18a592f0d6147e18ddb05ac650a8ba4~mv2.png/v1/fill/w_49,h_14,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_d18a592f0d6147e18ddb05ac650a8ba4~mv2.png)

  

Looking closer at the dev-tools confirmed it

  

![](https://static.wixstatic.com/media/d12c69_d2fedac98883428ea46ee09a58c0ce17~mv2.png/v1/fill/w_54,h_15,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/d12c69_d2fedac98883428ea46ee09a58c0ce17~mv2.png)

  

A new XSS was born

Only to then quickly died because I reported this to Google :)

  

####  Timeline

  * Mar 27th 2021 - Reported issue to Google

  * Apr 1st 2021 - “Nice Catch” response from Google 

  * Apr 13th 2021 - Awarded a bounty of 5000$ 

  * Jul 7th 2022 - Notice the issue was fixed (in reality this was fixed way quicker, there was just an issue with the notice)

  * Jul 9th 2022 - Blog post published

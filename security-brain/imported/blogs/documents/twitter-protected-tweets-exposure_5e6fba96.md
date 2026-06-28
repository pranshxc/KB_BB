---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-19_twitter-protected-tweets-exposure.md
original_filename: 2019-04-19_twitter-protected-tweets-exposure.md
title: Twitter - protected tweets exposure
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 5e6fba969c8c4b04b832d3e8c47d7e8e9f7a2acdb8836f5106c94523ea7c1bf2
text_sha256: 1b09de5dcc06c42cf0ae7c4758853c21649106841825e7973b8e1b4e4d9c836e
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Twitter - protected tweets exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-19_twitter-protected-tweets-exposure.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `5e6fba969c8c4b04b832d3e8c47d7e8e9f7a2acdb8836f5106c94523ea7c1bf2`
- Text SHA256: `1b09de5dcc06c42cf0ae7c4758853c21649106841825e7973b8e1b4e4d9c836e`


## Content

---
title: "Twitter - protected tweets exposure"
page_title: "Twitter - protected tweets exposure - HackMD"
url: "https://terjanq.github.io/Bug-Bounty/Twitter/protected-tweets-exposure-efvju8i785y1/"
final_url: "https://terjanq.github.io/Bug-Bounty/Twitter/protected-tweets-exposure-efvju8i785y1/"
authors: ["Terjanq (@terjanq)"]
programs: ["Twitter"]
bugs: ["Information disclosure"]
bounty: "560"
publication_date: "2019-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5300
---

# Twitter - protected tweets exposure

## Summary

Leaking sensitive information from protected tweets via a prepared website. This vulnerability could lead to exposure of information such as **credit card numbers** , **bank account numbers** , **phone numbers** , **tokens** , **specific words** or even the **whole phrases** but also the exposure of any additional information such as **mentioned users** , **tweet time frames** , **tweet locations** or **hashtags**.

## Description

When searching for further **URL exposure** vulnerabilities on Twitter I noticed that a very unsafe URL redirect happens, depending on search results, when a user searches for some tweets.

The endpoint I found is that:

> If there are no search results for a query e.g. [https://twitter.com/search?q=veryveryunsaferedirect&src=typd](https://twitter.com/search?q=veryveryunsaferedirect&src=typd) the URL changes to [https://twitter.com/search?f=tweets&q=secret from%3Aterjanq&src=typd](https://twitter.com/search?f=tweets&q=secret%20from%3Aterjanq&src=typd) and it doesn’t when results were found. As can be spotted, the `f=tweets` parameter was added and hence that state can be leaked.

The detection of the URL change can be achieved in several ways, I will use the technique I already reported to Twitter in <https://hackerone.com/reports/491243> and also described in <https://terjanq.github.io/Bug-Bounty/Twitter/url-information-disclosure-q67svgtbqarv/index.html>.

Thanks to _Advanced Search_ option the attacker can obtain very detailed information about the victim’s tweets when knowing their username even if the tweets are set as private. The full list of available options is as in the image below.  
![](https://i.imgur.com/xJeaixk.png)

To make the _X-Search_ attack more effective, the attacker can use logical operators `AND` and `OR` to narrow down the search area. For example, by using phrases like `1001 OR 1002 OR 1003 OR 1004 …` the attacker can use binary-search to extract all four-digit numbers in only few requests. However, I noticed that the limit for the number of words that can be used in the search is limited by 50. Nevertheless, that number is big enough to effectively extract those four-digit numbers – it would only take around 300 requests to extract all of them and then by combining them in the correct order the whole phrases such as credit card number can be leaked.

In the Proof of Concept, I have prepared an easy attack abusing this observation for three-digit ones.

## Steps To Reproduce:

  1. Prepare test twitter accounts and enable the option _Protect your Tweets_ in the settings.
  2. Visit the <https://terjanq.github.io/Bug-Bounty/Twitter/protected-tweets-exposure-efvju8i785y1/poc.html> and click the button to start the PoC.
  3. Put phrases you want to find in your tweets and fill the field `from:` with your account’s username and submit the form.
  4. When you are done with the previous step, click on the button `Fetch all 3-digit numbers from tweets` and wait for the timer to stop.
  5. You should see all the three-digit numbers from your tweets.

_Please note that the exploit can be coded much more efficiently. For example, instead of using one window to make the redirects several can be used to speed it up. Also due to the style it was written in, false-positives can appear when lags occur (it has primitive protection implemented for that case, but it’s not perfect)_

## Impact:

A regular user of Twitter can have their protected tweets leaked along with additional information such as **mentioned users** , **tweet time frames** , **tweet locations** etc.

## Supporting Material/References:

I made a short video demonstrating the PoC in action  
<https://youtu.be/bSUS4THqssY>  
![](//img.youtube.com/vi/bSUS4THqssY/hqdefault.jpg)__

__

  * Twitter - protected tweets exposure
  * Summary
  * Description
  * Steps To Reproduce:
  * Impact:
  * Supporting Material/References:

Expand allBack to topGo to bottom

  * Twitter - protected tweets exposure
  * Summary
  * Description
  * Steps To Reproduce:
  * Impact:
  * Supporting Material/References:

Expand allBack to topGo to bottom

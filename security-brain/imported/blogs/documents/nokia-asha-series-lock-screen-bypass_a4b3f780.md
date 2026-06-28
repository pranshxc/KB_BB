---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-01_nokia-asha-series-lock-screen-bypass.md
original_filename: 2017-06-01_nokia-asha-series-lock-screen-bypass.md
title: Nokia Asha Series Lock Screen Bypass
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: a4b3f7800616c0450fea12161626ebf565a3624dd7ad38aad39ec68a6d4b4b87
text_sha256: 470f95a53137f11e30518843bce130ba69d793a9db6d753ed36c366ff1e55a75
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Nokia Asha Series Lock Screen Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-01_nokia-asha-series-lock-screen-bypass.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a4b3f7800616c0450fea12161626ebf565a3624dd7ad38aad39ec68a6d4b4b87`
- Text SHA256: `470f95a53137f11e30518843bce130ba69d793a9db6d753ed36c366ff1e55a75`


## Content

---
title: "Nokia Asha Series Lock Screen Bypass"
page_title: "Nokia Asha Series Lock Screen Bypass - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2017/06/nokia-asha-series-lock-screen-bypass.html"
final_url: "https://www.rafaybaloch.com/2017/06/nokia-asha-series-lock-screen-bypass.html"
authors: ["Hammad Shamsi (@HammadShamsii)"]
programs: ["Nokia"]
bugs: ["Authentication bypass", "Lock screen bypass"]
publication_date: "2017-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6191
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjONRkIllaBCkIKr5aqh8bM4f6FhIQ8w0TKUmyc_GFCsTYuH7HBn2G8e5gU3JykeE_-o728QMkP7rLtdeAtn2-PyrEnCVFgZAvEvdo4XuBhb531UQ1rM4dmOvOl6uLD9C2zKgmrdR6ZAvQ/s1600/296216,xcitefun-nokia-asha-311-2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjONRkIllaBCkIKr5aqh8bM4f6FhIQ8w0TKUmyc_GFCsTYuH7HBn2G8e5gU3JykeE_-o728QMkP7rLtdeAtn2-PyrEnCVFgZAvEvdo4XuBhb531UQ1rM4dmOvOl6uLD9C2zKgmrdR6ZAvQ/s1600/296216,xcitefun-nokia-asha-311-2.jpg)

  
There have been a lot of lock screen bypasses lately in almost every mobile deice such as iPhone, Samsung galaxy, HTC etc and if you observe carefully most of them rely upon abusing the "**Emergency Calling** " option some how. **Hammad Shamsi** a Security researcher from RHAinfoSec has found a lockscreen bypass which resides in all the latest versions of Nokia Asha series. The bypass occurred due to mishandling of SOS button (Emergency Panic Button) which is present in all Nokia Asha Series and is used to perform the emergency calls.  

####  How to Reproduce?

Here are the steps to reproduce, in case you are curious:  
  
**i)** First, set up the lock code to lock the screen.  
**ii)** Next, type any number on the unlock screen.  
**iii)** Next, press the SOS button followed the green button and you are sent to recent call lists.  
  
This could be furthur abused into gaining complete phonebook access, add/delete a number, turning bluetooth on/off etc. **Hammad** , has created a series of three video which demonstrates how you could go about accomplishing it.  

####  Nokia Asha Lock Screen Bypass - Video #1

  
  

####  Nokia Asha Lock Screen Bypass - Video #2

  
  

####  Nokia Asha Lock Screen Bypass - Video #3

  
  

####  Reward

Hammad was awarded Nokia Lumia 1520, though mobile bugs are not a part of their bug bounty programs, however an exception was made while taking the impact of the bug in location.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrLOFjdWFydRBxlfU1YckEXk8C8ZTLPj0Gmxmsb-qzLB90BnyuivIZY6Tf8xlFXqwOe81_1n3yrDMnIZZR9Hu2slU-vyY3Pmz9dCR8_9_UhUPkwhfd5r0YRra6NZViF-6hFWIsBWJy_QU/s1600/10536599_10204654169533824_1587056244_n.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrLOFjdWFydRBxlfU1YckEXk8C8ZTLPj0Gmxmsb-qzLB90BnyuivIZY6Tf8xlFXqwOe81_1n3yrDMnIZZR9Hu2slU-vyY3Pmz9dCR8_9_UhUPkwhfd5r0YRra6NZViF-6hFWIsBWJy_QU/s1600/10536599_10204654169533824_1587056244_n.jpg)

  

I on behalf of all RHAinfoSec Team members would like to congratulate him and would like to wish him best of luck for future researches. 

####  Timeline

**25/04/14 -** The vulnerability was reported.  
**30/04/14 -** Initial response from Nokia notifying that they are working on a fix.  
**1/06/14 -** Nokia lumia was received.  
**7/07/14 -** The issue was fixed.  
**7/12/2014 -** Writeup was released.

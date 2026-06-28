---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-30_researching-polymorphic-images-for-xss-on-google-scholar.md
original_filename: 2020-04-30_researching-polymorphic-images-for-xss-on-google-scholar.md
title: Researching Polymorphic Images for XSS on Google Scholar
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- file-upload
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- file-upload
- api-security
- mobile-security
language: en
raw_sha256: b5fee7e848037c5930ef7d33a9fbeca2ff39fa65bc8604c768c948deb661b3fb
text_sha256: ef0fcfe9e6d27a7bbf0c878d4fa5777876b64d94a07903570593d5caa9cf1d98
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Researching Polymorphic Images for XSS on Google Scholar

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-30_researching-polymorphic-images-for-xss-on-google-scholar.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, file-upload, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b5fee7e848037c5930ef7d33a9fbeca2ff39fa65bc8604c768c948deb661b3fb`
- Text SHA256: `ef0fcfe9e6d27a7bbf0c878d4fa5777876b64d94a07903570593d5caa9cf1d98`


## Content

---
title: "Researching Polymorphic Images for XSS on Google Scholar"
page_title: "Researching Polymorphic Images for XSS on Google Scholar · Doyensec's Blog"
url: "https://blog.doyensec.com/2020/04/30/polymorphic-images-for-xss.html"
final_url: "https://blog.doyensec.com/2020/04/30/polymorphic-images-for-xss.html"
authors: ["Lorenzo Stella (@lorenzostella)"]
programs: ["Google"]
bugs: ["Stored XSS"]
bounty: "9,401.1"
publication_date: "2020-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4620
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Researching Polymorphic Images for XSS on Google Scholar

30 Apr 2020 - Posted by Lorenzo Stella

A few months ago I came across a curious design pattern on [Google Scholar](https://scholar.google.com/). Multiple screens of the web application were fetched and rendered using a combination of `location.hash` parameters and XHR to retrieve the supposed templating snippets from a relative URI, rendering them on the page unescaped.

![Google Scholar's design pattern](../../../public/images/scholar-issue.png)

This is not dangerous per se, unless the platform lets users upload arbitrary content and serve it from the same origin, which unfortunately Google Scholar does, given its image upload functionality.

While any penetration tester worth her salt would deem the exploitation of the issue trivial, Scholar’s image processing backend was applying different transformations to the uploaded images (i.e. stripping metadata and reprocessing the picture). When reporting the vulnerability, Google’s VRP team did not consider the upload of a polymorphic image carrying a valid XSS payload possible, and instead requested a PoC||GTFO.

Given the age of this technique, I first went through all past “well-known” techniques to generate polymorphic pictures, and then developed a test suite to investigate the behavior of some of the most popular libraries for image processing (i.e. Imagemagick, GraphicsMagick, Libvips). This effort led to the discovery of some interesting caveats. Some of these methods can also be used to conceal web shells or Javascript content to [bypass “self” CSP directives](https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs).

### Payload in EXIF

The easiest approach is to embed our payload in the metadata of the image. In the case of JPEG/JFIF, these pieces of metadata are stored in application-specific markers (called `APPX`), but they are not taken into account by the majority of image libraries. [Exiftool](https://exiftool.org/) is a popular tool to edit those entries, but you may find that in some cases the characters will get entity-escaped, so I resorted to inserting them manually. In the hope of Google’s Scholar preserving some whitelisted EXIFs, I created an image having 1.2k common EXIF tags, including [CIPA](http://www.cipa.jp/std/std-sec_e.html) standard and non-standard tags.

![JPG having the plain XSS alert\(\) payload in every common metadata field](../../../public/images/payload_in_all_known_metadata.jpg) ![PNG having the plain XSS alert\(\) payload in every common metadata field](../../../public/images/payload_in_all_known_metadata.png)

While that didn’t work in my case, some of the EXIF entries are to this day kept in many popular web platforms. In most of the image libraries tested, PNG metadata is always kept when converting from PNG to PNG, while they are always lost from PNG to JPG.

### Payload concatenated at the end of the image (after 0xFFD9 for JPGs or IEND for PNGs)

This technique will only work if no transformations are performed on the uploaded image, since only the image content is processed.

![JPG having the plain XSS alert\(\) payload after the trailing 0xFFD9 chunk](../../../public/images/payload_in_trailer.jpg) ![PNG having the plain XSS alert\(\) payload after the trailing IEND chunk](../../../public/images/payload_in_trailer.png)

As the name suggests, the trick involves appending the JavaScript payload at the end of the image format.

### Payload in PNG’s iDAT

In PNGs, the iDAT chunk stores the pixel information. Depending on the transformations applied, you may be able to directly insert your raw payload in the iDAT chunks or you may [try to bypass](https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/) the resize and re-sampling operations. Google’s Scholar only generated JPG pictures so I could not leverage this technique.

### Payload in JPG’s ECS

In the JFIF standard, the entropy-coded data segment (ECS) contains the output of the raw Huffman-compressed bitstream which represents the Minimum Coded Unit (MCU) that comprises the image data. In theory, it is possible to position our payload in this segment, but there are no guarantees that our payload will survive the transformation applied by the image library on the server. Creating a JPG image resistant to the transformations caused by the library was a process of trial and error.

As a starting point I crafted a “base” image with the same quality factors as the images resulting from the conversion. For this I ended up using [this image](https://github.com/ianare/exif-samples/blob/master/jpg/tests/67-0_length_string.jpg) having 0-length-string EXIFs. Even though having the payload positioned at a variable offset from the beginning of the section did not work, I found that when processed by Google Scholar the first bytes of the image’s ECS section were kept if separated by a pattern of `0x00` and `0x14` bytes.

![Hexadecimal view of the JFIF structure, with the payload visible in the ECS section](../../../public/images/ecs-xss-hex-view.png)

From here it took me a little time to find the right sequence of bytes allowing the payload to survive the transformation, since the majority of user agents were not tolerating low-value bytes in the script tag definition of the page. For anyone interested, we have made available the images embedding the [onclick](/public/images/onclick-xss-ecs.jpeg) and [mouseover](/public/images/mouseover-xss-ecs.jpeg) events. Our image library test suite is available on Github as [doyensec/StandardizedImageProcessingTest](https://github.com/doyensec/StandardizedImageProcessingTest).

![Exploitation result of the XSS PoC on Scholar](../../../public/images/scholar-xss-poc-proof.png)

## Timeline

  * **[2019-09-28]** _Reported to Google VRP_
  * **[2019-09-30]** _Google’s VRP requested a PoC_
  * **[2019-10-04]** _Provided PoC #1_
  * **[2019-10-10]** _Google’s VRP requested a different payload for PoC_
  * **[2019-10-11]** _Provided PoC #2_
  * **[2019-11-05]** _Google’s VRP confirmed the issue in 2 endpoints, rewarded $6267.40_
  * **[2019-11-19]** _Google’s VRP found another XSS using the same technique, rewarded an additional $3133.70_

### Other relevant posts:

  * ###  [ Windows Installer, Exploiting Custom Actions 18 Jul 2024 ](/2024/07/18/custom-actions.html)

  * ###  [ Office Documents Poisoning in SHVE 03 Nov 2023 ](/2023/11/03/Office-Document-Poisoning.html)

  * ###  [ Client-side JavaScript Instrumentation 25 Sep 2023 ](/2023/09/25/clientside-javascript-instrumentation.html)

  * ###  [ Introducing Session Hijacking Visual Exploitation (SHVE): An Innovative Open-Source Tool for XSS Exploitation 31 Aug 2023 ](/2023/08/31/introducing-session-hijacking-visual-exploitation.html)

  * ###  [ Windows Installer EOP (CVE-2023-21800) 21 Mar 2023 ](/2023/03/21/windows-installer.html)

  * ###  [ SSRF Cross Protocol Redirect Bypass 16 Mar 2023 ](/2023/03/16/ssrf-remediation-bypass.html)

  * ###  [ A New Vector For “Dirty” Arbitrary File Write to RCE 28 Feb 2023 ](/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)

  * ###  [ ImageMagick Security Policy Evaluator 10 Jan 2023 ](/2023/01/10/imagemagick-security-policy-evaluator.html)

  * ###  [ Let's speak AJP 15 Nov 2022 ](/2022/11/15/learning-ajp.html)

  * ###  [ Diving Into Electron Web API Permissions 27 Sep 2022 ](/2022/09/27/electron-api-default-permissions.html)

  * ###  [ Regexploit: DoS-able Regular Expressions 11 Mar 2021 ](/2021/03/11/regexploit.html)

  * ###  [ One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse 22 Aug 2019 ](/2019/08/22/modern-password-managers-flag-secure.html)

  * ###  [ Jackson gadgets - Anatomy of a vulnerability 22 Jul 2019 ](/2019/07/22/jackson-gadgets.html)

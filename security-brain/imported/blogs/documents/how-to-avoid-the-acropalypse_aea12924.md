---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-30_how-to-avoid-the-acropalypse.md
original_filename: 2023-03-30_how-to-avoid-the-acropalypse.md
title: How to avoid the aCropalypse
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: aea1292451f906644f290ad221467433949128d0a01965cd28af71b2fb829bf3
text_sha256: 339761348993c92f22ed1a30670cbe2ec2087a127579f292ebca70328dd1c8ee
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# How to avoid the aCropalypse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-30_how-to-avoid-the-acropalypse.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `aea1292451f906644f290ad221467433949128d0a01965cd28af71b2fb829bf3`
- Text SHA256: `339761348993c92f22ed1a30670cbe2ec2087a127579f292ebca70328dd1c8ee`


## Content

---
title: "How to avoid the aCropalypse"
page_title: "How to avoid the aCropalypse - The Trail of Bits Blog"
url: "https://blog.trailofbits.com/2023/03/30/acropalypse-polytracker-blind-spots/"
final_url: "https://blog.trailofbits.com/2023/03/30/acropalypse-polytracker-blind-spots/"
authors: ["Henrik Brodin"]
programs: ["Google", "Microsoft"]
bugs: ["Privacy issue", "Information disclosure", "Android"]
publication_date: "2023-03-30"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1319
---

# How to avoid the aCropalypse

[Henrik Brodin](/authors/henrik-brodin/)

March 30, 2023

[program-analysis](/categories/program-analysis/), [research-practice](/categories/research-practice/)

Page content

  * The aCropalypse is upon us!
  * Understanding the aCropalypse
  * aCropalyptic files will have Blind Spots when processed
  * Show me!
  * PolyFile to the rescue
  * It doesn’t stop here
  * Acknowledgements

## The aCropalypse is upon us!

Last week, news about CVE-2023-21036, nicknamed the “[aCropalypse](https://www.da.vidbuchanan.co.uk/blog/exploiting-acropalypse.html),” spread across [Twitter](https://twitter.com/ItsSimonTime/status/1636857478263750656) and other media, and I quickly realized that the underlying flaw could be detected by our tool, [PolyTracker](https://github.com/trailofbits/polytracker). I’ll explain how PolyTracker can detect files affected by the vulnerability even without specific file format knowledge, which parts of a file can become subject to recovery using [acropalypse.app](https://acropalypse.app/), and how Google and Microsoft could have caught this bug by using our tools. Coincidentally, my colleagues, Evan Sultanik and Marek Surovič, and I [wrote a paper](https://arxiv.org/abs/2301.08700) that describes this class of bugs, defines a novel approach for detecting them, and introduces our implementation and tooling. It will appear at this year’s workshop on Language-Theoretic Security ([LangSec](https://langsec.org/spw23/)) at the IEEE Security and Privacy Symposium.

We use PolyTracker to instrument the image parser, `libpng`. (Any parser will do, not just aCropalyptic ones.) The PolyTracker instrumentation tells us which portions of the input file are completely ignored by the parser, which we call _blind spots_. Blind spots are almost always indicators of design flaws in the file format, malformation in the input file, and/or a bug in the parser. Normal images should have almost no blind spots, but parsing malformed aCropalyptic images through `libpng` reveals the cropped data in a large blind spot. The aCropalypse bugs could have been caught if the vulnerable products had been instrumented with PolyTracker and their output tested for blind spots.

![PolyTracker blind spot detection example](/2023/03/30/acropalypse-polytracker-blind-spots/646f5cdf68158456ebd6beb5c4a96dfd_hu_b4f60086f9418dc3.webp)
  
  
  # parse the screenshot with an instrumented version of pngtest
  $ ./pngtest.instrumented re3eot.png.png out_re3eot.png.png
  # ask polytracker to identify any blindspots in the file
  $ polytracker cavities polytracker.tdag
  Re3eot.png,697120,1044358
  # found a blind spot starting at offset 697120 (size ~300KiB), it is ignored and contains the cropped out image data that could be retrieved

## Understanding the aCropalypse

According to [this tweet](https://twitter.com/ItsSimonTime/status/1636857478263750656), it is possible to recover parts of an original image from a cropped or redacted screenshot. The TL;DR is that when the Google Pixel built-in screenshot editing tool, Markup, is used to crop or resize an image, it overwrites the original image, but only up to the offset where the new image ends. Any data from the original image after that offset is left intact in the file. David Buchanan devised an algorithm to recover the original image data still left in the file; you can read more about the specifics on [his blog](https://www.da.vidbuchanan.co.uk/blog/exploiting-acropalypse.html).

![aCropalypse vulnerability illustration](/2023/03/30/acropalypse-polytracker-blind-spots/0c62c614297e4dcabd39207441eabae1_hu_45d9ea2880e87b6d.webp)

More recently, Chris Blume identified a similar vulnerability for the Windows Snipping Tool. The methodology we describe here for the Markup tool can be used on images produced by the Windows Snipping Tool.

PolyTracker has a feature we introduced a couple of years ago called _blind spot detection_. We define _blind spots_ as the set of input bytes whose data flow never influences either the control flow that leads to an output or an output itself. Or, in layman’s terms, _unused file data that can be altered to have any content without affecting the output_. The cropped-out regions of an aCropalypse image are, by definition, blind spots, so PolyTracker should be able to detect them!

One of the challenges of tracking input bytes and detecting blind spots for real-world inputs like PNG images or PDF documents is _taint explosion_. The PNG file format contains compressed chunks of image data. Compression is especially keen on contributing to taint explosion as input bytes combine in many ways to produce output bytes. PolyTracker’s unique representation of the taint structure allows us to track 2^31 unique taint labels, which is necessary for analyzing taints propagated during [zlib](https://zlib.net/)-decompression of image data.

## aCropalyptic files will have Blind Spots when processed

To understand why the aCropalypse vulnerability produces blind spots, we need to combine our knowledge of the vulnerability with the description of blind spots. When parsing a PNG file with a PNG parser, the parser will interpret the header data and consume chunks according to the PNG specification. In particular, it will end at a chunk with type IEND, even if that is not at the actual end of the file.

We use PolyTracker to [instrument a tool](https://github.com/trailofbits/polytracker/blob/acropalypse/examples/Dockerfile-acropalypse.demo) (pngtest from the [libpng](https://libpng.sourceforge.io/) project) that reads PNG files and writes them to disk again. This will produce an additional output file, called `polytracker.tdag`, that captures the data flow from the runtime trace. Using that file and PolyTracker’s blind spot detection feature, we can enumerate the input bytes that do not affect the resulting image. Remember, these are the bytes of the input file that neither affect any control flow, nor end up (potentially mixed with other data) in the output file. They have no actual meaning in interpreting the format for the given parser.

## Show me!

Using the PolyTracker-instrumented `pngtest` application, we load, parse, and then store the below image to disk again. During this processing, we track all input bytes through PNG and zlib processing until they eventually reach the output file in some form.

![Example aCropalyptic image](/2023/03/30/acropalypse-polytracker-blind-spots/646f5cdf68158456ebd6beb5c4a96dfd_hu_b4f60086f9418dc3.webp)

We use a [Docker image](https://github.com/trailofbits/polytracker/blob/acropalypse/examples/Dockerfile-acropalypse.demo) containing the PolyTracker instrumented pngtest application.
  
  
  docker run -ti --rm -v $(pwd):/workdir acropalypse
  cd /workdir
  /polytracker/acropalypse/libpng-1.6.39/pngtest.instrumented re3eot.png.png out_re3eot.png.png

The `re3eot.png` image is 1044358 bytes in size, whereas the `out_re3eot.png` is 697,182 bytes. Although this indicates a fairly large reduction in size, at this point we can’t tell why; it could, for example, be the result of different compression settings.

Next, let’s find the blind spots from this process:
  
  
  $ polytracker cavities polytracker.tdag
  
  100%|███████████████████| 1048576/1048576 [00:01<00:00, 684922.43it/s]
  re3eot.png,697120,1044358
  out_re3eot.png,37,697182

The output we are interested in is:
  
  
  re3eot.png,697120,1044358

This tells us that the data starting from offset 697,120 to the end of the file was ignored when producing the output image. We have found a blind spot! The additional 347,238 bytes of unused data could be left from an original image—an indication of the aCropalypse vulnerability. Let’s use the [acropalypse.app](https://acropalypse.app/) web page to see if we can recover it.

![Acropalypse app recovery attempt](/2023/03/30/acropalypse-polytracker-blind-spots/9178517825282e8a56caee6a1ee351d8_hu_2d54d450d0971512.webp)

This indicates that the file was in fact produced by the vulnerable application. At this point, we know that the image contains data from the original image at the end, as that is the core of the vulnerability. We also know the exact location and extent of that data (according to the blind spot’s starting offset and size). To confirm that the data is in fact a blind spot, let’s manually crop the original image and redo the `pngtest` operation to ensure that the resulting files are in fact equal. First, let’s copy only the portion that is not a blind spot—the data that is used to produce the output image.
  
  
  dd if=re3eot.png of=manually_cropped_re3eot.png count=1 bs=697120

Next, let’s run the `pngtest` application again:
  
  
  /polytracker/acropalypse/libpng-1.6.39/pngtest.instrumented manually_cropped_re3eot.png out_manually_cropped_re3eot.png

If our assumption—that only the first 697,120 bytes were used to produce the output image— is correct, we should have two identical output files, despite the removal of 347,238 bytes from the `manually_cropped_re3eot.png` input file.
  
  
  $ sha1sum out_manually_cropped_re3eot.png out_re3eot.png
  8f4a0417da4c68754d2f85e059ee2ad87c02318f  out_manually_cropped_re3eot.png
  8f4a0417da4c68754d2f85e059ee2ad87c02318f  out_re3eot.png

Success! To ensure that the manually cropped file isn’t still affected by the vulnerability, let’s use the web page to try to reconstruct additional image data in the file. This attempt was unsuccessful, as we have removed the original image contents. (Yes, I have checked the cropped screenshot for blind spots 😁).

![Verification that manual crop removed vulnerability](/2023/03/30/acropalypse-polytracker-blind-spots/5d5fb0447eef120416210fa040cbc2c4_hu_d9f29ecc4d1c6515.webp)

To better understand why the blind spot started at the particular offset, we need to examine the structure of the original image.

## PolyFile to the rescue

PolyTracker has a sibling tool: [PolyFile](https://github.com/trailofbits/polyfile), a pure Python cleanroom implementation of libmagic, with instrumented parsing from Kaitai struct and an interactive hex viewer. We will use PolyFile’s ability to produce an HTML rendering of the file structure to understand why file processing ends before the file ends.

First, we use the following command to produce an HTML file representing the file format:
  
  
  polyfile --html re3eot.html re3eot.png.

When we open the `re3eot.html` file in a browser, we’ll see an initial representation of the file.

![PolyFile HTML representation initial view](/2023/03/30/acropalypse-polytracker-blind-spots/ecbe6cba711f52d62eb85407d052d3c2_hu_21ce77f139f6cbc9.webp)

By repeatedly expanding the file structure on the left-hand side, we eventually reach the final chunk.

![PolyFile showing IEND chunk and blind spot location](/2023/03/30/acropalypse-polytracker-blind-spots/0da38cb47c9ea5dbc6721f44a9f677b7_hu_365c7dddcea87c43.webp)

As shown in the above picture, the final chunk, when interpreting the PNG-format, has type IEND. Following that chunk is the remaining data from the original file. Note how the superfluous data starts at offset 0xaa320—that is, 697,120, the exact same offset of the identified blind spot. If you were to scroll all the way to the end, you would find an additional IEND structure (from the original image), but that is not interpreted as a valid part of the PNG file.

## It doesn’t stop here

Having almost no knowledge of the PNG file format, we were able to use PolyTracker instrumentation on an existing PNG processing application to detect not only files that have blind spots, but also their exact location and extent.

PolyTracker can detect blind spots anywhere in the file, not only at the end. Even though we analyzed PNG files, PolyTracker isn’t limited to a specific format. We have previously [analyzed conversion of PDFs to PostScript using MμPDF](https://arxiv.org/abs/2301.08700). The same technique is valid for any application that does a load/store or deserialize/serialize operation. To further increase our understanding of the format and the effects of the vulnerability, we used PolyFile to inspect the file structure.

These are just a couple of use cases for our tools, there are plenty of others! We encourage you to try our [PolyTracker](https://github.com/trailofbits/polytracker) and [PolyFile](https://github.com/trailofbits/polyfile) tools yourself to see how they can help you identify unexpected processing and prevent vulnerabilities similar to the aCropalypse in your application.

## Acknowledgements

This research was supported in part by the Defense Advanced Research Projects Agency (DARPA) SafeDocs program as a subcontractor to Galois under HR0011-19-C-0073. The views, opinions, and findings expressed are those of the author and should not be interpreted as representing the official views or policies of the Department of Defense or the U.S. Government.

Many thanks to Evan Sultanik, Marek Surovič, Michael Brown, Trent Brunson, Filipe Casal, Peter Goodman, Kelly Kaoudis, Lisa Overall, Stefan Nagy, Bill Harris, Nichole Schimanski, Mark Tullsen, Walt Woods, Peter Wyatt, Ange Albertini, and Sergey Bratus for their invaluable feedback on the approach and tooling. Thanks to Ange Albertini for suggesting _angles morts_ —French for “blind spots”—to name the concept, and to Will Tan for sharing a file affected by the vulnerability. Special thanks to Carson Harmon, the original creator of PolyTracker, whose ideas and discussions germinated this research, and Evan Sultanik for helping write this blog post.

#### If you enjoyed this post, share it:

[ X](https://x.com/trailofbits "X")

[ LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[ GitHub](https://github.com/trailofbits "GitHub")

[ Mastodon](https://infosec.exchange/@trailofbits "Mastodon")

[ Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

## Related Posts

### [Maat: Symbolic execution made easyFebruary 23, 2022We have released Maat, a cross-architecture, multi-purpose, and user-friendly symbolic execution framework. It provides …](/2022/02/23/maat-symbolic-execution-made-easy/)### [Two New Tools that Tame the Treachery of FilesNovember 1, 2019Parsing is hard, even when a file format is well specified. But when the specification is ambiguous, it leads to …](/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/)### [Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.May 12, 2026We built gosentry, a fuzzing-oriented fork of the Go toolchain that keeps the standard fuzzing workflow while using a …](/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-08_the-story-of-a-fuzzing-integration-reward.md
original_filename: 2020-04-08_the-story-of-a-fuzzing-integration-reward.md
title: The story of a fuzzing integration reward
category: documents
detected_topics:
- automation-abuse
- sso
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- automation-abuse
- sso
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: fc3653870fb4cbc63989341927fedaf6d44a2178e565a1584b202c035c12b4be
text_sha256: 78e28b35f54586074a78df77c308ccde0635811f527be98e63d8c33faec40f91
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# The story of a fuzzing integration reward

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-08_the-story-of-a-fuzzing-integration-reward.md
- Source Type: markdown
- Detected Topics: automation-abuse, sso, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `fc3653870fb4cbc63989341927fedaf6d44a2178e565a1584b202c035c12b4be`
- Text SHA256: `78e28b35f54586074a78df77c308ccde0635811f527be98e63d8c33faec40f91`


## Content

---
title: "The story of a fuzzing integration reward"
page_title: "LibreSSL and OSS-Fuzz · Doyensec's Blog"
url: "https://blog.doyensec.com/2020/04/08/libressl-fuzzer.html"
final_url: "https://blog.doyensec.com/2020/04/08/libressl-fuzzer.html"
authors: ["Andrea Brancaleoni (@nJoyneer)"]
programs: ["Google"]
bugs: ["Memory corruption"]
bounty: "10,000"
publication_date: "2020-04-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4659
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

# LibreSSL and OSS-Fuzz

08 Apr 2020 - Posted by Andrea Brancaleoni

# The story of a fuzzing integration reward

In my first month at Doyensec I had the opportunity to bring together both my work and my spare time hobbies. I used the 25% research time offered by Doyensec to integrate the [LibreSSL](https://www.libressl.org/) library into [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz). LibreSSL is an API compatible replacement for [OpenSSL](https://www.openssl.org/), and after the [heartbleed](http://heartbleed.com/) attack, it is considered as a full-fledged replacement of OpenSSL on [OpenBSD](https://www.openbsd.org), [macOS](https://www.apple.com/macos) and [VoidLinux](https://voidlinux.org/).

![OSS-Fuzz Fuzzying Process](../../../public/images/libressl.jpg)

Contextually to this research, we were [awarded by Google](https://www.google.com/about/appsecurity/patch-rewards/) a **$10,000 bounty** , 100% of which was donated to the [Cancer Research Institute](https://www.cancerresearch.org/join-the-cause/donate). The fuzzer also discovered **14+ new vulnerabilities** and four of these were directly related to memory corruption.

In the following paragraphs we will walk through the process of porting a new project over to [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) from following the community provided steps all the way to the actual code porting and we will also show a vulnerability fixed in [`136e6c997f476cc65e614e514ac3bf6ee54fc4b4`](https://github.com/libressl-portable/openbsd/commit/136e6c997f476cc65e614e514ac3bf6ee54fc4b4).
  
  
  commit ***REDACTED-SUSPECT-TOKEN***  Author: beck <>
  Date:  Sat Mar 23 18:48:15 2019 +0000
  
  Add range checks to varios ASN1_INTEGER functions to ensure the
  sizes used remain a positive integer. Should address issue
  13799 from oss-fuzz
  ok tb@ jsing@
  
  src/lib/libcrypto/asn1/a_int.c  | 56 +++++++++++++++++++++++++++++++++++++++++++++++++++++---
  src/lib/libcrypto/asn1/tasn_prn.c |  8 ++++++--
  src/lib/libcrypto/bn/bn_lib.c  |  4 +++-
  3 files changed, 62 insertions(+), 6 deletions(-)
  

## The FOSS historician blurry book

As a [voidlinux maintainer](https://voidlinux.org/), I’m a long time [LibreSSL](https://www.libressl.org/) user and proponent. [LibreSSL](https://www.libressl.org/) is a version of the TLS/crypto stack forked from OpenSSL in 2014 with the goals of modernizing the codebase, improving security, and applying best practice development procedures. The motivation for this kind of fork arose after the discovery of the [Heartbleed](http://heartbleed.com/) vulnerability.

[LibreSSL](https://www.libressl.org/)’s efforts are aimed at removing code considered useless for the target platforms, removing code smells and including additional secure defaults at the cost of compatibility. The [LibreSSL](https://www.libressl.org/) codebase is now nearly 70% the size of [OpenSSL](https://www.openssl.org/) (237558 cloc vs 335485 cloc), while implementing a similar API on all the major modern operating systems.

> Forking is considered a Bad Thing not merely because it implies a lot of wasted effort in the future, but because forks tend to be accompanied by a great deal of strife and acrimony between the successor groups over issues of legitimacy, succession, and design direction. There is serious social pressure against forking. As a result, major forks (such as the Gnu-Emacs/XEmacs split, the fissioning of the 386BSD group into three daughter projects, and the short-lived GCC/EGCS split) are rare enough that they are remembered individually in hacker folklore.  
>  
> _Eric Raymond_ **Homesteading the Noosphere**

The [LibreSSL](https://www.libressl.org/) effort was generally well received and it now replaces [OpenSSL](https://www.openssl.org/) on [OpenBSD](https://www.openbsd.org), [macOS](https://www.apple.com/macos) since 10.11 and on many other Linux distributions. In the first few years 6 critical vulnerabilities were found in OpenSSL and none of them affected [LibreSSL](https://www.libressl.org/).

Historically, these kinds of forks tend to spawn competing projects which cannot later exchange code, splitting the potential pool of developers between them. However, the [LibreSSL](https://www.libressl.org/) team has largely demonstrated of being able to merge and implement new OpenSSL code and bug fixes, all the while slimming down the original source code and cutting down on rarely used or dangerous features.

## OSS-Fuzz Selection

While the development of [LibreSSL](https://www.libressl.org/) appears to be a story with an happy ending, the integration of fuzzing and security auditing into the project was much less so. The [Heartbleed](http://heartbleed.com/) vulnerability was like a wakeup call to the industry for tackling the security of libraries that make up the core of the internet. In particular, Google opened up [OSS-Fuzz project](https://opensource.google.com/projects/oss-fuzz). [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) is an effort to provide, for free, Google infrastructure to perform [fuzzing](https://en.wikipedia.org/wiki/Fuzzing) against the most popular open source libraries. One of the first projects performing these tests was in fact [Openssl](https://www.openssl.org/).

![OSS-Fuzz Fuzzying Process](../../../public/images/oss-fuzz.png)

[Fuzz testing](https://en.wikipedia.org/wiki/Fuzzing) is a well-known technique for uncovering programming errors in software. Many of these detectable errors, like [buffer overflows](https://en.wikipedia.org/wiki/Buffer_overflow), can have serious security implications. [OpenSSL](https://www.openssl.org/) included fuzzers in [`c38bb72797916f2a0ab9906aad29162ca8d53546`](https://github.com/openssl/openssl/commit/c38bb72797916f2a0ab9906aad29162ca8d53546) and was integrated into [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) later in 2016.
  
  
  commit ***REDACTED-SUSPECT-TOKEN***  Refs: OpenSSL_1_1_0-pre5-217-gc38bb72797
  Author:  Ben Laurie <ben@links.org>
  AuthorDate: Sat Mar 26 17:19:14 2016 +0000
  Commit:  Ben Laurie <ben@links.org>
  CommitDate: Sat May 7 18:13:54 2016 +0100
  Add fuzzing!
  

Since both [LibreSSL](https://www.libressl.org/) and [OpenSSL](https://www.openssl.org/) share most of their codebase, with [LibreSSL](https://www.libressl.org/) mainly implementing a secure subset of OpenSSL, we thought porting the [OpenSSL](https://www.openssl.org/) fuzzers to [LibreSSL](https://www.libressl.org/) would have been a fun and useful project. Moreover, this resulted in the discovery of several memory related corruption bugs.

To be noted, the following details won’t replace the official [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) guide but will instead help in selecting a good target project for [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) integration. Generally speaking applying for a new [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) integration proceeds in four logical steps:

  * **Selection:** Select a new project that isn’t yet ported. Check for existing projects in [OSS-Fuzz projects directory](https://github.com/google/oss-fuzz/tree/master/projects). For example, check if somebody already tried to perform the same integration in a [pull-request](https://github.com/google/oss-fuzz/pulls).
  * **Feasibility:** Check the feasibility and the security implications of that project on the Internet. As a general guideline, the more impact the project has on the everyday usage of the web the bigger the bounty will be. At the time of writing, [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) bounties are up to $20,000 with the [Google patch-reward program](https://www.google.com/about/appsecurity/patch-rewards/). On the other hand, good coverage is expected to be developed for any integration. For this reason it is easier to integrate projects that already employ fuzzers.
  * **Technical integration:** Follow the super detailed [getting started guide](https://google.github.io/oss-fuzz/getting-started/accepting-new-projects/) to perform an initial integration.
  * **Profit:** Apply for the [Google patch-reward program](https://www.google.com/about/appsecurity/patch-rewards/). Profit?!

We were awarded a bounty, and we helped to protect the Internet just a little bit more. You should do it too!

## Heartbreak

After a crash was found, [OSS-Fuzz infrastructure](https://opensource.google.com/projects/oss-fuzz) provides a minimized test case which can be inspected by an analyst. The issue was found in the [ASN1 parser](https://www.itu.int/en/ITU-T/asn1/Pages/introduction.aspx). [ASN1](https://www.itu.int/en/ITU-T/asn1/Pages/introduction.aspx) is a formal notation used for describing data transmitted by telecommunications protocols, regardless of language implementation and physical representation of these data, whether complex or very simple. Coincidentally, it is employed for [x.509 certificates](https://www.itu.int/rec/T-REC-X.509), which represents the technical base for building [public-key infrastructure](https://en.wikipedia.org/wiki/Public_key_certificate).

Passing our testcase `0202 ff25` through [dumpasn1](https://manpages.debian.org/stretch/dumpasn1/dumpasn1.1.en.html) it’s possible to see how it errors out saying that the integer of length 2 (bytes) is encoded with a negative value. This is not allowed in [ASN1](https://www.itu.int/en/ITU-T/asn1/Pages/introduction.aspx), and it should not even be allowed in [LibreSSL](https://www.libressl.org/). However, as discovered by [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz), this test crashes the [Libressl parser](https://www.libressl.org/).
  
  
  $ xxd ./test
  xxd ../test
  00000000: 0202 ff25  ...%
  $ dumpasn1 ./test
  0  2: INTEGER 65317
  :  Error: Integer is encoded as a negative value.
  
  0 warnings, 1 error.
  

Since the LibreSSL implementation was not guarded against negative integers, trying to covert the ASN1 integer crafted a negative to an internal representation of BIGNUM and causes an uncontrolled over-read.
  
  
  AddressSanitizer:DEADLYSIGNAL
  =================================================================
  ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x00009fff8000 (pc 0x00000058a308 bp 0x7ffd3e8b7bb0 sp 0x7ffd3e8b7b40 T0)
  ==1==The signal is caused by a READ memory access.
  SCARINESS: 20 (wild-addr-read)
  #0 0x58a307 in BN_bin2bn libressl/crypto/bn/bn_lib.c:601:19
  #1 0x6cd5ac in ASN1_INTEGER_to_BN libressl/crypto/asn1/a_int.c:456:13
  #2 0x6a39dd in i2s_ASN1_INTEGER libressl/crypto/x509v3/v3_utl.c:175:16
  #3 0x571827 in asn1_print_integer_ctx libressl/crypto/asn1/tasn_prn.c:457:6
  #4 0x571827 in asn1_primitive_print libressl/crypto/asn1/tasn_prn.c:556
  #5 0x571827 in asn1_item_print_ctx libressl/crypto/asn1/tasn_prn.c:239
  #6 0x57069a in ASN1_item_print libressl/crypto/asn1/tasn_prn.c:195:9
  #7 0x4f4db0 in FuzzerTestOneInput libressl.fuzzers/asn1.c:282:13
  #8 0x7fd3f5 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /src/libfuzzer/FuzzerLoop.cpp:529:15
  #9 0x7bd746 in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) /src/libfuzzer/FuzzerDriver.cpp:286:6
  #10 0x7c9273 in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) /src/libfuzzer/FuzzerDriver.cpp:715:9
  #11 0x7bcdbc in main /src/libfuzzer/FuzzerMain.cpp:19:10
  #12 0x7fa873b8282f in __libc_start_main /build/glibc-Cl5G7W/glibc-2.23/csu/libc-start.c:291
  #13 0x41db18 in _start
  

This “wild” address read may be employed by malicious actors to perform leaks in security sensitive context. The [Libressl](https://www.libressl.org/) maintainers team not only addressed the vulnerability promptly but also included an ulterior protection in order to guard against missing `ASN1_PRIMITIVE_FUNCS` in [`46e7ab1b335b012d6a1ce84e4d3a9eaa3a3355d9`](https://github.com/libressl-portable/openbsd/commit/46e7ab1b335b012d6a1ce84e4d3a9eaa3a3355d9).
  
  
  commit ***REDACTED-SUSPECT-TOKEN***  Author: jsing <>
  Date:  Mon Apr 1 15:48:04 2019 +0000
  
  Require all ASN1_PRIMITIVE_FUNCS functions to be provided.
  
  If an ASN.1 item provides its own ASN1_PRIMITIVE_FUNCS functions, require
  all functions to be provided (currently excluding prim_clear). This avoids
  situations such as having a custom allocator that returns a specific struct
  but then is then printed using the default primative print functions, which
  interpret the memory as a different struct.
  

## Closing the door to strangers

[Fuzzing](https://en.wikipedia.org/wiki/Fuzzing), despite being seen as one of the easiest ways to discover security vulnerabilities, still works very well. Even if [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) is especially tailored to open source projects, it can also be adapted to closed source projects. In fact, at the cost of implementing the `LLVMFuzzerOneInput` interface, it integrates all the latest and greatest clang/llvm fuzzer technology. As Dockerfile language improves enormously on the devops side, we strongly believe that the [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz) fuzzing interface definition language should be employed in every non-trivial closed source project too. If you need help, contact us for your [security automation](https://doyensec.com/automation.html) projects!

As always, this research was funded thanks to the [25% research time offered at Doyensec](https://doyensec.com/research.html). Tune in again for new episodes!

### Other relevant posts:

  * ###  [ Product Security Audits vs. Bug Bounty 02 May 2024 ](/2024/05/02/products-security-audit-vs-bugbounty.html)

  * ###  [ Huawei Theme Manager Arbitrary Code Execution 26 Jul 2023 ](/2023/07/26/huawei-theme-arbitrary-code-exec.html)

  * ###  [ CSRF Protection Bypass in Play Framework 20 Aug 2020 ](/2020/08/20/playframework-csrf-bypass.html)

  * ###  [ Don't Clone That Repo: Visual Studio Code^2 Execution 16 Mar 2020 ](/2020/03/16/vscode_codeexec.html)

  * ###  [ Signature Validation Bypass Leading to RCE In Electron-Updater 24 Feb 2020 ](/2020/02/24/electron-updater-update-signature-bypass.html)

  * ###  [ Security Analysis of the Solo Firmware 19 Feb 2020 ](/2020/02/19/solokeys-audit.html)

  * ###  [ Heap Overflow in F-Secure Internet Gatekeeper 03 Feb 2020 ](/2020/02/03/heap-exploit.html)

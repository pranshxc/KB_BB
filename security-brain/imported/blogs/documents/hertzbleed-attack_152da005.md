---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_hertzbleed-attack.md
original_filename: 2022-06-14_hertzbleed-attack.md
title: Hertzbleed Attack
category: documents
detected_topics:
- sso
- command-injection
- rate-limit
- automation-abuse
- race-condition
- clickjacking
tags:
- imported
- documents
- sso
- command-injection
- rate-limit
- automation-abuse
- race-condition
- clickjacking
language: en
raw_sha256: 152da005f780d98ea91da2d67092320e1563f945b2172ebc26971941d7304051
text_sha256: 90ce8bd5a3cb886f3fa436e5a8bccd4e2db4b15af7936e57819759336580097d
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hertzbleed Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_hertzbleed-attack.md
- Source Type: markdown
- Detected Topics: sso, command-injection, rate-limit, automation-abuse, race-condition, clickjacking
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `152da005f780d98ea91da2d67092320e1563f945b2172ebc26971941d7304051`
- Text SHA256: `90ce8bd5a3cb886f3fa436e5a8bccd4e2db4b15af7936e57819759336580097d`


## Content

---
title: "Hertzbleed Attack"
url: "https://www.hertzbleed.com"
final_url: "https://www.hertzbleed.com/"
authors: ["Yingchen Wang (@YingchenWang96)", "Riccardo Paccagnella (@ricpacca)", "Elizabeth Tang He", "Hovav Shacham (@hovav)", "Christopher Fletcher", "David Kohlbrenner (@dkohlbre)"]
programs: ["Intel", "Cloudflare", "Microsoft"]
bugs: ["Side-channel attack", "Hardware hacking", "Cryptographic issues"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2551
---

# Hertzbleed Attack

  * [Original Paper (USENIX'22)](/hertzbleed.pdf)
  * [Follow-Up Paper (S&P'23)](/2h2b.pdf)

📣 Update: Our S&P 2026 follow-up work introduces Goldilocks, a practical Hertzbleed mitigation with formal leakage guarantees. Check out [the paper](https://www.cs.cmu.edu/~rpaccagn/papers/goldilocks-sp2026.pdf)!

📣 Update: In follow-up work appearing in S&P 2025, we show that on modern Intel processors, Hertzbleed-style attacks are more effective (5x faster) and work even in the absence of frequency side-channel leakage. Check out [the paper](/scheduled-disclosure-sp2025.pdf)!

Looking for the (unrelated) GPU.zip side channel? Check it out [here](/gpu.zip)!

📣 Update: Our follow-up paper expanding the scope of Hertzbleed has appeared in the IEEE Symposium on Security and Privacy 2023. See details below.

Hertzbleed is a new family of side-channel attacks: frequency side channels. In the worst case, these attacks can allow an attacker to extract cryptographic keys from remote servers that were previously believed to be secure.

Hertzbleed takes advantage of our experiments showing that, under certain circumstances, the dynamic frequency scaling of modern x86 processors depends on the data being processed. This means that, on modern processors, the same program can run at a different CPU frequency (and therefore take a different wall time) when computing, for example, `2022 + 23823` compared to `2022 + 24436`.

Hertzbleed is a real, and practical, threat to the security of cryptographic software. We have demonstrated how a clever attacker can use a novel chosen-ciphertext attack against [SIKE](https://sike.org/) to perform full key extraction via remote timing, despite SIKE being implemented as “constant time”.

  

**_Update (April 2023):_**

SIKE has now been deprecated due to unrelated security concerns. For more information, see the Eurocrypt 2023 papers “An efficient key recovery attack on SIDH” (Wouter Castryck and Thomas Decru), “Breaking SIDH in polynomial time” (Damien Robert) and “A Direct Key Recovery Attack on SIDH” (Luciano Maino et al.).

  

📣 **_Update (May 2023):_**

In follow-up work, we demonstrated that Hertzbleed, combined with existing cryptanalysis, affects “constant-time” implementations of cryptosystems beyond SIKE, including ECDSA and Classic McEliece. We also demonstrated that Hertzbleed extends to programs beyond cryptography and that CPU frequency can leak information about computations occurring in other processor components such as the GPU. Specifically, Hertzbleed can be used to launch a pixel stealing attack on cross-origin iframes in Google Chrome. For more information, see our paper “DVFS Frequently Leaks Secrets: Hertzbleed Attacks Beyond SIKE, Cryptography, and CPU-Only Data” (linked [here](/2h2b.pdf)).

In independent and concurrent work, Taneja et al. showed that GPU computations can also trigger _GPU_ frequency changes. For more information, see their paper “Hot Pixels: Frequency, Power, and Temperature Attacks on GPUs and ARM SoCs” (linked [here](https://arxiv.org/abs/2305.12784)).

## Research Papers

The original Hertzbleed paper appeared in the 31st USENIX Security Symposium (Boston, 10–12 August 2022) with the following title:

  * _Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86_

You can download a preprint from [here](/hertzbleed.pdf), and the BibTeX citation from [here](/hertzbleed.bib).

The paper is the result of a collaboration between the following researchers:

  * [Yingchen Wang](https://www.cs.utexas.edu/~yingchen/) (University of Texas at Austin)
  * [Riccardo Paccagnella](https://rp8.web.engr.illinois.edu/) (University of Illinois Urbana-Champaign)
  * Elizabeth Tang He (University of Illinois Urbana-Champaign)
  * [Hovav Shacham](https://www.cs.utexas.edu/~hovav/) (University of Texas at Austin)
  * [Christopher Fletcher](http://cwfletcher.net/) (University of Illinois Urbana-Champaign)
  * [David Kohlbrenner](https://homes.cs.washington.edu/~dkohlbre/) (University of Washington)

  

📣 **_Update (May 2023):_**

The follow-up paper appeared in the 44th IEEE Symposium on Security and Privacy (San Francisco, 22-25 May 2023) with the following title:

  * _DVFS Frequently Leaks Secrets: Hertzbleed Attacks Beyond SIKE, Cryptography, and CPU-Only Data_

You can download a preprint from [here](/2h2b.pdf), and the BibTeX citation from [here](/2h2b.bib).

The paper is the result of a collaboration between the following researchers:

  * [Yingchen Wang](https://www.cs.utexas.edu/~yingchen/) (University of Texas at Austin)
  * [Riccardo Paccagnella](https://rp8.web.engr.illinois.edu/) (University of Illinois Urbana-Champaign)
  * Alan Wandke (University of Illinois Urbana-Champaign)
  * Zhao Gang (University of Texas at Austin)
  * Grant Garrett-Grossman (University of Illinois Urbana-Champaign)
  * [Christopher Fletcher](http://cwfletcher.net/) (University of Illinois Urbana-Champaign)
  * [David Kohlbrenner](https://homes.cs.washington.edu/~dkohlbre/) (University of Washington)
  * [Hovav Shacham](https://www.cs.utexas.edu/~hovav/) (University of Texas at Austin)

## Questions and Answers

### Am I affected by Hertzbleed?

Likely, yes.

[Intel’s security advisory](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00698.html) states that _all_ Intel processors are affected. We experimentally confirmed that several Intel processors are affected, including desktop and laptop models from the 8th to the 11th generation Core microarchitecture.

[AMD’s security advisory](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1038) states that several of their desktop, mobile and server processors are affected. We experimentally confirmed that AMD Ryzen processors are affected, including desktop and laptop models from the Zen 2 and Zen 3 microarchitectures.

Other processor vendors (e.g., Arm) also implement frequency scaling in their products and were made aware of Hertzbleed. However, we have not confirmed if they are, or are not, affected by Hertzbleed.

**_Update (Nov 2022):_**

  * Arm has released a [documentation update](https://developer.arm.com/documentation/ka005111/1-0/) stating that “Arm CPUs may be affected”.
  * Ampere has released a [security bulletin](https://amperecomputing.com/products/security-bulletins/hertzbleed.html) stating that their Altra, Altra Max, and AmpereOne processors are affected by Hertzbleed.

### What is the impact of Hertzbleed?

First, Hertzbleed shows that on modern x86 CPUs, power side-channel attacks can be turned into (even remote!) timing attacks—lifting the need for any power measurement interface. The cause is that, under certain circumstances, periodic CPU frequency adjustments depend on the current CPU power consumption, and these adjustments directly translate to execution time differences (as 1 hertz = 1 cycle per second).

Second, Hertzbleed shows that, even when implemented correctly as constant time, cryptographic code can still leak via remote timing analysis. The result is that current industry guidelines for how to write constant-time code (such as [Intel’s one](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/secure-coding/mitigate-timing-side-channel-crypto-implementation.html)) are insufficient to guarantee constant-time execution on modern processors.

**_Update (May 2023):_**

Beyond cryptography, our follow-up paper has demonstrated that Hertzbleed renders many of the existing mitigations against pixel stealing attacks ineffective. For more information on pixel stealing attacks, see Paul Stone’s “Pixel Perfect Timing Attacks with HTML5” (Black Hat US 2013) or read our S&P 2023 paper.

### Should I be worried?

If you are an ordinary user and not a cryptography engineer, probably not: you don’t need to apply a patch or change any configurations right now.

**_Update (May 2023):_**

Our follow-up work has demonstrated that Hertzbleed has wider applicability than first believed. Fortunately, the risk is still limited as most web pages are not vulnerable to cross-origin iframe pixel stealing.

### Is there an assigned CVE for Hertzbleed?

Yes. Hertzbleed is tracked under CVE-2022-23823 (AMD) and CVE-2022-24436 (Intel) in the Common Vulnerabilities and Exposures (CVE) system.

**_Update (Nov 2022):_**

  * Ampere has assigned CVE-2022-35888 to track Hertzbleed.

### Is Hertzbleed a bug?

No. The root cause of Hertzbleed is dynamic frequency scaling, a _feature_ of modern processors, used to reduce power consumption (during low CPU loads) and to ensure that the system stays below power and thermal limits (during high CPU loads).

### When did you disclose Hertzbleed?

We disclosed our findings, together with proof-of-concept code, to Intel, Cloudflare and Microsoft in Q3 2021 and to AMD in Q1 2022. Intel originally requested our findings be held under embargo until May 10, 2022. Later, Intel requested a significant extension of that embargo, and we coordinated with them on publicly disclosing our findings on June 14, 2022.

### Do Intel and AMD plan to release microcode patches to mitigate Hertzbleed?

No. To our knowledge, Intel and AMD do not plan to deploy any microcode patches to mitigate Hertzbleed. However, Intel provides [guidance](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/technical-documentation/frequency-throttling-side-channel-guidance.html) to mitigate Hertzbleed in software. Cryptographic developers may choose to follow Intel’s guidance to harden their libraries and applications against Hertzbleed. For more information, we refer to the official security advisories ([Intel](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00698.html) and [AMD](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1038)).

### Why did Intel ask for a long embargo, considering they are not deploying patches?

Ask Intel.

### Is there a workaround to mitigate Hertzbleed?

In most cases, a workload-independent workaround to mitigate Hertzbleed is to disable frequency boost. Intel calls this feature “Turbo Boost”, and AMD calls it “Turbo Core” or “Precision Boost”. Disabling frequency boost can be done either through the BIOS or at runtime via the frequency scaling driver. In our experiments, when frequency boost was disabled, the frequency stayed fixed at the base frequency during workload execution, preventing leakage via Hertzbleed. However, this is not a recommended mitigation strategy as it will significantly impact performance. Moreover, on some system configurations, data-dependent frequency updates may occur even when frequency boost is disabled.

### [_new_] When did you disclose the pixel stealing attacks via Hertzbleed on Chrome?

We disclosed our findings, together with proof-of-concept code, to Google in November 2022.

As of May 22 2023 (start date of the 44th IEEE Symposium on Security and Privacy), the Chrome developers are still deciding whether and how to patch.

### [_new_] Is there a workaround to mitigate pixel stealing attacks via Hertzbleed on Chrome?

Yes. One way is to prevent your website from being rendered inside an cross-origin iframe unless specifically needed. This can be done by setting the X-Frame-Options HTTP header to `deny` or `sameorigin`.

### What is SIKE?

SIKE (Supersingular Isogeny Key Encapsulation) is a decade old, widely studied key encapsulation mechanism. It is currently a finalist in NIST’s Post-Quantum Cryptography competition. It has multiple industrial implementations and was the subject of an in-the-wild deployment experiment. Among its claimed advantages are a [“well-understood” side channel posture](https://eprint.iacr.org/2021/543). You can find author names, implementations, talks, studies, articles, security analyses and more about SIKE on [its official website](https://sike.org/).

**_Update (April 2023):_**

SIKE has been proven insecure and is now deprecated. For more information, see the Eurocrypt 2023 papers “An efficient key recovery attack on SIDH” (Wouter Castryck and Thomas Decru), “Breaking SIDH in polynomial time” (Damien Robert) and “A Direct Key Recovery Attack on SIDH” (Luciano Maino et al.). For security implications of Hertzbleed beyond SIKE, see May 2023 updates.

### What is a key encapsulation mechanism?

A key encapsulation mechanism is a protocol used to securely exchange a symmetric key using asymmetric (public-key) cryptography.

### How did Cloudflare and Microsoft mitigate the attack on SIKE?

Both Cloudflare and Microsoft deployed the mitigation suggested by [De Feo et al.](https://eprint.iacr.org/2022/054) (who, while our paper was under the long Intel embargo, independently re-discovered how to exploit anomalous 0s in SIKE for power side channels). The mitigation consists of validating, before decapsulation, that the ciphertext consists of a pair of linearly independent points of the correct order. The mitigation adds a decapsulation performance overhead of 5% for CIRCL and of 11% for PQCrypto-SIDH.

### Is SIKE-751 vulnerable because it is slow? Is it just SIKE-751?

No, SIKE-434 shows a timing signal as big as that of SIKE-751.

### Is my constant-time cryptographic library affected?

Affected? Likely yes. Vulnerable? Maybe.

Your constant-time cryptographic library might be vulnerable if is susceptible to secret-dependent power leakage, and this leakage extends to enough operations to induce secret-dependent changes in CPU frequency. Future work is needed to systematically study what cryptosystems can be exploited via the new Hertzbleed side channel.

### Can I use the logo?

Yes. The Hertzbleed logo is free to use under a [CC0](https://creativecommons.org/publicdomain/zero/1.0/) license.

  * Download logo: [SVG](/images/Hertzbleed-logo.svg), [PNG](/images/Hertzbleed-logo.png)
  * Download logo with text: [SVG](/images/Hertzbleed-logo-with-text.svg), [PNG](/images/Hertzbleed-logo-with-text.png)

### Did we really need another vulnerability logo?

We know some of you don’t really like vulnerability logos, and we hear you. However, we really like our logo (and hope you do too!).

### Did you release the source code of the Hertzbleed attack?

Yes, for full reproducibility. You can find the source code of all the experiments from our paper at the link: <https://github.com/FPSG-UIUC/hertzbleed>

Last updated on May 29, 2026. This website was inspired by the [DROWN attack](https://drownattack.com/) website, which was designed by [Sarah Madden](http://sarahmadden.com/) and is free to use under a CC0 license.

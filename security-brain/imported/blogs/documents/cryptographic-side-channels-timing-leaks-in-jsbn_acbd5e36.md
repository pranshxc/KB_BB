---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_cryptographic-side-channels-timing-leaks-in-jsbn.md
original_filename: 2022-06-14_cryptographic-side-channels-timing-leaks-in-jsbn.md
title: Cryptographic Side-Channels (Timing Leaks) in JSBN
category: documents
detected_topics:
- command-injection
- mfa
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- mfa
- api-security
- supply-chain
language: en
raw_sha256: acbd5e36e43234b2168895c94cb4c40cf7d930e1035a8b3ed4f81a9c0cd845b6
text_sha256: e3eac90bc88f8ed3e252e62749010891293117840a7c83062526796d75f8be33
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Cryptographic Side-Channels (Timing Leaks) in JSBN

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_cryptographic-side-channels-timing-leaks-in-jsbn.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `acbd5e36e43234b2168895c94cb4c40cf7d930e1035a8b3ed4f81a9c0cd845b6`
- Text SHA256: `e3eac90bc88f8ed3e252e62749010891293117840a7c83062526796d75f8be33`


## Content

---
title: "Cryptographic Side-Channels (Timing Leaks) in JSBN"
page_title: "Cryptographic Side-Channels (Timing Leaks) in JSBN · Issue #43 · andyperlitch/jsbn · GitHub"
url: "https://github.com/andyperlitch/jsbn/issues/43"
final_url: "https://github.com/andyperlitch/jsbn/issues/43"
authors: ["Soatok (@SoatokDhole)"]
programs: ["Xfinity Opensource"]
bugs: ["Cryptographic issues", "Side-channel attack", "Timing attack"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2556
---

[ andyperlitch ](/andyperlitch) / **[jsbn](/andyperlitch/jsbn) ** Public

  * [ Notifications ](/login?return_to=%2Fandyperlitch%2Fjsbn) You must be signed in to change notification settings
  * [ Fork 42 ](/login?return_to=%2Fandyperlitch%2Fjsbn)
  * [ Star  174 ](/login?return_to=%2Fandyperlitch%2Fjsbn)

  * [ Code ](/andyperlitch/jsbn)
  * [ Issues 16 ](/andyperlitch/jsbn/issues)
  * [ Pull requests 3 ](/andyperlitch/jsbn/pulls)
  * [ Actions ](/andyperlitch/jsbn/actions)
  * [ Projects ](/andyperlitch/jsbn/projects)
  * [ Wiki ](/andyperlitch/jsbn/wiki)
  * [ Security and quality 0 ](/andyperlitch/jsbn/security)
  * [ Insights ](/andyperlitch/jsbn/pulse)

Additional navigation options

  * [ Code  ](/andyperlitch/jsbn)
  * [ Issues  ](/andyperlitch/jsbn/issues)
  * [ Pull requests  ](/andyperlitch/jsbn/pulls)
  * [ Actions  ](/andyperlitch/jsbn/actions)
  * [ Projects  ](/andyperlitch/jsbn/projects)
  * [ Wiki  ](/andyperlitch/jsbn/wiki)
  * [ Security and quality  ](/andyperlitch/jsbn/security)
  * [ Insights  ](/andyperlitch/jsbn/pulse)

# Cryptographic Side-Channels (Timing Leaks) in JSBN #43

New issue

Copy link

New issue

Copy link

Open

Open

Cryptographic Side-Channels (Timing Leaks) in JSBN#43

Copy link

## Description

[![@soatok](https://avatars.githubusercontent.com/u/8157726?u=745a87c2f5fffe11a0443c00c3767b89fe50d570&v=4&size=48)](https://github.com/soatok)

[soatok](https://github.com/soatok)

opened [on Jun 14, 2022](https://github.com/andyperlitch/jsbn/issues/43#issue-1271134833)

Issue body actions

# Issue Summary

JSBN contains a lot of timing leaks that make it unsuitable for cryptographic use. However, JSBN is broadly used in JavaScript implementations of asymmetric cryptography.

## Modular Exponentiation

JSBN's implementation of modular exponentiation can be found [here](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1228-L1313). The critical loop of this implementation can be found [here](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1266-L1311). For odd moduli larger than 255 (a.k.a. any cryptographic usage), [Montgomery reduction is used](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L556-L625).

  * The [first step of each iteration of the critical loop](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1267-L1271) contains a [branch controlled by secret data](https://github.com/veorq/cryptocoding#avoid-branchings-controlled-by-secret-data).
  * The result of the previous step (w) controls how many times [this loop iterates](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1274-L1277) (i.e. the number of low 0 bits).
  * Finally, there's another [secret-dependent loop bound](https://github.com/veorq/cryptocoding#avoid-secret-dependent-loop-bounds) located [at the end of the critical loop](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1301-L1310).  
The sum of these implementation details is that the bits of your exponent will be leaked (breaking SRP and Diffie-Hellman protocols).

Interestingly, the base (called g [in the critical loop](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1245-L1258)) is never directly leaked in this loop, which would superficially make it only safe for RSA encryption.

(However, values derived directly from the base are passed as [parameters to mulTo()](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1298), which passes to the Montgomery reduction functions linked above. At minimum, this leaks via [comparison](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L606).)

## Modular Inversion

JSBN's implementation of modular inversion can be found [here](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1358-L1407).

  * [This code](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1380) continues for as long as the lowest bit of v (the number being inverted) is cleared (equal to `0`).
  * [This code](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1391-L1399) accesses variables based on a conditional branch (see bignum comparison below). If these two variables are physically located on different memory chips that take a perceptible difference of time to read from, the memory access pattern will be visible to the CPU.
  * After the first loop iteration, the bits of u control a [while loop iteration](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L1369-L1379).

## Bignum Comparison

The implementation of `compareTo()` can be found [here](https://github.com/andyperlitch/jsbn/blob/52fab097bf5fe2ad981be3d5f22b97032811c6a7/index.js#L261-L270). I've reproduced the algorithm below, but reformatted it to be more legible.
  
  
  // (public) return + if this > a, - if this < a, 0 if equal
  function bnCompareTo(a) {
  var r = this.s - a.s;
  if (r != 0) {
  return r;
  }
  var i = this.t;
  r = i - a.t;
  if (r != 0) {
  return this.s < 0 ? -r : r;
  }
  while (--i >= 0) {
  if ((r = this[i] - a[i]) != 0) {
  return r;
  }
  }
  return 0;
  }

It should be clear that `this` will return a value quicker if the first limb differs between `this` and `a` than if a later limb differs. This function leaks information about the two numbers being compared.

## Exploitation and Impact

Timing leaks are pernicious to cryptographic implementations. A cache-timing attack on software AES famously [revealed the secret key](https://cr.yp.to/antiforgery/cachetiming-20050414.pdf) in an attack that took about 65 milliseconds to conclude.

The main exploitation path for a library like JSBN is to have malicious code running in another browser window or service worker that probes the JavaScript engine (i.e. v8 in Chrome) to perform [this sort of timing attack](https://eprint.iacr.org/2013/448.pdf). For prior art, see Rowhammer, Meltdown, and Spectre.

If successful, this will leak the following for the respective asymmetric cryptography algorithms.

**Algorithm / Operation ** | **What Gets Leaked**  
---|---  
RSA encryption | Message (base in exponentiation)  
RSA signing | Private key (exponent)  
Diffie-Hellman | Private key (exponent)  
SRP | Private key (exponent `x`)  
ECDSA signing | One-time secret `k` (via modular inverse)  
  
## Mitigations

The only effective mitigation is to make the JSBN code constant-time. I've previously written [an open source constant-time implementation](https://github.com/soatok/constant-time-js) of bignum arithmetic in TypeScript (which can be trivially compiled to JavaScript).

My code uses [constant-time conditional swaps instead of branches](https://github.com/soatok/constant-time-js/blob/48a47c3b287e86989c6d24edd164aec39aec2358/lib/bignum.ts#L141-L184) and [peasant multiplication](https://github.com/soatok/constant-time-js/blob/48a47c3b287e86989c6d24edd164aec39aec2358/lib/bignum.ts#L215-L240) (which side-steps [variable time multiplication opcodes](https://www.bearssl.org/ctmul.html) on some architectures).  
It also [avoids touching the high bit of JavaScript numbers](https://github.com/soatok/constant-time-js/blob/48a47c3b287e86989c6d24edd164aec39aec2358/lib/int32.ts), which the v8 engine uses to store a flag and would create a memory access timing leak.

This can serve as a reference implementation for recommending patch strategies to JSBN.

# Disclosure Timeline

  * **2022-04-08** : Reported to the [Xfinity Open Source](https://bugcrowd.com/xfinity-opensource) program on Bugcrowd, which advertises jsbn as "in scope".

  * **2022-04-10** : Bugcrowd employee closes as "not applicable" because I didn't write an exploit.

  * For a bit of background: I am not an exploit developer, and it would probably take me hundreds of hours of research and education to pull off the most basic exploit demo that works against any JavaScript engine with significant market share. That's not a good use of my time, especially since that's the barrier put in place to get Bugcrowd's triage team to take a report seriously.
  * **2022-04-10** : I push back on this unrealistic hurdle towards the report being even looked at by Xfinity's team. I request disclosure, arguing, "If it's not applicable, there's logically no harm in disclosure."

  * **2022-04-10** : Bugcrowd employee agrees to check with the team and update the ticket.

  * **2022-05-06** : Comcast PSIRT says they've informed Andy of the details.

  * **2022-06-14** : Comcast PSIRT says they still haven't heard back from Andy, and denied my disclosure request.

> Since we don't author or maintain this code, we do not have any authority to grant a disclosure request. However you might be able to engage with them on the repository, or develope a further PoC that would enable validation of your claims.

  * **2022-06-14** : Immediate public disclosure on GitHub issue tracker.

Reactions are currently unavailable

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

No labels

No labels

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

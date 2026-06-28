---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-20_sha-3-buffer-overflow.md
original_filename: 2022-10-20_sha-3-buffer-overflow.md
title: SHA-3 Buffer Overflow
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: dd497c7241b640bf47835f5c4d234bba6b2fb992e51837f6a262b15b66704816
text_sha256: e24fb294ef1ff1e899f8e6af6009e279f1eff81907b9d78f2b8f9e9726c87717
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# SHA-3 Buffer Overflow

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-20_sha-3-buffer-overflow.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `dd497c7241b640bf47835f5c4d234bba6b2fb992e51837f6a262b15b66704816`
- Text SHA256: `e24fb294ef1ff1e899f8e6af6009e279f1eff81907b9d78f2b8f9e9726c87717`


## Content

---
title: "SHA-3 Buffer Overflow"
page_title: "SHA-3 Buffer Overflow – Nicky Mouha"
url: "https://mouha.be/sha-3-buffer-overflow/"
final_url: "https://mouha.be/sha-3-buffer-overflow/"
authors: ["Nicky Mouha"]
programs: ["XKCP", "Apple", "Python", "PHP", "PyPy", "SHA3 for Ruby"]
bugs: ["Buffer Overflow", "Memory corruption", "Cryptographic issues"]
publication_date: "2022-10-20"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 2012
---

**Update:** This result appeared in the proceedings of CT-RSA 2023. A [preprint](https://eprint.iacr.org/2023/331.pdf) is available.

Over the past few months, I’ve been coordinating the disclosure of a new vulnerability that I’ve found. Today is the disclosure date, so I am excited that I can finally talk about what I’ve been working on! The vulnerability has been assigned [CVE-2022-37454](https://nvd.nist.gov/vuln/detail/CVE-2022-37454) and bug reports are available for [Python](https://github.com/python/cpython/issues/98517), [PHP](https://bugs.php.net/bug.php?id=81738), [PyPy](https://foss.heptapod.net/pypy/pypy/-/commit/860b897b2611a4099ef9c63ce848fdec89c74b31), [pysha3](https://github.com/tiran/pysha3/issues/29), [SHA3 for Ruby](https://github.com/johanns/sha3/issues/17), and [XKCP](https://github.com/XKCP/XKCP/security/advisories/GHSA-6w4m-2xhg-2658).

The vulnerability impacts the [eXtended Keccak Code Package (XKCP)](https://github.com/XKCP/XKCP), which is the “official” [SHA-3](https://csrc.nist.gov/projects/hash-functions/sha-3-project) implementation by its designers. It also impacts various projects that have incorporated this code, such as the [Python](https://www.python.org/) and [PHP](https://www.php.net/) scripting languages.

Perhaps the best way to introduce the vulnerability is to give a short proof of concept.

On an older (vulnerable) implementation, the following Python script will generate a segmentation fault:
  
  
  import hashlib
  h = hashlib.sha3_224()
  h.update(b"\x00" * 1)
  h.update(b"\x00" * 4294967295)
  print(h.hexdigest())

And the same code in PHP is as follows:
  
  
  <?php
  $ctx = hash_init("sha3-224");
  hash_update($ctx, str_repeat("\x00", 1));
  hash_update($ctx, str_repeat("\x00", 4294967295));
  echo hash_final($ctx);
  ?>

(The scripts use quite a bit of memory, so it may happen that the Out Of Memory (OOM) killer will terminate the process.)

The reason for the segmentation fault is that the scripts will attempt to write more data to a buffer than it can hold. Such a vulnerability is known as a [buffer overflow](https://en.wikipedia.org/wiki/Buffer_overflow), which [OWASP](https://owasp.org/) describes as “[probably the best-known form of software security vulnerability](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow).”

A small variant of the code will cause an infinite loop: just replace 4294967295 with 4294967296. Note the similarity with [CVE-2019-8741](https://nvd.nist.gov/vuln/detail/CVE-2019-8741), another vulnerability that I found that affected the firmware of over 1.4 billion Apple devices, which also caused an infinite loop.

This type of behavior is not supposed to happen for “safe” languages such as Python and PHP, as they check that all read and write operations are within the bounds of the buffer. However, the problem is that the vulnerability is present in the underlying “unsafe” C language…

I’ve shown how this vulnerability in XKCP can be used to violate the [cryptographic properties of the hash function](https://cacr.uwaterloo.ca/hac/about/chap9.pdf) to create preimages, second preimages, and collisions. Moreover, I’ve also shown how a specially constructed file can result in arbitrary code execution, and the vulnerability can also impact signature verification algorithms such as [Ed448](https://csrc.nist.gov/publications/detail/fips/186/5/draft) that require the use of SHA-3. The details of these attacks will be made public at a later date. 

The vulnerable code was released in January 2011, so it took well over a decade for this vulnerability to be found. It appears to be difficult to find vulnerabilities in cryptographic implementations, even though they play a critical role in the overall security of a system. (Perhaps people are not even looking for such vulnerabilities, as neither this vulnerability in XKCP nor the [Apple vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2019-8741) mentioned earlier are eligible for any bug bounty program!)

So this is just the beginning… Expect more to come as soon as I can disclose other vulnerabilities that I’ve found!

For comments or questions, feel free to send me an email: 

SHA-3 Buffer Overflow

[nicky](https://mouha.be/author/nicky/) [October 20, 2022May 25, 2023](https://mouha.be/sha-3-buffer-overflow/ "09:48") [Vulnerabilities](https://mouha.be/category/vulnerabilities/)

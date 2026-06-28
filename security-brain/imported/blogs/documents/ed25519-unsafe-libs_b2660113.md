---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-11_ed25519-unsafe-libs.md
original_filename: 2022-06-11_ed25519-unsafe-libs.md
title: ed25519-unsafe-libs
category: documents
detected_topics:
- jwt
- idor
- command-injection
- mfa
- api-security
- cloud-security
tags:
- imported
- documents
- jwt
- idor
- command-injection
- mfa
- api-security
- cloud-security
language: en
raw_sha256: b2660113ce34d0450641af36d6d4b1702013ab135feeb0788ffe6023400489de
text_sha256: 349d749dbe18c73b954da4a758eaac3bdfa7bfba6084e5878b29d2bac6e40c71
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# ed25519-unsafe-libs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-11_ed25519-unsafe-libs.md
- Source Type: markdown
- Detected Topics: jwt, idor, command-injection, mfa, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `b2660113ce34d0450641af36d6d4b1702013ab135feeb0788ffe6023400489de`
- Text SHA256: `349d749dbe18c73b954da4a758eaac3bdfa7bfba6084e5878b29d2bac6e40c71`


## Content

---
title: "ed25519-unsafe-libs"
page_title: "GitHub - MystenLabs/ed25519-unsafe-libs: List of unsafe ed25519 signature libs · GitHub"
url: "https://github.com/MystenLabs/ed25519-unsafe-libs"
final_url: "https://github.com/MystenLabs/ed25519-unsafe-libs"
authors: ["Konstantinos Chalkias"]
bugs: ["Cryptographic issues"]
publication_date: "2022-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2569
---

# ed25519-unsafe-libs

### Double Public Key Signing Function Oracle Attack on Ed25519

A list of potentially unsafe ed25519 signature libraries that allow a public api where secret and public key can be provided independently as signing function inputs. Misuse of these public apis can result to private key exposure.

Μost of the repositories in our analysis are enlisted in [IANIX :: Things that use Ed25519](https://ianix.com/pub/ed25519-deployment.html).

Number of impacted libraries: 45  
Number of libraries that fixed the issue after the announcement: 8  
_last updated: May 04, 2023_

## Proof of Concept implementations that demonstrate this potential exploit:

  * Rust: [ed25519-chalkias-exploit](https://github.com/MystenLabs/ed25519-unsafe-libs/tree/main/ed25519-chalkias-exploit)
  * Python: [Ed25519 Vulnerability in Python](https://asecuritysite.com/eddsa/ed03), _Buchanan, William J (2022). Ed25519 Vulnerability in Python (Recovering Private Key). Asecuritysite.com._

## Talks:

  * Invited talk to USA's National Institute of Standards and Technology (NIST) Crypto Reading Club: [slides - Taming the Many EdDSAs](https://csrc.nist.gov/csrc/media/Presentations/2023/crclub-2023-03-08/images-media/20230308-crypto-club-slides--taming-the-many-EdDSAs.pdf) (pages 28-39), _Konstantinos Chalkias, François Garillot, Valeria Nikolaenko (2023). Taming the Many EdDSAs & Ed25519 Signing Attacks._

## News and social network coverage of this attack

  * [NIST Crypto Reading Club](https://csrc.nist.gov/presentations/2023/crclub-2023-03-08) "Taming the Many EdDSAs" _(March 08, 2023)_
  * [The Daily Swig](https://portswigger.net/daily-swig/dozens-of-cryptography-libraries-vulnerable-to-private-key-theft) "Dozens of cryptography libraries vulnerable to private key theft" _(June 28, 2022)_
  * [Risky Biz News](https://riskybiznews.substack.com/p/risky-biz-news-hackers-hit-iranian#%C2%A7vulnerabilities-and-bug-bounty) "New crypto vulnerability: Tens of cryptography libraries have misimplemented the Ed25519 digital signature algorithm" _(June 28, 2022)_
  * [SafeHeron blogpost](https://blog.safeheron.com/blog/safeheron-originals/analysis-on-ed25519-use-risks-your-wallet-private-key-can-be-stolen) "Analysis on Ed25519 Use Risks: Your Wallet Private Key Can Be Stolen" _(June 17, 2022)_
  * [kryptera.se](https://kryptera.se/sarbarhet-i-flertalet-ed25519-bibliotek) "Vulnerability in most ed25519 libraries" (in Swedish) _(June 29, 2022)_
  * [Difesa e Sicurezza](https://www.difesaesicurezza.com/cyber/cybersecurity-importante-vulnerabilita-sulle-librerie-ed25519/) & [Yoroi](https://yoroi.company/warning/librerie-crittografiche-ed25519-potenzialmente-non-sicure) "Librerie crittografiche ed25519 potenzialmente non sicure" (in Italian) _(July 1 & June 29, 2022)_
  * [Medium post by Prof Bill Buchanan OBE](https://medium.com/asecuritysite-when-bob-met-alice/ed25519-is-great-but-9f75eab65f) "Ed25519 is Great, But ..." _(July 1, 2022)_
  * [Reddit r/crypto](https://www.reddit.com/r/crypto/comments/vfl2se/initial_impact_report_about_this_weeks_eddsa/) _(best post of the month - June 18, 2022)_
  * [Reddit r/cryptography](https://www.reddit.com/r/cryptography/comments/vextlk/40_unsafe_ed25519_libs_where_private_key_can_be/) _(June 17, 2022)_
  * Interesting tweets: 
  * [tweet 1](https://twitter.com/kostascrypto/status/1535579208960790528) (by Kostas Kryptos - "The original 26 vulnerable libs")
  * [tweet 2](https://twitter.com/kostascrypto/status/1538351278413058048) (by Kostas Kryptos - "Aftermath of the 40 vulnerable libs")
  * [tweet 3](https://twitter.com/campuscodi/status/1541927414648827905) (by Catalin Cimpanu - "40 cryptography libraries are impacted by same Ed25519 misimplementation")
  * [tweet 4](https://twitter.com/kennyog/status/1538768590404452353) (by Kenny Paterson - "Potential for widespread EdDSA private key recovery, cf. <http://kopenpgp.com> where same vector exploited in OpenPGP libs")
  * [tweet 5](https://twitter.com/EllipticKiwi/status/1538632666571894784) (by Steven Galbraith - "A hazard for deterministic signatures: better check it is the correct public key!")
  * [tweet 6](https://twitter.com/riyazdf/status/1538352392164364288) (by Riyaz Faizullabhoy - "If you’re using EdDSA in prod please take a look")
  * [tweet 7](https://twitter.com/bpreneel1/status/1542065725174587397) (by Bart Preneel - "Reminder that implementing cryptographic algorithms securely and correctly is hard").
  * CTF (capture the flag) challenges that feature this attack: 
  * [ImaginaryCTF - JWT25519 (200pts)](https://imaginaryctf.org/ArchivedChallenges/30) _(June 30, 2022)_

## What is the issue?

Note that normally and according to the related [rfc8032](https://datatracker.ietf.org/doc/html/rfc8032), EdDSA signatures are deterministic, and thus for the same input message to be signed, a unique signature output that includes two elements, a curve point `R` and a scalar `S`, is returned.

An algorithmic detail is that that signer's public key is involved in the deterministic computation of the `S` part of the signature only, but not in the `R` value. The latter implies that if an adversary could somehow use the signing function as an Oracle (that expects arbitrary public keys as inputs), then it is possible that for the same message one can get two signatures sharing the same `R` and only differ on the `S` part. Unfortunately, when this happens, one can easily extract the private key; this [StackOverflow post](https://crypto.stackexchange.com/questions/13129) post explains why this is feasible.

That said, public apis should NOT allow a decoupled private/public key-pair as signing input. To circumvent that, many implementations store the public key along with the private key (or seed) and consider the whole keypair as the secret OR they always re-derive the public key inside the signing function. Unfortunately, a large number of existing libraries fail to address this issue by allowing arbitrary public keys as inputs without checking if the input public key corresponds to the input private key.

_Of course, this does not mean that all applications with dependencies to these libraries are prone to key exposure attacks; actually, most are probably safe due to usually not publicly exposing the affected api to their users and coupling their pub/priv key pair just before the`sign` invocation. On the other hand, even when these apis are not exposed, there are applications with different TCB threat model strategies on how the private and public keys are managed and stored. That said, to prevent this attack, developers should also enforce an integrity protection protocol for the public keys as well._

Here, we enlist some affected libraries along with the related code-references.

[![Ed25519 api misuse resulting to key extraction](/MystenLabs/ed25519-unsafe-libs/raw/main/dalek_api_misuse.jpg?raw=true)](/MystenLabs/ed25519-unsafe-libs/blob/main/dalek_api_misuse.jpg?raw=true) Fig 1. An example api misuse in the ed25519-dalek Rust crate.

## Affected libraries

  * C: OpenGNB  
<https://github.com/gnbdev/opengnb/blob/master/libs/ed25519/sign.c#L7>

  * C: GNU Nettle  
<https://github.com/gnutls/nettle/blob/fe7ae87d1b837e82f7c7968b068bca7d853a4cec/ed25519-sha512-sign.c#L43>

  * ASM/C: iroha-ed25519 (Hyperledger Project)  
<https://github.com/hyperledger/iroha-ed25519/blob/main/lib/ed25519/ref10/ed25519.c#L27> and <https://github.com/hyperledger/iroha-ed25519/blob/main/lib/ed25519/amd64-64-24k-pic/ed25519.c#L30>

  * C: ed25519-donna (Andrew Moon)  
<https://github.com/floodyberry/ed25519-donna/blob/master/ed25519.c#L59>

  * C: ed25519 (Orson Peters)  
<https://github.com/orlp/ed25519/blob/master/src/sign.c#L7>

  * C: libbrine (Kevin Smith)  
<https://github.com/kevsmith/libbrine/blob/master/src/ed25519/sign.c#L7>

  * C++: Ed25519 (ArduinoLibs)  
<https://rweather.github.io/arduinolibs/classEd25519.html#a36ecf67b4c5d2d39a31888f56af1f8a5>

  * C#: ed25519 (Hans Wolff)  
<https://github.com/hanswolff/ed25519/blob/master/Ed25519/Ed25519.cs#L146>

  * C#: Ed25519 (CryptoManiac)  
<https://github.com/CryptoManiac/Ed25519/blob/972829ac688847895d5105f19ca1e5777131b421/Chaos.NaCl/Internal/Ed25519Ref10/keypair.cs#L7>

  * Dart: ed25519_dart (Oleksii Semeshchuk)  
<https://github.com/semolex/ed25519_dart/blob/master/lib/src/ed25519_dart_base.dart#L200>

  * Dart: riclava_ed25519 (riclava)  
<https://github.com/riclava/ed25519/blob/master/lib/ed25519.dart#L125>

  * Clojure: ed25519 (Kevin Downey)  
<https://github.com/hiredman/ed25519/blob/master/src/ed25519/core.clj#L168>

  * Haskell: hs-scraps (Vincent Hanquez)  
<https://github.com/vincenthz/hs-scraps/blob/master/Crypto/Signature/Ed25519.hs#L115>

  * Java: ed25519-java (k3d3)  
<https://github.com/k3d3/ed25519-java/blob/master/ed25519.java#L144>

  * Java: ed25519 (Bjorn Arnelid)  
<https://github.com/BjornArnelid/ed25519/blob/master/src/ed25519/application/Ed25519.java#L32>

  * Java: Punisher.NaCl (Arpan Jati)  
<https://github.com/arpanj/Punisher.NaCl/blob/c9619ca3028b90d0556c0473e4eba1d429a3744c/Punisher.NaCl/src/Punisher/NaCl/Ed25519Operations.java#L72>

  * Java: ED25519 (Mick Michalski)  
<https://github.com/michami/ED25519/blob/master/ED25519.java#L60>

  * Java: vRallev/ECC-25519 (Ralf Wondratschek)  
<https://github.com/vRallev/ECC-25519/blob/master/ECC-25519-Java/src/main/java/net/vrallev/java/ecc/Ecc25519Helper.java#L102>

  * Perl: Crypt::Ed25519 (Marc Lehmann)  
<https://metacpan.org/release/MLEHMANN/Crypt-Ed25519-0.9/view/Ed25519.pm#$signature-=-Crypt::Ed25519::sign-$message,-$public_key,-$private_key>

  * Python: ed25519.py (Ed25519 authors)  
<https://ed25519.cr.yp.to/python/ed25519.py>

  * Python: ed25519 (Python Cryptographic Authority)  
<https://github.com/pyca/ed25519/blob/main/ed25519.py#L243> (_authors mention it’s unsafe against side channels anyway_)

  * Python: python-pure25519 (Brian Warner)  
<https://github.com/warner/python-pure25519/blob/master/pure25519/eddsa.py#L21>

  * Python: nmed25519 (naturalmessage)  
<https://github.com/naturalmessage/nmed25519/blob/master/nmed25519.py#L150>

  * Python: ed25519.py (Shiho Midorikawa)  
<https://gist.github.com/elliptic-shiho/f41fd75cc30646a61d7ad63043fdd56e#file-ed25519-py-L77>

  * Python: bindings for ed25519-dalek: py-ed25519-bindings  
<https://github.com/polkascan/py-ed25519-bindings/blob/master/src/lib.rs#L111>

  * Swift: ed25519swift (pebble8888)  
<https://github.com/pebble8888/ed25519swift/blob/master/Ed25519ref/ed25519s.swift#L120>

  * JS: supercop.js (1p6 Flynx)  
<https://github.com/1p6/supercop.js/blob/master/index.js#L29>

  * JS: substack/ed25519-supercop (James Halliday)  
<https://github.com/substack/ed25519-supercop/blob/master/index.js#L3>

  * C: libeddsa (Philipp Lay)  
<https://github.com/phlay/libeddsa/blob/master/lib/ed25519-sha512.c#L85>

  * C#: SommerEngineering/Ed25519 (Thorsten Sommer)  
<https://github.com/SommerEngineering/Ed25519/blob/master/Ed25519/Signer.cs#L80>

  * CUDA: ChorusOne/solanity  
<https://github.com/ChorusOne/solanity/blob/master/src/cuda-ecc-ed25519/sign.cu#L10>

  * C: ncme/c25519 (Daniel Beer and Nikolas Rösener)  
<https://github.com/ncme/c25519/blob/master/src/edsign.c#L115>

  * C: luazen (Phil Leblanc)  
<https://github.com/philanc/luazen/blob/master/src/x25519.c#L508> (_authors modified the function to accept pk instead of the original nacl 64-byte sk which includes pk as the last 32 bytes_)

  * C++: amber (Pelayo Bernedo)  
<https://github.com/bernedogit/amber/blob/master/src/group25519.cpp#L1661>

  * C: FLD ECC AVX2 (Armando Faz-Hern'{a}ndez and Julio L'{o}pez and Ricardo Dahab)  
<https://github.com/armfazh/fld-ecc-vec/blob/master/src/sign255.c#L391>

  * Elixir: mwmiller/ed25519_ex (Matt Miller)  
<https://github.com/mwmiller/ed25519_ex/blob/master/lib/ed25519.ex#L146>(_Public key is optional. Per author's comment: if only the secret key is provided, the public key will be derived therefrom. This adds significant overhead_)

  * PHP (C wrapper): php-ed25519-ext  
<https://github.com/encedo/php-ed25519-ext/blob/master/ed25519-ext.c#L93>

  * Nim: niv/ed25519.nim (Bernhard Stöckner)  
<https://github.com/niv/ed25519.nim/blob/master/ed25519.nim#L26>

  * Typescript: mipher (Marco Paland)  
<https://github.com/mpaland/mipher/blob/master/src/x25519.ts#L936>

  * Lua: LuaMonocypher  
<https://github.com/philanc/luamonocypher/blob/main/src/luamonocypher.c#L268>

  * Crystal: monocypher.cr  
<https://github.com/konovod/monocypher.cr/blob/master/src/monocypher.cr#L39>

  * Python: py_ssh_keygen_ed25519 (Péter Szabó)  
<https://github.com/pts/py_ssh_keygen_ed25519/blob/master/ed25519_compact.py#L128> (_Public key is optional_)

  * Javascript: KinomaJS  
<https://github.com/Kinoma/kinomajs/blob/701879d37e7fe5001420e0053cd60df6b91e4553/xs6/extensions/crypt/crypt_ed25519.js#L92> (_Public key is optional_)

  * Haskell: gen-ed25-keypair  
<https://github.com/awakesecurity/gen-ed25-keypair>

  * C: horse25519 (Yawning Angel)  
<https://github.com/Yawning/horse25519/blob/master/src/ref10/sign.c#L7> _Note: This repo includes a copy of djb's ref10 ed25519 implementation lifted from supercop to avoid pulling in another dependency, but the intention is to provide a standalone executable that does ed25519 vanity keypair generation. While it does use the API in an odd way, this is intentional as it's already doing something extremely exotic and unusual with respect to key generation and the lib is not meant to be used for signing._

## Fixed libraries

  * C: Trezor firmware  
Fixed in this PR: [trezor/trezor-firmware#2349](https://github.com/trezor/trezor-firmware/pull/2349) _(Fix merged on June 27, 2022)_

  * Java: ed25519-elisabeth (Jack Grigg)  
Fixed in this commit: <https://github.com/cryptography-cafe/ed25519-elisabeth/commit/49545ce47d550fed807522dff86546c812ccbbac> _(Fix merged on June 19, 2022)_

  * C: Harbour (Viktor Szakats)  
Fixed in this commit: <https://github.com/vszakats/hb/commit/bae610b63d35c6c1793d94a3bf9467c3b1eded18> _(Fix merged on June 30, 2022)_

  * Rust/Wasm: polkadot-js/wasm  
Fixed in this PR: <https://github.com/polkadot-js/wasm/pull/381/files> _(Fix merged on July 3, 2022)_

  * C: horse25519 (Yawning Angel)  
Fixed in this PR: [Yawning/horse25519#3](https://github.com/Yawning/horse25519/pull/3) _(Fix merged on August 15, 2022)_

  * Erlang: erlang-libdecaf  
Fixed in this commit: <https://github.com/potatosalad/erlang-libdecaf/commit/16ba07ea122660e95f6cfa9107e28ed58bada713>. Logic addressed in this issue: [ed25519-unsafe-libs/issues/7](https://github.com/MystenLabs/ed25519-unsafe-libs/issues/7) _(Fix merged on August 28, 2022)_

  * Rust: ed25519-dalek (Isis Agora Lovecruft)  
Fixed in this PR: [dalek-cryptography/ed25519-dalek#205](https://github.com/dalek-cryptography/ed25519-dalek/pull/205) _(Fix merged on October 22, 2022)_

  * C: Monocypher (Loup Vaillant)  
Fixed in this commit: <https://github.com/LoupVaillant/Monocypher/commit/da7b5407d20329f21a53ea993f516fb55e2f5e26> _(Fix merged on February 27, 2023)_

## False Positives (probably safe)

Libraries originally reported as vulnerable, but removed from the list based on community feedback.

  * Go: threshold-ed25519 — Threshold Signatures using Ed25519  
<https://gitlab.com/unit410/threshold-ed25519/-/blob/main/pkg/ed25519.go#L161> -> see report [#9](https://github.com/MystenLabs/ed25519-unsafe-libs/pull/9) _(reported on Oct 27, 2022 by nitronit)_

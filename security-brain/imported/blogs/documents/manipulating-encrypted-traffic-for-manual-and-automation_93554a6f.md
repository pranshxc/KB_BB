---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_manipulating-encrypted-traffic-for-manual-and-automation.md
original_filename: 2023-03-06_manipulating-encrypted-traffic-for-manual-and-automation.md
title: Manipulating Encrypted Traffic for Manual and Automation
category: documents
detected_topics:
- rate-limit
- automation-abuse
- command-injection
- otp
- mobile-security
- supply-chain
tags:
- imported
- documents
- rate-limit
- automation-abuse
- command-injection
- otp
- mobile-security
- supply-chain
language: en
raw_sha256: 93554a6f7ded25e61519bfb29a9c14646d1b89d264cfbc82b0f0e4713e6c8325
text_sha256: 5459c11869eee842150e8fda6e19864f19d470c0f455b404d2541bea6fb20c2b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Manipulating Encrypted Traffic for Manual and Automation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_manipulating-encrypted-traffic-for-manual-and-automation.md
- Source Type: markdown
- Detected Topics: rate-limit, automation-abuse, command-injection, otp, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `93554a6f7ded25e61519bfb29a9c14646d1b89d264cfbc82b0f0e4713e6c8325`
- Text SHA256: `5459c11869eee842150e8fda6e19864f19d470c0f455b404d2541bea6fb20c2b`


## Content

---
title: "Manipulating Encrypted Traffic for Manual and Automation"
url: "https://medium.com/@Ano_F_/manipulating-encrypted-traffic-using-pycript-b637612528bb"
authors: ["Sourav Kalal (@Ano_F_)"]
bugs: ["Client-side encryption bypass", "Bruteforce"]
publication_date: "2023-03-06"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1419
scraped_via: "browseros"
---

# Manipulating Encrypted Traffic for Manual and Automation

Manipulating Encrypted Traffic for Manual and Automation
Sourav Kalal
Follow
7 min read
·
Mar 6, 2023

62

Press enter or click to view image in full size
Introduction

I have been doing the pentest of mobile and web applications and recently I found that many applications are implementing client-side encryption in both mobile and web applications. Earlier I hosted a simple Javascript-based AES encryption and decryption script on GitHub. The script allows me to encrypt and decrypt the parameter to continue testing. The script was created after I found that many applications use the CryptoJS library with AES CBC 256 or 128-bit encryption.

The same method could be applied by writing the same encryption logic as your application. As or alternative method we can use the browser console and breakpoint in web applications and JavaScript-based mobile applications.

Problem

The problem with the above method is you need to perform the encryption and decryption for each parameter or request again and again. This approach slows down the testing process and the time taken to complete the pentesting. Another problem is many time application is vulnerable and requires any type of automation to exploit it like OTP brute-force. If encryption is there it's not possible to perform any kind of automation.

A few months back I was pentesting a web application vulnerable to OTP brute force and due to encryption, I was not able to perform the brute force. I came up with the solution of writing a simple python script that will go through the text file with 4-digit OTP and will create a new text file with an encrypted version of the OTP. I could use the encrypted OTP to bypass the OTP. I create several burp extensions to perform the encryption especially to run automation like an intruder or SQLMAP.

The major problem was modifying the burp suite extension based on the parameter and encryption logic used by the application. Also, the one problem with manually decrypting and encrypting parameters is it takes a lot of time.

Solution

I came up with the idea of creating a new burp suite extension that works on all the applications and allows you to just provide the encryption and decryption logic and the extension will take care of everything whether is manual pentesting or automation.

I created an extension named PyCript that solves all the problems. The extension decrypts the encrypted parameters on the fly and allows you to modify the value in the plain text directly inside the burp suite. This solves the problem of manually encrypting and decrypting each parameter and request again and again and we can test the application as there is no encryption.

I also added functionality that allows running automation on plain text requests and the extension will take care of encryption. This solves the challenge of running the tools like SQLMAP, Intruder or Burp Scanner.

Analysis

I have one of the applications I am working on and by intercepting the traffic I can confirm that the request is using some kind of client-side encryption.

Press enter or click to view image in full size
Encrypted Request

The post body seems to have some kind of encryption and won’t allow us to perform any attacks on parameters. At this stage, I try to find out the encryption logic including key and iv from the Javascript code.

Get Sourav Kalal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Using the browser dev tool and searching for some strings like aes,encrypt,cryptojs,secretkey,iv,padding I can see the encryption logic.

Press enter or click to view image in full size
Encryption

The search result shows that it uses AES encryption using the CryptoJS library. The result shows that it has two different encryption codes. By clicking on both files I can verify that the encryption logic is the same for both.

Press enter or click to view image in full size
Encryption JS Code
Press enter or click to view image in full size
Encryption Code

As mentioned I have hosted the Cryptojs-based encryption decryption script on GitHub. Using the provided key and IV from the above code I can decrypt the request parameters.

Press enter or click to view image in full size
Decrypt
PyCript and Decryption

Now I am able to confirm that I can decrypt the encrypted strings. Now I can use the same encryption logic to write the encryption and decryption script in PyCript format.

//Decryption 
var CryptoJS = require("crypto-js");
const program = require("commander");
const {
  Buffer
} = require('buffer');
program.option("-d, --data <data>", "Data to process").parse(process.argv);
const options = program.opts();
const requestbody = Buffer.from(options.data, 'base64').toString('utf8');
var key = CryptoJS.enc.Utf8.parse('8080808080808080');
var iv = CryptoJS.enc.Utf8.parse('8080808080808080');
var plainText = CryptoJS.AES.decrypt(requestbody, key, {
  keySize: 128 / 8,
  iv: iv,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
});
console.log(plainText.toString(CryptoJS.enc.Utf8))
//Encryption
var CryptoJS = require("crypto-js");
const program = require("commander");
const {
  Buffer
} = require('buffer');
program.option("-d, --data <data>", "Data to process").parse(process.argv);
const options = program.opts();
const requestbody = Buffer.from(options.data, 'base64').toString('utf8');
var key = CryptoJS.enc.Utf8.parse('8080808080808080');
var iv = CryptoJS.enc.Utf8.parse('8080808080808080');
var encryptedclientDetail = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(requestbody), key, {
  keySize: 128 / 8,
  iv: iv,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
});
console.log(encryptedclientDetail.toString())

Now I have the encryption and decryption script ready and I can use the script inside the PyCript extension to modify the traffic same as a normal application. In my case, the body is in JSON format and only the value is encrypted I can select the appropriate request type in the extension.

Press enter or click to view image in full size
PyCript

Now the setup is completed I can go back to the request in my burp suite and can see a new tab in the request section named PyCript and it shows the decrypted data. I can modify the data directly inside the tab and can send the modified request and the extension will take care of encryption for modified data.

Press enter or click to view image in full size
PyCript Request

The problem with the tab is in many cases you need to see the complete request, not just the body and also want to test the application like there is no encryption at all.

For the same, I can right-click on the request and select the Decrypt Request from the PyCript.

Press enter or click to view image in full size
Decrypt Request

Once I do that extension will store the decrypted request inside the table. I can send that request to the repeater intruder scanner etc to test the request the same as a normal app and it won't require me to edit the request from the PyCript tab. I can directly edit the request in the Raw or the pretty tab.

Press enter or click to view image in full size
Decrypted Request

But since the extension will only encrypt the request if I modify the data from PyCript, not from Raw or Pretty tab. I can go back to the config tab within the PyCript extension.

Press enter or click to view image in full size
Auto Encrypt

I can turn on Auto Encrypt and select the tool in my case repeater I will select the repeater. This will allow the extension to encrypt the request and then send it to the server. I can now use the plain text request for scanners or intruders etc and the extension will handle the encryption in the background.

Press enter or click to view image in full size
Auto Encrypt

If I go back to the repeater tab. I can use the plain text request like there is no encryption at all and the extension will handle everything for me. If I want to run the SQLMAP I can give this plain text request to the SQLMAP. and can use the proxy option īnsde the SQLMAP to send all the requests to the burp proxy from the PyCript I can select the proxy for Auto Encrypt.

All the tools can be found below.

GitHub - Anof-cyber/PyCript: Burp Suite extension that allows for bypassing client-side encryption…
Burp Suite extension that allows for bypassing client-side encryption using custom logic for manual and automation…

github.com

GitHub - Anof-cyber/PyCript-Template: Encryption and Decryption code for Pycript Extensions with…
Encryption and Decryption code for Pycript Extensions with common JavaScript encryption logic - GitHub …

github.com

CryptoJS - AnoF
Edit description

souravkalal.tech

Twitter — https://twitter.com/ano_f_

GitHub — https://github.com/Anof-cyber/

Linkedin — https://www.linkedin.com/in/sourav-kalal/

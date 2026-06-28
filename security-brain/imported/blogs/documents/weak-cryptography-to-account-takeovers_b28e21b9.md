---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-15_weak-cryptography-to-account-takeovers.md
original_filename: 2020-11-15_weak-cryptography-to-account-takeovers.md
title: Weak Cryptography to Account Takeover’s
category: documents
detected_topics:
- oauth
- sso
- idor
- access-control
- command-injection
- password-reset
tags:
- imported
- documents
- oauth
- sso
- idor
- access-control
- command-injection
- password-reset
language: en
raw_sha256: b28e21b95ce676536b0a8d342d70e81eecc6fb66a3dd082f695f3f841e38d39c
text_sha256: bf247865b1eaef8421db25e0ce4465b352d0b86752872e2c48c9bf9b28c1f687
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Weak Cryptography to Account Takeover’s

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-15_weak-cryptography-to-account-takeovers.md
- Source Type: markdown
- Detected Topics: oauth, sso, idor, access-control, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b28e21b95ce676536b0a8d342d70e81eecc6fb66a3dd082f695f3f841e38d39c`
- Text SHA256: `bf247865b1eaef8421db25e0ce4465b352d0b86752872e2c48c9bf9b28c1f687`


## Content

---
title: "Weak Cryptography to Account Takeover’s"
url: "https://medium.com/@vasuyadav0786/weak-cryptography-to-account-takeovers-87782224ed0d"
authors: ["letmeslidein (@VasuYadaav)"]
bugs: ["Cryptographic issues", "Account takeover", "IDOR"]
publication_date: "2020-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4131
scraped_via: "browseros"
---

# Weak Cryptography to Account Takeover’s

Weak Cryptography to Account Takeover’s
Vasuyadav
Follow
4 min read
·
Nov 15, 2020

348

1

Good day, everyone!

In this article, I’ll discuss some of my discoveries that were made possible by weak cryptography, resulting in account takeovers.
Before we get started, I’d like to ask that you leave a like and a remark if you learned something.

So first, What is Cryptography?

=>Cryptography is associated with the process of converting ordinary plain text into unintelligible text and vice-versa. It is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it.

Now what is Weak Cryptography?

=>A weak cipher is defined as an encryption/decryption algorithm that uses a key of insufficient length. Using an insufficient length for a key in an encryption/decryption algorithm opens up the possibility (or probability) that the encryption scheme could be broken (i.e. cracked)

So if you follow me or have read my recent write ups then you would have known that how much I love Account Takeover. I was testing an Web application and let’s say its “cantdisclose.com”

I requested password reset for my account and received a link on my email and it looked like this.

Press enter or click to view image in full size

As soon as I saw ‘==’ in the end I thought it may be Base 64, So I copied it and went to decoder and pasted the token and the results were-

Press enter or click to view image in full size

Now if you are not a beginner then you would already know how we can exploit it to generate our own tokens but if you don’t then I am going to explain.

Below are the Steps To Reproduce that I sent in the Report too.

Get Vasuyadav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1.I used my two accounts for this purpose.
1.vasuyadav@gmail.com
2.vasuyadav2@gmail.com

Suppose the 1 one is the attacker’s account and 2 one is the victim’s account.

2.Request Password reset for 1 account and capture it in burp suite.
3.Send it to the intruder and select the email parameter and add the victim’s email. I used it because it sends requests to the server very fast and so that the sent time will be near or same for both accounts.
4.Check the attacker’s account and copy the link.
5.Decode the string as base64 after index/.
6.e.g “senttime/1593586556/token/vasuyadav1@gmail.com”
7.change this with the victim’s email i.e vasuyadav2@gmail.com and sent time let be the same and then “senttime/1593586556/token/vasuyadav2@gmail.com” encode it to base 64 and.
8.The encoded string will be like this “c2VudHRpbWUvMTU5MzU4NjU1Ny90b2tlbi92YXN1eWFCXYxOTg0QGdtYWlsLmNvbQ==” use this to make an valid link.
9.https://www.cantdisclose.com/resetpassword/index/c2VudHRpbWUvMTU5MzU4NjU1Ny90b2tlbi92YXN1eWFkYXYxOTg0QGdtYWlsLmNvbQ==.
10.If this does not work then try changing the sent time by 1 or 2 and do the same process.
11.In my case it worked when I changed sent time by 1 and boom I was able to change the password of my other account without checking the link that was sent on mail.

Now let’s head to the Second finding which was in OAUTH implementation.

I was checking the requests which were being sent while using OAUTH and how authentication is being done and the request looked like this.

Press enter or click to view image in full size

The requests contains a Authorization header and it also using Base 64 and it can be easily decrypted.

Press enter or click to view image in full size

I did the same here i.e by changing the email to my other account email and then encoded it to Base 64 and then simply forwarded that request and I was logged into my other account.

Here is one more write-up from 
Harsh Bothra
 related to the same-”https://medium.com/bugbountywriteup/weak-cryptography-in-password-reset-to-full-account-takeover-fc61c75b36b9"

Thank you for reading. If you liked this write-up, please like, comment or follow me on Twitter/LinkedIn/Medium.

Your support inspires me to write!

If you have any questions, please contact me:

Twitter-”https://twitter.com/VasuYadaav”

Linkedin-”https://www.linkedin.com/in/vasu-yadav-82ba701a0/”

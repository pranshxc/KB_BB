---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-03_manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys.md
original_filename: 2022-12-03_manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys.md
title: Manipulating AES Traffic using a Chain of Proxies and Hardcoded Keys
category: documents
detected_topics:
- mobile-security
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- command-injection
- otp
language: en
raw_sha256: 83fa1b1fab2c906b8e1d708bd732a566859d01656867d0462dc19371564148af
text_sha256: 129de0e1880bba61f09c7adc918ae8ae02361be647cddcac3d954ef61c7fb6ea
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Manipulating AES Traffic using a Chain of Proxies and Hardcoded Keys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-03_manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `83fa1b1fab2c906b8e1d708bd732a566859d01656867d0462dc19371564148af`
- Text SHA256: `129de0e1880bba61f09c7adc918ae8ae02361be647cddcac3d954ef61c7fb6ea`


## Content

---
title: "Manipulating AES Traffic using a Chain of Proxies and Hardcoded Keys"
url: "https://blog.dixitaditya.com/manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys"
final_url: "https://blog.dixitaditya.com/manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys"
authors: ["Aditya Dixit (@zombie007o)"]
bugs: ["Android", "Hardcoded credentials", "Client-side encryption bypass"]
publication_date: "2022-12-03"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1819
---

# Manipulating AES Traffic using a Chain of Proxies and Hardcoded Keys

Intercepting and Manipulating client-side AES encrypted traffic in mobile applications having hardcoded Key and IV

UpdatedDecember 5, 2022

•6 min read•[ __View as Markdown](/manipulating-aes-traffic-using-a-chain-of-proxies-and-hardcoded-keys.md)

![Manipulating AES Traffic using a Chain of Proxies and Hardcoded Keys](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1669990436681%2Fc45bebca-5464-47f1-b154-514cec5565a6.png&w=3840&q=75)

[ A](https://hashnode.com/@adityadixit)

[Aditya Dixit](https://hashnode.com/@adityadixit)

[ __](https://twitter.com/zombie007o)[__](https://www.linkedin.com/in/ad17ya/)

I'm leading the Research at Credshields, and Pentest teams at Cobalt Labs and HackerOne. I occasionally blog about my findings and adventures in pentesting.

On this page

OverviewSource Code AnalysisThe Chained ProxiesThe FlowPython ScriptsMitmproxy-1Mitmproxy-2Everything in ActionMitigations

## Overview

Mobile applications are becoming more resilient to reverse engineering and tampering with all kinds of client and server-side protections, binary hardening, code obfuscations, SSL pinning, etc which makes it that much more difficult for good or bad hackers to dig deeper into these applications.

Let's say the attacker manages to bypass the SSL Pinning and Root detection and using Burp Suite or any intercepting proxy, they are able to monitor all the requests. What are the developers supposed to do in this case to hide their API implementation from end users?

This is where some recent applications have been found encrypting their traffic client-side and sending it to the server where it's decrypted and analyzed. This minimizes the possibility of injections given that proper client-side input validations are implemented in the application. The attacker won't be able to see plaintext traffic in their proxy, and thus, won't be able to modify the endpoints and parameters.

In this article, I'll be talking about one such android application which our team at [CredShields](https://credshields.com) was working on, that was using `AES/CBC/PKCS5Padding` to encrypt its traffic, which was then decrypted on their server, making the traffic completely gibberish to an intercepting proxy, and the technique I used to decrypt and bypass the encryption.

## Source Code Analysis

It was evident from the request that the application was encrypting the request body using some kind of encryption technique and sending it to the server. Here's how a sample request looks:

![Encrypted Sample Request](https://cdn.hashnode.com/res/hashnode/image/upload/v1670003952603/092d6414-525c-45cd-a963-0146ee14ae07.png)

The POST body was in the following format - `data=AESEncryptedData:IV`

So the encryption part was happening somewhere inside the APK. It is generally a good idea to have the application decompiled at this stage to analyze the source code. I use `jadx-gui` for this.

Let's call the app `victim.apk`. While going through the source code I noticed that it was not obfuscated, making my job much easier. I thought about searching for the keyword `encrypt` to look for any functions that are being used for the encryption. There were many results but a particular function caught my eye because it was inside the application's folder itself and the file name (AES) kind of gave it away.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1669998203346/cfebc7e5-e44b-4e94-b42d-895a7babca86.png)

I opened the file `com/victim.app/utils/Java_AES_Cipher` which confirmed my assumptions. It was indeed the code for encrypting and decrypting strings using `AES/CBC/PKCS5Padding` .

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1669999459690/87bf9ad4-214c-46b2-99b3-e910dd998e5c.png)

I won't be going into the details of how the AES encryption works (Google is your friend). From the code, it is clear that the function `encrypt()` is taking 3 string type parameters as arguments. Now to find all the places where the function is used, the shortcut key `x` can be used in `jadx-gui`. This lists out all the instances where the function is called. From the function call, the parameters become clear:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1669999792814/4a46c86a-706b-4ba7-b59a-5aa2b3646d3f.png)

So the `encrypt()` function is using a `key` and an `iv` to encrypt the data inside `jSONObject2`. This data is then sent to the server. The `key` and `iv` are being fetched from the `BaseMethod` class. Now, if you are really lucky, 1/10 times you will find the `key` and `iv` values hardcoded in the APK, as I did inside `com/victim.app/base/BaseMethod`

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1670000070258/aba53ac0-6c03-4336-9de8-5b1683494752.png)

By now, I had all the things I needed to decrypt the traffic. I could even do it manually on this [website](https://www.devglan.com/online-tools/aes-encryption-decryption). But decrypting the traffic, modifying it on my side, and then encrypting it again to send to the server was too much of a hassle. The challenge was automating this part.

## The Chained Proxies

If you're not already familiar with this powerful tool, let me introduce you to [Mitmproxy](https://mitmproxy.org/). This thing can execute python scripts on the ongoing traffic and make changes to the requests dynamically.

For the complete flow to work, I'll be using 3 proxy servers - Mitmproxy-1, Burp, and Mitmproxy-2, which will then forward the request to its final destination.

### The Flow

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1670001267007/a5d10e32-1409-4a49-b086-08b5e6765265.png)

  1. The victim app will send encrypted AES traffic to my Mitmproxy-1.

  2. Mitmproxy-1 will listen to my requests in upstream mode, execute my python script to decrypt AES traffic, and send the plaintext JSON object to Burp.

  3. Burp will see all the traffic as it should, in plaintext where I'll be able to tamper with everything, and once I submit the requests, it'll go to Mitmproxy-2 since Burp will be set to forward all requests to Mitmproxy-2.

  4. Mitmproxy-2 will execute my python script to encrypt the traffic and send it to the application's server and the response returned will be seen in my Burp.

## Python Scripts

### Mitmproxy-1

Mitmproxy-1 will be using the following script to intercept the traffic, decrypt it, and send it to the Burp:
  
  
  from mitmproxy import http
  from urllib.parse import quote, unquote
  from Crypto.Cipher import AES
  from base64 import b64decode
  from Crypto.Util.Padding import pad, unpad
  
  iv = bytes("verysecretkey", 'utf-8')
  key = bytes("verysecretiv", 'utf-8')
  
  def request(flow: http.HTTPFlow) -> None:
  #if host matches the victim
  if flow.request.host == "victim.com":
  post_body = (flow.request.content).decode('utf-8')
  #do voodoo magic to decode the data=AESEncodeddata:IV 
  to_decrypt = unquote(post_body.split("=")[1]).split(":")[0].replace("\n","")
  #send decrypted data
  flow.request.content = decrypt(to_decrypt)
  
  #function to decrypt AES
  def decrypt(message):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  decrypted = unpad(cipher.decrypt(b64decode(message)), AES.block_size)
  return decrypted
  

This script is intercepting the traffic for the domain `victim.com`, splitting the POST data and extracting only the AES-encrypted POST body which is then set as the new content and sent to Burp Suite.

### Mitmproxy-2
  
  
  from mitmproxy import http
  from urllib.parse import quote, unquote
  from Crypto.Cipher import AES
  from base64 import b64encode
  from Crypto.Util.Padding import pad, unpad
  
  #keys
  iv = bytes("verysecretkey", 'utf-8')
  key = bytes("verysecretiv", 'utf-8')
  
  def request(flow: http.HTTPFlow) -> None:
  #if host matches
  if flow.request.host == "victim.com":
  print(flow.request.host)
  post_body = (flow.request.content).decode('utf8')
  #encrypting data coming from Burp
  edata = quote(encrypt(post_body))
  #appending IV to the request as it was originally done 
  prefix = quote(":") + quote(b64encode(iv))
  #final POST body
  to_send = "data=" + edata + prefix
  #send to server
  flow.request.content = bytes(to_send, 'utf-8')
  
  #function to encrypt AES
  def encrypt(message):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  encrypted = cipher.encrypt(pad(message.encode("UTF-8"), AES.block_size))
  return (b64encode(encrypted).decode('utf-8'))
  

This script intercepts the plaintext traffic coming from Burp, extracts the POST body, encrypts it, appends IV, base64 encodes the whole thing, and sends it to the victim server.

## Everything in Action

I started by installing Mitmproxy's SSL certificate on my android device. This process is similar to what you do with Burp Suite. A detailed guide for mitmproxy is available [here](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/howto-install-system-trusted-ca-android.md).

I configured a proxy on my android device to forward all traffic to my device's IP (`192.168.xx.xx`) and port `8080`.

Once that was done, I started my first proxy listener in upstream mode which listens on port `8080` and forwards all traffic to `http://127.0.0.1:7070` using the following command:
  
  
  mitmproxy --mode  upstream:http://127.0.0.1:7070 --ssl-insecure -s mitm_to_burp.py
  

I configured Burp to listen on port `7070` on all interfaces. I also enabled upstream proxy in Burp to forward all traffic to port `8082`:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1670004427669/d06f3aec-4c07-447a-8b71-727b9d9b8391.png) ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1670003337434/0c231a4f-2cf8-42ec-99f6-e206e9f81939.png)

I started another Mitmproxy instance to listen on port `8082` for the traffic coming from Burp with the following command:
  
  
  mitmproxy --listen-port 8082 -s burp_to_mitm.py
  

Now that everything was set up, it was time to initiate a request in the application and verify the flow:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1670003686102/bb27df0a-8a77-4d21-a076-903b36a2fc9f.png)

And it worked. Burp was able to intercept and manipulate the requests successfully and show the response returned by the server.

The whole process could have been done in an efficient way using Burp Suite's Extender API or Frida hooks. Maybe that's a topic for the next part?

## Mitigations

  * DO NOT hardcode sensitive data inside your application as it can easily be decompiled and obtained. Use [Android Keystore API](https://developer.android.com/training/articles/keystore) for storing sensitive keys and tokens.

  * Obfuscate the source code using Proguard or similar tools which will make it difficult for attackers to reverse engineer the code.

  * Have Root detection and SSL Pinning in place

The Python scripts can also be found at:

<https://github.com/az0mb13/hooker>

[#security](/tag/security)[#pentesting](/tag/pentesting)[#java](/tag/java)[#android](/tag/android)[#android-app-development](/tag/android-app-development)

 __8.1K views

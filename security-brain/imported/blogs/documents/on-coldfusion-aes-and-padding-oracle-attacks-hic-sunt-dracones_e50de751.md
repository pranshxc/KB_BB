---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-03_on-coldfusion-aes-and-padding-oracle-attacks-hic-sunt-dracones.md
original_filename: 2023-07-03_on-coldfusion-aes-and-padding-oracle-attacks-hic-sunt-dracones.md
title: 'On ColdFusion, AES, and Padding Oracle Attacks: Hic Sunt Dracones'
category: documents
detected_topics:
- automation-abuse
- sqli
- command-injection
- mfa
- otp
- information-disclosure
tags:
- imported
- documents
- automation-abuse
- sqli
- command-injection
- mfa
- otp
- information-disclosure
language: en
raw_sha256: e50de7511c304722e744d003dc7cf44d8c9ae993e0f45c7a36334a69a5bfd458
text_sha256: 8bef0d54859b10655d1d409d35c8f143f5dced61dbcc4c4da2e467706c6b8a0c
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# On ColdFusion, AES, and Padding Oracle Attacks: Hic Sunt Dracones

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-03_on-coldfusion-aes-and-padding-oracle-attacks-hic-sunt-dracones.md
- Source Type: markdown
- Detected Topics: automation-abuse, sqli, command-injection, mfa, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `e50de7511c304722e744d003dc7cf44d8c9ae993e0f45c7a36334a69a5bfd458`
- Text SHA256: `8bef0d54859b10655d1d409d35c8f143f5dced61dbcc4c4da2e467706c6b8a0c`


## Content

---
title: "On ColdFusion, AES, and Padding Oracle Attacks: Hic Sunt Dracones"
page_title: "HoyaHaxa: A Security Research Blog: On ColdFusion, AES, and Padding Oracle Attacks:  Hic Sunt Dracones"
url: "https://hoyahaxa.blogspot.com/2023/07/on-coldfusion-aes-and-padding-oracle.html"
final_url: "https://www.hoyahaxa.com/2023/07/on-coldfusion-aes-and-padding-oracle.html"
authors: ["Brian (@hoyahaxa)"]
bugs: ["Padding oracle attack", "ColdFusion", "Cryptographic issues"]
publication_date: "2023-07-03"
added_date: "2023-07-04"
source: "pentester.land/writeups.json"
original_index: 973
---

**TL; DR:**_If you use AES-CBC (or another block cipher operating in CBC mode) to decrypt user-controlled ciphertext, validate the ciphertext with an HMAC or similar integrity check prior to decryption to avoid Padding Oracle vulnerabilities. All user-controlled input is untrusted and can be dangerous, even if it is encrypted data._

_  
_

_  
_

  

### **Introduction**

In my [last post](https://hoyahaxa.blogspot.com/2023/05/why-you-dont-want-to-use-cfmxcompat.html), I closed by saying that AES in CBC (Cipher Block Chaining) mode is the best native option for symmetric block encryption in ColdFusion -- but added that it can lead to vulnerabilities if not implemented correctly. In this post we're going to look at how you should (and shouldn't) implement AES and other block ciphers if you want to avoid Padding Oracle Attacks. And although we're focused on ColdFusion, the general concepts apply to any application language.

Let's consider the code snippet below. This code is materially similar to many AES-CBC implementations in ColdFusion that I've seen in real applications, shared libraries, example code, technical documentation, and other sources that are likely to be in common, widespread use. **_Can you spot why it's vulnerable?_**

  

<cfscript>  
decryptedVal = decrypt(COOKIE.AUTH_USER, mySecretKey, "AES/CBC/PKCS5Padding", "HEX");  
</cfscript>

  

  

This code decrypts a cookie named "AUTH_USER" (which is expected to be a hex-encoded string) with AES-CBC, using "mySecretKey". ** _But since we're not performing any integrity checking (such as a signature or HMAC) on the ciphertext to be decrypted that the user passes in the cookie, an application that implements AES-CBC in this way is likely vulnerable to a Padding Oracle Attack._**

  

### **AES-CBC Refresher**

  

Let's start with a quick refresher of how AES-CBC works. There are lots of great books, articles, and other sources that that cover it much greater detail but we'll hit the relevant parts. As shown below, AES-CBC encryption splits a message into fixed-length blocks (specifically 16-bytes blocks, for AES-CBC) and encrypts each block independently. Prior to encrypting a block, the plaintext to be encrypted is XORed with the previous block of encrypted ciphertext (or the IV, in the case of the first block of plaintext). During this process, we're creating a "chain" based on input from previous encrypted blocks -- hence the name. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiznJlIro2Zi-YU0epYU6iGU5uP189bS1V1JKO4pQ3MMnSbq59aNv10S8e0uSYIjdxCnZW_nFCCclq7P8wiLQ6t4QSzoAclJffPjuCDB6M3rCcvCjc3tjY6q2BO3WpmzUjor17qvuCNAYNq7QufxqzDkvXfMmpsVqD6ImkAUQe38JOEpU92xK1gi9wJCEE/w654-h265/600px-CBC_encryption.svg.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiznJlIro2Zi-YU0epYU6iGU5uP189bS1V1JKO4pQ3MMnSbq59aNv10S8e0uSYIjdxCnZW_nFCCclq7P8wiLQ6t4QSzoAclJffPjuCDB6M3rCcvCjc3tjY6q2BO3WpmzUjor17qvuCNAYNq7QufxqzDkvXfMmpsVqD6ImkAUQe38JOEpU92xK1gi9wJCEE/s600/600px-CBC_encryption.svg.png)

  

AES-CBC _decryption_ works the same way, but in reverse. After passing an encrypted block though our decryption cipher, that intermediate-state value is XORed with the previous block of ciphertext to get a block of our original plaintext message:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCt_8P5BGz7Bx-kaG1fdD9kDcKHeWVz_fihSlF-tMDV-7i7fbV57UFIv5Q2A_9TuqJcxi9tfuya5sxzQlwFyn_Yd5NE0DJeNR8EIoHfzkmB7N7_HychVZ7gxifcCSqzsB39qCAAFHWWG3-l_KzH9BxNdvpfNMSywAcFMb8Y2XiUtXDIue_KyNR8CeJnEk/w655-h264/600px-CBC_decryption.svg.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCt_8P5BGz7Bx-kaG1fdD9kDcKHeWVz_fihSlF-tMDV-7i7fbV57UFIv5Q2A_9TuqJcxi9tfuya5sxzQlwFyn_Yd5NE0DJeNR8EIoHfzkmB7N7_HychVZ7gxifcCSqzsB39qCAAFHWWG3-l_KzH9BxNdvpfNMSywAcFMb8Y2XiUtXDIue_KyNR8CeJnEk/s600/600px-CBC_decryption.svg.png)

  

_[ Images from<https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)> ]_

_  
_

  

### **Message Padding**

  

Before we cover Padding Oracle Attacks, let's talk about message padding. Message padding lets us encrypt messages of any size when using a block cipher. Block ciphers need the input to be multiple of the block size (e.g., 16 bytes for AES), but padding takes care of this for the user. There are a handful of common padding standards, but in PKCS#5/PKCS#7 (the padding standards that we'll be using), the values of the padded bytes is equal to the number of padded bytes we need. For example, we need need seven bytes of padding for the message below, so our padded plaintext would look like:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhI1aiIaASh9xN9nH8IR7fvntde8N2qpo_sfiUWkSvrg3cDcOTFktUCCVWI_aW0e2BKa0mPPybyq4vTfXTwd0k4CrQYWqp5QKTXcJ5Fd6uaCME2dVldtrW1GmsgWjpcRsTS1bs1HWqXr8uoeQkY1yPWvIrcWZ28NI89O_6nVTUfyWfldUJkNHa2DGAFWP4/w686-h129/padded.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhI1aiIaASh9xN9nH8IR7fvntde8N2qpo_sfiUWkSvrg3cDcOTFktUCCVWI_aW0e2BKa0mPPybyq4vTfXTwd0k4CrQYWqp5QKTXcJ5Fd6uaCME2dVldtrW1GmsgWjpcRsTS1bs1HWqXr8uoeQkY1yPWvIrcWZ28NI89O_6nVTUfyWfldUJkNHa2DGAFWP4/s1459/padded.png)

  

  

During decryption, the message padding gets checked. A typical padding check will work similar to:

  

  * Read the final byte of decrypted plaintext, _N_
  * If _N_ > blocksize: **PADDING ERROR**
  * Loop through _N - 1_ bytes ; if any don’t contain _N_ : **PADDING ERROR**
  * Remove last _N_ bytes from the message
  * No Errors = **Decryption Successful!**_(*could still be garbage data or cause errors later)_

So **Swordfish[0x07][0x07][0x07][0x07][0x07][0x07][0x07]** becomes **Swordfish** after the padding check is complete.

  

But if there is any type of padding error, the application with throw an exception. Here we see what a verbose padding error looks like in Adobe ColdFusion:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyu-Y3REJPCel7qfWj-Hwfa4hma7l98In8fHYaOB3kMEKuquhjjMWF_5jP6xkCXyymfAJRjG3l5tMJGEriL36f_JcqZZYQAE0Wj9XCtvFX88mOheKRRksC6xnSiF-rMb63cTaNmVihf_RFdnPcKZ76FmohookvlxhDg3TFrbiXn7si6Pp3JceSsTQYQ4U/w679-h401/padding-error.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyu-Y3REJPCel7qfWj-Hwfa4hma7l98In8fHYaOB3kMEKuquhjjMWF_5jP6xkCXyymfAJRjG3l5tMJGEriL36f_JcqZZYQAE0Wj9XCtvFX88mOheKRRksC6xnSiF-rMb63cTaNmVihf_RFdnPcKZ76FmohookvlxhDg3TFrbiXn7si6Pp3JceSsTQYQ4U/s1872/padding-error.png)

  

And the differentiation between these two end-states (padding error vs. no padding error) is what we're going to use to carry our our Padding Oracle Attack. 

  

### **The Padding Oracle Attack**

  

[  _Note: to avoid any confusion, this attack has nothing to do with a certain giant database company. The "oracle" here refers to being able to divine secret, unknown information. Think the Oracle at Delphi, not the Oracle at Redwood Shores, CA._ ☺ __]

If you use a block cipher in CBC mode and don't perform an integrity check on user-controlled ciphertext prior to decryption, your application is almost certainly vulnerable to a padding oracle attack. Our example today focuses on ColdFusion and AES, but any language and any block cipher operating in CBC mode can be vulnerable to the same type of flaw. Padding Oracle Attacks have been a known vulnerability class for over a decade, and some high-profile examples have included the [POODLE attack](https://en.wikipedia.org/wiki/POODLE) and a [framework-wide padding oracle in ASP.NET (MS10-070)](https://www.troyhunt.com/fear-uncertainty-and-and-padding-oracle/).

  

It's also worth highlighting that AES-CBC is cryptographically sound from an algorithm perspective. We're not using complex math, cracking keys, or attacking the actual encryption algorithm. Instead, we're leveraging flaws in the software implementation of AES-CBC that let us perform a side-channel attack based on application behavior and feedback -- essentially letting us circumvent encryption due to our ability to make valuable inferences. And while we do need to be able to distinguish between "padding error" vs. "no padding error", we do not need verbose error messages. Any detectable, consistent differences in these end states (such as distinct generic errors) will let us perform our attack. 

  

So let's now walk through what an attack looks like and recall how AES-CBC decryption works. The image on the left shows the process of decrypting one block of ciphertext (C2) into one block of plaintext (P2). Note that "decryption" with our cipher and key first gets us to our intermediate state (I2), and we don't actually obtain our plaintext until we XOR I2 with C1 (our previous block of ciphertext). Also note that these XOR transformations work in either direction, from top down or bottom up. 

  

The image below shows the logical flow of our Padding Oracle Attack. The left side shows how a single block gets decrypted. On the right - because of how padding standards and padding checks work, we can assume there's a  _chosen_ ciphertext block C'1 that will result in a new plaintext P'2 block that ends in 0x01 (one byte of padding) when XORed with I2. Recall that since there's no integrity checking on the inputted ciphertext, we can modify the ciphertext bytes in any encrypted values and make all of the guesses that we need. So now all we need to do is make a maximum of 256 guesses for the _last byte_ of our chosen C'1 (referred to as C'1[16]) where P'2[16] is 0x01 (one byte of padding). We should get "padding errors" from our application for all values except for one -- and that's the value that we want. We can then solve for the last byte of the intermediate value I2[16], and then use and then use this value to decrypt one byte of the _real_ plaintext, P2[16]. Next we can solve for a case where our chosen block of ciphertext results in a plaintext that ends with two bytes of padding, 0x02 0x02 -- which will give us another byte of I2. From here, we can continue byte by byte, modifying values, making guesses, observing padding behavior, and decrypt our entire ciphertext value. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggCLhcP-bczr6uvodT3TPPLc74sF8WAUNh8WCg-M3LkRSkzbuD8UirKiLKwLx7-Z4PKQnv762NjLtB5DjjI2x4QTeYDjzzc_NrfLf49CSagQXz8PC0mpF7piETXVQ3bsFSPmpTxNklzATNMDPM8NzudhcB2xsrrSM5TBizD1AjO2vD_mswHygWHPobZKA/w797-h315/poa-flow.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggCLhcP-bczr6uvodT3TPPLc74sF8WAUNh8WCg-M3LkRSkzbuD8UirKiLKwLx7-Z4PKQnv762NjLtB5DjjI2x4QTeYDjzzc_NrfLf49CSagQXz8PC0mpF7piETXVQ3bsFSPmpTxNklzATNMDPM8NzudhcB2xsrrSM5TBizD1AjO2vD_mswHygWHPobZKA/s1655/poa-flow.png)

  

  

 _[The images above are adapted from[Robert Heaton's Padding Oracle Attack write-up (https://robertheaton.com/2013/07/29/padding-oracle-attack/)](https://robertheaton.com/2013/07/29/padding-oracle-attack/), which remains a personal favorite on the subject. Highly recommended. Go read it. ]_

  

And if  _decrypting_ ciphertext with no knowledge of the key isn't scary enough, be aware that Padding Oracle Attacks can be used to create entirely new blocks of ciphertext from fully-chosen plaintext too!

  

### **A Sample Vulnerable Application**

  

Let's consider a vulnerable application that consumes an encrypted value from a URL parameter -- much like our original COOKIE.AUTH_USER example but with a different source of user-controlled data. Assuming decryption works, the application will display a username and a user role, obtained from our decrypted token. Maybe a little contrived, but very similar to how some actual user authentication schemes may work. 

  

And since the application isn't validating the ciphertext prior to decryption, we can carry out our Padding Oracle Attack, as shown in the video below. Our automated attack tool makes short work of decrypting the encrypted token -- with no knowledge of the key or any internal application details. Watch ciphertext change to plaintext, byte by byte and block by block. 

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsuJpXBoS9WE8GdJ2RHqot3NBL2M6Guf_wVwuEOPjl8u3XBzgz0_z0kNdKNht4klzph1mWJdeQBNYPnVaXo0OZvEdxSY_jVUQxwzbu4HAHRVJfw_saeSCiTgz5EcP3tWqOmt3ajvHqVDeyZR_VhAbHkDH3jhI2xI_DCRhRYf55LC9okx5h05lZLryU5A8/w711-h309/poa-app.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsuJpXBoS9WE8GdJ2RHqot3NBL2M6Guf_wVwuEOPjl8u3XBzgz0_z0kNdKNht4klzph1mWJdeQBNYPnVaXo0OZvEdxSY_jVUQxwzbu4HAHRVJfw_saeSCiTgz5EcP3tWqOmt3ajvHqVDeyZR_VhAbHkDH3jhI2xI_DCRhRYf55LC9okx5h05lZLryU5A8/s2103/poa-app.png)

  

  

  

  

  

  

  

Included below is some sample vulnerable ColdFusion code you can play with, if you want to reproduce and walk through a Padding Oracle Attack on your own. **Needless to say, this is vulnerable code that should not be used or deployed anywhere other than a local, offline test environment.** Usage of the sample code should be pretty simple -- if you pass in a "secret" URL parameter, the application will try to decrypt it. Without this parameter, it will output some encrypted ciphertext (that you can then pass in to decrypt): 

  

  

<cfscript>

  

encryptionKey = "JAidBZLaYf37huVuM4MNTA=="; //our AES key

  

// if there's a "secret" URL parameter, we'll attempt to decrypt it

// vulnerable to POA because there's no integrity check of the ciphertext 

if (isDefined("url.secret")) { 

  

decryptedInput = decrypt( url.secret, encryptionKey, "AES/CBC/PKCS5Padding", "hex" );

writeOutput( "Decrypted Stuff: #decryptedInput# <br>" );

}

  

  

// if we don't have a "secret" URL parameter, just output some ciphertext

// you can then use this as a value to decrypt, passed in url.secret

else { 

  

input = "Here is the super secret stuff we want to encrypt.";

encryptedInput = encrypt( input, encryptionKey, "AES/CBC/PKCS5Padding", "hex" );

writeOutput( "Encrypted Stuff: #encryptedInput# <br>" );

}

  

</cfscript>

  

This code is vulnerable since no integrity checking is done prior to decryption. Once you get the vulnerable code up and running, observe that if you change one hex value in a valid "secret" URL parameter with another valid hex value, you should get a padding error. Other ciphertext value modifications may result in other encryption errors or application errors. Then see if you can manually walk through the Padding Oracle Attack operations to decrypt one byte of ciphertext. (Keep in mind that the last byte of the decrypted plaintext will probably be a byte of padding.)

  

Building a fully-working Padding Oracle Attack script is an exercise left for the reader. There are many tools, tutorials, and resources to help you build a fully-working exploit. I'm partial to [Bletchly](https://code.blindspotsecurity.com/trac/bletchley), which is a great choice if you're comfortable with Pyhton3. It does not help you  _find_ Padding Oracle vulnerabilities, but it is very handy to automate the steps for data decryption and modification, once you've found a vulnerable application component. [This post on Padding Oracle Attacks from NCC Group](https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles/) may be helpful too. If you get stuck on the exploitation part, feel free to drop me a line or leave a comment.

  

### **Prevention and Detection of Padding Oracle Attacks**

  

So how do we make our AES-CBC implementation more secure? We could potentially use an entirely different encryption algorithm, specifically something other than a block cipher in CBC mode. But let's assume we can't make that change, and need to use AES. Then the best thing to do first is to add some integrity checking to our decryption process, using something like an HMAC or signature for the ciphertext. This signature must be checked prior to decryption, and if it fails, decryption should not even be attempted. This would detect if the ciphertext has been modified, such as during all of our guesses needed for a Padding Oracle Attack.

  

Our new code adds a key used for signing, generates an HMAC for the ciphertext, and checks the HMAC prior to attempting to decrypt the ciphertext. There's certainly lots of room for improvements in this code -- such as moving the actions to functions and adding better error handling -- but it's only intended as a basic guide on how to quickly add integrity checking (an HMAC) prior to decryption. 

  

<cfscript>

  

encryptionKey = "JAidBZLaYf37huVuM4MNTA=="; //our AES key

signingKey = "pickSomethingBetter"; //let's use a different key for signing

  

// A valid url.secret should now contain <CIPHERTEXT>-<HMAC>

// If there's a "secret" URL parameter, we'll attempt to decrypt it - ONLY IF the HMAC is valid

if (isDefined("url.secret")) { 

  

// Does the "secret" contain two parts - presumably the ciphertext and an HHAMC? 

secretParts = listToArray(url.secret,"-");

if (len(secretParts) != 2) {

writeOutput("nope");

cfabort();

}

// Is the HMAC valid?

if (hmac(secretParts[1], signingKey, "HMACSHA256") != secretParts[2]) { 

writeOutput("nope");

cfabort();

} 

  

decryptedInput = decrypt( secretParts[1], encryptionKey, "AES/CBC/PKCS5Padding", "hex" );

writeOutput( "<b>Decrypted Stuff:</b><br> #decryptedInput# <br>" );

}

  

// if we don't have a "secret" URL parameter, just output valid ciphertext with an HMAC

// you can then use this as a value to validate and decrypt, passed in url.secret

else { 

  

input = "Here is the super secret stuff we want to encrypt.";

encryptedInput = encrypt( input, encryptionKey, "AES/CBC/PKCS5Padding", "hex" );

hmac = hmac(encryptedInput, signingKey, "HMACSHA256"); 

writeOutput( "<b>Encrypted Stuff:</b><br> #encryptedInput#-#hmac# <br>" );

}

  

</cfscript>

  

  

It's also worth noting that exploiting Padding Oracle Attacks can be noisy, since an attacker may need to make up to 256 requests per byte when making guesses. This can result in lots of requests, lots of logs, and lots of errors. Repeated, high-volume padding errors generated in your application could be an indicator of an attempted attack.

  

Finally - remember that encryption (and even data integrity checking) is just one aspect of security, and one approach to secure portions of an application. Often times, you may not even want to expose encrypted sensitive values to the user at all, an instead may want to pass some type of reference value, to be used to fetch (and keep) sensitive data entirely on the backend. 

  

### **Closing Thoughts**

The Padding Oracle Attack is just one more example of the risk of _any_ user-controlled input. Developers may already be wary of user input that flows into SQL queries to avoid SQL injection, or rendered content to avoid Cross Site Scripting -- but _all_ user-controlled input should be validated, **_even encrypted data_**. Encryption on its own may prevent a malicious users from reading data or _intelligibly_ modifying data -- but it provides no native protection against blind, random, or automated modification of ciphertext. Validate the integrity of all user-controlled ciphertext with a signature, HMAC, or similar mechanism. If that validation fails, don't even attempt decryption.

  

As always, never trust user-controlled input.

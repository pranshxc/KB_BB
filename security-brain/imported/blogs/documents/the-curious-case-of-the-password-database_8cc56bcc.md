---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-20_the-curious-case-of-the-password-database.md
original_filename: 2022-10-20_the-curious-case-of-the-password-database.md
title: The Curious Case Of The Password Database
category: documents
detected_topics:
- command-injection
- idor
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- idor
- rate-limit
- api-security
language: en
raw_sha256: 8cc56bccc436637b54844219d8579ab21c468c731273f86d0721f45297fa2d8d
text_sha256: 8ac0835cd31ae2440e481ac774984aff19a87329d35c400e556a1a4d95b01234
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# The Curious Case Of The Password Database

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-20_the-curious-case-of-the-password-database.md
- Source Type: markdown
- Detected Topics: command-injection, idor, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `8cc56bccc436637b54844219d8579ab21c468c731273f86d0721f45297fa2d8d`
- Text SHA256: `8ac0835cd31ae2440e481ac774984aff19a87329d35c400e556a1a4d95b01234`


## Content

---
title: "The Curious Case Of The Password Database"
page_title: "TrustedSec | The Curious Case of the Password Database"
url: "https://www.trustedsec.com/blog/the-curious-case-of-the-password-database/"
final_url: "https://www.trustedsec.com/blog/the-curious-case-of-the-password-database"
authors: ["Travis Kaun (@W9HAX)"]
programs: ["Zoho (ManageEngine)"]
bugs: ["Cryptographic issues"]
publication_date: "2022-10-20"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 2010
---

* [Blog](https://trustedsec.com/blog)
  * [The Curious Case of the Password Database](https://trustedsec.com/blog/the-curious-case-of-the-password-database)

October 20, 2022

# The Curious Case of the Password Database

Written by Travis Kaun 

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/CuriousCasePasswordDatabase_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767067094&s=d7bff62708bab7f24fc57c650ee3f730)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#d2eda1a7b0b8b7b1a6ef91bab7b1b9f7e0e2bda7a6f7e0e2a6babba1f7e0e2b3a0a6bbb1beb7f7e0e2b4a0bdbff7e0e286a0a7a1a6b7b681b7b1f7e0e3f4b3bfa2e9b0bdb6abef86bab7f7e0e291a7a0bbbda7a1f7e0e291b3a1b7f7e0e2bdb4f7e0e2a6bab7f7e0e282b3a1a1a5bda0b6f7e0e296b3a6b3b0b3a1b7f7e193f7e0e2baa6a6a2a1f7e193f7e094f7e094a6a0a7a1a6b7b6a1b7b1fcb1bdbff7e094b0bebdb5f7e094a6bab7ffb1a7a0bbbda7a1ffb1b3a1b7ffbdb4ffa6bab7ffa2b3a1a1a5bda0b6ffb6b3a6b3b0b3a1b7 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=The%20Curious%20Case%20of%20the%20Password%20Database%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database&mini=true "Share on LinkedIn")

Nowadays, password managers are king. We use password managers to secure our most sensitive credentials to a myriad of services and sites; a compromise of the password manager could prove devastating.

Due to recently [_disclosed critical Common Vulnerabilities and Exposures (CVEs_](https://www.manageengine.com/products/passwordmanagerpro/issues-fixed.html)) involving ManageEngine's Password Manager Pro software, a client came to us at TrustedSec, wondering: _If an attacker gained access to our Password Manager Pro server, would our passwords be compromised?_

![Scooby Doo meme](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun1-meme.jpg)

Since the client was assured that data within the Password Manager Pro server was encrypted, our answer was assuredly, "No." Right? We set off to find out!

The [_recent CVEs affecting the Password Manager Pro software_](https://thehackernews.com/2022/09/cisa-warns-of-hackers-exploiting-recent.html) were some of the worst kind: Remote Code Execution (RCE). For the sake of this engagement, we were focused not so much on the initial attack vector, but rather on the extent of the post-exploitation possibilities. Simply, with access to the system's data, could we recover the encrypted secrets stored within?

We started with access an attacker would presumably have:

  * [_Password Manager Pro v10.5_](https://archives2.manageengine.com/passwordmanagerpro/10501/)

Note: Mid-engagement, we identified some newly published work by [_smaury at Shielder_](https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/) regarding tearing apart Password Manager Pro. The timing was astounding. Our collective articles may look similar; but our approaches, experience, and code differ. We highly suggest checking out his terrific write-up regarding this topic.

## Step 1 - Application Enumeration

We staged an instance of Linux running ManageEngine’s Password Manager Pro version 10.5 to replicate the client's environment. After fetching the [_application software_](https://archives2.manageengine.com/passwordmanagerpro/10501/) and initiating a [_restore_](https://www.manageengine.com/products/passwordmanagerpro/help/disaster_recovery.html), we started by analyzing the running processes and identifying key information. The application was running Java and PostgreSQL as the primary components.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_1-1.png)Figure 1 - ManageEngine's Running Processes

TrustedSec then explored the Password Manager Pro application directory, revealing a collection of Java JAR application and configuration files. By reading application documentation, TrustedSec identified the username and encrypted database password stored in the **_database-params.conf_** file.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_2.png)Figure 2 - Encrypted Database Password

The **_pmp_key.key_** file reveals the PMP key, which will come in handy later.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_3.png)Figure 3 - PMP Key

## Step 2 - PostgreSQL Password Recovery

One of the best parts of working at TrustedSec is being surrounded by a diverse and talented team of people who are willing and able to help. My Java skills didn't make it much past my sophomore year of college; however, my skilled coworker [_Rob Simon_](https://trustedsec.com/team-members/rob-simon) was able to hop in and provide additional guidance.

We extracted the application JAR files located in **_/opt/ManageEngine/PMP/lib_** and decompiled and analyzed the files to reveal how decryption functions for the underlying PostgreSQL database were handled. While walking through the code, we found that the application uses a static secret key derived from the string **_@dv3n7n3tP@55Tri_** that was used to encrypt the database password—notably, only five (5) characters: **_7n3tP_**.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_4.png)Figure 4 - JAR Decompilation![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_5-1.png)Figure 5 - Password Manager Pro Hardcoded Password – 7n3tP![Scooby Doo meme unmasking](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun2-meme.jpg)

Using the **_decryptPassword_** function, we could then whip up a bit of Java code using Password Manager Pro’s own functions to conduct the decryption for the database password. This revealed our PostgreSQL database password.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_6.png)Figure 6 - Database Decryption Function

Hey, that's a plaintext database password!

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_7.png)Figure 7 - Recovered Database Password

## Step 3 - Database Interrogation - Master Key

TrustedSec investigated the **_PasswordEncryptDecrypt_** class to determine how encrypted passwords could be recovered. A master key is required to decrypt database passwords. To obtain the decrypted master key, TrustedSec identified the encrypted master key stored within the database as **_notesdescription_** and supplied the **_pmp_key_** to the **_decryptPassword_** function of the **_PMPEncryptDecrypt_** class. This resulted in the plaintext master key.

To pull the encrypted **_master_key_** , within Postgres, issue:

`select * from Ptrx_NotesInfo`

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_8-1.png)Figure 8 - Encrypted Master Key (notesdescription)

Then plug the newly acquired encrypted **_master_key_** into our Java script to derive the plaintext master key. Groovy, we got a plaintext master!

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_9.png)Figure 9 - Master Key Decryption Function![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_10.png)Figure 10 - Recovered Master Password

## Step 4 - Database Interrogation - Encrypted Passwords!

To harvest the data of interest stored within PostgreSQL, you can use the following query. Notice that the **_decryptsblob_** table will still be encrypted. One last decryption step will be needed.
  
  
  select decryptschar(PASSWORD,'<INSERT master_key>') from ptrx_passbasedauthen

Around this time in our analysis, I stumbled upon the previously mentioned research from [_smaury @ Shielder_](https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/) . He included a robust query that was great for pulling with additional table columns.
  
  
  select ptrx_account.RESOURCEID, ptrx_resource.RESOURCENAME, ptrx_resource.RESOURCEURL, ptrx_password.DESCRIPTION, ptrx_account.LOGINNAME, decryptschar(ptrx_passbasedauthen.PASSWORD,'***master_key***') from ptrx_passbasedauthen LEFT JOIN ptrx_password ON ptrx_passbasedauthen.PASSWDID = ptrx_password.PASSWDID LEFT JOIN ptrx_account ON ptrx_passbasedauthen.PASSWDID = ptrx_account.PASSWDID LEFT JOIN ptrx_resource ON ptrx_account.RESOURCEID = ptrx_resource.RESOURCEID

Data should look similar to the image below, which I then exported via DBeaver.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_11-1.png)Figure 11 - Database Extraction - Encrypted Passwords

## Step 5 - Password Recovery

Now, we have the decrypted database password and the **_master key_** , but we still have an encrypted password column within the database. Using the same **_PasswordEncryptDecrypt_** class that we examined earlier, we can build a script where we supply an encrypted password along with **_pmp_key_** to reveal the stored plaintext credential.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_Shaggy.png)

Leveraging the expertise of the TrustedSec resident Python wizard, [_Charles Yost_](https://trustedsec.com/team-members/charles-yost), we opted to script this in Python versus working in Java because, honestly, who prefers Java?!

On that note, we’re happy to announce the release of [**Zoinks – the Password Manager Pro Decrypter**!](https://github.com/trustedsec/Zoinks)

The script can be operated in interactive mode or supplied parameters at runtime.

Step 1 - Provide the following:

  * Encrypted Database Password (**_database_params.conf_**)

Step 2 - Once the database has been accessed, provide the following:

  * Password Manager Pro Key (**_pmp_key.key_**)
  * Encrypted Master Key (**_notesdescription_**)
  * Encrypted Password (**_decryptsblob_**)

Let’s go after HackingDave’s password and plug it into our **_zoinks.py_** script.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_12-1.png)Figure 12 - Zoinks Decryption Toolkit

## Conclusion

In the midst of a breach, we often hear, "Don't panic—the data on the server was encrypted!" Data encryption is a best practice; it checks the audit box, and it allows us to sleep soundly. During this engagement, the more we peeled back layers of the Password Manager Pro application, the clearer it became that, while data was encrypted, everything needed to decrypt the data was stored on the server.

TrustedSec determined that someone with access to a Password Manager Pro server could recover encrypted data stored within the server due to ManageEngine’s implementation of encryption keys and methods.

Shoutout to my TrustedSec team ([_Rob_](https://trustedsec.com/team-members/rob-simon), [_Charles_](https://trustedsec.com/team-members/charles-yost), and [_Phillip_](https://trustedsec.com/team-members/philip-dubois)) for the time and guidance and to smaury for the timely write-up!

![Scooby Doo meme](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun4-meme.jpg)

#### Update (November 3, 2022)

TrustedSec determined that someone with access to a Password Manager Pro server could potentially recover encrypted data stored within the server if conditions are met. TrustedSec suggests clients using ManageEngine’s PMP [review their best practices](https://www.manageengine.com/products/passwordmanagerpro/help/installation.html#managing) to securely manage key files to prevent this type of attack.

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#e6d99593848c838592dba58e83858dc3d4d6899392c3d4d6928e8f95c3d4d68794928f858a83c3d4d68094898bc3d4d6b2949395928382b58385c3d4d7c0878b96dd8489829fdbb28e83c3d4d6a593948f899395c3d4d6a5879583c3d4d68980c3d4d6928e83c3d4d6b687959591899482c3d4d6a287928784879583c3d5a7c3d4d68e92929695c3d5a7c3d4a0c3d4a092949395928382958385c885898bc3d4a0848a8981c3d4a0928e83cb8593948f899395cb85879583cb8980cb928e83cb9687959591899482cb8287928784879583 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=The%20Curious%20Case%20of%20the%20Password%20Database%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database&mini=true "Share on LinkedIn")

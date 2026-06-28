---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-24_the-art-of-chaining-vulnerabilities.md
original_filename: 2023-12-24_the-art-of-chaining-vulnerabilities.md
title: The ART of Chaining Vulnerabilities
category: documents
detected_topics:
- command-injection
- rate-limit
- mobile-security
- sso
- idor
- ssrf
tags:
- imported
- documents
- command-injection
- rate-limit
- mobile-security
- sso
- idor
- ssrf
language: en
raw_sha256: a180b210a23eaca40914aa28724fc1f71cb362d1ca8ad9a5e47bcc53f3edb1b8
text_sha256: c0ba2b1823267b32453053d00b304a9cd868015e9a9ec3b76f39b316b148155f
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# The ART of Chaining Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-24_the-art-of-chaining-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, mobile-security, sso, idor, ssrf
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `a180b210a23eaca40914aa28724fc1f71cb362d1ca8ad9a5e47bcc53f3edb1b8`
- Text SHA256: `c0ba2b1823267b32453053d00b304a9cd868015e9a9ec3b76f39b316b148155f`


## Content

---
title: "The ART of Chaining Vulnerabilities"
url: "https://ahmdhalabi.medium.com/the-art-of-chaining-vulnerabilities-e65382b7c627"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["Android", "WAF bypass", "Bruteforce", "Hardcoded credentials", "RCE"]
publication_date: "2023-12-24"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 595
scraped_via: "browseros"
---

# The ART of Chaining Vulnerabilities

Top highlight

The ART of Chaining Vulnerabilities
Ahmad Halabi
Follow
8 min read
·
Dec 24, 2023

768

5

Press enter or click to view image in full size

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

Hello,

My name is Ahmad Halabi.

During my career, I had the chance to be part of an Operation Unit running projects on a high level scale. We had one goal to achieve: hacking the complete infrastructure of a target.

In this article, I will be mentioning two projects where I was capable of accomplishing the goal without any interaction from the target end.

The purpose of this operation was to assess the scale of the damage that can be achieved by criminals if they were able to infiltrate into the target infrastructure.

Before we start… Who Am I ? (Short Summary)

I started my hacking career in Mid of 2019 and within 5 months I was able to mark my name as the top hacker by the U.S. Department of Defense leaderboard on hackerone in 2019 (Read my Article about it).

Then I did full time bug bounty for 6 months and it was great (Read my article about my experience in BB).

Then I kept doing bug bounty hunting for some time and I worked on my startup ‘Cybit Sec’ focused on blackbox Penetration Testing and Vulnerability Research, which later was acquired by ‘Resecurity’ — a leading Company in the Threat Intelligence field.

The ART Of Chaining Vulnerabilities

Concepts:

The process of Chaining Vulnerabilities requires a set of procedures that allows hackers to use the advantage of multiple errors/bugs within the application to achieve the maximum impact.

Simple example can be chaining Open redirect with XSS, then XSS to Account Takeover. SSRF to RCE. As for us, we didn’t stop at chaining 2 or 3 vulnerabilities together, but we chained every step to infiltrate into the networks and pivot into the infrastructures, to obtain as a final result, a “Full Remote Access into the Target”.

Project 1: Owning the Company from a mobile App.

Having a mobile app (apk file) in hand to start.

My first step was to decompile the apk file.
Press enter or click to view image in full size
APK File

You may use `jadx` or `apktool` which help you decompiling the Dex & Apk Files to a readable Java and Smali code.

Press enter or click to view image in full size
Decompiling mobile app apk

2. After reviewing the source code, I noticed that the configuration files are encrypted with JSC Extension.

Press enter or click to view image in full size
JSC Encryption

JSC stands for JavaScript compiled Script that developers use to encrypt files containing sensitive information (Ex: Server IP, Credentials, Secret Keys, etc).

3. Next step will be decrypting JSC files in order to reveal the source code.

JSC uses Cocos2d-x (an open source cross-platform development framework).

So I started searching for Cocos2d-x files in the decompiled application files.

Press enter or click to view image in full size
Cocos2d-x files

4. I started reverse Engineering the `libcocos2d-x.so` file and searching for `main.js` function.

And for this, nothing better than IDA Pro to be used :)

The purpose is to find the decryption key `XXTEA` that `Cocos2d-x` uses to Encrypt the Files.

Press enter or click to view image in full size
Extracting XXTEA Key to decrypt files

5. Then I used the `XXTEA` Key to decrypt the JSC Files.

Press enter or click to view image in full size
Decrypting JSC Files

After JSC Files are decrypted, I got access to Javascript files and now I can easily read the Source Code. And by decrypting the JSC Files, I successfully broke the Application Encryption.

6. Starting Source Code Review phase, I found an interesting IP Address in one of the decrypted configuration files.

Press enter or click to view image in full size
IP Address identification in the decrypted JS File

7. Started doing some Port Scanning, but clearly there was some protection as I was getting huge delays in packets.

Press enter or click to view image in full size
Delays and latency in packets

8. So I used an alternative option to detect open ports by trying Open source Intelligence (Shodan/Censys), and I found an open port `8100` running GitLab.

Press enter or click to view image in full size

9. Navigating to the IP:8100, I found a Gitlab page with `Register` button and luckily it was working. So I registered for an account and accessed company’s Gitlab.

Press enter or click to view image in full size

No Public Projects were available for users with normal role/privilege.

10. After some work around content discovery, I found an endpoint `api/v4/users` which discloses user details and the username of the Administrator was found there.

Press enter or click to view image in full size

11. I marked the username, logged out from my account, and added the admin username `root` and prepared a wordlist to brute force the password.

The password’s wordlist wasn’t random, I spent couple of hours going to all the company profiles on social media, open source (github, etc), website and any other sources that allow me to have proper understanding and get the right intel about the possible password that the Admin might be using.

12. The web application was using WAF to protect against Brute Force Mechanisms.

I successfully tricked the WAF and bypassed the Brute Force Protection using `X-Forwarded-For:127.0.0.$1$` and it by 1 for each request.

Press enter or click to view image in full size

By obtaining successful login, I successfully broke the WAF Protection.

So now both App Encryption and WAF Protection are broken.

13. I got access to Gitlab with Admin privileges and I was able to view the private repositories.

Press enter or click to view image in full size

14. Reviewing source code, I identified credentials to access the company’s infrastructure.

Press enter or click to view image in full size
Cloud Databases
Press enter or click to view image in full size
SQL Databases
Press enter or click to view image in full size
Redis Databases

15. And from the databases, I found the credentials of the target Server.

Server Username

The password was hashed but it was easy to decode.

Press enter or click to view image in full size
Server Password

I got the credentials to access all the backend management systems.

Press enter or click to view image in full size

From Redis, I escalated it to RCE and accessed the another server.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I started pivoting and infiltrating from one server to another ending up accessing all the servers.

Press enter or click to view image in full size

And by that, I owned the whole company and stayed persistent without anyone notice :)

Timeline:

It took me 25 hours in total to close this project.

5 days — 5 hours per day.

Reference:

I explained some of the stages of this project in details during my talk at BlackHat 2022.

Press enter or click to view image in full size
My talk During BlackHat

https://youtu.be/Zb6oQXJdSsU?si=v9zr0aZ5LettzLfM

Lesson Learned:

Importance Of Implementing Multi Security Layers/Protections:

We saw that even though the target company was implementing Code Encryption and Web Application Firewall, I was able to Break the Encryption and Bypass the WAF which allowed me later to fully compromise the Target.

Don’t rely on One Security Layer:

Additional to Code Encryption, Don’t add any sensitive information in the Application Source Code.
Additional to WAF, Implement Web Security Protections inside your Web Application Server and Code.

ROUND 2: Now let’s discuss the second project.

Project 2: Owning the whole Company from having only 1 IP Address as prerequisites.

Port Scanning the IP Address [Found open SSH but not vulnerable + brute forcing the password didn’t work].
Performed Reverse IP Lookup [Found the Domain Name].
Performed Subdomain Enumeration [Found a Resolving Subdomain `vip.target.com`].
Port Scanning [Found Nginx, Xampp, Java Running].
Checking for common vulnerabilities and known exploits [None were vulnerable to CVE].
Directory Brute Force [Found Login Page].
Trying common usernames and Brute Forcing the password input [Didn’t work].
Viewing Page Source + Reading JavaScript Files [Found hidden Registration Page].
Registration required a Whitelisted Range of Phone Numbers.
After several tries, Found the phone number pattern.
Verification code is sent to the phone number and it is required in order to register [Problem is that I don’t have access to the phone number that I added and can’t add different pattern].
Intercepting requests and responses, I found that the Verification Code is being Leaked in the Response.
Confirmed the verification code and registered successfully.
Navigated to Login Page (Required Username and password to Login).
Unable to Login [Response Message: Username is not Valid (Knowing that I used the same username in registration)].
Added the registered phone number instead of the username [Logged In Successfully].
Server is running Xampp. I searched for File Upload endpoints [All picture uploads were validated and protected].
After 2 hours of browsing the dashboard and checking every single functionality, I found an endpoint that is missing to validate the upload icon extension.
Uploaded php reverse shell and navigated to the directory where it is stored [Shell didn’t execute and PHP wasn’t rendered in the page].
Checked the requests and found (.do) in the request URL [Although application is running Xampp, But it is using Java in the backend].
Wrote simple jsp reverse shell, Then uploaded it.
I got Remote Code Execution (RCE) and accessed the server as Administrator.
Press enter or click to view image in full size

Timeline:

It took me 4 hours to finish this project.

Lesson Learned:

Chaining Vulnerabilities is a Mindset and a mentality gathered with time and experience.
Remote Code Execution is not a vulnerability but a process.
Dedication, persistence and patience when testing a target.
Check all possibilities before moving on to another target.
With experience and practice you will get faster in accomplishing such high level projects.
My experience in Bug Bounty helped me in RedTeaming and Pentesting projects.

Hope you enjoyed reading!

I created private bug bounty course to help struggled hunters find valid bugs and earn bounties.

If you are struggling in finding valid bugs or earning enough bounties, you just need to enroll and your mindset about approaching bug bounty hunting will improve.

Check Student bounties and feedbacks and enroll now: https://ahmadhalabi.net/course

Press enter or click to view image in full size

You can follow me on: LinkedIn / Twitter / Instagram / My Website / Youtube .

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Kind Regards.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-03_write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed.md
original_filename: 2022-02-03_write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed.md
title: 'Write Up – Private Bug Bounty: RCE In EC2 Instance Via SSH With Private Key
  Exposed On Public Github Repository – $xx,000 USD'
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- cloud-security
- mobile-security
language: en
raw_sha256: a0caf09a7d7687eef980581848935b458f86407ca5270ac07b62e8af4cc775fe
text_sha256: d53c677af04b43f4191043d237e0abb33a64768013d6606a75bac1b49ef7b9dd
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# Write Up – Private Bug Bounty: RCE In EC2 Instance Via SSH With Private Key Exposed On Public Github Repository – $xx,000 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-03_write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `a0caf09a7d7687eef980581848935b458f86407ca5270ac07b62e8af4cc775fe`
- Text SHA256: `d53c677af04b43f4191043d237e0abb33a64768013d6606a75bac1b49ef7b9dd`


## Content

---
title: "Write Up – Private Bug Bounty: RCE In EC2 Instance Via SSH With Private Key Exposed On Public Github Repository – $xx,000 USD"
page_title: "PRIVATE BUG BOUNTY – RCE IN EC2 INSTANCE VIA SSH WITH PRIVATE KEY EXPOSED ON PUBLIC GITHUB REPOSITORY – @omespino"
url: "https://omespino.com/write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed-on-public-github-repository-xx000-usd/"
final_url: "https://omespino.com/write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed-on-public-github-repository-xx000-usd/"
authors: ["Omar Espino (@omespino)"]
bugs: ["Information disclosure"]
publication_date: "2022-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2940
---

WEB$$,$$$ USD[February 2022](/write-up-private-bug-bounty-rce-in-ec2-instance-via-ssh-with-private-key-exposed-on-public-github-repository-xx000-usd/)

# PRIVATE BUG BOUNTY – RCE IN EC2 INSTANCE VIA SSH WITH PRIVATE KEY EXPOSED ON PUBLIC GITHUB REPOSITORY

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about a private bug bounty program and why you can always check public repos on GitHub, because you will be surprised. 

**Report Summary** Hi REDACTED COMPANY team, I have found a private key exposed and a config file for ssh in some GitHub public repo from a REDACTED COMPANY employee that lead me to perform an RCE on AWS ec2 instance.

**Proof of concept** 1.- On GitHub, after some dorks (**/src/github.com/redacted_company IdentityFile** was the winner dork), I have found this public repository [https://github.com/redacted_employee/configfiles/tree/23114…51312/ssh/](https://github.com/redacted_employee/configfiles/tree/23114...51312/ssh/) that contains 2 files, config and pkey.pem file: config file:
  
  
  config: 
  Host devenv
  HostName X.X.X.X
  User ec2-user
  Port 22
  IdentityFile ~/configfiles/ssh/pkey.pem
  pkey.pem: (private key)

pkey.pem file:
  
  
  -----BEGIN RSA PRIVATE KEY-----
  - - - R E D A C T E D - - -
  SSBkb24ndCBrbm***REDACTED-SUSPECT-TOKEN***  - - - R E D A C T E D - - -
  -----END RSA PRIVATE KEY-----

2.- Then with any ssh client you just need to run: 
  
  
  # X.X.X.X was the IP of the Host that appears in the config file
  # you need to save the pkey.pem and change the key file permissions
  # with chmod 600 pkey.pem
  omespino@h0st:~# chmod 600 pkey.pem
  omespino@h0st:~# ssh -i pkey.pem ec2-user@X.X.X.X

3.- Once I got access I executed **sudo su** and **id** in order to confirm the admin privileges and we got **root** :
  
  
  [ec2-user@ip-172-X-X-X ~]$ sudo su
  root@ip-ip-172-X-X-X:/home/ec2-user# id
  uid=0(root) gid=0(root) groups=0(root)

**Environment and tools** Any ssh client  
\- My IP was X.X.X.X and I executed the sudo su and id commands to fingerprint the users and privileges and logged out immediately and I started to write this report, according to program terms no steps deeper were taken.

**Impact** The attacker can gain access to this ec2 instance and perform arbitrary commands as root. Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.[](https://www.facebook.com/sharer/sharer.php?u=/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/&display=popup&ref=plugin&src=share_button)

[](/write-up-private-bug-bounty-bypass-redacted-android-application-screen-lock-via-local-brute-forcing/)

[](/write-up-private-bug-bounty-firebase-database-exposed-by-misconfiguration-2000-usd/)

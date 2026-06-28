---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-17_security-concerns-with-the-e-tugra-certificate-authority.md
original_filename: 2022-11-17_security-concerns-with-the-e-tugra-certificate-authority.md
title: Security concerns with the e-Tugra certificate authority
category: documents
detected_topics:
- command-injection
- password-reset
tags:
- imported
- documents
- command-injection
- password-reset
language: en
raw_sha256: 85767d469b150f00f239664224c77709a6df5316725c1f5d49f8931d32179ae4
text_sha256: bbcf8c0c53d6e410806c6b5ee2191ed6c024ea867a361505b7f638a46875c73f
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Security concerns with the e-Tugra certificate authority

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-17_security-concerns-with-the-e-tugra-certificate-authority.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `85767d469b150f00f239664224c77709a6df5316725c1f5d49f8931d32179ae4`
- Text SHA256: `bbcf8c0c53d6e410806c6b5ee2191ed6c024ea867a361505b7f638a46875c73f`


## Content

---
title: "Security concerns with the e-Tugra certificate authority"
url: "https://ian.sh/etugra"
final_url: "https://ian.sh/etugra"
authors: ["Ian Carroll (@iangcarroll)"]
programs: ["e-Tugra"]
bugs: ["Default credentials", "Exposed registration page"]
publication_date: "2022-11-17"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 1900
---

Certificate authorities (CAs) are a critical backbone of internet security; when they are compromised, users lose the ability to securely connect to websites without fear of interception. Websites cannot insulate themselves against a fully-compromised CA, even if they normally use other CAs.

In many regards, certificate authorities are audited comprehensively against industry-specific audit standards. Certificate authorities also [routinely](https://en.wikipedia.org/wiki/DigiNotar) [get](https://arstechnica.com/information-technology/2022/11/state-sponsored-hackers-in-china-compromise-certificate-authority/) [hacked](https://arstechnica.com/information-technology/2011/09/comodo-hacker-i-hacked-diginotar-too-other-cas-breached/). Despite this, **not a single certificate authority runs a bug bounty program** , and of the major CAs, only GlobalSign and Let’s Encrypt even offer a `security.txt` to help disclose issues. Only an annual penetration is generally required of CAs.

As a result, I suspected that there was a lot of low-hanging fruit in certificate authorities, which malicious actors may have already discovered. I decided to look into several certificate authorities, in particular looking into the applications they are exposing to the internet.

I ended up taking a deep look into e-Tugra, a Turkey-based certificate authority trusted by Apple, Google, Mozilla, and other clients. I found a number of alarming issues that worry me as to the security practices inside their company, and want to share the details in hope of preventing these issues in the future. While every company suffers from security issues, these appear to be concerning issues in critical infrastructure, and I am disclosing them quickly in order to raise awareness of the potential risks.

## Administrative tools with default passwords

e-Tugra appears to use a common framework for many of their internal tools. They have a similar appearance, but also similar conspicuous text on their homepages.

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/85866eb0-5bec-4d96-91cd-75841e8c564a/e-Tugra_Default_Password/w=1920,quality=90,fit=scale-down)

Although it’s written in Turkish, the homepage helpfully offers the default credentials for this application are either `admin / admin123%` or `user / user123%`. This is quite alarming to see on a certificate authority’s production website! Nevertheless, these credentials did not work at first, until I stumbled upon another application:

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6f37af81-9b2a-479c-b70d-28e2a58c8023/Screenshot_2022-11-13_at_3.13.27_AM/w=1920,quality=90,fit=scale-down)

This appeared to be a server storing logs from their other applications, and **the default password worked**! This allowed logging in and viewing over 14 million log entries, as well as adding other users to the application as an administrator. Notably, there was no other user configured, so the default passwords would have had to be willingly used by e-Tugra staff in order to access this system.

Additionally, there were many log lines referencing [EJBCA](https://www.ejbca.org/), which is the software used by many certificate authorities as part of their issuance infrastructure. As a result, **this system was likely connected to other systems with the ability to issue certificates**. Luckily, the log lines did not appear to have sensitive or secret values in them, albeit many are in Turkish which I do not speak.

## Administrative tools with sign-up enabled(!)

I tried the default passwords on another similar e-Tugra application written with the same framework. Luckily, they had been changed and did not work. However, there was an additional button on the login form — **to sign up for a new account**! I registered an account with the email `admin2@admin2.com` and was immediately logged into into a massive administrative panel.

This administrative tool contains every email message, text message, and uploaded document sent to and from e-Tugra’s systems. It contains numerous amounts of PII including uploaded Turkish IDs, email addresses, phone numbers, and physical addresses.

![568k sent emails from e-Tugra systems](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/d233c555-5891-43c9-8156-c8449ed8a16b/Screenshot_2022-11-13_at_3.41.27_AM/w=1920,quality=90,fit=scale-down)568k sent emails from e-Tugra systems

![Documents uploaded to e-Tugra](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8aa6bb73-d341-4d21-a2f6-66277cf478ae/Screenshot_2022-11-13_at_3.43.50_AM/w=1920,quality=90,fit=scale-down)Documents uploaded to e-Tugra

This is, undoubtedly, a very serious issue. It is likely also a massive data breach of personal information. However, for certificate authorities, they also have a unique role of validating control of certain things like domain names. One way certificate authorities do this is by sending a unique code to specific email addresses, like `admin@yourdomain.com`, and having you send them that code as proof of control of the email address.

_(Side note: Email validation is the only allowed domain validation method that relies on “secret” values. DNS and HTTP validation methods use public values that are then hosted on the domain, but email validation is the only one to have secrets which must be kept from the user.)_

This issue in e-Tugra’s system allowed me to view the contents of any email sent to any e-Tugra user. Here, they are sending me a confirmation code to my own email address, but I could view these for any user:

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/5db9556d-47b6-4c6c-a1fd-48def1081a08/Screenshot_2022-11-13_at_3.40.47_AM/w=1920,quality=90,fit=scale-down)

In this same administrative panel, we can see that it has an email template for proving control of a domain name. We can also edit the template, which is extremely concerning in itself. It appears this template may be presently unused by e-Tugra at the moment, however any domain validation previously completed through this system likely should be considered invalid.

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e1bb8e75-fdda-43c0-8699-80b04fd1db61/Screenshot_2022-11-13_at_3.47.55_AM/w=1920,quality=90,fit=scale-down)

## Customer-facing panel issues

e-Tugra also offers a customer panel for customers to purchase certificates. Using the above issues, we could capture password reset emails and take over any account on this site. Without going into specific details due to them potentially not being resolved, there were numerous additional issues in this customer panel:

  * Several trivial and critical issues which could lead to user account takeover

Hopefully I can add more details to these issues in the future, but I must stress how trivial they are. I was unable to test the customer panel in detail because it did not accept foreign credit cards, despite my best attempts. However, customer panels for certificate authorities often allow re-issuing existing certificates without further validation. These would be a critical issue for any user of e-Tugra.

## Response

Under the [CA/B Forum Network Security Guidelines](https://cabforum.org/wp-content/uploads/CA-Browser-Forum-Network-Security-Guidelines-v1.7.pdf), e-Tugra is required to remediate critical security vulnerabilities within 96 hours. I disclosed all of these issues in detail to e-Tugra, but have decided to publish this post without waiting for approval from e-Tugra due to the potential ecosystem risks.

  * **Nov 13, 2022 4:10** : Initial contact to e-Tugra about administrative systems (no response)
  * ********Unknown******** : Administrative systems no longer reachable on the internet
  * **Nov 13, 2022 18:50** : Second set of issues reported to e-Tugra, follow-up on initial issues that appeared fixed
  * **Nov 14, 2022 8:35** : Initial reply from e-Tugra saying they are working on resolution
  * **Nov 14, 2022 17:18** : Asked how to report security issues in the future (no response)
  * **Nov 16, 2022 22:52:** Notified e-Tugra of impending disclosure (no response)
  * **Nov 17, 2022** : Disclosed this post

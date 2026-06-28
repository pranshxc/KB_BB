---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-04_en-account-takeover-and-sensitive-data-leakage-via-cors-misconfiguration.md
original_filename: 2020-07-04_en-account-takeover-and-sensitive-data-leakage-via-cors-misconfiguration.md
title: EN \| Account Takeover and Sensitive Data Leakage via CORS Misconfiguration
category: documents
detected_topics:
- cors
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- cors
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: bf289a427fd1ce8709ede1a67342c29185feea6a90429764e207785d90a52ee0
text_sha256: 7f53a7dc398796745cdcb5ecee84233dab8d508cdec183fe49aa2062848ea5e6
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# EN \| Account Takeover and Sensitive Data Leakage via CORS Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-04_en-account-takeover-and-sensitive-data-leakage-via-cors-misconfiguration.md
- Source Type: markdown
- Detected Topics: cors, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `bf289a427fd1ce8709ede1a67342c29185feea6a90429764e207785d90a52ee0`
- Text SHA256: `7f53a7dc398796745cdcb5ecee84233dab8d508cdec183fe49aa2062848ea5e6`


## Content

---
title: "EN | Account Takeover and Sensitive Data Leakage via CORS Misconfiguration"
page_title: "EN \| Account Takeover and Sensitive Data Leakage via CORS Misconfiguration Lütfü Mert Ceylan"
url: "https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc/"
final_url: "https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc/"
authors: ["Lütfü Mert Ceylan (@lutfumertceylan)"]
bugs: ["CORS misconfiguration", "CSRF", "Account takeover"]
publication_date: "2020-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4444
---

# 

EN \| Account Takeover and Sensitive Data Leakage via CORS Misconfiguration

July 04, 2020

![](https://portswigger.net/web-security/images/attack-on-cors.svg)  

In June of this year, I found a CORS Misconfiguration vulnerability in a datacenter company. The system was very simple, a PUT command sent to the API Server both changed the account email and showed all the data of the account in JSON format as Response. Then, I reported this weakness and the company rewarded me with a $$$ bounty. Also, I would like to thank [Bugra Eskici](https://twitter.com/bugraeskici) , who helped me a lot to detect this vulnerability.

### Recon

I was reviewing the responses by sending requests to the system. When I looked at request header, I saw that the “Origin” attribute was defined. The vulnerable site was defined in the “Origin” attribute as a value, and this value was also defined in the “Access-Control-Allow-Origin” attribute in the Response. Also, the “Access-Control-Allow-Credentials” value was “true”.

### Is it vulnerable?

I write evil.com as the value to Origin. And Bingo! The response status was “200 OK” and evil.com was also included in the Access-Control-Allow-Origin attribute.  

![](/images/corsheader.png)  

That is, there was a CORS Misconfiguration vulnerability.

### Double Shot!!

I can change the account email with a simple PUT request. Moreover, the server was showing the sensitive data of the account as Response. Then, I have created a simple script for both changing email and stealing sensitive data.

You can find the script I created in my tweet:

> A script you can use for Sensitive Data Leakage via CORS Misconfiguration 🕵️🧙‍♂️  
>  
> Source Code: <https://t.co/TroWuo34cJ>[#bugbountytips](https://twitter.com/hashtag/bugbountytips?src=hash&ref_src=twsrc%5Etfw) [#bugbountytip](https://twitter.com/hashtag/bugbountytip?src=hash&ref_src=twsrc%5Etfw) [#bugbounty](https://twitter.com/hashtag/bugbounty?src=hash&ref_src=twsrc%5Etfw) [#cybersecurity](https://twitter.com/hashtag/cybersecurity?src=hash&ref_src=twsrc%5Etfw) [#infosec](https://twitter.com/hashtag/infosec?src=hash&ref_src=twsrc%5Etfw) [#ethicalhacking](https://twitter.com/hashtag/ethicalhacking?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/e0hId2BKmG](https://t.co/e0hId2BKmG)
> 
> — Lütfü Mert Ceylan (@lutfumertceylan) [June 21, 2020](https://twitter.com/lutfumertceylan/status/1274829687177515011?ref_src=twsrc%5Etfw)

  

With the script, I changed the e-mail address by sending a PUT request. (Account Takeover) ![](/images/putreqcors.jpg)  

Then, I sent the Response containing sensitive data to a request-bin service with this script. ![](/images/respcors.jpg)  

And, sensitive data sent the attacker’s site. ![](/images/sensdatacors.jpg)  

So I was able to both change the e-mail address of the victim account and steal sensitive data. Both vulnerabilities were caused by CORS Misconfiguration. As I have explained, it is possible to exploit these vulnerabilities with a simple script.

### The end :

10 June 2020 - Report sent  
10 June 2020 - Confirmed  
11 June 2020 - I was awarded a $$$ bounty  

**__Tags:** [account takeover](https://lutfumertceylan.com.tr/tags/#account-takeover),  [Bug Bounty](https://lutfumertceylan.com.tr/tags/#bug-bounty),  [bugbounty](https://lutfumertceylan.com.tr/tags/#bugbounty),  [cors misconfiguration](https://lutfumertceylan.com.tr/tags/#cors-misconfiguration),  [hack](https://lutfumertceylan.com.tr/tags/#hack),  [poc](https://lutfumertceylan.com.tr/tags/#poc),  [sensitive data leak](https://lutfumertceylan.com.tr/tags/#sensitive-data-leak),  [write-up](https://lutfumertceylan.com.tr/tags/#write-up)

#### Share on

[ __Twitter](https://twitter.com/intent/tweet?text=https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc/ "Share on Twitter") [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc/ "Share on Facebook") [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc/ "Share on LinkedIn") [Previous](https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc0/ "EN | Account Takeover and Sensitive Data Leakage via CORS Misconfiguration ") [Next](https://lutfumertceylan.com.tr/posts/alertbox-manipulation-base64/ "EN | Alert-box Message Content Manipulation based Base64 ")

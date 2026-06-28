---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-31_hunting-on-aspx-application-for-p1s-unauthenticated-soaprce-info-disclosure.md
original_filename: 2020-05-31_hunting-on-aspx-application-for-p1s-unauthenticated-soaprce-info-disclosure.md
title: Hunting on ASPX Application For P1's [Unauthenticated SOAP,RCE, Info Disclosure]
category: documents
detected_topics:
- idor
- xss
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: a7047196317e67adfd89969f0c8ad80bc2fd27560953ce0bf6fbd721bf500668
text_sha256: 206c82ebfaab73fa62eccfa0ca5f10e712e64c8b9ec10af8a46183dacc4a8d6e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting on ASPX Application For P1's [Unauthenticated SOAP,RCE, Info Disclosure]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-31_hunting-on-aspx-application-for-p1s-unauthenticated-soaprce-info-disclosure.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a7047196317e67adfd89969f0c8ad80bc2fd27560953ce0bf6fbd721bf500668`
- Text SHA256: `206c82ebfaab73fa62eccfa0ca5f10e712e64c8b9ec10af8a46183dacc4a8d6e`


## Content

---
title: "Hunting on ASPX Application For P1's [Unauthenticated SOAP,RCE, Info Disclosure]"
url: "https://elmahdi.tistory.com/3"
final_url: "https://elmahdi.tistory.com/3"
authors: ["ElMahdi Mrhassel (@ElMrhassel)"]
bugs: ["RCE", "Information disclosure", "IDOR"]
publication_date: "2020-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4541
---

## 티스토리 뷰

**[카테고리 없음](/category)**

### [Hunting on ASPX Application For P1's [Unauthenticated SOAP,RCE, Info Disclosure]](/3)

elmahdi 2020\. 5. 31. 18:52 

Hi, I wanna share with you how i found a P1 Vulnerabilities in a private program.  
  
At first i grabbed subdomains and titles via assetfinder and, then resolved them using httprobe and extracted the the title of the responsive ones with get-title.  
  
I started looking at the titles and i saw that there is a title that had "LOGIN" in it, i opened that page in my browser and i found that the website is an ASPX Application, the page didn't have any link for me to register, so i tried directories discovery with ffuf in orded find pages and sensitive files but i didn't find anything interesting so i moved to the next strep wich is Google search engine, i just made a basic dork search :
  
  
  site: care.redacted.com

![](https://blog.kakaocdn.net/dna/rsFgZ/btqEu6oTNmp/AAAAAAAAAAAAAAAAAAAAAJ8gw3QaUynkDiz6Hb4YNHA7GprWUqbQ6IsCUaN5Mu2n/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=WS1p0SJ4hslGFnAAIP1kT%2Fqk9Fk%3D)

I opened all the pages and i noticed that there's a page for registeration but i didn't have the informations needed to do register myself :( , I clicked on CTRL+U to see if there are any JS Files that are included in the page and i found these two Files

![](https://blog.kakaocdn.net/dna/7Owyh/btqEwhQlvDE/AAAAAAAAAAAAAAAAAAAAABz3bakZyX7y6G0mGqVshMLaIP5iJy-xzWhoaZv0esAL/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=ui0WHwe%2FepdFo69M21pcaBpBHM0%3D)

#### Unauthenticated SOAP To [ Delete Documents, Get Informations Of Users, Access To Messages Of User , And Information Of Any Configuration of System, Other Functions ] : 

I opened the config.js file and i found a SOAP File.
  
  
  /services/CareRedactedredacted.asmx/ 

![](https://blog.kakaocdn.net/dna/m6wn9/btqEw3KCs0X/AAAAAAAAAAAAAAAAAAAAAHYIjzoXS1xN_-g2zXNna1FI2KL4N6lX4GvIM1Czds16/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=3qIpJdVw9hMcfVIdJZe7gqI4h0s%3D)

I opened the SOAP file and i found many user and system functions, i thought these function will surely require credentials, i coppied one of the urls that had a parameter id wich i gave it a radom value : 328915 and made the request.
  
  
  https://care.redacted.com/services/CareRedactedredacted.asmx/GetCustomerinfobydoc?Redacted=string&id=328915

Surprise, the website returned all the user sensitive informations without any authentication !!

#### Remote Command Execution in Telerik UI via CVE 2017-9248 And Critical IDOR thats Leak all Users PII : 

After i reported the SOAP bug, i opened the second JS File , i found that theres an URL For an ASPX page wich had an upload functionality( Ohh !!) I tried to upload malicious files such as [ aspx , asp , html ] but it didnt work, and even uploading a valid file ( PDF ) the website would not return the URL for the document or the id for it ( Oh shit ) but i noticed thats the website uses Telerik for uploading the files and managing them ( Amm ) I searched for Telerik Exploits in Google and i found a blog that showed how to Pwn Telerik.
  
  
  https://captmeelo.com/pentest/2018/08/03/pwning-with-telerik.html

i read it and understood and tried exploiting it, and It worked, I got access to Telerik Filemanager and uploaded a TXT file to confirm the vulnerability.

[via GIPHY](https://giphy.com/gifs/kung-fury-hackerman-3knKct3fGqxhK)

After reporting the RCE, I returned to the page and i clicked cheked the source code of the page, and i found that there is an aspx File inside the JS Code (Oh) that was for reading Documents !!
  
  
  var url = '/DocumentManagement/' + 'ViewDocumentImage.aspx?id=' + docid;

I Copied the URL And gave the id parameter a random number 15, the website returned PDF document wich had sensitive informations about a user without any authentication !!

#### Tomnomnom Tools : 

[github.com/tomnomnom/hacks/tree/master/assetfinder](https://github.com/tomnomnom/hacks/tree/master/assetfinder)

[github.com/tomnomnom/hacks/tree/master/get-title](https://github.com/tomnomnom/hacks/tree/master/assetfinder)

[github.com/tomnomnom/httprobe](https://github.com/tomnomnom/hacks/tree/master/assetfinder)

[ tomnomnom/hacks A collection of hacks and one-off scripts. Contribute to tomnomnom/hacks development by creating an account on GitHub. github.com ](https://github.com/tomnomnom/hacks/tree/master/assetfinder)

Special Thanks to Anass Sbai @Flashy911 for rewrite this post And thanks to 之𝛜𝓭 ン挨ぁ @zedsec009 ♥️♥️

공유하기

게시글 관리

__**ElMahdi - マハディ**

**공지사항**

**최근에 올라온 글**

  * [Cache Poisoning via SelfXSS⋯](/5)
  * [Bypassing the Redirect filt⋯](/4)
  * [Hunting on ASPX Application⋯](/3)
  * [XSS Stored On Messages In [⋯](/2)

**최근에 달린 댓글**

Total
  14,077

Today
  2

Yesterday
  0

**링크**

  * [Twitter](https://twitter.com/elmyuyu)
  * [Bugcrowd](https://bugcrowd.com/elmahdi)
  * [Hackerone](https://hackerone.com/elmahdi)

**TAG**

  * [xss](/tag/xss)
  * [cross site scripting](/tag/cross%20site%20scripting)

[more](https://elmahdi.tistory.com/tag)

[«](/archive/202605 "1개월 앞의 달력을 보여줍니다.") [2026/06](/archive/202606 "현재 달의 달력을 보여줍니다.") [»](/archive/202607 "1개월 뒤의 달력을 보여줍니다.") 일 | 월 | 화 | 수 | 목 | 금 | 토  
---|---|---|---|---|---|---  
| 1 | 2 | 3 | 4 | 5 | 6  
7 | 8 | 9 | 10 | 11 | 12 | 13  
14 | 15 | 16 | 17 | 18 | 19 | 20  
21 | 22 | 23 | 24 | 25 | 26 | 27  
28 | 29 | 30 |  |  |  |  
  
**글 보관함**

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-21_idor-facebook-malicious-person-add-people-to-the-top-fans.md
original_filename: 2018-07-21_idor-facebook-malicious-person-add-people-to-the-top-fans.md
title: 'IDOR FACEBOOK: malicious person add people to the ''Top Fans'''
category: documents
detected_topics:
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: 4e4cbeeae7d7613c5a4cde271923df2d686317cb48fe8841072ea9323584c535
text_sha256: 5da4dd66e843e8d22a076e7c7a489ebb8fbad6db05f426a3118eb2eba7f080df
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR FACEBOOK: malicious person add people to the 'Top Fans'

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-21_idor-facebook-malicious-person-add-people-to-the-top-fans.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4e4cbeeae7d7613c5a4cde271923df2d686317cb48fe8841072ea9323584c535`
- Text SHA256: `5da4dd66e843e8d22a076e7c7a489ebb8fbad6db05f426a3118eb2eba7f080df`


## Content

---
title: "IDOR FACEBOOK: malicious person add people to the 'Top Fans'"
page_title: "IDOR FACEBOOK: malicious person add people to the 'Top Fans'  - Update - أب ديت"
url: "https://www.updatelap.com/2018/07/the-malicious-person-add-people-to-top.html"
final_url: "https://www.updatelap.com/2018/07/the-malicious-person-add-people-to-top.html"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2018-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5794
---

##  **_Hi_**** __****_, hackers all over the world_**

**_[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9zl_bELlpAfZE6ZE6kRMciOrXZO5zI2AzUUChyphenhyphenpgax2kOjhouDETXPGnbBV9zOJ77enH5ZCJP3emKSkb6Tih33eoRU3sgcfUKtlcxs-FNMdYLeDTcwAUXcOHkWpkQhsxiarO34z4Nn_rU/s640/pornhub_bug_bounty_program.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9zl_bELlpAfZE6ZE6kRMciOrXZO5zI2AzUUChyphenhyphenpgax2kOjhouDETXPGnbBV9zOJ77enH5ZCJP3emKSkb6Tih33eoRU3sgcfUKtlcxs-FNMdYLeDTcwAUXcOHkWpkQhsxiarO34z4Nn_rU/s1600/pornhub_bug_bounty_program.jpg)  
_**

**_  
_**

_Today I will write the story of this publication that you published when I discovered his security issues on Facebook_

**__**

****  

  * **General information**

**Vulnerability Type**

  * _Privacy / Authorization_

Product Area

  * _Pages_

## 

  * **Technical details of the bug.**

_After digging around in Facebook looking for possible bug’s, I watched Facebook recently added a feature that allows fans to allow them to submit requests to be categorized in their favorite pages as their "Top Fans". Facebook has made this optional. If you want to send a request through the notification I received to add it to the list._

  

__After poking around in the HTTP requests, I found that the endpoint to send an request to join the "Top fans" list did not verify the sender is actually the sender.__

__The security flaw you have discovered allows a malicious person add users to the list of the "Top fans", without requiring the user to do so by sending or approving the request.__

  

  * __

Impact

__

__The impact of this situation on privacy is greater than security.__

  
__An attacker can know people who are interested in a page by simply following comments or like them and then add them to the list of the "Top fan s".__

  
__The attacker can not access any user data, but I can be interacting with a page, but I do not like content. I think my classification as one of my most unpopular users is a violation of my privacy.__

____

__

  * __

Steps

__
__
_1\. Facebook sends messages to all users who follow certain pages and Facebook considers them the "Top Fans" of the page.  
  
2\. The malicious person clicks on the notification of the "Top Fans" Facebook has sent him._

  

> https://web.facebook.com/top_fans/fan_opt_in_dialog/?page_id[PageID]&fan_id= [UserID]

__  

_[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlhkAv-0XRnuzHj82jo0dtI90_saFIVdWsFGFK9eC8zYutZLTRNxDqHbmv7hRXi3v2syW9eiE9MfW3guU_PHiU8fTdNMgwoqDcg54g45J9QEuSif3e-6yxvUoNVeIwL9dEUtPZwbQW88U3/s1600/ddture.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlhkAv-0XRnuzHj82jo0dtI90_saFIVdWsFGFK9eC8zYutZLTRNxDqHbmv7hRXi3v2syW9eiE9MfW3guU_PHiU8fTdNMgwoqDcg54g45J9QEuSif3e-6yxvUoNVeIwL9dEUtPZwbQW88U3/s1600/ddture.JPG)_

__  
__

_3\. After clicking on the "display Top Fans badge" icon, the request is intercepted._

_  
_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPolFvwEoO6E6KRSA31je_iX2f6J-cLhAbwm2puIaIFXi5fCmCkGoHd4B4qdDijp-lmH9iTk45AqvZ-O_2hJBbR3U2Q4Vz1B2AyuNtYxh7wS7sFa2bhNzK1Wb8VicWsHPAyVNCDFXK85sS/s640/dfdf.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPolFvwEoO6E6KRSA31je_iX2f6J-cLhAbwm2puIaIFXi5fCmCkGoHd4B4qdDijp-lmH9iTk45AqvZ-O_2hJBbR3U2Q4Vz1B2AyuNtYxh7wS7sFa2bhNzK1Wb8VicWsHPAyVNCDFXK85sS/s1600/dfdf.JPG)

_  
_

_  
4\. The attacker will modify the link to the victim's information_

> _https://web.facebook.com/top_fans/fan_opt_in/?status=OPTED_IN &entry_point=notification&creator_id[Page ID]&fan_id=[Victim ID]&dpr=1_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiw9C-QtebXpBUSrmgBf3OtcNRg5jXZ8OLkk0GGUNbRL14Wlssy8FMq6V6fxGkYgmXGTsJkj_7eveKCJrTpNSX2OlC83oR4eS41SqKvoFEaBqPLNJXm6MAAOM1PHrdK0qANt23JcojsR23/s640/dfgdfg.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiw9C-QtebXpBUSrmgBf3OtcNRg5jXZ8OLkk0GGUNbRL14Wlssy8FMq6V6fxGkYgmXGTsJkj_7eveKCJrTpNSX2OlC83oR4eS41SqKvoFEaBqPLNJXm6MAAOM1PHrdK0qANt23JcojsR23/s1600/dfgdfg.JPG)

_5\. Send the request after editing.  
  
6\. Now the target person has been added to the list of the "Top Fans" without his knowledge or to send the request._  
__  

> _حصلت على أعتراف من الفريق الامني بشركة Facebook لأكتشافي ثغره أمنية في خدمات الشركة الخاصه بالصفحات،الخلل الامني تم معالجته من قبل الشركة ولاكن بعد أعادتي للفحص تبين انني ما زلت أستطيع أعادة توليد الثغره لذلك تم أعادة النظر في الترقيع الامني، والثغره حاليا قيد المعالجه[pic.twitter.com/4D2HA19Uhd](https://t.co/4D2HA19Uhd)_
> 
> _— Update - أب ديت (@UpdateLap)[July 9, 2018](https://twitter.com/UpdateLap/status/1016145907849617409?ref_src=twsrc%5Etfw)_

  
  

  * PoC

  
  

  * _TimeLine_

_27-Jun-2018_ _T he report was submitted _

_27-Jun-2018_ _The vulnerability was accepted_

_29-__Jun-2018 The security team told me they were patching Vulnerability._

___29-__Jun-2018___ Re-testing and showing that the security defect still exists

_05-Jul-2018 Reopen the report_

_17-Jul-12018 Patches were done_

_19-Jul-2018 Reward paid_

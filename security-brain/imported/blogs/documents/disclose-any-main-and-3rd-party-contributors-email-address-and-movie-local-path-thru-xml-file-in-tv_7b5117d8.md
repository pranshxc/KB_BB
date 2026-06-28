---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-24_disclose-any-main-and-3rd-party-contributors-email-address-and-movie-local-path-.md
original_filename: 2019-07-24_disclose-any-main-and-3rd-party-contributors-email-address-and-movie-local-path-.md
title: Disclose any main and 3rd party contributors email address and movie local
  path thru XML file in Plex TV - plex.tv (Write Up)
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
language: en
raw_sha256: 7b5117d8840d7307295ee968280b7e1353f6d75b89bb83068edbb397f8975dd6
text_sha256: 51df02409333a2ba0ebfcd91675b1a768c0bb35216b305cc5d58984c092120e6
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose any main and 3rd party contributors email address and movie local path thru XML file in Plex TV - plex.tv (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-24_disclose-any-main-and-3rd-party-contributors-email-address-and-movie-local-path-.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7b5117d8840d7307295ee968280b7e1353f6d75b89bb83068edbb397f8975dd6`
- Text SHA256: `51df02409333a2ba0ebfcd91675b1a768c0bb35216b305cc5d58984c092120e6`


## Content

---
title: "Disclose any main and 3rd party contributors email address and movie local path thru XML file in Plex TV - plex.tv (Write Up)"
page_title: "Evan Ricafort | Blog: Disclose any main and 3rd party contributors email address and movie local path thru XML file in Plex TV - plex.tv (Write Up)"
url: "https://blog.evanricafort.com/2019/07/business-logic-plex-tv.html"
final_url: "https://blog.evanricafort.com/2019/07/business-logic-plex-tv.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Plex"]
bugs: ["Information disclosure", "Internal path disclosure"]
publication_date: "2019-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5125
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiErbJs_jQYBQH3575avhSc4l0ZbjnWYSZTDaYZuHIotd4dQV3doHt7kyj25U7oH01CHOQr3-G5blmGJ9ka1mLN2oSqN23kd6bWkHwbYzjUzpDPa4upSEWd64gtocrij1JrwngNalNf/s640/Untitled+1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiErbJs_jQYBQH3575avhSc4l0ZbjnWYSZTDaYZuHIotd4dQV3doHt7kyj25U7oH01CHOQr3-G5blmGJ9ka1mLN2oSqN23kd6bWkHwbYzjUzpDPa4upSEWd64gtocrij1JrwngNalNf/s1600/Untitled+1.png)

  
  
Good day! In this article I will show you how I found a simple issue on chapterdb.plex.tv (Plex TV) that allow me to get their Contributors and 3rd party contributors email address and local path of the movies they contributed thru their feature that any user can download the XML file from the Contributors profile.

  
So I was having a good time hunting on this program since the last few weeks and I found some issues which is mostly a Business Logic issues that earned me a couple bucks.  
  
So long story short, here's my report timeline and proof of concept of this issue.  
  
  
**_\--Proof of Concept--_**  
  
1\. Go to http://chapterdb.plex.tv  
2\. Go to http://chapterdb.plex.tv/contributors  
3\. Select any contributors from the page. in my demo I will use this one (http://chapterdb.plex.tv/browse?createdBy=<REDACTED>)  
4\. Select any movie from dongafford's page. in my demo I will use this one (http://chapterdb.plex.tv/browse/<REDACTED>)  
5\. In the upper right corner you will see a Download button, hover your mouse cursor into the button and click the XML (I prefer the XML download so that you can easily check the datas)  
6\. Download the XML file  
7\. Open the XML file and see the result  
  
  
Result (Demo PoC):  
  

> _<?xml version="1.0"?>-<chapterInfo xml:lang="eng" xmlns="http://jvance.com/2008/ChapterGrabber" confirmations="11" client="ChapterGrabber 4.4" extractor="ChapterGrabber 4.4" version="2"><title>Tommy Boy</title>_  
> 
>
>> _- <ref><chapterSetId><REDACTED></chapterSetId></ref>__-**< source><name>D:\BDMV\PLAYLIST\00001.mpls</name> <\---- PATH LEAKAGE<type>Blu-Ray</type>**<hash>a50136227ca54eed0b46fff609511448</hash><fps>23.976023976023978</fps><duration>01:37:03.8180000</duration></source>__- <chapters><chapter name="School Daze" time="00:00:00"/><chapter name="Sandusky, Ohio" time="00:05:28.7450666"/><chapter name="A Perfect 10" time="00:13:02.5317333"/><chapter name="Cow Tipping" time="00:15:25.8415777"/><chapter name="Wonder Boy" time="00:18:21.8507333"/><chapter name="The Luckiest Man in the World" time="00:21:12.5629555"/><chapter name="Playing with Your Dinghy" time="00:27:35.4037333"/><chapter name="The Future of Callahan" time="00:30:30.2867777"/><chapter name="On the Road" time="00:33:04.4407777"/><chapter name="Whadya Do?" time="00:36:42.6170666"/><chapter name="Bad Mommy" time="00:39:11.1404444"/><chapter name="Road Kill" time="00:41:26.6091111"/><chapter name="Fat Guy in a Little Coat" time="00:46:19.1930666"/><chapter name="Oh, Baby" time="00:49:16.4952000"/><chapter name="A Pretty New Pet" time="00:52:27.7279111"/><chapter name="Guarantee" time="00:55:45.3836888"/><chapter name="Spanky" time="00:59:10.9640666"/><chapter name="On the Road to Success" time="01:02:14.6475777"/><chapter name="Heading Home" time="01:06:30.6950222"/><chapter name="Killer Bees" time="01:10:25.4712444"/><chapter name="Fly Boys" time="01:12:45.9866222"/><chapter name="Zalinsky Auto Parts" time="01:17:36.6102888"/><chapter name="I've Got a Plan" time="01:23:54.1541111"/><chapter name="The New President" time="01:30:16.9114888"/></chapters>**< createdBy>d[REDACTED][[email protected]](/cdn-cgi/l/email-protection)</createdBy> <\--- Contributor's Email Address<createdDate>2011-01-29T11:09:50.35-05:00</createdDate><updatedBy>a[REDACTED][[email protected]](/cdn-cgi/l/email-protection)</updatedBy> <\--- 3rd Party Contributor's Email Address**<updatedDate>2017-12-05T01:11:36.2260171-07:00</updatedDate></chapterInfo>_

  
  
_**\--Report Timeline--**_  
_**  
**_Report Title: Vulnerability Issue (Business Logic Issue - Information Disclosure of Contributors in http://chapterdb.plex.tv)  
Reported: Wed, Jul 3, 2019, 5:05 PM  
First Response: Mon, Jul 8, 11:53 PM  

> _Hi Evan,__  
> __We are still looking into this issue.__  
> __Regards,__The Plex Security Team_

Fixed: Fri, Jul 12, 9:18 AM  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjoV_mhFI130DAtpQ8WQrMhiHEdz_0OlJyIjBYZExHrVyuv-nM39N4RW3AHYXcBCL98hFUxjIblrDLTVrq40woElNOTwrvxE1KC7b9LSAbztnjt5ZRArK3gf0w_HVJHhcgWBLuOdlR/s640/Screenshot_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjoV_mhFI130DAtpQ8WQrMhiHEdz_0OlJyIjBYZExHrVyuv-nM39N4RW3AHYXcBCL98hFUxjIblrDLTVrq40woElNOTwrvxE1KC7b9LSAbztnjt5ZRArK3gf0w_HVJHhcgWBLuOdlR/s1600/Screenshot_2.png)  

> _Hello,  
>  We believe the issue is fixed, but since we don't maintain the code for this project ourselves, we're reaching out to the original developer to make sure. It seems to be fixed on most, but not all movies.  
> Regards,  
> The Plex Security Team_

Final Decision: Not qualified for a bounty since as what they have said on their last email, they didn't own the code for ChapterDB and they reached out the owner and says that _"He's not even actively maintaining the code anymore (which is why it's a read-only archive). As he is no longer involved or maintaining the project anymore."_  
  
Public Disclosure Request: Tue, Jul 23, 10:05 AM  
  
Fixed  
  
I hope you enjoy this write up. have a great day!  
  

_**“There are no shortcuts to any place worth going.”**_

_Beverly Sills_

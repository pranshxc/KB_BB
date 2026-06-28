---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-04_xss-because-of-wrong-content-type-header.md
original_filename: 2017-08-04_xss-because-of-wrong-content-type-header.md
title: XSS Because of wrong Content-type Header
category: documents
detected_topics:
- xss
- command-injection
- csrf
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- csrf
- api-security
- cloud-security
language: en
raw_sha256: a1e44d9244b74b6b6fe5617af4c17c761be673c9a35dc9cffb754f6a2653c219
text_sha256: 32b1d1be9d5682aea8af1312cac6a5b622980d4c77a95942a15fdcce49405a9b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Because of wrong Content-type Header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-04_xss-because-of-wrong-content-type-header.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a1e44d9244b74b6b6fe5617af4c17c761be673c9a35dc9cffb754f6a2653c219`
- Text SHA256: `32b1d1be9d5682aea8af1312cac6a5b622980d4c77a95942a15fdcce49405a9b`


## Content

---
title: "XSS Because of wrong Content-type Header"
url: "https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html"
final_url: "https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html"
authors: ["Noman Shaikh (@nomanali181)"]
programs: ["Internshala"]
bugs: ["XSS"]
publication_date: "2017-08-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6132
---

###  XSS Because of wrong Content-type Header 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ August 04, 2017  ](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html "permanent link")

Hello All,  
  

###  XSS because of Wrong content type in InternShala.com

  
**Internshala :**  

> **Internshala is an internship platform, this website helps students find internships with organisations in India -[wiki](https://en.wikipedia.org/wiki/Internshala)**

  
While checking this site I got an endpoint which didn't had CSRF protection.  
I can change the user details (name, address,etc) Not email :(  
  
  
One thing that was weird with that endpoint was that it was giving a JSON response  
But the content type header was not : application/javascript  
  

Rather it was set as : text/html

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz9OXKLUTofQawNue1K-UuQLE4oBrRBNaGDJ12VtzBaO6SfSbrjxWaRBPW2EU0r42iP4iFUSKty_KcDSecRy7DVceKIUyu6MC-bnyfYLz_fetY-hd-5ScxKGK26cLr-wTdRLcDkFLHq7W6/s1600/intern1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz9OXKLUTofQawNue1K-UuQLE4oBrRBNaGDJ12VtzBaO6SfSbrjxWaRBPW2EU0r42iP4iFUSKty_KcDSecRy7DVceKIUyu6MC-bnyfYLz_fetY-hd-5ScxKGK26cLr-wTdRLcDkFLHq7W6/s1600/intern1.png)

  

  

  

I was fiddling with that as I knew if we can inject html then we can get XSS here :D

  

  

But they had filters so it was just HTML Injection -_- that isn't cool to report 

  

  

But there was another parameter current_city_administrative_area_level_2

changing its value caused and error 

  

####  Lets Build Payload 

  

**Problem no (1)**

  

White space was not allowed between text and neither **** forward slash /**** was allowed

  

so I use + for that :p 

Payload : <h1+onmouseover

  

Now i was able to inject event handlers :D 

  

**Problem no (2)**

  

Next alert and prompt was blocked :v

  

But they forgot confirm :D

Payload : <h1+onmouseover=confirm

  

**Problem no (3)**

  

Parentheses/brackets ( ) were blocked :3

  

so i use backtick **`** instead 

  

Payload : <h1+onmouseover=confirm`1`

  

**Problem no (4)**

  

we need to end the tag with > but this wasn't allowed -_-

so i use +%0a for that :v 

  

Payload : <h1+onmouseover=confirm`1`+%0a>Lol</h1>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8E9VZKvyjj3FY39_IC1SIikA70krYnd2K42NViKSeqwimapSEPzh6IqP4dqGFuHOJqU3HjxKjMK7NcOnih087Vp79QvPd2Vcj-r64N_HEwRrrFepB6PTm6qN52HvRIsc0FcPNxnjQ8SZb/s1600/intern3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8E9VZKvyjj3FY39_IC1SIikA70krYnd2K42NViKSeqwimapSEPzh6IqP4dqGFuHOJqU3HjxKjMK7NcOnih087Vp79QvPd2Vcj-r64N_HEwRrrFepB6PTm6qN52HvRIsc0FcPNxnjQ8SZb/s1600/intern3.png)

  

  

Finally it worked ^_^  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXS9-VMfTlFMbdFCS91rnG4sF32bzVhtIM0eT_hswYIkV6T0DFelcrdlYGrrLeGAJXc0WjYANoJFJomFILCK8h2Ylh6NMZvX_sAjf1O1q7C5p8CnZYnBRpUpL1eS0q5f_quYlM_5sKbf9w/s1600/intern2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXS9-VMfTlFMbdFCS91rnG4sF32bzVhtIM0eT_hswYIkV6T0DFelcrdlYGrrLeGAJXc0WjYANoJFJomFILCK8h2Ylh6NMZvX_sAjf1O1q7C5p8CnZYnBRpUpL1eS0q5f_quYlM_5sKbf9w/s1600/intern2.png)

  
So keep an eye at the Content-type header when there is JSON response  
  
My Reaction  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHi_ZfRlppk70M5Lzeo_ObTr_qzjdBOeET3CakjsxUQnllj73fcx-NSXtExDsMkjOmzQOjOH3e24lwgvCCe36VDF9OYUud8BkQE3t9JMUxpbyNs8RERGG2VXhpOsONP-Z_0THHOwgPu1sO/s400/party.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHi_ZfRlppk70M5Lzeo_ObTr_qzjdBOeET3CakjsxUQnllj73fcx-NSXtExDsMkjOmzQOjOH3e24lwgvCCe36VDF9OYUud8BkQE3t9JMUxpbyNs8RERGG2VXhpOsONP-Z_0THHOwgPu1sO/s1600/party.jpg)

  
  
  
  
**My XSS Guru's**  
**@[soaj1664ashar](https://twitter.com/soaj1664ashar)**  
**@[brutelogic](https://twitter.com/brutelogic)**  
**@[Asystolik](https://twitter.com/Asystolik)**  
  
  
Note : This bug is Patched by InternShala Team  
  
  
Thanks

[Bugbounty](https://bugbaba.blogspot.com/search/label/Bugbounty) [XSS](https://bugbaba.blogspot.com/search/label/XSS)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/04511565033610353821)[4 August 2017 at 09:04](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501862688737#c7942606324825099252)

nice and best of luck for future hunting bro.  

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/7942606324825099252)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[4 August 2017 at 09:31](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501864290967#c6063738995776911148)

Thanks 

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/6063738995776911148)

Replies

Reply

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/03676986592001453849)[4 August 2017 at 09:43](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501865020260#c6907973603172475785)

Nice! write up! 

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/6907973603172475785)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[4 August 2017 at 09:52](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501865579809#c4820115963813112889)

Thanks :)

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/4820115963813112889)

Replies

Reply

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/08287865062880417062)[4 August 2017 at 09:47](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501865264895#c6403044381950884915)

Awesome Writeup, Dear!

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/6403044381950884915)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[4 August 2017 at 09:52](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501865565398#c3958239799189802010)

I am Glad that you liked it :)

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/3958239799189802010)

Replies

Reply

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[securitybreaker](https://www.blogger.com/profile/12905665605970134507)[4 August 2017 at 10:21](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501867266139#c283118594639190050)

Awsome After Long time Read the Cool Bypass :)

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/283118594639190050)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[4 August 2017 at 10:30](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501867823438#c5869175124502748988)

Thanks :)

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/5869175124502748988)

Replies

Reply

Reply

  5. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMLI_RE5oqAlwJTRRSqXxdTExxO17N3esDisktVNcYuaFviLBIR9dUD29Zul4tCuBWSKKewFnJ6ULEUH__wn1sfGrnc8oNObYkL_Iv-qvFgDxPolKzsIBatmDFFb1kEg/s45-c/15822537_1820492461547015_6989773609366303757_n.jpg)

[An0n 3xPloiTeR](https://www.blogger.com/profile/05328174510396339878)[5 August 2017 at 18:37](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1501983422010#c494644426490649315)

BugChod Baba Zindabad <3 :D  

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/494644426490649315)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/01722426665651907286)[7 August 2017 at 02:30](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1502098222662#c7412435453887810510)

Really cool!!

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/7412435453887810510)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[9 August 2017 at 10:04](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1502298241364#c2866627173986956068)

Thanks :) 

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/2866627173986956068)

Replies

Reply

Reply

  7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/11898247661445437170)[9 August 2017 at 00:30](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1502263818553#c4124604067844310364)

Cool Write Up O:) 

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/4124604067844310364)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Noman Shaikh](https://www.blogger.com/profile/14849012228586858561)[9 August 2017 at 10:04](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1502298263083#c2737839933520345632)

Thanks sir ^_^

[Delete](https://www.blogger.com/comment/delete/6751850223539484706/2737839933520345632)

Replies

Reply

Reply

  8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[javascript:alert(1)](https://www.blogger.com/profile/10516649045342262327)[15 September 2017 at 12:09](https://bugbaba.blogspot.com/2017/08/xss-because-of-wrong-content-type-header.html?showComment=1505502578189#c5499463841450249602)

Thanks bro <3 learned something new <3

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/5499463841450249602)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/6751850223539484706?po=3889648471582142790&hl=en-GB&saa=85391&origin=https://bugbaba.blogspot.com&skin=contempo)

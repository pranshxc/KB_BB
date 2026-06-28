---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-05_site-wide-csrf-on-a-popular-program.md
original_filename: 2020-02-05_site-wide-csrf-on-a-popular-program.md
title: Site wide CSRF on a popular program
category: documents
detected_topics:
- access-control
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 7782fb1c3281bf0c1d18a483dba7e910debac82be64aa79a895d2554ce474b68
text_sha256: 5310635dbeb46a2f9430ba37b903f2a742db12dce19778af595d2e725966b73f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Site wide CSRF on a popular program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-05_site-wide-csrf-on-a-popular-program.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `7782fb1c3281bf0c1d18a483dba7e910debac82be64aa79a895d2554ce474b68`
- Text SHA256: `5310635dbeb46a2f9430ba37b903f2a742db12dce19778af595d2e725966b73f`


## Content

---
title: "Site wide CSRF on a popular program"
url: "https://fellchase.blogspot.com/2020/02/site-wide-csrf-on-popular-program.html"
final_url: "https://fellchase.blogspot.com/2020/02/site-wide-csrf-on-popular-program.html"
authors: ["Ajinkya Pathare (@fellchase)"]
bugs: ["CSRF"]
publication_date: "2020-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4786
---

###  Site wide CSRF on a popular program 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ Wednesday, February 05, 2020  ](https://fellchase.blogspot.com/2020/02/site-wide-csrf-on-popular-program.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmtF9WS8SfAbZuXZ8kVH5MpjOtzF_WmfrRdJf4pkPEg4I5u5GoNFq__kQ-1z0arVrCn9ZdF-2BR8drG0juDNzKLjcJnbjnsAb3GVGdRw6xjRCgBvQP_dBVSlNuGwOqL4o-fglC4oSvTEUS/w640-h404/feXpdV001o4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmtF9WS8SfAbZuXZ8kVH5MpjOtzF_WmfrRdJf4pkPEg4I5u5GoNFq__kQ-1z0arVrCn9ZdF-2BR8drG0juDNzKLjcJnbjnsAb3GVGdRw6xjRCgBvQP_dBVSlNuGwOqL4o-fglC4oSvTEUS/s1600/feXpdV001o4.jpg)

  
  
I found this bug in the same program that I explained in this post "[Authorization bug every bug hunter missed](https://fellchase.blogspot.com/2019/12/authorization-bug-that-every-bug-hunter-missed-on-a-popular-program.html)"  
  
I was moving through another target on this program when I noticed that there was no CSRF protection like there were no tokens etc so I wondered what they were using to prevent CSRF, I noticed some high entropy strings in headers but request worked without those headers as well so that wasn't protecting the website from CSRF. Request body consisted of JSON objects basically {key: "value"} pairs the assumption behind using it was that in a typical CSRF attack attackers don't send JSON payloads, so using JSON will naturally protect the application against CSRF.  
  
Here's where the trick comes in, It's actually more of check that you should perform while trying to find CSRF bugs, I spotted it on Twitter first you may or may not be familiar with it, here's how it works.  
  
It's very simple assume that server side framework is expecting some JSON input by default in the HTTP Request body so if it detects JSON object it will automatically parse it.  
  
But even if you send regular Content-Type that is application/x-www-form-urlencoded then also it will automatically parse that and start using it, problem is caused by not checking the Content-Type, it should be strictly application/json if you're expecting JSON input.  
  
So in this case to trigger CSRF I just sent regular CSRF payload but due to their negligence of not validating Content-Type header to be strictly JSON server accepted the regular HTTP parameters and triggered the CSRF.  

> <html>  
>  <form id="csrf" enctype="application/x-www-form-urlencoded" method="POST" action="https://www.example.com/api/REDACTED/PATH">  
>  <table>  
>  <tr><td>primaryPhoneType</td><td><input type="text" value="0101101101" name="primaryPhoneType"></td></tr>  
>  <tr><td>firstName</td><td><input type="text" value="YOUREcsrfedCongratsbtw" name="firstName"></td></tr>  
>  </table>  
>  <input type="submit" value="https://www.example.com/api/REDACTED/PATH">  
>  </form>  
>  <script type="text/javascript">  
>  document.getElementById('csrf').submit()  
>  </script>  
>  </html>

This could have been prevented by validating Content-Type header to be application/json  
  
In my case the server was accepting regular HTTP Post parameters along with expected JSON, so I reported the bug, but my report was marked as duplicate 😩 against someone who reported site wide CSRF using Flash.  
  
If you find JSON objects without CSRF protection being passed around in HTTP body try to change it to regular HTTP parameters and see if it works, if the server side application is accepting non JSON parameters then it'll process the input and you maybe able to get a CSRF.  

  

Happy bug hunting.

[bug bounty](https://fellchase.blogspot.com/search/label/bug%20bounty) [write up](https://fellchase.blogspot.com/search/label/write%20up)

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

[pforprathm](https://www.blogger.com/profile/02041147668402886093)[Wednesday, February 12, 2020 2:11:00 pm](https://fellchase.blogspot.com/2020/02/site-wide-csrf-on-popular-program.html?showComment=1581496867769#c1158598853301409293)

How you perform CSRF (By converting json to form body) ?? 

Reply[Delete](https://www.blogger.com/comment/delete/7751137191614975110/1158598853301409293)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7751137191614975110?po=8137872251640495195&hl=en-GB&saa=85391&origin=https://fellchase.blogspot.com&skin=contempo)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-09_simple-open-redirect-bypass.md
original_filename: 2022-08-09_simple-open-redirect-bypass.md
title: Simple Open Redirect Bypass.
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 3fb051837ba1b559c7988526da526a0aa4303552a4c449b8b7fa6132d9bfc84f
text_sha256: 8f968b01efd7d4d2454e1ec3c3adc82f59b00e7e8d3c2cc362e6cf3e9fc5ab51
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Simple Open Redirect Bypass.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-09_simple-open-redirect-bypass.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `3fb051837ba1b559c7988526da526a0aa4303552a4c449b8b7fa6132d9bfc84f`
- Text SHA256: `8f968b01efd7d4d2454e1ec3c3adc82f59b00e7e8d3c2cc362e6cf3e9fc5ab51`


## Content

---
title: "Simple Open Redirect Bypass."
page_title: "open redirect bypass"
url: "http://blog.h4rsh4d.com/2022/08/open-redirect-bypass.html"
final_url: "http://blog.h4rsh4d.com/2022/08/open-redirect-bypass.html"
authors: ["Harshad Gaikwad (@h4rsh4d)"]
bugs: ["Open redirect"]
publication_date: "2022-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2353
---

###  open redirect bypass 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ August 09, 2022  ](http://blog.h4rsh4d.com/2022/08/open-redirect-bypass.html "permanent link")

####  **Simple Open Redirect Bypass.**

  

Was checking the login page for XSS and other stuff. noticed that the login page had one hidden parameter. "returnToUrl"

Here, Application had some server-side protection which was checking user input URL's. 

Payload : https://google.com : forbidden

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh2YQAdxpuozwCm76eOG5qze7N1jSo71Ok2yf0MRukv6RLao_Lzp8YXn1HgpHFL6RGvQMXSz9RmM8dNZcgzvb3Tnh6nd-VAec2ywcsjfB6C3S0OEdYx-YOAt8emnwbU9oX04nGWCGz-Bx2AXzmKVX5aEW82GSG6wNMvHWFeeV4VJdI76Jli5nGwpRcd=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEh2YQAdxpuozwCm76eOG5qze7N1jSo71Ok2yf0MRukv6RLao_Lzp8YXn1HgpHFL6RGvQMXSz9RmM8dNZcgzvb3Tnh6nd-VAec2ywcsjfB6C3S0OEdYx-YOAt8emnwbU9oX04nGWCGz-Bx2AXzmKVX5aEW82GSG6wNMvHWFeeV4VJdI76Jli5nGwpRcd)

  
  

  
  

Payload : //google.com : forbidden

[![](https://blogger.googleusercontent.com/img/a/AVvXsEja1IJdRNk0YYiArD3qYeqvKHTmwaSf8dXHWuQslKiYJ_POXdvxrw28MMripuIDmJD0Np1ivEK_tOynpfsM1RhbJWIDQi7-np27y2gdcpkAEtug6lWvcaXmRWsnX_SCwoPRIvu2WXJaTOMKXifg2gXPhpxFaXcgvZw6PZd20rleJETbG_z_ReLcMHm8=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEja1IJdRNk0YYiArD3qYeqvKHTmwaSf8dXHWuQslKiYJ_POXdvxrw28MMripuIDmJD0Np1ivEK_tOynpfsM1RhbJWIDQi7-np27y2gdcpkAEtug6lWvcaXmRWsnX_SCwoPRIvu2WXJaTOMKXifg2gXPhpxFaXcgvZw6PZd20rleJETbG_z_ReLcMHm8)

  
  

  
  

Payload: https://142.250.188.4 : forbidden

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh5xuX-Vy_DwOIb-V_ZI7FQsi0ZXXJEWyAGl8GYp5UMwl6Pxi767ok6XFzSRY49o6jlBXP1i1OSBXvS8u2YbOeuK761014cOnDCWzKrSl1S5SluJjd8jhIwm4AnTwoKJsdnw_DEi9k1ly8cWgPTlrF-qytZnlqZxdPM61PJPKqSC2JrEewtEtuKvSpr=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEh5xuX-Vy_DwOIb-V_ZI7FQsi0ZXXJEWyAGl8GYp5UMwl6Pxi767ok6XFzSRY49o6jlBXP1i1OSBXvS8u2YbOeuK761014cOnDCWzKrSl1S5SluJjd8jhIwm4AnTwoKJsdnw_DEi9k1ly8cWgPTlrF-qytZnlqZxdPM61PJPKqSC2JrEewtEtuKvSpr)

  
  

  
Bypass Payload: https:///google.com

https://example.com/something/do/login?returnToUrl=https:///google.com

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiS12j8ZYp9Vry2Rr4LKEi53F4VZQVgy0ea6Rio37Jgi3C3M5_nHotSVjlbLcITVOdtq9cugwzUlGckRRonflHddvTzZrjTULWA-LJub4FBP6-Yj2YxjhWoi_sCO9aB3ruATsgDu5B4uOaCUU_ZrC_CLJ-xEXSQ6sH4Biy_EokCV-zmXn0pxe9snmMy=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEiS12j8ZYp9Vry2Rr4LKEi53F4VZQVgy0ea6Rio37Jgi3C3M5_nHotSVjlbLcITVOdtq9cugwzUlGckRRonflHddvTzZrjTULWA-LJub4FBP6-Yj2YxjhWoi_sCO9aB3ruATsgDu5B4uOaCUU_ZrC_CLJ-xEXSQ6sH4Biy_EokCV-zmXn0pxe9snmMy)

  
  

  

💜

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/2656914608170622406?po=249736810970156954&hl=en-GB&saa=85391&origin=http://blog.h4rsh4d.com&skin=contempo)

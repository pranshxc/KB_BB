---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-26_full-address-bar-spoofing-on-opera-mini-android.md
original_filename: 2020-12-26_full-address-bar-spoofing-on-opera-mini-android.md
title: Full Address Bar Spoofing On Opera Mini Android
category: documents
detected_topics:
- command-injection
- race-condition
- mobile-security
tags:
- imported
- documents
- command-injection
- race-condition
- mobile-security
language: en
raw_sha256: 86dbb1e7ee5d2d00c95060d74f453ac058db65d9501356377adb5505764b10f2
text_sha256: 0ce398a76b4cc98d2b97e5815fa88df71e2a8864ad599ea8166496acc7754070
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Full Address Bar Spoofing On Opera Mini Android

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-26_full-address-bar-spoofing-on-opera-mini-android.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `86dbb1e7ee5d2d00c95060d74f453ac058db65d9501356377adb5505764b10f2`
- Text SHA256: `0ce398a76b4cc98d2b97e5815fa88df71e2a8864ad599ea8166496acc7754070`


## Content

---
title: "Full Address Bar Spoofing On Opera Mini Android"
url: "https://0x48piraj.medium.com/full-address-bar-spoofing-on-opera-mini-android-597fafa60627"
authors: ["Piyush Raj ~ Rex (@0x48piraj)"]
programs: ["Opera", "Google"]
bugs: ["Address Bar Spoofing"]
publication_date: "2020-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4049
scraped_via: "browseros"
---

# Full Address Bar Spoofing On Opera Mini Android

Full Address Bar Spoofing On Opera Mini Android
Patience is indeed* a virtue — bug bounty
Piyush Raj ~ Rex
Follow
3 min read
·
Dec 26, 2020

58

I found a race condition flaw which caused browser to preserve the address bar and to load the content from the spoofed page. Address bar spoofing allows for attacks where a malicious page can spoof the identify of another site.

Summary

During my testing, it was observed that the browser allowed JavaScript to update the address bar while the page was still loading. Upon requesting data from a non-existent port the address was preserved and hence a due to race condition over a resource requested from non-existent port combined with the delay induced by setInterval function managed to trigger address bar spoofing. It causes browser to preserve the address bar and to load the content from the spoofed page.

Impact

Opera Mini Android is installed on more than 500,000,000+ devices. The vulnerability gives attackers the ability to steal data using phishing or spread misinformation using legitimate domains.

Most Address Bar Spoofing vulnerabilities are not very practical but this vulnerability not only spoofs the address bar, but also makes the spoofed web-page completely responsive so the attack becomes practical.

Expected behavior

The browser should handle load events in expected order when JS redirects page before sub-resource load finishes.

[1] https://bugs.webkit.org/show_bug.cgi?id=194131
[2] https://bugs.webkit.org/show_bug.cgi?id=194208

Reproducibility

1) Visit the following link for the vulnerable browser — https://0x48piraj.com/--REDACTED--/operafabs.html

Get Piyush Raj ~ Rex’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2) You will notice that the URL is pointing to https://www.opera.com:8080/, however the content is hosted on 0x48piraj.com.

The Great Plot

So, it all started when I got a reply from Opera Software saying,

Opera Software asking POC
The Proof of Concept

Before redirecting the user to the website with the closed port, I decoded the base64 encoded version of my evil page, and then added it to the DOM. I managed to keep the spoofed address stable by using the setinterval() function.

<html>
<title>Not Opera</title>
<body>
<script>
 function spoof()
 {
 var data = 'PGh0bWw+PGJvZHk+PGgxIGFsaWduPSJjZW50ZXIiPlRoaXMgaXMgZGVmaW5pdGVseSBub3QgT3BlcmEuPC9oMT48L2JvZHk+PC9odG1sPg=='; // base64 encoded html content
 document.body.innerHTML=atob(data);
 window.location.assign("https://www.opera.com:8080");
 }
setInterval(spoof(),100000);
</script>
</script>
</body>
</html>

The payload is <html><body><h1 align=”center”>This is definitely not Opera.</h1></body></html>.

Validation or say, “Oh my god, I really found a valid bug, I can’t believe it!” moment
The bug was found valid, …ob..viously?!
The “arm-twisting”
Hello there? Anyone?
I ❤ Opera‘s Responsiveness
Translation: OMG! I am a genius!
Finally! The bug fix moment
Aftermaths & The End
The Hall of Fame
Press enter or click to view image in full size
Opera Security Hall of Fame (HoF)

Ho Ho Ho ..Merry Christmas!

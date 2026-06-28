---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-12_mass-xs-search-using-cache-attack.md
original_filename: 2019-11-12_mass-xs-search-using-cache-attack.md
title: Mass XS-Search using Cache Attack
category: documents
detected_topics:
- supply-chain
- xss
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- supply-chain
- xss
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 2c899eff9bdca0ef56ab9cfd2b20d28bed6d08c5eccff914596ccb8007998a75
text_sha256: 7a8dd06d1f73a7ea794e516e7d87a4ef0d1f6f85a6410acbf53d5455a8a34d85
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Mass XS-Search using Cache Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-12_mass-xs-search-using-cache-attack.md
- Source Type: markdown
- Detected Topics: supply-chain, xss, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2c899eff9bdca0ef56ab9cfd2b20d28bed6d08c5eccff914596ccb8007998a75`
- Text SHA256: `7a8dd06d1f73a7ea794e516e7d87a4ef0d1f6f85a6410acbf53d5455a8a34d85`


## Content

---
title: "Mass XS-Search using Cache Attack"
page_title: "Mass XS-Search using Cache Attack - HackMD"
url: "https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/index.html"
final_url: "https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/index.html"
authors: ["Terjanq (@terjanq)"]
programs: ["Google"]
bugs: ["XS-Search"]
publication_date: "2019-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4947
---

# Mass XS-Search using Cache Attack

I was researching all over Google for vulnerable endpoints that allow a malicious third party to obtain sensitive information about the user. I found them so many that I couldn’t decide whether to report all of the vulnerable pages as a one report or maybe split them as separate ones. The impact varies from retrieving the private book collections to obtaining all the user’s contacts char by char. After that struggle, I decided to include all of the endpoints (excluding one I already reported [b/124326006](https://issuetracker.google.com/issues/124326006 "b/124326006")) in this report. I am aware that these reports might not be treated separately but I believe that you will review the overall impact very closely and evaluate whether some of the vulnerabilities could be split into separate pieces or not.

**The vulnerable websites:**

  1. My Activity: [myactivity.google.com](http://myactivity.google.com)
  2. Google Mail: [mail.google.com](http://mail.google.com)
  3. Google Search: [google.com/search](http://google.com/search)
  4. Google Books: [books.google.com](http://books.google.com)
  5. Google Bookmarks: [bookmarks.google.com](http://bookmarks.google.com)
  6. Google Keep: [keep.google.com](http://keep.google.com)
  7. Google Contacts (old version): [google.com/contacts](http://google.com/contacts)
  8. YouTube: [www.youtube.com](http://www.youtube.com)

### Overall impact

A regular user of Google Products can have their sensitive information exposed when visiting a malicious website. The example information that could be leaked is as follows:

  * search history,
  * videos watched
  * the exact URLs visited
  * time frames of the activities
  * private book collection
  * books read / purchased / bookmarked / favorite / etc.
  * private emails
  * tokens / credit card numbers / phone numbers / etc.
  * frequency of mailing
  * people the user’s email with
  * contacts (including email addresses, names, phone numbers)
  * private notes
  * bookmarked websites
  * and more.

### PoC

I have prepared a joint Proof of Concept for all attacks: <https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html>. I tried to keep it as human-friendly as possible so I encourage you to read the source code to better understand the mechanics behind each attack.

### Attack

All of the presented attacks depend on detecting whether the resource has been loaded by abusing Error-Based Caching Attack. The attack has been invented by Eduardo and can be read here <https://github.com/xsleaks/xsleaks/wiki/Browser-Side-Channels#cache-and-error-events>. To not waste any more time I will just step into describing each attack and try to draw the brief impact.

### I. My Activity

**Vulnerable resource:**  
Depending on the search results different resources are being loaded and one of them is the image: <https://www.gstatic.com/history/static/myactivity_20190212-0122_1/images/no_results_gm2.png>.

**Impact**  
Along with the visited webpages, the example information that can be leaked is:

  * **search history** ,
  * **videos watched** ,
  * the **exact URLs visited** (e.g. [google.com/foo/foo1.html](http://google.com/foo/foo1.html)),
  * the exact **time frames of the activities** ,
  * and more.

The impact and the attack is the same as in another issue [b/122677661](https://issuetracker.google.com/issues/122677661 "b/122677661")

**Steps to reproduce**

  1. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  2. Find `My Activity` section
  3. Fill the website you want to check if visited. Use `"` character to match the exact expression and logical operator `OR` to make queries more efficient.
  4. Submit the form

**Video** : <https://youtu.be/Gz7OPlhLzNE>

![](//img.youtube.com/vi/Gz7OPlhLzNE/hqdefault.jpg)__

### II. Google mail

**Vulnerable resource**  
Again, depending on the results different resource is loaded and that is: <https://www.gstatic.com/images/icons/material/system/1x/chevron_left_black_20dp.png>

**Impact**  
With help of advanced search (<https://support.google.com/mail/answer/7190?hl=en>) available in Google Mail it is possible to expose information such as

  * **Private emails**
  * **Tokens** / **credit card numbers** / **phone numbers** / etc.
  * **Frequency of mailing**
  * **Email addresses**
  * pretty anything that can be searched for.

**Tweaks**  
It is possible to use logical operators to make the binary-search possible and therefore to effectively search for information, e.g. `1234 OR 1235 OR 1236 ...`. I managed to search for ~250 words at the same time.

**Steps to reproduce**

  1. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  2. Find the section `Google Mail`
  3. Insert the message you want to search for
  4. Submit the form

**Video** : <https://youtu.be/H3JTx0JhAng>

![](//img.youtube.com/vi/H3JTx0JhAng/hqdefault.jpg)__

### III. Google Search (personal)

I have already reported this one. More info can be found here [b/124326006](https://issuetracker.google.com/issues/124326006 "b/124326006")

**Video** : <https://youtu.be/nQJHGHw94fM>

![](//img.youtube.com/vi/nQJHGHw94fM/hqdefault.jpg)__

### IV. Google Books

**Vulnerable resource**  
No surprise. Depending on the search results additional resources are being loaded and two of them are:

  * <https://ssl.gstatic.com/ui/v1/menu/checkmark.png> → this will show up if there are results
  * <https://books.google.pl/googlebooks/images/my_library_logo.png> → this one will only show up if the resulted book was bookmarked into some bookshelf

**Impact**  
Exposing user’s

  * **private book collection**
  * **bookmarked books**
  * **books watched / read / purchased / etc**

The impact is very similar to the report [b/123482975](https://issuetracker.google.com/u/1/issues/123482975 "b/123482975")

**Steps to reproduce**

  1. Make sure to have some books you want to search for
  2. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  3. Find the `Google Books` section
  4. Fill the `book title` you want to search for and `shelf id`
  5. Submit the form

**Tweaks**  
The attack uses another vulnerability I had found and described in the mentioned report and that is [https://books.google.com/books?uid=vulnerability&q=hack](https://books.google.com/books?uid=vulnerability&q=hack). When accessing that URL the results for the logged user will be displayed without the need of knowing their `id`. Otherwise, the attacker would have to know that value.

**Video** : <https://youtu.be/thRWVw24srM>

![](//img.youtube.com/vi/thRWVw24srM/hqdefault.jpg)__

### V. Google Bookmarks

**Vulnerable resource**  
Here, the different resource is <https://ssl.gstatic.com/ui/v1/star/star-lit4.png> which shows up when there are search results

**Impact**  
This vulnerability allows the attacker to obtain information about **bookmarked websites** by the user.

**Steps to reproduce**

  1. Access the [Poc](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  2. Find the section `Google Bookmarks`
  3. Insert the website you want to search for
  4. Submit the form

**Video** : <https://youtu.be/bMzFRZfxMF8>

![](//img.youtube.com/vi/bMzFRZfxMF8/hqdefault.jpg)__

### VI. Google Keep

**Vulnerable resource**  
The resource here is quite different this time. I noticed that additional font is being loaded when there are search results and that is <https://fonts.gstatic.com/s/googlesans/v11/4UaGrENHsxJlGDuGo1OIlL3Owp4.woff2>

**Impact**  
Exposing user’s private notes at <https://keep.google.com>

**Steps to reproduce**

  1. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  2. Find the section `Google Keep`
  3. Insert the content of the note you want to search for
  4. Submit the form
  5. Prepare not containing `trjnq` and click on the button `find secret`
  6. Wait for the results

**Tweaks**  
The attack allows obtaining information **character by character** as presented in the video included below. It allows the attacker to dump any information that can be accessed on the website and the impact is almost as it was XSS Injection.

**Video:** <https://youtu.be/naPmFYsHRcI>

![](//img.youtube.com/vi/naPmFYsHRcI/hqdefault.jpg)__

### VII. Google Contacts

**Vulnerable resource**  
Similar to the previous attacks, a lot of vulnerable resources can be found. Two of them are:

  * <https://ssl.gstatic.com/ui/v1/star/star-lit4.png> → shows up if there is a result tagged with star
  * <https://ssl.gstatic.com/ui/v1/star/star4.png> → shows up if there is a result but not tagged with start

**Impact**  
Exposing **user’s contacts** including:

  * **phone numbers**
  * **names**
  * **e-mail addresses**
  * any other info that can be found in there.

**Steps to reproduce**

  1. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC")
  2. Insert the details you want to search for (phone number/name/email)
  3. Submit the form
  4. Create a new contact with a name starting with`trjnq_` and tag it with the start
  5. Click on the button `Find starred contact trjnq_...`
  6. Wait for the attack to finish

**Tweaks**  
Firstly, the attack only works on the old version of contacts. When a new user accesses the <https://google.com/contacts> they will be redirected to new version <https://contacts.google.com/>. I managed to bypass this obstacle by forcing the user to use the old version by appending the hidden parameter `cplus=0` (<https://www.google.com/contacts/u/0/?cplus=0>).

Another tweak is that the attack allows obtaining information **character by character** as presented in the video included below. It allows the attacker to dump any information that can be accessed on the website and the impact is almost as it was XSS Injection.

**Video:** <https://youtu.be/F8Kuj7B4tMo>

![](//img.youtube.com/vi/F8Kuj7B4tMo/hqdefault.jpg)__

### VIII. YouTube (watching history)

**Vulnerable resource**  
This one is tricky. The resources that depend on the search results on <https://www.youtube.com/feed/history> are video thumbnails. Each of them looks a little complicated, e.g. [https://i.ytimg.com/vi/CU9Iafc-Igs/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLACWMy85SQ_D3b1STEV2-l7XeY8XQ](https://i.ytimg.com/vi/CU9Iafc-Igs/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLACWMy85SQ_D3b1STEV2-l7XeY8XQ) because there are two parameters appended which seem to have unpredictable values. However, I found that when searching for a specific video using main YouTube search results with the same URLs. Hence, it’s possible to leak the information about the watched videos.

**Impact**  
The user can have their **watched videos exposed** to the third-party applications.

**Steps to reproduce**

  1. Access the [PoC](https://terjanq.github.io/Bug-Bounty/Google/cache-attack-06jd2d2mz2r0/poc.html "PoC").
  2. Find the section `YouTube (watching history)`.
  3. Choose the video you want to check if watched.
  4. If not watched click on the URL from status and after some time try again.

_Note that checking same video two times in a row can result in false-negative because caching system works weirdly. You can try to reproduce this and inspect it further._

**Video:** <https://youtu.be/S-QEkOvljCQ>

![](//img.youtube.com/vi/S-QEkOvljCQ/hqdefault.jpg)__

__

  * Mass XS-Search using Cache Attack
  * Overall impact
  * PoC
  * Attack
  * I. My Activity
  * II. Google mail
  * III. Google Search (personal)
  * IV. Google Books
  * V. Google Bookmarks
  * VI. Google Keep
  * VII. Google Contacts
  * VIII. YouTube (watching history)

Expand allBack to topGo to bottom

  * Mass XS-Search using Cache Attack
  * Overall impact
  * PoC
  * Attack
  * I. My Activity
  * II. Google mail
  * III. Google Search (personal)
  * IV. Google Books
  * V. Google Bookmarks
  * VI. Google Keep
  * VII. Google Contacts
  * VIII. YouTube (watching history)

Expand allBack to topGo to bottom

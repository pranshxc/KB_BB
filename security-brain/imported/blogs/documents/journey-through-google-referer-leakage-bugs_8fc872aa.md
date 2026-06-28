---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-28_journey-through-google-referer-leakage-bugs.md
original_filename: 2018-10-28_journey-through-google-referer-leakage-bugs.md
title: Journey through Google referer leakage bugs.
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 8fc872aa9c45b44791d6c91ad79db53296c7f4f47e1b08b82330de759d71cceb
text_sha256: 6e836fc23461b47e9f9878caf42d0b58fbc68fec90e42ea3831b40c9163e2aa8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Journey through Google referer leakage bugs.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-28_journey-through-google-referer-leakage-bugs.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8fc872aa9c45b44791d6c91ad79db53296c7f4f47e1b08b82330de759d71cceb`
- Text SHA256: `6e836fc23461b47e9f9878caf42d0b58fbc68fec90e42ea3831b40c9163e2aa8`


## Content

---
title: "Journey through Google referer leakage bugs."
page_title: "Journey through Google referer leakage bugs. – The Security Experts"
url: "https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/"
final_url: "https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/"
authors: ["KL Sreeram (@kl_sree)"]
programs: ["Google"]
bugs: ["Information disclosure", "Referer leakage"]
bounty: "4,633.7"
publication_date: "2018-10-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5622
---

# [Journey through Google referer leakage bugs.](https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/)

![](https://thesecurityexperts.files.wordpress.com/2018/10/google-bug-bounty-program.png?w=728&h=380&crop=1)

![google-bug-bounty-program](https://thesecurityexperts.wordpress.com/wp-content/uploads/2018/10/google-bug-bounty-program.png?w=736)

Hi there,  
This write-up is a walk-through to the misconfiguration which leaks sensitive URL through referer header.This affected various Google products and has been fixed now.

Generally, Google have a feature to share documents through “**shareable links** “. Which means you can generate an unique link for your project or document and share it. The person with that link will have access (view or modify) to your documents .

![Screenshot from 2018-12-31 19-49-48](https://thesecurityexperts.wordpress.com/wp-content/uploads/2018/10/Screenshot-from-2018-12-31-19-49-48.png?w=736)

**Leaking Shareable Link – Google Colab (Bug 1)**

Scrolling through the infosec- Twitter, I got stopped by an interesting write-up ([XSS in Google Colab](https://blog.bentkowski.info/2018/06/xss-in-google-colaboratory-csp-bypass.html)). After reading this, I decided to test [Google Colab](https://colab.research.google.com) . After an hour of poking around to learn the site’s behavior, I discovered the feature to import project from Github. As these kinds of feature are prone to SSRF, I decide to test for it. But no luck 😦

To look at the API queries and request, I switched to “HTTP-History” tab in Burp Suite.As unexpected things happen, I found my Google Colab link with unique ID got reflected in referer header of Github API’s call to import project.

![Screenshot from 2018-12-31 19-53-24](https://thesecurityexperts.wordpress.com/wp-content/uploads/2018/10/Screenshot-from-2018-12-31-19-53-24.png?w=736)

This means Github would be able to see all the unique ID of all Google Colab users who used their import feature. This is perfectly normal in most applications,as just by knowing the unique ID without any authentication you won’t be able to make any harm. But this was an exception. Google Colab have the first mentioned feature to share projects via sharable link. So with this link leaked to Github, they can access the projects or documents of people who enabled share via link feature.

**Impact**

The person having access to Github log can see all shareable link of Google Colab.

**Reward**

$3133.7

(I guess the reward was high because the normal flow of the website was itself vulnerable without any malicious interaction)

**BUG 2**  
I guessed there must be similar bugs in some other Google products. As Google had same sharing feature in several other sites. So I decided to try this issue in some other endpoints. How can anyone miss Youtube when thinking about shareable URL (Unlisted videos). So I decided to give a try on Youtube. I just tried to comment a link on a youtube video and then click on it. But there is something called Youtube redirector 😦 It will initially redirect the our URL to another URL which looks like: <https://www.youtube.com/redirect?q=http%3A%2F%2Fevil.com>. Due to this the referer header will always have the value as : “[https://www.youtube.com/redirect&#8221](https://www.youtube.com/redirect&#8221);. So I decided to get back and watch some CTF videos. In my Youtube home page I noticed something called Youtube Gaming. When I clicked on it, I got redirected to another subdomain called <https://gaming.youtube.com>. As it is another subdomain I decided to give a try for the same bug here  
1, So I opened a random video.  
2, I was lazy to open Burp. So I pasted the link: <https://whatismyreferer.com> (This site displays the value of your referer header).

3, Then clicked on it. Surprisingly it also leaked the referer ID without any redirection in between.

With this I can leak unlisted Gaming video’s URL. Yipee!!  
For this I was awarded $500 from Google VRP.

**Bug 3**  
After finding this issue again I was looking for similar endpoints like a wild beast,testing all Google subdomains.Finally I found something called Google Fusion Tables (<https://fusiontables.google.com>). There too you can share the document with shareable link.  
It had an option to insert a link in the description. I inserted <https://whatismyreferer.com> there and clicked it. Guess what? it worked again. 😉 I was welcomed with the shareable link tothe document.Bingo! Again I was awarded $500 for this bug.

**Bug 4**  
Remember leaking unlisted Youtube video link through referer header (bug 2)? One week later it was fixed and was verified from both end. After a month later I was going through Google News and found a news that there is a major update in Youtube Gaming. So I visted <https://gaming.youtube.com> . Then I found a lot of changes in it, Including logo ![:/](https://s1.wp.com/wp-content/mu-plugins/wpcom-smileys/uneasy.svg) So I decided to test it again. As there are more chance to revert back security update in new development update. So I tested it again and I my instinct wasn’t wrong. The fix was reverted and the bug was present in the same endpoint again. Reported the same issue and was awarded $500 again.

Thanks for Google Security Team for managing such an amazing VRP and huge rewards.

Wait no info-sec writeup is complete without a gif. Here is one

![af00faaf5ae314fc805c7154ec4677b6.gif](https://thesecurityexperts.wordpress.com/wp-content/uploads/2018/10/af00faaf5ae314fc805c7154ec4677b6.gif?w=736)

### Share this:

  * [ Share on X (Opens in new window) X ](https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://thesecurityexperts.wordpress.com/2018/10/28/journey-through-google-referer-leakage-bugs/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://0.gravatar.com/avatar/32dcb6585fa857f70a0fb3dad5be471439889652438e9036ea43ff96a3a998d4?s=90&d=identicon&r=G)

##  Published by Sree Ram KL

[ View all posts by Sree Ram KL ](https://thesecurityexperts.wordpress.com/author/sreeramkl/)

__October 28, 2018

__[Uncategorized](https://thesecurityexperts.wordpress.com/category/uncategorized/)

## Post navigation

[Red Team Village CTF- Decfon dc0471x002 (write up)](https://thesecurityexperts.wordpress.com/2018/10/01/red-team-village-ctf-decfon-dc0471x002-write-up/)

[XSS on Google Custom Search Engine](https://thesecurityexperts.wordpress.com/2019/07/11/xss-on-google-custom-search-engine/)

### Leave a comment [Cancel reply](/2018/10/28/journey-through-google-referer-leakage-bugs/#respond)

Δ

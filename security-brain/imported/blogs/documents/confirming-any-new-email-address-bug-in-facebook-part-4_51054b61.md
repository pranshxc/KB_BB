---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-17_confirming-any-new-email-address-bug-in-facebook-part-4.md
original_filename: 2021-08-17_confirming-any-new-email-address-bug-in-facebook-part-4.md
title: Confirming any new Email Address bug in Facebook (Part-4)
category: documents
detected_topics:
- rate-limit
- command-injection
- automation-abuse
tags:
- imported
- documents
- rate-limit
- command-injection
- automation-abuse
language: en
raw_sha256: 51054b6127566fa9bfb4449f120f3f9ab5a2f415b4de9815990fedb151d923d7
text_sha256: c85998747ff2e915965185189557662eb46f52b3a741f5db03d65325362eea14
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Confirming any new Email Address bug in Facebook (Part-4)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-17_confirming-any-new-email-address-bug-in-facebook-part-4.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `51054b6127566fa9bfb4449f120f3f9ab5a2f415b4de9815990fedb151d923d7`
- Text SHA256: `c85998747ff2e915965185189557662eb46f52b3a741f5db03d65325362eea14`


## Content

---
title: "Confirming any new Email Address bug in Facebook (Part-4)"
url: "https://lokeshdlk77.medium.com/confirming-any-new-email-address-bug-in-facebook-part-4-70cfe1b4dca5"
authors: ["Lokesh Kumar (@lokeshdlk77)"]
programs: ["Meta / Facebook"]
bugs: ["Rate limiting bypass"]
bounty: "3,449"
publication_date: "2021-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3411
scraped_via: "browseros"
---

# Confirming any new Email Address bug in Facebook (Part-4)

Confirming any new Email Address bug in Facebook (Part-4)
Lokesh Kumar
Follow
3 min read
·
Aug 17, 2021

259

1

This post is about an bug that I found on Facebook which used to Confirming any email address in new Facebook account by using IP and Account Rotation brute force attack. this post is bypass of my previous write-up → Disable Any Unconfirmed Account in Facebook

Vulnerable Endpoint:

https://m.facebook.com/confirmemail.php?e=victim@mail.com@&c=15579&report=1&message=1

After the Permanent fix of Disable Any Unconfirmed Account bug. I tried to bypass it so first I need to find what changes that Facebook Team made in previous fix. when the wrong 5digit code was entered the server responded with Status Code: 200 (Invalid Confirmation code)

Press enter or click to view image in full size

But if the 5digit code was matched the server responded with Status Code: 500 (Internal Server Error). So attacker can determine the exact confirmation code with status code.

Press enter or click to view image in full size

But the real challenge is the Rate Limit was implemented. After 20 wrong attempts all request will get blocked. so the only way is to bypass the rate limit. but the IP rotation technique can not bypass this. because Facebook already fixed this method in my previous finding. but I noticed that this endpoint works with and without login sessions. so I tried the same URL in another account but I got the same error message.

Press enter or click to view image in full size

Later I tried the URL in my mobile on chrome browser I got 500 (Internal Server Error). then I found that the rate limit can be bypassed with different account with different IP address.

IP Address can be easily rotated for each request as following the steps in my blog: How to Rotate IP ADDRESS For Each Request in Burp Suite

But the account rotation is not as easier. the 5digit code length is 00000 ~ 99999 so the attacker need 100000 Facebook accounts to make this attack. In Facebook Apps 2000 Test-user can be created in single app. so 2000 x 50 = 100000 Accounts can be created. I made a simple python script to Automate the whole account creations and extracted the cookies.

Press enter or click to view image in full size

Reproduction Steps:

Create any New Facebook Account with Victim’s Email Address.
Open Burp Suite and paste the below request in Intruder.
GET /confirmemail.php?e=redacted@email.com&c=12345&report=1&message=1 HTTP/1.1
Host: m.facebook.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: c_user=0; xs=0;

3. Choose Attack type as Pitchfork.

Get Lokesh Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Set payload 1 as 5 digit code range ex: 00000 to 99999 (payload marker in 12345)

5. set payload 2 as Test account cookies. and uncheck payload Encoding option (c_user=0; xs=0)

6. enable IP Rotation service in Burp Upstream Proxy server.

7. start the attack if the correct code got matched the server response will be 500 Internal Server Error

Press enter or click to view image in full size

Video POC:

https://www.youtube.com/watch?v=cqmdyja9YQQ

Timeline:

07-jan-2021: Report Sent

21-Jan-201: Further investigation by Facebook

01-Feb-2021: Fixed confirmed by Facebook and me

01-Feb-2021: $3449 bounty awarded by Facebook (With Bonus)

Press enter or click to view image in full size

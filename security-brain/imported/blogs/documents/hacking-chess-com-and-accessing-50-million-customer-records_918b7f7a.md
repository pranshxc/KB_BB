---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-11_hacking-chesscom-and-accessing-50-million-customer-records.md
original_filename: 2021-02-11_hacking-chesscom-and-accessing-50-million-customer-records.md
title: Hacking Chess.com and Accessing 50 Million Customer Records
category: documents
detected_topics:
- xss
- mobile-security
- command-injection
- mfa
- otp
- information-disclosure
tags:
- imported
- documents
- xss
- mobile-security
- command-injection
- mfa
- otp
- information-disclosure
language: en
raw_sha256: 918b7f7abaef9959db107ab97a268c457d8cd26727977455efec4ad30543f59a
text_sha256: 7eab08eca111d3d65fa9c2c43df3770072fcfb62e8601ae48ee19aab67c49c72
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Chess.com and Accessing 50 Million Customer Records

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-11_hacking-chesscom-and-accessing-50-million-customer-records.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, command-injection, mfa, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `918b7f7abaef9959db107ab97a268c457d8cd26727977455efec4ad30543f59a`
- Text SHA256: `7eab08eca111d3d65fa9c2c43df3770072fcfb62e8601ae48ee19aab67c49c72`


## Content

---
title: "Hacking Chess.com and Accessing 50 Million Customer Records"
url: "https://samcurry.net/hacking-chesscom/"
final_url: "https://samcurry.net/hacking-chesscom"
authors: ["Sam Curry (@samwcyo)"]
programs: ["Chess.com"]
bugs: ["Reflected XSS", "Information disclosure", "Account takeover"]
publication_date: "2021-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3918
---

[Back to blog](/)

# Hacking Chess.com and Accessing 50 Million Customer Records

December 16, 2020

![Hacking Chess.com and Accessing 50 Million Customer Records](/_next/image?url=%2Fimages%2Fhacking-chesscom%2F9Ho9K6v.jpg&w=3840&q=75)

To preface: the bug we found here is really simple. The interesting thing here is the impact of the vulnerability itself.

The reason I really wanted to write about this is because of how much fun we had finding it. I think me [@sshell_](https://twitter.com/sshell_) were laughing about this bug in a voice call for probably an hour before we realized we needed to actually report it.

Something that many many not know is that Chess.com has a bug bounty program on their own website (as many other companies do) that accepts submissions via email. Their program page is located [here](https://www.chess.com/news/view/chess-com-bug-bounty-policy) and I'd genuinely suggest checking them out.

## Background

When I first started hacking them in November of 2019 I spent a huge amount of time searching for generic web vulnerabilities.

I was able to find a different reflected XSS, but nothing interesting.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fccom-1024x380.png&w=3840&q=75)

The XSS could've been escalated to an account backdoor via extracting the "Connect to Google" URL, authenticating into it with an account you owned, then using an XSS hook to send an HTTP request with the callback to bind the attacker's Gmail account to the victim's Chess.com account.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fcon_ax.png&w=3840&q=75)

I guess this was a neat bypass for weaponizing XSS, but it really didn't satisfy my curiosity with hacking the app. I really wanted to find a higher severity issue.

I'd come back and hack on them every once in a while but never really seemed to make any progress. Every time I checked back, it felt like I was looking at the same pieces of functionality and never finding anything new.

## Account Takeover Vulnerability

I was hacking another company via my iPhone and Burp Suite when I realized that I'd never even opened the chess.com app while intercepting HTTP traffic. When I did, there was a new subdomain I'd never seen before.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fapi_chess_com-1024x231.png&w=3840&q=75)

There were signed API requests being sent to "api.chess.com".

The fact the app used this domain was super interesting to me as I'd tried to manually form HTTP requests to the website before but never had any luck. Each one sent by the app itself had properly formed headers and actually worked.

The first few requests looked something like this:
  
  
  GET /v1/users/validate-username/test?signed=iOS3.9.7-047a13c395ee9c059f98f1af74bb11c802047d47 HTTP/1.1
  Host: api.chess.com
  

After trying to tamper with the request, it was clear that the "signed" parameter was used as a hash for all of the request parameters. You couldn't tamper with any part of the HTTP request without it giving an unauthorized error as the application was using some sort of secret to sign the whole request. This meant that if you changed anything whatsoever then the application wouldn't let you send it.

Since we were the ones signing the request through our mobile phone, it would theoretically be possible to extract the secret and write a script to arbitrarily sign requests.

But, before trying to actually tamper with the app, I just simply clicked around to see the different functionality.

There was a really interesting HTTP request that came up when I searched for the username "hikaru" to send a message to. The following is the HTTP request and response when the app tried to fetch the information about the user:
  
  
  GET /v1/users?loginToken=98a16127fb8cb4dc97a3a02103706890&username=hikaru&signed=iOS3.9.7-7b9f1383b669614302e9503ba7db81875e440d7e HTTP/1.1
  Host: api.chess.com
  
  
  
  {
  "status": "success",
  "data": {
  "email": "REDACTED@REDACTED.COM",
  "premium_status": 3,
  "id": 15448422,
  "uuid": "REDACTED",
  "country_id": 2,
  "avatar_url": "https://images.chesscomfiles.com/uploads/v1/user/15448422.90503d66.200x200o.f323efa57fd0.jpeg",
  "last_login_date": REDACTED,
  "session_id": "REDACTED",
  "location": "Sunrise, Florida",
  "username": "Hikaru",
  "points": 52,
  "chess_title": "GM",
  "first_name": "Hikaru Nakamura",
  "last_name": null,
  "country_name": "United States",
  "member_since": REDACTED,
  "about": "",
  "is_blocked": false,
  "is_tracked": false,
  "are_friends": false,
  "friend_request_exists": true,
  "is_able_to_change_username": null,
  "flair_code": "diamond_traditional",
  "show_ads": true,
  "is_fair_play_agreed": true
  }
  }
  

When I first saw this HTTP response, I was very happy because it was returning the email address of the user! This meant it was possible to arbitrarily retrieve the email addresses of anyone, a probably medium severity bug.

Even though we didn't have a way to sign the HTTP requests, we could just simply search for a specific user via the mobile app, intercept the traffic, and lastly be able to see the HTTP response containing the victim email address.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fvictim.png&w=3840&q=75)

Before I began writing the report to submit to their security team, I searched through the profile field and tried to see if there was anything else being leaked. Overall it looked kind of boring, but after searching for two separate users I realized something:
  
  
  "session_id":"56c5257a0800d.....86d28934868a88",
  
  
  
  "session_id":"1f3d112b9a3f.....dbbf19438fcd8d",
  

The "session_id" values were different for each user. Since it was returning a user object, this meant that they likely belonged to the user versus something that belonged to my session.

The question was what they were used for and if it was anything sensitive.

I logged into the website on my desktop and checked my cookies. They were using "PHPSESSID" as a session token, and when I searched my own username, it returned my own "PHPSESSID" in the "session_id" field!

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2FPHPSESSId.png&w=3840&q=75)
  
  
  HTTP/1.1 200 OK
  Date: Sat, 9 Dec 2020 05:52:47 GMT
  Content-Type: application/json
  ...
  "session_id":"3947398c39ef15a.....56523b5a4533"
  ...
  

Since the PHPSESSID was the only means of authorizing users, this meant we could extract this value from any user and hijack their session.

Jackpot, full arbitrary account takeover of any chess.com user!

In order to demonstrate maximum impact, I went ahead and retrieved the PHPSESSID cookie of [Daniel Rensch](https://twitter.com/danielrensch), a chess.com administrator.

After authorizing to his session, I was a bit disappointed. There was no administrative interface.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fauthd-1024x325.png&w=3840&q=75)

I clicked around the app until I remembered something from earlier testing: there was an "admin.chess.com" subdomain.

I scoped the leaked administrative PHPSESSID cookie for ".chess.com" then opened up a new tab to see if we could access it. When I loaded the page, it didn't kick me out like it did in the past. We were into the administrator dashboard!

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Fadmin-2-1024x334.png&w=3840&q=75)

At this point, we pulled up the profile of ourselves on the app:

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Flol-2-1024x559.png&w=3840&q=75)

If we were malicious actors, this could've been abused to fully take over anyone's account. Worst of all, we could've updated our profiles to pretend we were anything above 400 ELO.

![](/_next/image?url=%2Fimages%2Fhacking-chesscom%2Ftitlz.png&w=3840&q=75)

At this point, we wrote and submitted the bug sometime around 4:00 AM. They responded to the email within an hour and had patched it in two.

Thanks for reading and Happy Holidays!

## Timeline

  * 12/12/2020, 12:34 AM - Reported
  * 12/12/2020, 03:17 AM - Validated
  * 12/12/2020, 07:42 AM - Remediated
  * 12/16/2020, 02:40 PM - Rewarded

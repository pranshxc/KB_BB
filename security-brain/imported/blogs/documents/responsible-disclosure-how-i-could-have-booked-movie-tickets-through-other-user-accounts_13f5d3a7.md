---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-18_responsible-disclosure-how-i-could-have-booked-movie-tickets-through-other-user-.md
original_filename: 2018-06-18_responsible-disclosure-how-i-could-have-booked-movie-tickets-through-other-user-.md
title: '[Responsible disclosure] How I could have booked movie tickets through other
  user accounts'
category: documents
detected_topics:
- rate-limit
- password-reset
- command-injection
- otp
- api-security
tags:
- imported
- documents
- rate-limit
- password-reset
- command-injection
- otp
- api-security
language: en
raw_sha256: 13f5d3a792b89fafb857efc23812f212395daf756c8f1163c64a29bb5fda8a23
text_sha256: 441d45d50f53f09182077e50007cebceac90bd88ebdfb68283c8d8f45148c457
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# [Responsible disclosure] How I could have booked movie tickets through other user accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-18_responsible-disclosure-how-i-could-have-booked-movie-tickets-through-other-user-.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `13f5d3a792b89fafb857efc23812f212395daf756c8f1163c64a29bb5fda8a23`
- Text SHA256: `441d45d50f53f09182077e50007cebceac90bd88ebdfb68283c8d8f45148c457`


## Content

---
title: "[Responsible disclosure] How I could have booked movie tickets through other user accounts"
url: "https://medium.com/bugbountywriteup/responsible-disclosure-how-i-could-have-booked-movie-tickets-through-other-user-accounts-2db26a037b4c"
authors: ["Bharathvaj Ganesan"]
programs: ["AGS Cinemas"]
bugs: ["Password reset", "Account takeover", "Bruteforce", "OTP bypass"]
publication_date: "2018-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5836
scraped_via: "browseros"
---

# [Responsible disclosure] How I could have booked movie tickets through other user accounts

Bharathvaj Ganesan
 highlighted

[Responsible disclosure] How I could have booked movie tickets through other user accounts
Bharathvaj Ganesan
Follow
2 min read
·
Jun 18, 2018

367

Note: The vulnerability has been reported and is now fixed.

AGS Cinemas is one of the famous theatres in Chennai, Tamil Nadu. They launched their own movie ticket booking website and apps last year.

Press enter or click to view image in full size
“Two CCTV cameras on a gray wall” by Scott Webb on Unsplash

This post is about a simple vulnerability I discovered on AGS Cinemas which I could have used to hack into other users’ accounts easily and without any user interaction.

This gave me full access to other users account by setting a new password. I was able to view ticket history, their credit wallet, and other private information.

Suresh Kumar, the CEO of MacAppStudio (Technology partner for AGS Cinemas) acknowledged the issue promptly, fixed it. There are quite a few humble persons like him who would accept these kind of security bugs, because many would have confronted me on testing their site without their permission.

How the hack worked

Whenever a user Forgets their password on AGS Cinemas, they have an option to reset the password by entering their phone number on the forgot password popup.

AGS Cinemas will then send a 4 digit code to this phone number which the user has to enter in order to set a new password.

I tried to brute force the 4 digit code (eg. 3286) on www.agscinemas.com and wasn’t blocked after even 5-6 invalid attempts. Interestingly, rate limiting was missing from forgot password endpoint.

Get Bharathvaj Ganesan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to take over my own account and was successful in setting a new password for my account. I could then use this same password to log into my own hacked account.

A proof of concept video of the hack

As you can see in the video, I was able to set a new password for the user by brute forcing the code which was sent to their phone number.

POST /php/otpverify.php HTTP/1.1

Host: www.agscinemas.com

mobile=XXXXXXXXXX&randomnums=XXXX

Brute forcing the “randomnums” successfully allowed me to set new password for any AGS Cinemas account.

Disclosure Timeline

Feb 21st, 2018 : Bug was discovered.

Feb 22nd, 2018 : Report sent to MacAppStudio team.

Feb 23rd, 2018 : Acknowledged by CEO.

Feb 24th, 2018 : Issue resolved from their side.

Thanks for reading through 🙌🏼. If you found this article useful, please applaud using the 👏 button and share it through our circles.

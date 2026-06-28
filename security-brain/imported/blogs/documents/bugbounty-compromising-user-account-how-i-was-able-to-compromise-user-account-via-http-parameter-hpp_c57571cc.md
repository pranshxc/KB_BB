---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-07_bugbounty-compromising-user-account-how-i-was-able-to-compromise-user-account-vi.md
original_filename: 2018-07-07_bugbounty-compromising-user-account-how-i-was-able-to-compromise-user-account-vi.md
title: '#BugBounty - Compromising User Account- ''How I was able to compromise user
  account via HTTP Parameter Pollution(HPP)'''
category: documents
detected_topics:
- command-injection
- password-reset
tags:
- imported
- documents
- command-injection
- password-reset
language: en
raw_sha256: c57571cc89f1e95b959914e4368ac826476649f2eaea84f7a1f13b4e1da2f9dc
text_sha256: 433d65064bfe0e8f55ddd130126e16e0ecdf576b179239d0b844ffc6a1101544
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty - Compromising User Account- 'How I was able to compromise user account via HTTP Parameter Pollution(HPP)'

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-07_bugbounty-compromising-user-account-how-i-was-able-to-compromise-user-account-vi.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c57571cc89f1e95b959914e4368ac826476649f2eaea84f7a1f13b4e1da2f9dc`
- Text SHA256: `433d65064bfe0e8f55ddd130126e16e0ecdf576b179239d0b844ffc6a1101544`


## Content

---
title: "#BugBounty - Compromising User Account- 'How I was able to compromise user account via HTTP Parameter Pollution(HPP)'"
page_title: "#BugBounty — Compromising User Account- ”How I was able to compromise user account via HTTP Parameter Pollution(HPP)” | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-compromising-user-account-how-i-was-able-to-compromise-user-account-via-http-4288068b901f"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["HTTP parameter pollution", "Password reset", "Account takeover"]
publication_date: "2018-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5814
scraped_via: "browseros"
---

# #BugBounty - Compromising User Account- "How I was able to compromise user account via HTTP Parameter Pollution(HPP)"

#BugBounty — Compromising User Account- ”How I was able to compromise user account via HTTP Parameter Pollution(HPP)”
Avinash Jain (@logicbomb)
Follow
3 min read
·
Jul 7, 2018

1.1K

4

Hi Guys,

As the title suggests , this particular blog is about “How I was able to compromise user account exploiting HTTP Parameter Pollution (HPP) vulnerability. HPP — What, Why, How? and below is the short description—

HTTP Parameter Pollution, as implied by the name, pollutes the HTTP parameters of a web application in order to perform or achieve a specific malicious task/attack different from the intended behaviour of the web application. Supplying multiple HTTP parameters with the same name may cause an application to interpret values in unanticipated ways.

Recently, I have been reading a lot about this, some of the hackerone reports and how different application handles it, made it more clear for me. Targeting it, I found the same in one of the Indian Online Shopping Site and I then escalated it to “User Account Compromise”.Let’s see how I was able to do so—

Like every other shopping apps have, this website was also having the functionality to share the shortlisted shopping items on social media sites or we may call it social sharing button. Below is the redacted HTTP request for the same —

https://www.redacted.com/zephyr-mini-alpha board/p/&pid=ETYDBYSKDDZQGDJD&vi=XXXX

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here was a simple HPP vulnerability where adding the parameter ‘u’ (https://www.redacted.com/zephyr-mini-alpha board/p/?u=http://www.evil.com&pid=ETYDBYSKDDZQGDJD&vi=XXXX) and sharing it on facebook will change the content to https://www.facebook.com/sharer.php?u=https://www.redacted.com/zephyr-mini-alpha board/p/?u-http://www.evil.com&pid=ETYDBYSKDDZQGDJD&vi=XXXX and instead of sharing the shortlisted item, “evil.com” was getting shared on victim’s Facebook page. Now as I knew that HPP occurs due to the way the different web servers and development frameworks handle multiple parameters hence it’s basically a backend application technology issue. So if it is occurring on social sharing button , it can be present in other part of the application as well. In the search to exploit it more, I went to test login authentication page where there was a reset password functionality.

Press enter or click to view image in full size
Reset Password Page

Before that, I analysed the backend application framework being used using “Wappalyzer” which shows that “JSP and Apache” were in use. Now, providing victim’s mail id and submitting it, triggers the below HTTP request-

Press enter or click to view image in full size
Reset Password HTTP Request

According to the functionality, it generated the reset password link taking the value as “harrysonito@gmail.com” and send it to the same mail id.

Now as I knew that HPP is existing in the framework and “JSP and Apache” were being used as backend application and in order to know more about this framework ,how they handle parameter pollution, this helped me-https://www.acunetix.com/blog/whitepaper-http-parameter-pollution/

and I went to check whether supplying multiple “email” parameters causes the backend application framework to work differently. I added attacker’s email id and the tampered request looks like-

Press enter or click to view image in full size
Tampered HPP Reset Password Request

and as I was expecting , the backend application (JSP in this case)took the value of first “email” parameter to generate the password reset link and used the value supplied in the second “email” value to trigger the send mail to “petercheckk852234@gmail.com . Because of which “attacker” receive the link to reset password of “victims” account. :) and I then opened the link, set the password for victim account and able to login into the same to finally takeover the account and this is how I was able to compromise any user account via HTTP Parameter Pollution.

Press enter or click to view image in full size

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )

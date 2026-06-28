---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-11_clickjacking-on-google-myaccount-worth-7500.md
original_filename: 2018-11-11_clickjacking-on-google-myaccount-worth-7500.md
title: Clickjacking on Google MyAccount Worth 7,500$
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
language: en
raw_sha256: 2205b7b7123226c623e8bdaca0f7cf4a2bad585a157160a5bee682276215761f
text_sha256: fb1dc1d5ed7eaacde13bb2460dccc1a3ebbec753c70696cc8a933d006c40d2b6
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjacking on Google MyAccount Worth 7,500$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-11_clickjacking-on-google-myaccount-worth-7500.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `2205b7b7123226c623e8bdaca0f7cf4a2bad585a157160a5bee682276215761f`
- Text SHA256: `fb1dc1d5ed7eaacde13bb2460dccc1a3ebbec753c70696cc8a933d006c40d2b6`


## Content

---
title: "Clickjacking on Google MyAccount Worth 7,500$"
page_title: "Clickjacking on Google MyAccount Worth 7,500$ – Apapedulimu"
url: "https://apapedulimu.click/clickjacking-on-google-myaccount-worth-7500/"
final_url: "https://apapedulimu.click/clickjacking-on-google-myaccount-worth-7500/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["Google"]
bugs: ["Clickjacking"]
bounty: "7,500"
publication_date: "2018-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5597
---

![](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-09-26-at-4.40.13-AM-825x510.png)

# Clickjacking on Google MyAccount Worth 7,500$

Recently, I got surprised from google, I found bug Clickjacking On Google My account. And they reward me 7,500$ for single bug. Amazing, right?. This bug I’ve found on March 2018, but the clickjacking is just blocked by CSP, and on August, I’ve found way to bypass it.

Actually, I’ve been research on **business.google.com** subdomain and look around, just dummies touching the feature. See the respond and request. Try a stupid thing, edit the parameter, etc. And when I want to manage the user is redirect me to **myaccount.google.com** which is place where I found the bug.

I look at my Lovely**Community Edition of Burp Suite,** There’s no header **X-Frame-Option** on it. At that time, I use Firefox ESR, I craft simple html just to iframe the page. And success, report them, but not applicable. Because on Firefox Quantum, Say **Blocked By CSP,**

![Clickjacking Blocked By CSP](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-08-11-at-6.56.49-AM-1024x330.png)Clickjacking Blocked By CSP on Modern Browser

Sad to hear that, but I realize I just too noob. So, It’s okay. I leave my research on google until August 15th. I try to look around again on my previous research. With more focus and of course my black coffee. I try to understand the code work.

I realize if the **CSP rule** is reflected from my **request parameter.** I found it on business.google.com , so the parameter of the host is **business.google.com.**

URL : [https://myaccount.google.com/u/0/brandaccounts/group/101656179839819660704/managers?originProduct=AC&origin=https://business.google.com](https://myaccount.google.com/u/0/brandaccounts/group/101656179839819660704/managers?originProduct=AC&origin=https://business.google.com)

And the respond is :

![Response And Request Header](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-08-11-at-7.13.16-AM-1024x301.png)

I realize if host just accept from **business.google.com** on origin parameter. So, I think the only way to execute it just from **business.google.com** . But, I try to edit parameter the origin to **https://akugalau.business.google.com**. It’s accepted! But, It’s impossible to use that subdomain. Hmmmm,

![](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-08-11-at-7.13.43-AM-1024x308.png)

Okay, The csp still here, And I can’t do nothing, right? Do, I must give up? Come on, It’s a big company and I ? Just **little kid with the broken heart story 🙁 SAD!**

But, I have a lot free time to do stupid thing, right? So, I just **adding illegal character on the origin parameter.** I try to put URL Encode before the business.google.com. Become like this :

https://myaccount.google.com/u/0/brandaccounts/group/101656179839819660704/managers?originProduct=AC&origin=https://%0d.business.google.com

And the **CSP is disappear** , w000tttttt!!!!?!@?#!@?3!@?3?

![The CSP is disappear](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-08-11-at-7.14.22-AM-1024x373.png)

I try to iframe that And, I success to perform the clickjacking :’ . **My condition is between not believe this and happy.**

![](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-08-11-at-6.57.27-AM-1024x556.png)

If you ask me where the logic from adding the**url encode** on that. I dont understand :’ ,**I just lucky kid.**

I make report quickly and submit to google. After 1 month, I just expected it’s worth 3,133.7 or 5,000. But, the google give me bigger bounty, they give me **7,500$ . What !**

![](https://apapedulimu.click/wp-content/uploads/2018/11/Screen-Shot-2018-09-25-at-4.05.47-AM.png)

I dont know what i suppose to say. :’ , I dont believe it because I just **noob kid.**

**PoC Code :**

> <iframe src=”[https://myaccount.google.com/u/0/brandaccounts/group/{your-group-id}/managers?originProduct=AC&origin=https://%0d.business.google.com](https://myaccount.google.com/u/0/brandaccounts/group/%7Byour-group-id%7D/managers?originProduct=AC&origin=https://%0d.business.google.com)” width=”1000″ height=”1000″>

**Attack Scenario :**

1\. Admin invite new user on **group-id**  
2\. New user will accept the invitation  
3\. New user know the **{your-group-id}**  
4\. New user**create a malicious page including this clickjacking to trick admin** make the**new user account to the owner**  
5\. The group is takeover by the user.

**Video :**

**Timeline :**

  * **Aug 11 :** Report to Google
  * **Aug 15 :** Google Staff Ask Detail
  * **Aug 15 :** Adding Detail
  * **Aug 21 :** Google Can’t Prove Bug
  * **Aug 21 :** Give them Video to PoC
  * **Aug 28 :** Google Ask About Attack Scenario
  * **Aug 28 :** Give the Attack Scenario
  * **Sep 11 :** Nice Catch!
  * **Sep 25 :** Bounty 7,500$
  * **Sep 25 :** I Cry.

And also, Big thanks to all Indonesia Bug Hunter Community, Who has been teach me a lot about Bug Bounty and the ethical of bug hunter.

Get in touch with me on twitter : [LocalHost31337](https://twitter.com/LocalHost31337)

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [November 11, 2018](https://apapedulimu.click/clickjacking-on-google-myaccount-worth-7500/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Clickjacking](https://apapedulimu.click/tag/clickjacking/), [Google](https://apapedulimu.click/tag/google/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-03_how-the-use-of-hidden-form-fields-lead-to-email-verification-bypass.md
original_filename: 2021-08-03_how-the-use-of-hidden-form-fields-lead-to-email-verification-bypass.md
title: How the use of hidden form fields lead to Email verification bypass
category: documents
detected_topics:
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- command-injection
- password-reset
- otp
language: en
raw_sha256: 3954f80f162b43645b51614096d0df70c91841f2a1cd39f580d9fb1cfde78673
text_sha256: 7ecbcf680ce0100fae98ee5a8f88f932b6d1cf1b33794063626b3c01cee78e5d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How the use of hidden form fields lead to Email verification bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-03_how-the-use-of-hidden-form-fields-lead-to-email-verification-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `3954f80f162b43645b51614096d0df70c91841f2a1cd39f580d9fb1cfde78673`
- Text SHA256: `7ecbcf680ce0100fae98ee5a8f88f932b6d1cf1b33794063626b3c01cee78e5d`


## Content

---
title: "How the use of hidden form fields lead to Email verification bypass"
url: "https://yashswarup12.medium.com/how-the-use-of-hidden-form-fields-lead-to-email-verification-bypass-3c8d7c25bd31"
authors: ["Yash Swarup (@wazirsec)"]
bugs: ["Email verification bypass", "Client-side enforcement of server-side security"]
publication_date: "2021-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3444
scraped_via: "browseros"
---

# How the use of hidden form fields lead to Email verification bypass

How the use of hidden form fields lead to Email verification bypass
Yash Swarup
Follow
4 min read
·
Aug 3, 2021

307

Hello everyone, I hope you are doing well. Today I’m gonna explain one of my findings, by which I was able to bypass the email verification feature of a web application by using hidden form fields. As this was a private program, so I’ll assume it as example.com.

Overview

According to the Web application hacker’s handbook, Hidden HTML form fields are a common mechanism for transmitting data via the client in a superficially unmodifiable way. If a field is flagged as hidden, it is not displayed on-screen. However, the field’s name and value are stored within the form and are sent back to the application when the user submits the form.

An intercepting proxy is tremendously useful when attacking a web application so I’ll be using Burp Suite for this.

Burp Suite has an inbuilt feature to automatically modify certain HTML features on the fly. You can unhide hidden form fields, remove input field limits, and remove JavaScript form validation.

To use this go to the Proxy “Options” tab and locate the “Response Modification” section. Click the checkbox next to “Unhide hidden form fields”.

There is also a sub-option to prominently highlight unhidden fields on-screen, for easy identification.

Press enter or click to view image in full size
Exploitation

This program that I was testing had only one subdomain in its scope which was https://example.com. So now I turned on my Burp proxy and enabled the “Unhide hidden form fields” feature of Burp suite and started to play with the functionality of the web application in the browser, exploring all the features of that web application.

After exploring the web application, I understood some things:

1. I am able to access my account only after verifying my email by clicking on the verification link that comes on my email after signing up.

2. My primary email is the one that I used during sign-up on the website and the web application does not allow me to edit it. It’s permanent.

3. I can also add some secondary emails on my account which I can remove anytime and I have to verify them also.

4. After verifying the secondary emails, they also get full access to the account.

Now using Burp’s Unhide hidden form fields feature when I visited my profile page on the website, I found two hidden form fields on that page.

example_user_profile[email]
example_user_profile[_token]
Press enter or click to view image in full size

The parameter example_user_profile[email] was having the same value as my primary email so I thought maybe I can misuse this hidden email form field to change my primary email address which the web application does not permit me to do.

Get Yash Swarup’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I changed the value of the email to wazirsec1@example.com and clicked on update.

Press enter or click to view image in full size

Now notice the change in the email field, It’s saying that it is not verified and also I can remove it now.

So I tried to remove my primary email and I was successfully able to do it.

After removing that email address my profile looked like this.

Press enter or click to view image in full size

Now I reloaded my profile page and my primary email address was changed to wazirsec1@example.com which was the value that I gave previously in the email hidden form field.

So with the help of this vulnerability, I would have been able to change my email address to any email address without any verification.

Mitigation

The best advice is not to put important data, such as the price of the product, in plain view. Just because it is in a “hidden” field doesn’t mean you can’t find it. It’s only hidden when running the page. The field and its data are easily found in the page source. Rather than using a hidden field, such data can easily be stored in a backend database.

Don’t forget to share your ideas and criticism with me.

Hope you guys like this. Do give it a Clap if liked it. 👏

You can connect with me on Linkedin or Twitter if you wish to.

Cheers.

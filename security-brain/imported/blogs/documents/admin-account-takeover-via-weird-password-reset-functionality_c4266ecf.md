---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-02_admin-account-takeover-via-weird-password-reset-functionality.md
original_filename: 2022-07-02_admin-account-takeover-via-weird-password-reset-functionality.md
title: Admin account takeover via weird Password Reset Functionality
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- supply-chain
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- supply-chain
language: en
raw_sha256: c4266ecf794fed4444826c653ce1c664f0f5dbcc026f9dddbeaf462402e115e7
text_sha256: d0dec5aa9d0d35675566091d0aa02a5895bb4589647b67b22ec492236f39ef22
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Admin account takeover via weird Password Reset Functionality

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-02_admin-account-takeover-via-weird-password-reset-functionality.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `c4266ecf794fed4444826c653ce1c664f0f5dbcc026f9dddbeaf462402e115e7`
- Text SHA256: `d0dec5aa9d0d35675566091d0aa02a5895bb4589647b67b22ec492236f39ef22`


## Content

---
title: "Admin account takeover via weird Password Reset Functionality"
url: "https://0xmahmoudjo0.medium.com/admin-account-takeover-via-weird-password-reset-functionality-166ce90b1e58"
authors: ["Mahmoud Youssef (@0xmahmoudjo0)"]
bugs: ["Account takeover", "Authentication bypass", "Password reset"]
publication_date: "2022-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2492
scraped_via: "browseros"
---

# Admin account takeover via weird Password Reset Functionality

Top highlight

Admin account takeover via weird Password Reset Functionality
Mahmoud Youssef
Follow
5 min read
·
Jul 2, 2022

1.4K

10

Hello all, I hope you’re fine! Our story today is a funny ATO I recently found it, so I decided to share it with you.

Press enter or click to view image in full size
Background:

Let’s assume that our vulnerable subdomain is sub.redacted.com and it deals with an API subdomain called api.redacted.com , and the forget password function on our site works like this :

Go to /forgetPass and type the email
If the email exists, the site sends a reset email, if it doesn’t it gives you an error.
The backend sends a third-party link with a unique token to redirect you to https://sub.redacted.com/verify/<UNIQUE-HASH> to type a new password
Analysis:

I started looking into /forgetPass and asked for a password reset link, and I started looking around the request

Press enter or click to view image in full size

There’s nothing suspicious in the request, so let’s analyze the third-party reset link

Press enter or click to view image in full size

So, when you click on the reset link which you received in your inbox, it gives you an endpoint to reset your password which is https://sub.redacted.com/verify/<UNIQUE-HASH>

Behind the scene, when you were be redirected to https://sub.redacted.com/verify/<UNIQUE-HASH> there’s a request used to verify the hash with api.redacted.com and its response is the email in which you requested to reset its password

Press enter or click to view image in full size

I tried to play with the token, but I got nothing :(

Just let us continue, So the next request is the request for resetting the password. The request requires three parameters: password & password_confirmation & email

Press enter or click to view image in full size

I tried to put another email, in this case, was victim email, but I got 400 bad request

Press enter or click to view image in full size

In the last pic I observed some things:

The verification of the token was in a separate request.
The request to change the password doesn’t require any token or something to prove that you’re the account owner
The response when I changed the email with the victim email was suspicious, I didn’t expect 400 bad request ever!

After some searching and trying some of the known techniques, actually, I got nothing

On the next day, I continued trying to understand how the site resets the password because I felt that I missed something and I observed some weird behavior on the site. The same request which gave me 200 OK in the first time

Press enter or click to view image in full size

when I sent the same request again, I got 400 Bad request , it’s the same response if tried to put the victim's email !!

Press enter or click to view image in full size

So,mmmmmmmmmmm at this point I think I got the site logic

Since the site doesn’t require any token while resetting the password, and at the same time gives me 400 Bad request when I try to put another email or put my email for another time after resetting and getting 200 OK.

Get Mahmoud Youssef’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I think that the site only checks if the sent email in the reset request has requested to reset his password or not, regardless of the sent token or verified hash. So let’s exploit it!!

Exploitation:
Firstly, we’ll send a password reset link to the attacker and victim's email
We’ll ignore all the verification of the token because it’s useless as it’s not used to validate the identity. We just need the site to know that the victim will reset his password and we’ll take charge of the other steps
Press enter or click to view image in full size
Press enter or click to view image in full size

So, now the site knows that VICTIM-EMAIL@gmail.com will reset his password ok now we’ll continue the regular process to reset the password, and when the site sends the password & password_confirmation & email we’ll replace our email with the victim's email. And voila I reseted his password successfully

Press enter or click to view image in full size

I went to the login panel and type the victim email and the password I set, and……. I’mmmmmm innn.

Actually, I didn’t expect it will be easy like this, but it took time just to understand the site behavior.

How about taking over the Admin account?

When I have a target to test, I collect as much I can the employee's emails from Github and LinkedIn, and keep it for default credentials and some stuff like that, So I think it’s time to use it now.

I made a request to reset the password, then intercepted it and sent it to the intruder to see which account on my list exists as admin on the site.

Press enter or click to view image in full size

And voilaaaaaaa !! I found one that exists.

Actually, I didn’t go deeper to reset the employee's password, I just informed the security team that I could take over one of the employees and he may have high privilege access to the site.

— — — — — — — —

and now I’m done. Thanks for reading!

For any feedback or questions, just dm me on Twitter

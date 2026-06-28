---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-28_how-i-was-able-to-take-over-any-account-via-the-password-reset-functionality.md
original_filename: 2020-06-28_how-i-was-able-to-take-over-any-account-via-the-password-reset-functionality.md
title: How I was able to take over any account via the Password Reset Functionality.
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- rate-limit
- api-security
language: en
raw_sha256: 9bfda3cfb865d994f7ef02f5601f26b9f9475454cc89b5fe46c18d58f43968b0
text_sha256: 65af5e8552db492d630114d2ff9dc125880f26b2be6abf947bca9199296a83a3
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to take over any account via the Password Reset Functionality.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-28_how-i-was-able-to-take-over-any-account-via-the-password-reset-functionality.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9bfda3cfb865d994f7ef02f5601f26b9f9475454cc89b5fe46c18d58f43968b0`
- Text SHA256: `65af5e8552db492d630114d2ff9dc125880f26b2be6abf947bca9199296a83a3`


## Content

---
title: "How I was able to take over any account via the Password Reset Functionality."
url: "https://medium.com/@fatnassifiras45/how-i-was-able-to-take-over-any-account-via-the-password-reset-functionality-ef1659f8b481"
authors: ["Firas Fatnassi (@Fatnass1F1ras)"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2020-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4466
scraped_via: "browseros"
---

# How I was able to take over any account via the Password Reset Functionality.

Top highlight

How I was able to take over any account via the Password Reset Functionality.
Firas Fatnassi
Follow
4 min read
·
Jun 28, 2020

978

4

Hey, This is my first writeup and I will talk about an account takeover that I found in May on a vulnerability disclosure program. Let’s assume https://target.com is the target since the program does not allow public disclosure.

The first thing I do when I start hunting for a new target is navigating the entire application to understand it (What does it do, the main functionality, Technologies used..), After that, I test the Password Reset Functionality.

How I test bugs in password reset functionality:
I change hosts when sending the request.
I look for the token in response.
Tamper with id/email params if available (Add them if not).
I collect a good number of tokens and analyze them by asking questions like this:
Can it be decoded?
Is it bruteForcable?
Is it predictable?
What part of the token remains the same?

So, when testing the password reset functionality on target.com the first 3 tests failed no host header injection, no token leakage as well there is no ID/Email params. However, after collecting about 8 tokens I figured out that there are 2 parts of the token that remains the same and the other 2 parts change every time.

Green: Remains the same/Orange: changes every time

Although the part that changes every time is smaller than the static part I still cannot brute-force the token since the orange part contains letters/numbers and they are random. So I saved the tokens, took some notes, and moved to test other functionalities.

After, 3–5 days while reading my notes I wanted to give it another shot. So, I opened https://target.com, made another account, and manually I sent 2 requests to reset the password(One to my 1st account, and one to my 2nd account). Got the tokens, Copied/pasted them on my bloc note, and to my surprise, the tokens differ only in the last 3 characters.

It seems like the shorter the duration between the requests the more the tokens are similar.

You would ask why when I first collected the tokens I did get 5 different characters. It’s because I was sending 1 request at a time, save the token and repeat again.

Get Firas Fatnassi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now we have 2 tokens that differ only in the last 3 characters but still, they are random. Which makes it hard If not impossible to brute-force. So, I thought maybe if I send them with burp intruder I can get better results since intruder sends requests faster than my hands :D. I fired up BurpSuite, captured the request, send it to the intruder:

Payloads: My 2 accounts emails.
Threads: 20
URL-Encode: OFF
Intruder’s attack payloads.

Now, after configuring burp intruder I launched the attack and boom I got 2 tokens that differ only in the last character.

Attack scenario:

With burp intruder, I send 2 password reset links one for me and one for the victim.
The password reset link looks like this: https://exmaple.com/reset/5ec6ea8d546ca610758297e*2*
By design, if I visit a password reset link with an invalid token the application won’t display the form to change the password. So, I only have to change the last number and check if the form is there.
Press enter or click to view image in full size

Also, I found an API endpoint from which I can enumerate email addresses, which will make it easier for an attacker.

Finally, I reported the bug. And even though it was a VDP they rewarded me with a bounty!

Takeaways:
Take notes so when you learn something new or you get new ideas you can test them.
Always think outside the box, ask good questions.

My Twitter: https://twitter.com/Fatnass1F1ras

Big thanks to Rajesh Ranjan and Ananda Dhakal for checking the draft of this article.

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live

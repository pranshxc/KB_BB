---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-23_story-of-a-beautiful-account-takeover_2.md
original_filename: 2023-03-23_story-of-a-beautiful-account-takeover_2.md
title: Story of a Beautiful Account Takeover.
category: documents
detected_topics:
- password-reset
- otp
- rate-limit
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- password-reset
- otp
- rate-limit
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: dd2d03d6a3736875a0a5d9cb9d87aee29c09cc63211ae3b0d23a072579ac71bc
text_sha256: b32185a79a778818d94f4c0f57f3a0f7b6046e99ebba840ccae486625fa6a42b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a Beautiful Account Takeover.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-23_story-of-a-beautiful-account-takeover_2.md
- Source Type: markdown
- Detected Topics: password-reset, otp, rate-limit, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `dd2d03d6a3736875a0a5d9cb9d87aee29c09cc63211ae3b0d23a072579ac71bc`
- Text SHA256: `b32185a79a778818d94f4c0f57f3a0f7b6046e99ebba840ccae486625fa6a42b`


## Content

---
title: "Story of a Beautiful Account Takeover."
url: "https://medium.com/@ambushneupane4/story-of-a-beautiful-account-takeover-869ef61ac6c8"
authors: ["Ambush Neupane (@N_ambush)"]
bugs: ["Account takeover", "OTP bypass"]
publication_date: "2023-03-23"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1345
scraped_via: "browseros"
---

# Story of a Beautiful Account Takeover.

Story of a Beautiful Account Takeover.
Ambush Neupane
Follow
5 min read
·
Mar 23, 2023

362

9

Hello Everyone, I am Ambush Neupane from Nepal. I hope you all are doing great. This is my first blog and in this blog I am going to explain how I found an interesting security issue in a dutch government site which could have allowed an attacker to gain unauthorized access to any registered account with “just” information of users email address.

You might say ,Huhhhh!!!, That’s a big “just” in the first place. Attacker getting Email addresses of registered users would be an issue on its own .

Yes you are right but in this case the program has a feature of public profile and allows users to make their email address public. So for the attack to be carried out getting email won’t be a big issue. Furthermore, accessing any account with just information of email would still be quite a concerning issue

So without a further ado let’s start the Story.
If you don’t have time to stick till the end Here’s a TLDR for you. :)

TLDR:- OTP was used for email verification after signup. I simply changed my email address to the victim’s email address in the request during the email verification step and account takeover was possible.

For those who have decided to read till the end , I will try my best to explain every detail on how I got the issue.

Technical Details and My failed attempts for the A/TO:-

After signing up, an OTP was sent to my email address for the verification. I entered the OTP and My account was sent for admin’s permission. (Yes, We need admin’s permission to successfully create and start using the account). After a few days I received mail which said I was now able to use the account on the site.

I logged into the account and played around with the functionalities. After spending some time understanding the site, I decided to Jump into Login and Forgot Password Feature.

In the forgot password feature, a 6 digit verification code is sent to my email address.Entered random OTP and captured the request in burp. I saw an OTP ,email address and some kind of token was passed in the request.

My failed attempts for account takeover:-

1)Checked if OTP is leaked somewhere in the response or is sent along with the request. NO it wasn’t.

2) Left the OTP value blank and forwarded the request as sometimes the application validates the OTP only if its value is present. But Not this time so it didn’t work.

3) Completely removed the ‘OTP’ parameter from the request and forwarded it. This also resulted in error.

4) Passed an array of emails[“attacker.@xyz.com”,“victim.@xyz.com”] to check how the application behaves.Does It send the same OTP to both
accounts? No It didn’t.

5) Entered the correct OTP but changed my email address to the victim’s address. Unsuccessful, The OTP seems to be tied with the email address.

6) Tried to brute-force the code but there was some kind of rate limiting present. So it also failed.

Get Ambush Neupane’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

7) Sometimes passing an array of numbers/OTP with the valid one might result in something interesting. Check this. So I passed the array of few OTP along with the valid one. This also didn’t work.

8) To check the randomness of the OTP I decided to send many requests at a time in the forget password endpoint. But I got an error saying too many requests. So most probably there was some kind of limit on it.

Nothing worked Lol.

As I got nothing in the Password Reset feature. I thought of testing the signup function as it was also sending OTP for verification.

I tried to create an account with an already registered email to see how the site behaves but nothing interesting happened as it threw an “Email already Exists” error. I carried out my further testing by adding %00, space at the end, space at the beginning of the email but none of my attack ideas were successful. I didn’t get anything here.

So I forwarded the request and it asked me to enter the OTP sent to my address. The following request was made for validating the OTP.

I played with the OTP just like I did in the forget Password endpoint but I didn’t get any success in this either. I also tried to bypass it with a response manipulation technique but Nope it didn’t work. Following is the response of my unsuccessful attempts.

In the request above I noticed an email address present in. I changed my address[attacker@gmail.com] with the victim’s address[victim@gmail.com]. Following was the response I got:-

I have modified the values for Privacy reasons.

Hmmmm something happened right? Yes, I got information about the victim in the response. Is that Information leak? Well as I mentioned earlier that the site had a public profile feature so this information can easily be achieved simply by viewing the profile.

So I Forwarded it and in the next request I saw the token of the victim and upon forwarding the request I was logged into the Victim’s account.
Beautiful, isn’t it? That’s what I said when I saw the victim’s account on my browser :).

I was surprised and TBH really excited to see this. I controlled my excitement and tested it for the verification and Yes it’s possible to log into the account with just email information.

So basically, I can takeover any account I want with the email address of the victim and without User Interaction. I made a POC video and sent the report to the Dutch government.
Looking at it, it seems to be an easy find. Simply change the email to victim’s address and get access to the account. But understanding and finding this endpoint took quite a long time for me. Also,it was really boring and frustrating as I had to enter a new address every time and verify it with the OTP.
The vulnerability is fixed now and they have decided to send me a Lousy T-shirt as a Swag.

Thank you for taking time to Complete this. Hope you guys enjoyed it. Feedbacks are always Welcome. That’s it for today.

Twitter:- @N_ambush

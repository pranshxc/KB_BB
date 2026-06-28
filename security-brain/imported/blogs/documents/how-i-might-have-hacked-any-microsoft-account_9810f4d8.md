---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-02_how-i-might-have-hacked-any-microsoft-account.md
original_filename: 2021-03-02_how-i-might-have-hacked-any-microsoft-account.md
title: How I Might Have Hacked Any Microsoft Account
category: documents
detected_topics:
- mfa
- rate-limit
- password-reset
- command-injection
- automation-abuse
- race-condition
tags:
- imported
- documents
- mfa
- rate-limit
- password-reset
- command-injection
- automation-abuse
- race-condition
language: en
raw_sha256: 9810f4d853eb85ca17f50177a758dc5f05e0f94ff9423c373248dbdd0fd02a0e
text_sha256: 20d6ef279061c1ae7f2be5bd8b29a27adcd510422a73ac4174769bd1589cce86
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I Might Have Hacked Any Microsoft Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-02_how-i-might-have-hacked-any-microsoft-account.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, password-reset, command-injection, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9810f4d853eb85ca17f50177a758dc5f05e0f94ff9423c373248dbdd0fd02a0e`
- Text SHA256: `20d6ef279061c1ae7f2be5bd8b29a27adcd510422a73ac4174769bd1589cce86`


## Content

---
title: "How I Might Have Hacked Any Microsoft Account"
page_title: "How I Might Have Hacked Any Microsoft Account - The Zero Hack"
url: "https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account"
final_url: "https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account"
authors: ["Laxman Muthiyah (@laxmanmuthiyah)"]
programs: ["Microsoft"]
bugs: ["Account takeover", "Password reset", "Bruteforce", "2FA / MFA bypass"]
bounty: "50,000"
publication_date: "2021-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3845
---

# How I Might Have Hacked Any Microsoft Account

[![Laxman Muthiyah](https://secure.gravatar.com/avatar/b86030f152800e9eb32868123706a65f29e57b9c2cf221b504460ae27f64d655?s=96&d=mm&r=g)](https://thezerohack.com/author/laxmanm1 "Laxman Muthiyah")

By [Laxman Muthiyah](https://thezerohack.com/author/laxmanm1)

__

__December 6, 2024

__

[ Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhow-i-might-have-hacked-any-microsoft-account "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=How+I+Might+Have+Hacked+Any+Microsoft+Account&url=https%3A%2F%2Fthezerohack.com%2Fhow-i-might-have-hacked-any-microsoft-account&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account&media=https://thezerohack.com/wp-content/uploads/2021/03/How-I-Could-Have-Hacked-Any-Microsoft-Account.jpg&description=How+I+Might+Have+Hacked+Any+Microsoft+Account "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=How+I+Might+Have+Hacked+Any+Microsoft+Account %0A%0A https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "WhatsApp")

__

_This article is about how I found a vulnerability on Microsoft online services that might have allowed anyone to takeover any Microsoft account without consent permission. Microsoft security team patched the issue and rewarded me $50,000 as a part of their Identity Bounty Program._

After my [Instagram account takeover vulnerability](https://thezerohack.com/hack-any-instagram), I was searching for similar loopholes in other services. I found Microsoft is also using the similar technique to reset user’s password so I decided to test them for any rate limiting vulnerability. 

To reset a Microsoft account’s password, we need to enter our email address or phone number in their [forgot password page](https://account.live.com/ResetPassword.aspx), after that we will be asked to select the email or mobile number that can be used to receive security code. 

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Once we receive the 7 digit security code, we will have to enter it to reset the password. Here, if we can bruteforce all the combination of 7 digit code (that will be 10^7 = 10 million codes), we will be able to reset any user’s password without permission. But, obviously, there will be some rate limits that will prevent us from making large number of attempts. 

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Intercepting the HTTP POST request made to code validation endpoint looked like this

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

If you look at the screenshot above, the code 1234567 we entered was nowhere present in the request. It was encrypted and then sent for validation. I guess they are doing this to prevent automated bruteforce tools from exploiting their system. So, we cannot automate testing multiple codes using tools like Burp Intruder since they won’t do the encryption part 😕

![confused jimmy fallon GIF by The Tonight Show Starring Jimmy Fallon](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

After some time, I figured out the encryption technique and was able to automate the entire process from encrypting the code to sending multiple concurrent requests. 

My initial test showed the presence of rate limits as expected. Out of 1000 codes sent, only 122 of them got through, others are limited with 1211 error code and they are blocking the respective user account from sending further attempts if we continuously send requests. 

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Then, I tried sending simultaneous / concurrent requests like I did for Instagram, that allowed me to send large number of requests without getting blocked but I was still unable to get the successful response while injecting the correct 7 digit security code. I thought they have some controls in place to prevent this type of attack. Although I am getting an error while sending the right code, there was still no evidence of blocking the user like we saw in the initial test. So I was still hoping that there would be something.

![Never Give Up Reaction GIF by Best Friends Animal Society](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

After some days, I realized that they are blacklisting the IP address if all the requests we send don’t hit the server at the same time, even a few milliseconds delay between the requests allowed the server to detect the attack and block it. Then I tweaked my code to handle this scenario and tested it again. 

![Supernatural Dean Winchester GIF](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Surprisingly, it worked and I was able to get the successful response this time 😀 

![Celebration Dancing GIF by Juli](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

I sent around 1000 seven digit codes including the right one and was able to get the next step to change the password. 

The above process is valid only for those who do not have two factor authentication enabled, if a user has enabled 2FA, we will have to bypass two factor code authentication as well, to change the password. 

I tested an account with 2FA and found both are same endpoint that are vulnerable to this type of attack. At first, user will be prompted to enter a 6 digit code generated by authenticator app, only then they will be asked to enter 7 digit code sent to their email or phone number. Then, they can change the password. 

**Putting all together, an attacker has to send all the possibilities of 6 and 7 digit security codes that would be around 11 million request attempts and it has to be sent concurrently to change the password of any Microsoft account (including those with 2FA enabled).**

It is not at all a easy process to send such large number of concurrent requests, that would require a lot of computing resources as well as 1000s of IP address to complete the attack successfully. 

Immediately, I recorded a video of all the bypasses and submitted it to Microsoft along with detailed steps to reproduce the vulnerability. They were quick in acknowledging the issue. 

**Also, see how hackers[hack IG account](https://thezerohack.com/hack-instagram) and their prevention techniques.**

The issue was patched in November 2020 and my case was assigned to different security impact than the one expected. I asked them to reconsider the security impact explaining my attack. After a few back and forth emails, my case was assigned to **Elevation of Privilege (Involving Multi-factor Authentication Bypass)**. Due to the complexity of the attack, bug severity was assigned as important instead of critical.

## **Bount email from MSRC**

  * ![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

## **Microsoft Acknowledgement for Reporting this issue**

  * ![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

I received the bounty of $50,000 USD on Feb 9th, 2021 through hackerone and got approval to publish this article on March 1st. I would like to thank Dan, Jarek and the entire MSRC Team for patiently listening to all my comments, providing updates and patching the issue. I also like to thank Microsoft for the bounty 🙏 😊

_This article is available as[PDF Download](https://thezerohack.com/publications/hacking-any-microsoft-account.pdf)_.

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhow-i-might-have-hacked-any-microsoft-account "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=How+I+Might+Have+Hacked+Any+Microsoft+Account&url=https%3A%2F%2Fthezerohack.com%2Fhow-i-might-have-hacked-any-microsoft-account&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account&media=https://thezerohack.com/wp-content/uploads/2021/03/How-I-Could-Have-Hacked-Any-Microsoft-Account.jpg&description=How+I+Might+Have+Hacked+Any+Microsoft+Account "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=How+I+Might+Have+Hacked+Any+Microsoft+Account %0A%0A https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "WhatsApp")

__

[![Laxman Muthiyah](https://secure.gravatar.com/avatar/b86030f152800e9eb32868123706a65f29e57b9c2cf221b504460ae27f64d655?s=96&d=mm&r=g)](https://thezerohack.com/author/laxmanm1 "Laxman Muthiyah")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1)

Security researcher • Web developer • Aspiring entrepreneur — fueled by curiosity and exploration.

[__](https://www.facebook.com/laxmanmuthiyah "Facebook")[__](https://www.linkedin.com/in/laxman-muthiyah-2a0a1797/ "Linkedin")[__](https://twitter.com/laxmanmuthiyah "Twitter")

### Related Stories

[ ](https://thezerohack.com/apple-vulnerability-bug-bounty "How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It](https://thezerohack.com/apple-vulnerability-bug-bounty "How I Found A Vulnerability To Hack iCloud Accounts and How Apple Reacted To It")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - June 20, 2021

[ ](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Hacked Instagram Again](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - August 25, 2019

[ ](https://thezerohack.com/hack-any-instagram "How I Could Have Hacked Any Instagram Account")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Could Have Hacked Any Instagram Account](https://thezerohack.com/hack-any-instagram "How I Could Have Hacked Any Instagram Account")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - July 14, 2019

[ ](https://thezerohack.com/hack-instagram "8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures](https://thezerohack.com/hack-instagram "8 Ways To Hack Someone’s Instagram Account and Its Prevention Measures")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - September 15, 2018

[ ](https://thezerohack.com/hack-facebook-password "11 Hacker Ways To Hack Facebook Account Without Password")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [11 Hacker Ways To Hack Facebook Account Without Password](https://thezerohack.com/hack-facebook-password "11 Hacker Ways To Hack Facebook Account Without Password")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - December 19, 2017

[ ](https://thezerohack.com/3-ways-recover-hacked-facebook-account "3 Ways to Recover Hacked Facebook Account")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [3 Ways to Recover Hacked Facebook Account](https://thezerohack.com/3-ways-recover-hacked-facebook-account "3 Ways to Recover Hacked Facebook Account")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - February 6, 2017

#### 9 Comments

  1. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Abdu ELkam March 2, 2021 At 10:34 pm

This article misses so many things, how the encryption worked and what you did to decrypt it, sharing the script code would be great too, how you bypassed the rate limit (details)? if it was a CTF it would be strange to read “there was a rate limit, there was an encryption, I wrote a tool for the encryption, I modified the tool once, it worked”, this is very superficial.

Reply

  2. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) chaitanya krishna March 3, 2021 At 8:59 am

Hi Laxman I was following you since your first Insta hack you inspired but I don’t know where to start for become a bounty hunter like you . I have only hope on you please

Reply

  3. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/add75d306f470a751e78ead1d0d58131x96.png) Hackerhumble March 3, 2021 At 10:51 am

Superb article.

May I know how is it possible to send those number of requests concurrently please ?

Reply

  4. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Arun J March 3, 2021 At 8:32 pm

Can u pls share the source code for brute force?

Reply

  5. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Shiv](https://www.iitmind.com) March 4, 2021 At 12:04 am

Incredible!!!

Reply

  6. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/c510febb9bed68b5cc4a09f076701e0fx96.png) Anonymous March 4, 2021 At 4:09 am

” After some days, I realized that they are blacklisting the IP address if all the requests we send don’t hit the server at the same time”  
How did you bypassed this?

Reply

  7. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Vineeth March 4, 2021 At 10:47 pm

Hello Laxman, 

Congrats for your recognition from Microsoft for what you have. If possible please please make a course on bug bounty hunts. 

Regards,  
Vineeth.

Reply

  8. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) DotBot March 6, 2021 At 12:08 am

Can you please explain how did you make sure that all 1000 requests hit the server at the same time?  
Since network is not reliable requests have +-ms range, I was never able to do that.

Reply

  9. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) min March 8, 2021 At 8:38 pm

hi, i guess the encryption technique is aes?

Reply

### Leave A Reply [Cancel reply](/how-i-might-have-hacked-any-microsoft-account#respond)

Comment:

Please enter your comment!

Name:*

Please enter your name here

Email:*

You have entered an incorrect email address!

Please enter your email address here

Website:

Save my name, email, and website in this browser for the next time I comment.

### Stay on top - Get the latest updates in your inbox

Subscribe

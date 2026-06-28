---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-14_how-i-could-have-hacked-any-instagram-account.md
original_filename: 2019-07-14_how-i-could-have-hacked-any-instagram-account.md
title: How I Could Have Hacked Any Instagram Account
category: documents
detected_topics:
- rate-limit
- password-reset
- race-condition
- mobile-security
- sso
- command-injection
tags:
- imported
- documents
- rate-limit
- password-reset
- race-condition
- mobile-security
- sso
- command-injection
language: en
raw_sha256: 201b447bfebf12f9c845f04bb92320cbbeb6866d1fc1a0be030e7c6bce772103
text_sha256: f7a528a4c091c13e8b29c689d977e237b2f0a001666dbd0a65e6d3a0793fbc3f
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I Could Have Hacked Any Instagram Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-14_how-i-could-have-hacked-any-instagram-account.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, race-condition, mobile-security, sso, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `201b447bfebf12f9c845f04bb92320cbbeb6866d1fc1a0be030e7c6bce772103`
- Text SHA256: `f7a528a4c091c13e8b29c689d977e237b2f0a001666dbd0a65e6d3a0793fbc3f`


## Content

---
title: "How I Could Have Hacked Any Instagram Account"
page_title: "How I Could Have Hacked Any Instagram Account - The Zero Hack"
url: "https://thezerohack.com/hack-any-instagram"
final_url: "https://thezerohack.com/hack-any-instagram"
authors: ["Laxman Muthiyah (@LaxmanMuthiyah)"]
programs: ["Meta / Facebook"]
bugs: ["Race condition", "Rate limiting bypass"]
bounty: "30,000"
publication_date: "2019-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5151
---

# How I Could Have Hacked Any Instagram Account

[![Laxman Muthiyah](https://secure.gravatar.com/avatar/b86030f152800e9eb32868123706a65f29e57b9c2cf221b504460ae27f64d655?s=96&d=mm&r=g)](https://thezerohack.com/author/laxmanm1 "Laxman Muthiyah")

By [Laxman Muthiyah](https://thezerohack.com/author/laxmanm1)

__

__October 19, 2024

__

[ Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhack-any-instagram "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=How+I+Could+Have+Hacked+Any+Instagram+Account&url=https%3A%2F%2Fthezerohack.com%2Fhack-any-instagram&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/hack-any-instagram&media=https://thezerohack.com/wp-content/uploads/2018/09/hack-instagram.jpg&description=How+I+Could+Have+Hacked+Any+Instagram+Account "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=How+I+Could+Have+Hacked+Any+Instagram+Account %0A%0A https://thezerohack.com/hack-any-instagram "WhatsApp")

__

_This article is about how I found a vulnerability on Instagram that allowed me to hack any Instagram account without consent permission. Facebook and Instagram security team fixed the issue and rewarded me $30000 as a part of their bounty program._

Facebook is working constantly to improve its security controls on all of their platforms. As a part of it, they recently increased reward payouts for all critical vulnerabilities including account takeovers. So I decided to try my luck on Facebook and Instagram. Fortunately, I was able to find one on Instagram.

Instagram forgot password endpoint is the first thing that came to my mind while looking for an account takeover vulnerability. I tried to reset my password on the Instagram web interface. They have a link based password reset mechanism which is pretty strong and I couldn’t find any bugs after a few minutes of testing.

Then switched to their mobile recovery flow, where I was able to find a susceptible behavior. When a user enters his/her mobile number, they will be sent a six-digit passcode to their mobile number. They have to enter it to change their password. Therefore if we are able to try all the one million codes on the verify-code endpoint, we would be able to change the password of any account. But I was pretty sure that there must be some rate limiting against such brute-force attacks. I decided to test it.

My tests did show the presence of rate limiting. I sent around 1000 requests, 250 of them went through and the rest 750 requests were rate limited. Tried another 1000, now many of them got rate limited. So their systems are validating and rate limiting the requests properly.

Two things that struck mind was the number of requests and the absence of blacklisting. I was able to send requests continuously without getting blocked even though the number of requests I can send in a fraction of time is limited.

After a few days of continuous testing, I found two things that allowed me to bypass their rate limiting mechanism.

  1. Race Hazard
  2. IP rotation

For those who are unaware of race condition, please [read it here](https://resources.securitycompass.com/blog/race-condition-web-applications). Sending concurrent requests using multiple IPs allowed me to send a large number of requests without getting limited. The number of requests we can send is dependent on concurrency of reqs and the number of IPs we use. Also, I realized that the code expires in 10 minutes, it makes the attack even harder, therefore we need 1000s of IPs to perform the attack.

I reported the vulnerability to the Facebook security team and they were unable to reproduce it initially due to lack of information in my report. After a few emails and solid proof of concept video, I was able to convince them that the attack is feasible.

**Also, see how hackers[hack Instagram account](https://thezerohack.com/hack-instagram) and their prevention techniques.**

#### **Proof of concept:**

##### **Requesting passcode**

_POST /api/v1/users/lookup/ HTTP/1.1_  
 _User-Agent: Instagram 92.0.0.11.114 Android (27/8.1.0; 440dpi; 1080×2150; Xiaomi/xiaomi; Redmi Note 6 Pro; tulip; qcom; en_IN; 152830654)_  
_Accept-Language: en-IN, en-US_  
 _Content-Type: application/x-www-form- urlencoded; charset=UTF-8_  
 _Accept-Encoding: gzip, deflate_  
 _Host:[i.instagram.com](https://i.instagram.com/)_  
 _Connection: keep-alive_

_q=mobile_number &device_id=android-device-id-here_

The victim will receive a passcode and it will expire in 10 minutes.

##### **Verify passcode**

POST /api/v1/accounts/account_recovery_code_verify/ HTTP/1.1  
User-Agent: Instagram 92.0.0.11.114 Android (27/8.1.0; 440dpi; 1080×2150; Xiaomi/xiaomi; Redmi Note 6 Pro; tulip; qcom; en_IN; 152830654)  
Accept-Language: en-IN, en-US  
Content-Type: application/x-www-form-urlencoded; charset=UTF-8  
Accept-Encoding: gzip, deflate  
Host: [i.instagram.com](https://i.instagram.com/)  
Connection: keep-alive

recover_code=123456&device_id=_android-device-id-here_

Now we need to brute-force this endpoint using multiple IPs. Roughly, I was able to send 200 requests from a single IP without hitting rate limit.

I have used 1000 different machines (to achieve concurrency easily) and IPs to send 200k requests (that’s 20 percent of total one million probability) in my tests.

#### **Sending 200k requests**

In a real attack scenario, the attacker needs 5000 IPs to hack an account. It sounds big but that’s actually easy if you use a cloud service provider like Amazon or Google. It would cost around 150 dollars to perform the complete attack of one million codes.

The Facebook security team was convinced after providing the above video of sending 200k valid requests. They were also quick in addressing and fixing the issue.

#### **After the patch**

[![Bounty](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://thezerohack.com/wp-content/uploads/2019/07/Bounty.jpg)$30000 USD Reward

I thank Facebook security team for rewarding me through their bug bounty program. Let me know your thoughts in comments 🙂

_This article is available as[PDF Download](https://thezerohack.com/publications/hacking-any-instagram-account.pdf)_.

__

Share

[__Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fthezerohack.com%2Fhack-any-instagram "Facebook")[ __Twitter](https://twitter.com/intent/tweet?text=How+I+Could+Have+Hacked+Any+Instagram+Account&url=https%3A%2F%2Fthezerohack.com%2Fhack-any-instagram&via=laxmanmuthiyah "Twitter")[ __Pinterest](https://pinterest.com/pin/create/button/?url=https://thezerohack.com/hack-any-instagram&media=https://thezerohack.com/wp-content/uploads/2018/09/hack-instagram.jpg&description=How+I+Could+Have+Hacked+Any+Instagram+Account "Pinterest")[ __WhatsApp](https://api.whatsapp.com/send?text=How+I+Could+Have+Hacked+Any+Instagram+Account %0A%0A https://thezerohack.com/hack-any-instagram "WhatsApp")

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

[ ](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "How I Might Have Hacked Any Microsoft Account")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Might Have Hacked Any Microsoft Account](https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account "How I Might Have Hacked Any Microsoft Account")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - March 2, 2021

[ ](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Hacks / Security](https://thezerohack.com/bug-bounty-hacks)

### [How I Hacked Instagram Again](https://thezerohack.com/hack-instagram-again "How I Hacked Instagram Again")

[Laxman Muthiyah](https://thezerohack.com/author/laxmanm1) - August 25, 2019

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

#### 23 Comments

  1. ![](https://secure.gravatar.com/avatar/b8e5783104c5b8e13c412fb323b3ab368477048ad085155208e44741c7f6393f?s=50&d=mm&r=g) raji sekar July 15, 2019 At 2:12 am

Smart one bro…  
Keep hunt and inspiring people…

Reply

  * ![](https://secure.gravatar.com/avatar/a68edf5b8c3a9161ea612b6c22fe6226bfbb76d5b541682f6abfaa1dbc830185?s=50&d=mm&r=g) [Laxman Muthiyah](https://zerohacks.com) July 15, 2019 At 7:42 am

Thank you 🙂

Reply

  2. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Mohammad Owais July 15, 2019 At 5:10 am

How did you send many requests with muliple IPs?

Reply

  3. ![](https://secure.gravatar.com/avatar/070b12bf2488a39361884b99d78bc83b56e4bd2d6b39224993a57e693cbebfa8?s=50&d=mm&r=g) John Doe July 15, 2019 At 9:23 am

I have to mention this. By using a windows machine yoy have busted a myth that you need Linux to preform attacks. Kudos keep making the internet a safe place

Reply

  4. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) I Tech Info July 15, 2019 At 1:56 pm

Hey, how can you got those ips?

Reply

  5. ![](https://secure.gravatar.com/avatar/6fa2eb9dcac81f3d37c2a1da2a67968d8baabc218596524cd1610d9b2785f93a?s=50&d=mm&r=g) Memon July 15, 2019 At 1:57 pm

Can you provide your phone code?

Reply

  6. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Bikash Kumar Dora July 15, 2019 At 2:41 pm

Congrats bro, inspiration for us.

Reply

  7. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Anudeep reddy](http://techgeekhub.ml) July 15, 2019 At 3:48 pm

hey, how do you monitor the api calls in android?

Reply

  8. ![](https://secure.gravatar.com/avatar/03c48678f205dff9fe9364e4b2cafede35e4395d1344a2a2376cf87b2c0bb7e4?s=50&d=mm&r=g) Vishal Surelia July 15, 2019 At 5:26 pm

Nice catch 👍🔥

Reply

  9. ![](https://secure.gravatar.com/avatar/90e2b75938dff6d2eb5bfc351f54985c5b7b19eaceb8adc0354d0db68c3f21fd?s=50&d=mm&r=g) Shamil' July 16, 2019 At 6:05 pm

so what about call4.php ? It’s not clear which response leads to “… wrong code”

Reply

  10. ![](https://secure.gravatar.com/avatar/a23194f88155b97b3ea573120d5b03192e9952a102ffcfb4ad95abc9f319c55a?s=50&d=mm&r=g) Rajched July 18, 2019 At 9:12 pm

How did you deploy 1000 instances of EC2?

Reply

  11. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [Douglas Muth](http://www.dmuth.org/) July 18, 2019 At 10:22 pm

Well done, and thanks for reporting it. I do have a question–didn’t AWS’s security systems catch on to the fact that you were using 1K machines to hit the same IP? I figured they would have some anti-DDoS monitoring systems in place to catch things like that. (even though you weren’t DDoSing, it definitely wasn’t a normal usage pattern)

Reply

  12. ![](https://secure.gravatar.com/avatar/7817b2b42fbc613320d8413d4abaa59d4841226686a3e2d97670f4919eee9ce4?s=50&d=mm&r=g) [sha](https://www.aiomag.com) July 19, 2019 At 9:22 am

wow amazing. finally you did it

Reply

  13. ![](https://secure.gravatar.com/avatar/9f87fcb1a8f497c3bc4a1713c4f495c3b3035101db4f19ae4d1fe999ebe3e55b?s=50&d=mm&r=g) Paresh Solanki July 19, 2019 At 1:34 pm

I don’t no why We (India) do not have our own social media app or other IT’s complicated but very useful things! when we have so many talented Laxman in our country, your work is plausible bro, keep it up. 👏👏👏

Reply

  14. ![](https://secure.gravatar.com/avatar/df9a8c7536f678fcd88922b7be6e76efe6914df02416ce32c2d6c6cd7652cdbc?s=50&d=mm&r=g) Spydiii Star July 20, 2019 At 1:34 pm

Hey bro… congrats for what u did…i really feel proud as an Indian…keep doing so…hey I gonna want to talk to u…how can i contact u?

Reply

  15. ![](https://secure.gravatar.com/avatar/ced89a12ba5a179c0cfe10ed41b1c3d773d26cde129bb14450392a6d0efc76a4?s=50&d=mm&r=g) Ueli Kunz July 24, 2019 At 7:06 am

Good job. But maybe / hopefully it is already hard to retrieve a suitable android-device-id / IMEI.

Reply

  16. ![](https://secure.gravatar.com/avatar/50176d51b04fc267076a0a4fbd8618f48defe4ebc0657ddae318753b664791ce?s=50&d=mm&r=g) Christopher July 25, 2019 At 2:58 pm

Hey

Reply

  17. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) [杨鼎睿](https://yuque.com/abser) July 26, 2019 At 7:53 am

So good!  
I Found that find leak or bug need knowledge but a liiiiitte .  
You are good at thinking

Reply

  18. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) izzi April 9, 2020 At 11:52 pm

It was helpful. Keep on posting!

Reply

  19. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Aaron July 10, 2020 At 1:34 am

Great job! Well deserved. This was a clever workaround. Something I will keep in mind for other scenarios.

Reply

  20. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Abhishek July 11, 2020 At 12:53 pm

I have lost my phone number, so I am not getting OTP from Instagram, even I am filling right I’d and password, they wants to verify with OTP , I have not linked my facebook and Gmail to my Instagram, please HELP 😥😥😥😥

Reply

  21. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Firoz July 15, 2020 At 11:36 am

Bro can send me the hacking tips

Reply

  22. ![](https://thezerohack.com/wp-content/uploads/fv-gravatar-cache/mystery96.png) Baloch_ meher.47 July 15, 2020 At 12:40 pm

Nyc

Reply

### Leave A Reply [Cancel reply](/hack-any-instagram#respond)

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

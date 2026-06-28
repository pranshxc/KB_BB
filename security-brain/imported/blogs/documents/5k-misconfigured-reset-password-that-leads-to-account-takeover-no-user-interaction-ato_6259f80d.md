---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-24_5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interacti.md
original_filename: 2021-08-24_5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interacti.md
title: '[$5K] Misconfigured Reset password that leads to Account Takeover (No user
  Interaction ATO)'
category: documents
detected_topics:
- password-reset
- oauth
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- password-reset
- oauth
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 6259f80dce61527d40b7a5f5c493aebf087587375b5190ec996b1bc069f9887b
text_sha256: 2a07f6459c0f82f1ffd4851e7ef1350e7d18e9c56bbf76dec5a2041dfa912852
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# [$5K] Misconfigured Reset password that leads to Account Takeover (No user Interaction ATO)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-24_5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interacti.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6259f80dce61527d40b7a5f5c493aebf087587375b5190ec996b1bc069f9887b`
- Text SHA256: `2a07f6459c0f82f1ffd4851e7ef1350e7d18e9c56bbf76dec5a2041dfa912852`


## Content

---
title: "[$5K] Misconfigured Reset password that leads to Account Takeover (No user Interaction ATO)"
url: "https://medium.com/@noob.assassin/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183"
authors: ["Aditya Sharma (@Assass1nmarcos)"]
bugs: ["Account takeover", "Password reset", "Information disclosure"]
bounty: "5,000"
publication_date: "2021-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3394
scraped_via: "browseros"
---

# [$5K] Misconfigured Reset password that leads to Account Takeover (No user Interaction ATO)

[$5K] Misconfigured Reset password that leads to Account Takeover (No user Interaction ATO)
Aditya Sharma
Follow
4 min read
·
Aug 24, 2021

1.2K

2

Hello Folks,

I hope you are all keeping yourselves safe and healthy through this challenging time, Aditya here today I would like to share one of my findings that I came across on a public program on Hackerone which I expect is known by many of them here, so let’s begin.

Summary

I usually hunt on Hackerone and while hunting on it, one of the well-known public program grabbed my attention, nothing much about the target but it’s one of the leading online Adult Entertainment Platform so you can guess it ;)(They also have Private with a wide scope so I got invited for submitting this finding to their private program as the domain was out of scope in public program)

I found out there is a page for affiliate registration which has the Vulnerable function of Password Reset that leads to Account takeover.

This is one of my interesting and quickly found critical issue wherein I was able to exploit this vulnerability within 5–10 mins of time so let’s get started and know more about it. Let’s assume the vulnerable target as company.com

Pic1: let's hack it boi
Technical Details and Exploiting the Issue in wild:

When Testing on the Login Pages and Signup page I didn’t Find anything impressive here, There was an OAuth miss-config which led to an Open redirect on the login page. I also tested the forgot password functionality and as expected it sends a reset token link on performing the forgot password action so no luck here.

But I didn’t give up here and tried my luck again and looked into the page source of the application to discover anything interesting as the web application was working on AJAX Request(AJAX allows web pages to be updated asynchronously by exchanging data with a web server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.). When the user clicks on forgot password there is no process or reloading on-page, the user just gets a password reset link with a set of unique tokens. An ordinary user will have no idea of what’s happening behind there.

Pic 2: AJAX Working Process

As there was an endpoint in the XMLHttpRequest which be like:

https://company.com/api/REDACTED/resetPasswordToken/

The response looked somewhat like this:

Press enter or click to view image in full size
Pic 3: Response of Vulnerable Endpoint

Then I intercepted the Request of Reset password page again:

https://company.com/api/REDACTED/resetPassword<username>

I intercepted the Reset password request again and this time I focused on the response received for the following POST request and the response was something which I was not expecting and I was like Daaaummm !!!!

Pic 4: Reaction after successful exploit

The Response Looks like this:

Press enter or click to view image in full size
Pic 5: Password Reset Token in Response( Developer was high on grass that day)

{
“id”: 11077,
“token”: “4PjLzn7fyLU<Redacted>f1h1P2F”,
“stamp”: 1628796031082,
“username”: “test13337”
}

Due to some misconfiguration on the server-side, the Server leaks the token in response for any user who is requesting it for any valid existing username. But now the question is how we can use this disclosure of tokens to perform an Account Takeover of any user? so it’s pretty easy.

Get Aditya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Reset URL Format looks somewhat like :

https://www.company.com/#/changePassword/<username>/<token>

We are halfway there. Let’s craft a password Reset link here, as the response of the request leaks the “username” and “token” so all we have to do is to replace the values with the above-mentioned URL.

The Final reset token would be

https://www.company.com/#/changePassword/test13337/4PjLzn7fyLU<Redacted>f1h1P2F

Performing the above steps the attacker can successfully takeover any valid user’s account and perform any suspicious activities or can also Divert the payments to his crypto address which was a critical issue.

Pic 6: Scene at Desk of Developer on the same day. 😆

I immediately went ahead and reported this vulnerability and The team validated and triaged the issue within 10 minutes of my submission and I was rewarded with a huge $5000 bounty for this finding.

Press enter or click to view image in full size
Pic 7: Reward for Vulnerability
Tips:

Be creative and think out of the box, easy, isn’t it ;)

Timeline:

Issue found: Aug 16th, 2021 9:30 PM IST

Issue Reported: Aug 16th, 2021 10:00 PM IST

Issue Triaged: Aug 16th, 2021 10:10 PM IST (Quick tho)

Rewarded: Aug 16th, 2021 10:30 PM IST with $5000 Bounty

Fixed: Aug 17th, 2021 9:41 AM IST

It was really fun hunting on this program and I’ll be publishing more write-ups in the upcoming days so stay tuned.!

Hope you guys enjoyed it! and Feel free to reach me out on Twitter.

Until then take care, stay safe and keep grinding.

Cheers..!

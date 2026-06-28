---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-16_how-i-was-able-to-bypass-otp-code-requirement-in-razer-the-story-of-a-critical-b.md
original_filename: 2019-10-16_how-i-was-able-to-bypass-otp-code-requirement-in-razer-the-story-of-a-critical-b.md
title: How I was able to bypass OTP code requirement in Razer [The story of a critical
  bug]
category: documents
detected_topics:
- otp
- xss
- sqli
- command-injection
- mfa
- cors
tags:
- imported
- documents
- otp
- xss
- sqli
- command-injection
- mfa
- cors
language: en
raw_sha256: c88827441113a4393d6636f02eec0848fc6aee60874bec6be019b7d16d0d9c23
text_sha256: 372f90bbc205b15f5a97a7375b3b0c3a2b506ecbb6607184106461f7068084da
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to bypass OTP code requirement in Razer [The story of a critical bug]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-16_how-i-was-able-to-bypass-otp-code-requirement-in-razer-the-story-of-a-critical-b.md
- Source Type: markdown
- Detected Topics: otp, xss, sqli, command-injection, mfa, cors
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c88827441113a4393d6636f02eec0848fc6aee60874bec6be019b7d16d0d9c23`
- Text SHA256: `372f90bbc205b15f5a97a7375b3b0c3a2b506ecbb6607184106461f7068084da`


## Content

---
title: "How I was able to bypass OTP code requirement in Razer [The story of a critical bug]"
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-bypass-otp-token-requirement-in-razer-the-story-of-a-critical-bug-fc63a94ad572"
authors: ["Ananda Dhakal (@dhakal_ananda)"]
programs: ["Razer"]
bugs: ["OTP bypass"]
bounty: "1,000"
publication_date: "2019-10-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4985
scraped_via: "browseros"
---

# How I was able to bypass OTP code requirement in Razer [The story of a critical bug]

1

Top highlight

How I was able to bypass OTP code requirement in Razer [The story of a critical bug]
Ananda Dhakal
Follow
6 min read
·
Oct 16, 2019

1.3K

7

It’s @dhakal_ananda from Nepal and this is my first blog post. Without further ado, let’s move on to the bug already.

So the story is a long one. Before Razer became public in Hackerone, it was a private program as most of you know if you had seen at the time it was public and I was also invited to the private program. But I dunno why I didn’t hack in the program and just rejected the invitation. After some time, it became public and when I saw that, it caught my attention very much. I got very interested in the program and started hacking immediately.

Since I am more interested in bypassing security functionalities rather than searching for XSS and SQLi, I got into bypassing the OTP token because it got my attention in the first look.

Press enter or click to view image in full size

I fuzzed some times and found that the application was using a long token to validate whether the OTP code has been entered or not. The OTP token was only provided after entering the valid OTP code.

So what can we do to bypass the code?? I don’t know if that came to your hacker-mind but yeah, it’s using the attacker’s token to validate the victim’s token. I tried that method and it worked.

Here is how you could reproduce the issue:
Login to the attacker’s account
Go to https://razerid.razer.com/account and click on the email field
You will see a dialog saying that you need to enter an OTP code
Enter the valid code and intercept the request of changing the email
Send the request to repeater
Login to the victim’s account assuming that you have credentials of the victim
Intercept the request of changing the name
Copy the user_id and user_token and save it in a file
Paste the victim’s user_id and user_token in the field of the attacker’s user_id and user_token at the request that was sent to the repeater
Submit the request and see that the email address is added into the victim’s account without OTP token requirement
POST /api/emily/7/user-security/post HTTP/1.1
Host: razerid.razer.com
Connection: close
Content-Length: 260
Accept: application/json, text/plain, */*
Origin: https://razerid.razer.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
DNT: 1
Sec-Fetch-Mode: cors
Content-Type: application/json;charset=UTF-8
Sec-Fetch-Site: same-origin
Referer: https://razerid.razer.com/account/email
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: ...
{"data":"<COP><User><ID>user_id</ID><Token>user_token</Token><OTPToken>otp_token_value_here</OTPToken><login><email>attacker-email@example.com</email><method>add</method><primary>1</primary></login></User><ServiceCode>0060</ServiceCode></COP>"}

Note: This steps for reproduction is not the same as I submitted in the report. This is simplified and actual steps for reproduction with exploitable POC.

I did this because the application didn’t validate the cookies and other things. All it validated was user_id, user_token and OTP_token. But the OTP_token was only validated if it was a valid one. It was not validated if it is of the specific user. It means I could paste the attacker’s token in the victim’s request and bypass OTP validation for the victim account.

You know what?? The process didn’t end up smoothly. Here is the real story.

Get Ananda Dhakal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I submitted the report with steps for reproduction as below. The below steps for reproduction and the above steps for reproduction were the same at last. It's just that the below steps for reproduction is complicated and not understandable.

Press enter or click to view image in full size

Yes, you could follow those steps to reproduce to access the victim’s settings and it was also what I found at first. It is by changing the response and doing things and things and things but, from the above steps for reproduction, the team members thought that it would require physical access to the victim’s device/browser. I had fuzzed so much to get these final steps for reproduction but Hackerone triage team-member asked for more information regarding it saying something like this:

Press enter or click to view image in full size

I was like “what the hell?”

I am exactly doing that thing. I replied with some shitty thing that had no answer to this question if I see it now. After my reply, the member closed the report as Informative. I asked him to let the internal team evaluate the issue. The internal team member said that this was not a valid issue i.e he also didn’t clearly understand what I was trying to say. I asked him to open the issue so that I can self-close it because they didn’t seem to understand it at all. To be more clear, I also didn’t understand it as I do now. He then opened the report for me to self-close because it didn’t have a negative impact on my signal.

#BugBountyTip: Before you submit bug like this, make sure that you have clear steps for reproduction. Try to simplify the steps as much as you can. The bug that you can understand could not be understood by the team member and you could end up getting an N/A or Informative like I did at first.

I completely left the report and moved on. After 3 days of moving on, I went back to the report because I realized a thing. Most of the application asks you to enter the 2FA code at the time you login but it asked when I tried to change the sensitive information. So I commented in the report that I was bypassing the 2FA requirement so it must be a valid vulnerability.

Press enter or click to view image in full size

I got a reply after a day saying something like:

If you have a PoC where you have access only to the victim user’s Razer ID account and password and then can access or change profile information, it would be a valid report.

And I was like Challenge Accepted!!

The team member provided me the email address and password of a test account to change the email address. I changed the email address of that account without accessing the OTP token and removed the previous email. After doing that, I said that I had changed the email address and you could not access the account with previous email.

I with my brother and my cousin were together during this hack and we were really shouting after I completely exploited the bug early in the morning :P.

One day after that, he reopened the report and changed the status to Triaged with severity set as Critical. I was really happy since I was able to show a POC and exploit the vulnerability.

After 2 days, I thought I would do a writeup on this issue and save a video for it. But before I could create a video POC, it was fixed.

I was awarded a total of $1000 bounty for the issue. The bounty was $750 and the bonus was $250 for the very very long misunderstanding.

#BugBountyTip: Make sure you fuzz the parameters and use one user’s tokens in another user’s session. Sometimes, there could be token-validation but missing user-token validation.

After a few days of triage, I found another OTP bypass and it is already resolved. It was a really fast and efficient fix and the bounty is pending.

I hope you guys enjoyed this really long blog post. Feel free to send some feedback as I will really appreciate it. See you again in another writeup.

Hackerone profile: https://hackerone.com/dhakal_ananda

Twitter profile: https://twitter.com/dhakal_ananda

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

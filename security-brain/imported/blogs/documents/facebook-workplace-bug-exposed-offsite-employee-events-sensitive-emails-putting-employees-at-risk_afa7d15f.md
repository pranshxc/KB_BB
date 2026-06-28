---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-16_facebookworkplace-bug-exposed-offsite-employee-events-sensitive-emails-putting-e.md
original_filename: 2019-02-16_facebookworkplace-bug-exposed-offsite-employee-events-sensitive-emails-putting-e.md
title: Facebook/Workplace Bug Exposed Offsite Employee Events, Sensitive emails Putting
  Employees at Risk
category: documents
detected_topics:
- command-injection
- path-traversal
- password-reset
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- path-traversal
- password-reset
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: afa7d15f94477c92481e3692eab58342f5d359488a7fe24170d067f84c5f5eb5
text_sha256: 04704885f6548f124cdf97a7cbde494d866c9dc746a93c96c688afd953579657
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook/Workplace Bug Exposed Offsite Employee Events, Sensitive emails Putting Employees at Risk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-16_facebookworkplace-bug-exposed-offsite-employee-events-sensitive-emails-putting-e.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, password-reset, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `afa7d15f94477c92481e3692eab58342f5d359488a7fe24170d067f84c5f5eb5`
- Text SHA256: `04704885f6548f124cdf97a7cbde494d866c9dc746a93c96c688afd953579657`


## Content

---
title: "Facebook/Workplace Bug Exposed Offsite Employee Events, Sensitive emails Putting Employees at Risk"
url: "https://medium.com/@rohitcoder/facebook-workplace-bug-exposed-offsite-employee-events-sensitive-emails-putting-employees-at-risk-813d77a0c0ab"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2019-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5408
scraped_via: "browseros"
---

# Facebook/Workplace Bug Exposed Offsite Employee Events, Sensitive emails Putting Employees at Risk

Facebook/Workplace Bug Exposed Offsite Employee Events, Sensitive emails Putting Employees at Risk
Rohit kumar
Follow
5 min read
·
Feb 16, 2019

173

Hello Bug hunters! This blog post is about Facebook/Workplace security vulnerability. This bug could have exposed user’s sensitive email subjects. You all know what kind of notifications or messages Facebook sends you to your email inbox. The attacker was able to expose these all details with that specific bug.

Press enter or click to view image in full size
Image credits: Ask Buddie

These type of sensitive information was exposed to an attacker.

Press enter or click to view image in full size

Summary (For those who want to know exact bug and they don’t have time to read this long blog post)

Facebook was having a misconfigured feature -https://www.facebook.com/settings?tab=security&section=recent_emails&view this page contains a list of all emails which was sent by Facebook/Workplace to user. Facebook was just hiding this page from unverified users but the attacker was able to see this page directly by typing URL. An attacker was able to signup with unverified email (victim@gmail.com) and the attacker was able to see all future upcoming emails from Facebook on that page. Here an interesting point “Both, victim & attacker account will show list of all these emails. So, the attacker was able to see account activity of victim for long time”

Now, Those who want to read this report & reproduction steps in detail.
Affected product => Facebook and Facebook workplace

Usually, whenever we create a facebook account we need to verify it using OTP received on user’s email.

Now after verifying our email We are supposed to use a facebook feature known as “Check Recent emails”. But using this vulnerability we can expose lot of possible details of a facebook user or any Workplace organization user.

Note: Here we are able to expose details using only email’s subject which are available in fb accounts (Luckily most of the information can be fetched from email subject)

Impact
===
1. Business-related and page roles related notifications (which are not visible in fb notifications and are sent only to emails)
2. Sensitive activities
3. Mail sent by facebook to user’s email.

Repro steps

Setup
===
1. Think any logical email or ask email of any organisation’s important person like ceo@company.com or bill@microsoft.com

Steps for reproducing this on Facebook.com
===
1. Visit facebook signup page. Create 1 new account using any email say stevejobs@apple.com

2. Now stevejobs@apple.com will get otp for fb account verification but you are not having access to that email so you can’t verify it.

3. Now suppose apple’s business account manager invites stevejobs@apple.com for some business related stuff.

4. Now most of the business related activities which are done by that organisation for that specific email (stevejobs@apple.com) can be seen by any user without verifying email.

5. Sometimes facebook support team also contacts some user for any information (maybe bug bounty discussion) and if our email is not verified i can’’t visit facebook.com/support i will be directed to otp verification and i can’t see what fb support team is sending me and in notifications we can only se “We are having 1 message for you in dashboard”. But using this vulnerability we can also see these notifications.

6. You can check all these notifications or activities via this link https://www.facebook.com/settings?tab=security&section=recent_emails&view without verifying your otp.

Note: Usually you will get this link in settings>security & login>Recent emails from facebook (If your account is verified) otherwise fb will not show this link but you can enter this link directly in browser for checking all info.

Steps for reproducing this on workplace.facebook.com
===

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In workplace facebook i think we are not having any feature like this (even if your email is verified) but i think while creating workplace facebook most of the code are copied from facebook so you can also see these all info by directly visit this link https://workplace.facebook.com/settings?tab=security&section=recent_emails&view

Now, tricky conversation

Most of you know that my previous reported bug was closed as informative and then i convinced them to reopen my report and then i received an award of 3000$. So, here again, this report was closed then I again convinced them.

They replied

17 Nov 2018

Hi Rohit,

Thank you for sharing this information. Facebook allows the creation of accounts without full email verification. That is intended. Due to the sent email not being shown after the Victim verifies the account, this does not fully qualify for the bug bounty. The issue you are seeing about being able to login, is that Facebook recognizes that you are using an old email for the account and logs you. It may seem odd but is intended.

Although this issue does not qualify as a part of our bounty program we appreciate your report. We will follow up with you on any security bugs or with any further questions we may have.

Thanks,

Ed Kurson
Security

My Reply

Hi Ed,

Ok i understood and agree your point “Facebook allows the creation of accounts without full email verification”.

But this report was about disclosing user’s or any business manager’s activity for any specific person. This can expose sensitive details like page role details or business related details of that person.

I hope this is not intended feature that’s why Facebook is not showing the link of “ Check recent emails from Facebook” In security tab if email is not verified.

This report wasn’t about creating multiple accounts without email verification. It was about simply, a Misconfigured Facebook feature which is exploiting users privacy.

Please, think again the impact of this vulnerability in long run.

Then after a few months and conversations

Hi Rohit Kumar,

After reviewing this issue, we have decided to award you a bounty of $1000. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.

Singing up with an unconfirmed email would show all notifications previously sent to that email.

Hall of fame facebook.

I will come back again with a new vulnerability report in summer 2019. I am busy with my own startups and other stuffs. I look for bugs only in winter and summer holidays!

Thanks, have a good day ahead!

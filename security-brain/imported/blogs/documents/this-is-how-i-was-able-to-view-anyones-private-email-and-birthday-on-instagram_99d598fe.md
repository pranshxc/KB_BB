---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-20_this-is-how-i-was-able-to-view-anyones-private-email-and-birthday-on-instagram.md
original_filename: 2020-12-20_this-is-how-i-was-able-to-view-anyones-private-email-and-birthday-on-instagram.md
title: This is how I was able to view anyone’s private email and birthday on Instagram
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- business-logic
language: en
raw_sha256: 99d598fe63b0afe49b1b85d67b7ffec9f5418f00d086489d23de61f8e0bc4078
text_sha256: 68a7df2e3e63d2017a4ab91cdf9ae00b14ee0da7dccdcf5711c55e01a5ee44b7
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# This is how I was able to view anyone’s private email and birthday on Instagram

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-20_this-is-how-i-was-able-to-view-anyones-private-email-and-birthday-on-instagram.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `99d598fe63b0afe49b1b85d67b7ffec9f5418f00d086489d23de61f8e0bc4078`
- Text SHA256: `68a7df2e3e63d2017a4ab91cdf9ae00b14ee0da7dccdcf5711c55e01a5ee44b7`


## Content

---
title: "This is how I was able to view anyone’s private email and birthday on Instagram"
url: "https://saugatpokharel.medium.com/this-is-how-i-was-able-to-view-anyones-private-email-and-birthday-on-instagram-1469f44b842b"
authors: ["Saugat Pokharel (@saugatscript)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
bounty: "13,125"
publication_date: "2020-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4056
scraped_via: "browseros"
---

# This is how I was able to view anyone’s private email and birthday on Instagram

Saugat Pokharel
 highlighted

This is how I was able to view anyone’s private email and birthday on Instagram
Saugat Pokharel
Follow
5 min read
·
Dec 20, 2020

1K

3

Summary: I discovered that Facebook Business Suite was leaking private information about Instagram users from the page messaging section. With this bug, an attacker could get the personal email and birthday of any Instagram user just by messaging them.

Hi, I am Saugat from Kathmandu, Nepal. This is a write-up about a bug that I found recently on Facebook.

It was October 22, Thursday evening, I was looking for any security/privacy issues when I read that Facebook brought a new app called Facebook Business Suite.

What is a Business Suite?

Business Suite is an upgraded version of the page manager app (an app for managing Facebook Pages). In the business suite, business admin can link their Facebook page with their Instagram account. Then admin can create or schedule posts, view analytics, message, or reply to comments on both Instagram and Facebook using a single application. Business Suite can be accessed on the desktop at business.facebook.com.

I connected my own personal Instagram account with the Facebook Page through: Page Name>Settings>Instagram.

As I connected my own personal Instagram account to the page, now I could reply to my Instagram inbox through the business suite.

When I was replying to one friend, the email that I saw in the top right corner of Business Suite caught my attention. There was an email of her. I asked my friend whether she had the privacy of her email as public or not. She was unable to provide me with proper confirmation. So, I quickly googled about email privacy on Instagram.

Press enter or click to view image in full size
Email of an Instagram user being exposed through Business Suite

On the official help page of Instagram, it was clearly mentioned that email address is not visible to other users. I became 99% sure that it was a bug.

Press enter or click to view image in full size
It is written in Instagram help page that Email, phone number, and gender is always private.

Also, I went to my Instagram app >Edit Profile>Personal Information Settings. Even there, it was mentioned that email, phone number, gender and date of birth is never visible to other users. Then, I was like Yesssssss!

Press enter or click to view image in full size
The above information is supposed not to be viewable by others

When I opened a conversation window with another friend, I was able to view his email address as well. I wanted to try whether I can fetch the email address of a private user or not.

So, I created one test Instagram account and changed the privacy to private. Then, I wrote a message to that account from my Instagram account. Now, that message appeared in the Business suite and BINGO. I was able to view the email address of any private users.

I created another account and set the setting as: Only followers can send me messages. Now, I wrote a message to that user. As expected, the message was not sent but this opened a chat window in the business suite and the email of that account was also disclosed. I was shocked.

Get Saugat Pokharel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, I realized that I am able to disclose the primary email address of any Instagram user just by messaging them. Even the accounts that were set to private and accounts that were set to not accept DMs from the public were vulnerable to this attack. So, without any delay, I immediately wrote a report to Facebook with a detailed description and a video POC.

Also, I am in a workplace group where we can directly communicate with Security Engineers working on Facebook. So, I notified one of the security engineers to look into my report before it reaches any bad guy. The issue was then quickly triaged and fixed was deployed in less than 2 hours of the triage. In this way, the personal email disclosure issue got fixed.

After 8–9 hours of me noticing the patch, I received a message from the Security team saying the issue got fixed. I was asked to check whether the patch resolves the issue or not. And here comes another part:

Birthday Disclosure of any user:

When I was checking for the fix, I saw that birthday of one Instagram user was leaking from the same place. I was again shocked. I then wrote a reply saying my birthday is leaking from the same place. Facebook Engineer replied that they’ve already identified the birthday issue due to my initial report and they are working on a fix.

The next day, the birthday issue was also fixed. But, during my investigation what I found was: The birthday was leaking only for those users who manually signed up for Instagram. So, in this way: I was able to infer whether a user created an Instagram account through the Login with Facebook method or not. I believed this is another privacy concern.

If birthday disclosed = Manually signed up
If birthday not disclosed = Logged in with Facebook

Here is a video POC and explanation of the issue: https://youtu.be/YeopEVjjtPI

I was so eager to know about the bounty decision. I already knew it would be a very good bounty since the issue was highly critical in terms of user privacy.

After waiting patiently for 7 weeks, five digits bounty was issued by the Facebook. I became very much happy as it was the highest bounty reward in my entire lifetime.

Timeline of the report:

Initial report sent: October 22, 2020, 6:59 PM
Triaged: October 23, 2020
Email disclosure issue fixed: October 23, 2020
Birthday disclosure issue fixed: October 28, 2020
Rewarded: December 16, 2020

Press enter or click to view image in full size

Thank you for taking time to read my article. Have a great day!

You can follow me on Facebook or Twitter if you would like to stay connected with me.

Below is the coverage from the press regarding this issue.

A Facebook bug exposed Instagram users' personal email addresses and birthdays
When signing up for an Instagram account, the service promises that your email and birthday won't be publicly visible…

www.theverge.com

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-27_story-about-stop-10000-users-to-get-their-job-notification.md
original_filename: 2021-02-27_story-about-stop-10000-users-to-get-their-job-notification.md
title: Story About Stop 10000+ users to get Their job notification
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 3b3156cd98eafc6493767f87b16561c80e166b430c8fdbecd7308d023e880044
text_sha256: 8bf3dca025a134516db6d84295af96e3b7968da38db579968a46281ab146ab11
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Story About Stop 10000+ users to get Their job notification

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-27_story-about-stop-10000-users-to-get-their-job-notification.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `3b3156cd98eafc6493767f87b16561c80e166b430c8fdbecd7308d023e880044`
- Text SHA256: `8bf3dca025a134516db6d84295af96e3b7968da38db579968a46281ab146ab11`


## Content

---
title: "Story About Stop 10000+ users to get Their job notification"
url: "https://pallabjyoti218.medium.com/story-about-stop-10000-users-to-get-their-job-notification-6a8aca542c85"
authors: ["PJBorah"]
bugs: ["Logic flaw"]
publication_date: "2021-02-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3861
scraped_via: "browseros"
---

# Story About Stop 10000+ users to get Their job notification

Story About Stop 10000+ users to get Their job notification
PJBorah
Follow
3 min read
·
Feb 26, 2021

17

Greeting Everyone ! Hope Everything Is going good ! This Story Is about to How I able to Stop all Users of example.com to get their Subscribed Job Notification . in my hunting Period I encountered Interesting Bug Which allow me to Stop All 10000+ users to Get their Job Notification Update .

As I was testing on example.com and I am able to Encountered Same issue on their subdomain too.

The Story about My recent Finding Now begin !

As I was testing on example.com and this has functionality that we can Update Job basically site Is a Job seeker platform so Whenever You will update Your Specific Job this will send a Confirmation mail to your Registered Inbox with Secret Token That whenever You want to remove Your Job Update you need to browse That mail which has private token and you able to access your Job Update dashboard it includes all Job updates that user subscribed for it.

Now How attack scenario lets start ?

As I already Told You site is about job seeker now I simply Created an account (Victim Account) after I update for Job Notification with Your some specific job After I update it send me some Private token that whenever I want to cancel my job notification then I need to go through that private Token and it also includes all previously Update job notification detail details.

Then I forgot to check response body of Previous Update Request and One thing come to my mind yes I need to check response body again i

Get PJBorah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Request with some another job category and update job j notification and I look for It source code using burp ! Boom It leaking Token ,

Then I create another account { Attacker Account} On example.com and I update for Job Notification And using burp I intercept the Request And change Attacker Mail To Victim email And right click + Do intercept + Request to this host And I simply Look for Token and then I browse that Link which carries token

Boom ! I am able to access victim Job Notification Portal which victim also has older victim job notification and Now I can simply stop Victim and all 10000+ user to get their Job Notification ,

Sorry For My Explanation ! This is all About My finding!

And Then I reported

Rewarded $$$

My Linkedin: Pallab Jyoti Borah

Byeee!

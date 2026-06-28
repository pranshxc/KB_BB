---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-04_this-is-how-i-managed-to-win-2000-through-facebook-bug-bounty.md
original_filename: 2019-07-04_this-is-how-i-managed-to-win-2000-through-facebook-bug-bounty.md
title: This is how I managed to win $2000 through Facebook Bug Bounty
category: documents
detected_topics:
- command-injection
- path-traversal
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: cc8e14bd54e4bbc0aa664d421916f2754383f19570b0f5b75ae2f884974b3855
text_sha256: a4bfb14ec9c2929f3ce2428a7883c597d4de4c8d3cd74062abdbe50f402a9d95
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# This is how I managed to win $2000 through Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-04_this-is-how-i-managed-to-win-2000-through-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `cc8e14bd54e4bbc0aa664d421916f2754383f19570b0f5b75ae2f884974b3855`
- Text SHA256: `a4bfb14ec9c2929f3ce2428a7883c597d4de4c8d3cd74062abdbe50f402a9d95`


## Content

---
title: "This is how I managed to win $2000 through Facebook Bug Bounty"
url: "https://medium.com/@saugatpokharel/this-is-how-i-managed-to-win-2000-through-facebook-bug-bounty-a7d531d5097e"
authors: ["Saugat Pokharel (@saugatscript)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "2,000"
publication_date: "2019-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5165
scraped_via: "browseros"
---

# This is how I managed to win $2000 through Facebook Bug Bounty

This is how I managed to win $2000 through Facebook Bug Bounty
Saugat Pokharel
Follow
6 min read
·
Jul 4, 2019

385

1

Disclaimer: This is the my first bug report on Facebook. At the time, when I was submitting this report, I had no idea about bug bounty. So, no any technical terms are used in this report.

I am Saugat Pokharel from Kathmandu, Nepal. Today I am going to write up on how I managed to receive a reward of $2000 through Facebook bug bounty.

Let me elaborate in detail.

I am an admin of the Facebook page Students of Nepal. The page mainly focuses and brings out the educational information as well as ongoing recent topics of our country Nepal.

It was June 24, Monday evening. There were news floating around Facebook that Biplop Maoist, a recently banned political party has announced Educational strike the next following day demanding the release of their party members from police custody. There was no clue either the news was actually true or not. But, many of the school/colleges had already decided not to take the risk and made a public announcement of holiday due to strike.

The message box of the page was flooded with the query either it was holiday due to strike on the next day or not. I replied to all of them, ‘Please ask your college and get confirmed.’

I was replying the queries that were asked in the page, I suddenly saw exactly same queries asked at the same time. They were three girls from St. Xavier’s School, Godavari.

All of them asked, “Is there any possibility of holiday tomorrow?”

“Please kindly contact your college administration.” I replied.

They said, “Do you think our college will provide us holiday?”

“Most probably” I replied.

Again they replied “Hope so.”

Every time their reply and timing was exactly same. I was quite shocked and I asked them the reason for replying the same message at the same time.

“Unemployment” jokingly they said.

Conversation in page goes like this.
The term ‘Berojgarr’ is a Nepalese word for unemployment which they said jokingly.

Then I replied, “ Please visit merojob.com or other job seeking sites for better job opportunities.” This was a funny reply as well. I wrote the message for the first person and copied the same text for rest two others.

I was replying through page manager app, an official Facebook app for managing Facebook pages. I was waiting for their reply to see what they will say. To my surprise, strange thing happened. My latest message was sent through my personal profile. How can this be possible ? I was really shocked and worried.

The message which was sent through my personal ID when replying through page manager app.

I wrote a apology letter to three of them saying that I had no intention to communicate with them through my personal profile. I didn’t even knew how that happened. Replying through page and all of a sudden, the message was sent through my personal profile. Isn’t that so ridiculous? I was so frustrated and anxious at that moment but they responded very calmly saying “It’s okay, nothing to worry about.” Their response gave me a little bump, still I thought that I should report this issue seriously on Facebook.

I realized that whenever I reply the followers of the page with the link (URL) attached, the message was sent through my personal account. Then immediately, I wrote to the Facebook support with the following message:

Description:

I am an admin of a page “Students of Nepal” (fb.com/studentofnepal)”. We perform occasional interactions with visitors and followers of the page there. Today, I was responding the messages in the page through page manager app. I was replying people with same copied messages as the query was exactly similar. Then strange thing happened suddenly, the messages I was sending through the page manager was sent through my personal profile in the same window which can be seen in screenshot below.

What have actually happened?

When I reply with no links, the message is sent through page.
But when I reply with external website link (in my case: its merojob.com), it is sent through personal profile.

I checked through another phone, the message didn’t appear there. And I confirmed that it was sent through my personal profile while responding to people through page manager.

I never checked their profile, yet the message was sent through my personal ID through page manager.

Impact:

This can have serious impact with the life of admin as it is not good to reply people unknowingly which can create thought conflict among followers. This can also cause bad reputation of the page due to the Facebook bug.

Steps to recreate bug:

Go to page manager.
Go to inbox.
Reply any message with no links it works fine.
But when if you have links, it replies from admins personal profile.

Device I use: Apple I-pad Pro 11 inch 2018 version

Operating System: IOS 12.3.4

(I included a screenshot of the bug as well.)

Get Saugat Pokharel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On June 25, I got the following reply from Facebook.

Hi Saugat,

Thank you for your report. I attempted to re-create the issue but was unable to using multiple links (including google and merojob). Is this a one time issue or something that is occurring on a regular basis? If it happens regularly would you be able to take a video of the process so we can see exactly what is happening?

Thanks,

Juana

Security Analyst

In the same day, along with the video recording of the bug, I wrote:

Sure, here is the video where I can reproduce the issue. When I send normal text like hello, it is replied through page but when I paste the message with link (URL), it is replied from my personal profile. This is seriously causing issue replying the followers of the page.

Video link: https://youtu.be/LpCqaHqEdXU

I got reply from Facebook the next day as follows:

Hi Saugat,

Thank you for your submission and further information. We’ve managed to reproduce your report and will get back to you once we have had a chance to investigate.

Thanks,

Juana

Security Analyst

Again on June 27, I got the message from Facebook with the message

Hi Saugat,

Thank you for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress.

Thanks,

Joel

Security

I replied them “okay”.

On June 28, I got reply with the following text.

Hi Saugat,

We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.

Thanks,

Neal

Security

I replied them mentioning that the vulnerability has been patched and the issue has been fixed.

Finally on July 3, Morning when I just woke up, I saw a message from Facebook in the support inbox. I was quite sure that it was related to the issue that I had reported few days back.

The following message was written.

Hi Saugat Pokharel,

After reviewing this issue, we have decided to award you a bounty of $2000. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.

Replying to messages with links lead to page admin disclosure

Thank you again for your report. We look forward to receiving more reports from you in the future!

Press enter or click to view image in full size
Message from Facebook with the bounty reward

I was so happy and excited to read that official message from Facebook. Actually, that was the highest amount of cash reward which I had ever received in my entire life. I never expected that I would receive $2000 bounty just for a simple bug report.

I am really thankful to the team members of our admin panel of the page. Very special thanks goes out to those three amazing girls: Pramita, Swasti and Subi ! May god bless you all.

Thank you for taking the time to read my article. Have a great day!

You can follow me on Facebook or Twitter if you would like to stay connected with me.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-18_hacked-google-meet.md
original_filename: 2021-12-18_hacked-google-meet.md
title: Hacked Google-Meet…??!
category: documents
detected_topics:
- automation-abuse
- sso
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- automation-abuse
- sso
- access-control
- command-injection
- api-security
language: en
raw_sha256: 3e0e92dfc13fab51b96ec38899f5da78ae3d69480cbb36f9582386f3b72e619a
text_sha256: bcf897a93ed7aa8d9c553381bddd910e15c2dcbb54416fa2eab9f1a7e1bcdc5b
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Hacked Google-Meet…??!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-18_hacked-google-meet.md
- Source Type: markdown
- Detected Topics: automation-abuse, sso, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `3e0e92dfc13fab51b96ec38899f5da78ae3d69480cbb36f9582386f3b72e619a`
- Text SHA256: `bcf897a93ed7aa8d9c553381bddd910e15c2dcbb54416fa2eab9f1a7e1bcdc5b`


## Content

---
title: "Hacked Google-Meet…??!"
url: "https://infosecwriteups.com/hacked-google-meet-40f364bb8368"
authors: ["7𝖍3𝖍4𝖈kv157 (@7h3h4ckv157)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2021-12-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3081
scraped_via: "browseros"
---

# Hacked Google-Meet…??!

Hacked Google-Meet…??!
7h3h4ckv157
Follow
7 min read
·
Dec 18, 2021

816

3

15th June 2021
Press enter or click to view image in full size
Let’s bounce back a few months :)

Hello, infosec community ✋
Today I’m here to reveal an occurrence in my life which happened in June 2021. If you’re a complete beginner, leet, or off folk in infosec, whatever, it doesn’t matter. This write-up is for every individual who has a vigorous appetite for reading. I have to consider my buddies who were out of this domain. So it’s imperative to cover essentials for way better understanding.

Important:

1. It’s not approximately bringing down Google’s server or compromising google-meet all over within the globe. But trust me, it’ll be worth your time. I’m talking about a cool authorization bug that existed in google-meet.

2. Don’t skip, if you are a 1337 like me (with small arrogance) you can skip the nuts and bolts merely know.

3. You can finalize the opinion by DM me (Twitter), but make sure you don’t miss each scenario that I conveyed.

At first, let’s talk about the basics
Press enter or click to view image in full size
What is CAPTCHA?

CAPTCHA →Completely Automated Public Turing test to tell Computers and Humans Apart

The CAPTCHA helps websites that wanna confirm whether the client isn’t a robot. The test helps distinguish genuine humans and computer programs (Bots). The test has two parts- a randomly produced arrangement of letters or numbers that show up as the misshaped picture, a content box and sometimes, images are provided to let you choose the correct one. To pass the test and demonstrate your human character, sort the characters you see within the picture into the content box. Or tap the comparing pictures which inquired.

Thus, CAPTCHA prevents any spam or bots from entering your site.

Q) Does Google-Meet use CAPTCHA? How did I glimpse that?

In the past year, during the pandemic, all the classes were online & I was sluggish to join every class (I’m comprehensively not an academic kid). My friend Mahshooq Zubair (@mq_xz_), a community member, publicized a story that shows the simple program for entering each class on google-meet & marking the attendance. Yeah, Completely by automation!!

(Presently, there’s no CAPTCHA).

Selenium is an open-source tool that automates web browsers which provides a single interface that lets you write test scripts in programming languages like Ruby, Java, NodeJS, PHP, Perl, Python, and C#, among others. Selenium Python bindings provide a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver intuitively. ←(Copied).

You can refer on the internet, there’re plenty of resources available about this.

Example:

watch this
So the question is, why does it matter?

I’ll elaborate. If you’re presenting a screen on google meet, probably the count will increase on the meet.

So if there’s N number of users in the meeting, when you start the presentation it’ll become n+1. Just like I have shown below.

Both are me
Host/User
Host/User presenting

Note:
While presenting, even if you are the host or user, it’ll happen. The count n to n+1 ensues anyways.

Idea behind the exploitation
Press enter or click to view image in full size

So we affirmed that when screen presentation, the count of individuals within the Google-Meet will increment — N to N+1 (same client twice).

Get 7h3h4ckv157’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Google says: Anyone with a Google Account can create an online meeting with up to 100 participants *60 minutes per meeting.
Businesses, schools, and other organizations can take advantage of advanced features, including meetings with up to 250 internal or external participants and live streaming to up to 100,000 viewers within a domain.

What if I told you that it was conceivable to fill the whole meeting employing a single account by automating ??! Definitely, you can fill the whole meet by utilizing your single account, then present your screen, & can make it N*2 !!

PoC that uploaded in my drive (which I showed to google) ↓↓↓

Note: I didn’t fill up the entire meeting! (but I can)
Just a PoC for presenting the report to google.

Exploitation / Reproduction Steps
1. Use your Gmail for creating an account
2. Login to the meet (online class, job meeting, or whatever)
3. Fill the meet by your account (use automation) : CAPTCHA 404
It can be done manually. Open the Tabs & join the same meeting. You will see the count increasing
4. Start screen presentation & turn On your mic
5. Boom

The moment you fill the meet by using a single account by automation, It’ll be like the bees on honeycomb.

Meet filled by your account

If there are N accounts of yours, start the presentation & make N*2 !! That moment itself the meet fall into the loop. You’re showing your screen, the other shadow of yours interior the meet has your screen, the reflect of circles will emerge and it’ll fall onto the infinite loop!

Press enter or click to view image in full size
~

It’s just a matter of turning on your mic. Boom !!! The entire meeting is done.

Job done
Note: 
Even if the admin "kicked/blocked" that account from the meet, that one gets influenced & still, the remaining exist without any issue.
Case:
An attacker logged 50 accounts by automating & the admin kicked/blocked him, then "only one" gets restricted. The remaining 49 accounts of that aggressor exist within the meet & can perform any action without further issues. So there aren't any options to wipe out the abuse by the admin. 

I detailed google about my finding. And they triaged my report.

Press enter or click to view image in full size
Triaged

But the inside team made me puzzled. We can assume it as Reply X (Important)

Press enter or click to view image in full size
WTF

They’re pointing to the authentication and neglecting my report. But what about authorization?

Authentication vs Authorization
Don’t skip

Authentication is the method of recognizing a user’s
identity. Distinctive systems may require diverse sorts of credentials to discover a user’s character.

Here the meet admin (Host) determines who can join the meeting. I respect their psychological / Technical pointing towards authentication.

Now let’s talk about Authorization (My turn)

Authorization is the process of giving someone permission to do or have something. It is a security mechanism to determine access levels or user/client privileges related to system resources.

My point is, the host can’t control the automation attack carried out by a client. The exploit script can surge the meeting with a single account replicating like a virus. The attacker can bring down the entire meet by running the simple exploit script. There’s no way to trigger any controls on the attacker’s mic & screen presentations. The infinite loops gradually lead to an explosion when the mic turns up.

I ping them to review my report. And their reply made me sick. We can assume it as Reply Y (Important)

Press enter or click to view image in full size
WTF

You can compare their Reply X & Y At first, they pointed the authentication & rejects, and whereas they understand the authorization issues they said they’re mindful of the situation.

Cool..!!
The Current state:

They successfully patched the issue that I detailed.

Make sense, right?
Conclusion

Beyond any suspicion, I can declare that it was a valid bug & abuse risk. Still, I respect the decision of google. Because nothing else I can do. I dunno what you’re thinking about. If you still questioning your mind whether it’s an issue/not, then just think about the fix carried out by Google.

Although, it’s not an end. It’s a fair starting of the career. My best is yet to come! I trust you appreciate this write-up. And do not disregard to put through with me on Twitter @•7h3h4ckv157

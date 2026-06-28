---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-30_how-i-hacked-a-website-integrated-w-facebook-having-11-mil-users-under-45-second.md
original_filename: 2019-01-30_how-i-hacked-a-website-integrated-w-facebook-having-11-mil-users-under-45-second.md
title: How I hacked a website integrated w/ Facebook having 1.1 mil. users under 45
  seconds.
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 317afc9c48c419c4156ca4778a4c46dad7b10827460da5d57051920b107a1a67
text_sha256: 35528802a54b62faa9c85eefe2283ad2163294c430a558cb2228e05d7bd8a0aa
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked a website integrated w/ Facebook having 1.1 mil. users under 45 seconds.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-30_how-i-hacked-a-website-integrated-w-facebook-having-11-mil-users-under-45-second.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `317afc9c48c419c4156ca4778a4c46dad7b10827460da5d57051920b107a1a67`
- Text SHA256: `35528802a54b62faa9c85eefe2283ad2163294c430a558cb2228e05d7bd8a0aa`


## Content

---
title: "How I hacked a website integrated w/ Facebook having 1.1 mil. users under 45 seconds."
url: "https://medium.com/@0x48piraj/how-i-hacked-a-website-integrated-w-facebook-having-1-1-mil-users-under-45-seconds-e4adcfe8ccd6"
authors: ["Piyush Raj (@0x48piraj)"]
programs: ["WeeQuizz"]
bugs: ["Information disclosure"]
publication_date: "2019-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5440
scraped_via: "browseros"
---

# How I hacked a website integrated w/ Facebook having 1.1 mil. users under 45 seconds.

How I hacked a website integrated w/ Facebook having 1.1 mil. users under 45 seconds.
How a 17 year old hacked 1.1 million people’s mind, leaving an active hack, which is not yet fixed!
Piyush Raj ~ Rex
Follow
7 min read
·
Jan 30, 2019

570

5

Press enter or click to view image in full size

F
or a long time I was thinking about publishing this work on the web. However, after not getting any response from weequiz after reporting several times what I’d done, I decided to publish what happened in .. May,
LAST YEAR. 2017. (procrastination? maybe.)

Sweet Note : These bugs are still active. Enjoy roaming to what I call, “The Candy Land”.

Fairy Tale
Press enter or click to view image in full size

I got intrigued when an app named en.weequizz.com became viral.

All of my friends started playing it.
And as the name says, it creates random, user made personal quizzes and all your Facebook circle can answer the questions.
I got excited too, played the quizzes, and failed. *actually came 2nd, 3rd*

But I wanted to come first in all the quizzes!

Not a good reason, Piyush.

Okay, ..

Brownie Point — This application has over 1.1 million likes. (This stat was enough to get me started)

For serious cyber security enthusiasts, I will soon publish a whitepaper focusing on only technical side, just in case you don’t want to see my bad meme selections.

Technical background and Reconnaissance corner *boring*

So, I started playing around, testing the website to find out how it works.
Only in around ~1 hour, I was able to figure out some pretty interesting high impact flaws.

At that time, I was like …

Chapter 0 : Something is awry

After a quick look, I started inspecting the code. For this purpose I used Chrome Inspection Tool (Ctrl+Shift+I).
The structuring of the ‘Question and Option IDs’ attracted my attention. Something is awry.

Press enter or click to view image in full size
Initial Inspection

Let’s take a closer look :

Press enter or click to view image in full size
view-source: en.weequizz.com | Highlighted Question 1

What conclusions can we draw here ? Let’s see :

Questions comes loaded beforehand and are not dynamic in nature.

Once the Quiz ID loads (ex. etswuypxf), the server sends all the questions, respective options to the client side at once.
There is an interesting onclick=”cAnswer(…)” parameter.
( super interesting actually)
Chapter 1: Digging the rabbit hole

In no time I broke their ridiculous algorithm. *literally under 45 seconds!*
Let’s dig the hole and find out what they were made of!

Let’s take a closer look at their cAnswer(…)

Press enter or click to view image in full size
Question with Options

Their custom-made function cAnswer contains the structure like :
cAnswer(1, 10, ‘b2b8x’, ‘p6lg8’, ‘exy5s’, ‘etsyuypdf’, ‘n08t3’, true)”

Obviously, the first sub-parameter which in this case is “1” seems to be the Question ID in the class named ”m_question_q_list” and indeed it is.

The first, second and the last sub-parameter are “1”, “10” and “true” respectively. *useless constraints for us*

Now comes the interesting part, the variables :

cAnswer(1, 10, 'b2b8x', 'p6lg8', 'exy5s', 'etsyuypdf', 'n08t3', true)
cAnswer(1, 10, 'b2b8x', 'p6lg8', 'z3jpz', 'etsyuypdf', 'n08t3', true)
cAnswer(1, 10, 'b2b8x', 'p6lg8', 'n08t3', 'etsyuypdf', 'n08t3', true)
cAnswer(1, 10, 'b2b8x', 'p6lg8', 'rxmj5', 'etsyuypdf', 'n08t3', true)

You saw, what I just saw? No?
Okay, let’s do again!

cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘exy5s’, ‘same’, ‘same’, bullsh**t)
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘z3jpz’, ‘same’, ‘same’, bullsh**t)
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘n08t3’, ‘same’, ‘same’, bullsh**t)
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘rxmj5’, ‘same’, ‘same’, bullsh**t)

This is even better, right ? :3
Got something this time? Again? Okay!

cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘exy5s’, ‘same’, ‘n08t3’, bullsh**t)
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘z3jpz’, ‘same’, ‘n08t3’, bullsh**t)
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘n08t3’, ‘same’, ‘n08t3’, bullsh**t)←
cAnswer(bulls**t, bulls**t, ‘same’, ‘same’, ‘rxmj5’, ‘same’, ‘n08t3’, bullsh**t)

Press enter or click to view image in full size
Jackpot!

Yep, that’s it. Don’t you believe me?
I have something sweet for you —

Bugs and Exploits Corner : *’Yay!’ Zone*
Manual Exploitation of the Wee Quizz Algorithm :
Voila!

You just nailed the quiz of an unknown person, Enjoy!

#1 Exploit : Tangled List Bug
Press enter or click to view image in full size

As of now, you all know how ridiculously they implemented the algorithm and how badly they are treating sensitive data.

Get Piyush Raj ~ Rex’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, you all can follow the above exploit method to “Hack your crush’s quiz and make him or her your bae!”

But Wait !!

Are you seriously going to do all of that?
Why to put your precious-precious eyes in immense pain?

Let’s Automate!

We are hackers, we are coders, programmers .. and Automaters?

What?, I love Iron Man!! ❤
Boom!

*I just moved closer in making my future girlfriend, a real girlfriend*

We are done!
What? You guys want a github repository with all the code ?
Sorry guys, I can only give this to you —

Code of the Exploit Sandwitch

Yes, It’s blurred, I know.

It’s merely 22 lines of code!
and that too when I’m being a good boy. *code formatting*
I can give you a hint or say, a piece of advice, which is —

→ Take care of the time delays, loading of DOM Objects when clicking the target object :)

I learnt Javascript, by getting intrigued with ‘chrome extensions’, I learnt how to build, package, debug one, and many a things in the process of building Connect-Me which is now a core-project of FOSSASIA.

I actually learnt much more things about Javascript while trying to automate this, and, I think you will too.

Takeaway?

Just <code>

I’ll love if anyone can build a chrome extension for this exploit, or discover new methods to exploit this website.
I’ve more ideas to exploit, you can tweet me.
Just be sure to ping me up, I’ll love to share your findings.

Happy Hunting!

#2 Bug : W.T.F. Bug! *for the lazy ones*

After looking through it’s Workflow and HTTP Responses,
Another obvious evil plan came to my *empty* mind.

It involves just three easy steps.

Step One : Generate a Quiz ID, load the quiz in your browser.

Step Two : Kill transmission (Cut the LAN Cable, Break your WiFi Router?) and then, start clicking randomly (obviously on options.)

Step Two 1/2 : Write down or remember the answers.
(if you have god-given photographic memory)

Step Three : Connect transmission and do the quiz again.

*This time you have all the answers needed to impress your crush*
and let the weequizz’s server to acknowledge the transaction, and complete the process.

Final chapter: The Aftermath

I was brought up a law-abiding citizen. Ethics are embedded.
(so I hack ethically, .. yeah, I know that’s boring.)

I decided to write a mail to WeeQuizz to caution them about the bug.

Now what?

1,2,3….7 days i.e. one week was over and there was no response, maybe they were busy handling more quizzes.

After 4 weeks, I sent a remainder mail saying that “it’s fine if you guys aren’t interested in improving your system.”

I haven’t heard anything from them since I hit the “send” button.

As my bug is not catastrophic enough to drastically hurt them other than destroying the very purpose of making quizzes, I decided to publish after waiting for almost three years.

Bottom line 1/2

Our target en.weequiz.com was handling the sensitive data (quiz answers in this case) on client’s side, and we all know that, handling sensitive data on client’s side is not good for health.

Bottom line *the other 1/2*

Don’t trust if someone scores perfect in your personal online quizzes.

About the Author

Piyush Raj is now a 18 year old crazy kid who is hacker in night and developer after midnight. (you guessed it, he has insomnia)

You can connect with him over LinkedIn, Twitter, Instagram.

Social Jazz.

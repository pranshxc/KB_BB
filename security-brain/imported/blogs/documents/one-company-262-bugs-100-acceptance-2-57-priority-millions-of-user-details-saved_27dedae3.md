---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-25_one-company-262-bugs-100-acceptance-257-priority-millions-of-user-details-saved.md
original_filename: 2017-02-25_one-company-262-bugs-100-acceptance-257-priority-millions-of-user-details-saved.md
title: 'One company: 262 bugs, 100% acceptance, 2.57 priority, millions of user details
  saved.'
category: documents
detected_topics:
- xss
- automation-abuse
- idor
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- automation-abuse
- idor
- command-injection
- otp
- csrf
language: en
raw_sha256: 27dedae357a04f1bc173a439802fe2ad547c636bd027c02a76c09910bf349344
text_sha256: 52fb071638f1b76ab0d316c05f487d0269e812377bb6f5fab7ce1294593f8dd9
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# One company: 262 bugs, 100% acceptance, 2.57 priority, millions of user details saved.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-25_one-company-262-bugs-100-acceptance-257-priority-millions-of-user-details-saved.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, idor, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `27dedae357a04f1bc173a439802fe2ad547c636bd027c02a76c09910bf349344`
- Text SHA256: `52fb071638f1b76ab0d316c05f487d0269e812377bb6f5fab7ce1294593f8dd9`


## Content

---
title: "One company: 262 bugs, 100% acceptance, 2.57 priority, millions of user details saved."
url: "https://medium.com/@sean.roesner/one-company-262-bugs-100-acceptance-2-57-priority-300million-user-details-saved-dd88ecb10f6f"
authors: ["Zseano (@zseano)"]
bugs: ["Stored XSS", "Blind XSS", "CSRF", "Account takeover", "IDOR"]
publication_date: "2017-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6217
scraped_via: "browseros"
---

# One company: 262 bugs, 100% acceptance, 2.57 priority, millions of user details saved.

Top highlight

One company: 262 bugs, 100% acceptance, 2.57 priority, millions of user details saved.
Sean
Follow
5 min read
·
Feb 25, 2017

648

3

Press enter or click to view image in full size

Welcome all! Firstly, let me introduce myself. I’m known as @zseano and i’m known for being mostly active on BugCrowd. One thing most people don’t know is that all of my bug bounty time is dedicated to one company. That’s right, 99.9% of my bugs have been to one company in the hope I am securing them from the bad guys and helping them learn security. Ive really enjoyed getting to know some of their security team, as well as getting an understanding as to how they work. (perfect for when discovering vulns, seriously! :D)

I’ve risen in the ranks and i’m currently ranked #6, although I have quite a few bugs in the NEW state so hoping to hit #2 soon. The top 10 is very active, and you quickly go up and down the ranks. (bugcrowd analysts: pls validate all my new bugs :P). In my time of reporting I have received great feedback from this program.

Even though their payouts aren’t anywhere near $xx,xxx for criticals I still really enjoy running in their bounty program. I also like to think my reports are helping their devs think before pushing vuln code (bad for me as no bugs, but good for them). I’ll revisit this post in a year and see how many new bugs I find. ;)

Get Sean’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With all that out of the way, it’s time to recap the last 6months of reporting bugs and to tally up just how much data i’ve saved from criminal hands and outline some interesting facts..

8 IDOR which resulted in me being able to gain access to MILLIONS of users’ personals details. (Saved you some work Troy Hunt!) This ranged from emails, phone numbers, sessions, and even plaintext passwords. My latest IDOR finding allowed me to input ANY users “id” and it would auto log me into their account.
19 IDOR which allowed me to modify users content. For example users’ photos, comments, or bio. These types of IDOR did not leak any personal data as such, they simply allowed me to manipulate and change it. A rough figure of how much data I could of manipulated: millions.
62 Stored XSS. A lot of my stored xss was discovered in sensitive areas, and by sensitive areas I mean areas of a website that a mod/admin would visit (and did infact on one of my tests) and I could potentially hijack their session, phish them, etc. I like to show a company that XSS isn’t just “woah you can pop 0”. For example whilst playing around with stored xss it actually fired on the admin backend accidently. Double win.
8 account takeovers via mis-configured facebook applications chained with open url redirects. Not only this, but we could of quite easily stolen users’ facebook access tokens as well. I released a blog post on this and I highly recommend taking my advice and trying it on sites. Turn those open url redirects into $bounties$!
Too many CSRF. I rarely report CSRF unless the action has some sort of impact (such as updating their email), but one noteable experience is worth going into more detail about which should help you when researching. One website had CSRF tokens etc on every post, but if you simply removed the token, it would reflect the changes you wanted to make but display an error, “invalid csrf token”. Since they reflected the changes I want to make (imagine i’m updating your email) and they also didn’t have X-FRAME-OPTIONS:SAMEORIGIN this created a perfect opportunity to take over users’ accounts via clickjack. This issue was site-wide. Even if a site has csrf tokens, I highly recommend playing with it more to see what you can do.. you’d be surprised.

What i’ve learnt

Mobile apps are usually always vulnerable. I’ve outlined this again in my blog post, but i’ll stress it here again: mobile apps are usually always vulnerable to IDOR! Due to poor design, they normally just ping example.com/api/user/1, and changing 1 to any id you want will reveal that users data (and sometines in my case, their sessiontoken which allowed me into their account).
Scrape data from everywhere. Look in all js files, look on waybackmachine for old files (especially robots.txt) that aren’t on their current site, but are still on the server. Look on shodan, crt.sh, dnsdumpster, google dorking etc. Meeting the extremely talented Nathaniel Wakelam (@nnwakelam) and seeing how much of a recon god he is made me step my game up with scraping.
Check for use of third-party apps. If they have a FB app chances are it’s mis-configured to allow for *.theirsite.com/*. Go get that open url redirect and achieve account takeover.
Inject blind XSS everywhere you can, and use XSSHunter to do this. I had the privledge of meeting @IAmMandatory (and even hacking next to him) and his service is amazing for blind XSS. If you use it, give him a little thanks and donate, after all, he gives us access for free.
Be professional. If you don’t agree with a payout or a decision, explain why. I’ll admit sometimes I have been hasty, but we all have bad days right? From my experience being professional and showing them you’re taking their program seriously will get you further.
Read. Read. Read. HackerOne disclosures, blog posts, even just random tweets. Find as much reading material as possible and see what everyone else is doing, then apply that knowledge to the program you’re working on. Who knows, one day that RCE might appear when you least expect it.
Note down vulnerable params somewhere. Companies like to re-use code so perhaps that reflective XSS you got on one endpoint might be vulnerable on another. Moar bounties pls sir.
Have fun. Doing security research isn’t all about the money, it’s about having fun. Enjoy what you do, and the bugs will follow. Get involved with people, share some cool bugs (if you’re allowed) and help others where you can. We’re a community, and as HackerOne says: Together we hit harder.

And my last peice of advice: Set yourself a goal. Don’t just go running into a site blindly not knowing what your actual aim is. Think in your head, “what is this company about?”, “what do they care about most?”, and work towards it. For example, I like to go for the critical bugs first.. and if I stumple upon smaller bugs (such as XSS.. they’re everywhere), then great.

All in all, i’ve really enjoyed my time reporting bugs on bugcrowd to this 1 company and I hope the success continues. Bugcrowd anaylsts have been great lately and i’ve been happy with how my reports are handled. If there are two things I want on bugcrowd though.. search and inline images. *hint hint*

— zseano

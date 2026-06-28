---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-21_new-clubhouse-security-vulnerabilities-could-happen-to-any-growing-unicorn.md
original_filename: 2021-04-21_new-clubhouse-security-vulnerabilities-could-happen-to-any-growing-unicorn.md
title: New Clubhouse Security Vulnerabilities Could Happen to Any Growing Unicorn
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: 97e74d71c09d46dc7ffc9faf03318d5d95402be405b29aac8c394bd6bb0f3669
text_sha256: e990948de7808121d8df2b700dd9a1cf860eea8915c43c9d08f16092cbc8c7e7
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# New Clubhouse Security Vulnerabilities Could Happen to Any Growing Unicorn

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-21_new-clubhouse-security-vulnerabilities-could-happen-to-any-growing-unicorn.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `97e74d71c09d46dc7ffc9faf03318d5d95402be405b29aac8c394bd6bb0f3669`
- Text SHA256: `e990948de7808121d8df2b700dd9a1cf860eea8915c43c9d08f16092cbc8c7e7`


## Content

---
title: "New Clubhouse Security Vulnerabilities Could Happen to Any Growing Unicorn"
url: "https://www.lutasecurity.com/post/new-clubhouse-security-vulnerabilities-could-happen-to-any-growing-unicorn"
final_url: "https://www.lutasecurity.com/post/new-clubhouse-security-vulnerabilities-could-happen-to-any-growing-unicorn"
authors: ["Katie Moussouris (@k8em0)"]
programs: ["Clubhouse"]
bugs: ["Logic flaw"]
publication_date: "2021-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3717
---

# New Clubhouse Security Vulnerabilities Could Happen to Any Growing Unicorn 

  * [Katie Moussouris](https://www.lutasecurity.com/members-area/84b3262f-2f5c-4a7b-90c2-eefd0a1fb1e4/profile)
  * Apr 21, 2021
  * 7 min read

Updated: Mar 13, 2024

##  _Para Bailar la Banshee Bomb_

  

![](https://static.wixstatic.com/media/3b8a7d_618f416179314731ac7d64324c2b6aab~mv2.jpg/v1/fill/w_106,h_190,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3b8a7d_618f416179314731ac7d64324c2b6aab~mv2.jpg)

  

Gather around folks, it's hacker story time, and today I want to tell the tale of how I hacked Clubhouse. It's a new social app that’s rocketed to popularity by facilitating live, audio-only group chats in virtual rooms. The app's viral popularity has vaulted its company to multiplatinum unicorn status. Recent valuations peg Clubhouse to be [worth upward of $4B](https://www.reuters.com/technology/clubhouse-closes-new-round-funding-that-would-value-app-4-billion-source-2021-04-18/). 

  

With a little bit of probing, **I was able to uncover some new problems (now fixed) in the app with serious security and privacy implications: My attack made it possible to appear as if I had left a room, while actually maintaining full bidirectional voice capabilities in that room as an invisible user, immune to moderator tools.**

  

The bug discoveries I made and the ensuing process of collaborating with Clubhouse to get them fixed should offer many startups some really valuable lessons. Not just technical ones—though I think the details of the attack are pretty interesting—but more importantly, some real-world lessons on the common missteps that companies make in running vulnerability disclosure programs and in creating bug bounties.

  

All organizations have vulnerabilities to address, and they all go through the [5 stages of vulnerability response grief](https://www.youtube.com/watch?v=T6e70upcfl4). Startups often mistakenly believe that the fastest path to establishing a strong security culture is by starting a bug bounty right away – but that is the worst first step. 

The point of this post isn't to shame Clubhouse, because this could have happened to any high-growth startup. Instead, I wanted to take the opportunity to run through how things went down in order to help every startup understand the growing pains they can experience if they jump into bug bounties too fast, even if leadership's heart is in the right place with security good intentions.

  

**The Biggest Takeaway: Don’t kill the messenger. Don’t ignore them either.**

Even people who’ve known me for many years sometimes forget that I am a hacker. While I haven’t made a living hacking computers for over a dozen years, I will never run out of the curiosity that drives me to push the limits of what systems were designed to do. This is what led me to dig into the Clubhouse app.

  

After hearing about some of the issues related to API abuse recently reported about Clubhouse, I felt that curiosity start to well up. I decided I wanted to test the session termination/invalidation that was rumored to address some of the privacy issues related to the API abuse. I initiated my test by installing the Clubhouse app on another iPhone, to see if it forced a logout in all sessions on all devices. 

  

It did not. 

  

Or at least, it didn’t behave that way in practice that would matter in this attack.

  

This behavior had serious security and privacy implications, violating the security and privacy policies of the Clubhouse app. The impact of this one issue was two-fold:

  

**1\. Eavesdropping ghost (Stillergeist):**

Victim users in any room, including private rooms, could be spied upon without their knowledge at any time by a silent attacker still in the room, if the attacker was * **ever** * in that room. 

  

**2\. Trolling ghost (Banshee Bombing):**

Victims would be unable to carry on a room uninterrupted by trolling and noise if they allowed the attacker onto the stage to speak at any time. This vulnerability also removed the ability for moderators of a room from muting or removing the attacker user, which would significantly downgrade the experience of users in important conversations, rendering the platform unusable, especially for open discussion rooms. 

  

I’ve been sworn at many times as a researcher. Thankfully, nobody swore at me this time when I reported my findings to Clubhouse, at least where I could hear it. In fact, I didn’t' hear much of anything because it took multiple emails and a few weeks of effort to get a response from the company. 

  

Receiving abuse for disclosing security findings stink, but being ignored isn’t fun either. Especially because we researchers do our thing to protect users, which should be a shared goal of security researchers and their research targets.

  

It took multiple attempts for Clubhouse to respond to data requests from Whitney Merrill too, a seasoned former FTC attorney who had been trying every avenue to exercise her privacy rights under the [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa). Clubhouse did eventually get back to her with the requested data, but the process should not have taken so long [_(60+days for her)_](https://twitter.com/wbm312/status/1382160730456162305?s=20) on both the privacy and security fronts.

  

Once I reached a human on the Clubhouse side, they invited me to join their private bug bounty program. So it is clear that they have ***some*** kind of protocol in place to field security research findings. I refused to accept the private bug bounty invitation due to the NDA required, but the founders of Clubhouse did agree to donate the bug bounty to the [Pay Equity Now Foundation](https://payequitynowfoundation.org/donate). 

  

Clubhouse has committed to the donation, but unfortunately at the time of publication, their bug bounty platform provider failed to come up with a bounty amount recommendation. Vendors tasked with helping you manage your bug bounty or VDP must never cause delays or friction in this process, or they are your weakest link. 

  

Here’s what else Clubhouse did right: They didn’t ignore my report indefinitely, and they didn’t threaten me with legal action when they did acknowledge receipt of the report. Those may not seem like a big deal, but in reality, security researchers are most often met with silence or hostility. It’s rare for an early-stage startup to demonstrate a genuine willingness to engage with helpful hackers to improve their security.

  

Nevertheless, the time it took to respond to me with my unsolicited vulnerability disclosure should offer clues to fellow startups on why starting a private bug bounty may not be a great first step. The heavy lifting in a [_sudden surge in popularity and vulnerability cases_](https://www.lutasecurity.com/post/luta-security-highlights-for-zoom-bug-bounty-programs) can bog down a small team that hasn't prepared with other fundamentals.

  

Once they did respond, they said they hoped to fix it in a few days’ time. They let me know about a week later that they’d fixed it. I retested the attacks, and found the issue only looked mitigated but not fixed. The attacker would get automatically muted, as would the audio of the room, if they used a second device to try to eavesdrop or to disrupt. The issue of improper session termination did not appear to be addressed though, since I could still use two phones to join two different rooms simultaneously. Later, it turned out that what I thought was one vulnerability was actually two, and not the root cause I thought, as Clubhouse says they revoked all session tokens on the server side, but that the issue I saw was related to a feed cache – read on. 

  

Had I been less experienced in vulnerability disclosure and less patient with this company, this bug would have easily been a fun one to drop as zero day. There were several points in this disclosure journey that might have made a researcher drop zero day, which would have certainly knocked down that $4B valuation. It could have happened during the weeks it took to get a human response, or at the point at which it seemed they didn’t get the fix done at the server where it belonged, or certainly when their lead investor, Marc Andreesen, suddenly blocked me without us ever interacting on Twitter after following me for years. All those behaviors to a researcher would indicate indifference or hostility from the company. 

  

An audio-only service that allows an attacker, with no special equipment, to silently eavesdrop (Stillergeist) or loudly disrupt (Banshee Bomb) the experience would have directly impacted the value of the business.

  

**The Technical Details**

So here are the gory details of the attack as first reported to Clubhouse, and a [video demo](https://youtu.be/TtfdpXop8g4). [[Bonus outtakes with my cat Scapy](https://youtu.be/RLWu6ZlvXao)]

![](https://static.wixstatic.com/media/a77f63_38a7acbb7e464dbbb823c5acb98b66a8~mv2.png/v1/fill/w_53,h_75,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/a77f63_38a7acbb7e464dbbb823c5acb98b66a8~mv2.png)

Upon my response that the vulnerability still wasn’t fixed, Clubhouse explained that the above root cause was not correct – that they did manage sessions statefully on the server, and that it was actually two bugs, not one. The real root cause of one vulnerability was a missed call to a session termination API when a user logs into a new device, leaving the old device logged in simultaneously. The second issue, that Clubhouse already knew about, appeared to be a delay in session invalidation on the server side. Instead they said this was due to a caching delay in the feed the attacker sees, that was allowing the appearance of still being able to join more than one room on different devices.

  

**What Would A Secure Startup Do?**

The prevailing lesson here is that startups driven by market pressures tend to prioritize growth over building a culture of security and privacy. While it’s clear in talking to Clubhouse that they are making a sincere effort, it appears that they've made the common mistake of putting bug bounties ahead of other internal security investments.

  

What investments in security and privacy should startups like this make to avoid this pitfall? 

Here are my suggestions in order of priority:

  

**1.** Start with a [_Vulnerability Coordination Maturity Model (VCMM)_](https://www.lutasecurity.com/solutions) assessment to identify gaps in people, process, and technology

**2.** Conduct a professional penetration test before starting private bug bounty

**3.** Fix bugs in code & fill process gaps

**4.** Open a VDP & we recommend running it for a couple of years before starting a bug bounty

**5.** Hire security engineers, maybe from your VDP pool of talent to build your in-house capabilities

**6.** Profit!

  

The folks at Clubhouse were friendly with me once they knew who I was, but you shouldn’t have to be the coauthor of the ISO standards on vulnerability disclosure to have your bug reports acknowledged and fixed. Nor should you have to be a former FTC attorney to get your data privacy requests answered. 

  

Frankly, I love this app more than I thought I would, even as introverted as I am – it’s given us all a sense of togetherness and presence unmatched in other social media. Where else could I stumble into a random room, hear MC Hammer discussing philosophy, tweet about it, only to have [MC Hammer retweet it](https://twitter.com/k8em0/status/1384376929478873089?s=20). Vulnerability response requires a focused presence as well to maximize smooth security outcomes.

  

Because at the end of the day you don’t have to be a hacker like me to find security and privacy bugs in new software that's been built by a company that hasn’t hired their own dedicated security team yet. It just takes some curiosity, maybe even an optional cat, and a willingness to challenge the assumptions of the designers of the service. 

  

Given this experience with Clubhouse, I have faith that they are getting the hang of security and privacy as they build. Let’s hope the next unicorn startups apply their massive resources and enthusiasm to growing their trust and safety in proportion to their customer growth.

  

Tags:

  * [bug bounty](https://www.lutasecurity.com/blog/tags/bug-bounty)
  * [vulnerabilities](https://www.lutasecurity.com/blog/tags/vulnerabilities)
  * [vulns](https://www.lutasecurity.com/blog/tags/vulns)
  * [Hacked](https://www.lutasecurity.com/blog/tags/hacked)
  * [Clubhouse](https://www.lutasecurity.com/blog/tags/clubhouse)
  * [bugs](https://www.lutasecurity.com/blog/tags/bugs)

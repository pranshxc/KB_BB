---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-11_attack-of-the-week-airdrop-tracing.md
original_filename: 2024-01-11_attack-of-the-week-airdrop-tracing.md
title: 'Attack of the week: Airdrop tracing'
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 15086642df065d7c197ab7536052f64a945b770cd0772d62aa4752683c2d10af
text_sha256: 172aceca1299585a46e961fd032a9c91d72377e7eee1b8140cf1d81273f5fe86
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Attack of the week: Airdrop tracing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-11_attack-of-the-week-airdrop-tracing.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `15086642df065d7c197ab7536052f64a945b770cd0772d62aa4752683c2d10af`
- Text SHA256: `172aceca1299585a46e961fd032a9c91d72377e7eee1b8140cf1d81273f5fe86`


## Content

---
title: "Attack of the week: Airdrop tracing"
page_title: "Attack of the week: Airdrop tracing – A Few Thoughts on Cryptographic Engineering"
url: "https://blog.cryptographyengineering.com/2024/01/11/attack-of-the-week-airdrop-tracing/"
final_url: "https://blog.cryptographyengineering.com/2024/01/11/attack-of-the-week-airdrop-tracing/"
authors: ["Matthew Green (@matthew_d_green)"]
programs: ["Apple (AirDrop)"]
bugs: ["Cryptographic issues", "Privacy issue"]
publication_date: "2024-01-11"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 559
---

It’s been a while since I wrote an “attack of the week” post, and the fault for this is entirely mine. I’ve been much too busy writing boring posts about [Schnorr signatures](https://blog.cryptographyengineering.com/2023/10/06/to-schnorr-and-beyond-part-1/)! But this week’s news brings an exciting story with both technical _and_ political dimensions: new reports claim that Chinese security agencies have developed a technique [to trace the sender of AirDrop transmissions](https://www.techradar.com/pro/security/chinese-hackers-claim-to-have-found-a-way-to-crack-apple-airdrop-and-find-out-email-addresses-phone-numbers). 

Typically my “attack of the week” posts are intended to highlight recent research. What’s unusual about this one is that the attack is not really _new_ ; it was discovered way back in 2019, when a set of TU Darmstadt researchers — Heinrich, Hollick, Schneider, Stute, and Weinert — reverse-engineered the Apple AirDrop protocol and disclosed several privacy flaws to Apple. (The resulting paper, which appeared in Usenix Security 2021 [can be found here](https://www.usenix.org/conference/usenixsecurity21/presentation/heinrich).)

What makes this _an attack of the week_ is a piece of news that was initially reported by [Bloomberg](https://www.bloomberg.com/news/articles/2024-01-09/china-says-cracked-apple-s-airdrop-to-identify-message-sources?embedded-checkout=true&leadSource=uverify%20wall) (here’s some [other coverage](https://www.techradar.com/pro/security/chinese-hackers-claim-to-have-found-a-way-to-crack-apple-airdrop-and-find-out-email-addresses-phone-numbers) [without paywall](https://www.macrumors.com/2024/01/09/airdrop-cracked-chinese-authorities/)) claiming that researchers in China’s Beijing Wangshendongjian Judicial Appraisal Institute have used these vulnerabilities to help police to identify the sender of “unauthorized” AirDrop materials, using a technique based on rainbow tables. While this new capability may not (yet) be in widespread deployment, it represents a new tool that could strongly suppress the use of AirDrop in China and Hong Kong. 

And this is a big deal, since AirDrop is apparently one of a few channels that can still be used to disseminate unauthorized protest materials — and indeed, that was used in both places in 2019 and 2022, and (allegedly as a result) has already been subject to various [curtailments](https://mashable.com/article/apple-limit-airdrop).

In this post I’m going to talk about the Darmstadt research and how it relates to the news out of Beijing. Finally, I’ll talk a little about what Apple can do about it — something that is likely to be as much of a _political_ problem as a technical one.

As always, the rest of this will be in the “fun” question-and-answer format I use for these posts.

### What is AirDrop and why should I care?

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2024/01/image.png?w=760)](https://blog.cryptographyengineering.com/wp-content/uploads/2024/01/image.png)Image from Apple. Used without permission.

If you own an iPhone, you already know the answer to this question. Otherwise: [AirDrop is an Apple-specific protocol that](https://support.apple.com/guide/security/airdrop-security-sec2261183f4/web) allows Apple devices to send files (and contacts and other stuff) in a peer-to-peer manner over various wireless protocols, including Bluetooth and WiFi. 

The key thing to know about AirDrop is that it has two settings, which can be enabled by a potential receiver. In “Contacts Only” mode, AirDrop will accept files only from people who are in your Contacts list (address book.) When set to “Everyone”, AirDrop will receive files from any random person within transmit range. This latter mode has been extensively used to distribute protest materials in China and Hong Kong, as well as to distribute [indecent photos](https://mashable.com/article/airdrop-dick-pics-what-to-do-iphone) to strangers all over the world.

The former usage of AirDrop became such a big deal in protests that in 2022, Apple [pushed a software update](https://www.cnbc.com/2022/11/30/apple-limited-a-crucial-airdrop-function-in-china-just-weeks-before-protests.html) exclusively to Chinese users that limited the “Everyone” receive-from mode — ensuring that phones would automatically switch back to “Contacts only” after 10 minutes. The company later extended this software update to [all users worldwide](https://appleinsider.com/articles/22/12/07/ios-162-implements-10-minute-airdrop-time-limit-globally), but only after they were extensively criticized for the original move.

### Is AirDrop supposed to be private? And how does AirDrop know if a user is in their Contacts list? 

While AirDrop is not explicitly advertised as an “anonymous” communication protocol, any system that has your phone talking to strangers has _implicit_ privacy concerns baked into it. This drives many choices around how AirDrop works.

Let’s start with the most important one: do AirDrop senders provide their ID to potential recipients? The answer, at some level, must be “yes.”

The reason for this is straightforward. In order for AirDrop recipients in “Contacts only” mode to check that a sender is in their Contacts list, there must be a way for them to check the sender’s ID. This implies that the sender must somehow reveal their identity to the recipient. And since AirDrop presents a list of possible recipients any time a sending user pops up the AirDrop window, this will happen at “discovery” time — typically before you’ve even decided if you really want to send a file.

But this poses a conundrum: the sender’s phone doesn’t actually know which nearby AirDrop users are willing to receive files from it — i.e., which AirDrop users have the sender in their Contacts — _and it won’t know this_ until it actually talks to them. But talking to them means your phone is potentially shouting at everyone around it _all the tim_ e, saying something like:

> _Hi there! My Apple ID is john.doe.28@icloud.com. Will you accept files from me!??_

Now forget that this is being done by phones. Instead imagine yourself, as a human being, doing this to every random stranger you encounter on the subway. It should be obvious that this will quickly become a privacy concern, one that would scare even a company that _doesn’t_ care about privacy. But Apple generally does care quite a bit about privacy!

Thus, just solving this basic problem requires a clever way by which phones can figure out whether they should talk to each other — i.e., whether the receiver has the sender in its Contacts — without either side leaking any useful information to random strangers. Fortunately cryptographic researchers have thought a lot about this problem! We’ve even given it a cool name: it’s called [Private Set Intersection](https://en.wikipedia.org/wiki/Private_set_intersection), or PSI.

To make a long story short: a Private Set Intersection protocol takes a set of strings from the Sender and a set from the Receiver. It gives one (or both) parties the _intersection_ of both sets: that is, the set of entries that appear on both lists. Most critically, a good PSI protocol doesn’t reveal _any other information about either of the sets._

In Apple’s case, the Sender would have just a few entries, since you can have a few different email addresses and phone numbers. The Receiver would have a big set containing its entire Contacts list. The output of the protocol would contain either (1) one or more of the Sender’s addresses, or (2) _nothing_. A PSI protocol would therefore solve Apple’s problem nicely.

### Great, so which PSI protocol does Apple use?

The best possible answer to this is: 😔.

For a variety of mildly defensible reasons — which I will come back to in a moment — Apple _does not use_ a secure PSI protocol to solve their AirDrop problem. Instead they did the thing that every software developer does when faced with the choice of doing complicated cryptography or “hacking something together in time for the next ship date”: they threw together their own solution using hash functions.

The TU Darmstadt researchers did a nice job of reverse-engineering Apple’s protocol [in their paper.](https://www.usenix.org/system/files/sec21-heinrich.pdf) Read it! The important bit happens during the “Discovery” portion of the protocol, which is marked by an HTTPS POST request as shown in the excerpt below:

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2024/01/image-1.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2024/01/image-1.png)

The very short TL;DR is this:

  1. In the POST request, a sender attaches a[ truncated SHA-256 hash](https://en.wikipedia.org/wiki/Hash_function) of its own Apple ID, which is contained within a signed certificate that it gets from Apple. (If the sender has more than one identifier, _e.g.,_ a phone number and an email address, this will contain hashes of each one.)
  2. The recipient then hashes every entry in its Contacts list, and compares the results to see if it finds a match.
  3. If the recipient is in Contacts Only mode and finds a match, it indicates this and accepts later file transfers. Otherwise it aborts the connection.

(As a secondary issue, AirDrop also includes a very short [two byte] portion of the same hashes in its BLE advertisements. Two bytes is pretty tiny, which means this shouldn’t leak _much_ information, since many different addresses will collide on a two-byte hash. However, some other researchers have determined that it [generally does](https://habr.com/ru/companies/ruvds/articles/505384/) work well enough to guess identities. Or they may have, the source isn’t translating well for me.)

A second important issue here is that the hash identifiers are apparently stored in logs within the recipient’s phone, which means that to obtain them you don’t have to be physically present when the transfer happens. You can potentially scoop them out of someone else’s phone after the fact. 

### So what’s the problem?

Many folks who have some experience with cryptography will see the problem immediately. But let’s be explicit.

Hash functions are designed to be one-way. In theory, this means that there is should be no efficient algorithm for “directly” taking the output of a hash function and turning it back into its input. But that guarantee has a huge asterisk: if I can _guess_ a set of possible inputs that could have produced the hash, I can simply _hash each one of my guesses and compare it to the target._ If one input matches, then chances are overwhelming that I’ve found the right input (also called a pre-image.) 

In its most basic form, this naive approach is called a “[dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack)” based on the idea that one can assemble a dictionary of likely candidates, then test every one. Since these hashes apparently don’t contain any session-dependent information (such as salt), you can even do the hashing in advance to assemble a dictionary of _candidate hashes_ , making the attack even faster.

This approach won’t work if your Apple ID (or phone number) is not guessable. The big question in exploiting this vulnerability is whether it’s possible to assemble a complete list of candidate Apple ID emails and phone numbers. The answer for phone numbers, as the Darmstadt researchers point out, is _absolutely yes_. Since there are only a few billion phone numbers, it is entirely possible to make a list of every phone number and have a computer grind through them — given a not-unreasonable amount of time. For email addresses this is more complicated, but there are many [lists of email addresses](https://haveibeenpwned.com/) in the world, and the Chinese state authorities almost certainly have some good approaches to collecting and/or generating those lists.

As an aside, exploiting these dictionaries can be done in three different ways:

  1. You can make a list of candidate identifiers (or generate them programmatically) and then, given a new target hash, you can hash each identifier and check for a match. This requires you to compute a whole lot of SHA256 hashes for each target you crack, which is pretty fast on a GPU or FPGA (or ASIC) but not optimal.
  2. You can pre-hash the list and make a database of hashes and identifiers. Then when you see a target hash, you just need to do a fast lookup. This means all computation is done _once_ , and lookups are fast. But it requires a ton of storage.
  3. Alternatively, you can use an intermediate approach called a _time-memory tradeoff_ in which you exchange _some_ storage for _some_ computation once the target is found. The most popular technique is called a [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table), and it really deserves its own separate blog post, though I will not elaborate today.

The Chinese announcement explicitly mentions a rainbow table, so that’s a good indicator that they’re exploiting this vulnerability. 

### Well that sucks. What can we, or rather Apple, do about it?

If you’re worried about leaking your identifier, an immediate solution is to turn off AirDrop, assuming such a thing is possible. (I haven’t tried it, so I don’t know if turning this off will really stop your phone from talking to other people!) Alternatively you can unregister your Apple ID, or use a bizarre high-entropy Apple ID that nobody will possibly guess. Apple could also reduce their use of logging.

But those solutions are all terrible.

The proper technical solution is for Apple to replace their hashing-based protocol with a _proper_ PSI protocol, which will — as previously discussed — reveal only one bit of information: whether the receiver has the sender’s address(es) in their Contacts list. Indeed, that’s the solution that the Darmstadt researchers propose. [They even devised a Diffie-Hellman-based PSI protocol called “PrivateDrop” and](https://www.usenix.org/conference/usenixsecurity21/presentation/heinrich) showed that it can be used to solve this problem.

But this is not necessarily an easy solution, for reasons that are both technical _and_ political. It’s worth noting that Apple almost certainly knew from the get-go that their protocol was vulnerable to these attacks — but even if they didn’t, they were told about these issues back in May 2019 by the Darmstadt folks. It’s now 2024, and Chinese authorities are exploiting it. So clearly it was not an easy fix.

Some of this stems from the fact that PSI protocols are more computationally heavy that the hashing-based protocol, and some of it (may) stem from the need for more interaction between each pair of devices. Although these costs are not particularly unbearable, it’s important to remember that phone battery life and BLE/WiFi bandwidth is precious to Apple, so even minor costs are hard to bear. Finally, _Apple may not view this as really being an issue._

However in this case there is an even tougher political dimension.

### Will Apple even fix this, given that Chinese authorities are now exploiting it?

And here we find the hundred billion dollar question: if Apple actually replaced their existing protocol with PrivateDrop, would that be viewed negatively by the Chinese government? 

Those of us on the outside can only speculate about this. However, the facts are pretty worrying: Apple has enormous manufacturing and sales resources located inside of China, which makes them extremely vulnerable to an irritated Chinese government. They have, in the past, taken actions that _appeared_ to be targeted at restricting AirDrop use within China — and although there’s no definitive proof of their motivations, it certainly looked bad. 

Finally, Apple has recently been the [subject of pressure by the Indian government](https://www.washingtonpost.com/world/2023/12/27/india-apple-iphone-hacking/) over its [decision to alert journalists](https://techcrunch.com/2023/12/27/india-pressed-apple-on-state-sponsored-warnings-report-says/?guccounter=1) about a set of allegedly state-sponsored attacks. Apple’s response to this pressure was to substantially tone down its warnings. And Apple has many fewer resources at stake in India than in China, although that’s [slowly changing](https://www.wsj.com/tech/apple-aims-to-make-a-quarter-of-the-worlds-iphones-in-india-ab7f6342).

Hence there is a legitimate question about whether it’s politically wise for Apple to make a big technical improvement to their AirDrop privacy, right at the moment that the _lack of privacy_ is being viewed as an asset by authorities in China. Even if this attack isn’t really that critical to law enforcement within China, the decision to “fix” it could very well be seen as a slap in the face. 

One hopes that despite all these concerns, we’ll soon see a substantial push to improve the privacy of AirDrop. But I’m not going to hold my breath.

### _Related_

[![Matthew Green's avatar](https://2.gravatar.com/avatar/b8e81a16777cfcacc459c2a900d9f120f88bef2d30669a33df5b2a486b8e29c2?s=100&d=identicon&r=PG)](https://blog.cryptographyengineering.com/author/matthewdgreen/)

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/) I'm a cryptographer and professor at Johns Hopkins University. I've designed and analyzed cryptographic systems used in wireless networks, payment systems and digital content protection platforms. In my research I look at the various ways cryptography can be used to promote user privacy. 

**Published** January 11, 2024January 12, 2024

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-03_how-i-am-able-to-hijack-you_2.md
original_filename: 2019-04-03_how-i-am-able-to-hijack-you_2.md
title: How I am able to hijack you.
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- business-logic
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- business-logic
language: en
raw_sha256: b6521487f5eb0d11c63362bf4c508746a9558eae62d784beaf86a5c0ac69de90
text_sha256: afb7ab3a0da3567ded9643501f2383389fffaf22cc5893fa69c8884adc0833c6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I am able to hijack you.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-03_how-i-am-able-to-hijack-you_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, business-logic
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b6521487f5eb0d11c63362bf4c508746a9558eae62d784beaf86a5c0ac69de90`
- Text SHA256: `afb7ab3a0da3567ded9643501f2383389fffaf22cc5893fa69c8884adc0833c6`


## Content

---
title: "How I am able to hijack you."
url: "https://medium.com/bugbountywriteup/how-i-am-able-to-hijack-you-1cab793a01d1"
authors: ["Terjanq (@terjanq)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2019-04-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5332
scraped_via: "browseros"
---

# How I am able to hijack you.

How I am able to hijack you.
or rather: How I am able to hijack your autosuggestions in Google Search.
terjanq
Follow
3 min read
·
Apr 3, 2019

190

1

Google Search has been going through a lot lately due to the outstanding XSS finding that was done by Masato Kinugawa. In this brief article I wanted to share with you, maybe not as exciting as the finding mentioned above, but for sure a very cool bug that I discovered when sniffing around Google Search lately.

The title with the intro image at the side should already reveal what the vulnerability that I found is about. It’s manipulation of one’s autosuggestion list that pops out when they’re searching for phrases using the Google Search website.

What I discovered is that the only step required to add an exact phrase into the mentioned list is simply visiting the URL https://www.google.com/search?q=phrase. Simple as that. The attacker can just make a few requests in the background and put anything into your autosuggestions without you even noticing.

Why would the attacker want to achieve this?

The answer to this question is not trivial. However, I found a few cases that could impact the users in one way or another. These cases are as follows.

Advertising the product. The company could try to advertise their product by flooding the visitor’s autosuggestion list, so when they’re searching for a specific item the company brand would show up before the user even hits the ENTER.

Get terjanq’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Phishing. The attacker could try to put the phishing websites at the top of the list, e.g. facebook⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀site:facehook.tk that would steal their credentials when attempting logging in.

Press enter or click to view image in full size
facebook⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀site:facehook.tk

Annoyance. The reason behind the flooding doesn’t necessarily have to pose any security impact to do damage. For example, the only goal that the attacker could have in mind could be to flood someone’s autosuggestion list with thousands of phrases. Just to annoy. Clicking a thousand times ‘remove’ could be really frustrating if you didn’t happen to know a way to clear all the search history at once.

Embarrassment. Another possible goal is to cause the victim to feel embarrassed. Imagine someone presenting in front of the audience and in the middle of a speech, when attempting searching for something, very inappropriate results show up. I can’t imagine a bigger embarrassment during the speech :)

Security issue or not?

In my opinion, the finding is a security issue in a way that could impact a lot of users. Nevertheless, the Google team didn’t share that point of view, which I fully respect, and the issue was closed as Won’t Fix (Intended behavior).

The flooding one’s autosuggestion doesn’t seem to have a great motivation factor for the attacker, what would they gain out of this?

We think the issue might not be severe enough for us to track it as a security bug.

I probably should also mention that this vulnerability was part of a bigger report that was related to clickjacking the Google reCAPTCHA which is a bridge to many other attacks that will also appear on my Twitter wall soonly. Follow me on Twitter to stay up to date @terjanq.

If you’ve come all the way here and you are currently logged into your Google account, I’ve left an easter egg for you there! Open the google.com website in a new tab and start typing terjanq in the search bar there. If you solved the riddle or you have any other suggestions in what devilish way the vulnerability could be abused, let me know in the comments! :)

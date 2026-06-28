---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-08_hacking-a-large-company-in-minutes-by-reading-docs.md
original_filename: 2023-09-08_hacking-a-large-company-in-minutes-by-reading-docs.md
title: Hacking a Large Company in MINUTES by Reading Docs
category: documents
detected_topics:
- access-control
- sso
- command-injection
- otp
- mobile-security
- supply-chain
tags:
- imported
- documents
- access-control
- sso
- command-injection
- otp
- mobile-security
- supply-chain
language: en
raw_sha256: 94c5d2b7a490657a859f6643563b5f9b9bc35b633a0092f02091ba984e7bca3d
text_sha256: 6053b6a7767d18e8a9920e0e1b2d45415a209529afe29380c6e4381ef16bfda3
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a Large Company in MINUTES by Reading Docs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-08_hacking-a-large-company-in-minutes-by-reading-docs.md
- Source Type: markdown
- Detected Topics: access-control, sso, command-injection, otp, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `94c5d2b7a490657a859f6643563b5f9b9bc35b633a0092f02091ba984e7bca3d`
- Text SHA256: `6053b6a7767d18e8a9920e0e1b2d45415a209529afe29380c6e4381ef16bfda3`


## Content

---
title: "Hacking a Large Company in MINUTES by Reading Docs"
url: "https://medium.com/@dan.lig/hacking-a-large-company-in-minutes-by-reading-docs-62dfafced22e"
authors: ["dan.lig"]
bugs: ["Broken Access Control", "Authentication bypass"]
publication_date: "2023-09-08"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 796
scraped_via: "browseros"
---

# Hacking a Large Company in MINUTES by Reading Docs

Hacking a Large Company in MINUTES by Reading Docs
dan.lig
Follow
4 min read
·
Sep 9, 2023

30

2

The vulnerability discussed in this blog post has been reported to the relevant company by the author, and it has been promptly addressed. To protect privacy and security, specific details are omitted. The alias “BIC” (Big Italian Company) will be utilized to denote the mentioned company.

AI Disclaimer: This article was edited with the help of AI to improve its readability and flow.

It was a seemingly ordinary day when I found myself navigating BIC’s website. A boring task quickly transformed into an exhilarating journey as I embarked on a path of unexpected discoveries.

Innocently enough, I decided to create a new account. The process seemed straightforward, and within moments, I received the expected confirmation email.
But there, lurking beneath the surface, was a subtle enigma. As I scrutinized the email, something caught my eye, subtly hidden in the confirmation link. The domain it led to was not the familiar BIC domain I had just interacted with.

My curiosity piqued, I isolated the domain part and cautiously entered it into my browser’s address bar. What I stumbled upon left me surprised: a clandestine login page.

Press enter or click to view image in full size

But the plot thickened as I delved deeper. Examining the website’s footer, I uncovered its connection to a third-party framework. My quest for answers led me to scour the annals of the internet until I uncovered the official website associated with this enigmatic framework. Within its documentation lay the key to a potentially explosive revelation.

Press enter or click to view image in full size

I skimmed through the cryptic content, a nagging suspicion growing in my mind. It mirrored the initial unease I felt when dissecting the account confirmation link, particularly the perplexing “execservice.vcmd?commands=” segment. It dawned on me that I might hold the key to unlocking any hidden function, merely by altering the “commands” GET parameter.

Get dan.lig’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My quest took an intriguing turn when I came across the “getsessionview” function. The documentation, tantalizingly vague, provided no roadmap.

Press enter or click to view image in full size

My insatiable curiosity urged me onward, pushing me to execute the mysterious command. The URL path “/execservice.vcmd?commands=getsessionview” became my ticket to the unknown, and to my astonishment, it worked seamlessly.

Press enter or click to view image in full size

In an instant, I was granted access to the clandestine realm of logged-in users, without a whisper of authentication. A thrill surged through me as I realized the magnitude of my newfound power.

Intriguingly, these session tokens bore a striking resemblance to the coveted session cookie. The pieces of the puzzle began to fall into place.

Press enter or click to view image in full size

With a daring experiment, I replaced my session cookie with one of the tokens I had seized. The result was nothing short of miraculous, I found myself in possession of a golden key to the website’s admin panel.

Press enter or click to view image in full size

The world I had uncovered was beyond my wildest dreams. The company I had believed to be small and unassuming revealed its true scale, an empire with over 500,000 clients. With this access, I held the keys to modify product information, manipulate prices, forge new coupons and gift cards, and delve into confidential customer data.

Yet, in a twist of morality, I chose the path of the virtuous digital wanderer. I knew what needed to be done. With a sense of responsibility, I immediately reported this monumental security breach to BIC, knowing that my discovery could have easily led me down a darker path.

In this labyrinth of digital intrigue, I had uncovered a hidden world of power and vulnerability, but in the end, I chose to be the silent hero, guarding the gate to the kingdom rather than storming its fortress.

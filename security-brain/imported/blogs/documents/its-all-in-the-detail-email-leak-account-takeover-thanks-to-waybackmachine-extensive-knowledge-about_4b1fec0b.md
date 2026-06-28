---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-30_its-all-in-the-detail-email-leak-account-takeover-thanks-to-waybackmachine-exten.md
original_filename: 2018-10-30_its-all-in-the-detail-email-leak-account-takeover-thanks-to-waybackmachine-exten.md
title: 'It’s all in the detail: Email leak & Account takeover thanks to WayBackMachine
  & extensive knowledge about the program'
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 4b1fec0b6a3810d8d5a1ded55f10ffde6142eff806136d4c10aa780b04d64f53
text_sha256: 65254e946b9500b773c100a03b2f033540086846225b8078b1f6cf8acce311cf
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# It’s all in the detail: Email leak & Account takeover thanks to WayBackMachine & extensive knowledge about the program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-30_its-all-in-the-detail-email-leak-account-takeover-thanks-to-waybackmachine-exten.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4b1fec0b6a3810d8d5a1ded55f10ffde6142eff806136d4c10aa780b04d64f53`
- Text SHA256: `65254e946b9500b773c100a03b2f033540086846225b8078b1f6cf8acce311cf`


## Content

---
title: "It’s all in the detail: Email leak & Account takeover thanks to WayBackMachine & extensive knowledge about the program"
url: "https://medium.com/@zseano/its-all-in-the-detail-email-leak-account-takeover-thanks-to-waybackmachine-extensive-4be365580dd7"
authors: ["Zseano (@zseano)"]
bugs: ["Information disclosure", "Authentication bypass", "Account takeover"]
publication_date: "2018-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5617
scraped_via: "browseros"
---

# It’s all in the detail: Email leak & Account takeover thanks to WayBackMachine & extensive knowledge about the program

It’s all in the detail: Email leak & Account takeover thanks to WayBackMachine & extensive knowledge about the program
Sean (zseano)
Follow
3 min read
·
Oct 30, 2018

463

2

When a researcher spends a lot of time on one bugbounty program the bug impact tends to increase as they gain knowledge around the web assets and how things work & are connected together. (atleast in my experience, if you have spent a lot of time on one program i’d love to hear your thoughts). I strongly believe bugbounties can help companies & researchers form a strong relationship :)

How I generally feel sometimes heh :D
Understanding how your target works

When a lot of people message me, “How do I go looking for bugs? Where do I start?” i’ll always tell them: Just simply use the site with BURP running and start learning & playing. I stand by that advice, you simply can’t go wrong and if you’re new to hacking then this should be your first step on a program. As your experience&knowledge grows you’ll start to expand out and start using more tools to discover subdomains, common files, etc. Then in time, you can set your tools running whilst you begin poking. :)

With that said, in my testing on this site I saw that for the unsubscribe feature it required what looked like just my unencoded userID and encoded. If valid it would show you the email you’re unsubscribing. Something I want to play with more.

https://www.redacted.com/unsubscribe?1=38384&2=BBG45345DDW34W

I straight away went to my profile and verified that the “2” value was indeed my encoded userID, so 1 must be it unencoded. But how do I get it?

First interesting bug found relating to user id leak

This one didn’t lead to account takeover but did lead to any userid’s email being leaked remotely. If you messaged the user, the URL would look like this:

https://www.redacted.com/community/message?uid=ABC12345DDW34W

Straight forward. The ?uid= value is their userid encoded. Except upon sending the user a message in the source was that users unencoded ID. I went back to the URL to send a message and yup, there it was as well. Now all I had to do was scrape both values, visit the URL below with their ID and their email address is leaked.

https://www.redacted.com/unsubscribe?1=here&2=here

Simple! :) Bug one.

Where else can it be used?

I’ve mentioned before that I will always use WayBackMachine to scrape a sites /robots.txt file from years ago as you never know what was in there and if any of those files are still on the server. Armed with my results I did a search for anything containing “unsubscribe”. Bingo, “unsubscribe2” found.

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Excited, I quickly visited /unsubscribe2?1=userid&2=encryptedid only to just be redirected to the homepage.

But wait….. i’m logged into my other account?

So it turns out visiting /unsubscribe2 will grant you access to that account as long as the IDs are both valid. Nice! Looking back at the request in BURP I can see it just sets the session cookies and redirects. :D So now we can leak any users email and also gain access to their account.

When hunting, write NOTES.

Yes, I wrote Notes in big letters for a reason as it’s another reason why I started BugBountyNotes. I hope to create a platform for users to easily write their notes & thoughts when testing to help yourself, and other researchers, as well as being able to find & share anything bugbounty related.

Writing notes when testing is extremely useful especially if you spend lots of time on one program. When a new feature is released, or if you spot certain values in certain places, you can instantly know what you’re looking at/for. I also think this is why it’s crucial for programs to build strong relationships with researchers as the more engaging & welcoming a program is, the more researchers will stay and continue poking. The longer they spend, atleast in my experience, bug impact rises as they understand your assets more.

From my experience and looking back some of the bugs i’ve found and the thought-train I must of been having, I surprise myself. How did you think to try that?! Then I read back at my notes and it makes sense. :) Do you do the same and if so, what is your process and where do you store notes, would love to hear others thoughts!

Until the next one:)

-zseano

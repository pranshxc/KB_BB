---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-08_bugbounty-how-i-takeover-microsoft-store.md
original_filename: 2018-11-08_bugbounty-how-i-takeover-microsoft-store.md
title: '#bugbounty How I Takeover Microsoft Store.'
category: documents
detected_topics:
- sso
- xss
- command-injection
- path-traversal
- mobile-security
tags:
- imported
- documents
- sso
- xss
- command-injection
- path-traversal
- mobile-security
language: en
raw_sha256: b922e30adc6f370731564dc91cbd387b0380d8d170f8cb2b47565c1c3c8ed113
text_sha256: 879d09e9d00221be1de642b4ddc692974b70edc93f59cdfa7158d7592713a0a5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# #bugbounty How I Takeover Microsoft Store.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-08_bugbounty-how-i-takeover-microsoft-store.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, path-traversal, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b922e30adc6f370731564dc91cbd387b0380d8d170f8cb2b47565c1c3c8ed113`
- Text SHA256: `879d09e9d00221be1de642b4ddc692974b70edc93f59cdfa7158d7592713a0a5`


## Content

---
title: "#bugbounty How I Takeover Microsoft Store."
page_title: "#Bugbounty How I Takeover Microsoft Store. | by Sadiq West | Medium"
url: "https://medium.com/@sadiqwest01/bugbounty-how-i-takeover-microsoft-store-a58c1b785aa0"
authors: ["Sadiq West"]
programs: ["Microsoft"]
bugs: ["Subdomain takeover"]
publication_date: "2018-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5600
scraped_via: "browseros"
---

# #bugbounty How I Takeover Microsoft Store.

#Bugbounty How I Takeover Microsoft Store.
Sadiq West
Follow
3 min read
·
Nov 9, 2018

146

2

Hi,Guys

Today. I will proudly share to you, how I was successfully takeover microsoft store page, i have been learning from diffrent security researchers write-up in the bug bounty field, so i decided to share my few findings with you as it might help others who started in the Bug Bounty journey.

The bug i wanna share with you, it was new to me hence i never came across any bug like this throughout my reading from other researchers write-up.

From low impact to store takeover, “this how i may call it”

The first tool I used to identify the vulnerable of a domain was https://github.com/aboul3la/Sublist3r

Running on my android through TERMUX

I am recommending you to have it on your smartphone you can download it here https://play.google.com/store/apps/details?id=com.termux

Let’s the game started:

I was not a full time bug hunter, so i usually start looking a bug when i have time so this time, i started my recon on flipgrid.com.

What is flipgrid?

Flipgrid is the leading video discussion platform used by millions of PreK to PhD students, educators, and families around the world.

You can check it out that it was manage by microsoft

https://educationblog.microsoft.com/2018/06/flipgrid-microsoft-education/

I start up my termux I did a simply recon using Sublist3r and found a subdomain

Press enter or click to view image in full size

Store.flipgrid.com after visiting it, i got a redirect to flipgrid.bigcartel.com

Get Sadiq West’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Whith an erro like this.

Press enter or click to view image in full size

Which means that i can takeover the store page

The question is what is bigcartel?

Bigcartel is a unique online store, where you can sell your work, and run a creative business. Perfect for clothing designers, bands, jewelry makers, crafters, and other artists. Just like Shopify

I quckly sign up

Open a store with flipgrid.bigcartel.com

Now when ever a user visit store.flipgrid.com he got redirected to my claimed store page

Press enter or click to view image in full size

You know Noobs ain’t like duplicate

I quickly write the report to microsoft got a replay within 3Hrs of my report

Press enter or click to view image in full size

Do you wanna know what i get from microsoft? HOF

Press enter or click to view image in full size

Once again i was happy for that because i learn new things.

I hope 
Ed
 will add it on his repo because it was a new thing

https://github.com/EdOverflow/can-i-take-over-xyz/blob/master/README.md

Lesson learn:
Finding bugs on your target its base on how you think you can make it: don’t say “ i can’t do it on my smartphone” because it suck’s” to me: if you had Termux on your smartphone, its like you had your PC on your pocket

Most of my finding like XSS,LFI,SQL, e.t.c, i did it with my smartphone.

https://twitter.com/Sadiq_West

Hey 👋If you found my post usefull, show some ❤️ . You can now buy me a coffee!

https://www.buymeacoffee.com/sadiq

Thanks for reading

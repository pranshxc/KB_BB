---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-17_story-of-a-very-lethal-idor.md
original_filename: 2021-02-17_story-of-a-very-lethal-idor.md
title: Story of a very lethal IDOR.
category: documents
detected_topics:
- xss
- rate-limit
- sso
- idor
- command-injection
- password-reset
tags:
- imported
- documents
- xss
- rate-limit
- sso
- idor
- command-injection
- password-reset
language: en
raw_sha256: 571d7c198ec02a6a40e845eaf1b82a5da513a71ac4c235782fe51ec7615da562
text_sha256: e52fcc828db029ecd00bb959bc9160d383009679761cff947bde42fe4eabff85
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a very lethal IDOR.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-17_story-of-a-very-lethal-idor.md
- Source Type: markdown
- Detected Topics: xss, rate-limit, sso, idor, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `571d7c198ec02a6a40e845eaf1b82a5da513a71ac4c235782fe51ec7615da562`
- Text SHA256: `e52fcc828db029ecd00bb959bc9160d383009679761cff947bde42fe4eabff85`


## Content

---
title: "Story of a very lethal IDOR."
url: "https://vedanttekale20.medium.com/idor-that-allowed-me-to-takeover-any-users-account-129e55871d8"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["XSS", "IDOR", "Account takeover"]
publication_date: "2021-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3894
scraped_via: "browseros"
---

# Story of a very lethal IDOR.

Story of a very lethal IDOR.
Vedant Tekale
Follow
4 min read
·
Feb 17, 2021

852

6

Hello all! My name is Vedant, also known as Vegeta(on twitter). I’m a cybersecurity enthusiast, computer engineering student and a bug bounty hunter. Today I’m going to share one of my best findings with you. So little bit info about the target, it was a RDP let’s call it target.com for now. It was basically an online shopping website with lots of functionalities.

Press enter or click to view image in full size

So without any further ado, let’s get started :)

Phase 1:-

So as target.com had lot’s of functionalities for me to play with, I decided to create an account on it and start finding some basic vulnerabilities without doing any recon. So I turned on my burp and started to capture the requests. I didn’t find anything interesting in registration or login functionality, but the password reset and some other functionalities were vulnerable for rate limiting attacks. While creating an account on any website I enter my name as <h1>tester</h1> to check for HTML injection and XSS, so while creating an account on target.com I did the same and logged in and visited my dashboard but unfortunately the h1 tag didn’t execute. I continued to look for stored XSS in my profile section but any of those fields weren’t vulnerable. Then I went to address book section and there also I entered the same payload in all the fields and this time it worked on first name and last name fields :) Then I quickly changed the payload to a simple XSS payload(<svg onload=alert(document.cookie)>),clicked on save changes and yeah, the stored XSS triggered successfully! But then a question came to me, how can I exploit this? Then I remembered I encountered this kind of situation once before(If you read my previous blog then you know what I was thinking) I tried to exploit it by changing my first name and last name fields to a blind XSS payload and I waited for 2 days hoping that an admin would visit my profile but no, seemed like admin didn’t care about it that much. Then I tried to exploit the stored XSS with CSRF attack but it didn’t work either.

Me at that time😂

Phase 2:-

After trying all possible things there I almost gave up on that stored XSS and started to look for other vulnerabilities. I tested almost every vulnerability that I usually look for in any target but nothing worked :( at this point I was really frustrated. Then I visited that address book section again and that self stored XSS triggered again so I clicked on edit address to remove that XSS payload(it was triggering again and again and it was really annoying for me😂😂) and then I observed the URL it was like following,

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.target.com/my/addressbook/30916

After looking at it you probably have an idea what to do here, I changed that number from 30916 to 30915 hoping to see other people’s address book but no, a message appeared saying, “you are not allowed to perform this action”. Then I got to edit address section again and removed that XSS payload and this time I intercepted this request and then I observed the following parameter in the request,

Press enter or click to view image in full size

This time I changed the Id parameter from 30916 to 30915 and forwarded the request and message appeared saying Address changed successfully, but that stored XSS triggered again😂 but this time I knew exactly what happened, I changed someone else’s address book :) To confirm this I created another account and got it’s address Id and with my first account I went to edit address section and just clicked on save changes (keeping that XSS payload as it is), intercepted the request, changed the Id from my first account Id to second account Id, forwarded the request and this time it worked like a charm! As the Id was easily guessable and there was no rate limiting on any endpoint I could easily takeover any user’s account :)

So I went from self stored XSS →IDOR →Account takeover.

Press enter or click to view image in full size

As this was a RDP, sadly I didn’t get any bounty for this but I learned a valuable lesson from this finding. We have to get out of our comfort zone to achieve great things. If I didn’t even try to find that IDOR vulnerability I couldn’t have achieved this account takeover.

If you enjoyed reading this please do clap on it :) If you have any doubts regarding this write-up you can DM me here.

Until next time, good bye and happy hacking!

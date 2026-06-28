---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-12_how-does-my-recon-win-250-in-15-minutes.md
original_filename: 2019-09-12_how-does-my-recon-win-250-in-15-minutes.md
title: How does my recon win $250 in 15 minutes
category: documents
detected_topics:
- api-security
- oauth
- ssrf
- xss
- command-injection
- csrf
tags:
- imported
- documents
- api-security
- oauth
- ssrf
- xss
- command-injection
- csrf
language: en
raw_sha256: 7950bd6b68f33c03d15bb9f828ecc34d7ca60aa15f9d22e949af7dac2788ad87
text_sha256: 47a60532582604e4ce4a43758800e906123170b4a465afc5f297ade2e8d231bc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How does my recon win $250 in 15 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-12_how-does-my-recon-win-250-in-15-minutes.md
- Source Type: markdown
- Detected Topics: api-security, oauth, ssrf, xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7950bd6b68f33c03d15bb9f828ecc34d7ca60aa15f9d22e949af7dac2788ad87`
- Text SHA256: `47a60532582604e4ce4a43758800e906123170b4a465afc5f297ade2e8d231bc`


## Content

---
title: "How does my recon win $250 in 15 minutes"
url: "https://medium.com/@heinthantzin/how-does-my-recon-win-250-in-15-minutes-a1992508b911"
authors: ["Hein Thant Zin (@H3Lowr)"]
bugs: ["Open redirect"]
bounty: "250"
publication_date: "2019-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5035
scraped_via: "browseros"
---

# How does my recon win $250 in 15 minutes

How does my recon win $250 in 15 minutes
Hein Thant Zin
Follow
2 min read
·
Sep 12, 2019

175

2

Hi there again,

I’m Hein Thant Zin and just a noob bug hunter .Today, I’m going to share how recon helps me to find eazy bug in 
HackerOne
 ‘s Private program.

The story began when I was awarded my first bounty. I was really motivated to bug another bugs on h1 so then I got a private invitation and checked out it .

Sadly, there was only set 2 domains in scope for their program.

Let’s say the program name as http://reacted.com

The scope domains are

http://app.reacted.com

http://api.reacted.com

Alright , I was testing some common bugs like csrf, xss, other logical bug in main app domain but I didn’t find anything coz there was tested by other experienced hackers so you know very less chance for me to find valid bug there.

The next day, I remembered to do some recon for the program.So I went through github and checking all their repository. Suddenly, I found a payment api endpoint in their repo.

https://api.reacted.com/authorize?scope=payments&client_id=12345&redirect_uri=https://app.reacted.com

Get Hein Thant Zin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As you can see , redirect_uri parameter looks like interesting .

I changed https://app.reacted.com to http://google.com

Open redirect ? Nahh… I’ve got bad request response with 400 status.

Then I tried to bypass and the followings url was successfully bypassed and redirected to the site .

https://api.reacted.com/authorize?scope=payments&client_id=12345&redirect_uri=https://google.com

Also I’ve tested for ssrf and xss but failed .So I reported the bug and they rewarded me 250$ for this simple open redirect bug.

Press enter or click to view image in full size

That was happened in only just 15 mins, at last night I was spending at least 4 or 5 hours testing main app but got nothing. What is different between?

When you are doing bug bounty , you need to have the right approach for the target.

Don’t skip every recon steps , the more recon the more possible to win $$$$.

I hope you enjoyed this write up. Actually I’m not IELTS guys , execuse me for any grammatical mistakes.Btw u can find me there https://twitter.com/H3Lowr

Thanks for reading, Seee ya guys………….

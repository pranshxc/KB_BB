---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-28_how-i-was-able-to-get-free-money-via-sending-negative-tokens.md
original_filename: 2022-10-28_how-i-was-able-to-get-free-money-via-sending-negative-tokens.md
title: How i was able to get free money via sending negative tokens
category: documents
detected_topics:
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- business-logic
language: en
raw_sha256: 6eaa5f29ba828d7e3a7741eddac2236402f4c0b2e63505e9bad92089bce84751
text_sha256: e42e49bc7d6e5636503d1062d2e7bb8c3110603db18d82088d31cca042aebf1d
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to get free money via sending negative tokens

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-28_how-i-was-able-to-get-free-money-via-sending-negative-tokens.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `6eaa5f29ba828d7e3a7741eddac2236402f4c0b2e63505e9bad92089bce84751`
- Text SHA256: `e42e49bc7d6e5636503d1062d2e7bb8c3110603db18d82088d31cca042aebf1d`


## Content

---
title: "How i was able to get free money via sending negative tokens"
url: "https://0xm5awy.medium.com/how-i-was-able-to-get-free-money-via-sending-negative-tokens-1ed2e0e710e0"
authors: ["Mohamed Anani (@0xM5awy)"]
bugs: ["Logic flaw", "Payment tampering"]
publication_date: "2022-10-28"
added_date: "2022-10-29"
source: "pentester.land/writeups.json"
original_index: 1972
scraped_via: "browseros"
---

# How i was able to get free money via sending negative tokens

Mohamed Anani
 highlighted

Mohamed Anani
Follow
2 min read
·
Oct 29, 2022

380

3

How i was able to get free money via sending negative tokens

How i was able to get free money via sending negative tokens

Hello Awesome Hackers, I hope you all doing well!
My name is Mohamed Anani Or 0xM5awy.

In this Write-Up, we will talk about how I got free money by sending negative tokens

In the beginning, let’s explain how the website works. The site has two permission, the first is a user and the other is streamer. The site provides users to buy tokens in order to support streamers and streamers can also send tokens to anouther streamer, and this turns into money for streamers, so I tried to find a way to own tokens without buying them, and through this I will create a streamer account and send tokens for myself To infinity

I started to understand all the functions on the website until I found a function that allows the user to send private messages to streamroll. To do this, you must buy private messages for tokens. Unfortunately, I did not find any bug here. But what comes after this is the important thing :)

Get Mohamed Anani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I bought private messages in order to be able to message the streamer, it turned out that there are 3 functions inside the private chat

Send a private message to the streamer ( I didn’t find anything )
Upload an image or video file to the streamer ( I didn’t find anything )
Send token tips to the streamer (bug)

Now my eyes are shining and the first thing I think of is what will happen if I send negative tips? Like ( -5 , -10 , etc. ) so I did and the request was like.

POST /endpoint HTTP/1.1
Host: 0xM5awy.com
{"message":"negative tips","tokens":-100"}

ANDDDDDDDDDDDDDD BOOOOOOOOOOOOOOOOOOOOOOOOOM WE DID IT

100 negative token have been sent to streamer and I was have 150 token before now i have 250 :DDDDDD

Attack Workflow:

The attacker will have two accounts, one is streamer and the other is user
The attacker will buy private messages to talk to his streamer account
The attacker will send negative tokens to his streamer account
The attacker will send 100 negative tokens to the streamer, but his account will be increased by 100 free coins
The attacker can do this more than 100 times, so he will win more than 10K dollars

Impact

The attacker can get free coins infinitely, and these coins will turn into money. Imagine how much money he will earn :)

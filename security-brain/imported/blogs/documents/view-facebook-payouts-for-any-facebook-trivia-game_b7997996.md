---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-27_view-facebook-payouts-for-any-facebook-trivia-game.md
original_filename: 2019-06-27_view-facebook-payouts-for-any-facebook-trivia-game.md
title: View Facebook payouts for any Facebook Trivia Game
category: documents
detected_topics:
- mobile-security
- command-injection
- otp
- graphql
- information-disclosure
tags:
- imported
- documents
- mobile-security
- command-injection
- otp
- graphql
- information-disclosure
language: en
raw_sha256: b79979965df2a7ea1aceaad12234c7be0bca84742732fa505147156ba1691a5a
text_sha256: d07a389a7e7c63a651d793f234ab7d8423b0a42c07273860f02fe3ed5a2f5a76
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# View Facebook payouts for any Facebook Trivia Game

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-27_view-facebook-payouts-for-any-facebook-trivia-game.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, otp, graphql, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b79979965df2a7ea1aceaad12234c7be0bca84742732fa505147156ba1691a5a`
- Text SHA256: `d07a389a7e7c63a651d793f234ab7d8423b0a42c07273860f02fe3ed5a2f5a76`


## Content

---
title: "View Facebook payouts for any Facebook Trivia Game"
page_title: "View Facebook payouts for any Facebook Trivia Game - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/view-facebook-payouts-for-any-facebook-trivia-game/"
final_url: "https://philippeharewood.com/view-facebook-payouts-for-any-facebook-trivia-game/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2019-06-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5180
---

Posted on [May 27, 2019](https://philippeharewood.com/view-facebook-payouts-for-any-facebook-trivia-game/)

# View Facebook payouts for any Facebook Trivia Game

Facebook is testing trivia games in select countries. It seems I can pull the payout information for the full winner list for any game. It’s assumed that I shouldn’t be able to pull the winner list with full payout information which can allow me to collect overall payouts over time for repeat players.

![](https://philippeharewood.com/wp-content/uploads/2019/06/Screenshot-2019-06-26-at-7.08.19-AM-1024x491.png)

GraphQL Request  
  
`graphql?q=node(VIDEO_ID){trivia_game{id,trivia_game_payouts{nodes{user{id,name}, payout{formatted_amount}}}}}`

This lists payouts for any Facebook user that won the trivia game.

Initially, I assumed this to be intentional since the docID (when viewing in mobile IOS/Android) pulls the winners count and one of the winners. I have been looking online and I haven’t seen anywhere that allows me to pull the full winner list with the payout information.

A bonus to this is that from this list I saw in some of the games there were users cheating trivia games for double payouts (multiple accounts).

Facebook’s response

> Due to the limited nature of this issue, we don’t feel it has enough of a security impact to be rewarded via the bug bounty program.

Timeline

May 27, 2019 – Report Sent  
May 28, 2019 – Request for clarification by Facebook  
May 28, 2019 – Video sent  
May 28, 2019 – Confirmation of submission by Facebook  
May 29, 2019 – Further investigation by Facebook  
Jun 5, 2019 – Marked as informative

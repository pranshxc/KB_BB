---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-10_hacking-chesscom-my-journey-to-unlock-premium-bots-on-the-android-app.md
original_filename: 2023-05-10_hacking-chesscom-my-journey-to-unlock-premium-bots-on-the-android-app.md
title: 'Hacking Chess.com: My Journey to Unlock Premium Bots on the Android App'
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 7cbeadf73294b796bd75aa378b8f6639242b4d785d00da8524570fc13ef89730
text_sha256: d8d44e26f3a28103e2b47cc456a8a784f442823267c9d3ddbe203eeff43fdbb3
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Chess.com: My Journey to Unlock Premium Bots on the Android App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-10_hacking-chesscom-my-journey-to-unlock-premium-bots-on-the-android-app.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `7cbeadf73294b796bd75aa378b8f6639242b4d785d00da8524570fc13ef89730`
- Text SHA256: `d8d44e26f3a28103e2b47cc456a8a784f442823267c9d3ddbe203eeff43fdbb3`


## Content

---
title: "Hacking Chess.com: My Journey to Unlock Premium Bots on the Android App"
url: "https://medium.com/@icebre4ker/hacking-chess-com-my-journey-to-unlock-premium-bots-on-the-android-app-d8cac9d25094"
authors: ["Fr4 (@_icebre4ker_)"]
programs: ["Chess.com"]
bugs: ["Android", "Privilege escalation"]
publication_date: "2023-05-10"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1166
scraped_via: "browseros"
---

# Hacking Chess.com: My Journey to Unlock Premium Bots on the Android App

Hacking Chess.com: My Journey to Unlock Premium Bots on the Android App
Fr4
Follow
5 min read
·
May 9, 2023

204

4

Introduction

The rules of chess are simple: “Each player controls sixteen pieces of six types on a chessboard. Each type of piece moves in a distinct way. The object of the game is to checkmate (threaten with inescapable capture) the opponent’s king” (Wikipedia). However, throughout history, brilliant players like Paul Morphy, Mikhail Tal and Bobby Fischer have impressed the entire world with spectacular matches with ingenious strategies, unthinkable tactics and spectacular sacrifices.

I’m not a chess champion, but I still remember when my father taught me to play chess. I was about 6 or 7 years old, and he used a beautiful wooden chessboard, which my mother had given him for one of his birthdays, to explain to me how the different pieces moved on the 64 squares of the board. After a lot of years, I’m still here to play chess, (unfortunately) no longer on the wooden chessboard, but mainly on apps such as chess.com or lichess.

But this article is not about “How to checkmate the opponent’s king” but how I pwned the most famous mobile chess app outstanding: chess.com

Background

With over 100 million members and more than 17 million games played daily, chess.com is the foremost online chess gaming platform worldwide.
Furthermore, a couple of months ago, chess.com became the most popular free game in different counties on both the iOS app store and Google Play Store as described here.

Even though you can play on chess.com for free, it contains three types of premium plans (as shown in Figure 1).

Press enter or click to view image in full size
Figure 1 — Chess.com Premium Plans

One of the paid features is the “Bot Players”. Basically, you can play against bots that are similar to famous players like: Nakamura and Ian Nepo or against famous chess streamers, such as GothamChess and Anna Cramling.

Since this is a fairly recent feature, I decided to analyze the application code to see how this new feature had been implemented and if it was possible to bypass the subscription restrictions (since I had seen that they have a bug bounty program.)

Figure 2 — Premium Bots
Technical Details

In chess, like in reverse code engineering, having a strategy is important. It is not possible (with a limited amount of time) to understand every single line of code, especially if there are 50,000+ classes to analyze. (You need to know where you want to begin the static analysis.)

A quote from the second World Champion, Emanuel Lasker, goes:

”A bad plan is better than no plan at all.”

The initial strategy was to decompile the Android application with Jadx and search for the string of some bot player, such as ‘GothamChess’, in the hope of finding some reference inside the code (since the code is not obfuscated).

And here we go!

Inside the /res directory there was a JSON file with all the information about every bot player.

Press enter or click to view image in full size
Figure 3 — Jadx-gui

Inside the bots.json file are stored all the information and property of all bot players. For example the phrases used by the bot during the games, the ranking, if the bot was considered premium or not, etc.

Press enter or click to view image in full size
Figure 4 — bots.json file

At this point, I decided to set the “is_premium” property of every bot as “false,” repackaged the app and see if it worked.
By opening the patched app, I noticed that for a couple of seconds all bots were unlocked, but immediately afterwards, they were re-locked.
By intuition I thought of some kind of double-check. So, I decided to uninstall the app, switch off the Wi-Fi connection and reinstall the patched app.

Get Fr4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

… and all bots were unlocked.

But, wait wait…
At that point another sentence of Lasker’s came to mind:

“If you see a good move, look for a better one.”

So why not try to bypass the connection limit as well?

Analyzing the code, I spotted the method “is_premium()” inside the “PersonalityBotData.smali” file, in “smali_classes3/com/chess/net/model”.

In particular, patching the smali code of the is_premium() method in order to return always false (as shown in Figure 5), it is possible to unlock all premium bot players.

Press enter or click to view image in full size
Figure 5 — Patch of is_premium method

The result is that now you can play with all bots, without a premium account and with the internet connection ;)

Figure 6 — Unlocked bots
Conclusion

The following vulnerability can be mapped with the OWASP “Extraneous Functionality”. By patching the bots.json file inside the apk file, I was able to unlock a premium feature that was not intended to be available to a “free” user.

As shown, this vulnerability can be easily exploited through static analysis (it took me just 10 minutes), without having a chess.com account (since it is not necessary to login to play against “free” bot players) and on a non-rooted device.

09/03/2023: I found and sent my discovery to chess.com, as they have a bug bounty program.
11/03/2023: They replied to me, but unfortunately this type of vulnerability is out of scope :(
27/03/2023: They gave me three months’ subscription to Diamond membership
Chess.com vulnerable version: v4.5.13-googleplay (262093)

Oh and by the way, I played against Nakamura and GothamChess bots, and of course I lost; but I am happy with the draw by repetition against Anna Cramling bot (considering that she has a ranking of 2100)

That’s all folks. I hope you enjoyed the reading as much as I enjoyed finding this vulnerability! ;)

Press enter or click to view image in full size
Figure 7 — My game against Anna Cramling bot

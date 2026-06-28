---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-28_disclosing-facebook-page-admins-by-playing-a-game.md
original_filename: 2023-01-28_disclosing-facebook-page-admins-by-playing-a-game.md
title: Disclosing Facebook page admins by playing a game
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- business-logic
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- business-logic
language: en
raw_sha256: 9d161aa320cbd47ffe07d60217bc9a061c4fc86207f0fa3dea4bdd3c6d6919e5
text_sha256: 355f686ac04f1224174edac555e44d8102e8e0d77eb3ecb7d600b320b4327445
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Disclosing Facebook page admins by playing a game

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-28_disclosing-facebook-page-admins-by-playing-a-game.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `9d161aa320cbd47ffe07d60217bc9a061c4fc86207f0fa3dea4bdd3c6d6919e5`
- Text SHA256: `355f686ac04f1224174edac555e44d8102e8e0d77eb3ecb7d600b320b4327445`


## Content

---
title: "Disclosing Facebook page admins by playing a game"
url: "https://medium.com/@sudipshah_66336/disclosing-facebook-page-admins-by-playing-a-game-2b0f4ed082e4"
authors: ["Sudip Shah"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Information disclosure"]
bounty: "2,075"
publication_date: "2023-01-28"
added_date: "2023-01-31"
source: "pentester.land/writeups.json"
original_index: 1619
scraped_via: "browseros"
---

# Disclosing Facebook page admins by playing a game

Disclosing Facebook page admins by playing a game
Sudip Shah
Follow
4 min read
·
Jan 28, 2023

562

1

Hello there, It’s been a long time since I wrote any article on my resolved reports due to some internal problems so today I’m going to write about a bug in Facebook(now Meta) which I had found nearly 2–3 years ago . The vulnerability got resolved and fixed few months ago and I was seeking for some ways to bypass it so it took some time for the publish.

I found a medium impact privacy bug on Facebook where I was able to leak page admin’s personal account id by playing a game with them(Instant Games).

The Bug :
There was a feature in Facebook messenger associated with Facebook Instant games which allowed users to play games with their friends through the Messenger app . I was able to use this ability to create a game play between page and attacker which is an unintended thing to be and it resulted in disclosure of the page admin.
Though it requires some user interaction from the page like clicking the game and playing it , It is however a unique way of approach by an attacker to disclose the admin .

Impact:
It leads to page admin disclosure which is a privacy issue to the page. The impact is high because the page’s admin information is meant to be kept private and not shown to the public.

Affected app: CreatorStudio app version — 25.0.0.42.106

Setup:
Users: UserA , UserB , UserC , PageX
Environment: UserA is the attacker , UserB is any friend of UserA , UserC is the Admin of PageX and UserC uses CreatorStudio App to check inbox of PageX

Repro Steps:

1. UserA(attacker) sends a “Play a Game” message to UserB by going to www.messenger.com > www.messenger.com/t/{userB_id} and clicking on “ Play a game “ option .
2. UserA then intercepts the request and clicks on any game .
3. Now a POST request is sent with doc_id=3037811092958141 where UserA replaces “contextSourceID “ , “context_source_id” and “thread_id” with page_id of PageX and forwards the edited request .
4. Now UserC(PageX admin ) opens CreatorStudio app and Checks the Page inbox and clicks on the Game to play it .
5. A game session between the attacker and Page is now created .
6. The page plays one round . Then the score is sent to attacker(UserA) by UserC instead of PageX. Attacker(UserA) will receive one message and notification that {page_admins_personal_id} played the game . Thus it leads to page admin disclosure as the game is played by the admin_personal_id instead of Page_id .

Press enter or click to view image in full size
vulnerable parameters

Here is the poc : https://youtu.be/Yt6bc41dSec

After some time of the report the Instant Games feature in messenger was removed as they were switching to Facebook Gaming Tab .
You can check out this article by Leo to learn more about the migration here : https://www.facebook.com/fbgaminghome/blog/instant-games-platform-update
Engadget and Business-Standard has also covered this story .

Timeline:

Get Sudip Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Initial report sent: August 23, 2020
Fb asked for more info : August 29, 2020
Additional info sent: August 29, 2020
More info sent(I found out that it was doing something with the timestamps which resulted in the bug reproducible only when the request is modified within 17–20 seconds): September 11, 2020

Press enter or click to view image in full size

Fb team asked for more info: September 15, 2020
Sent more info with updated poc: September 15, 2020
Pre-triaged: September 21, 2020
Triaged: September 25, 2020

Press enter or click to view image in full size

Bounty rewarded(without fix): 500$ on January 15, 2021

Press enter or click to view image in full size

Bounty dispute : January 15, 2021
Bounty rewarded again : 1500$ on March 5, 2021

Press enter or click to view image in full size
I was amazed by this message xD

Fixed: March 6, 2021
Asked for public disclosure: May 10, 2021
Facebook working on a more holistic fix: September 2, 2021

Press enter or click to view image in full size

Fixed finally: November 29, 2022

Press enter or click to view image in full size

Resolved: December 7, 2022

So in total, I received a bounty of 500$ + 1500$ + 75$ = 2075$. I was thrilled to receive the bounty notification at that time, as it allowed me to purchase a phone of my own choice which helped me testing further .I will try more and learn more to find good bugs in the upcoming days.

See ya hehe xD

Thank you for taking the time to read my article. Have a great day! < 3

You can follow me on
Twitter : https://twitter.com/kn1ght_yagami
Facebook : https://www.facebook.com/sudipshah505/
Instagram : https://www.instagram.com/sudip_shah_582/
LinkedIn : https://www.linkedin.com/in/sudip-shah-714852211/

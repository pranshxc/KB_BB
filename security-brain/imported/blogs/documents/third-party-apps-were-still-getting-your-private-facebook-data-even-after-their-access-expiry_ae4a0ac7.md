---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-20_third-party-apps-were-still-getting-your-private-facebook-data-even-after-their-.md
original_filename: 2021-05-20_third-party-apps-were-still-getting-your-private-facebook-data-even-after-their-.md
title: Third-Party Apps were still getting your private Facebook data even after their
  access expiry.
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- api-security
- supply-chain
language: en
raw_sha256: ae4a0ac783127464d9d02348e32ee5030a71ce16554b34958f7b5267a274bc96
text_sha256: 1e91d7c2d87ea4616483fed844669b5ffa223a62cdabac5d25938a57b8be5e6d
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Third-Party Apps were still getting your private Facebook data even after their access expiry.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-20_third-party-apps-were-still-getting-your-private-facebook-data-even-after-their-.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `ae4a0ac783127464d9d02348e32ee5030a71ce16554b34958f7b5267a274bc96`
- Text SHA256: `1e91d7c2d87ea4616483fed844669b5ffa223a62cdabac5d25938a57b8be5e6d`


## Content

---
title: "Third-Party Apps were still getting your private Facebook data even after their access expiry."
page_title: "Third-Party Apps were getting your private Facebook data even after their access expiry. | by Samip Aryal | InfoSec Write-ups"
url: "https://infosecwriteups.com/third-party-apps-were-still-getting-your-private-facebook-data-even-after-their-access-expiry-6e4be4880e6e"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2021-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3637
scraped_via: "browseros"
---

# Third-Party Apps were still getting your private Facebook data even after their access expiry.

Third-Party Apps were getting your private Facebook data even after their access expiry.
Samip Aryal
Follow
8 min read
·
May 20, 2021

237

3

…

Press enter or click to view image in full size

Hello, I am Samip Aryal from Nepal and this writeup is about my 2nd valid vulnerability report at Facebook Bug Bounty Program.

I found that the access of Third-Party application (that it gained via ‘Login with Facebook’ functionality) was not properly being expired (even after 90 days of inactivity); when looking up friends of a given user. Specifically, if the target user’s app access had expired but the source user’s had not, Facebook would’ve still returned data about the target user to the Third Party app.

To understand it clearly; let us move toward the complete story of this vulnerability.

…

A
bout a year ago; while I was randomly browsing an app named ‘Smule’ (where users can do karaokes), I reached to ‘Facebook Friends’ section inside the app where it was showing the list of my friends who were also using that app and who had also provided the required access(email, friend list data) from their Facebook account to that Third-Party application i.e. Smule via ‘Login with Facebook’ functionality.

So, as I was looking at the names of my friends; I got the profile of one of my recent friends named Prabesh; there. I clicked and opened his Smule profile and saw there that his latest duet was from about two years ago from back then. Moreover, he had had several duets before that in a sort of a continuous manner. This means; there was kind of a similar subtle gap between each of his published duet periods but it suddenly got discontinued there about two years ago from that frame of reference. So; I didn’t see any kind of interactions from him in that app in recent periods. Hence; I anticipated that maybe his Facebook account access has expired for his Smule account due to over 90 days of inactivity.

And suddenly the best part which excited me back then was the fact that we became friends on Facebook just about a week ago. So; I was like:

Hence, Eagerly I asked Prabesh to go to his ‘Apps and Websites’ security settings inside his Facebook account towards the ‘Expired’ section. And he sent me the screenshot of it:

After seeing this; I was like:

→You may ask, ‘Why… I mean; what is so interesting about these things?’

Well, look at the top of the screenshot picture. There you can clearly see an indication telling something like this:

‘These are apps and websites that you’ve used Facebook to log in to. They can receive information that you chose to share with them. Expired and removed apps may still have access to information that was previously shared with them, but they can’t receive additional non-public information.’

So, here some of you may have already understood what fishy was going on. Still; let me make it clear using this indicative flow of events that happened:

UserA >> Gives his data access including the private friend list data to the third-party app via ‘Login with Facebook’ functionality >> Stops using the third-party app >> over 90 days passes >> Access for the third-party app expires >> Now, it shouldn’t be getting any new private data from UserA’s Facebook account >> Then, UserA becomes friend with UserB >> UserB opens his account in the same third-party app >> UserB sees UserA in the ‘Facebook Friends who also use this app’ list

…

This timeline of events made me ask a question:

‘How was the Third-Party app showing UserA in the UserB’s friend list inside the app even though it wasn’t getting any friend list data from UserA to confirm that UserB actually is a friend with UserA as UserA’s Facebook access was already expired for the app way before they two became friends?’

This question was the main plot of the story that led me to think that ‘Maybe Facebook is providing data to Third-Party Apps even after their expiry and thus that Third-Party app got the latest friend list data of UserA even after being expired which included UserB inside of it which made it confirmed to show there that both are friends with each other’.

WAIT A MINUTE…

If you look at the question above; you may notice something and ask;

‘ Hey!, But the Third-Party app was still getting friend list data from UserB’s Facebook account which was active for it, and thus it may be showing UserA in UserB’s ‘Facebook Friends’ section inside the app because it got UserA inside the friend list data of UserB which it fetched via UserB’s Facebook account access? ’

I too asked this question to myself for a moment but suddenly a potential question popped up:

‘How can the Third-Party app even know surely that the user it picked from the Facebook Friend List data of UserB uses this app too?’

So, this can only happen when the Third-Party App has UserA’s Facebook account access too from which it can confirm that he uses this app too and the access here for this third-party app is his ‘friend list data’. So, it gets the friend list data from UserA’s Facebook account as a result of still having access from which it also confirms that UserB is a friend with UserA.

Hence, only after getting the Facebook friend list data from both the users’ Facebook accounts, it can confirm that both the Users use this app and are friends with each other on Facebook too. This finally will allow the app to show UserA in UserB’s ‘Facebook friends who use this app too’ section.

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Apparently, this was some satisfying thought for me but it wasn’t enough to prove the technicality behind it. So, I found a way to experimentally test this hypothesized workflow.

…

For this, I made two dummy Facebook accounts that I used to log in to the Third-Party app. So, initially; the two User accounts weren’t in friendship with each other. Then, I went to the ‘Apps and Websites’ section in Security Settings from the first Facebook account, and after that; I went to the active-apps section; clicked on the ‘Edit’ option at the side of that connected Third-Party App, and toggled-off the option for providing additional friend list data to the app. Now, only after this; I made both the User accounts friend with each other on Facebook.

Now, look at this setup environment here; it has the same analogy to the expired one case where the Third-Party app is getting friend list data only from one User but isn’t getting it from the other.

So, I went to the ‘Facebook Friends’ section inside the Third-Party app and was amazed to see that this time; the Third-Party app wasn’t showing each other in the ‘Facebook Friends list’ section inside the app even if it was still getting the Friends List data from the second user account which included the first user account inside the list.

Hence, I was somehow satisfied to see my predicted hypothesis regarding this workflow algorithm came true because now, I could surely confirm that the Third-Party app needed the friend list data from both users' Facebook account including each other in the friend list of each one’s. So, In a nutshell; it was confirmed somehow that Third-Party apps were still getting User’s private data from their Facebook account even after its expiry.

I was like:

Hu! Finally…

…

[BUT] There still was one challenge remaining which was to report this vulnerability in a way so that I could make Facebook Security Team members understood it clearly and get Satisfied as I was.

[(Unnecessary Portion describing possibility) Yah! I know I could’ve simply made a simple app and using the third-party plugin from developers.facebook; I could’ve requested ‘Login with Facebook’ functionality on my app, and after it would get approved & would’ve become live; I just needed to log into that app using my Facebook accounts and provide the requested Facebook data access to the app. Then, just wait 3 months without using that app to make the access expire for it and just show them that ‘Hey, look I am still getting the users data in my app admin panel even after its expiry for their Facebook accounts’ as a POC. Yes, this might have been possible but this was a very long nasty process just for a POC.]

So….., with just every single piece of information, I had about this vulnerability; I reported it simply in the descriptive way as above to the Facebook Security team including a couple of POC videos to show how was I convinced/testing and all.

…

Here,

the reply tread went something like this (Though it’s a bit melodramatic😂):

Press enter or click to view image in full size
Report Closed 4 Times Consecutively in a row

Then,

Absolutely not like this😂 but still tried my part to make them agree.

Finally..a hope; 😌

FIRST BETTER REPLY FROM THEIR SIDE

Now, the difficult period arrives;

FOR 4 MONTHS (the last one’s a joke though)

But Again;

Press enter or click to view image in full size
SIMILAR REPLIES -UPTO WAY LONG AFTER FIX

And suddenly the CLIMAX:

REWARD MESSAGE FROM FACEBOOK

Finally, After a year of investigation and a full of 42 crowded reply exchanges, I got this message just today (on the day of this write-up publication).

…
Thank you for reading this write-up about a vulnerability I found on Facebook. I hope you’ve enjoyed it. If you have any suggestions/queries, I’m available on Facebook/ Instagram.
…..

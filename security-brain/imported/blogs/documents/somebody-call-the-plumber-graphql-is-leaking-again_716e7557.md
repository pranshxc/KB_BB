---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_somebody-call-the-plumber-graphql-is-leaking-again.md
original_filename: 2021-02-28_somebody-call-the-plumber-graphql-is-leaking-again.md
title: Somebody Call The Plumber, GraphQL is Leaking Again…
category: documents
detected_topics:
- api-security
- graphql
- command-injection
- automation-abuse
- information-disclosure
- webhooks
tags:
- imported
- documents
- api-security
- graphql
- command-injection
- automation-abuse
- information-disclosure
- webhooks
language: en
raw_sha256: 716e75576fc0935a72e3287095ae6c55c2473c86b4368cb188daf65dcc9badfe
text_sha256: 0fa1241e0c944a93ea213dca51d8c0dead7061fa214d8306fa8f23918a93dcb6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Somebody Call The Plumber, GraphQL is Leaking Again…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_somebody-call-the-plumber-graphql-is-leaking-again.md
- Source Type: markdown
- Detected Topics: api-security, graphql, command-injection, automation-abuse, information-disclosure, webhooks
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `716e75576fc0935a72e3287095ae6c55c2473c86b4368cb188daf65dcc9badfe`
- Text SHA256: `0fa1241e0c944a93ea213dca51d8c0dead7061fa214d8306fa8f23918a93dcb6`


## Content

---
title: "Somebody Call The Plumber, GraphQL is Leaking Again…"
url: "https://n0ur5sec.medium.com/somebody-call-the-plumber-graphql-is-leaking-again-654bf1a38d26"
authors: ["N0ur5"]
bugs: ["Information disclosure", "GraphQL"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3857
scraped_via: "browseros"
---

# Somebody Call The Plumber, GraphQL is Leaking Again…

1

Somebody Call The Plumber, GraphQL is Leaking Again…
N0ur5
Follow
9 min read
·
Feb 27, 2021

66

2

Hello Everyone, I have a story for you today. It primarily will be about a GraphQL vulnerability I was recently awarded for though a public program hosted on BugCrowd’s platform. This program doesn’t allow for disclosure so I may be redacting or editing where needed to stay within “the rules” :). It also will touch on a little strong-arming I felt I had to do, to ensure my bounty payout was appropriate.

So to quickly get everyone up to speed… GraphQL is a technology that allows for database query and manipulation via API interactions. It was developed by Facebook and used only internally until 2015 when they released it to the public. It is incredibly common to come across in larger companies nowadays. BugCrowd is a company that middle-mans the interaction between bug bounty hunters and organizations who pay BugCrowd to essentially play referee. Those are both extremely high level definitions and you can do plenty of research on them independently should you choose.

I don’t always have a ton of time to dedicate to bug bounty programs nowadays, I work as a pentester/threat hunter. I’m a dad, a husband, a gamer, a DIY’er… it’s just difficult to fit everything in to be honest. So when I do try to spend sometime on a bounty, it typically ends up being very recon heavy. Meaning I’m just trying to find portions of the web application that maybe haven’t been explored as much. Or in the case of todays example, portions that shouldn’t be accessible to the public at all…

While poking around on the target’s primary “.com” domain, I looked in my Burpsuite Target tab and noticed the “/api” endpoint along with its child endpoints. Most of these were discovered passively while just browsing and working through “normal” functions on the website. A couple of them I also discovered while directory brute-forcing to uncover as many API endpoints as I could.

Semi-redacted as usual

Each of these different child API endpoints for the most part limited the data we could obtain by requiring authentication. Others were giving us data that simply was used to propagate the website interface (things like avatars, side bar logos, etc). In other words, nothing of use to me as a bug hunter. At least vulnerability-wise.

I did however notice that most of these endpoints leveraged GraphQL queries…

If there is one thing I have learned about GraphQL, it is that it’s rarely set-up correctly initially. Many companies have had unsecured GraphQL endpoints floating around and called out on Bug Bounty reports. It’s understandable considering the complexity of GraphQL on top of the existing technologies that it aims to bridge. But once I noticed this, I started down my GraphQL testing path. I’ve tested GraphQL endpoints in a couple other public programs and a private program and never quite found anything but as previously mentioned, I’ve read enough bug reports to know it was only a matter of time! One that can help keep you motivated is the one where HackerOne paid out $20,000 to a bounty hunter who found a bunch of sensitive data leaking from their GraphQL instance.

Press enter or click to view image in full size

Anyways… my first step is typically to try to run introspection queries against the endpoints. If successful; an Introspection query in GraphQL will give you a ton of information about the “schema”/data configuration. Things like what type of information exists, how it all is connected, what format it accepts, how to query the data, and how to manipulate the data.

Almost every article you will read about testing a GraphQL instance will tell you to look for the following endpoints:

/graphql
/graphiql
/graphql.php
/graphql/console

And if you use the GraphQL “InQL Scanner” BApp(add on) in BurpSuite, all you have to do is type out the URL you want to send an introspection query to. However I think it is important to realize that just because those endpoints listed above indicate the presence of GraphQL, doesn’t mean it should be considered an all-inclusive list of endpoints to run introspection queries against if you suspect a target is running an instance. For example… you can indeed see some /graphql endpoints in my screenshot above… But the endpoint I actually got juicy details from when running the Introspecition query was not labeled “graphql” at all!

I don’t want to/can’t really say the actual endpoints name to keep confidentiality squared up with the target, but we will call it “/api/vulnerable” to keep things easy… just know that graphql was not the name of the endpoint since that is the point I’m ultimately trying to make. So I send https://[redacted].com/api/vulnerable over to the InQL Scanner in Burpsuite and sure enough… tons of interesting looking data queries are potentially available based on the queries supported by this endpoint. I quickly send a query called “customer.query” over to the Repeater tab and fill in the “ID” parameter with just a guess of “1” to see if any user data comes back but I’m basically given an error that says the ID format is not accepted.

Press enter or click to view image in full size
I also see a part of a SQL statement, and that “Psycopg2” is in use. Which tells me they are using Python, and PostgresSQL most likely.

Ok so I’m looking for a UUID… probably will be too complex to guess one… So I look at the other possible queries available from the initial introspection query I ran and I see “customers.query” (note that customers is plural in this case). Well sheesh, why didn’t I just start with that one! haha… I fire that query away which only required two parameters… number of results per page… and what page to query…. How easy is that?! I don’t have to guess anything, so hopefully the query runs without authentication…

Press enter or click to view image in full size

Well I surely didn’t “hack” anything. But I did just find a bunch of sensitive information that I don’t think I should have! Next logical step was just to explore the other queries I was able to play with. There was some more sensitive information on various partners and users related to the platform in other ways (kind of like contractors). I found some API keys along with external webhook urls as well but those urls were out of scope so I wasn’t able to really do much besides mention them in the report on BugCrowd.

Get N0ur5’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I compiled my data, tried to drive impact as much as possible, and shipped the report off. While selecting the category I believed that this vulnerability would fit in to I noticed this was likely to be considered a “P1” severity based on the fact it results in “Sensitive Secrets” leaking. I then looked at the programs payout on P1’s and quickly realized I could be getting a decent payout if all went well.

I submitted the report on a Saturday night so anxiously awaited the review that I assumed wouldn’t happen until Monday….

Press enter or click to view image in full size

Monday arrived and most of the day passed before I simply got a response that the Proof of Concept I sent in the report was not producing the same results when they ran it. I sent some alternative payloads that I knew would circumvent the copy/paste formatting issue that I believed was the cause of the original Curl proof of concept I sent not working. Then more time passed and I didn’t hear a word. Around midnight on Monday a BugCrowd employee jumped on the report to what I assume was nudge the target to move forward on the report. I woke up Tuesday to the following from the target…

“The finding was legitimate and as a result we pulled the site. The data in use was fake, however we do recognize the researcher would not have known that and we are evaluating the bounty. We appreciate the good work, and will be awarding shortly.

Thanks.”

Inside my gut said that the data didn’t seem fake. It seemed like I was digging around in production. And if the data was fake, why pull the page entirely and so quickly? Something didn’t add up.

I pivoted back into recon mode… I took a few customer names off of my query from earlier and popped their names in to the Facebook and LinkedIn search bars…. Boom! I was finding numerous people, whos names and locations matched perfect with the names and locations in the PII… So I fought back on the report thread with a screenshot of some of the users on Facebook whos names and towns side-by-side-matched-up to the PII from my “customers.query” proof of concept. What can they say now? I have their email address, phone number, and heck some of their Facebook pages now too. I’ll just go ask the users themselves if they use the target web site… haha ok ok I’m just kidding about doing that part.

The last thing I wanted to do was get into a situation where I was calling out a program on BugCrowd for lying about this so I tried to word things as nicely as possible in the event there was some genuine misunderstanding on their side. And again… I waited…

Press enter or click to view image in full size
I should probably try to watch Narcos again. Seems like a good show. Subtitles get exhausting sometimes though.

Two days later, I gave them a nudge. They responded to let me know my payout was coming but never really responded to my comments about the data being real. But I think the delayed response came from some internal confusion about the data for sure. Ultimately they just slapped a “p3” severity on it (“Moderate” severity — apparently there is a “p3” version “Sensitive Secrets Disclosed” 😕 I’ll take it though.. lol) and sent me my bounty, with some kind words.

Press enter or click to view image in full size
…annnnd off to buy some home gym equipment 😃

To conclude: A few points really…

Monitor your web logs. This ideally means putting a SIEM in place and ensuring web server logs are being forwarded for log correlation. I can’t image the madness that would commence from dumping web server logs in a public bug bounty target into a SIEM though. I suppose since most programs ask that you include a special string in the User-Agent header, you could drop/filter out all the bounty traffic that way. But I’m sure you would still get pummeled with people who don’t read the Rules of Engagement or know how to configure their tools to modify the UA header. However you could then in theory use a WAF to blacklist IP’s with malicious behavior who are obvious rookie testers, allow the proper User-Agents through, and monitor logs from the web server that don't meet either of those two categories. Just an off-the-top thought, but something along that logic might make sense. Of course, in that case an attacker could just use a bug-bounty accepted user-agent and go-unmonitored while actually being malicious. See how quickly this turns into cat-and-mouse!?
There are very few reasons to allow introspection queries to be ran by public users on GraphQL endpoints. Yet I believe it was and possibly still is the default setting in a GraphQL instance 😐. Dont trust default settings on anything. Read the “security concerns” section of everything you implement, ESPECIALLY if web facing.
In terms of bug bounty hunting, my own logic is that “Recon Is King”, just like many others. Of course I’ve heard the opposing argument from the P1 Warriors that sometimes just being thorough with what’s in plain sight is a better option. It is all based on your own strengths really and you’ll end up molding your own methods over time from what I’ve seen on my own journey as well as others. I’ll just say this… people have put together extensive reports filled with complex steps for a couple hundred bucks. I found an open endpoint and spent maybe an hour querying it to find impact before submitting a bug with a 2k payout. I’m not saying money should be the main motivator, it makes it harder to learn if that is your primary driver anyways. But I am saying, even if you don’t love recon deep dives, they clearly have some value! $2000 in this case lol.

*No hacking occurred during this bounty 😉.*

Until next time!

N0ur5

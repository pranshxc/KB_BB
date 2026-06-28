---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-06_how-we-breached-zdfheute-live-on-television.md
original_filename: 2022-12-06_how-we-breached-zdfheute-live-on-television.md
title: How we breached ZDFheute live on television
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: e301d800c9c699b110a8df46208fd51a4d666a4d5fa060f9513f63d8a0beea86
text_sha256: 388c4a705bf9fd7fe4b74420bfddcaefa4fbd5a09c1c2124aed3d82ae9f5bbc4
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How we breached ZDFheute live on television

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-06_how-we-breached-zdfheute-live-on-television.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `e301d800c9c699b110a8df46208fd51a4d666a4d5fa060f9513f63d8a0beea86`
- Text SHA256: `388c4a705bf9fd7fe4b74420bfddcaefa4fbd5a09c1c2124aed3d82ae9f5bbc4`


## Content

---
title: "How we breached ZDFheute live on television"
url: "https://medium.com/@cybercitizen.tech/how-we-breached-zdfheute-live-on-television-7530509b91be"
authors: ["CyberCitizen"]
programs: ["Zweites Deutsches Fernsehen"]
bugs: ["Information disclosure"]
publication_date: "2022-12-06"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1810
scraped_via: "browseros"
---

# How we breached ZDFheute live on television

How we breached ZDFheute live on television
CyberCitizen
Follow
4 min read
·
Dec 6, 2022

95

Press enter or click to view image in full size
TV test pattern

In summer this year, we came across some security misconfiguration in Germany’s biggest — and one of Europe’s largest — Television networks named ZDF (Zweites Deutsches Fernsehen). This misconfiguration allowed us to access the internal communication while live on air, which was used to define the content of the show.

But in order to get a further understanding about this and its potential impact we will start off chronologically.

9th of July, 2022: We were watching a recording of the TV program ZDFheute via YouTube. This program is a format where a current topic is discussed live on TV, together with invited experts. Viewers get the chance to raise questions directly to the experts on live television via YouTube chat, email and other channels.

As you might have already guessed, this direct viewer interaction demands some sort of moderation to filter out inappropriate comments before they get redirected to the host of the show live on-air to read out loud and ask on behalf.

During this episode, the camera showed the moderators laptop screen for a split second. Checking out this frame further, we noticed it displayed an open browser with an opened Google Docs editor.

We navigated our browser to this link and were presented with that very same Google Document. No Authentication was needed. The document was utilized to communicate between the editorial staff and the TV show host live on air and delivered comments from the audience.

Press enter or click to view image in full size
First Access to ZDFheute Google Document

Having checked our permissions, we had full read and write permissions and could also take part as an editorial staff from now on, making news.

Additionally, we could also see the entire version history of that document, dating back roughly 2 years by using our Google account after signing in. This allowed us to see anything that was typed within that document for those past 2 years, so each ZDFheute show since then, because no one took care of removing the old content.

These contained personal information of the viewers, such as full names and email addresses, as well as personal commentary by the editorial staff.

10th of July, 2022: After we gathered all evidence and information in order to properly evaluate the risk and impact, we reached out directly to ZDF via email with a detailed description. We didn’t receive any response.

A few weeks passed by during which we were joining the editorial staff live on air, almost every evening that the ZDFheute live show took place.

Get CyberCitizen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We could observe several people (with full names) being actively working in that document, adding names and comments of viewers who were posting questions via social media or via email.

Particularly notable were the shows on a flooding causing many deaths and destruction in central Germany:

Press enter or click to view image in full size
ZDFheute live on Flood in Germany

Another one was on the Russian war in the Ukraine in which we could have manipulated the communication, comments and therefore possibly news being released live on air:

Press enter or click to view image in full size
ZDFheute live on War in Ukraine

During such tense times, imagine what a false announcement on the Russian war on Germany’s biggest TV channel could have possibly lead to.

Which is why the “Media and Culture” is classified as Critical Infrastructure (KRITIS) in Germany with especially high requirements on security.

After having waited for a couple of weeks without any response or action taken overall, on 27th of July, 2022, we decided it is time to reach out to more people at ZDF, and eventually contacted their Data Protection Officer.

He took swift action and made sure the document was no longer reachable publicly over the internet and briefly thanked us for the report.

Thoughts on the root of the problem:

The issue of publicly open Google Documents and files of all sorts is a commonly known problem. There are even specific search engines focusing on these files.

It is no coincidence that the latest OWASP TOP 10 from 2021 has ranked “Identification and Authentication Failures” as the number seven issue in web applications and “Security Misconfiguration” as the fifth amongst the most common security issue categories.

Press enter or click to view image in full size
OWASP Top 10:2021

Never think of URL that supposedly no one else knows about and which does not require further authentication, as a private place. Anything that is publicly available on the internet can and will be found, sooner or later.

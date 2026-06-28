---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-01_yet-another-unexpected-hack-for-bounty.md
original_filename: 2019-03-01_yet-another-unexpected-hack-for-bounty.md
title: Yet Another (unexpected) Hack for Bounty
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 0fad640821b456c7247a01cccf9e224f93a092b0c5d98e64d161b781b28ac0ec
text_sha256: e186aced09f4002a1aed2f9a3a9f4b5cb5ca009f36002d11637ddfee1cf7f4c5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Yet Another (unexpected) Hack for Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-01_yet-another-unexpected-hack-for-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0fad640821b456c7247a01cccf9e224f93a092b0c5d98e64d161b781b28ac0ec`
- Text SHA256: `e186aced09f4002a1aed2f9a3a9f4b5cb5ca009f36002d11637ddfee1cf7f4c5`


## Content

---
title: "Yet Another (unexpected) Hack for Bounty"
url: "https://medium.com/@pumudu88/yet-another-unexpected-hack-for-bounty-295cee0ecc24"
authors: ["Pumudu Ruhunage"]
programs: ["Sli.do"]
bugs: ["Information disclosure"]
bounty: "150"
publication_date: "2019-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5384
scraped_via: "browseros"
---

# Yet Another (unexpected) Hack for Bounty

Yet Another (unexpected) Hack for Bounty
Pumudu Ruhunage
Follow
4 min read
·
Mar 1, 2019

61

Press enter or click to view image in full size

I
always wanted to start blog on medium but lacked that interesting story to begin with. So finally here I am with something interesting to share

I did my first web hack back in 2014 and got my first Bounty for disclosing a vulnerability. After plunged into my day job, hacking slowly slipped away from me. My last (kind of) hack was an instructable to unlock passive coded key locks in 2016.

This story is about my second web hack which got me a bounty offer. Story begins with an event I participate early January 2019. During the event, event organizers used Slido to get audience participation.
It’s an awesome app to get questions,comments,opinions from audience. Making events,meetings more interactive and less boring.

Also using slido can’t be more simple. you’ll get an event code from event organizers.Then you just need to open up sli.do website from whatever the device you are using, enter the event code in home page and that’s it!! Now you can start engage with the presenters by asking questions/comments etc. I was fascinated by this simple yet awesome idea which made events and meetings much awesome.

Press enter or click to view image in full size
Sli.do home page

Questions will remain anonymous and will not be publicly viewable

Hmm, so this was the initial message greeted when I log into the slido event for the first time. Event organizers has enabled the moderator approval feature. So inputs from audience are not viewable by the audience until it’s approved by a moderator(event organizers). By instinct I was curious what fellow audience were asking from presenters and how slido implemented this feature. So I open up the browser console just to give ‘hack’ a try. ;)

By looking at DOM elements it was obvious that whenever someone posted a question its pushed to all end users(audience) and removed, if moderator not yet approved. Not the ideal way to handle this usecase. With this in mind, wrote a small JS snippet in browser console to capture any mutation in the div element whenever a question posted. (Hint for developers: Easiest way to do this is by, ‘mutation observers’). Once you capture the DOM element mutation event using observer, it’s just matter of console log whatever the details required from the captured elements.

Get Pumudu Ruhunage’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This will enable to view questions posted while anonymous authors still remain anonymous.

Press enter or click to view image in full size
console output with all the questions

After around 15 mins of fiddling I managed to get all questions posted real-time printed in browser console as log output.

After the event ends, there was nothing much interesting in console logs. But hack I unexpectedly found was really interesting. This is a feature breaking vulnerability in slido. So I thought of inform my findings to slido developers. Deep down I wanted to know how much my 15 mins of fiddling worth to them as well.

So I sent an email with my findings including steps to reproduce, to slido security mailing group. After around day or two, got following reply.

Press enter or click to view image in full size
Cool!! $150 for 15 min hack

Knowing they have estimated the vulnerability disclosure for $150 bounty alone was an achievement. Unfortunately, I’m living in an “awesome” country where government has banned paypal accounts from receiving money. There are few “gray workarounds” for this. But didn’t felt like going through those for $150. (May be I’m getting too old and responsible now :D )

After few back and forth emails we still couldn’t sort a common platform for transaction. Mostly because limitations where I live. Anyhow, I got bounty offered for my findings and that was my objective. So I sent following email.

Press enter or click to view image in full size
Sometimes it’s just enjoy hacking. Hope Slido development team enjoyed their Pizza treat :D

Hacking shouldn’t be an unpleasant experience for either businesses or hackers. Slido is an awesome company which accepts this fact as well. In fact sites like hackerone promotes hackers and companies to work together. Not all hackers hack just for money, at least in the beginning. It’s an addictive art with great sense of accomplishment when they find a good exploitable vulnerability.

Update: I ended up receiving generous gift from Slido :)

Press enter or click to view image in full size
Thanks Slido :)

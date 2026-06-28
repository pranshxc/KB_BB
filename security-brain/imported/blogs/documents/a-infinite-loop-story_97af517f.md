---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-29_a-infinite-loop-story.md
original_filename: 2018-08-29_a-infinite-loop-story.md
title: A Infinite Loop Story.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 97af517ffb1c46ce4ce613b0ca179d285320dcf23056b35ecfae6d7735aab274
text_sha256: 605c8bc8f7b8ea8920a1cefcd1231d26ac7db3da95789ff2096248ab4bf12de5
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# A Infinite Loop Story.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-29_a-infinite-loop-story.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `97af517ffb1c46ce4ce613b0ca179d285320dcf23056b35ecfae6d7735aab274`
- Text SHA256: `605c8bc8f7b8ea8920a1cefcd1231d26ac7db3da95789ff2096248ab4bf12de5`


## Content

---
title: "A Infinite Loop Story."
url: "https://medium.com/@D0rkerDevil/a-infinite-loop-story-f2bc05771a88"
authors: ["Ashish Kunwar (@D0rkerDevil)"]
bugs: ["DoS"]
bounty: "100"
publication_date: "2018-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5732
scraped_via: "browseros"
---

# A Infinite Loop Story.

A Infinite Loop Story.
Ashish Kunwar
Follow
2 min read
·
Aug 30, 2018

300

Note: i have already covered this vulnerability previously 2 times on my blogs so you can check that out.

Now , I will just go straight to the point.

I was in My bugcrowd account, Roaming Through Programs, and with my previous experience with Redacted.com program.

I thought why not give it a try, after all i had really bad reputation then.

So i opened the subdomain.Redacted.com as it was in scope , soi took a moment looking at “Wappalyzer”, and i found nothing more than this

Bulls***

my eyes shifted towards the url and saw “.jsp”

“ https://example.Redacted.com/dir/dir/public/SomethingHere.jsf”

and i was like

Press enter or click to view image in full size
Wohoo!

It Reminds of my previous Finding (i did writeup on)

Next Step

I made a small custom dir file base on my previous encounter .

Dir.txt

web-console , admin-console,…. so on

and ran it with dirbuster

I thought it was running tomcat but i was wrong , i remember from my previous reports that they are using some “IBM web app” .

and found a strange thing

Get Ashish Kunwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

/web-console/ is doing

302 redirection.

so i opened it in browser.

And found that,It kept redirecting me to infinity..

Press enter or click to view image in full size
Redacted few things.

So as of my previous two encounters on two different programs and turn out to be valid

“So far i think that path confusions leads to this vulnerability.”

where web application confuse where to go next and hence result into Infinite Loop.

Note: If i m wrong and anyone can explain better , you are welcome

All i found is a CWE-835, which says

“An infinite loop will cause unexpected consumption of resources, such as CPU cycles or memory. The software’s operation may slow down, or cause a long time to respond.”

So i reported and turn to valid and BugCrowd Rewarded me 100$ and 5 points

References:

https://dxploiter.blogspot.com/

Again My DM is open everyone

Thank you for so much love and support.

Peace out :-)

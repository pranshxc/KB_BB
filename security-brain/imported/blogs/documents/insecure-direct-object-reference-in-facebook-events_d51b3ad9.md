---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-11_insecure-direct-object-reference-in-facebook-events.md
original_filename: 2017-08-11_insecure-direct-object-reference-in-facebook-events.md
title: Insecure Direct Object Reference In Facebook Events
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: d51b3ad9bfee824d8c8900cf0a6d6c581556adc97081644e7e4c872adcd4cb31
text_sha256: 310f6a374486bade90f11f58575d0a40229d264c7ab2fe146971ee6d4810e340
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Insecure Direct Object Reference In Facebook Events

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-11_insecure-direct-object-reference-in-facebook-events.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d51b3ad9bfee824d8c8900cf0a6d6c581556adc97081644e7e4c872adcd4cb31`
- Text SHA256: `310f6a374486bade90f11f58575d0a40229d264c7ab2fe146971ee6d4810e340`


## Content

---
title: "Insecure Direct Object Reference In Facebook Events"
url: "https://medium.com/@armaanpathan/idor-was-leading-to-privilege-escalation-and-violating-the-facebook-policy-355c67c654e6"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "2,000"
publication_date: "2017-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6128
scraped_via: "browseros"
---

# Insecure Direct Object Reference In Facebook Events

Insecure Direct Object Reference In Facebook Events
Armaan Pathan
Follow
4 min read
·
Aug 11, 2017

411

2

One day I was playing with the events and I found that the user can make private events and can invite the guests I created a private event.

Press enter or click to view image in full size

after making a private event i have started invited people in my event.
now while i was inviting friends into my event i was also capturing the request in burp suite.

Press enter or click to view image in full size

* now as you will notice the highlighted part in the request. it is a user id of my account as i was inviting my self only. **
here i have deiced to fuzz this parameter “profilechooseritems” with different values.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

## If you have noticed that whenever you create a facebook account the facebook will provide you the UNIQUE **username** and also it also gives userid.
so as per the facebook’s policy you can only invite facebook users in your private event who are into your facebook account.
so i had tried to put my friend @hackerspider1 into my event who was not added into my current testing facebook account’s friendlist and i was able to add/invite him into my event. i was like yeah!! :D i think i have found something. so i had also one more facebook testing account, which is also not added into my current facebook account’s friendlist.i had tried to invite that facebook user too.

Press enter or click to view image in full size

and whatt ! i was able to invite that account too. !!

Press enter or click to view image in full size

but i wanted to exploit it more! without wasting my time i also added @jaypatel9717 into my private event.(now jay patel is also not added into my this testing account’s friendlist.)
i was scrolling my facebook’s news feed and also was thinking that how can i exploit it more? at that time i saw one of my friend’s post “******** is going to DHINCHAK POOJA’s Live Event”.
so i started exploring more that if i m able to post behalf of jay patel like “jay patel is going to this event or not”
and what!! i was able to post that jay patel in going to this event. !

without wasting any time ! i made a PoC of this and reported to facebook.
and the next day moring…. i got a reply :/

so as per the facebook’s policy if someone is added into your facebook’s friendlist and you are adding other facebook users who are not added into your account but they are into the person’s friend list who is added into your facebook’s friend list and if you add them somehow then its a normal behavior. :/// i was like aghhhh !!!
but i dint give up ! quickly made a new facebook account. now i just made an account so there is no one added in my friend list. :3
now i went back to my testing account and tried to add this fresh made facebook account .
and ! yeah ! i was able to add that account too into my private event & make a same post also like ( testarmaanpathantest armaan is going to soo and so event).

again i made a quick PoC and reported to facebook.
after 5–6 days ! i got a reply from facebook that they have patched the issue and please conform that is not reproducible anymore.
After conforming
they Rewarded me with a good amount.

spacial thanks to @jaypatel9717
and yeah ! also learnt that if any friend is taunting you. take it as a challange and prove him/her wrong.
Thanks for reading.
have a great day ahead.

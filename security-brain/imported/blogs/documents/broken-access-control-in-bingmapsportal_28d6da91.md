---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-01-23_broken-access-control-in-bingmapsportal.md
original_filename: 2016-01-23_broken-access-control-in-bingmapsportal.md
title: Broken Access Control in bingmapsportal !!!
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 28d6da91fc456952d0dc4399588130c986a14082c7ea46919b38eb9d8e35ca24
text_sha256: 962ed58497c97c9497356a311b7a07d1b67507a6c15513db4a0707530a614570
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access Control in bingmapsportal !!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-01-23_broken-access-control-in-bingmapsportal.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `28d6da91fc456952d0dc4399588130c986a14082c7ea46919b38eb9d8e35ca24`
- Text SHA256: `962ed58497c97c9497356a311b7a07d1b67507a6c15513db4a0707530a614570`


## Content

---
title: "Broken Access Control in bingmapsportal !!!"
url: "https://medium.com/bugbountywriteup/broken-access-control-in-bingmapsportal-a012bffd2c43"
authors: ["Sai Krishna Kothapalli (@kmskrishna)"]
programs: ["Microsoft"]
bugs: ["Broken Access Control"]
publication_date: "2016-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6322
scraped_via: "browseros"
---

# Broken Access Control in bingmapsportal !!!

Broken Access Control in bingmapsportal
Sai Krishna Kothapalli
Follow
2 min read
·
Jan 23, 2016

311

Hello everyone,

This blog post is going to be about the 3rd vulnerability I reported to Microsoft.

You can manage your Bing maps API keys in bingmapsportal and while updating the name of an application something caught my eye.

POC :-

Whenever you change something like the name of the application etc, the website is using a PUT request to perform the update.

It looks like this.

Screenshot

As you can see, it is sending JSON data like this

{“applicationId”:1707630,”applicationName”:”testing xml”,”applicationUri”:null,”ticket”:”bjc7REBGwm6NNTL3Ot5R~INcJpFU5r-KxjNtDZK2Nkg~ApWBovtZEhj4-Uodq6qTluDURLTLmTpJVOTl_V-4l8f6fnFO1KQlIlmLAijCJgXL”,”accountId”:1418767,”keyTypeId”: 2,“keyType”:”Basic”,”keySubtypeId”:39,”keySubtype”:”Universal Windows App”,”validFrom”:”12/23/2015″,”validTo”:”None”,”isMutable”:true,” showButtonTextEnable”:false,”keyStatus”:”Enabled”,”showKeyEnableDisableButton”:true}

The difference between a PUT and a POST request is that put overwrites whatever is there previously.

The things that caught my eyes were applicationId and accountId. What if I change the application ID what will happen? Who knows let’s try.

So, I asked my sister to use her outlook account and created an Application key with her account.

I create an Application named bounty_1 in my Account and bounty_2 in her account.

Then I intercepted a PUT request with my sister’s account and changed the applicationId from bounty_2’s Application ID to bounty_1’s Application ID

and the response was “Key updated successfully“.

Get Sai Krishna Kothapalli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was like WHAT !!!! and refreshed my Account.

To my surprise the application got transferred from my account to my sister’s account.

The backend is not validating whether the attacker owns the application or not.

I reported this to Microsoft and it’s patched now.

Timeline :-

23–12–2015 — Initial report sent.

Done some follow-up in the next couple of days

05–01–2016 — asked for any updates.

06–01–2016 — got reply saying no updates.

21–01–2016 — Asked once more for any updates

22 -01–2016 — Got reply saying the Issue is fixed

I will be listed in Microsoft’s HALL OF FAME for the month of January 2016

Thank you for reading.

Feel free to contact me if you have any doubts.

Peace :D

Originally published at kmskrishna.wordpress.com on January 23, 2016.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-03_hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part.md
original_filename: 2018-02-03_hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part.md
title: Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit
  (PART-1)
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: 523a825809863bad397b08159e0545ac9408fb0ff0df606b043f631a991c2d38
text_sha256: 8c5c206b9634f001bb9ad20ad4cb0f87d65c8f24e4d219606fb4d2f110f13259
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit (PART-1)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-03_hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `523a825809863bad397b08159e0545ac9408fb0ff0df606b043f631a991c2d38`
- Text SHA256: `8c5c206b9634f001bb9ad20ad4cb0f87d65c8f24e4d219606fb4d2f110f13259`


## Content

---
title: "Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit (PART-1)"
url: "https://codeburst.io/hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part-1-f338c6a52782"
authors: ["Mohammed Abdul Raheem (@mohdaltaf163)"]
bugs: ["IDOR"]
bounty: "3,000"
publication_date: "2018-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5988
scraped_via: "browseros"
---

# Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit (PART-1)

Mohammed Abdul Raheem
 highlighted

Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit (PART-1)
Mohammed Abdul Raheem
Follow
4 min read
·
Feb 3, 2018

800

2

Hello Guys!!

This is my first Blog post and i am starting with IDOR Vulnerability. In this Post you will know about many endpoints to test IDOR vulnerability! Hope you will like it.

Arbaz Hussain
 get invitation to test one private program and find vulnerabilities with his team mates but he was busy with his work and selected me to test that program. So i would like to thank 
Arbaz
 for sharing site and Thanks to AqeelAsif for teaching me lots of stuff from which i was able to find 21 valuable vulnerabilities in 2-days in this program :) and received $3000 in CryptoCurrency!!

Recently i have conducted penetration testing of Popular Social Media Platform and Found lot of IDOR Vulnerabilities .

A direct object reference is likely to occur when a developer exposes a reference to an internal implementation object, such as a file, directory, or database key without any validation mechanism which allows attackers to manipulate these references to access unauthorized data ~ TutorialPoint

https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References

Without wasting more time i am directly going to write about endpoints on which i have found IDORs in that program.

#1. IDOR — Deleting All Posts Of Website

When i have posted a status on my timeline and click on my post it redirects me to another page on which i was able to see my post id in URL.

Press enter or click to view image in full size
Victim post id in URL

So after seeing postid in url quickly i have logged in with Attacker’s Account and posted on timeline to check what i can do with this postid .

Press enter or click to view image in full size
Attacker’s Post

Due to improper validation of postid parameter at Server side leads to Delete All Posts On Website Remotely using IDOR Vulnerability at Following Endpoint .

Get Mohammed Abdul Raheem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

on clicking *Delete the item* Option makes following Request to the server .

Press enter or click to view image in full size
Request making to Server Side

As you can see there is id parameter in POST Data values which is unique id of posts, So i tried changing value from Attacker’s postid to victim’s postid and it deleted Victim’s Post.

Press enter or click to view image in full size
Victim’s Post Deleted

Again i thought if userid parameter is vulnerable and not validating at server side then i can find many IDOR’s ……And i was right !! Luckily i was able to find 12-IDOR Vulnerabilities ;)

#2. IDOR — Changing Anyone’s Profile Picture

Due to improper validation of userid at Server side leads to Change anyone’s Profile Picture Remotely using IDOR Vulnerability at Following Endpoint .

Press enter or click to view image in full size
Profile of Attacker

on clicking *Browse* Option and selecting image file and Clicking Upload makes following Request to server .

Press enter or click to view image in full size
Request Making To Server

As you can see there is userid parameter in POST Data values which is unique id of user , So i tried changing it to another victim account userid value and it changed Victim’s Profile Picture .

Press enter or click to view image in full size
Changed Victim Profile photo with Attacker Photo
#3. IDOR — Changing Anyone’s Cover Picture

Due to improper validation of userid at Server side leads to Change anyone’s Profile Picture Remotely using IDOR Vulnerability at Following Endpoint .

Press enter or click to view image in full size
Profile Of Attacker

on clicking *Browse* Option and selecting image file and Clicking Upload makes following Request to server .

Press enter or click to view image in full size
Request Making To Server

As you can see there is userid parameter in POST Data values which is unique id of user , So again i tried changing it to another victim account userid value and it changed Victim’s Cover Picture .

Press enter or click to view image in full size
Changed Victim Cover Pic with Attacker Pic

What’s next?? Any Option to Delete Profile Pic And Cover Pic? ;)

Yes!! Again i have tested IDOR to Delete “Profile Pictue” & “Cover Picture” and all was working from my side. I was able to Delete “Profile Pictue” & “Cover Picture” of every user. So without wasting time on making POC Video i have reported the issue and got quick response within hours.

Press enter or click to view image in full size

“i like quick responses so i boost up myself to test this program.”

In Part-2 i have added all interesting endpoints to look for IDOR. For my other blog posts you can visit my profile Link.

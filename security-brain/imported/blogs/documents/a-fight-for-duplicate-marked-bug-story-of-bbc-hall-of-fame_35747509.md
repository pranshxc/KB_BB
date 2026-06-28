---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-20_a-fight-for-duplicate-marked-bug-story-of-bbc-hall-of-fame.md
original_filename: 2019-06-20_a-fight-for-duplicate-marked-bug-story-of-bbc-hall-of-fame.md
title: 'A Fight For Duplicate Marked Bug: Story of BBC Hall Of Fame'
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 3574750906e562cdaab0175d4d36232f82a148a312fb7b58f93536269d8941e5
text_sha256: fb1a67e2e085395ad0b7e2529b528124ceccbb77682cfc232c0988447c7c8740
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A Fight For Duplicate Marked Bug: Story of BBC Hall Of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-20_a-fight-for-duplicate-marked-bug-story-of-bbc-hall-of-fame.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3574750906e562cdaab0175d4d36232f82a148a312fb7b58f93536269d8941e5`
- Text SHA256: `fb1a67e2e085395ad0b7e2529b528124ceccbb77682cfc232c0988447c7c8740`


## Content

---
title: "A Fight For Duplicate Marked Bug: Story of BBC Hall Of Fame"
url: "https://medium.com/@dr.spitfire/a-fight-for-duplicate-marked-bug-story-of-bbc-hall-of-fame-16f9c8215315?sk=9269454dd3557dc8ea9c1ec26be033dd"
authors: ["Wasim Shaikh (@Wa_sim_sim)"]
programs: ["BBC"]
bugs: ["XSS"]
publication_date: "2019-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5197
scraped_via: "browseros"
---

# A Fight For Duplicate Marked Bug: Story of BBC Hall Of Fame

InfoSec Brothers
Follow
4 min read
·
Jun 20, 2019

26

3

A Fight For Duplicate Marked Bug: Story of BBC Hall Of Fame

I am writing this post not because I want to tell the Infosec community about my achievement of finding XSS on the BBC’s home page. It’s been days I am reading tweets and posts related to how the programs with “Responsible Disclosure” are cheating bug bounty hunters by marking their valid bug duplicate. Even the programs on Bugcrowd are trying to do the same nowadays. Following are some bug bounty hunters who have faced the stigma of duplicate bugs for a very good vulnerability.

Press enter or click to view image in full size
https://twitter.com/satishkmr834
Press enter or click to view image in full size
https://twitter.com/MrG0LEM
Press enter or click to view image in full size
https://twitter.com/Cache_Bounty

Many of the bug bounty hunters don’t give up and keep hunting the bugs on same programs. But, in my opinion; if the program is marking any bug as a duplicate, it should provide the substantial shreds of evidence that the same vulnerability with same attack scenario was reported by other bug bounty hunter before him/her. I have seen 
HackerOne
 following the policy of mentioning the report number of a report submitted by another bug bounty hunter. But, if the program is marking any bug duplicate without providing the evidence, stop hunting on the same program. Share how that program is cheating on you with your fellow security researchers and bug bounty hunters via Twitter and LinkedIn.

Get InfoSec Brothers’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, coming back to my story, I was hunting on BBC as I wanted my name in their Hall Of Fame list. I saw many bug bounty hunters have reported an XSS to BBC and they have patched XSS very well. I thought, let’s start by using Burp Suite’s intruder to fire the XSS payloads. I fired a few hundreds of XSS payloads that are mostly used to bypass WAF and to bypass implemented prevention measures for an XSS. I was out of luck. The best approach to find an XSS vulnerability is noticing how the application is responding back to your input. I noticed, the payload, “<script>alert(“Hacked By DrSpitfire”)</script> was getting embedded in the value=”payload here”. After lots of tries, I got the idea to try to end the value=”payload here” tag. Thus, I started using payloads such as “”<script>alert(“Hacked By DrSpitfire”)</script> and it did not work. After few tries the payload “<script>alert(“Hacked By DrSpitfire”)</script>“<script>alert(“Hacked By DrSpitfire”)</script> worked and I got the most awaited pop-up.

Press enter or click to view image in full size
Magical Pop-Up!

I was happy that I will be there on BBC’s HOF listing. Without taking any break, I reported it to the BBC ( security@bbc.co.uk). However, I got the following response from their Information Security team,

Press enter or click to view image in full size
Reported Few Days Back?

I sent another email to the BBC and ask them to follow the transparency. I asked them to share the proofs that same finding was reported by another bug bounty hunter before me. After many days, I got a very polite reply stating that the issue was fixed and the bug was marked duplicate by mistake.

Press enter or click to view image in full size
Reported Very Shortly after me?

The point here is, I asked the program to follow the transparency and BBC Information security team was fair enough to take a stand. They had the courage to accept their mistake and to correct it as well. However, many programs are not doing that. I have seen bug bounty hunters submitting P1 issues and very critical security vulnerabilities to the program and getting a response as a duplicate bug. These programs even do not participate in further communication with the security researcher. Thus, in my opinion, there is no point in wasting precious time on programs like this. There is a need to expose these programs on LinkedIn and Twitter so that they will start following the rules before marking any submission duplicate. Let’s work together to fight with programs with abhorrent “Responsible Disclosure”.

Finally, after a day, my name was up there on BBC’s Hall Of Fame List.

Press enter or click to view image in full size
Wasim Shaikh Will be here as long as the BBC is there!

./SigningOff

Thank you!

You can follow me on Twitter: https://twitter.com/Wa_sim_sim

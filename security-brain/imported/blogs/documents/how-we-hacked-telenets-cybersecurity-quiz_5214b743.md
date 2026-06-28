---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-07_how-we-hacked-telenets-cybersecurity-quiz.md
original_filename: 2022-11-07_how-we-hacked-telenets-cybersecurity-quiz.md
title: How we ‘hacked’ Telenet’s cybersecurity quiz
category: documents
detected_topics:
- rate-limit
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- rate-limit
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 5214b74360ac468f530a5338ca09550131c2882f8af0d37582d233a75da707a4
text_sha256: 7cf342e6c7ac0c7eb7c90bc7f4e52143a6b5f1f1cd822d27d29dfc0c53df43a7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How we ‘hacked’ Telenet’s cybersecurity quiz

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-07_how-we-hacked-telenets-cybersecurity-quiz.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `5214b74360ac468f530a5338ca09550131c2882f8af0d37582d233a75da707a4`
- Text SHA256: `7cf342e6c7ac0c7eb7c90bc7f4e52143a6b5f1f1cd822d27d29dfc0c53df43a7`


## Content

---
title: "How we ‘hacked’ Telenet’s cybersecurity quiz"
url: "https://mickeydebaets.medium.com/how-we-hacked-telenet-s-cybersecurity-quiz-958c1d3ee2ba"
authors: ["Mickey De Baets"]
programs: ["Telenet"]
bugs: ["Logic flaw"]
publication_date: "2022-11-07"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 1941
scraped_via: "browseros"
---

# How we ‘hacked’ Telenet’s cybersecurity quiz

How we ‘hacked’ Telenet’s cybersecurity quiz
Mickey De Baets
Follow
4 min read
·
Nov 8, 2022

4

Press enter or click to view image in full size
Quiz by Telenet Business

Not so long ago, Telenet Business ran a quiz to find the smartest cyber specialist. The quiz consisted out of 20 questions and your score was based both on whether the answer was correct and your reaction time.

Of course we just had to give it a try. While looking at the quiz, we quickly found a few things. First of all, after submitting the answer to a question, the correct answer was revealed. Secondly, multiple attempts were possible, even with the same email address (In the end it was made clear that they were in fact monitoring double attempts, but fake email addresses still exist (: ).

Press enter or click to view image in full size
First quiz question
Press enter or click to view image in full size
Answer of the question

So the first possible cheating strategy here, would be to use either fake credentials or the contact info of a colleague, to reveal the correct answers, write them down and to use this info in your advantage… So, that’s what we did and before I knew, I had first place! At this point, the competition was more about who can click the fastest…

Press enter or click to view image in full size
Getting the maximum score
But wait, there’s more

With the answers written down and lightning fast clicks, it was very hard to beat this reaction time. So imagine my surprise when on the last day, I looked at my score again and saw I dropped down to second place…

Get Mickey De Baets’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s when I received a call from my colleague Robin Bruynseels telling me he found something. You see, he was also trying to check his score, but when typing “telenet” in his search bar, he clicked on a link that brought him back to the page of the last question. He just clicked next and suddenly saw his score went up and above the maximum score of 2370. All credit for finding this ‘exploit’ goes to him!

I reviewed his technique and confirmed the cache issue and started thinking: “What are the odds they’ll allow me to run these requests with a script?”.

With only a few lines of python code it became clear very quickly that rate limiting would not be an issue and Robin’s ‘exploit’ was scriptable.

Press enter or click to view image in full size
Python script
Result
Press enter or click to view image in full size
Scoring way above maximum

I ended up getting a score far above the maximum one allowed and finished first in the competition. Of course, after it ended, Robin and I notified Telenet of what we found and how we were able to get this insanely high score. Unfortunately, due to multiple attempts being against the competition guidelines, our scores were deemed as invalid 🥲. They did thank us for our enthusiastic participation however and were very happy that we reported our findings.

Of course we were expecting this and at least we’re getting a fun blog post out of it! It again shows the value of always testing everything, in every scenario. The happy path is a myth and someone will almost always find a way to do things you never imagined.

Big shout out to Telenet Business and their reaction. They were open to our feedback and even took the time to schedule a meeting with us. For a quiz in theme of awareness and cybersecurity, it is the perfect example of the smallest things matter and how a receptive attitude towards feedback can greatly improve your cybersecurity resilience.

Did you read this and are you now wondering if we can break into your web application / infrastructure / company? Do you have any questions about ethical hacking and penetration testing? Feel free to talk with us!

Penetration testing service
A SOC, not to be confused with the socks on your feet, is a real security solution that can save companies a lot of…

easi.net

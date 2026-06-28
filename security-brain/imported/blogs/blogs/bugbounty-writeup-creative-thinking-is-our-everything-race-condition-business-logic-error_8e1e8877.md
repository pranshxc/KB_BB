---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-05_bugbounty-writeup-creative-thinking-is-our-everything-race-condition-business-lo.md
original_filename: 2019-08-05_bugbounty-writeup-creative-thinking-is-our-everything-race-condition-business-lo.md
title: BugBounty WriteUp — Creative thinking is our everything (Race Condition + Business
  Logic Error)
category: blogs
detected_topics:
- business-logic
- command-injection
- otp
- race-condition
tags:
- imported
- blogs
- business-logic
- command-injection
- otp
- race-condition
language: en
raw_sha256: 8e1e8877490b7fcf244771ea0652bfa40582b09b9a3f9df71fee9d6f26ab1b2c
text_sha256: 58ac5bf547e57994e3ca6c149a96acf4751b7d721cf80e83e14d59924b5e5dce
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# BugBounty WriteUp — Creative thinking is our everything (Race Condition + Business Logic Error)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-05_bugbounty-writeup-creative-thinking-is-our-everything-race-condition-business-lo.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, otp, race-condition
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `8e1e8877490b7fcf244771ea0652bfa40582b09b9a3f9df71fee9d6f26ab1b2c`
- Text SHA256: `58ac5bf547e57994e3ca6c149a96acf4751b7d721cf80e83e14d59924b5e5dce`


## Content

---
title: "BugBounty WriteUp — Creative thinking is our everything (Race Condition + Business Logic Error)"
url: "https://medium.com/@04sabsas/bugbounty-writeup-creative-thinking-is-our-everything-race-condition-business-logic-error-2f3e82b9aa17"
authors: ["Oleksandr Opanasiuk (@Lekssik2)"]
bugs: ["Race condition", "Logic flaw"]
publication_date: "2019-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5098
scraped_via: "browseros"
---

# BugBounty WriteUp — Creative thinking is our everything (Race Condition + Business Logic Error)

BugBounty WriteUp — Creative thinking is our everything (Race Condition + Business Logic Error)
Oleksandr Opanasiuk
Follow
5 min read
·
Aug 6, 2019

209

1

So hello everyone! My name is Leks and this is the happy story of combining two vulnerabilities.

Press enter or click to view image in full size

[PART 1 — Logical] While testing an application with the ability to make a payment and increase the balance, I came across incorrect processing of zeros after the decimal point in the sum. Everywhere, the program rounds the numbers to a larger amount and the same thing in final price for billing.

Buut… not everything was so simple with 0.009. It turned out that the service simply credited 0.01 price without checking a bank card (respectively, and without withdrawing money). Then I was already relaxed, and I think this is a buzz, it will be P1 — unlimited adding money to the account. But after the second time, I got a little upset — it turned out that the larger the amount we put into the account, the more the minimum deposit to our account grows, so after the second time, when we had 0.02 on the account, our trick with 0.009 did not work, and we can’t replenish more(the rule was: you can make a payment only for sum, more or equal than you have on your account, thats why after 2nd time, I do have 0.02, and cant purchase 0.01 as its little). After the opening of such an unpleasant surprise, I wrote down in ToDo list the fact of such vuln. At that time, I already exploited the Condition Race before, so I just wrote it down as an idea to use.

[PART 2 — Technical] 1 month later… :) I decided to return to this vulnerability and exploit it further. Since there was an idea with Race Conditions.

I need to explain how does Race Condition works here. When we start several threads at the same time, some of them catch old data on the server, what we use to our advantage.

Press enter or click to view image in full size

We have balance (a=0) and minimum deposit replenishment (b=0), which, as we know, increasing after every purchase. When we are increasing the balance (a+1), servers is looking at minimum deposit(b) and checks that the number to which we replenish is bigger than the balance (1≥b).

In example of 8 requests: 1-4 requests caught on the server limit b=0, so only 4th request caught b=1. 5–8 made the same things. Because the server works with threads separately — the variables with which they begin to work do not change during this work. So in 5–8 requests — b=1, and only on 9th request data is updated, and the request no longer passes by the rules of the limit.

This is important to understand — threads do not communicate with each other, like — Hey dude, I have +1 here, you need to change limit — Oh ok, np bro. Thats why we can create a race condition, during what threads use a non-updated date. Ok? Let’s go to exploiting.

I started writing scripts. As I love python ❤, and I think that I can write everything on it, my scripts were on it. But after some time have found such a tool — I did not try it myself, but maybe it will make your life easier.

aaronhnatiw/race-the-web
Tests for race conditions in web applications by sending out a user-specified number of requests to a target URL (or…

github.com

So let’s look a little bit of scripts we need to exploit Race Condition.

Race Conditions is exploiting easy — we just need to create scripts with requests and send them simultaneously to the site — and the more the better (for a white hacker, 20 requests will come down, only to show that the vulnerability exists, but if you want to exploit the vulnerability with maximum benefit — then you need a lot of requests).

Get Oleksandr Opanasiuk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The request to purchase was looked like:

Press enter or click to view image in full size

I’m using python “requests”:

Press enter or click to view image in full size

Such script making POST-request with headers and tokens

And cheers! Finally, he hacked and everything is behind! — you thought.

Well, not so easy :) In my case, I had two pages, on one I make a payment, on the second I confirm, so I had to get unique tokens that were stored in the HTML code. Everything sounds easy — one script in this way created requests and collected tokens in a separate file, and the second took these tokens, substituted them into forms and confirmed. But in reality it was a little hard to do, in terms of sequence logic. As a result, the logic of my PoC was this: the 1st file creates payments and collects tokens. At this time, another accepts these tokens, creates a bunch of scripts (yeap, the script creates scripts, the future is near :) and inserts tokens into their code so that each file carries a unique token.

After that, he creates a script like this — operand “&” runs them at the same time (more precisely, runs the next line of the script, without waiting for the end of the current line)

And boooom! Everything worked and we got the cool Race Condition :)

It is sometimes difficult to exploit such a vulnerability due to tokens, but it is nevertheless possible — just write down what is going on and make a plan.

Many thanks to the 
HackerOne
 support team, as they quickly provided me with an account to test it after a letter with a request, and the owners of the program quickly confirmed the vulnerability and kept up to date with all the updates.

So just keep thinking how to hack — and you will make it :)

We reached the end, so I want to say — it is my first writeup, and you can follow me on Twitter to find out more — I will try to do it more often:

Oleksandr Opanasiuk
The latest Tweets from Oleksandr Opanasiuk (@Lekssik2). Great manager and not bad pentester. Ukraine

twitter.com

Have a nice day! :)

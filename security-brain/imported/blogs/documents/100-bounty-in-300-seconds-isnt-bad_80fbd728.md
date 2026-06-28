---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-31_100-bounty-in-300-seconds-isnt-bad-.md
original_filename: 2018-08-31_100-bounty-in-300-seconds-isnt-bad-.md
title: $100 Bounty in 300 seconds isn’t bad !!!
category: documents
detected_topics:
- xss
- sqli
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- mobile-security
language: en
raw_sha256: 80fbd72813a975f6f9ca03ab2950479816a492da91c1547f872ca38536ebb371
text_sha256: a8488b95c94a237a7cd7d0f7be5a5b84f1766caeb24b4e15b7eb5d76e5903ad4
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# $100 Bounty in 300 seconds isn’t bad !!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-31_100-bounty-in-300-seconds-isnt-bad-.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `80fbd72813a975f6f9ca03ab2950479816a492da91c1547f872ca38536ebb371`
- Text SHA256: `a8488b95c94a237a7cd7d0f7be5a5b84f1766caeb24b4e15b7eb5d76e5903ad4`


## Content

---
title: "$100 Bounty in 300 seconds isn’t bad !!!"
url: "https://medium.com/@rohanchavan/100-bounty-in-300-seconds-isnt-bad-4f4112c102ef"
authors: ["Rohan Chavan (@rohanchavan1918)"]
programs: ["Zoho"]
bugs: ["Stored XSS"]
bounty: "100"
publication_date: "2018-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5729
scraped_via: "browseros"
---

# $100 Bounty in 300 seconds isn’t bad !!!

$100 Bounty in 300 seconds isn’t bad !!!
Rohan Chavan
Follow
4 min read
·
Aug 31, 2018

93

1

Hey guyzz …!!! I hope you are fine and doing absolutely awesome in your own fields. Thanks for the awesome response on my last article have got almost 18K views, 11k reads, and 450+ claps and counting..!!! In the meanwhile I wrote a few other articles but not on medium ( they are posted on Secjuice ) such as writing a Directory bruteforcing tool in 25 lines of python , India from a hackers perspective and few other awesome writeups are posted here.

This write up is about my recent findings in zoho. First of all I would like to thank zoho security team for allowing me to write about this bug. The bug was an stored xss in one of their subdomain. So I was just going through the facebook posts in one of the bug bounty hunters group, one of the guy there posted his zoho leaderboard post, until then i wasn’t knowing that zoho had a BugBounty Program. I was like ….

I hopped on and fired up my machine, I saw their program and scope and was ready for the hunt.

This is where you can start the timer, 3,2,1 …..LAUNCH ..!!!

So I browsed to their website, and created an account and landed on their dashboard. It was the first time I was on ZOHO, there were three main options, campaigns , enterprise & uummm…….lets keep that a secret.(I dont remember the third one and i’m lazy to login again and see it for the blog 😂 🤣). Like every other bug hunter , I started playing with it to understand how the site is working.In the dashboard I saw there was an calendar, Out of curiosity I started testing it, clicking here and there, i wasn’t yet analyzing requests in burp, just clicking here and there.

Press enter or click to view image in full size

So I clicked on one of a date and an modal box prompted me,in this box there was an option mark this date.

Press enter or click to view image in full size

When I clicked on that button, it took me to another page,where I was able to write title, add action and stuff. Initially I quickly tried some sqli and xss payloads but didnt seem to workout, I wasn’t really having any hope on this but was motivated enough to keep going further. I was putting xss payloads in every text input available,you never know , when you might get lucky just like I got this time. So I again entered the xss payload in the notes input. and then submitted the form. I had my fingers crossed but nothing happened , I was back to the calendar page.I again started wandering here and there….then I noticed that the title which I had written was on the calendar date within blue strip. I remembered I haven’t checked that out yet, So I clicked on that and what ……

.

.

.

Get Rohan Chavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

.

(nope it didnt give me the xss popup) nothing happened yet.The same modal popped up again it was having the details of whatever I entered.

I noticed the small action in blue, I clicked it and ….

It triggered the XSS, I was very surprised that it wasnt even more than 5 minutes that I found something on it. Since the Bug was in action of a calendar, I was hoping if it would execute on itself (It would be a complete time bomb if it could 😂 🤣) but to my bad luck it didn’t go the way i wanted it to, but thats okay, That xss made my day.After that I made an report and reported it to zoho security Team.(Writing the report is always boring :( ..!!

Press enter or click to view image in full size

They awarded me a bounty of $100 and 200 points and HOF. yeah i do think $100 was low for a stored xss but knowing the fact that I didn’t put much efforts in it, it was completely an luck catch and I was okay with $100.

Video POC :

TimeLine :

Reported on, 22/08/18

Acknowledged by team ,Aug 24, 2018 12:27:10 PM

Awarded 200 points and closed the Bug, Aug 27, 2018 8:01:22 PM

Awarded Bounty of $100, Aug 31, 2018 6:22:47 PM

Thats it, Thanks for Reading ..!!!

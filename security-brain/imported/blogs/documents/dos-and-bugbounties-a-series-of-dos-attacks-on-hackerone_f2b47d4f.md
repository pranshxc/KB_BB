---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-12_dos-and-bugbounties-a-series-of-dos-attacks-on-hackerone.md
original_filename: 2020-06-12_dos-and-bugbounties-a-series-of-dos-attacks-on-hackerone.md
title: DoS and BugBounties :A series of DoS attacks on HackerOne
category: documents
detected_topics:
- rate-limit
- cloud-security
- sso
- command-injection
- automation-abuse
- race-condition
tags:
- imported
- documents
- rate-limit
- cloud-security
- sso
- command-injection
- automation-abuse
- race-condition
language: en
raw_sha256: f2b47d4fadd918a0ae73eda0dc0fbca25a071a67ef41d25f13b0fd82953204d1
text_sha256: 3fff60eceba9124a16d63ed9e0f9561aea133e148fe0fbaa8594e354ec494b41
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# DoS and BugBounties :A series of DoS attacks on HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-12_dos-and-bugbounties-a-series-of-dos-attacks-on-hackerone.md
- Source Type: markdown
- Detected Topics: rate-limit, cloud-security, sso, command-injection, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f2b47d4fadd918a0ae73eda0dc0fbca25a071a67ef41d25f13b0fd82953204d1`
- Text SHA256: `3fff60eceba9124a16d63ed9e0f9561aea133e148fe0fbaa8594e354ec494b41`


## Content

---
title: "DoS and BugBounties :A series of DoS attacks on HackerOne"
url: "https://medium.com/@NinadMishra/dos-and-bugbounties-a-series-of-dos-attacks-on-hackerone-9c8316e192c9"
authors: ["Ninad Mishra (@iamr000t)"]
bugs: ["DoS"]
bounty: "500"
publication_date: "2020-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4505
scraped_via: "browseros"
---

# DoS and BugBounties :A series of DoS attacks on HackerOne

DoS and BugBounties :A series of DoS attacks on HackerOne
Ninad Mishra
Follow
6 min read
·
Jun 13, 2020

374

1

Greetings, this is my first writeup and I will discuss a very common vulnerability that is so underrated everybody seems to ignore it during their testing “DoS”, in this writeup I will also share about my 4 valid reports on HackerOne program and also how I was able to create an impact on a very old report which was closed as an informative,which resulted in hackerone rewarding bounties to both the researchers (me) and the person whose report was closed as an informative.

Why as a Bug Bounty hunter you should care about DoS ?

most of the BugBounty programs generally consider DoS out of scope,however a quick google search with a simple custom dork can be used to find out how many programs actually accept DoS as a valid issue and are interested in fixing it (and there are a lot).

site:hackerone.com/reports/ “dos” “Bounty”

so without wasting anymore time lets get started.

Challenges faced during testing for DoS vulnerabilities :

Testing for DoS vulnerability on a production webapp can be very tricky,as it is very easy during testing for DoS to actually break / do some damage on the target. one should always follow the approach of “Bend, but not break” ie one should try to create a minimalist POC and avoid doing any kind of damage.

Positive aspect of DoS Challenges.

When we think it in a more optimistic manner this also means that DoS vulnerabilities can be very common and easy to find, as it is significantly harder to test for DoS vulnerabilities in a production environment.

Types Of interesting DoS you should definitely read : ( Covering all type of DoS attacks will not be possible, below are some of the DoS attacks which I find really unique and interesting along with the references )

ReDoS ref :->https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
CpDoS ref:->https://cpdos.org/
Zalgo Text DoS :-> http://www.iphonehacks.com/2013/03/imessage-denial-of-service-attack.html
AWS SES DoS :->https://medium.com/@keshavaarav22/an-unexpected-bounty-email-bounce-issues-b9f24a35eb68
1.)Creating an Impact on old Informative Report.

While testing ctf.hacker101.com I came across an interesting feature which allows us to create groups and invite other hackers to join it on the endpoint https://ctf.hacker101.com/group the things I observed while testing were the following :-

No rate limiting on creating Groups
No pagination while displaying Groups (all the groups were shown in a single response )

After these observation it was clear to me that this can be abused to DoS the website by creating a large number of groups and then sending a simple GET request to see all the groups. although, when i reported this issue my report was duplicated to a report which specified the lack of rate limiting issue and was closed as an informative. Another researcher who originally had reported lack of rate limiting didn’t tried to create a realistic impact and after I demonstrated the impact which was DoS on ctf.hacker101.com. HackerOne decided to reopen that informative report and award both of us 50%-50% bounty and the issue was mitigated by applying a limit of how much groups a user can create and applying pagination in the response.

Press enter or click to view image in full size
Creating Impact on rate limiting issue.
2.) Bypassing the fix.

After the fix was applied, I tested the endpoint again I kind of knew it will be possible to bypass this somehow as I already have a large number of groups created on ctf.hacker101.com, after testing it seemed the response time was higher but I was unable to make the server respond with a 502 response, hence i decided to try to bypass the pagination by opening the website with a different accept encoding value ie

Accept-Encoding: gzip, gzip,deflate,br 

As the response time was significantly higher I also tried to make multiple requests concurrently and it worked, i noticed that if i make multiple requests concurrently the server started responding with a 502, to test this safely I didn’t used intruder instead I decided to simply used multiple tabs and I was successful, hence I created a new report and was awarded a 500$ bounty you can read the report here https://hackerone.com/reports/861170/

Press enter or click to view image in full size
using earlier created groups to recreate the same impact.
3.)AWS SES DoS attack on HackerOne.

As you might already know that AWS SES is nothing but Amazon’s simple email service, the funny thing with Amazon’s simple email service is that it suspends your account if emails which were sent by your account have a bounce rate > 10%, this actually means that if you can make a target that is using AWS SES send some mails on the emails which does not exist the Amazon will actually suspend their SES account, denying them to be able to send any email to their users. while testing on hackerone I came across an interesting endpoint which allowed program members to invite hackers to their program, I made following observations :-

No rate limiting enforced while inviting other hacker.
No, RFC 5322 verification while sending invites.

I used a simple payload that was anyemail$1@anything.com and sent an email invitation, and to my surprise the email was accepted and invitation was sent however according to RFC5322 email like that can not actually exist

Get Ninad Mishra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Although after reporting this issue my report was first marked as not applicable and a duplicate to Email Spamming (all thanks to my lack of report writing skills I guess) and due to some misunderstandings and miscommunications I did some damage and my report was marked as ineligible for bounty. although the issue was valid and fixed (closed as resolved ) and I learnt a lot about testing for DoS attacks safely so it is like a win win for everybody.

4.)GraphQL DoS attacks :

While spending time reading the best practices of GraphQL here (https://graphql.org/learn/best-practices/) one interesting thing caught my attention that was

Pagination

The GraphQL type system allows for some fields to return lists of values, but leaves the pagination of longer lists of values up to the API designer. There are a wide range of possible API designs for pagination, each of which has pros and cons.

This simply means that GraphQL doesn’t implements any type pagination by default therefore one can actually use this information to form a query which would result in long response and may timeout the target server.

Lessons learned while testing for DoS :
before starting to test for DoS must check the program’s scope to see it is not listed as out of scope.
testing for DoS should always be done very carefully and one must follow Bend, but not break approach.
use of automated tools should be minimum and if possible “null” while testing for DoS as it may cause unintentional damage.
Communication with the team is crucial while testing for DoS, as it reduces the risk of damage.
patience is the key, it is really easy to get frustrated in the process of reporting, one must realize that validating DoS vulnerability is time consuming and difficult and therefore one must have patience while the report is made and is being validated.
My personal experience :

After my 3rd report (AWS SES DoS) was marked as ineligible for bounty I was really frustrated as at first it was marked NA and while demonstrating the impact I unintentionally did some damage,I felt like my time was wasted, I even misbehaved with HackerOne’s team for which I would truly like to apologize for, Though after doing some rational thinking I realized that I can use this experience to learn from my mistakes and make it useful for me as well as others by improving my methodologies, report writing and sharing my experience. during this whole experience the support and guidance I received from Ben Willis was really amazing and inspiring. I would like to thank him for all his hard work in guiding me in the right direction and motivating me in improving my techniques.

Credits:

Ben Willis
HackerOne Team

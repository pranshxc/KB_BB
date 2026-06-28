---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-21_facebook-bug-bounty-secondary-damage-one-report-that-leads-to-more-bugs-fairness.md
original_filename: 2013-10-21_facebook-bug-bounty-secondary-damage-one-report-that-leads-to-more-bugs-fairness.md
title: 'Facebook bug bounty: secondary damage (one report that leads to more bugs),
  fairness, and why I really like reporting to Facebook'
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: 8e70a1a7819ba5e4ad232377f0e82bc90908fdb3493021a1a691c2540fb4346d
text_sha256: a17af2de20cd1d1512c9060babf78048fbc06d3db96deebabfb0043dd8af0d1d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook bug bounty: secondary damage (one report that leads to more bugs), fairness, and why I really like reporting to Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-21_facebook-bug-bounty-secondary-damage-one-report-that-leads-to-more-bugs-fairness.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8e70a1a7819ba5e4ad232377f0e82bc90908fdb3493021a1a691c2540fb4346d`
- Text SHA256: `a17af2de20cd1d1512c9060babf78048fbc06d3db96deebabfb0043dd8af0d1d`


## Content

---
title: "Facebook bug bounty: secondary damage (one report that leads to more bugs), fairness, and why I really like reporting to Facebook"
page_title: "Josip Franjković - archived security blog: Facebook bug bounty: secondary damage (one report that leads to more bugs), fairness, and why I really like reporting to Facebook"
url: "https://josipfranjkovic.blogspot.com/2013/11/facebook-bug-bounty-secondary-damage.html"
final_url: "https://josipfranjkovic.blogspot.com/2013/11/facebook-bug-bounty-secondary-damage.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
publication_date: "2013-10-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6393
---

Hello,  
  
Usually, the process for bug bounty is as follows:  
  

  1. Person finds a bug, reports it to company
  2. Company fixes the bug
  3. $$ sent to the reporter.

An example is a critical [bug I reported to Facebook](http://pyx.io/blog/facebook-csrf-leading-to-full-account-takeover) some time ago.  
  
But few days ago, I read a [blog by Facebook security](https://www.facebook.com/notes/facebook-security/an-update-on-our-bug-bounty-program/10151508163265766): one paragraph states that "Bugs that lead us to more bugs get bigger payouts. In these cases, the initial bug is much more valuable because the subsequent investigation and fixing of the original bug leads us to additional issues that we can fix."  
  
Frankly, I did not believe this; why would Facebook (or any other company) increase the reward for bugs they found in their internal investigation? The person who reported the original bug would never know that thanks to their report, Facebook fixed bugs the reporter did not find.  
  

###  It turns out, I was **very, very** wrong - Facebook does pay for secondary bugs, and are extremely fair about it. 

###  M**y original report:****  
**

>  
> 
> 
> Subject: **Report a Security Vulnerability - Low-risk CSRF that adds verified students to school groups**  
>  Title: Low-risk CSRF that adds verified students to school groups  
>  Product / URL: Groups for Schools <https://www.facebook.com/groups/>  
>  Description and Impact: Hello,  
>  
>  This vulnerability allows attacker to make victim a member of groups for schools.  
>  It is very specific and low-risk because victim must:  
>  1\. have school/university email VERIFIED  
>  2\. not already be part of group  
>  
>  In order for this to work, this must also be victim's FIRST time to join group.  
>  
>  Attacker must know that victim has email verified in one of school/uni domains.  
>  
>  **Reproduction Instructions / Proof of Concept:**  
> 
> 
>  
> 
> 
> 1\. a victim must have verified school address  
>  2\. victim must make GET request to  
>  https://www.facebook.com/groups/{{schoolGroupName}}/_join_/  
>  for example, in my test case:  
>  victim with jxfXXXX@***.edu verified visits site with <img src="https://www.facebook.com/groups/GroupsAt***/_join_/">  
>  and becomes member of the group.

  
Basically, I hoped for the minimum reward because the bug I reported was, as you can see, really crappy one: very specific and has really limited functionality.  
Few days later, Facebook Security team replied that they are looking into the issue and will reply when it is fixed. Then came the  

###  Facebook's second reply: 

> > Hi Josip,
>
>> OK, just talked with the team. This particular issue is actually a wontfix for them: the goal when you have a school/university email is for you to be associated with your school/university community. However, it did lead us to a related issue which would have allowed for CSRF to add people to arbitrary groups, so we'll be paying you a bounty for that. Nice work. :-)

  
**Wait, what? Of course, I wanted to know what bug did I miss. I checked if _join_ CSRF works for usual groups, and it did not. So where was the bug?**  
  
**Here is explanation from the sec team:**  

> I don't think it's something you would have found; when we were investigating your report we found references in the code to a _join_if_can_ flag which worked the same way you described but on more general types of groups (not arbitrary groups though: I misspoke earlier). It looks like the flag wasn't being used and it was simple enough to remove. :-)

  
  
**WAIT, WHAT???!!111??!**  
I got a (pretty huge) reward for a bug that was IMPOSSIBLE to find to outside people, because it is pretty much impossible to guess the "_join_if_can_" flag - it was not in production. So, a reward on a basis of really, really low-impact report.  
  
Through this blog I would like to say a **GIANT THANKS** to the Facebook security team, not only for running their program, **but also for being extremely sincere and fair towards us, the bug bounty hunters.**  
**  
**Edit: timeline of the report:  
  

  1. 18\. of October, 2013 - bug reported
  2. 18\. of October, 2013 - reply from Facebook team (not bot, but team)
  3. 26\. of October, 2013 - Facebook is working on a fix, should be live soon
  4. 20\. of November, 2013 - Facebook team replies that their investigation led to another bug and they decided to award me for it
  5. 20\. of November, 2013 - Chat with the team, bounty rewarded
  6. 21\. of November, 2013 - This blog published

I am not really sure when exactly they fixed the vulnerability, or found the new flag/bug (never checked as it was low-priority). I can only assume it was between 26th and middle of November.  
**  
****  
****\--** Josip Franjković  
**  
****  
**  
  
  

>

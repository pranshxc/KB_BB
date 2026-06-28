---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-26_horizontal-privilege-escalation-on-quora-which-can-compromise-all-users-on-quora.md
original_filename: 2019-02-26_horizontal-privilege-escalation-on-quora-which-can-compromise-all-users-on-quora.md
title: Horizontal Privilege Escalation on Quora which can compromise all users on
  Quora
category: documents
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- documents
- idor
- access-control
- command-injection
language: en
raw_sha256: a0a65fc2717526ea708d4548777f3a2882e16124ac9ee9628012124ebeb316ca
text_sha256: c814d0a26dcd66ee6512a383e347f6c484dba26cc11409fc045968d4237d3ac1
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Horizontal Privilege Escalation on Quora which can compromise all users on Quora

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-26_horizontal-privilege-escalation-on-quora-which-can-compromise-all-users-on-quora.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `a0a65fc2717526ea708d4548777f3a2882e16124ac9ee9628012124ebeb316ca`
- Text SHA256: `c814d0a26dcd66ee6512a383e347f6c484dba26cc11409fc045968d4237d3ac1`


## Content

---
title: "Horizontal Privilege Escalation on Quora which can compromise all users on Quora"
url: "https://spyclub.tech/2019/02/26/horizontal-privilege-escalation-on-quora/"
final_url: "https://spyclub.tech/2019/02/26/horizontal-privilege-escalation-on-quora/"
authors: ["SpyD3r (@TarunkantG)"]
programs: ["Quora"]
bugs: ["Privilege escalation"]
publication_date: "2019-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5385
---

#  Horizontal Privilege Escalation on Quora which can compromise all users on Quora 

SpyClub

2019-02-26

__[blog](/categories/blog/)

__[Bug](/tags/Bug/), [BugBounty](/tags/BugBounty/), [Privilege-Escalation](/tags/Privilege-Escalation/), [Writeup](/tags/Writeup/)

Hey, I am SpyD3r([@TarunkantG](https://twitter.com/TarunkantG)) and in this blog, I will be discussing the bug I have found in Quora which can compromise all users on Quora due to Horizontal Privilege Escalation. 

I worked more than 18 hrs a day and did it for a week to get familiar with all Quora functionality/workings, then finally I got two bugs 1 medium and 1 critical, here I will be discussing critical one only because I didn’t get the bounty for Medium one yet ;). It was really fun working with Quora because it has a lot of functionalities and this was my first bug (which comes out to be critical). I started finding the bug because I need to finance my site(<https://spyclub.tech>) because subscription gonna end in March. Eventually, now I can take a subscription for 10 years, so let’s start. 

As I was testing each functionality, I was also figuring out which only thing can make a proper impact in the response like only `m-b` cookie is responsible for login, we can enumerate `uid` to get user details like Name, Profile pic etc. 

For enumerating `uid`, I figured out that we can do it from `kwargs`.  

  
  
  1  
  

| 
  
  
  json=%7B%22args%22%3A%5B%5D%2C%22kwargs%22%3A%7B%22uid%22%3A123456%7D ...  
  
  
---|---  
  
Changing the `uid` will let you know other user details. (BUT ONLY HERE?)  
After digging more I also got to know that in the some of the places putting the `uid` on `args`, will also get you the same (COOL). Now let’s go forward.

When I was checking the functionality of sending the request for an Question, I saw this the request:  

  
  
  1  
  

| 
  
  
  js_init=%7B%22asked_uid%22%3A365110562%2C%22viewer%22%3A730730786  
  
  
---|---  
  
Here, `asked_uid` is the `uid` of the person you asked and `viewer` is your `uid`, I tried changing viewer uid, but, obviously it didn’t worked(it’s not that easy IDOR). So I started checking here, which specific thing is responsible for telling that it’s me (Maybe I can overwrite that). My gut feeling was saying there can be a bug, because if we can enumerate `uid` to get the details, then why the same we can do here.  
So I left this part here and went to find the solution for that, by checking other things. I observed that in the one place `uid` parameter is given at `kwargs`, then I remembered back that, we could have actually do it, yeah, then I went back and tried adding one more parameter(`uid`) in `kwargs`, but it didn’t worked, okay, now I tried with `args` and guess!! HURRAY!! The `uid` got overwrite.  

  
  
  1  
  2  
  

| 
  
  
  json=%7B%22args%22%3A%5B<PUT_VICTIM_UID>%5D%2C%22kwargs%22%3A%7B ......  
  
  
  
---|---  
  
I was happy on that moment because this can be a bug because I can request for any Question to anyone on the Quora, also from account of most followed person, celeb etc.  
I was doing this testing in my working days, so I had classes, so on the way to my college, one idea clicked that was, while giving Answer or Ask Question if I can overwrite `uid`. But the problem was I had to wait for 3hrs (because of my class). As the class ended, I ran for the lab, takeout the laptop and tried it and guess what!!! IT WORKED!!! I got the critical bug… Now, I can put answers to any questions, ask any questions from a different account. 

Instantly, I reported this bug through HackerOne to Quora and they fixed it in less than 4hrs and awarded me the bounty next day. 

Thanks for reading it, I hope you get fun reading.

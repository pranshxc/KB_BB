---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-29_the-100-million-person-data-disclosure.md
original_filename: 2023-01-29_the-100-million-person-data-disclosure.md
title: The 100+ Million Person Data Disclosure
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
raw_sha256: 5aa080ea22b7f8cc25756b312e80a8931d063cd9b5d64b5a97a404cd481da376
text_sha256: 4e77e033423e56603d79fba899eb6fc5a5b488db22a92c5621571c894737a04d
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# The 100+ Million Person Data Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-29_the-100-million-person-data-disclosure.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `5aa080ea22b7f8cc25756b312e80a8931d063cd9b5d64b5a97a404cd481da376`
- Text SHA256: `4e77e033423e56603d79fba899eb6fc5a5b488db22a92c5621571c894737a04d`


## Content

---
title: "The 100+ Million Person Data Disclosure"
url: "https://www.jhaddix.com/post/the-100-million-person-data-disclosure"
final_url: "https://www.jhaddix.com/post/the-100-million-person-data-disclosure"
authors: ["Jason Haddix (@Jhaddix)"]
bugs: ["IDOR"]
publication_date: "2023-01-29"
added_date: "2023-02-07"
source: "pentester.land/writeups.json"
original_index: 1608
---

# The 100+ Million Person Data Disclosure

  * [Jason Haddix](https://www.jhaddix.com/profile/jhaddix56/profile)
  * Jan 29, 2023
  * 2 min read

  

  

![](https://static.wixstatic.com/media/abefef_b7561b1c1ac84ab189fee6784a7e1e5d~mv2.png/v1/fill/w_49,h_23,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/abefef_b7561b1c1ac84ab189fee6784a7e1e5d~mv2.png)

  

  

Or, That time I hacked a whole country by accident! 

  

I have done consulting gigs all over the world for security testing, and I frequently travel to speak at international conferences. 

  

Here’s a story about how I found a vulnerability that could have allowed me to steal the private information of over 100+ MILLION people. 

  

This is by far the biggest (in the number of people impacted) hack I’ve ever done… and it wasn’t even for work. 

  

Not too long ago I was planning on traveling out of the states for work, so I needed a VISA.

  

If you’ve ever applied for one you know that some countries pass this service off to 3rd party providers to do. This one did not. They had a government office and website to do passport verification, and application to get a VISA. 

  

I did the whole process. I created an account, uploaded all my passport info, answered personal questions, uploaded photos, etc. Somewhere at the end of the process was asked if I wanted to pay for a “rush” service. I did. I also entered my credit card info.

  

Toward the end of the application process, I was given a link to check my order status, something like: 

  

> [https://threat.dev/app/orderCheck](https://t.co/Bby3uwFcPW)

  

This page prompted me to log in using the credentials I had set up earlier. Then it redirected me to my account section which showed the page my order status.

  

In addition to this, there was an export to PDF button. Clicking this brought up a printable page of all my info referenced above. 

  

I hovered over the button and the link looked like so:

  

> [https://threat.dev/app/p](https://t.co/Bby3uwFcPW)rintApplication?id=105608983 

  

  

So… even when I’m not working, my hacker brain never turns off. 

  

That number, 105608983, what if I changed it to 10560898**2**? The number right before me? Surely the application would recognize that was not my id, and give me an error right?

  

Unfortunately for them, and for all the applicants before me, the change worked

  

Requesting: 

  

> [https://threat.dev/app/printApplication?id=105608982 ](https://t.co/1emQ78aC0T)

  

Returned another user’s personal information. Big sad.

  

This type of web vulnerability is typically called an IDOR (an Insecure Direct Object Reference). 

  

Since I found this bug totally outside of work, I started to get **very nervous** about finding such a big bug on a foreign gov site to which I was traveling.

  

I had to find a way to disclose it responsibly without getting in trouble. I reached out to several friends in the information security scene. 

  

Luckily one of them knew someone who worked in Cyber Security for that government. They asked that I pass along a written report. I did. 

  

I then worked with them to retest the issue once a fix was put in place. 

  

I discovered four more vulnerabilities in this process, one of which was that the database was being backed up in a tar file to the same place user images were being uploaded. This directory had no authentication or access controls on it. The database had some credit card numbers in it. Big Sad [#2](https://www.jhaddix.com/blog/hashtags/2) for them.  If you’re a security tester reading this, always check /backup or check for backup zip/tar files.

  

In the end, they were thankful for the disclosure & my work. My travel went without a hitch. 

  

I didn’t even get a t-shirt but, I might have saved someone's personal data from evil hackers!

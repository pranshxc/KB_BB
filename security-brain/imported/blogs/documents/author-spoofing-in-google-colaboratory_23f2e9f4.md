---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-09_author-spoofing-in-google-colaboratory.md
original_filename: 2021-06-09_author-spoofing-in-google-colaboratory.md
title: Author spoofing in Google Colaboratory
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 23f2e9f4c02496fa541055bbac0a4242823575cdedd8f1c7c58378adb7b9f639
text_sha256: f1a42765984a16002db68d8bb4bf1ccaa49de465f3f8a9568d758f5c2264d657
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Author spoofing in Google Colaboratory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-09_author-spoofing-in-google-colaboratory.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `23f2e9f4c02496fa541055bbac0a4242823575cdedd8f1c7c58378adb7b9f639`
- Text SHA256: `f1a42765984a16002db68d8bb4bf1ccaa49de465f3f8a9568d758f5c2264d657`


## Content

---
title: "Author spoofing in Google Colaboratory"
url: "https://www.ehpus.com/post/author-spoofing-in-google-colaboratory"
final_url: "https://www.ehpus.com/post/author-spoofing-in-google-colaboratory"
authors: ["Zohar Shachar"]
programs: ["Google"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2021-06-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3590
---

# Author spoofing in Google Colaboratory

  * zohar shachar
  * Jun 9, 2021
  * 3 min read

Recently, Google made public their new ‘[ _Abuse Research Grant Program_](https://security.googleblog.com/2021/06/announcing-new-abuse-research-grants.html) ’ - an awesome tool for motivating researchers to delve into an often overlooked angle of software security that doesn’t get the attention it deserves. 

I was very honored to be mentioned as a contributor to this effort, and I thought this is a good opportunity to write about one the first abuse-related bugs I’ve ever reported to Google - an identity spoofing issue in [_Google Colaboratory_](https://colab.research.google.com/) that allows you to bypass security warnings and trick victims into running your malicious code on their own environment. 

Let’s dive right in.

  

**What is Colaboratory anyway?**

Google Colaboratory is a powerful tool for running [_Python-Jupyter-Notebook_](https://jupyter.org/) ’s. Essentially, you can easily write python code and execute it in a ‘serverless’ environment (a new container is spawned for every new session). If you want to persist data, you can integrate your code with other Google products (such as Drive, Docs or Big Query), and you can also share code with your peers (just as you would share any other Google document). 

  

At this point, you’re probably thinking “well I’d be careful before running code written by someone else in my own environment”, and Google thought so too. And so, when you try to execute a notebook owned by someone else you face a very clear warning:

  

![](https://static.wixstatic.com/media/5527e6_e259bb52f78c47d190e0de240d2c6d56~mv2.png/v1/fill/w_49,h_18,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_e259bb52f78c47d190e0de240d2c6d56~mv2.png)

If you were a malicious entity trying to get some victim to execute your code, such a warning might be a serious blocker, as even the most naive of users might think twice when facing such an alert.

  

**Can we bypass it?**

If you pause to think about this alert message, a question may pop in your minds (or at least it popped in mine). As mentioned before, Google Colaboratory notebooks are shared just like any other document in Google drive, and can have several contributors. in fact, in order for the victim to even access this code and try to execute it, we had to initially share it with the victim and make him/her sort of a contributor. So, if we have several potential users writing code to the notebook, who’s the ‘Author’ mentioned in the alert message? 

  

Once the question was formulated in my mind the answer was also clear - the ‘author’ must be the original user who created the document - or in Google Drive’s lingo - the document owner.

  

But there’s the rub - a document owner in Google Drive is not constant, and can be changed - an owner can simply appoint some other contributor as the new owner.

(This makes sense - imagine you work with a colleague on some document authored by them, and then they leave the company and close their account. It wouldn’t make sense for the shared doc to just disappear, would it? Someone else will have to become its new owner. But that could not be determined ‘automatically’, and it only makes sense for the current owner to choose the future one). 

And indeed, quick testing showed that Colaboratory notebooks are managed just like any other Google doc, and using Google Drive’s settings you can change their owner (i.e. the 'author') to any of the contributors to the file. 

  

So now we have all the pieces of the puzzle, the attack becomes clear:

  * Create a new notebook in Colaboratory, and write your malicious code in it.

  * Share your notebook with your victim.

  * Using Google Drive, locate your notebook and set your victim as the notebook owner. 

  * Send the link to the victim and you’re good to go!

I’ve reported the bug to the Google abuse team, who granted a cool 500$ bounty.

  

Here's A POC video of the attack, showing first the ‘normal’ behavior and then the ‘spoofed’ one (and many thanks to [_Moti Harmats_](https://www.linkedin.com/in/moti-harmats-b232aa98/) for adding the oh-so-magnificent soundtrack):

  

  

**Final thoughts**

I really like this bug, due to its simplicity. It’s not a technical bypass, it’s not a code error, it didn’t result in the biggest bounty ever and it doesn’t even require a computer to discover - but that’s why I like it. it’s one of these things that suddenly comes to your mind when you're out for a walk after a day of playing with a system, and once you think about it you know it will work, you don’t even need to test it. 

I reported it around a year and half ago, and wanted to write about it ever since. It was even meant to be the first writeup on this blog, but somehow other things got in the way.

Thanks again Google’s team for this cool new grant program, that motivated me into finally giving this bug the post it deserved :)

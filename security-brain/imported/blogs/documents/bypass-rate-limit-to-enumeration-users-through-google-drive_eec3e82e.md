---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-24_bypass-rate-limit-to-enumeration-users-through-google-drive_2.md
original_filename: 2021-03-24_bypass-rate-limit-to-enumeration-users-through-google-drive_2.md
title: Bypass rate limit to enumeration users through Google Drive
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: eec3e82e57a509a37ef3d1adaf6b298e755af3a2406fe5ff8884809f8211a75d
text_sha256: 1f4c9239af3b0bd05ee7e0633784fc4f0f52a613b75dea989543d29a31e36ceb
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass rate limit to enumeration users through Google Drive

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-24_bypass-rate-limit-to-enumeration-users-through-google-drive_2.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `eec3e82e57a509a37ef3d1adaf6b298e755af3a2406fe5ff8884809f8211a75d`
- Text SHA256: `1f4c9239af3b0bd05ee7e0633784fc4f0f52a613b75dea989543d29a31e36ceb`


## Content

---
title: "Bypass rate limit to enumeration users through Google Drive"
url: "https://3bodymo.medium.com/bypass-rate-limit-to-enumeration-users-through-google-drive-ed64e07c879c"
authors: ["Abdullah Mohamed (@3bodymo_)"]
programs: ["Google"]
bugs: ["Rate limiting bypass"]
publication_date: "2021-03-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3794
scraped_via: "browseros"
---

# Bypass rate limit to enumeration users through Google Drive

Bypass rate limit to enumeration users through Google Drive
Abdullah Abdelrazek
Follow
6 min read
·
Mar 24, 2021

358

3

Press enter or click to view image in full size

Hi
everyone, today I’m gonna took about vulnerability that I found it in Google. In fact, when I sent the report to Google, it wasn’t a vulnerability, but I will tell you how I escalated the risk and bypass rate limit.

At first, I browsed Google drive looking for feature to misuse it and I found this feature..

Press enter or click to view image in full size
The feature that allow you to share files

In short, this feature allows you to share the folder or content that you uploaded to a specific person or several people by sending an invitation via e-mail. So I entered an email and ran burp suite to see what happens when I send an invitation. When I opened burp, I found this interesting request..

Press enter or click to view image in full size
At the bottom of the request, there is the e-mail that I sent

When I looked at the response I found the first and last name and the link for the profile picture of the email owner.

Press enter or click to view image in full size
Personal information about the owner of the e-mail

it might seem interesting, but the Google policy does not consider this to be a kind of vulnerability, but bypass rate limit is vulnerability. So I created a file containing 500 username and sent this request to intruder so that I would know if there was a limited rate or not.

Indeed, the attack succeeded, and I sent the report to Google.

In fact, the report was accepted but I was told that 500 requests were not enough to prove that there was a vulnerability. So I opened my laptop and created a file containing 2000 username to try it, unfortunately I arrived at the request number 845 and after that it started showing me a message that I exceeded the limit rate. In fact, I looked a little frustrated and I shut down my laptop, then it occurred to me the idea of ​​what if we split the attack into more than one folder.

It was just an idea (I’ll explain the details in a moment), I quickly opened my laptop and wrote a comment on my report contains my idea that will allows me to do 500K requests. But actually, when I wrote this comment, I didn’t know how I exploit this attack! It was just an idea. And after less than 24 hours I got this comment from security team, they want PoC for the scenario I described and also they say should not be possible at all.

Press enter or click to view image in full size
Security team comment

Now I will explain the idea, when I made 845 requests and got message that I exceeded the rate limit, what if I send 845 requests and then make another folder and send 845 other requests, I tried it and it really worked. But it sounds like an impractical idea and will take a lot of time. So I thought of creating a small program that creates a folder and then sends 845 request and then creates another folder and sends another 845 request. In fact it seems like a good idea, but I am not good at programming to do a program like that.

After deep thought, a good idea came to my mind. I thought about creating 1000 folders and saving these folder names. And send 500 username per folder (I know that I can send it 845 time but I send it 500 only to avoid any possible error), and if we have 1,000 folders, we’re actually able to send 500K requests.

The server of Google doesn’t give same name that we gave, so you want get the folder name, you have two ways, via the folder’s invitation link or another way which I will mention shortly.

When this idea came to my mind, I did not know how to get the names of 1000 folders, at first I was planning to create a folder and check its invitation link and get the folder name from it, but it would take a lot of time so I thought of another way. I told myself why I don’t check the request that creates the folder, maybe I can find something that interests me. I actually sent the request to burp (the request of make a new folder) and surprisingly, the response contains the name of the folder I want, wonderful.

The first problem was solved ✅

Press enter or click to view image in full size
Folder name in response

Before I begin describing the attack scenario, I’ll give you a quick summary of my trick:

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I noticed that request is accept send it 845 times but this for one folder so I make 1000 folder and I send 500 request for every folder, I know that I can send it 845 time but I send it 500 only to avoid any possible error, so I repeated each line 500 times in filename.txt to send 500 usernames with one folder and every folder I send it 500 time with different usernames, so until we can continue the process, and I guess that this process can be done indefinitely as long as I make 500K requests and the server didn’t stop me.

Now that we have everything done, let’s start the attack.

First we will create 1000 folders by sending a request of making a new folder to intruder.
Press enter or click to view image in full size
The request of make a new folder
Then we will set the payload 2–1000.

Remember we will create 1000 folders only to prove the vulnerability, but we can create more than that and also we can do more than 500K requests.

Press enter or click to view image in full size
Payload setting
Now we have to capture folder names from the response, so we will go to Options tab - Grep Extract - Add and choose the value of id to capture folders names from all the requests that we will send.
Press enter or click to view image in full size
Grep Extract setting
After running the intruder, we will have 1000 filenames, which we will put into a txt file. Now we have to repeat each name 500 times. So I looked for a way to repeat each line in a text file a certain number of times, and I found this simple command line..

perl -ne ‘for$i(1..500){print}’filename.txt | tee output.txt

Press enter or click to view image in full size
Here is a id column contain names of the folders, simply click anywhere in the white space next to the column, then press on Ctrl + A and it will select all and then press on Ctrl + C and it will copy them
Now we will go to burp again and send the request that invite person via e-mail to intruder. We’ll choose the folder name as payload number one and we’ll choose the username as payload number two.
Press enter or click to view image in full size
The request of invite person via e-mail

Now everything is ready. Indeed, the attack succeeded and I submitted the PoC to Google and got a 🎉 Nice catch! But unfortunately, three weeks later I was told my report was ineligible for bounty, but I was added to HOF.

Press enter or click to view image in full size
Attack operation

Thanks for your reading, I hope my story was useful.

Timeline:

[Jun 27, 2020] - Bug reported

[Jun 29, 2020] - Triaged

[Sep 15, 2020] - 🎉 Nice catch!

[Feb 23, 2021] - Won’t Fix

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-07_a-tale-of-5250-how-i-accessed-millions-of-users-data-including-their-national-id.md
original_filename: 2022-01-07_a-tale-of-5250-how-i-accessed-millions-of-users-data-including-their-national-id.md
title: 'A Tale Of 5250$: How I Accessed Millions Of User’s Data Including Their National
  ID’s'
category: documents
detected_topics:
- cloud-security
- command-injection
- otp
- automation-abuse
- information-disclosure
- mobile-security
tags:
- imported
- documents
- cloud-security
- command-injection
- otp
- automation-abuse
- information-disclosure
- mobile-security
language: en
raw_sha256: 7d72f18abb91688691f4628d92c67b8c58a939f7e5a6352a1f9a3eea68ad0483
text_sha256: 2121e5c574ecad124462097a740169653ef3949c2ec9ee6b4e1d118d807d4eeb
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# A Tale Of 5250$: How I Accessed Millions Of User’s Data Including Their National ID’s

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-07_a-tale-of-5250-how-i-accessed-millions-of-users-data-including-their-national-id.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, otp, automation-abuse, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `7d72f18abb91688691f4628d92c67b8c58a939f7e5a6352a1f9a3eea68ad0483`
- Text SHA256: `2121e5c574ecad124462097a740169653ef3949c2ec9ee6b4e1d118d807d4eeb`


## Content

---
title: "A Tale Of 5250$: How I Accessed Millions Of User’s Data Including Their National ID’s"
page_title: "Abc | InfoSec Write-ups"
url: "https://infosecwriteups.com/a-tale-of-5250-how-i-accessed-millions-of-users-data-including-their-national-id-s-fd48ca7ca0bf"
authors: ["Sam (@__Sam0_0)"]
bugs: ["AWS misconfiguration", "Information disclosure"]
bounty: "5,250"
publication_date: "2022-01-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3023
scraped_via: "browseros"
---

# A Tale Of 5250$: How I Accessed Millions Of User’s Data Including Their National ID’s

A TALE OF 5250$: HOW I ACCESSED MILLIONS OF USER’S DATA INCLUDING THEIR ADDRESS AND PERSONAL INFO
Sam
Follow
3 min read
·
Jan 7, 2022

297

Hi, Hope you guys are doing well, And a Happy New Year, YAY! ✨, Let’s start the blog without wasting more time.

As usual, I am hunting in Tecno src program for something in the source code of the application, As the scope is huge, So I collected all the applications and decompiled them all at once with apktool with this command: find . -iname “*.apk” -exec apktool d -o {}_out {} \;

(Yah it will take a good amount of time to decompile 🥲)

FINDING THE BUCKET :

Now I started to look for something juicy in decompiled files, but as there are

about 50+ applications, I can’t look at each of them manually right? I just got an idea of nuclei, and boom I knew there are templates for android applications,

I just downloaded them and, started nuclei on the whole directory😅

Command for that : nuclei -target /path-to-output-folder/”android testing”/allapks/ -t /path-to-tamplates/mobile-nuclei-templates/

After 18–19 mins of a run, Nuclei gave an output saying S3 Bucket Found, I tried to access it via AWS CLI, and it's like: Acess denied 😔, No luck there.

Get Sam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then after a few mins of running, I've got one more output for s3 bucket, I casually tried to access it without any hope, and damn! the s3 bucket is full of juice, And I was just like :

I just simply got access to tecno's data of internal files, Users, and everything they have, I can download everything, Even the whole bucket 😂.

Here is just a glimpse of the data: Now I am damn sure that the bucket is full of juice. Ahh, I wanted to look at more files but as we have to follow bug bounty rules I stopped doing more and directly reported to the team.

Now, After reporting it, I've got one more s3 bucket with nuclei, And it also contained about 4–5 gigs of data 😳

I've reported it too, But don't know why the team said “ both s3 buckets are managed by the same team” so they merged my report to the previous one 😔, I did not expect something like this😔, I tried to convince them they cant merge it, But they just did it😔 But they gave me extra 25 reputations on the program and moved the report to critical, which is still very less for what I just found! Guys, can you say they are right or wrong here for merging different reports? Write down in comments so the team can see 🥲, I’ve rewarded 5250$ for only one report and 0$ for the second one, Even it contained so much sensitive data🥲, I want to say that, I haven't downloaded any file from the buckets, I only downloaded one file from tecno's server to send it with the vulnerability report, now they fixed the server and, no one have any access to the data, and all the data of people is safe.

Links :

Nuclei: https://github.com/projectdiscovery/nuclei Thanks to projectdiscovery

Android templates for nuclei: https://github.com/optiv/mobile-nuclei-templates

APKTOOL: https://github.com/iBotPeaches/Apktool

Thanks, guys for reading, I hope you enjoyed it, and please ignore any mistakes and my grammar too😅, You guys can follow me on Twitter: @__sam0_0

I will publish more writeups soon stay tuned!!! YaY🔥

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-19_passive-recon-with-spyse-part-ii.md
original_filename: 2022-02-19_passive-recon-with-spyse-part-ii.md
title: Passive Recon with Spyse (Part-II)
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 3febcb73b451ad1cb4008ee8ceb8e859653b0a2d686ca82f5d4a77840a38485f
text_sha256: af4ae722a6e5e82486f06807d9d07ad6b99bf1c1aa5ce6e8a85695b0a3565caf
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Passive Recon with Spyse (Part-II)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-19_passive-recon-with-spyse-part-ii.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `3febcb73b451ad1cb4008ee8ceb8e859653b0a2d686ca82f5d4a77840a38485f`
- Text SHA256: `af4ae722a6e5e82486f06807d9d07ad6b99bf1c1aa5ce6e8a85695b0a3565caf`


## Content

---
title: "Passive Recon with Spyse (Part-II)"
page_title: "Passive Recon with Spyse (Part-II) | remonsec"
url: "https://remonsec.com/posts/passive-recon-with-spyse-part-II/"
final_url: "https://remonsec.com/posts/passive-recon-with-spyse-part-II/"
authors: ["remonsec (@remonsec)"]
bugs: ["Subdomain takeover", "AWS misconfiguration"]
bounty: "2,100"
publication_date: "2022-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2889
---

## Passive Recon with Spyse (Part-II)__

**بسم الله الرحمن الرحيم**

Assalamu Alaikum peace be upon you

## Introduction __

In part-1 I showed mass attack technique like subdomain takeover. in part-2 I will show some more about mass attacks and also about specific target recon. Last week I get some bounties by doing my recon with[Spyse](https://medium.com/u/943b150c124e?source=post_page-----3d6bce47365-----------------------------------). Let me share my experience with you

## Mass Attack __

So last time we saw some mass subdomain takeover

[](https://postimg.cc/CnR5JzWV)

what about other issues ! let me share a query that [**Markroze**](https://twitter.com/_markroze) shared with me

[](https://postimg.cc/34YgZZts)

[](https://postimg.cc/HrMXDNRG)

we can search for specific things. like here we have WATTrouter service you can do more query like jira, openvpn, wordpress so and so on But this act can be extremely evil hacking on random assets makes no sense.

Now it’s time to filter those things to find out websites with responsible disclosure policy

[](https://postimg.cc/7bbCrcJB)

Download your search result in CSV format, cut the end url and bruteforce the list with some common disclosure endpoint You may need a pro account to download your search result.

[](https://postimg.cc/gxyjKb10)

After that you can FUZZ like this to get out all hosts with disclosure program **NOTE** : FFUF -mr flag not working properly for me. If you face similar let me know, btw you can do similar with bash, python . . .

[](https://postimg.cc/JGLW5H8b)

Okay enough. we are done with mass attack things. do your own research to find out more interesting query and attacks.

## Recon your Target __

[](https://postimg.cc/7C6CPQQY)

After searching your target you will see things in crawler section. there’s a panel called related. that one really helps. you will see similar data there like if any other host is using similar icon of your target website

[](https://postimg.cc/TKZwGYmQ)

You will be getting AWS buckets that target company use to host assets. Now you can look for access control issues for those buckets. you will also get interesting 3rd party hosting services that your target may using for their asset hosting or any other work. so those 3rd party hosts also can lead security issue for your target

[](https://postimg.cc/VJbf7QTt)

If you move into DNS history & related category again you will see some options there to look into. This feature of Spyse helped me to earn some $cash last week

[](https://postimg.cc/4KJ0Ypz3)

webapp hosted on server from Canada was secure but same webapp hosted from US server was vulnerable with multiple server side attacks. That program was live from 2014. In 2021 they resolved 10 reports 6 of them is mine.

[](https://postimg.cc/2VD7jrdk)

[](https://postimg.cc/5Yz81R6Q)

[](https://postimg.cc/9zJy2Zfp)

[](https://postimg.cc/xkvb4b7L)

[](https://postimg.cc/xJjqppLS)

[](https://postimg.cc/PLy5Db9V)

No one was looking there so it was easy for me to find bugs.

I attached all reward and resource screenshot as reference material. You should not believe in a random boy from internet at all. There should some kind of proof what I am saying.

Now some will show offence that I am doing show off, if I don’t attach screenshot then also some will show offence that I am not telling the truth.

Whatever I am leaving it to you, you can show love or hate it’s your choice I am already broken so it make no changes to me :)

Those are things I found interesting for BugBounty hunters on [Spyse](https://medium.com/u/943b150c124e?source=post_page-----3d6bce47365-----------------------------------). You also can look into your own for other features. This recon writeup series sponsored by Spyse. They offered me their pro account to use and let them know my feedback about their service.

You can see it your own how I used [Spyse](https://medium.com/u/943b150c124e?source=post_page-----3d6bce47365-----------------------------------) for BugBounty stuff and earned some cash. Thanks [Spyse](https://medium.com/u/943b150c124e?source=post_page-----3d6bce47365-----------------------------------) for the sponsorship and your amazing service

I am ending this writeup here. If you have any question you can ask me on Twitter at this handle **remonsec**. If you have general questions then instead of DM you can mention me on your tweet. So other also may get benefit from your question or if I don’t know the answare I may mention someone who knows

Have a sweet day everyone Allah Hafiz

[](https://postimg.cc/cgtPW0R7)

* * *

wanna support my work! well just buy me a coffee

[](https://www.buymeacoffee.com/remonsec)

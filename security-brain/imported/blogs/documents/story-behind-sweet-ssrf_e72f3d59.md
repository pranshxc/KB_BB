---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-21_story-behind-sweet-ssrf.md
original_filename: 2021-01-21_story-behind-sweet-ssrf.md
title: Story Behind Sweet SSRF.
category: documents
detected_topics:
- ssrf
- xss
- cloud-security
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- xss
- cloud-security
- command-injection
- api-security
language: en
raw_sha256: e72f3d590aff2753ef5ec37e948b00e0fa7eb22cfe16cd4ce3faabe098a6700c
text_sha256: 0b21d1506dad11d8fcef592efbec1bb7ee20d152b0a4129cb6ae076b9a2bbc00
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Story Behind Sweet SSRF.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-21_story-behind-sweet-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, cloud-security, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `e72f3d590aff2753ef5ec37e948b00e0fa7eb22cfe16cd4ce3faabe098a6700c`
- Text SHA256: `0b21d1506dad11d8fcef592efbec1bb7ee20d152b0a4129cb6ae076b9a2bbc00`


## Content

---
title: "Story Behind Sweet SSRF."
url: "https://systemweakness.com/story-behind-sweet-ssrf-40c705f13053"
authors: ["Rohit Soni (@streetofhacker)"]
bugs: ["SSRF", "XSS"]
publication_date: "2021-01-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3979
scraped_via: "browseros"
---

# Story Behind Sweet SSRF.

Story Behind Sweet SSRF.
Rohit Soni
Follow
5 min read
·
Jan 20, 2021

619

6

Persistence is the Key to Success.🔥

Hey everyone! I hope you all are doing well!

Rohit soni is back with another write-up and this time it’s about critical SSRF which leads to AWS credentials disclosure. Let’s dive into it without wasting time.

Couple of months back when there was lockdown in whole world due to COVID-19 pandemic I was spending my most of time in hunting, learning and exploring new stuff (specifically about pentesting😜).

One day while scrolling linkedin feed I saw one guy’s post saying got hall of fame in target.com website. The post caught my attention and as I was not hunting on any program I started hunting on that program.

Note: I am not allowed to disclose the target website. So, Let’s call it target.com

I created an account on target.com and started exploring every functionalities. After spending couple of hours hunting and exploring functionalities I saw my email address was reflected in the response in script tag as shown in below image.

Look at that email address.

Ahh… Very first thing came into my mind was XSS. I changed my email address to testacc@hubopss.com‘-alert(“h4ck3d!!”)-’ But failed because it is not a valid email address. But In very next moment I intercepted the request using burp and changed my email address in intercepted request and forwarded it.

Boom….Got Stored XSS.

Press enter or click to view image in full size
XSS is Love❤ (Sorry for poor picture quality😅)
Payload reflected without filtering/encoding/sanitizing special characters.

Root cause of this XSS was lack of input validation at server side. Website was validating email address at client side only that’s why it did not allowed me to directly input my payload in email field but as server was not filtering out or encoding special characters my payload stored and I got the pop-up.

Okay, That’s cool but where is the SSRF you promised !? 😐

Main Story begins from here.

Stored XSS is nice finding but hacker inside me was screaming “You can find critical, I want P1😜”. So, I kept hunting and came across the functionality that allows to export user inputted text in pdf file.

After seeing this functionality I remembered a write-up which was about ssrf by abusing pdf generator functionality. I have not read the write-up but I remembered the title. I quickly googled the title and found the right write-up, I read and applied the same.

Identification Part :

I was able to figure out that Custom cover page content field was vulnerable.

Press enter or click to view image in full size

What I did was, I supplied <center><u>hello there</u></center> HTML tags as an input in Custom cover page content field and exported as pdf. and I got something very interesting.

Press enter or click to view image in full size
Ahh….Interesting..!!

As you can see in above screenshot, it accepted HTML tags and generated the pdf according to supplied HTML tags. Interesting..!!

Next step is to check if its vulnerable for SSRF. I confirmed that generate pdf file functionality is vulnerable for SSRF using <iframe> tag and burp collaborator client. Payload I used was:

<iframe src=“http://something.burpcollaborator.net”></iframe>

Press enter or click to view image in full size
Woah, SSRF Identified. {^_^}

HTTP request from target server is logged into my burp collaborator client window. Woah, SSRF Identified.

Root Cause: <iframe> tag used to embed/load website into another website. While generating pdf file, the target server requested my burp collaborator client to load it into <iframe> tag. As a result I got request logged into collaborator client.

Still, This SSRF does not has much impact. Let’s exploit and see what we can achieve by exploiting this SSRF.

Exploitation Part

To exploit this SSRF I used following payload.

<iframe src=“http://localhost”></iframe>

But unfortunately it doesn’t worked and showed me blank pdf file.

Press enter or click to view image in full size
Failed. -_-

After that I though to load files stored at server side. For example, /etc/passwd file. To do that I built following payload.

<iframe src=“file://etc/passwd”></iframe>

But again bad luck. Got same blank pdf file.

Get Rohit Soni’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used different different payloads to exploit the SSRF but I failed. Few of them are as follows. (I failed doesn’t mean you will also. Try your luck😉)

<iframe src=“file://etc/shadow”></iframe>

<iframe src=“http:localhost”></iframe>

<iframe src=“//192.168.0.1”></iframe>

<iframe src=“http://127.0.0.1”></iframe>

Any of the above payload was not working for me. Then, I thought to check the IP address which got on burp collaborator client on shodan and I came to know that the website is running on Amazon EC2 machine.

Website is Hosted on Amazon EC2 Instance.

After considerable amount of fail attempts. I took a break and thought to ask to ritik sahni. He is my good friend and 15yo talented hacker. I called him and told him whole scenario.

He took few minutes and replied, Try to load following URL in iframe source: http://169.254.169.254/latest/meta-data/

As soon as I did it, I was like, Woah!! I got their internal directories and files listed out in iframe.

Press enter or click to view image in full size
Got Internal Directories and Files.

You must be wondering from where 169.254.169.254 IP address came.!

The IP address 169.254.169.254 is a link-local address and is valid only from the instance. In simple terms, We can say this IP is localhost for your EC2 Instance.

and by using http://169.254.169.254/latest/meta-data/ we can retrieve instance metadata.

Then, Ritik told me to check iam/ directory. I was able to get AWS security credentials from iam directory. Have a look at below attached PoC.

Press enter or click to view image in full size
Payload

Final Payload:

<iframe src=“http://169.254.169.254/latest/meta-data/iam/security-credentials/Worker” width=“100%”></iframe>

Press enter or click to view image in full size
SSRF PoC 😍🔥

It took me around 4 hours to identify and exploit SSRF. Special thanks to my friend Ritik Sahni (@deep.tech).

Hope you enjoyed my story. If you have any questions or suggestions reach me through instagram, twitter or linkedin.

Happy Hunting. :-)

Instagram: @street_of_hacker

Twitter: @streetofhacker

LinkedIn: Rohit Soni

Special Thanks to Ritik Sahni: @deep.tech

And also Thanks to target.com for amazing swags.😁

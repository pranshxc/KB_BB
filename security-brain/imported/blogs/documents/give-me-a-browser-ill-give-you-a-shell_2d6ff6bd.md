---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-25_give-me-a-browser-ill-give-you-a-shell.md
original_filename: 2023-02-25_give-me-a-browser-ill-give-you-a-shell.md
title: Give me a browser, I’ll give you a Shell
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
- path-traversal
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
- path-traversal
- information-disclosure
- api-security
language: en
raw_sha256: 2d6ff6bda5bb447989eb11709560ed37f264d7d8b52b7140702f6c3beef050b1
text_sha256: 805717d90110837389e77de238716a8843ed0c7db0609203c3c717e9d0f054d9
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Give me a browser, I’ll give you a Shell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-25_give-me-a-browser-ill-give-you-a-shell.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection, path-traversal, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `2d6ff6bda5bb447989eb11709560ed37f264d7d8b52b7140702f6c3beef050b1`
- Text SHA256: `805717d90110837389e77de238716a8843ed0c7db0609203c3c717e9d0f054d9`


## Content

---
title: "Give me a browser, I’ll give you a Shell"
url: "https://systemweakness.com/give-me-a-browser-ill-give-you-a-shell-de19811defa0"
authors: ["Rend"]
bugs: ["Local Privilege Escalation", "Kiosk hacking"]
publication_date: "2023-02-25"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1472
scraped_via: "browseros"
---

# Give me a browser, I’ll give you a Shell

Top highlight

Give me a browser, I’ll give you a Shell
Rend
Follow
5 min read
·
Feb 25, 2022

756

13

A restricted browser, that’s all you have… what do you do?

Press enter or click to view image in full size

This is the scenario I was facing during a pentest. The target was a windows server, running a VDI — VMware Horizon.
you log into the VDI using your active directory account and get access to a limited browser that only allows you to use a single application, no internet connection.

Well, that’s a nice and secure way for employees to check their calendars or view the progress of their tasks.
but, as a red teamer, I need a shell, not a calendar.

ok, what do you do if the only thing you have access to is a browser?

well, you need to know with this only thing you can pwn a server if you know how to use it, the wrong way. 😏

Part One: Show Me What You Got
What about starting by reading the server’s files?
as long as we are not permitted to read them it’s considered as a LFI.
Ok, how?

you’ve already seen a URL, haven’t you? just for your knowledge, that’s what brought you to this article.
a URL has different parts:

Press enter or click to view image in full size
source: https://www.geeksforgeeks.org/components-of-a-url/

What I want to talk about is the very first part, schema or protocol.

the protocol indicates the set of rules that will decide the transmission and exchange of data.

In simpler words, protocol says how to treat the rest of the URI.
For example, the mailto protocol indicates that the rest of the URI is an email address. by clicking on a link like mailto:me@mail.com your browser opens a mail composing page in your default email application and sets the me@mail.com as the receiver's email address.

There is another cool protocol called file. By using that you can read files using a browser.
the first file I tried was the hosts file:
file:\\\C:WINDOWS\System32\drivers\etc\hosts

and as expected it returned the content of the hosts file.

Press enter or click to view image in full size

Cool… I mean just a normal behavior :)
but that’s very limited, you need to know the exact path of the file to be able to read its content.
A directory listing would have helped… Why not just ask for it?

The file protocol also shows the content of directories,
just if you give it the location of that directory, that simple.
Here’s a nice example: file:///c:/
enter it into the URL bar and it’ll list the content of C drive for you ✌

Press enter or click to view image in full size

Part Two: Files Are Good, But A Shell Is Better
I could read all the files on the server (almost), but I was still in the browser. I wanted to access the underlying OS, do you have any idea how to do that?

let me give you a hint:
What’s the procedure when you want to upload a file to a website?

Here’s where the story gets interesting…

when uploading a file, first you need to select that file, right?
The window that lets you select the file is an OS application and if you get access to this OS application you have access to some cool OS functionalities like creating and executing files.

ok, now should I start searching the web application and pray that I find an upload functionality? well, that might work.
but I choose a smarter way,
I create what I need: document.write('<input/type=file>')

Press enter or click to view image in full size

and…

Press enter or click to view image in full size

hehe, that was fun 😉

Get Rend’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PRO TIP
what if the devtools is disabled for any reason?
let me introduce you to another interesting protocol: javascript
if the browser is chromium-based you can enter this into the URL bar and get the same result: javascript:document.write('<input/type=file>')

ok, it’s give me my shell time…

The method I chose was to create a .bat file with the content cmd.exe
and execute it to get a shell.
you can create and execute files from this file picker window if you have the write and execute permission in the directory you are in.
but there can be a problem, if the file name extensions option is disabled you can’t change the file extension to .bat and execute it.
when the option is disabled:

and when enabled:

ok, let’s use a little trick here…

using Open in new window you’ll get access to the OS’s file explorer 🙃

From there you can change the file name extensions option and enable it. and then create and modify your file…

and… when black is the sexiest color 😎

Press enter or click to view image in full size

Ok, we got a shell, finished? no, not yet…

Part Three: Even More, Cus I’m A Hacker

what if you can’t open file explorer and enable the file name extensions option, or another kind of restriction?
let me help you, what do you see in this picture:

the ability to create a couple of different files? maybe.
but I see a reverse shell hidden among these options…

create a Microsoft Word Document,
open it,
Press ALT+F11,
and write your reverse shell code 🙂

Press enter or click to view image in full size

This is Microsoft Word’s scripting engine, you can write and execute
Visual Basic code using this functionality.
That’s the functionality social engineers use to penetrate an organization’s internal networks, using a phishing email and a malicious Word doc attachment.

Even More Restricted? you can’t create files?
find a Word doc on the server and edit it :)

PRO TIP
if you use a tool, learn all of its functionalities.

was it helpful?
I don’t ask you to buy me a cup of coffee,
teach me something…
Discord: REDN#9702

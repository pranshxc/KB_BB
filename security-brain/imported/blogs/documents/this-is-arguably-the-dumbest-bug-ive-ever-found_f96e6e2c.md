---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-02_this-is-arguably-the-dumbest-bug-ive-ever-found.md
original_filename: 2024-02-02_this-is-arguably-the-dumbest-bug-ive-ever-found.md
title: This is arguably the dumbest bug I’ve ever found.
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: f96e6e2cf962588246b9c7908a9cd84d0b8d2986cb201b59de6121484f0cb6c9
text_sha256: 01c3da001a8d7c5a7066a5f1291c9df845b6605a519689b5558a79cda742da67
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# This is arguably the dumbest bug I’ve ever found.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-02_this-is-arguably-the-dumbest-bug-ive-ever-found.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `f96e6e2cf962588246b9c7908a9cd84d0b8d2986cb201b59de6121484f0cb6c9`
- Text SHA256: `01c3da001a8d7c5a7066a5f1291c9df845b6605a519689b5558a79cda742da67`


## Content

---
title: "This is arguably the dumbest bug I’ve ever found."
page_title: "This is the dumbest bug I’ve ever found. | by Imad Husanovic | Medium"
url: "https://medium.com/@deadoverflow/this-is-arguably-the-dumbest-bug-ive-ever-found-3e451951d727"
authors: ["Imad Husanovic (@deadoverflow_)"]
bugs: ["Self-XSS"]
publication_date: "2024-02-02"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 462
scraped_via: "browseros"
---

# This is arguably the dumbest bug I’ve ever found.

This is the dumbest bug I’ve ever found.
Imad Husanovic
Follow
5 min read
·
Feb 2, 2024

390

7

Press enter or click to view image in full size

This is vulnerability I have found not so long ago and so far it is the dumbest issue I have ever discovered. Before I even start, if you are new here, I am deadoverflow and I put out educational content for free here on medium as well as on youtube. I also am in a process of writing a book on how do you use your knowledge about bugs or vulnerabilities to find them, the book will be free once I release it and hopefully that will be soon.

You can follow me here, or on @deadoverflow. I will be uploading educational videos on YouTube as well so don’t forget to subscribe not to miss anything out. With that said, let me start with this really funny and educative story.

So I was decided to do security research on a pretty much popular selling/buying website in my country. I have previously reported an account takeover vulnerability to the same website, you can read that here by the way, but now there was a new version of a website and everything was updated. Entire website got a new fresh look as well as some security improvements. Well, about security improvements, I am not sure if they improved.

When I created two test accounts I immediately wanted to test for XSS in message sending and receiving functionality that this website had to offer.

So I pasted in an input field what I usually paste when hunting for XSS just to see how would the web application handle my data: <><>”’<img src=xx onerror=alert(1)>. You can learn how I hunt for XSS here.

Press enter or click to view image in full size

So I just hit enter and this is what I saw.

Press enter or click to view image in full size

Not even a minute into my research, I found an XSS! I honestly was in disbelief since this is a pretty much popular website in my country used for buying and or selling products. XSS here would be really bad.

Well… As it turns out, this was as bad as I thought. See when I sent a message, an HTTP request was made to the server with the following payload:

Press enter or click to view image in full size

And in this is the response of this HTTP request:

Press enter or click to view image in full size

As you can see, my message was this: <><>\”’<img src=xx onerror=alert(1)> however this was the filtered message: &lt;&gt;&lt;&gt;\”’<img src=\”xx\” alt=\”xx\”>

Backend had a filter implemented where it removed the evil onerror attribute. But how? How did I see an alert pop up? I had to understand because it made no sense.

So I tried again, this time with: <img src=x onerror=alert(document.domain)>

Press enter or click to view image in full size

And again, when I sent this message, this is what happened:

Press enter or click to view image in full size

This honestly made no sense to me. How can I see an alert, when, clearly, backend was filtering messages properly.

Press enter or click to view image in full size

So I decided to get to the bottom of this, now I will be sending this as a message: <img src onerror=debugger;>

Get Imad Husanovic’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This will cause the chrome developer tools to pause then and there and allow me to inspect the call stack of what might’ve lead to execution of debugger;

Once I sent this, website froze and I could inspect what is happening in that instant.

Press enter or click to view image in full size

Here in the call stack, I will just click item right below onerror because that’s probably what caused code execution

Press enter or click to view image in full size

Here, the developer tools highlighted what caused the code execution so I will just click on that line to add a debugger there and inspect it further.

Press enter or click to view image in full size

Now I when I send any message, chrome will pause at this line of code, allowing me to inspect and see what is happening better.

Press enter or click to view image in full size

And as you can see in the image, a whole lot is actually happening, firstly we can see our payload right here being assigned as innerHTML of some element.

And just to make sure, we can observe this line of code that cause code execution even better at Console tab.

Press enter or click to view image in full size

So if I navigate to console and type out o, you can see where my XSS payload is being added to as innerHTML

Press enter or click to view image in full size

And value being added here to this element is exactly my payload.

Press enter or click to view image in full size

And I solved the mystery of self XSS vulnerability that I found and reported.

Honestly this design is really stupid. This is why I labeled this as dumbest bug I have ever found. Also implementing a filter on the backend is a terrible idea due to mutation XSS.

Using chrome developer tools was the reason why I have found so many different vulnerabilities and I recommend you do the same. I will be continuing to post regularly content that you could learn something from for free since I firmly believe everything would be much more secure only if some knowledge was given away for free.

Thanks for making it till the end and until the next time, goodbye!

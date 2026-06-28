---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-12_how-i-hacked-redbus-an-online-bus-ticketing-application.md
original_filename: 2020-09-12_how-i-hacked-redbus-an-online-bus-ticketing-application.md
title: How I hacked redbus [An online bus-ticketing application]
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: 2fad5d3653931550c0d128f03fa6d7b4b3410c70eea6e9b85802eb6361ba6a4e
text_sha256: ce7a940400acf542d8605a27e3e4e740853065c734774f5e03621c54679e06c3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked redbus [An online bus-ticketing application]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-12_how-i-hacked-redbus-an-online-bus-ticketing-application.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `2fad5d3653931550c0d128f03fa6d7b4b3410c70eea6e9b85802eb6361ba6a4e`
- Text SHA256: `ce7a940400acf542d8605a27e3e4e740853065c734774f5e03621c54679e06c3`


## Content

---
title: "How I hacked redbus [An online bus-ticketing application]"
url: "https://medium.com/bugbountywriteup/how-i-hacked-redbus-an-online-bus-ticketing-application-24ef5bb083cd"
authors: ["Sangeetha Rajesh S (@rajesh_sangi12)"]
programs: ["redBus"]
bugs: ["LFI", "SSRF"]
publication_date: "2020-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4267
scraped_via: "browseros"
---

# How I hacked redbus [An online bus-ticketing application]

How I hacked redbus [An online bus-ticketing application]
Sangeetha Rajesh S
Follow
5 min read
·
Sep 12, 2020

526

5

[I drafted this writeup 2 years ago. As it took a long time for the patch, posting it now]

It was a usual fresh and sleepy monday morning . I reached my desk and checking mails.

😴few minutes passed..

☎️ My Phone rang..

I thought thats a usual call from customer care. No. It was my mom (The only two souls who calls me daily 😅). She called me to remind about ticket booking for the weekend. That’s how it all started.

I booked the tickets and finally reached the confirmation page and clicked on something that I’ve never did before. The “Print/Download” link.

Press enter or click to view image in full size

On clicking the link , I got redirected to some other subdomain “pdf.redbus.com” which displayed the pdf version of my ticket.

Press enter or click to view image in full size

One important thing that got my attention was the “PD4ML” . The name
(PD-4-ML) itself says its a library for something. The most obvious case is it should be pdf generation library. But wait. How come it shows the pdf without any ticket ID or any equivalent identifier as a parameter 🤔. So i just went back to the previous page and monitored all the requests triggered after clicking the “Download” Link.

Here’s what I got ,

Press enter or click to view image in full size

So this is how they generate the pdf. From html content to pdf. First, to verify that the server makes a external call during the transformation, I tried the following tag,

<img src=”http://listener.myserver.com”>

Woot. 😃 I got a request from a java agent . Obviously that’s from redbus pdf server.

Press enter or click to view image in full size

At the next moment I tried iframe tag to check if it load the local files on the frame. All I got was a blank response. 😐

Press enter or click to view image in full size

Googled about pd4ml — whether it supports javascript(for dynamic pages). The answer is NO!
Without giving up, I started looking at the documentation of pd4ml. What I found was the iframe tag is not supported by pd4ml and some other tags like object, applet is also not supported.

Now what 😕. Scrolled down the documentation page. And found this interesting thing called “Proprietary tags”.

Started experimenting this <pd4ml:attachment> tag. As per the documentation it is used to embed attachments to the pdf. Now thats sounds interesting 😉. The tag expects a “src” attribute for the attachment link.

Simply modified the tag like this ,

<pd4ml:attachment src=”file:///etc/passwd”><pd4ml:attachment>

Voila 😲.

Press enter or click to view image in full size

At this point I confirmed the arbitrary file ready vulnerability. But I wasn’t very much satisfied with the passwd file. Digged further.
Fortunately, I could see the directory names too. So it was easy to jump to the directories.

Press enter or click to view image in full size
Press enter or click to view image in full size
partially redacted private key file

Now that looks like some real stuff 👻 . SSH private keys , config files with database passwords and mysql_history having some juicy information😜.

Get Sangeetha Rajesh S’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And the other user’s pdf tickets should be here somewhere 🤔.

Having arbitrary file read in hand, I’ve checked the source of the of the index.jsp and found where exactly the pdf files are stored.

Went to the directory and finally got this. 😍

Press enter or click to view image in full size

Its not about the pdfs. Its about the ticket IDs you got 😉

With the ticketID , any authenticated user can extract PIIs like email , Mobile number, Age , DOB (If available) etc.,

Press enter or click to view image in full size
partially redacted response

Takeaways:

For Bug hunters,
Always look at the documentation once you deduce the backend library using your recon.

For developers ,

Here’s the config you need to add to whitelist the local directory or remote resource

 Map m = new HashMap(); 
 m.put(PD4Constants.PD4ML_ALLOWED_RESOURCE_LOCATION, “http://server/webapp,file:/my/safe/file/folder"); 
 pd4ml.setDynamicParams(m);

Timeline:

[October 15, 2018] Issue reported to redbus.
[October 15, 2018] Redbus team immediately removed SSH Private keys as an immediate fix as soon as they acknowledged the issue.
[October 16, 2018] Reported the additional information that it also leaks user’s PII and it was considered to be duplicate as they were already tracking it as a separate issue.
[October 16, 2018] Got a nice bounty 🤥
[December 6, 2018] Redbus security team asked me to report it to pd4ml to get a CVE assigned for this issue if its reproducible in latest version .
[December 14, 2018] Sent an email to pd4ml to report the issue.
[December 19, 2018] Meanwhile , Got a mail from redbus security saying that they planned to remove the functionality
[January 4, 2019] After back to back emails with pd4ml I came to know that they’ve already got optional controls to avoid this issue and forwarded that to rebus team.
[February 26, 2019] Any updates ? — No Not yet.
[September 20, 2019] Any updates? — Patch will be release in a week
[December 18, 2019] Redbus team notifed me that they implemented a new workflow for the pdf generation . But still pdf.redbus.com was accessible and so as the issue.
[December 20, 2019] After digging up the new implementation , found out they were using PhantomJS for generating pdfs. Local file read was not allowed since they’re loading the custom html in about:blank page. Loading file:/// protocol is not allowed inside iframe, But http is allowed. Ended up in SSRF 😬 and reported the same.
[February 3, 2020] Redbus fixed the issue by moving the pdf generation module as an internal micro-service. (No bounty for this one 😅. That’s ok! )
[July 16, 2020] But pdf.redbus.com is still public , Any updates?
[September 11, 2020] pdf.rebus.com was removed from public access.

Throughout this journey, I noticed something that the guy who was handling this case got promoted to senior security engineer. Congrats Mate !😃. That was one looooong ride !

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-04_persistent-xss-unvalidated-oembed-at-mediumcom.md
original_filename: 2018-10-04_persistent-xss-unvalidated-oembed-at-mediumcom.md
title: Persistent XSS (Unvalidated oEmbed) at Medium.com
category: documents
detected_topics:
- xss
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: d6e25340ffc9f0fc413690dfc5fd4e6556ee1b36a810fde602faf301e55054df
text_sha256: 0f387db0bf262c531e22781c03f5276473898e90aa9b1527d58e49cc0aaf7ced
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Persistent XSS (Unvalidated oEmbed) at Medium.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-04_persistent-xss-unvalidated-oembed-at-mediumcom.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `d6e25340ffc9f0fc413690dfc5fd4e6556ee1b36a810fde602faf301e55054df`
- Text SHA256: `0f387db0bf262c531e22781c03f5276473898e90aa9b1527d58e49cc0aaf7ced`


## Content

---
title: "Persistent XSS (Unvalidated oEmbed) at Medium.com"
url: "https://medium.com/@jonathanbouman/stored-xss-unvalidated-embed-at-medium-com-528b0d6d4982"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Medium"]
bugs: ["Stored XSS"]
bounty: "100"
publication_date: "2018-10-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5665
scraped_via: "browseros"
---

# Persistent XSS (Unvalidated oEmbed) at Medium.com

Persistent XSS (Unvalidated oEmbed) at Medium.com
Jonathan Bouman
Follow
9 min read
·
Oct 4, 2018

423

3

Press enter or click to view image in full size
Proof of concept

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
In one of our previous reports we learned more about reflected XSS; the downside of this attack is that we need to trick an user in visiting a prepared URL.

But what if we can store our javascript code inside a page itself?

The impact will be much larger; no special urls involved and no XSS auditors ruining our game. We call this a stored or persistent XSS attack. As you may remember, we had success before with this type of attack; see the AH.nl report.

As always we’re looking for a target that encourages us to search for bugs. So what about Medium.com? Woohoo! They’ve got a nice bug bounty program.

I love their platform for writing my reports. The design is clean, no ads and it works great. High five, erm, I mean Claps for them!

Today is a good day to claim our position in the their Hall of Fame: https://medium.com/humans.txt

Press enter or click to view image in full size
https://medium.com/humans.txt

Identifying targets
Storing information and sharing it with others is what Medium is all about. We just need to find a way to put our code in the information in such a way that it gets executed. So let’s take a look at their story editor.

The editor supports different types of content; plain text, images and media embeds.

Medium documentation

Through media embeds you are able to enrich your stories. For example loading external videos, showing tweets that are enriched with your twitter profile information. You just press the (+) in the editor, paste the url, press enter and wait for the magic. This magic has a name; oEmbed.

Example of the oEmbed of a tweet

If you own a platform like Medium.com you want to support all sorts of embeds. That means maintaining a whitelist of approved external platforms, securely processing and transforming the embed data and keeping it all scalable at the same time.

That’s not easy, and guess what? Medium.com made a business out of it, hello Embed.ly!

Press enter or click to view image in full size
Embed.ly, a company owned by Medium.com

Mmm. What if we can become a provider, providing malicious code? That would be perfect, injecting code right away into the story through the embed code.

Let’s make a fake login for our proof of concept.

Finding holes, how does Embed.ly work?
Behind the scenes a lot of stuff is happening. First of all they state that they support the oEmbed specification.

So does that mean we’re done if our malicious external url contains the proper oEmbed tags? Think of a html page that contains oEmbed tags stating it is a video player, but silently loads a fake login page?

Not so fast sir, no. Your beautiful styled fake login embed will be rendered as a plain text box containing a title, description and the domain name; the fallback layout.

Press enter or click to view image in full size
Example of the fallback layout of Embedly

Only approved providers are allowed to embed their magic. I hear you say “well, become a provider!”. Unfortunately no. Applying to become a provider means that we need to social engineer, and that is not allowed by the responsible disclosure rules of Medium.com

Press enter or click to view image in full size
re·quire·ment 1. Something that is required; a necessity. 2. Something to bypass

Let’s open the Medium editor and see what the browsers does if we try to embed a vimeo video. Since Vimeo is on the whitelist it should work and we could learn more about the inner workings of Embed.ly.

How does the oEmbed implementation work, screenshot time!

Press enter or click to view image in full size
1. Request oEmbed details of our Vimeo video
Press enter or click to view image in full size
2. Response oEmbed details of our video, internal unique identifier mediaResourceId
Press enter or click to view image in full size
3. Story update that tells Medium.com to include our video oEmbed, using the mediaResourceId
Press enter or click to view image in full size
4. Requesting the oEmbed HTML, used to display the oEmbed.
Press enter or click to view image in full size
5. Response oEmbed HTML, containing the Vimeo player, hosted by Embed.ly
Press enter or click to view image in full size
6. The contents of the iframe url from the oEmbed HTML, an Embed.ly hosted player

Important to notice is that Embed.ly creates a mediaResourceId for every embed. This mediaResourceId is a MD5 hash of the URL. This is a smart move and allows them to cache the results. Is someone embedding an already processed URL? Embed.ly serves the embed immediately from their cache.

Medium uses the mediaResourceId inside their stories to refer to specific embeds. There is no HTML stored inside the story.

So we need to fool Embed.ly into creating a mediaResourceId for our fake login page. Furthermore this mediaResourceId should serve a response that loads our fake login through an iframe.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s see what happens if we try to create our own mediaResourceId:

Drommels, the iframe src property is not set. It does not work.

No success. Adding a few oEmbed or Open Graph tags in order to inject the fake login as a video player? No luck. I tried every combination I could think of and nothing worked.

So we have to think of something else.

Pretending we are Vimeo, raise the sails, setup your proxies!
As we learned from screenshot 5; Embed.ly embeds Vimeo videos fine and loads their vimeo player.

GET /widgets/media.html?src=https%3A%2F%2Fplayer.vimeo.com%2Fvideo%2F142424242%3Fapp_id%3D122963&dntp=1&url=https%3A%2F%2Fvimeo.com%2F142424242&image=https%3A%2F%2Fi.vimeocdn.com%2Fvideo%2F540139087_1280.jpg&key=b19fcc184b9711e1b4764040d3dc5c07&type=text%2Fhtml&schema=vimeo

Decoded:

GET /widgets/media.html?src=https://player.vimeo.com/video/142424242?app_id=122963&dntp=1&url=https://vimeo.com/142424242&image=https://i.vimeocdn.com/video/540139087_1280.jpg&key=b19fcc184b9711e1b4764040d3dc5c07&type=text/html&schema=vimeo

So what if we could do some sort of a man-in-the-middle-attack (MITM) and pretend we are Vimeo? We will change the Vimeo response so it loads our fake login page. Search for the string that points to the vimeo player https://player.vimeo.com/video/142424242 and change it into https://evildomain.ltd/fakelogin? Sounds good!

MITM Attack

Quick setup: Turn on your PHP server, upload fakelogin.html (file containing a properly designed fake login), upload proxy.php (miniProxy, allows us to load external urls, change the responses, serve the changed response).
Add 1 line to proxy.php, line 381, above //Parse the DOM:
$responseBody = str_replace("https://player.vimeo.com/video/142424242", "https://evildomain.ltd/embedly/fakelogin.html", $responseBody);
Create a new Medium story
Embed the url https://evildomain.ltd/embedly/proxy.php?https://vimeo.com/142424242
Medium.com their server will request the oEmbed details from https://evildomain.ltd/embedly/proxy.php?https://vimeo.com/142424242 , we send them a response that is identical to one from Vimeo, only now containing our fake login page instead of a video player.
Wait for the magic, we got our code injected!
Press enter or click to view image in full size
Our MITM response with the changed video:url, video:secure_url
Response from Embed.ly, containing our fake login url

Let’s reload our article and see if our fake login embed loads.

Press enter or click to view image in full size
Hurray, a working proof of concept!

Discussion, what is Coordinated Vulnerability Disclosure (CVD)?
As you may remember from the previous IKEA report; coordinated disclosure can take some time. Today we run into the same problem with Medium.com.

The problem is communication; it took us 11 emails before we got in direct contact with one of their engineers. When communication was setup we quickly discovered that the initial bug was resolved but their caching servers still serve malicious payloads. After Medium invalidated their cache the vulnerability was resolved and we were able to publish this report; 86 days after the initial report.

New guideline from the National Cyber Security Centre
On 04–10–2018 the Dutch Governement published a new guideline for coordinated vulnerability disclosure. This guideline is a revision of the Responsible Disclosure Guideline, published in 2013. They changed the name from Responsible Disclosure to Coordinated Vulnerability Disclosure. The main reason for that is that they want to focus on the importance of clear communication, the coordination of it.

Press enter or click to view image in full size
Cover of the guideline published in 2018

Direct communication between a bug reporter and the technical staff is required for a good functioning CVD. Also the last resort option, full disclosure, is now mentioned in the guideline:

The main intention of CVD is to mitigate the vulnerability, but ‘full disclosure’ of the vulnerability is always an option for a reporting party if it feels that the process will take too long. This measure is the proverbial ‘big stick’ available to the reporting party. Naturally, this situation must be prevented as much as possible.

As you remember from the IKEA report, this is something we should try to avoid.

Press enter or click to view image in full size
How to communicate? Guideline for Coordinated Vulnerabiltiy Disclosure, page 18

One of the lessons learned from this report is that even though a company has a CVD program we sometimes still need to have patience and persistence in getting a bug resolved.

For a company it’s important to have easy to approach engineers that coordinate the reported vulnerabilities and update the bug reporter of any updates. This saves both parties plenty of time ;-)

Conclusion
We found a way to store our JavaScript and HTML code in such a way that it is executed by the browser of the victim when he visits our Medium post. We did this by manipulating an oEmbed tag by performing a MITM attack.

Our injected javascript is sandboxed in an iframe by Medium.com, this means that even though our Javascript is injected in their pages we can’t access the Medium.com cookies or manipulate their DOM. This greatly reduced the impact of our bug.

However this bug could still cause a lot of harm; a regular visitor won’t be able to see the difference between this fake login and a real login.

Impact of this attack
- Perfect for phishing
- Open redirect possible by using top.location.href. We may auto redirect users to another page after they have entered their credentials for example.
- Attack visitors by embedding http://beefproject.com/
- Allows an attacker to perform clickjack attacks

Do I forget anything? Leave a comment!

Solutions that prevent this attack
- Improve oEmbed provider checks, disallow unapproved iframe sources
- Don’t allow iframes to break out by using top.location.href
- Always invalidate the caches (and that is hard)

Rewards
$100, mention in the humans.txt and a Medium t-shirt

Humans.txt mention!

Timeline
08–07–2018 Discovered bug, wrote this report, informed Medium by email
11–07–2018 Requested confirmation, Medium confirmed
20–07–2018 Requested update from support, reply that I got a reward of $100, mention in the humans.txt and Medium t-shirt, no updates on the bug itself
08–08–2018 Requested update from support, about to publish another blog that describes the same type of attack, bug not fixed on Medium. So the other report is halted (responsible disclosure), no reply
15–08–2018 Requested update from support
15–08–2018 Medium support replied that they requested an internal update from engineers, will contact me later
02–09–2018 Requested update from support, no reply
04–09–2018 Sent LinkedIn message to a Full Stack Software Engineer at Medium (check if they are aware of the bug), no reply
13–09–2018 Sent LinkedIn message to Executive Assistant of CEO at Medium (check if they are aware of the bug), no reply
18–09–2018 Requested update from support, no reply
19–09–2018 Sent LinkedIn message to Head of Legal at Medium
24–09–2018 Reply from Head of Legal, will request security engineers to contact me
03–10–2018 No updates from security engineer, just confirmed bug still exists, shared this report with Head of Legal, requested updates.
03–10–2018 Head of Legal introduced me to a security engineer, security engineer explained that they previously marked this bug as resolved, apologized for the lack of communication, discovered unvalidated cache that causes the payload to still work, explained they invalidated all the caches, allowed me to disclose the report at 04–10–2018.
04–10–2018 Published this Report

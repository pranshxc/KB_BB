---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-13_xss-at-hubspot-and-xss-in-email-areas.md
original_filename: 2018-08-13_xss-at-hubspot-and-xss-in-email-areas.md
title: XSS at Hubspot and XSS in email areas.
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 607a86411ccfffc0b40135e2964cd8be29e39712633d16edecdd639b1b78eb91
text_sha256: 5e613f7a1b814fcf6da991e462aa9650abbe5673569432ef265e905312407e5e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# XSS at Hubspot and XSS in email areas.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-13_xss-at-hubspot-and-xss-in-email-areas.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `607a86411ccfffc0b40135e2964cd8be29e39712633d16edecdd639b1b78eb91`
- Text SHA256: `5e613f7a1b814fcf6da991e462aa9650abbe5673569432ef265e905312407e5e`


## Content

---
title: "XSS at Hubspot and XSS in email areas."
url: "https://medium.com/@friendly_/xss-at-hubspot-and-xss-in-email-areas-674fa39d5248"
authors: ["Friendly (@SkeletorKeys)"]
programs: ["HubSpot"]
bugs: ["XSS"]
bounty: "450"
publication_date: "2018-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5751
scraped_via: "browseros"
---

# XSS at Hubspot and XSS in email areas.

1

Top highlight

XSS at Hubspot and XSS in email areas.
Friendly
Follow
5 min read
·
Aug 13, 2018

176

4

For those asking me what this Tweet and this Tweet is about — then I will be explaining it here in details as much as possible.

For this XSS, you’d want to have Kali Linux, KNOXSS, a SVG that contains an XSS and the basic understanding of how email rendering is displayed on users, admins and client side in email, ticket supports and on the web page.

If you do not have an SVG that contains an XSS, then I’d highly recommend you use the one I will provide:

Make a file name called: SVG.svg — then edit the file name and paste the following code inside of it and then save it:

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
  alert('XSS!');
  </script>
</svg>

Very basic stuff. [Well done, you have an SVG that contains an XSS!]

Steps to Reproduce:

First XSS is from https://bugcrowd.com/hubspot — although they only reward points and hall of fame. Even though this isn’t something you guys care about other than the 💰 [money], but this is a good stepping stone to learn about security.

To do this you’d need an account on: http://hubspot.com to test on.

First, we go to https://app.hubspot.com and then edit our signature:

First thing I do and see is an input field. I tried my very basic payloads, which are:

"><svg/onload=alert(1)>
<img>/><svg/onload=alert(1)>
"></\/\</script><script>alert(1)</script>
"><script>alert("xss");</script>
<div onmouseover="alert('XSS');">Hello :) 
^ [My favorite one - works like 80% of the time for me].
</style><script>a=eval;b=alert;a(b(/XSS/.source));</script>
That's all for now that I'll share.
Enjoy the payloads too. ;)

However, NONE of them worked sadly in this case and on this website. 😦

I did notice that were was an IMAGE icon there though. So I clicked it and saw my SVG being visible, and was able to being uploaded. I clicked my SVG and uploaded it. The SVG was then uploaded directly to the server and wasn’t filtered at all.

So I went to the direct link where my IMAGE SVG was and we got our XSS.

Awesome. SVGXSS — Nice. 😁

Some of you may stop here — However, I didn’t stop here. I wanted to go a step beyond that a step further and maybe do more for a bigger impact.

This other step:

“Requires” Kali Linux [You can skip this part if you’re not interested in Kali Linux].

I booted up Kali Linux and then I created a file name:

"><svg onload=alert(1)>.svg

Then I put my XSS inside of it and saved it.

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After doing that, I uploaded it on the server. The file name did not change at all on the location it was being uploaded to. However, I didn’t get my XSS.

So I changed the file name to:

"><svg onmouseover=alert(1)>.svg

Then I hovered over it and BAM. 😉

Press enter or click to view image in full size
Successfully got the mighty confirmation alert 1.

Now, if we visit that file link itself — we should get our confirmation.

Press enter or click to view image in full size
Our magical confirmation alert— “Friendly”. Ha.

And that being included, it shows our SVG. So if you’d right click “Open image in new tab”, you will be taken to the SVG which contains our XSS as well.

[ Thanks again KNOXSS here for providing insight, a powerful payload and bypass. ]

Basically, TWO XSS in one page.

Reward: Points.

— Yuck.

Finally, XSS via chat module with an email XSS.

This method was discovered by me [ Friendly ] and it works 70% of the times from the websites I’ve come across in my last 24–72 hours when I was testing with numerous websites with various chatting module systems like this one.

POC:

Press enter or click to view image in full size
Our beautiful XSS. [ The black box is just covering the website I’m chatting on. ]

I tried sending the payload itself without going to the email area, but unfortunately I got no XSS. So I’ll explain why it works this way with some live support chat modules.

If this makes any form of sense to you, or helps you in the long run, then be sure to let me know on Twitter by Tweeting at me.

The main question is, why does it work like that and how does it work? It’s quite simple. As soon as you input a payload inside the email field such as:

x@x.com<--`<img/src=` onerror=alert("Friendly-XSS")> --!> 
or
<--`<img/src=` onerror=alert("Friendly-XSS")> --!>

then send another payload similar to it will automatically register on the admins side which will then execute. HOWEVER! It will show it’s not registering on your side which is fine, so that means you will need to send the same payload in order for it to execute.

POC is provided above and on what this means.

The site Hubspot did NOT reward me for this, however a private Freelancing website did and I grateful for the reward $450 bounty reward.

Now which site did I get a reward from? That’s a freelancing website and there’s tons of websites out there that does offer freelancers bounties for their free time.

There’s tons that you can find and look for on your own and get a reward for if you Google and looked around.

If you have any questions or comments, feel free to message me on Twitter, or tweeting me @Skeletorkeys

Thanks for reading.

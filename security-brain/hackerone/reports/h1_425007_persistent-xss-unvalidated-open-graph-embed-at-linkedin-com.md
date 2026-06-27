---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '425007'
original_report_id: '425007'
title: Persistent XSS (unvalidated Open Graph embed) at LinkedIn.com
team_handle: linkedin
created_at: '2018-07-01T10:41:24.000Z'
disclosed_at: '2018-10-18T14:12:30.494Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 118
tags:
- hackerone
---

# Persistent XSS (unvalidated Open Graph embed) at LinkedIn.com

## Metadata

- HackerOne Report ID: 425007
- Weakness: 
- Program: linkedin
- Disclosed At: 2018-10-18T14:12:30.494Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**This report was previously published on [Medium.com/@JonathanBouman](https://medium.com/@jonathanbouman/persistent-xss-unvalidated-open-graph-embed-at-linkedin-com-db6188acedd9). 
Follow me on [Twitter](https://twitter.com/JonathanBouman) or [Medium](https://medium.com/@jonathanbouman/) for new reports.**

{F361972}
*Proof of concept*

##Background
In my [previous report](https://medium.com/@jonathanbouman/stored-xss-unvalidated-embed-at-medium-com-528b0d6d4982) we learned more about a special type of the persistent XSS attack; the **unvalidated oEmbed attack**. This attack allows us to inject our HTML and javascript code by manipulating the oEmbed functionality.

[**oEmbed**](https://oembed.com/) is an open format designed to allow embedding content from a website into another website. Almost all of the media rich platforms support the oEmbed standard. For example you can easily add a [**Vimeo**](https://developer.vimeo.com/apis/oembed) video to your [**Wordpress blog**](https://codex.wordpress.org/Embeds) by just pasting the link into the article. Wordpress will convert this link into HTML. This HTML loads the video player of Vimeo and starts the specific video.

**Medium for example** will create a nice box with my twitter profile picture if I paste a link to my [twitter profile](https://www.twitter.com/jonathanbouman) into this post. This is oEmbed in action. As we learned previously, [they were vulnerable](https://medium.com/@jonathanbouman/stored-xss-unvalidated-embed-at-medium-com-528b0d6d4982) and allowed unvalidated oEmbeds.

{F361953}
{F361954}
*oEmbed endpoint is specified by Twitter, Medium will use it for the embed*

Another way to embed visual rich content is by using the [**Open Graph Protocol**](http://ogp.me/). A website can add Open Graph Tags to their page in order to specify what type of content should be used for embeds.
{F361955}
*Wikipedia has an og:image meta tag, it defines the image that should be displayed if one embeds the article*

Most platforms check the urls for these specific oEmbed and Open Graph Tags before they embed the content. They do this in a [specific order](https://medium.com/slack-developer-blog/everything-you-ever-wanted-to-know-about-unfurling-but-were-afraid-to-ask-or-how-to-make-your-e64b4bb9254#d313). After checking all the tags they will decide if and how the link got embedded.

The big **advantage of embeds** is that readers don’t have to leave a blog to view the media rich content (e.g. video, images, presentations). Also for media platforms, like Vimeo and Youtube, it’s a great way to increase their exposure and views.

Most of the platforms that allow you to embed external content have a **whitelist** of allowed domains; see [Wordpress for example](https://codex.wordpress.org/Embeds#Okay.2C_So_What_Sites_Can_I_Embed_From.3F). You simply don’t want unvalidated HTML being injected into your platform.

But what happens if this whitelist fails and we are able to inject our evil code into our target platform?

We already proved [oEmbed to be vulnerable](https://medium.com/@jonathanbouman/stored-xss-unvalidated-embed-at-medium-com-528b0d6d4982), now let’s see if we can pull this trick again by **manipulating Open Graph tags**, let’s give it a try!

##Pick our target
Who should we pick today? **You say LinkedIn? Good choice!** LinkedIn is one of my favorite places to go whenever I try to stay in touch with fellow researchers. Furthermore it’s a place where plenty of CEO/CTO/CTTO/CNYANCATO’s hang around. So whenever I got stuck in reporting bugs (e.g. non responsonding support desks), I try to get in touch with the people responsible. Sending a quick LinkedIn direct message is often enough; ‘Hey, can you take a look at ticket 4242, your site is vulnerable. Support is sleeping.’

Last but not least; LinkedIn got a [nice responsible disclosure](https://security.linkedin.com/vulnerabilty-disclosure) and they even have a [(private) bug bounty program](https://hackerone.com/linkedin) at Hackerone.com.

So let’s try to get an invite for this bug bounty program by filing our first report with them!

##Identifying targets
Blogs, that’s what we think of if we look for places that allow us to embed external content; say hello to [LinkedIn Articles](https://www.linkedin.com/help/linkedin/topics/6198/6207/publishing-articles?lang=en). You can open this part of LinkedIn by visiting your news feed and press the [Write an Article](https://www.linkedin.com/post/new) button.

{F361958}
*Write an article*

We get a nice and clean editor that allows us to write our first article, consisting of a headline and some content. Next to our cursor there is a little icon that allows us to *‘Add images or video for visual impact.’*

{F361959}
*The blog editor*
If we press this little icon, we can pick the Links button and add *visual rich content* to our blog.

{F361960}
*The embed wizard, magic!*

##Embed Requests
Time to fire up [Burp Suite](https://portswigger.net/burp) and inspect our network traffic, what happens after we fill in the URL?
{F361961}
*Link got converted to HTML code that embeds the Youtube player*

As we can see LinkedIn converts our url into HTML code that we are allowed to embed. The response is URL encoded, the [URL decoded](https://meyerweb.com/eric/tools/dencoder/) version is:

```{“embedIframe”:”<iframe src=\”https://www.linkedin.com/pulse/api/edit/embed?embed={"request":{"originalUrl":"https://www.youtube.com/watch?v=9hWgA7qjK2c","finalUrl":"https://www.youtube.com/watch?v=9hWgA7qjK2c"},"images":[{"width":480,"url":"https://i.ytimg.com/vi/9hWgA7qjK2c/hqdefault.jpg","height":360},{"width":1920,"url":"https://i.ytimg.com/vi/9hWgA7qjK2c/maxresdefault.jpg","height":1080}],"data":{"com.linkedin.treasury.Video":{"width":480,"html":"<iframe scrolling=\”no\” allowfullscreen src=\”//media.licdn.com/embeds/media.html?src=https://www.youtube.com/embed/9hWgA7qjK2c?feature=oembed&amp;url=https://www.youtube.com/watch?v=9hWgA7qjK2c&amp;type=text/html&amp;schema=youtube\" width=\”480\” frameborder=\”0\” class=\”embedly-embed\” height=\”270\” />”,”height”:270}},”provider”:{“display”:”YouTube”,”name”:”YouTube”,”url”:”https://www.youtube.com/"},"author":{"name":"321 Relaxing — Meditation Relax Clips”},”description”:{“localized”:{“en_US”:”Rain HD video and forest, relaxing rain sounds and forest sounds for sleeping meditation. Nature sounds relaxation. Rainforest sounds: https://www.youtube.co..."}},"title":{"localized":{"en_US":"Rain Sounds and Forest Sounds — Relaxing Sleep”}},”type”:”video”}&signature=AcdfNDjBXZOjo2vdz4EOixtGBrlx\”></iframe>”,”universal”:true}```

The editor parses this iframe into our article and this results in three iframes being nested in each other before the video player shows up. There we go; we just embedded a Youtube video with [relaxing rain sounds](https://www.youtube.com/watch?v=dQw4w9WgXcQ).
{F361962}
*Nested iframes, it takes three iframes before we can listen to jungle sounds.*

This means that even if we are able to inject our own evil HTML we won’t have access to the LinkedIn domain; we are [isolated in an iframe](https://www.owasp.org/index.php/3rd_Party_Javascript_Management_Cheat_Sheet#Sandboxing_with_iframe). We can’t access any LinkedIn cookies and we are not able to manipulate the HTML outside of the iframe.

However the **impact can still be big if we can inject a fake LinkedIn login screen and steal passwords of visitors**. LinkedIn embeds the content without any visual hints that something is an embed, just clean borderless boxes. So it’s not possible for visitors to distinguish it from a real login screen.

##A perfect phishing login
First we need to design the phishing login screen. Since we want to show the impact in a way that **also non-tech people understand** the severity. A simple javascript [alert box](https://www.w3schools.com/js/js_popup.asp) is often not sufficient.

A good tool to duplicate HTML elements of other websites is SnappySnippet. This [Chrome extension](https://chrome.google.com/webstore/detail/snappysnippet/blfngdefapoapkcdibbdkigpeaffgcil?hl=en) lets you select an element in a website and copy paste it as plain HTML and CSS.
{F361965}
*SnappySnippet*

We paste the code from SnappySnippet into a new HTML file, tune it a little bit, and add some javascript at the end so it captures the email and password. If one submits the form we want to display the login details in a javascript alert box as a proof of concept.

{F361966}
*Javascript alert of the login details*

Let’s upload this fake login html file to our own server and try to embed it in our LinkedIn article. Just to see what happens if we link to it without any oEmbed or Open Graph tags.

{F361967}
*Fake login embed without any tags, it does not work*

As we can see it falls back to an *‘universal-embed-wrapper’* that just displays our URL with a little gray border around it.

##Exploiting the Open Graph
If we take a close look at the [Open Graph Protocol](http://ogp.me/) specs we discover that there is a tag named og:video. It defines how a video player should be embedded.

{F361968}
*Vimeo example of Open Graph video meta tags*

What if we create a HTML file with the *og:video* tags that loads our fake login instead of the video player?
{F361969}
*The document we are trying to embed, it loads the fake login as a video player*
{F361971}
*Our fake login loads, LinkedIn thinks it’s a genuine video player*

Tada! We’ve got our fake login embedded inside a LinkedIn article. Let’s name the article **‘Oops, something went wrong!’** and we’re ready to go.

We are now able to [**spear phish**](https://en.wikipedia.org/wiki/Phishing#Spear_phishing) other users by sharing them a private link to the draft of this article. Or we can just publish it on the LinkedIn network and see what happens.

We’ve got everything ready now, time to **file a report** with LinkedIn security.

##Proof of concept
{F361972}

##Conclusion
We found a way to create a perfect phishing website on the LinkedIn.com domain. We used the Open Graph Video meta tag in order to inject our phishing login as a video player in an LinkedIn article.

This is a variation of the persistent XSS attack.

##Impact of this attack
- Perfect situation for (spear) phishing
- We may auto redirect users to another page after they have entered their credentials, so it doesn’t look suspicious (by using ```top.location.href```)
- Attack visitors by embedding [http://beefproject.com/](http://beefproject.com/)
- Allows an attacker to perform [clickjack attacks](https://www.owasp.org/index.php/Clickjacking)

Do I forget anything? Leave a comment!

##Solutions that prevent this attack
- Never trust Open Graph Tags from strangers, use a whitelist for embeds
- Don’t allow iframes to [break out](https://stackoverflow.com/questions/369498/how-to-prevent-iframe-from-redirecting-top-level-window)

##Rewards
None.

##Timeline
01–07–2018 Discovered and reported bug by email
01–07–2018 LinkedIn informed me they received the report
20–07–2018 Requested update 
24–07–2018 LinkedIn replied that fix is deployed, I replied all my test accounts are blocked by LinkedIn, unable to confirm fix, requested to unblock the test accounts, no reply
02–08–2018 Used my personal account for testing, confirmed the fix, requested LinkedIn if bug is eligible for any rewards or invite into private program, requested to unblock my test account.
04–08–2018 Reply from LinkedIn that I’m on their review list for an invite to the private program. No answer on question if bug is eligible for reward. All accounts still blocked, so not able to test for any new bugs (no new accounts due to phone number verification). LinkedIn requested a review of this post prior publication.
08–08–2018 Sent LinkedIn draft of this blog for review, no reply
15–08–2018 Requested update from LinkedIn
21–08–2018 LinkedIn replied, approved the blog, informed me they don’t offer rewards outside of their private bug bounty program, I am added to their list of ‘researchers for consideration’.
07–10–2018 Published this blog on Medium.com (delayed the publication because I had to wait for Medium.com to fix [the same sort of bug](https://medium.com/@jonathanbouman/stored-xss-unvalidated-embed-at-medium-com-528b0d6d4982)). 
17-10-2018 Published this blog on HackerOne their new blogging platform.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-22_when-equal-is-not-another-webview-takeover-story_2.md
original_filename: 2022-03-22_when-equal-is-not-another-webview-takeover-story_2.md
title: When Equal is Not, Another WebView Takeover Story
category: documents
detected_topics:
- mobile-security
- command-injection
tags:
- imported
- documents
- mobile-security
- command-injection
language: en
raw_sha256: fb17a9adfe290877b0fc2b44011adbca4a6289e51f9a9e76233e63258b33a9cd
text_sha256: 5bfff4e4d72b06911fd24540eb80f2464ac4672e0b2abf88e3c461878f35cb76
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# When Equal is Not, Another WebView Takeover Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-22_when-equal-is-not-another-webview-takeover-story_2.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `fb17a9adfe290877b0fc2b44011adbca4a6289e51f9a9e76233e63258b33a9cd`
- Text SHA256: `5bfff4e4d72b06911fd24540eb80f2464ac4672e0b2abf88e3c461878f35cb76`


## Content

---
title: "When Equal is Not, Another WebView Takeover Story"
url: "https://valsamaras.medium.com/when-equal-is-not-another-webview-takeover-story-730be8d6e202"
authors: ["Dimitrios Valsamaras (@Ch0pin)"]
bugs: ["Android"]
publication_date: "2022-03-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2790
scraped_via: "browseros"
---

# When Equal is Not, Another WebView Takeover Story

When Equal is Not, Another WebView Takeover Story
+Ch0pin🕷️
Follow
4 min read
·
Mar 22, 2022

35

I have been assessing Android applications for some time and I must admit that despite the countless write-ups about unprotected WebViews, the particular issue is still on top of my list. Almost 80% of the reviewed apps were vulnerable to forced browsing with the actual impact varying from JavaScript execution to full account takeover.

The scenario is the same in most of the cases… A malicious URL, makes its way to the application’s WebView via an unvalidated query parameter, an intent extra or even an open redirect. The impact is usually low to medium since the dangerous features of this component are disabled by default, but it can get really rough when special conditions apply. For example, an “attached” JavascriptInterface with some fruitful exported functionality can be a recipe for disaster.

Press enter or click to view image in full size
Don’t put your blame on me

You might wonder that, since this issue is so common, haven’t the developer community heard about it ?… After all it can’t be that difficult to sanitise the user input.

Well, let me put it this way… think of multiple layers of java inheritance, where some superclass is loading “any” given url from an un-sanitised parameter. When you are writing code on the child of a child of a child … of a naughty parent, these issues are not as obvious as you might think.

To tackle this problem I wrote a Medusa module which, between else, can monitor the application’s WebView for “risky” features, including Javascript Interfaces, file access, url loading etc. Indeed this module pinpointed some nice findings, but as this post is not to do oneself proud I’ll get straight to the point.

When Equal is Not

During my assessments I encountered cases where the mistake is pretty much obvious and this is what this post is all about. I won’t be using real application names for obvious reasons, so I wrote a simple Android app to prove my concept. Let’s start with a deeplink declaration in my AndroidManifest file:

And here is the application’s code:

TL;DR Our application registers the deeplink example://webview which means that the MainActivity will be triggered through the intent filter for intents with action set to android.intent.action.VIEW and data example://webview . The onNewIntent callback inspects the data string and if this is not empty it calls the handleDeeplink to handle the intent. Finally the handleDeeplink will call the isAuthorisedURL function in order to check the validity of the incoming URL. If the return value is set to true, the WebView loads the URL. In the code snippet above, the isAuthorisedURL returns always true so any given URL will be loaded.

Equal is ! (Starts || Ends || Contains)

There are cases where the applications need to load various URLs in their WebViews including subdomains which are not always given during the application development. These subdomains are get added or removed from time to time to facilitate or discard various features and services.

Get +Ch0pin🕷️’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To handle this problem, the developers come up with various solutions which sometimes are not the best from a security aspect. The startsWith and endsWith or even the contains functions of the java.lang.String class are used to filter out invalid domains, in the most unsafe way. Let’s see a real example which I encountered in a 100,000,000+ downloads application.

The isAuthorisedURL function looked like bellow:

The objective was probably to include the foo subdomains of the foobar domain, but the implementation is obviously wrong since all the foo.foobar* URLs will be considered as valid and will be loaded to the WebView. Believe it or not, a similar issue with an endsWith function was found in a 10,000,000+ application. This time the request to the loaded URL was authenticated while the isAuthorisedURL looked like below:

One more time all the *foobar.com domains will pass the if condition thus they will be loaded to the WebView.

The host is dead, long live the host

Sometimes the development team during the staging phase uses hostnames which are valid inside a company’s local network but not in the world wide web … but they can be valid in the world wide web…. Here is an example:

In this case, the developers wanted to include the example.com, google.com and test.com but during the staging phase they also added the staging.site to test out this feature. While this is OK during the tests, when they publish the app they forgot to remove the extra URL. As you understand, assuming that the staging.site is available an attacker can register the domain and takeover the WebView. The same condition of course stands for expired domains.

Conclusion

This post just scratches the tip of the iceberg when it comes to WebView security vulnerabilities. The intention though was to pinpoint some cases where small mistakes (even in very popular applications) can literally have very serious impact.

See you on the next post !

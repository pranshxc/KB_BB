---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-01_xss-on-accountleagueoflegendscom-via-easyxdm-2016.md
original_filename: 2022-12-01_xss-on-accountleagueoflegendscom-via-easyxdm-2016.md
title: XSS on account.leagueoflegends.com via easyXDM [2016]
category: documents
detected_topics:
- oauth
- cors
- sso
- xss
- command-injection
- mfa
tags:
- imported
- documents
- oauth
- cors
- sso
- xss
- command-injection
- mfa
language: en
raw_sha256: ad2fad52ef028d666d8228c31555f921c78c329077053fd879ea774629f76b29
text_sha256: 9a3f3309ade187c3c3590e172ca5e0a613234b01515ede0c3c95ae9e58c41f48
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# XSS on account.leagueoflegends.com via easyXDM [2016]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-01_xss-on-accountleagueoflegendscom-via-easyxdm-2016.md
- Source Type: markdown
- Detected Topics: oauth, cors, sso, xss, command-injection, mfa
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `ad2fad52ef028d666d8228c31555f921c78c329077053fd879ea774629f76b29`
- Text SHA256: `9a3f3309ade187c3c3590e172ca5e0a613234b01515ede0c3c95ae9e58c41f48`


## Content

---
title: "XSS on account.leagueoflegends.com via easyXDM [2016]"
url: "https://medium.com/bored-engineer/xss-on-account-leagueoflegends-com-via-easyxdm-2016-75bcf9d582b5"
authors: ["Luke Young (@TheBoredEng)"]
programs: ["Riot Games"]
bugs: ["XSS", "postMessage"]
bounty: "2,000"
publication_date: "2022-12-01"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1835
scraped_via: "browseros"
---

# XSS on account.leagueoflegends.com via easyXDM [2016]

XSS on account.leagueoflegends.com via easyXDM [2016]
Luke Young
Follow
9 min read
·
Dec 1, 2022

35

1

This post contains a chain of vulnerabilities I responsibly disclosed to Riot Games in November of 2016. I’m publicly disclosing it now as it’s an interesting and technically complex vulnerability. The issue has long since been resolved, so long ago that most of the infrastructure referenced in the report has been replaced.

Press enter or click to view image in full size
Background

Various Riot Games ‘League of Legends’ webpages need to access metadata about the currently logged-in player to properly function. Sometimes these webpages are not located on the same (sub)domain as account.leagueoflegends.com and therefore must access the information cross-origin.

These days, this would be accomplished via Cross-Origin Resource Sharing (CORS) and/or window.postMessage, however back in 2016 browser support was inconsistent, particularly if you needed to support users on much older browsers. Many companies at the time, including Riot Games, turned to a library called easyXDM:

easyXDM is a Javascript library that enables you as a developer to easily work around the limitation set in place by the Same Origin Policy, in turn making it easy to communicate and expose javascript API’s across domain boundaries. — easyXDM.net

This JavaScript library provides a normalized interface for cross-origin communication that is backed by different browser transports (examples include window.postMessage, Flash's LocalConnection, HashTransport, etc). The transport is selected based on which is “best” supported by the user’s browser.

When using easyXDM, there is a producer and a consumer webpage. The producer page exports one or more JavaScript functions which can then be invoked (from another origin) by the consumer page which receives the result. For Riot Games the producer was account.leagueoflegends.com/pm.html which exported the following methods:

send: A wrapper function around jQuery.ajax allowing access to make requests/responses cross-origin
get-cookies: Retrieves cookies by name from document.cookie
set-cookies: Sets a cookie on the base domain via document.cookie

Even on the surface, these functions appear quite dangerous so predictably there were some protections against access/abuse by arbitrary webpages:

When the pm.html page was loaded, the document.referrer was checked to verify the top level domain matched an allowlist:

leagueoflegends.com
riotgames.com
lolesports.com
pvp.net
leagueoflegends.com.tr
lolespor.com
lolguilds.ru

Additionally, when receiving a cross-origin message from the easyXDM transport, the message origin (as reported by easyXDM) was checked against the same allowlist before executing the corresponding function.

A quick introduction to easyXDM

Before launching into the vulnerabilities, I need to take a moment to explain how easyXDM works and establish some terminology. easyXDM webpages obtain context about their configuration from a series of query parameters in the URL:

xdm_e (config.remote): The URL to load if the current page is a consumer or the URL of the parent page if the current page is a producer
xdm_c (config.channel): The channel to use when sending messages
xdm_s (config.secret): The secret to use to validate both parties are known
xdm_p (config.protocol): The id of which protocol transport to use for communication as defined in Core.js#L695

Because this context/configuration is obtained from the query parameters it is possible for a malicious actor to manipulate these values which I’ll need later.

Bypassing the Referrer Check

First I needed to bypass the referrer check. One way this could be accomplished is by posting a link on the boards.na.leagueoflegends.com forum (which matches the *.leagueoflegends.com referrer check) and hoping that a player clicks the link. However, this significantly limits the possible impact of any exploit as it would require specific user interaction.

A better exploit would be to utilize an open-redirect on any of the allowlisted domains. Unfortunately (or fortunately in this case for Riot) browsers have stopped carrying the Referrer header most on 301, 302, etc Location: based redirects. This leaves me looking for a JavaScript-based open redirect such as: window.location.href = "${open_redirect}";.

Thankfully, it is possible to abuse easyXDM to accomplish this. There is a vulnerability with option handling in FrameElementTransport.js. After the transport has loaded it will perform the following check:

Since document.referrer won't match the provided xdm_e parameter it will redirect the top window. This is intended to prevent spoofing origins when using the FrameElementTransport. I can force easyXDM to use this vulnerable transport by specifying a xdm_p parameter like this:

http://provider.easyxdm.net/current/example/remotetransport.html?xdm_e=https%3A%2F%2Fattackerdoma.in&xdm_c=channel&xdm_p=5

This method requires document.referrer to have a value for the payload to work. Since 2016, browsers have gotten more aggressive about removing referrers so this may no longer work in 2022, at least without further changes.

Great, now I have a JS-based open-redirect, however I can’t use it on pm.html because there is a catch-22 problem with the referrer checks. I needed to locate a different easyXDM consumer on one of the allowlisted domains to abuse. Thankfully there was another one at: apollo.na.leagueoflegends.com/apollo/cors/index.html.

Putting it all together, I have the following PoC which will load pm.html via the easyXDM open redirect on apollo.na.leagueoflegends.com, bypassing the referrer check:

Bypassing Origin Check

Next, I needed to bypass the origin checks on each message. Since the origin is provided by easyXDM, I needed to identify another bug/vulnerability in one of the transport implementations.

Eventually, I found one in HashTransport which works by passing data from a child iFrame to a parent window via window.location.hash. It works a little something like this:

Because this implementation is quite a workaround, it is not possible for the parent page (subdomain1) to determine who updated location.hash, unlike other transports such as window.parent.postMessage which have a event.origin property. To get around this, easyXDM assumes all messages come from config.remote (see HashTransport.js).

Get Luke Young’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is great and exactly the type of bug I needed, however there is an issue with where our exploit code gets loaded in the chain. If I set config.remote to attackerdoma.in to trigger our malicious page to load, all messages will have a non-allowlisted origin. But if I set it to a webpage on an allowlisted domain, our own webpage will never be loaded leaving us with no way to exploit the bug...

Callback hell with iFrames:

Looping back around to our referrer bypass, I can use a very similar technique to get around this issue. I can’t use the exact same open redirect bug since it calls window.top.location (replacing the top level window) which would break our exploit chain. However, I can use one of the other protocols (in this case HashTransport again) to force the apollo consumer to frame our attacker page, like this:

This results in the following nested frame layout:

https://account.leagueoflegends.com/pm.html
└── https://apollo.na.leagueoflegends.com/apollo/cors/index.html
  └── https://attackerdoma.in/...

At which point my script on attackerdoma.in can send messages to the parent frame like this:

This approach isn’t perfect though: when pm.html wants to send a message back to apollo it will set location.hash for the second level iframe which I can't access from attackerdoma.in context leaving me blind; I can send messages but not receive the reply...

Bypassing VerifyBehavior.js:

To throw another roadblock into the mix, easyXDM has already considered this attack and created VerifyBehavior.js. In their own words:

This behavior will verify that communication with the remote end is possible, and will also sign all outgoing, and verify all incoming messages. This removes the risk of someone hijacking the iframe to send malicious messages.

The good news is the implementation is also vulnerable and only protects against a scenario where the second level iframe is replaced mid-communication, not replaced from the start. The implementation looks roughly like this:

By sending a message first to establish a value for theirSecret:

1_1,2_0_theirSecret

Then waiting a few hundred milliseconds before sending a second message the request will continue:

1_1,3_0_theirSecret_${encodeURIComponent(message_payload)}
Turning jQuery.ajax into XSS:

At this point I can call any of the exposed methods mentioned earlier, but not receive the result. This leaves me with the ability to set cookies and make XHR requests but not read the response which is not particularly impactful. Thankfully, I can use a little-known “feature” of jQuery to abuse the XHR method. When calling jQuery.ajax if the url ends in =? jQuery will attempt to load the request as a JSONP call (even if dataType: "json" is set). You can test this out yourself (at least until jQuery v4):

So the crafted message payload to pm.html to trigger XSS becomes:

Putting it all together

At this point I have a rather complex chain of vulnerabilities:

Victim opens 85f32147–76c1–44e2–8aa8-a1f9fd8e2ed3.html
Redirect to https://apollo.na.leagueoflegends.com/apollo/cors/index.html occurs
Apollo redirects to https://account.leagueoflegends.com/pm.html with document.referrer set to a whitelisted domain
pm.html loads https://apollo.na.leagueoflegends.com/apollo/cors/index.html which is a whitelisted domain for messages
Apollo loads the nested frame of 8723f98f-e1f1–41cc-bc1e-f2afb4c8d933.html
8723... sends a message to pm.html setting theirSecret for the session
8723... sends a message to pm.html using theirSecret to call the send method
pm.html calls send which triggers a JSONP call to e26e42c0-08b7-4998-8e62-e9d8d6025d9e.js
XSS Payload fires

All of these vulnerabilities were privately reported to Riot Games with the above description and functional proof of concept.

Bypassing the mitigation

After some time, the Riot team indicated a partial mitigation had been rolled out, with more fixes on the way. This mitigation was an update to /apollo/cors/index.html to check if document.referrer is an allowlisted domain:

To bypass this, I needed to find another open-redirect from one of the allowlisted domains. Taking a look at the login process for leagueoflegends.com, the user is directed through an auth flow on auth.riotgames.com via login.riotgames.com using the following URL (assuming the user is in the NA region):

https://login.leagueoflegends.com/?region=na&lang=en_US&redirect_uri=http%3A%2F%2Fna.leagueoflegends.com%2F

While the redirect_uri parameter can't be manipulated to any URL making it an open-redirect, it could be modified to any subdomain of leagueoflegends.com, including apollo.na.leagueoflegends.com. This meant I could use this endpoint to redirect to the apollo page which will bypass the allowlist check like this:

https://login.leagueoflegends.com/?region=na&lang=en_US&redirect_uri=https%3A%2F%2Fapollo.na.leagueoflegends.com%2Fapollo%2Fcors%2Findex.html

Because this is abusing the login functionality, the victim has to be already logged-in to trigger the PoC.

This left me with a final vulnerability chain:

Victim opens a06250dd-ffd0–4a7e-8fb2-cf163021fe61.html
Redirect to https://login.leagueoflegends.com/
Redirect to https://auth.riotgames.com/authorize
Redirect to https://login.leagueoflegends.com/oauth2-callback
Redirect to https://login.lolesports.com/sso/login
Redirect to https://login.leagueoflegends.com/sso/callback
Redirect to https://apollo.na.leagueoflegends.com/apollo/cors/index.html occurs
Apollo redirects to https://account.leagueoflegends.com/pm.html with document.referrer set to a whitelisted domain
pm.html loads https://apollo.na.leagueoflegends.com/apollo/cors/index.html which is a whitelisted domain for messages
Apollo loads the nested frame of 8723f98f-e1f1–41cc-bc1e-f2afb4c8d933.html
8723... sends a message to pm.html setting theirSecret for the session
8723... sends a message to pm.html using theirSecret to call the send method
pm.html calls send which triggers a JSONP call to e26e42c0-08b7-4998-8e62-e9d8d6025d9e.js
XSS Payload fires

This bypass of the mitigation was also reported to Riot Games.

Accidentally Disclosing an 0-day

When drafting this post and verifying the original payloads in 2022, I realized that the latest release of easyXDM was still vulnerable to the message origin spoofing via HashTransport as well as the (limited) open-redirect vulnerabilities!

Before publishing these vulnerabilities publicly, I reached out to the easyXDM author to see if the project was still maintained and if a new security release would even make sense, they responded:

This project is not actively maintained as browsers have caught up to provide the core features natively.

And I would agree with this stance, the browser support for window.postMessage is pervasive and has been for 10+ years at this point. Newly developed software should be using the native window.postMessage functionality without compatibility shims like easyXDM, even if native postMessage still leaves plenty of room for its own different complex vulnerabilities.

Conclusion

This was a pretty fun chain of vulnerabilities to work on at the time, and really shows the hidden level of complexity you can inherit when you import seemingly straight-forward JavaScript compatibility shims.

P.S. Thanks to the Riot Games security team for giving me their blessing to publicly disclose this report when I reached out 6 years after the fact :)

Timeline
November 26th, 2016: Initial report to Riot Games via HackerOne
November 28th, 2016: Report acknowledged by triage team
November 29th, 2016: Riot confirms successful reproduction
February 21st, 2017: Riot indicates a patch was deployed
February 21st, 2017: Response that I am still able to reproduce, presumably because the patch is not completely rolled out yet
March 18th, 2017: Follow-up that I am still able to reproduce using the initial payload from the report
April 28th, 2017: Riot apologies for the confusion, indicates the patch is currently deployed
April 29th, 2017: Bypass of the patch is identified and reported to Riot
May 8th, 2017: Riot acknowledges the bypass
November 2nd, 2017: Follow-up on the report asking for updates
November 6th, 2017: Riot acknowledges the ping and indicates the issue has been fixed, although one individual vulnerability is remaining (but the full chain is broken at this point)
May 31st, 2018: Bounty ($2,000) awarded and report closed as resolved
November 3rd, 2022: Email sent to easyXDM author
November 19th, 2022: LinkedIn message to easyXDM author
November 19th, 2022: Response from easyXDM author indicating the project is not actively maintained
December 1st, 2022: Publication of this post

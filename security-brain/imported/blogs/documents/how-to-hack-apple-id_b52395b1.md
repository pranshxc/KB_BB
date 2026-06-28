---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-17_how-to-hack-apple-id.md
original_filename: 2021-08-17_how-to-hack-apple-id.md
title: How to Hack Apple ID
category: documents
detected_topics:
- oauth
- otp
- sso
- access-control
- xss
- command-injection
tags:
- imported
- documents
- oauth
- otp
- sso
- access-control
- xss
- command-injection
language: en
raw_sha256: b52395b1f3126d6ed54bb08ac52a61c83d730ffb46e51899500909015e2a676f
text_sha256: 5304521485cecc17b00bbe0f748f9a912f2a831acba5c54a29766582a981adbd
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How to Hack Apple ID

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-17_how-to-hack-apple-id.md
- Source Type: markdown
- Detected Topics: oauth, otp, sso, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `b52395b1f3126d6ed54bb08ac52a61c83d730ffb46e51899500909015e2a676f`
- Text SHA256: `5304521485cecc17b00bbe0f748f9a912f2a831acba5c54a29766582a981adbd`


## Content

---
title: "How to Hack Apple ID"
url: "https://zemnmez.medium.com/how-to-hack-apple-id-f3cc9b483a41"
authors: ["Zemnmez (@zemnmez)"]
programs: ["Apple"]
bugs: ["XSS", "Account takeover"]
bounty: "10,000"
publication_date: "2021-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3410
scraped_via: "browseros"
---

# How to Hack Apple ID

How to Hack Apple ID
Zemnmez
Follow
22 min read
·
Aug 17, 2021

440

11

Press enter or click to view image in full size
Demonstration of the exploit on iOS

Everyone knows what’s inside a computer isn’t really real. It pretends to be, sure, hiding just under the pixels — but I promise you it isn’t.

In the real world, everything has a certain mooring we’re all attuned to. You put money in a big strong safe, and, most likely if somehow it opens there will be a big sound, and a big hole. Everything has a footprint, everything has a size, there are always side-effects.

As the electrons wiggle, they’re expressing all these abstract ideas someone thought up sometime. Someone had an idea of how they’d dance, but that’s not always true. Instead, there are half-formed ideas, ideas that change context and meaning when exposed to others, and ideas that never really quite made sense.

The Alice in Wonderland secret of computers is that the dancers and their music are really the same. It’s easy to mistakenly believe that each word I type is shuffled by our pixie friends along predefined chutes and conveyors to make what we see on screen, when in reality each letter is just a few blits and bloops away from being something else entirely.

Sometimes, if you’re careful, you can make all those little blits and bloops line up in a way that makes the dance change, and that’s why I’ve always loved hacking computers: all those little pieces that were never meant to be put together that way align in unintended but beautiful order. Each individual idea unwittingly becomes part of a greater and irrefutable whole.

Before the pandemic, I spent a lot of time researching the way web of YouTube, Wikipedia and Twitter meets the other world of Word, Photoshop and Excel to produce Discord, 1Password, Spotify, iTunes, Battle.net and Slack. Here all the wonderful and admittedly very pointy and sharp benefits of the web meet the somewhat softer underbelly of the ‘Desktop Application’, the consequences of which I summarised one sunny day in Miami.

I’m not really a very good security researcher, so little of my work sees the light of day because the words don’t always form up in the right order, but my experience then filled me with excitement to publish more. And so, sitting again under the fronds of that tumtum tree, I found more — and I promise you what I found then was as exciting as what I’ll tell you about now.

But I can’t tell you about those. Perhaps naïve, it didn’t occur to me before that the money companies give you for your security research is hush money, but I know that now — and I knew that then, when I set out to hack Apple ID.

At the time, Apple didn’t have any formal way of paying you for bugs: you just emailed them, and hoped for the best. Maybe you’d get something, maybe you wouldn’t — but there is certainly nothing legally binding about sending an email in the way submitting a report to HackerOne is. That appealed to me.

Part 1: The Doorman’s Secret

Press enter or click to view image in full size

Computer systems don’t tend to just trust each other, especially on the web. The times they do usually end up being mistakes.

Let me ask you this: when you sign into Google, do you expect it to know what you watched on Netflix? Of course not.

That’s down to a basic rule of the web: different websites don’t default to sharing information to each other.

ICloud, then is a bit of a curiosity. It has its own domain, icloud.com, entirely separate from Apple’s usual apple.com yet its core feature is of course logging into your Apple iCloud account. More interestingly still, you might notice that most login systems for, say, Google, redirect you through a common login domain like accounts.google.com, but iCloud’s doesn’t.

Behind the looking-glass, Apple has made this work by having iCloud include a webpage that is located on the AppleID server, idmsa.apple.com. The page is located at this address:

https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-ebog4xzs-os6r-58ua-4k2f-xlys83hd&language=en_US&iframeId=auth-ebog4xzs-os6r-58ua-4k2f-xlys83hd&client_id=d39ba9916b7251055b22c7f910e2ea796ee65e98b2ddecea8f5dde8d9d1a815d&redirect_uri=https://www.icloud.com&response_type=code&response_mode=web_message&state=auth-ebog4xzs-os6r-58ua-4k2f-xlys83hd&authVersion=latest

Here, Apple is using OAuth 2, a capability based authentication framework. ‘Capability based’ is key here, because it means that a login from Apple.com doesn’t necessarily equate to one from iCloud.com, and also not all iCloud logins are necessarily the same either — that’s how Find My manages to skip a second-factor check to find your phone. This allows Apple to (to some extent) reduce the blast radius of security issues that might otherwise touch iCloud.

This is modified, however, to allow the login to work embedded in another page. response_mode=web_message seems to be a switch that turns this on.

If you visit the address, you’ll notice the page is just blank. This is for good reason: if anyone could just show the Apple iCloud login page then you could play around with the presentation of the login page to steal Apple user data (‘Redress Attack’). Apple’s code is detecting that it’s not being put in the right place and blanks out the page.

In typical OAuth, the ‘redirect_uri’ specifies where the access is being sent to; in a normal, secure form, the redirect uri gets checked against what’s registered for the other, ‘client_id’ parameter to make sure that it’s safe for Apple to send the special keys that grant access there — but here, there’s no redirect that would cause that. In this case the redirect_uri parameter is being used for a different purpose: to specify the domain that can embed the login page.

In a twist of fate, this one fell prey to a similar bug to the one from how to hack the uk tax system, i guess, which is that web addresses are extraordinarily hard to compare safely.

Necessarily, something like this parameter must pass through several software systems, which individually probably have subtly different ways of interpreting the information. For us to be able to bypass this security control, we want the redirect_uri checker on the AppleID server to think icloud.com, and other systems to think something else. URLs, web addresses are the perfect conduit for this.

Messing with the embed in situ in the iCloud page with Chrome Devtools, I found that a redirect_uri of ‘https://abc@www.icloud.com’ would pass just fine, despite it being a really weird way of saying the same thing.

The next part of the puzzle is how do we get the iCloud login page into our page? Consult this reference on embed control:

X-Frame-Options: DENY
Prevents any kind of embedding
pros: ancient, everyone supports it
cons: the kids will laugh at you; if you want only some embedding, you need some complicated and unreliable logic
X-Frame-Options: ALLOW-FROM http://example.com
Only allows embedding from a specific place
pros: A really good idea from a security perspective
cons: was literally only supported by Firefox and Internet Explorer for a short time so using it will probably make you less secure
Content-Security-Policy: frame-ancestors
Only allows embedding from specific place(s)
pros: new and cool, there are probably TikToks about how to use it; prevents embeds-in-embeds bypassing your controls
cons: probably very old browsers will ignore it

If you check Chrome DevTools’s ‘network’ panel, you will find the AppleID signon page uses both X-Frame-Options: ALLOW-FROM (which essentially does nothing), and Content-Security-Policy: frame-ancestors.

Here’s a cut-down version of what the Content-Security-Policy header looks like when ‘redirect_uri’ is set to the default “https://www.icloud.com/”

Content-Security-Policy: frame-ancestors ‘self’ https://www.icloud.com

This directs the browser to only allow embeds in iCloud. Next, what about our weirder redirect_uri, https://abc@icloud.com?

Content-Security-Policy: frame-ancestors ‘self’ https://abc@www.icloud.com

Very interesting! Now, humans are absolute fiends for context-clues. Human language is all about throwing a bunch of junk together and having it all picked up in context, but computers have a beautiful, childlike innocence toward them. Thus, I can set redirect_uri to ‘https://mywebsite.com;@icloud.com/’, then, the AppleID server continues to think all is well, but sends:

Content-Security-Policy: frame-ancestors ‘self’ https://mywebsite.com;@www.icloud.com

This is because the ‘URI’ language that’s used to express web addresses is contextually different to the language used to express Content Security Policies. ‘https://mywebsite.com;@www.icloud.com’ is a totally valid URL, meaning the same as ‘https://www.icloud.com’ but to Content-Security-Policy, the same statement means ‘https://mywebsite.com’ and then some extra garbage which gets ignored after the ‘;’.

Using this, we can embed the Apple ID login page in our own page. However, not everything is quite as it seems. If you fail to be able to embed a page in chrome, you get this cute lil guy:

But, instead we get a big box of absolutely nothing:

Press enter or click to view image in full size

Part 2: Communicating with the blank box

Our big box, though blank, is not silent. When our page loads, the browser console gives us the following cryptic message:

{"type":"ERROR","title":"PMRPErrorMessageSequence","message":"APPLE ID : PMRPC Message Sequence log fail at AuthWidget.","iframeId":"601683d3-4d35-4edf-a33e-6d3266709de3","details":"{\"m\":\"a:28632989 b:DEA2CA08 c:req h:rPR e:wSR:SR|a:28633252 b:196F05FD c:req h:rPR e:wSR:SR|a:28633500 b:DEA2CA08 c:rRE f:Application error. Destination unavailable. 500 h:rPR e:f2:rRE|a:28633598 b:B74DD348 c:req h:rPR e:wSR:SR|a:28633765 b:196F05FD c:rRE f:Application error. Destination unavailable. 500 h:rPR e:f2:rRE|a:28634110 b:BE7671A8 c:req h:rPR e:wSR:SR|a:28634110 b:B74DD348 c:rRE f:Application error. Destination unavailable. 500 h:rPR e:f2:rRE|a:28634621 b:BE7671A8 c:rRE f:Application error. Destination unavailable. 500 h:rPR e:f2:rRE|a:28635123 b:E6F267A9 c:req h:rPR e:wSR:SR|a:28635130 b:25A38CEC c:req h:r e:wSR:SR|a:28635635 b:E6F267A9 c:rRE f:Application error. Destination unavailable. 500 h:rPR e:f2:rRE|a:28636142 b:25A38CEC c:rRE f:Application error. Destination unavailable. 1000 h:r e:f2:rRE\",\"pageVisibilityState\":\"visible\"}"}

This message is mostly useless for discerning what exactly is going wrong. At this point, I like to dig more into the client code itself to work out the context of this error. The Apple ID application is literally millions of lines of code, but I have better techniques — in this case, if we check the Network panel in Chrome DevTools, we can see that when an error occurs, a request is sent to ‘https://idmsa.apple.com/appleauth/jslog’, assumedly to report to Apple that an error occurred.

Press enter or click to view image in full size

Chrome DevTools’ ‘sources’ panel has a component on the right called “XHR/fetch Breakpoints” which can be used to stop the execution of the program when a particular web address is requested.

Using this, we can pause the application at the point the error occurs, and ask our debugger to go backwards to the condition that caused the failure in the first place.

Eventually, stepping backward, there’s this:

new Promise(function(e, n) {
  it.call({
  destination: window.parent,
  publicProcedureName: "ready",
  params: [{
  iframeTitle: d.a.getString("iframeTitle")
  }],
  onSuccess: function(t) {
  e(t)
  },
  onError: function(t) {
  n(t)
  },
  retries: p.a.meta.FEConfiguration.pmrpcRetryCount,
  timeout: p.a.meta.FEConfiguration.pmrpcTimeout,
  destinationDomain: p.a.destinationDomain
  })
  }

The important part here is window.parent, which is our fake version of iCloud. It looks like the software inside AppleID is trying to contact our iCloud parent when the page is ready and failing over and over (see: retries). This communication is happening over the postMessage (the ‘pm’ of pmrpc ).

Lastly, the code is targeting a destinationDomain, which is likely set to something like https://www.icloud.com ; then, since our embedding page is not that domain, there’s a failure.

We can inject code into the AppleID Javascript and the iCloud javascript to view their version of this conversation:

AppleID → iCloud:
pmrpc.{“jsonrpc”:”2.0",”method”:”receivePingRequest”,”params”:[“ready”],”id”:”9BA799AA-6777–4DCC-A615-A8758C9E9CE2"}
AppleID tells iCloud it’s ready to receive messages.
iCloud → AppleID:
pmrpc.{“jsonrpc”:”2.0",”id”:”9BA799AA-6777–4DCC-A615-A8758C9E9CE2",”result”:true}
iCloud responds to the ping request with a ‘pong’ response.
AppleID → iCloud:
pmrpc.{“jsonrpc”:”2.0",”method”:”ready”,”params”:[{“iframeTitle”:” Sign In with Your Apple ID”}],”id”:”E0236187–9F33–42BC-AD1C-4F3866803C55"}
AppleID tells iCloud that the frame is named ‘Sign in with Your Apple ID’ (I’m guessing to make the title of the page correct).
iCloud → AppleID:
pmrpc.{“jsonrpc”:”2.0",”id”:”E0236187–9F33–42BC-AD1C-4F3866803C55",”result”:true}
iCloud acknowledges receipt of the title.
AppleID → iCloud:
pmrpc.{“jsonrpc”:”2.0",”method”:”receivePingRequest”,”params”:[“config”],”id”:”87A8E469–8A6B-4124–8BB0–1A1AB40416CD”}
AppleID asks iCloud if it wants the login to be configured.
iCloud → AppleID:
pmrpc.{“jsonrpc”:”2.0",”id”:”87A8E469–8A6B-4124–8BB0–1A1AB40416CD”,”result”:true}
iCloud acknowledges receipt of the configuration request, and says that it does, yes want the login to be configured.
AppleID → iCloud:
pmrpc.{“jsonrpc”:”2.0",”method”:”config”,”params”:[],”id”:”252F2BC4–98E8–4254–9B19-FB8042A78E0B”}
AppleID asks iCloud for a login dialog configuration.
iCloud → AppleID:
pmrpc.{“jsonrpc”:”2.0",”id”:”252F2BC4–98E8–4254–9B19-FB8042A78E0B”,”result”:{“data”:{“features”:{“rememberMe”:true,”createLink”:false,”iForgotLink”:true,”pause2FA”:false},”signInLabel”:”Sign in to iCloud”,”serviceKey”:”d39ba9916b7251055b22c7f910e2ea796ee65e98b2ddecea8f5dde8d9d1a815d”,”defaultAccountNameAutoFillDomain”:”icloud.com”,”trustTokens”:[“HSARMTnl/S90E=SRVX”],”rememberMeLabel”:”keep-me-signed-in”,”theme”:”dark”,”waitAnimationOnAuthComplete”:false,”logo”:{“src”:”data:image/png;base64,[ … ]ErkJggg==”,”width”:”100px”}}}}
iCloud configures the login dialog. This includes data like the iCloud logo to display, the caption “Sign in to iCloud”, and, for example whether a link should be provided for if the user forgets their password.
AppleID → iCloud:
pmrpc.{“jsonrpc”:”2.0",”id”:”252F2BC4–98E8–4254–9B19-FB8042A78E0B”,”result”:true}
iCloud confirms receipt of the login configuration.

In order to make our bootleg iCloud work, we will need code that completes the conversation in the same way. You can look at a version I made, here.

Our next problem is that destinationDomain I pointed out before: postMessage ensures that snot-nosed kids trying to impersonate iCloud can’t just impersonate iCloud — by having every postMessage have a targetOrigin, basically a specified destination of the webpage. It’s not enough that the message gets sent to window.parent; that parent must also be securely specified to prevent information going the wrong place.

Part 3: Snot-Nosed Kid Mode

This one isn’t as easy as reading what AppleID does and copying it. We need to find another security flaw between our single input, redirect_uri , through to destinationDomain, and then finally on to postMessage. Again, the goal here is to find some input redirect_uri that still holds the exploit conditions from Part 1, but also introduces new exploit conditions for this security boundary.

By placing a breakpoint at the destinationDomain line we had before, we can see that unlike both the AppleID server and Content-Security-Policy, the whole redirect_uri parameter, ‘https://mywebsite.com;@wwwicloud.com’ is being passed to postMessage, as though it were this code:

window.parent.postMessage(data_to_send, "https://mywebsite.com;@www.icloud.com");

At first, this seems like an absolute impasse. In no possible way is our page going to be at the address ‘https://mywebsite.com;@www.icloud.com’. However, once you go from the reference documentation, to the technical specification the plot very much thickens.

In section 9.4.3 of the HTML standard, the algorithm for comparing postMessage origins is specified, and step 5 looks like this:

Let parsedURL be the result of running the URL parser on targetOrigin.
If parsedURL is failure, then throw a “SyntaxError" DOMException.
Set targetOrigin to parsedURL’s origin.

Crucially, despite “https://mywebsite.com;@www.icloud.com” being not at all a valid place to send a postMessage, the algorithm extracts a valid origin from it (i.e. it becomes https://www.icloud.com). Again, this allows us purchase to sneak some extra content in there to potentially confuse other parts of AppleID’s machinery.

The source for the AppleID login page starts with a short preamble that tells the AppleID login framework what the destination domain (in this case iCloud) is for the purpose of login:

bootData.destinationDomain = decodeURIComponent("https://mywebsite.com;@www.icloud.com");

This information eventually bubbles down to the destinationDomain we’re trying to mess with. When toying with ‘redirect_uri’, I found that there’s a bug in the way this functionality is programmed in Apple’s server.

For an input ‘https://mywebsite.com;"@www.icloud.com’ (note the double quote), this code is produced:

bootData.destinationDomain = decodeURIComponent("https://mywebsite.com;\"@www.icloud.com");

The double quote is ‘escaped’ with a ‘\’ to ensure that we don’t break out of the quoted section and start executing our own code, however something a little odd happens when we input instead ‘https://mywebsite.com;%22@www.icloud.com’. ‘%22’ is what you get from ‘encodeURIComponent’ of a double quote, the opposite of what apple is doing here.

bootData.destinationDomain = decodeURIComponent("https://mywebsite.com;\"@www.icloud.com");

We get exactly the same response! This means that Apple is already doing a decodeURIComponent on the server before it even reaches this generated Javascript. Then, the generated Javascript is again performing the same decoding. Someone made the mistake of doing the same decoding on the client and server, but it didn’t become a functionality breaking bug because the intended usage doesn’t have any doubly encoded components. We can, however introduce these. 😉

Because the server is using the decodeURIComponent-ed form, and the client is using the twice decodeURIComponent-ed form, we can doubly encode special modifier characters in our URI that we want only the client to see — while still passing all the server-side checks!

After some trial and error, I determined that I can set redirect_uri to:

https%3A%2F%2Fmywebsite.com%253F%20mywebsite.com%3B%40www.icloud.com

This order of operations then happens:

AppleID’s server decodeURIComponent-s it, producing:
https://mywebsite.com%3F mywebsite.com;@www.icloud.com
AppleID’s server parses the origin from https://mywebsite.com%3F mywebsite.com;@www.icloud.com , and gets https://www.icloud.com , which passes the first security check
AppleID’s server takes the once-decodeURIComponent-ed form and sends Content-Security-Policy: allow-origin https://mywebsite.com%3F mywebsite.com;@www.icloud.com
The browser parses the Content-Security-Policy directive and parses out origins again, allowing embedding of the iCloud login from both ‘https://mywebsite.com%3f’ (which is nonsense) and ‘mywebsite.com’ (which is us!!!!). This passes the second security check and allows the page to continue loading.
AppleID’s server generates the sign in page with the Javascript bootData.destinationDomain = decodeURIComponent(“https://mywebsite.com%3F mywebsite.com;@www.icloud.com");
The second decodeURIComponent sets bootData.destinationDomain to https://mywebsite.com? mywebsite.com;@www.icloud.com
When the AppleID client tries to send data to www.icloud.com, it sends it to https://mywebsite.com? mywebsite.com;@www.icloud.com
The browser when performing postMessage parses an origin again again (!!) from https://mywebsite.com? mywebsite.com;@www.icloud.com . The ‘?’ causes everything after it to be ignored, resulting in the target origin ‘https://mywebsite.com’. This passes the third security check.

However, this is only half of our problems, and our page will stay blank. Here’s what a blank page looks like, for reference:

Press enter or click to view image in full size

Part 4: Me? I’m Nobody.

Though now we can get messages from iCloud, we cannot perform full initialisation of the login dialog without also sending them. However, AppleID checks the senders of all messages it gets, and that mechanism is also totally different from the one that is used for a postMessage send.

The lowest-level browser mechanism that AppleID must be inevitably calling sadly does not perform some abusable parse step beforehand. A typical message origin check looks like this:

if (message.origin != "https://safesite.com") throw new Error("hey!! thats illegal!");

This is just a ‘strict string comparison’, which means that we would, in theory have to impossibly be the origin https://mywebsite.com? mywebsite.com;@www.icloud.com which has no chance of ever happening on God’s green earth.

Get Zemnmez’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, the PMRPC protocol is actually open source, and we can view its own version of this check online.

Receipt of a message is handled by ‘processJSONRpcRequest’, defined in ‘pmrpc.js’. Line 254 decides if the request needs to be checked for security via an ACL (Access Control List) as follows:

254: !serviceCallEvent.shouldCheckACL || checkACL(service.acl, serviceCallEvent.origin)

This checks a value called ‘shouldCheckACL’ to determine if security is disabled, I guess 😉

That value, in turn comes from line 221:

221: shouldCheckACL : !isWorkerComm

And then isWorkerComm comes to us via lines 205–206:

205: var eventSource = eventParams.source;
206: var isWorkerComm = typeof eventSource !== "undefined" && eventSource !== null;

‘eventParams’ is the event representing the postMessage, and ‘event.source’ is a reference to the window (i.e. page) that sent the message. I’d summarise this check as follows:

if (message.source !== null && !(message.origin === "https://mywebsite.com? mywebsite.com;@www.icloud.com"))

That means the origin check is completely skipped if message.source is ‘null’.

Now, I believe the intention here is to allow rapid testing of pmrpc-based applications: if you are making up a test message for testing, its ‘source’ can be then set to ‘null’, and then you no longer need to worry about security getting in the way. Good thing section 9.4.3, step 8.3 of the HTML standard says a postMessage event’s source is always a ‘WindowProxy object’, so it can never be ‘null’ instead, right?

Ah, but section 8.6 of the HTML standard defines an iframe sandboxing flag ‘allow-same-origin’, which, if not present in a sandboxed iframe sets the ‘Sandboxed origin browsing context flag’ (defined in section 7.5.3) which ‘forces the content into a unique origin’ (defined in section 7.5.5), which makes the window an ‘opaque origin’ (defined in section 7.5), which when given to Javascript is turned into null (!!!!).

This means when we create an embedded, sandboxed frame, as long as we don’t provide the ‘allow-same-origin’ flag, we create a special window that is considered to be null , and thus bypasses the pmrpc security check on received messages.

A ‘null’ page however, is heavily restricted, and, importantly, if our attack page identifies as null via this trick, all the other checks we worked so hard to bypass will fail.

Press enter or click to view image in full size

Instead, we can embed both Apple ID with all the hard work we did before, and a ‘null’ page. We can still postMessage to the null page, so we use it to forward our messages on to Apple ID, which thinks since it is a ‘null’ window, it must have generated them itself.

You can read my reference implementation of this forwarding code, here.

Part 5: More than Phishing

Now that AppleID thinks we’re iCloud, we can mess around with all of those juicy settings that it gets. How about offering a free Apple gift card to coerce the user into entering their credentials?

In our current state, having tricked Apple ID into thinking that we’re iCloud, we have a little box that fills in your apple email very nicely.

When you log in to our embed we get an authentication for your Apple account over postMessage. Even if you don’t 2FA! This is because an authentication token is granted without passing 2FA for iCloud ‘Find My’, used for finding your potentially lost phone (which you might need to pass 2FA otherwise).

However, this is basically phishing — although this is extremely high-tech phishing, I have no doubt the powers that be will argue that you could just make a fake AppleID page just the same. We need more.

We’re already in a position of extreme privilege. Apple ID thinks we’re iCloud, so it’s likely that our interactions with the Apple ID system will be a lot more trusting with what we ask of it. As noted before, we can set a lot of configuration settings that affect how the login page is displayed:

pmrpc.{"jsonrpc":"2.0","id":"252F2BC4-98E8-4254-9B19-FB8042A78E0B","result":{"data":{"features":{"rememberMe":true,"createLink":false,"iForgotLink":true,"pause2FA":false},"signInLabel":"Sign in to iCloud","serviceKey":"d39ba9916b7251055b22c7f910e2ea796ee65e98b2ddecea8f5dde8d9d1a815d","defaultAccountNameAutoFillDomain":"icloud.com","trustTokens":["HSARMTnl/S90E=SRVX"],"rememberMeLabel":"keep-me-signed-in","theme":"dark","waitAnimationOnAuthComplete":false,"logo":{"src":"data:image/png;base64,[ ... ]ErkJggg==","width":"100px"}}}}

That’s all well and good, but what about the options that iCloud can use, but simply chooses not to? They won’t be here, but we can use Chrome DevTools’ ‘code search’ feature to search all the code the Apple ID client software uses.

‘signInLabel’ makes a good search term as it probably doesn’t turn up anywhere else:

d()(w.a, "envConfigFromConsumer.signInLabel", "").trim() && n.attr("signInLabel", w.a.envConfigFromConsumer.signInLabel),

It looks like all of these settings like ‘signInLabel’ are part of this ‘envConfigFromConsumer’, so we can search for that:

this.attr("testIdpButtonText", d()(w.a, "envConfigFromConsumer.testIdpButtonText", "Test"))  d()(w.a, "envConfigFromConsumer.accountName", "").trim() ? (n.attr("accountName", w.a.envConfigFromConsumer.accountName.trim()),  n.attr("showCreateLink", d()(w.a, "envConfigFromConsumer.features.createLink", !0)),  n.attr("showiForgotLink", d()(w.a, "envConfigFromConsumer.features.iForgotLink", !0)),  n.attr("learnMoreLink", d()(w.a, "envConfigFromConsumer.learnMoreLink", void 0)),  n.attr("privacyText", d()(w.a, "envConfigFromConsumer.privacy", void 0)),  n.attr("showFooter", d()(w.a, "envConfigFromConsumer.features.footer", !1)),  n.attr("showRememberMe") && ("remember-me" === d()(w.a, "envConfigFromConsumer.rememberMeLabel", "").trim() ? n.attr("rememberMeText", l.a.getString("rememberMe")) : "keep-me-signed-in" === d()(w.a, "envConfigFromConsumer.rememberMeLabel", "").trim() && n.attr("rememberMeText", l.a.getString("keepMeSignedIn")),  n.attr("isRememberMeChecked", !!d()(w.a, "envConfigFromConsumer.features.selectRememberMe", !1) || !!d()(w.a, "accountName", "").trim())),  i = d()(w.a, "envConfigFromConsumer.verificationToken", ""),

These values we know from our config get given different names to put into a template. For example, ‘envConfigFromConsumer.features.footer’ becomes ‘showFooter’. In DevTools’ network panel, we can search all resources, code and otherwise the page uses for where these inputs end up:

{{#if showRememberMe}}
<div class="si-remember-password">
  <input type="checkbox" id="remember-me" class="form-choice form-choice-checkbox" {($checked)}="isRememberMeChecked">
  <label id="remember-me-label" class="form-label" for="remember-me">
  <span class="form-choice-indicator"></span>
  {{rememberMeText}}
  </label>
</div>

What a lovely blast from the past! These are handlebars templates, a bastion of the glorious web 2.0 era I started my career in tech in!

Handlebars has a bit of a dirty secret. ‘{{value}}’ statements work like you expect, safely putting content into the page; but ‘{{{value}}}’ extremely unsafely injects potentially untrusted HTML code — and for most inputs looks just the same! Let’s see if an Apple engineer made a typo by searching the templates for “}}}”:

{{#if showLearnMoreLink}}
<div>
  {{{learnMoreLink}}}
</div>
{{/if}}
{{#if showPrivacy}}
<div  class="label-small text-centered centered tk-caption privacy-wrapper">
  <div class="privacy-icon"></div>
  {{{privacyText}}} 
</div>
{{/if}}

Perfect! From our previous research, we know that ‘privacyText’ comes from the configuration option ‘envConfigFromConsumer.privacy’, or just ‘privacy’. Once we re-configure our client to send the configuration option { "privacy": "<img src=fake onerror='alert(document.domain)'" } , Apple ID will execute our code and show a little popup indicating what domain we have taken over:

Part 6: Overindulgence

Now it’s time to show off. Proof of concepts are all about demonstrating impact, and a little pop-up window isn’t scary enough.

We have control over idmsa.apple.com, the Apple ID server browser client, and so we can access all the credentials saved there — your apple login and cookie — and in theory, we can ‘jump’ to other apple login windows. Those credentials are all stored in a form that we can use to take over an apple account, but they’re not a username and password. That’s what I think of as scary.

For my proof of concept, I:

Execute my full exploit chain to take over Apple ID. This requires only one click from the user.
Present the user with a ‘login with AppleID’ button by deleting all the content of the Apple ID login page and replacing it with the standard button
Open a new window to the real, full Apple ID login page, same as apple would when the button is clicked
With our control of idmsa.apple.com, take control over the real Apple ID login dialog and inject our own code which harvests the logins as they are typed
Manipulate browser history to set the exploit page location to https://apple.com, and then delete the history record of being on the exploit page — if the user checks if they came from a legitimate Apple site, they’ll just see apple.com and be unable to go back.

Full commented source code can be found here.

Video demonstration of the Proof of Concept on desktop

Although I started this project before apple had its bug bounty program, I reported it just as the bug bounty program started and so I inadvertently made money out of it.

Apple paid me $10,000 for my bug and proof of concept, which, while I’m trying not to be a shit about it, is 2.5 times lower than the lowest bounty on their Example Payouts page, for creating an app that can access “a small amount of sensitive data”. Hopefully other researchers are paid more!

I also hope this was an interesting read! I took a really long time to write this with the pandemic kind of sapping my energy, and my sincere hope that despite the technical complexity here, I could write something accessible to those new to security.

Thomas

Thanks to perribus, iammandatory, and taviso for reviewing earlier versions of this disclosure.

If Apple is reading this, please do something about my other bug reports, it has been literally years, and also add my name to the Apple Hall of fame 🥺🥺

Full timeline follows this article.

edit: Apple says my Hall of Fame will happen in September!

edit: September is almost over and it hasn’t happened!

Timeline

Report to fix time: 3 days
Fix to offer time: 4 months, 3 days
Payment offer to payment time: 4 months, 5 days
Total time: 8 months, 8 days
Friday, November 15th 2019
First apple bug, an XSS on apple.com reported
Saturday, November 16th 2019
Issues noticed in Apple ID
The previous bug I reported has been mitigated, but no email from Apple about it
Thursday, November 21st 2019, 3:43AM GMT
First proof of concept sent to Apple demonstrating impersonating iCloud to Apple ID, using it to steal Apple user’s information.
Thursday, November 21st 2019, 6:06AM GMT
Templated response from Apple, saying they’re looking into it
Thursday, November 21st 2019, 8:20PM GMT
Provided first Apple ID proof of concept which injects malicious code, along with some video documentation.
Sunday, November 24th 2019
The issue is mitigated (partially fixed) by Apple
Thursday, November 28th 2019
Ask for updates
Wednesday, December 4th 2019
I try to pull some strings with friends to get a reply
Tuesday, December 3rd 2019
Apple tells me there is nothing to share with me
December 10th 2019
I ask if there is an update
Friday, January 10th 2019
I get an automated email saying, in essence (1) don’t disclose the bug to the public until ‘investigation is complete’ and (2) Apple will provide information over the course of the investigation. Email for an update
Wednesday, January 29th 2020
Ask for another update (at the 2 month mark)
Friday, January 31st 2020
Am asked to check if it’s been fixed. Yes, but not exactly in the way I might have liked.
Sunday, February 2nd 2020
At Schmoocon, a security conference in Washington DC I happen to meet the director of the responsible disclosure program. I talk about the difficulties I’ve had.
Tuesday, February 4th 2020
Apple confirms the bug as fixed and asks for my name to give credit on the Apple Hall of Fame as of August 2021, I have still not been publicly credited. I reply asking if this is covered by the bounty program. Apple responds saying that they will let me know later.
Saturday, February 15th 2020
I ask for an update on status
Monday, February 17th 2020
Apple responds: no updates. I ask when I’ll hear back
Friday, February 21st 2020
I contact the director of the program with the details I got at schmoo, asking when the expected turnaround on bugs is
Monday, March 2nd 2020
Apple responds. They say they have no specfic date
Tuesday, March 3rd 2020
The director responds, saying they don’t give estimates on timelines, but he’ll get it looked into
Tuesday, March 24th 2020
Offered $10,000 for the Apple ID code injection vulnerability. Asked to register as an Apple developer so I can get paid through there
Sunday, March 29th 2020
Enroll in the Apple Developer program, and ask when I’ll be able to disclose publicly.
Tuesday, March 31st 2020
Told to accept the terms and set up my account and tax information (I am not told anything about disclosure)
Tuesday, March 31st 2020
Ask for more detailled instructions, because I can’t find out how to set up my account and tax information (this is because my Apple Developers application has not yet been accepted)
Thursday, April 2nd 2020
Ask if this is being considered as a generic XSS because the payout seems weird compared to the examples
Tuesday, April 28th
Apple replies to request for more detailed instructions (it’s the same thing, but reworded)
May 13th 2020
I ask for an update
May 18th 2020
Am told the money is “in process to be paid”, with no exact date but expected in May or early June. They’ll get back when they know.
May 23rd 2020
I am told my information has been sent to the accounts team, and that Apple will contact me about it when appropriate.
May 18th 2020
I ask again when I can disclose.
June 8th 2020
I ask for some kind of update on payment or when I can disclose.
June 10th 2020
I am informed that there is ‘a new process’. The new process means I pay myself for my Apple Developers account, and Apple reimburses me that cost. I tell Apple I did this several months ago, and ask how my bug was classified within the program. I also contact the Apple security director asking if I can get help. He’s no longer with Apple.
June 15th 2020
Apple asks me to provide an ‘enrolment ID’.
June 15th 2020
I send apple a screenshot of what I am seeing. All my application shows is ‘Contact us to continue your enrolment’. I say I’m pretty frustrated and threaten to disclose the vulnerability if I am not given some way forward on several questions: (1) how the bug was classified (2) when I can disclose this and (3) what I am missing to get paid I also rant about it on twitter, which was probably the most productive thing I did to get a proper response in retrospect
June 19th 2020
Apple gets in touch, saying they’ve completed the account review and now I need to set up a bank account to get paid in. Apple says they’re OK with disclosing, as long as the issue is addressed in an update. Apple asks for a draft of my disclosure
Thursday, July 2nd 2020
The Apple people are very gracious. They say thanks for the report, and say my writeup is pretty good. Whoever is answering is very surprised by, and asks me to correct where I say I found this bug only “a few days ago” in the draft I wrote 🤔
July 29th 2020
I get paid :D
… the pandemic happens
12 August 2021
I finish my writeup!

Amendments

22/Aug/21: Fixed link to ‘full source code’, which originally linked to only a very small portion of the full source.

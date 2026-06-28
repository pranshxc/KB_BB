---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-02_hacking-the-nintendo-dsi-browser.md
original_filename: 2023-03-02_hacking-the-nintendo-dsi-browser.md
title: Hacking the Nintendo DSi Browser
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: e3417b1e14ffac46ac16b6a60bfcdb33011854edba78dfd2509277723d711745
text_sha256: 22792a2192cf0a724b2dcb5244cdc257f5af7fb2afa6cf223f19b99298a258b5
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking the Nintendo DSi Browser

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-02_hacking-the-nintendo-dsi-browser.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `e3417b1e14ffac46ac16b6a60bfcdb33011854edba78dfd2509277723d711745`
- Text SHA256: `22792a2192cf0a724b2dcb5244cdc257f5af7fb2afa6cf223f19b99298a258b5`


## Content

---
title: "Hacking the Nintendo DSi Browser"
page_title: "Hacking the Nintendo DSi Browser | farlow.dev"
url: "https://farlow.dev/2023/03/02/hacking-the-nintendo-dsi-browser"
final_url: "https://farlow.dev/2023/03/02/hacking-the-nintendo-dsi-browser"
authors: ["Nathan Farlow (@0x1337cafe)"]
programs: ["Nintendo"]
bugs: ["Memory corruption", "Use-After-Free", "Browser hacking"]
publication_date: "2023-03-02"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1442
---

# Hacking the Nintendo DSi Browser

Mar 2, 2023 

I managed to exploit the Nintendo DSi browser 15 years after it was released in Japan. This post will go over the journey and the technical details.

To see the exploit in action, check out the [video](https://youtu.be/GywA40btJ6E). The exploit is available on [GitHub](https://github.com/nathanfarlow/stylehax). If you want a quick overview, you can skip to the TL;DR section.

## Motivation

I started looking at the browser early in the summer of 2022. My initial idea was to make a cursed pwn chal for [UIUCTF 2022](https://2022.uiuc.tf/). I thought that with the DSi’s age and lack of security mitigations, I could come up with an exploit in a weekend. That estimate was waaaay off. I ended up being consumed by the project on and off for around 6 months before finally coming up with something to show for it.

## Some Background

The DSi browser uses Opera 9.50. There are no security mitigations whatsoever. Jumping to shellcode is back on the menu! Stack buffer overflows are viable. Exploiting use-after-frees, which are often [common in browsers](https://www.zdnet.com/article/chrome-70-of-all-security-bugs-are-memory-safety-issues/), is easier than ever. In fact, the DSi doesn’t even have an operating system, so there’s no kernel to exploit. Various system privileges are handled by the [SCFG register](https://problemkaputt.de/gbatek-dsi-control-registers-scfg.htm). The browser has enough privileges to run most homebrew, but not enough to gain persistence across boots without another exploit.

## Resources

We don’t have source code or even symbols for the browser. However, there are several resources that are helpful for hacking DSi things:

  * [melonDS](https://melonds.kuribo64.net/) \- A DSi emulator that can emulate the home menu, browser, and Wi-Fi!
  * [melonDS GDB stub](https://github.com/melonDS-emu/melonDS/pull/1583) \- Allows us to connect GDB to the emulator to debug crashes
  * [GBATEK](https://problemkaputt.de/gbatek.htm) \- _Phenomenal_ documentation about DSi internals
  * [DSi Mode Hacking Community](https://discord.gg/yD3spjv) \- Lots of very knowledgeable and helpful people here to help with anything DSi

## Google-fu?

Naturally, I started googling for Opera bugs hoping to find something easy. [exploit-db](https://www.exploit-db.com/search?q=opera) gave lots of promising results. I used python’s HTTP server to host the POCs on my laptop and pointed the browser running in melonDS at it. I analyzed the resulting crashes in the melonDS output. Unfortunately, I found that I either couldn’t reproduce the bugs, or that they didn’t cause interesting crashes.

## Webkit Layout Test Fuzzing

MrNbaYoh wrote up their 3ds exploit “validityhax” [here](https://mrnbayoh.github.io/blog/exploiting-the-3ds-browsers-p2/). In the post, they found bugs by sending the browser all of WebKit’s layout tests. The intuition is that the WebKit layout tests have weird edge cases or regression tests which could cause problems on WebKit implementations that are out of date. This makes sense for the 3ds browser, since the 3ds browser uses WebKit. Would it work on the DSi? One way to find out.

I set up a flask app that sends a test case in an iframe. When the test is finished loading, the page refreshes itself to request a new test from the flask app. Eventually, the flask app consumes all ~100k HTML test files from the WebKit layout tests. We can spin up an arbitrary number of emulators to test in parallel.

![4 melonDS emulators receiving WebKit layout tests in parallel](/assets/2023-03-02-hacking-the-nintendo-dsi-browser/fuzz.gif)

The results were underwhelming. There were lots of null dereferences which I marked off as unexploitable. As it turns out, there is actually data mapped near address 0 on the DSi, but it’s not writable. The tests yielded some other weird crashes, but the underlying problem wasn’t obvious from the looking at the test case that caused it. Understanding the crash would take serious reversing work that I sure wasn’t going to do without symbols.

At this point, the project went on hold as I started another semester of school. But by the time winter break came, I had some new ideas to try.

## Heap Hypothesis

My hypothesis was that maybe the layout tests did have interesting heap bugs, but we just didn’t have a reliable way to detect them. For example, if a use-after-free occurred, but no new data was written to the freed memory, we wouldn’t even observe a crash. If we had a Windows or Linux build of Opera 9.50, we could use some heap debugging tools to catch heap bugs instead of letting them crash non-deterministically.

This sent me on an hour-long search to find a build of Opera 9.50. The [Wayback Machine](https://archive.org/web/) came to the rescue. I checked Opera’s old download page, but found that the downloads weren’t archived. The download page did give the filename, though, which I could google for. From Google, I found a handful of living sites that miraculously had the file. I crosschecked the md5sum across the sites and found that they matched. In the end, I couldn’t find a Linux build, but a Windows build will do.

Wine has heap debugging features which can be enabled using `WINEDEBUG=warn+heap`. This will fill freed memory with a canary value `0xfeeefeee` so that use-after-free bugs are more likely to cause a crash. In a crash dump, it will be obvious a use-after-free is involved if we see the canary value. Let’s rerun the layout test fuzzing with wine. My full command to run this ancient Opera version under wine was `WINEDEBUG=warn+heap WINEPREFIX=$HOME/.wine32 WINEARCH=win32 winedbg --gdb opera.exe`

## The Bug

One of the layout test crashes which was originally thought to be an unexploitable null dereference turned out to be a use-after-free! ![use-after-free crash](/assets/2023-03-02-hacking-the-nintendo-dsi-browser/uaf.png)

The reduced code that causes the crash is the following with comments added by me:
  
  
  // mediaRule.cssRules.length starts at 0
  
  mediaRule.insertRule(".test2 { color: blue; }", mediaRule.cssRules.length);
  
  // mediaRule.cssRules.length is now 1
  
  try {
  // fails with syntax error and throws javascript exception
  mediaRule.insertRule("@media screen { p { color: red; } };", mediaRule.cssRules.length);
  } catch (e) {
  }
  
  // mediaRule.cssRules.length is now 2 O.o
  // refreshing page causes the crash
  

There is something weird going on here, since in theory, adding a rule that causes a JavaScript exception to be thrown should not change the length of the `cssRules` array.

That being said, all we have here is a read from an address we could possibly control, which may or may not be exploitable in of itself. I don’t want to do any reversing work, so let’s try to play around with these corrupted JavaScript objects to see if we can get a write or a jump instead.

As it turns out, we can get a jump to `0xfeeefeeee` by adding the following after the previous excerpt:
  
  
  // clear out mediaRule.cssRules
  mediaRule.deleteRule(0);
  mediaRule.deleteRule(0);
  
  // accessing this property causes jump to 0xfeeefeee
  mediaRule.cssRules.length;
  

If I had to guess, some memory backing `cssRules` is getting freed after the last `deleteRule` invocation and there is some vtable shenaniganry going on when accessing its length. But again, I don’t know, since I’m not going to do any reversing work. The fewer mitigations which exist, the less we need to understand about the bug to exploit it.

## Exploitation

The high level goal is clear: spray NOP sled followed by shellcode, then reclaim the freed memory and write the address of our NOP sled.

In order to reclaim the freed memory, we need to allocate something around the same size as the freed chunk. For exploitation on modern browsers, things like Float32Arrays are a popular choice. Unfortunately, we’re working on an ancient browser that doesn’t have these features. Looking to see what the other exploits on ancient browsers do, I found that [str2hax](https://github.com/Fullmetal5/str2hax) creates canvases and resizes them to make precise allocations. This works great on the DSi as well. Filling in the RGBA pixels of the canvas gives us precise control over the memory.

The exploitation flow is as follows:

  1. Create a lot of canvases with a specific width and height = 1
  2. Do the `insertRule`/`deleteRule` bug to free `mediaRule.cssRules`
  3. Write the address of our NOP sled to all the canvases in the form of RGBA pixels. This will reclaim the freed memory because the drawing code will allocate the correct size chunk. The address of our NOP sled is found from the debugger and is relatively consistent thanks to no ASLR. This enables us to hard-code an address in our payload.
  4. Spray our NOP sleds and shellcode
  5. Evaluate `mediaRule.cssRules.length;` to jump to our NOP sled

This works on melonDS… sometimes! Let’s call the freed pointer `freed_ptr`. The memory it points to is what we reclaimed and wrote our NOP sled address to. It appears that around half the time, the browser will jump to `*freed_ptr`, which is good for us and consistent with what we observed under wine. The other half the time, it will jump to `**freed_ptr`, which tries to dereference a NOP instruction and jump there. That crashes of course. But this is an easy fix! The address of our NOP sled is “NOP enough” when treated as an instruction. This means we can use _the address of our NOP sled as the NOP instruction itself_ , which satisfies both of the cases.

## Payload

Now that we have an exploit that works somewhat reliably, we need to choose useful shellcode. Looking to other DSi exploits, it’s common to use [minitwlpayload](https://github.com/yellows8/dsi/tree/master/exploits/minitwlpayload) which loads boot.nds from the SD card and executes it. This is often something like [TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu). Putting all the pieces together, we can celebrate with a fully working exploit on real hardware.

## Thanks

  * [melonds](https://github.com/melonDS-emu/melonDS) developers for writing such an accurate DSi emulator, including wifi capability
  * [PoroCYon](https://github.com/PoroCYon) for writing a [gdbstub for melonds](https://github.com/melonDS-emu/melonDS/pull/1583), which was critical for debugging the exploit
  * [shutterbug2000](https://gbatemp.net/threads/memory-pit-a-new-dsi-exploit-for-dsi-camera.539432/) and [zoogie](https://gbatemp.net/threads/memory-pit-a-new-dsi-exploit-for-dsi-camera.539432/page-18) for memory pit source
  * [yellows8](https://github.com/yellows8) for [reference material](https://github.com/yellows8/dsi) and debugging help
  * Martin Korth and others for [these amazing docs](https://problemkaputt.de/gbatek.htm)
  * [Fullmetal5](https://github.com/Fullmetal5) for str2hax canvas idea
  * Many others

## TL;DR

  1. The DSi uses Opera 9.50, so Google for existing Opera 9.50 exploits and try them. No luck on melonDS emulator.
  2. Send the browser all of WebKit’s layout tests. No luck on melonDS.
  3. Find Opera 9.50 Windows build and run under wine
  4. Enable wine heap debugging with `WINEDEBUG=warn+heap WINEPREFIX=$HOME/.wine32 WINEARCH=win32 winedbg --gdb opera.exe` to catch use-after-frees
  5. Try WebKit layout tests again under wine
  6. Find a use-after-free, play around with corrupted objects, get it to jump to an address we could possibly control
  7. Reclaim freed memory using canvas trick from [str2hax](https://github.com/Fullmetal5/str2hax)
  8. Develop full exploit on melonDS emulator
  9. Verify exploit on real hardware

[](/2023/03/02/hacking-the-nintendo-dsi-browser.html)
